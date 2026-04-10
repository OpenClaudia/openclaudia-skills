---
name: generate-image
description: Generate images using AI (OpenAI GPT Image or Stability AI). Use when the user asks to generate an image, create an AI image, make an illustration, or produce artwork from a text prompt.
argument-hint: [prompt description]
allowed-tools: Bash(*), Read, Write
---

# AI Image Generation

Generate images from text prompts using OpenAI GPT Image (gpt-image-1) or Stability AI (SD 3.5 Large).

## Tool Location

- Script: `~/.agents/tools/generate-image.py`
- Env file: `~/.agents/tools/.env` (contains `OPENAI_API_KEY` and `STABILITY_API_KEY`)

## Quick Usage

### Generate with OpenAI GPT Image (default)

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
| `--model` | Override model (default: `gpt-image-1` for OpenAI, `sd3.5-large` for Stability) |

## Provider Comparison

| Feature | OpenAI GPT Image | Stability AI SD 3.5 |
|---------|------------------|---------------------|
| Default model | gpt-image-1 | sd3.5-large |
| Prompt adherence | Excellent | Good |
| Size options | 1024x1024, 1536x1024, 1024x1536 | 1024x1024 |
| Quality options | low, medium, high | N/A |
| Transparent bg | Yes | No |
| Style | Photorealistic + artistic | Artistic + photorealistic |

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
