---
name: ai-image-gen
description: >
  Generate images from text prompts using OpenAI GPT Image (gpt-image-1) or Stability AI
  (SD 3.5 Large). Use when asked to generate an image, create AI art, make an illustration,
  design a logo, or produce artwork from a text description.
---

# AI Image Generation

Generate images from text prompts using OpenAI or Stability AI.

## Prerequisites

- **OpenAI API key** in `OPENAI_API_KEY` environment variable (for GPT Image)
- **Stability AI API key** in `STABILITY_API_KEY` environment variable (optional, for Stable Diffusion)
- **Python 3** with `requests` and `base64` (standard library)

## OpenAI GPT Image (Recommended)

```python
import os, requests, base64

def generate_image_openai(prompt, output_path, size="1024x1024", quality="auto", background="auto"):
    """Generate an image with OpenAI GPT Image (gpt-image-1)."""
    resp = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={
            "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
            "Content-Type": "application/json",
        },
        json={
            "model": "gpt-image-1",
            "prompt": prompt,
            "n": 1,
            "size": size,           # 1024x1024, 1536x1024 (wide), 1024x1536 (tall)
            "quality": quality,     # "auto", "low", "medium", "high"
            "background": background,  # "auto", "transparent", "opaque"
        },
    )
    resp.raise_for_status()
    img_b64 = resp.json()["data"][0]["b64_json"]
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(img_b64))
    print(f"Image saved to {output_path}")

# Examples
generate_image_openai("a sunset over mountains, oil painting style", "./sunset.png")
generate_image_openai("modern tech logo", "./logo.png", size="1024x1024", quality="high")
generate_image_openai("minimalist cat icon", "./icon.png", background="transparent")
```

### Size Options
| Size | Best for |
|------|----------|
| `1024x1024` | Square — logos, icons, social media |
| `1536x1024` | Wide — blog covers, banners, hero images |
| `1024x1536` | Tall — mobile, stories, Pinterest |

## Stability AI (Alternative)

```python
def generate_image_stability(prompt, output_path, aspect_ratio="1:1"):
    """Generate with Stability AI SD 3.5 Large."""
    resp = requests.post(
        "https://api.stability.ai/v2beta/stable-image/generate/sd3",
        headers={
            "Authorization": f"Bearer {os.environ['STABILITY_API_KEY']}",
            "Accept": "image/*",
        },
        files={"none": ""},
        data={
            "prompt": prompt,
            "model": "sd3.5-large",
            "aspect_ratio": aspect_ratio,  # 1:1, 16:9, 9:16, 3:2, 2:3
            "output_format": "png",
        },
    )
    resp.raise_for_status()
    with open(output_path, "wb") as f:
        f.write(resp.content)

generate_image_stability("watercolor painting of a garden", "./garden.png", aspect_ratio="16:9")
```

## When to Use Which Provider

| Provider | Strengths |
|----------|-----------|
| **OpenAI GPT Image** | Best overall quality, text rendering, transparent backgrounds, follows complex prompts |
| **Stability AI** | Good for artistic styles, faster, often cheaper, no content policy surprises |

## Tips

- **Be specific**: "a golden retriever sitting on a red couch in a cozy living room" > "a dog"
- **Specify style**: "oil painting", "flat vector", "3D render", "watercolor", "photorealistic"
- **For logos**: use `background: "transparent"` with OpenAI, or post-process with PIL
- **For blog covers**: use wide format (`1536x1024` or `16:9`)
- **Batch generation**: generate multiple variations and let the user pick the best one
