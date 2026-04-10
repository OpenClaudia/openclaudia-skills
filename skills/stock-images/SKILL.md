---
name: unsplash-image
description: Search for images on Unsplash and download them. Optionally add text overlay (title/subtitle) to the image. Use when the user asks to find a stock photo, search for an image, get an Unsplash image, or download a photo with text.
argument-hint: [search query]
allowed-tools: Bash(*), Read, Write
---

# Unsplash Image Search & Download

Search Unsplash for images, download them, and optionally add text overlay.

## Tool Location

- Script: `~/.agents/tools/unsplash-search.py`
- Env file: `~/.agents/tools/.env` (contains `UNSPLASH_CLIENT_ID`)

## Quick Usage

### Search and download a random matching image

```bash
python ~/.agents/tools/unsplash-search.py \
  --query "nature landscape" \
  --output ./image.jpg
```

### With orientation filter

```bash
python ~/.agents/tools/unsplash-search.py \
  --query "coffee shop" \
  --orientation landscape \
  --output ./coffee.jpg
```

### With text overlay (title and subtitle)

```bash
python ~/.agents/tools/unsplash-search.py \
  --query "technology abstract" \
  --output ./cover.png \
  --title "My Blog Post Title" \
  --subtitle "A short description"
```

### List results without downloading

```bash
python ~/.agents/tools/unsplash-search.py \
  --query "sunset" \
  --list
```

### Pick the first result instead of random

```bash
python ~/.agents/tools/unsplash-search.py \
  --query "mountains" \
  --pick first \
  --output ./mountains.jpg
```

## CLI Options

| Option | Description |
|--------|-------------|
| `--query, -q` | **(Required)** Search query string |
| `--output, -o` | **(Required unless --list)** Output file path |
| `--orientation` | Filter: `landscape`, `portrait`, or `squarish` |
| `--color` | Color filter (e.g., `blue`, `green`, `red`, `black_and_white`) |
| `--pick` | How to select from results: `random` (default) or `first` |
| `--title` | Title text to overlay on the image |
| `--subtitle` | Subtitle text to overlay (only used with --title) |
| `--list` | List search results instead of downloading |
| `--count` | Number of results to fetch, max 30 (default: 30) |

## Text Overlay

When `--title` is provided, the script adds a text overlay to the bottom portion of the image with:
- Semi-transparent dark background behind the text
- White title text with shadow
- Gray subtitle text (if provided)
- Automatic word wrapping and font sizing

**Requires Pillow**: `pip install Pillow`

## Dependencies

- `requests` (for API calls and image download)
- `Pillow` (only needed if using text overlay with `--title`)

Install if needed:
```bash
pip install requests Pillow
```

## Output

The script prints:
- The download URL
- Photographer attribution (required by Unsplash)
- The saved file path
- Confirmation of text overlay if applied

## Notes

- Unsplash API guidelines require attribution. The script prints photographer info.
- The script triggers Unsplash's download tracking endpoint as required by their API terms.
- Images are downloaded at "regular" quality (1080px width). For higher resolution, modify the script to use `urls.full` or `urls.raw`.
