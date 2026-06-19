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
5. **Re-cutting a finished episode** — Surgically remove flagged sections from an already-rendered episode without re-running the whole pipeline
6. **Highlight clips & reel** — Cut shareable soundbites and stitch a ~1-minute reel with music

## Prerequisites

- `ffmpeg` and `ffprobe` installed
- `OPENAI_API_KEY` in environment (for Whisper API transcription)
- Python 3 with stdlib only (no extra deps for the helper script)
- Optional: `resemblyzer` (`pip install resemblyzer`) — only for speaker diarization when building highlight reels

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

## Re-cutting an already-finished episode

When the user flags specific problems in a published episode ("a few sentences were left in", "cut the part about X", "the ending was re-recorded", "drop the duplicate intro"), **do NOT re-run the whole pipeline from raw.** Surgically cut the offending ranges out of the finished MP3 and re-encode once:

1. Re-transcribe the *final* file in 5-min chunks (segment granularity) → one unified transcript with absolute timestamps. This is your map.
2. For each flagged item, get **word-level** timestamps for just the chunk containing it (these phrases are usually embedded mid-sentence, not on segment boundaries). Pin tight in/out points.
3. Build one `atrim`+`concat` filter that keeps everything *except* the cut ranges; render to WAV (`pcm_s16le`) then a single MP3 pass. **Do not re-apply the enhancement chain** — the final is already enhanced/loudnorm'd; re-running it double-processes.
4. **Verify every splice**: extract an ~11s window centred on each new join (in the *new* timeline) and re-transcribe it. Confirm the bad audio is gone and the rejoin reads cleanly.
5. Recompute any show-notes timeline: every timestamp after a cut shifts earlier by the summed length of all cuts before it. If the published file prepends a highlight reel, also account for the reel's duration as an offset (a re-cut reel changes length, so the whole episode shifts).

### Re-cut checklist — what the first pass commonly leaves in
These survive filler/silence removal because they're blended into real sentences. Scan the transcript for them explicitly:
- **Meeting/tech chatter:** "you're muted / unmute", "你声音太小 / 听得到吗", "can you see my screen", "等一下我看一下". Cut the phrase, keep the surrounding content.
- **Dead-end topics:** the panel raises a product/case nobody researched, then says "我们就跳过吧 / let's skip it" — cut the whole detour, not just the skip line.
- **Re-recorded segments (esp. endings):** a messy first take, then a marker like "重新开始 / 从头来 / let's restart / feels redundant", then a clean re-take. Cut the false-start take, keep the re-record. Always inspect the last ~3 min for this.
- **Pre-show / duplicate intros:** a self-introduction recorded before the official start that gets repeated later — cut the pre-show copy.

### Whisper API flakiness
Parallel word-level calls sometimes return empty (0 bytes). Retry the empties **sequentially with a `sleep 1`** between calls.

## Highlight clips & 1-min reel

Cut short, shareable soundbites from a finished episode (controversial / insightful moments), and optionally stitch them into a ~1-minute reel with music.

### Picking soundbites
- Each clip ≈ **2 sentences, ~8–20s**. Favor lines that are controversial, surprising, or quotable.
- **COVER EVERY SPEAKER — including the host(s).** On a multi-guest panel, do not let the reel collapse onto the 1–2 most talkative voices — pick at least one strong soundbite per participant and check attribution before building. (This is the #1 mistake: a "highlight" that's secretly one person.) The **facilitator/host is the easiest to omit** because they mostly ask questions — find a quotable host line (a reaction, a joke, a sharp framing) and include it too.
- **You cannot attribute speakers from transcript text — do not try, and do not ask the user to do it for you.** Whisper gives you words, not who said them; guessing the speaker from phrasing fails (a line that *reads* like the host is often actually a guest). When the reel needs a specific person, **diarize the audio** (recipe below) and attribution becomes a measurement, not a guess.
- Order the reel for flow (hook → … → strong closer) and **never put the same speaker back-to-back**.

### Identify WHO is speaking — speaker diarization (`resemblyzer`)
When you need a specific person's clip (or the user says "X isn't in the reel"), resolve it by voice, not by reading the transcript. `pip install resemblyzer` (bundles its own encoder — no HF token). Recipe that worked on a 5-speaker panel:
1. **Build clean reference voices** for everyone you *can* identify, from segments where they say their own name (intros) or pitch their own product (closing plugs) — these are guaranteed single-speaker. Average 2–3 windows per person for stability: `enc.embed_utterance(preprocess_wav(slice, source_sr=16000))`, mean, L2-normalize.
2. **Don't blind-cluster** the whole episode — Whisper segments contain crosstalk, so `AgglomerativeClustering` collapses into one giant blob + singletons. Instead, score every segment's embedding (cosine) against your clean references. Segments that match **nobody** well (best sim ≲ 0.78 when real matches land 0.88–0.94) are the unidentified Nth speaker.
3. **Confirm it's one consistent voice**: take those low-match segments, check they're mutually similar (≳0.87) and collectively distinct from each known reference. Build a reference from them, re-score all segments — the high-confidence hits should all be that person.
4. **Sanity-check against a known**: a confirmed clip (e.g. someone's product pitch) must score highest to its own reference (≳0.9). If your references don't separate, lengthen the windows and average more.

Load the whole episode once as 16 kHz mono float via an ffmpeg pipe (`-f f32le -`) and slice in memory — far faster than one ffmpeg call per segment.

### Verify before you cut (mandatory)
For each candidate, extract the window and **re-transcribe it** to (a) confirm it's the right content/speaker and (b) find clean sentence boundaries. Whisper mangles names — never trust the first transcript's spelling. Use word-level granularity to pin a start that doesn't clip the first word and an end that drops stutters/repeats.

### Two gotchas that waste time
- **`-ss` / `-to` must be INPUT options (before `-i`).** As output options they produce silence or wrong ranges. `ffmpeg -ss START -to END -i in.mp3 ...`
- **zsh arrays are 1-indexed.** `for s in "${SEG[@]}"` (iterate values) — never `${SEG[$i]}` from `i=0`.
- If the episode was edited (intro/low-quality cut) **after** the master was made, source clips from the edited file with **shifted timestamps** (subtract the seconds removed before each cut point).

### Build one clip (pauses removed + tune in/out)
```bash
# 1) extract + remove pauses (collapse gaps >0.2s; gaps sit near -25dB after dynaudnorm, so threshold ~-23dB)
ffmpeg -y -ss START -to END -i FINAL.mp3 -ar 44100 -ac 1 \
  -af "silenceremove=start_periods=1:start_silence=0.04:start_threshold=-30dB:stop_periods=-1:stop_duration=0.20:stop_threshold=-23dB:detection=peak" sr.wav
# 2) speech fades (compute fade-out start from sr.wav duration)
ffmpeg -y -i sr.wav -af "afade=t=in:st=0:d=0.12,afade=t=out:st=${DUR-0.3}:d=0.3" f.wav
# 3) tune in -> speech -> tune out
ffmpeg -y -i sting_in.wav -i f.wav -i sting_out.wav \
  -filter_complex "[0][1]acrossfade=d=0.18:c1=tri:c2=tri[a];[a][2]acrossfade=d=0.18:c1=tri:c2=tri[out]" \
  -map "[out]" -c:a libmp3lame -b:a 192k clip.mp3
```

Synthesize the stings (no audio assets needed) — a soft bell chord, low volume:
```bash
# tune-in: bright C-E-G bell
ffmpeg -y -f lavfi -i "sine=f=523.25:d=0.85" -f lavfi -i "sine=f=659.25:d=0.85" -f lavfi -i "sine=f=783.99:d=0.85" \
  -filter_complex "[0][1][2]amix=inputs=3:normalize=1,afade=t=in:st=0:d=0.02,afade=t=out:st=0.2:d=0.65,lowpass=f=3800,volume=0.30[s]" -map "[s]" -ar 44100 -ac 1 sting_in.wav
# tune-out: lower, gentler G-C bell
ffmpeg -y -f lavfi -i "sine=f=392:d=0.75" -f lavfi -i "sine=f=523.25:d=0.75" \
  -filter_complex "[0][1]amix=inputs=2:normalize=1,afade=t=in:st=0:d=0.06,afade=t=out:st=0.15:d=0.6,lowpass=f=3200,volume=0.22[s]" -map "[s]" -ar 44100 -ac 1 sting_out.wav
```

### 1-min reel (concat + music bed + fade in/out)
Concat the pause-trimmed speech segments (1.5s silent lead/tail, ~0.35s gaps between) via the concat demuxer, then mix a soft synth pad **underneath** and fade the whole piece in/out. Don't reuse the per-clip stings inside the reel — one master fade is cleaner.

```bash
# music bed: warm 4-chord pad (C-G-Am-F), each chord 4s, lowpass+tremolo, concat -> pad16.wav, then loop
# (mkchord mixes 3 sines, normalize=1, lowpass=f=750, tremolo=f=4.5:d=0.25, afade in/out)
ffmpeg -y -i speech_reel.wav -stream_loop 6 -i pad16.wav \
  -filter_complex "[1]atrim=0:${TOT},volume=0.075[m];[0][m]amix=inputs=2:normalize=0:duration=first[mix];[mix]afade=t=in:st=0:d=1.3,afade=t=out:st=${TOT-1.6}:d=1.6[out]" \
  -map "[out]" -c:a libmp3lame -b:a 192k highlight.mp3
```

- Pad volume ~0.075 keeps speech fully dominant (verify by re-transcribing the final mix — every line should still read cleanly). `amix … normalize=0` so the voice isn't ducked.
- Target the same **−16 LUFS**; the music shouldn't push it past ~−16.5.

### Output layout
- Individual clips: `episodes/ep{NNN}/highlights/ep{NNN}-clip{N}-{who}.mp3`
- Single reel: `episodes/ep{NNN}/ep{NNN}-highlight.mp3`

## Cover art generation (optional)

Generate episode cover art with the OpenAI GPT Image API (`gpt-image-1`), matching your show's house style. Supply a **style reference image** of your own (a previous cover, your wordmark, your palette) — the model imitates it.

```python
import openai, base64

client = openai.OpenAI()  # uses OPENAI_API_KEY from env
style_img = open("YOUR_STYLE_REFERENCE.png", "rb")

result = client.images.edit(
    model="gpt-image-1",
    image=[style_img],                       # add a content reference as a 2nd image if you have one
    prompt="""Create an illustration in the EXACT same art style as this image
(match the line work, color palette, background, and decorative elements).
Depict: [DESCRIBE THE SCENE]. Keep [YOUR SHOW NAME / wordmark] in the same
style and position as the reference.""",
    size="1024x1024",
)
with open("cover.png", "wb") as f:
    f.write(base64.b64decode(result.data[0].b64_json))
```

Notes: load `OPENAI_API_KEY` from the environment, output a 1024×1024 PNG, and keep your show's wordmark/branding consistent across episodes.

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

**Heading rule:** keep headings shallow and consistent — pick one level (e.g. H2) and flatten all sub-sections to it. Some publishing platforms only render a single heading level plus **bold**; if yours does, match it.

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

## Archiving & naming conventions (recommended)

Keep each episode self-contained in its own folder. A simple, zero-padded layout scales cleanly:

```
episodes/
├── ep001/
│   ├── ep001-final.mp3      # the finished episode
│   ├── ep001-highlight.mp3  # optional 1-min reel
│   ├── cover.png
│   └── shownotes.md
└── ep002/
    └── ...
```

- Directory: `ep{NNN}` (zero-padded 3 digits)
- Audio: `ep{NNN}-final.mp3`; highlight clips under `ep{NNN}/highlights/ep{NNN}-clip{N}-{who}.mp3`
- Episode title: lead with a catchy, descriptive title (hook the reader, don't just state the topic).

## Quick trim (no filler removal)

If the user just wants a simple trim (e.g., "cut the first 3s"):

```bash
ffmpeg -y -i "INPUT" -ss 3 -c copy "OUTPUT"
```

Use `-c copy` for instant lossless trim when no audio processing is needed.
