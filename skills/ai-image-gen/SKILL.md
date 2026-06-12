---
name: generate-image
description: Generate images using AI (OpenAI GPT Image or Stability AI). Use when the user asks to generate an image, create an AI image, make an illustration, or produce artwork from a text prompt.
argument-hint: [prompt description]
allowed-tools: Bash(*), Read, Write
---

# AI Image Generation

Generate images from text prompts using OpenAI GPT Image (gpt-image-2 / gpt-image-1 / variants) or Stability AI (SD 3.5 Large).

## Tool Location

- Script: `~/.agents/tools/generate-image.py`
- Env file: `~/.agents/tools/.env` (contains `OPENAI_API_KEY` and `STABILITY_API_KEY`)

## Available OpenAI image models (verified live via `/v1/models` 2026-05-15)

| Model ID | Notes |
|---|---|
| `gpt-image-2` | **Flagship.** Released 2026-04-21. Best prompt adherence, best photorealism. Default when image quality matters. |
| `gpt-image-2-2026-04-21` | Pinned dated variant of gpt-image-2 |
| `gpt-image-1.5` | Intermediate release between 1 and 2 |
| `gpt-image-1-mini` | Smaller/cheaper gpt-image-1 variant — use for batch/draft generation where cost matters |
| `gpt-image-1` | Original gpt-image. Still works; superseded by gpt-image-2. |
| `chatgpt-image-latest` | Always-current alias of the model ChatGPT.com uses (currently gpt-image-2-class). Use when you want "whatever ChatGPT uses today" |
| `dall-e-3` | Legacy fallback. Different quality semantics (standard/hd, not low/medium/high). |

Pass any of these to `--model`. The script branches on `gpt-image*` for the quality/format handling, so all gpt-image-* variants work out of the box.

**Default in the script is now `gpt-image-2`** (the flagship) — pass `--model gpt-image-1-mini` for cheap batch/draft work.

## Quick Usage

### Generate with OpenAI gpt-image-2 (flagship)

```bash
python ~/.agents/tools/generate-image.py \
  --prompt "a sunset over mountains, oil painting style" \
  --output ./sunset.png \
  --model gpt-image-2 \
  --quality high
```

### Generate with default (gpt-image-2)

```bash
python ~/.agents/tools/generate-image.py \
  --prompt "a sunset over mountains, oil painting style" \
  --output ./sunset.png
```

### High quality

```bash
python ~/.agents/tools/generate-image.py \
  --prompt "modern logo design for a tech company" \
  --output ./logo.png \
  --size 1024x1024 \
  --quality high
```

### Wide format (good for blog covers, banners)

```bash
python ~/.agents/tools/generate-image.py \
  --prompt "abstract digital art with blue tones" \
  --output ./banner.png \
  --size 1536x1024
```

### Tall format (good for mobile, stories)

```bash
python ~/.agents/tools/generate-image.py \
  --prompt "portrait of a futuristic city" \
  --output ./city.png \
  --size 1024x1536
```

### Transparent background (icons, logos)

```bash
python ~/.agents/tools/generate-image.py \
  --prompt "a minimalist cat icon, flat design" \
  --output ./icon.png \
  --background transparent
```

### Generate with Stability AI (SD 3.5 Large)

```bash
python ~/.agents/tools/generate-image.py \
  --prompt "watercolor painting of a garden" \
  --output ./garden.png \
  --provider stability
```

## CLI Options

| Option | Description |
|--------|-------------|
| `--prompt, -p` | **(Required)** Text prompt describing the desired image |
| `--output, -o` | **(Required)** Output file path |
| `--provider` | `openai` (default) or `stability` |
| `--size` | Image size for OpenAI: `1024x1024` (default), `1536x1024` (wide), `1024x1536` (tall) |
| `--quality` | OpenAI quality: `low`, `medium` (default), or `high` |
| `--background` | OpenAI background: `auto` (default), `transparent`, or `opaque` |
| `--model` | Override model (default: `gpt-image-2` for OpenAI, `sd3.5-large` for Stability) |

## Provider Comparison

| Feature | OpenAI gpt-image-2 | OpenAI gpt-image-1 | Stability AI SD 3.5 |
|---------|--------------------|--------------------|---------------------|
| Released | 2026-04-21 | 2025 | — |
| Prompt adherence | Best | Excellent | Good |
| Size options | 1024x1024, 1536x1024, 1024x1536 | 1024x1024, 1536x1024, 1024x1536 | 1024x1024 |
| Quality options | low, medium, high | low, medium, high | N/A |
| Transparent bg | Yes | Yes | No |
| Style | Photorealistic + artistic | Photorealistic + artistic | Artistic + photorealistic |
| Cost per image (high) | Higher than 1 | Baseline | N/A |

## Dependencies

- `requests` (for API calls)

Install if needed:
```bash
pip install requests
```

## Output

The script prints:
- The provider and model used
- The prompt (and revised prompt if applicable)
- The saved file path
