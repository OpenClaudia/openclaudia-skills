---
name: stock-images
description: >
  Search Unsplash for stock photos and download them. Optionally add text overlay
  (title/subtitle). Use when asked to find a stock photo, search for an image,
  get an Unsplash image, or download a photo for a blog post, landing page, or social media.
---

# Stock Images from Unsplash

Search Unsplash for images, download them, and optionally add text overlay.

## Prerequisites

- **Unsplash API key** in `UNSPLASH_CLIENT_ID` environment variable (register at unsplash.com/developers)
- **Python 3** with `requests` and `Pillow` (for text overlay)

## Usage

### Search and Download

Write a Python script or use the Unsplash API directly:

```python
import os, requests, random

def search_unsplash(query, orientation=None, count=30):
    """Search Unsplash and return photo results."""
    params = {
        "query": query,
        "per_page": count,
        "client_id": os.environ["UNSPLASH_CLIENT_ID"],
    }
    if orientation:
        params["orientation"] = orientation  # landscape, portrait, squarish
    resp = requests.get("https://api.unsplash.com/search/photos", params=params)
    resp.raise_for_status()
    return resp.json()["results"]

def download_photo(photo, output_path):
    """Download a photo's regular-size image."""
    url = photo["urls"]["regular"]
    resp = requests.get(url)
    resp.raise_for_status()
    with open(output_path, "wb") as f:
        f.write(resp.content)
    # Unsplash requires attribution
    print(f"Photo by {photo['user']['name']} on Unsplash")

# Example: search and download a random matching photo
results = search_unsplash("nature landscape", orientation="landscape")
photo = random.choice(results)
download_photo(photo, "./image.jpg")
```

### With Text Overlay

```python
from PIL import Image, ImageDraw, ImageFont

def add_text_overlay(image_path, title, subtitle=None, output_path=None):
    """Add title/subtitle overlay to an image."""
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Semi-transparent overlay at bottom
    overlay_height = height // 4
    overlay = Image.new("RGBA", (width, overlay_height), (0, 0, 0, 128))
    img.paste(overlay, (0, height - overlay_height), overlay)

    # Title text
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    except OSError:
        font = ImageFont.load_default()
        small_font = font

    title_y = height - overlay_height + 20
    draw.text((40, title_y), title, fill="white", font=font)

    if subtitle:
        draw.text((40, title_y + 60), subtitle, fill=(200, 200, 200), font=small_font)

    out = output_path or image_path
    img.save(out)

add_text_overlay("./image.jpg", "My Blog Post Title", "A short description")
```

## CLI Options to Support

When building a script, support these options:

| Option | Description |
|--------|-------------|
| `--query` | Search query string (required) |
| `--output` | Output file path (required unless listing) |
| `--orientation` | Filter: `landscape`, `portrait`, or `squarish` |
| `--color` | Color filter (e.g., `blue`, `green`, `black_and_white`) |
| `--pick` | Selection mode: `random` (default) or `first` |
| `--title` | Title text to overlay on the image |
| `--subtitle` | Subtitle text (only used with --title) |
| `--list` | List results without downloading |

## Important Notes

- **Attribution required**: Unsplash requires crediting the photographer. Always include `Photo by {name} on Unsplash` in your output.
- **Rate limits**: 50 requests/hour for demo apps, 5000/hour for production apps.
- **Image sizes**: `raw` (original), `full` (high-res), `regular` (1080px wide), `small` (400px), `thumb` (200px).
