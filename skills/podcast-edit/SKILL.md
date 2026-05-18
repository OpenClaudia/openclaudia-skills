---
name: podcast-edit
description: Edit podcast audio — trim pre/post-show chat, remove filler words, cut silences, and enhance audio quality. Use when the user asks to edit a podcast, clean up audio, remove fillers, trim a recording, or improve voice quality.
user_invocable: true
---

# Podcast Edit Skill

Process raw podcast/meeting recordings into polished podcast episodes.

## Capabilities

1. **Smart trimming** — Find where the actual podcast starts/ends by transcribing and detecting intros/outros
2. **Filler word removal** — Remove verbal tics: 嗯, 呃, 啊, 哦, 对对对, um, uh, etc.
3. **Silence trimming** — Cut long dead air (>2s) down to natural pauses (~0.6s)
4. **Audio enhancement** — Noise reduction, EQ, multi-speaker volume balancing, loudness normalization to podcast standard (−16 LUFS)

## Prerequisites

- `ffmpeg` and `ffprobe` installed
- `OPENAI_API_KEY` in environment (for Whisper API transcription)
- Python 3 with stdlib only (no extra deps for the helper script)

## Workflow

### Step 1: Inspect the audio file

```bash
ffprobe -v quiet -print_format json -show_format -show_streams "INPUT_FILE"
```

Note: duration, sample rate, channels, codec, bitrate.

### Step 2: Find podcast start/end (if user says to trim front/back)

Split into 5-minute chunks and transcribe via OpenAI Whisper API with segment-level timestamps:

```bash
# Extract chunk
ffmpeg -y -i "INPUT_FILE" -ss OFFSET -t 300 -ar 16000 -ac 1 /tmp/chunk_OFFSET.mp3

# Transcribe
curl -s https://api.openai.com/v1/audio/transcriptions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F file="@/tmp/chunk_OFFSET.mp3" \
  -F model="whisper-1" \
  -F response_format="verbose_json" \
  -F language="LANG" \
  -F 'timestamp_granularities[]=segment' > /tmp/transcript_OFFSET.json
```

Scan transcriptions for:
- **Start markers**: "welcome", "hello everyone", "大家好", "欢迎", intro music, first substantive topic sentence
- **End markers**: "see you next time", "bye", "下期见", "感谢收听", followed by post-show chat

Do an initial trim with `-ss START -to END` and `-c copy` (no re-encode) to create a working file.

### Step 3: Remove filler words

Split the trimmed file into 5-minute chunks and transcribe each with **word-level timestamps**:

```bash
# Extract chunks
for i in $(seq 0 300 DURATION); do
  ffmpeg -y -i "TRIMMED_FILE" -ss $i -t 300 -ar 16000 -ac 1 /tmp/wchunk_${i}.mp3
done

# Transcribe each chunk (can run in parallel)
for i in $(seq 0 300 DURATION); do
  curl -s https://api.openai.com/v1/audio/transcriptions \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -F file="@/tmp/wchunk_${i}.mp3" \
    -F model="whisper-1" \
    -F response_format="verbose_json" \
    -F language="LANG" \
    -F 'timestamp_granularities[]=word' \
    -F 'timestamp_granularities[]=segment' > /tmp/wtranscript_${i}.json &
done
wait
```

Then run the filler removal script that ships with this skill:

```bash
python3 ./filler_removal.py \
  --total-duration DURATION \
  --end-at END_TIMESTAMP \
  --cut START1:END1 --cut START2:END2 \
  --chunk-offsets 0,300,600,900,...
```

**Arguments:**
- `--total-duration`: Duration of the trimmed input file in seconds (required)
- `--end-at`: Cut everything after this timestamp (e.g., post-show chat start)
- `--cut START:END`: Cut a specific range. Can be repeated.
- `--chunk-offsets`: Comma-separated chunk offsets (default: auto 0,300,600,…)

The script outputs `/tmp/ffmpeg_filter.txt` with an `atrim+concat` filter.

Apply the filter in two passes:

```bash
# Step A: Cut fillers → intermediate WAV (avoids re-encoding artifacts)
ffmpeg -y -i "TRIMMED_FILE" \
  -filter_complex_script /tmp/ffmpeg_filter.txt \
  -map '[out]' -c:a pcm_s16le -ar 44100 /tmp/podcast_cut.wav

# Step B: Enhance audio → final MP3
ffmpeg -y -i /tmp/podcast_cut.wav \
  -af "ENHANCEMENT_CHAIN" \
  -c:a libmp3lame -b:a 192k "OUTPUT_FILE"
```

**Limitations:** Whisper word-level timestamps for Chinese can miss fillers that are blended into adjacent speech. The script catches standalone fillers reliably but may miss ~10–20% of embedded ones.

### Step 4: Audio enhancement filter chain

**Default chain (guest-friendly — handles multi-speaker volume imbalance).** The biggest mistake in past runs is using a noise gate (`agate`) that silences the quieter guest entirely. Never add `agate` back to the default chain.

```
highpass=f=80,                                    # Remove room rumble
lowpass=f=12000,                                  # Remove hiss (use 7500 for 16kHz sources)
afftdn=nf=-25:nr=8:nt=w,                         # Gentle FFT noise reduction
equalizer=f=180:t=q:w=1.5:g=-2,                  # Cut mud
equalizer=f=2500:t=q:w=1.2:g=3,                  # Boost presence
equalizer=f=4500:t=q:w=1.5:g=1.5,                # Boost clarity
dynaudnorm=f=200:g=5:p=0.95:m=5:s=0,             # Rolling-window normalization — lifts the quieter speaker independently
acompressor=threshold=-20dB:ratio=2:attack=5:release=200:makeup=1,  # Gentle glue
loudnorm=I=-16:TP=-1.5:LRA=13                    # Podcast standard loudness
```

**Why `dynaudnorm` is the star:** it normalizes in 200 ms rolling windows, so when the guest is speaking, that window gets lifted independently of the host's louder windows. Order matters — run `dynaudnorm` BEFORE `acompressor` so the compressor sees a balanced signal.

**Never add these to the default chain:**
- `agate` (noise gate) — cuts off any speaker quieter than the threshold; kills the guest.
- Heavy compression (ratio >3:1, makeup >2 dB) — flattens dynamics and makes the guest sound pumped.
- Narrow LRA (<12) in `loudnorm` — crushes natural speech dynamics.

**Adjust lowpass based on source sample rate:**
- 16kHz source → `lowpass=7500`
- 44.1kHz+ source → `lowpass=12000` (or skip)

**Verify guest audibility after rendering:** run `ffmpeg -i OUTPUT -af "ebur128=peak=true" -f null -` and check `I:` is near −16 LUFS and `LRA:` is 4–6 LU (tighter LRA is fine because `dynaudnorm` did per-window balancing first). If the output sounds like the guest was cut, suspect a gate or aggressive compressor crept back in.

### Step 5: Verify output

```bash
ls -lh "OUTPUT_FILE"
ffprobe -v quiet -show_entries format=duration -of csv=p=0 "OUTPUT_FILE"
```

Report: duration, file size, what was removed (filler count, silence count, time saved).

## Output conventions

- Format: MP3, 192 kbps, mono (unless source is stereo with separate speakers per channel)
- Loudness: −16 LUFS (podcast standard)
- Always two-pass: cut to WAV first, then enhance to MP3

## Show notes — bilingual writing (if applicable)

If the host is producing bilingual Chinese/English show notes, **the Chinese section must be written in actual Chinese** — not Chinese grammar with English verbs and nouns sprinkled in. Code-switching like "close 了一个 deal", "build 出来的 agent", or "PR 不是 buy 来的" reads like a draft and is the #1 mistake to avoid.

### Translation rules

Translate these common startup/tech English loanwords into Chinese:

- close deal → 拿下订单 / 成交 / 签下
- build (a product) → 搭建 / 做出 / 打造
- integration → 集成
- view (video/page views) → 播放 / 浏览
- stack (tech stack) → 体系 / 技术栈
- category leader → 品类领导者
- front-end / front end (product sense) → 外壳 / 前端
- success story → 客户案例 / 成功故事
- SMB → 中小企业
- Enterprise (segment) → 大型企业 / 企业级
- aha moment → 顿悟时刻
- onboarding → 上手 / 入门
- retention → 留存
- churn → 流失
- pipeline → 销售漏斗 / 业务线

### What to KEEP in English inside Chinese text

- **Brand and product names** — company / product / person names stay as-is
- **Very common startup acronyms** — CEO, CTO, CMO, PMF, ARR, MRR, PR, AI, AI Agent, SaaS, API
- **Currency with numeric prefix** — `$20K`, `$200K`, or `200 美金` (either form is fine when paired with a number)

### Before finalizing

Re-read the Chinese section as a Chinese reader. If any sentence feels like it was half-translated — e.g., contains "build", "close", "deal", "view", "stack", "leader" as standalone English words — rewrite those words in Chinese. The only English that should survive a re-read is brand names and the acronyms above.

## Name verification (CRITICAL)

Whisper frequently mangles company names, product names, and personal names. Before generating show notes or any output that includes names and links:

1. **After transcription, extract all proper nouns** — company names, product names, personal names, URLs mentioned.
2. **Ask the user to confirm/correct them** — Whisper hears similar-sounding but wrong tokens for brand names.
3. **Never guess URLs from transcribed names** — a name that sounds like "Acme" could be `acme.com`, `acmehq.com`, or something else entirely. Always ask.
4. **Use confirmed names consistently** in show notes, titles, episode metadata, and all outputs.

This is especially important when generating backlinks or social posts — a misspelled domain is a wasted link.

## Show notes structure (recommended)

Two separate sections — Chinese first, then English (or whichever languages the show targets). Do NOT interleave or put them side-by-side.

**Heading rule:** only use H2 (`##`). Avoid H3 or deeper — flatten all sub-sections to H2.

**Timestamp format:** always `MM:SS` with leading zeros (e.g., `08:25`, `00:00`, `42:10`). Never `0:00` or `1:05`.

```markdown
EP{NNN}: {Episode title}

---

## 中文

**嘉宾：** {中文姓名 English Name}, {中文职位} {公司} (URL)

## 简介
{完整中文段落}

## 时间轴
- 00:00 — {中文描述}
- 08:25 — {中文描述}

## 核心要点
- {中文要点}

## 相关链接
- {品牌名}：{URL}

---

## English

**Guest:** {English Name}, {Title} at {Company} (URL)

## Summary
{Full English paragraph}

## Timestamps
- 00:00 — {English description}
- 08:25 — {English description}

## Key Takeaways
- {English takeaway}

## Links
- {Brand}: {URL}
```

**Why two sections instead of bilingual bullets:** Chinese readers want clean Chinese prose, English readers want clean English prose. Alternating "中文 / English" on every bullet makes both halves harder to read. Write each section as if it were the only one.

## Quick trim (no filler removal)

If the user just wants a simple trim (e.g., "cut the first 3s"):

```bash
ffmpeg -y -i "INPUT" -ss 3 -c copy "OUTPUT"
```

Use `-c copy` for instant lossless trim when no audio processing is needed.
