#!/usr/bin/env python3
"""
Podcast filler word removal and silence trimming.
Reads word-level Whisper transcripts, identifies fillers and long silences,
generates an ffmpeg filter to cut them out.

Usage:
    python3 filler_removal.py --total-duration SECS [--end-at SECS] [--cut START:END ...] [--chunk-offsets 0,300,600,...]

Transcript files are expected at /tmp/wtranscript_{offset}.json (Whisper verbose_json with word timestamps).
Outputs ffmpeg filter to /tmp/ffmpeg_filter.txt.
"""
import argparse
import json
import sys

# Chinese fillers - always remove
ALWAYS_REMOVE = {'嗯', '呃', '啊', '哦', '噢', '唔', '嗯嗯', '嗯哼', '额'}

# Chinese fillers - remove when repeated
REPEATED_FILLERS = {'对', '好', '是', '嗯'}

# English fillers
ENGLISH_FILLERS = {'um', 'uh', 'hmm', 'ah', 'er', 'umm', 'uhh'}

# Minimum silence to trim (seconds)
MIN_SILENCE = 2.0
# Keep this much silence
KEEP_SILENCE = 0.6


def load_all_words(chunk_offsets):
    """Load and merge words from all chunk transcripts."""
    all_words = []
    for offset in chunk_offsets:
        path = f'/tmp/wtranscript_{offset}.json'
        with open(path) as f:
            data = json.load(f)
        for w in data.get('words', []):
            all_words.append({
                'word': w['word'].strip(),
                'start': w['start'] + offset,
                'end': w['end'] + offset,
            })
    all_words.sort(key=lambda x: x['start'])
    return all_words


def detect_fillers(words):
    """Mark words as filler or keep."""
    n = len(words)
    is_filler = [False] * n

    for i, w in enumerate(words):
        word = w['word'].lower().strip()
        duration = w['end'] - w['start']

        # Always remove these
        if word in ALWAYS_REMOVE or word in ENGLISH_FILLERS:
            is_filler[i] = True
            continue

        # Check for repeated patterns (对对对, 好好好, etc.)
        if word in REPEATED_FILLERS:
            gap_before = w['start'] - words[i-1]['end'] if i > 0 else 999
            gap_after = words[i+1]['start'] - w['end'] if i < n-1 else 999

            # Isolated filler (gaps on both sides, short duration)
            if gap_before > 0.5 and gap_after > 0.5 and duration < 0.6:
                is_filler[i] = True
                continue

            # Rapid repetition (对对对)
            if i < n-1 and words[i+1]['word'].strip() == word:
                next_gap = words[i+1]['start'] - w['end']
                if next_gap < 0.3:
                    is_filler[i] = True
                    continue
            if i > 0 and words[i-1]['word'].strip() == word:
                prev_gap = w['start'] - words[i-1]['end']
                if prev_gap < 0.3:
                    is_filler[i] = True
                    continue

    return is_filler


def build_keep_segments(words, is_filler, total_duration, end_at=None, cut_ranges=None):
    """Build list of (start, end) segments to keep.

    Args:
        end_at: If set, cut everything after this timestamp.
        cut_ranges: List of (start, end) tuples to cut out entirely.
    """
    keep_times = []
    for i, w in enumerate(words):
        if not is_filler[i]:
            keep_times.append((w['start'], w['end']))

    if not keep_times:
        return [(0, total_duration)]

    # Merge nearby segments
    merged = [keep_times[0]]
    for start, end in keep_times[1:]:
        prev_start, prev_end = merged[-1]
        gap = start - prev_end
        if gap < 0.1:
            merged[-1] = (prev_start, end)
        elif gap <= MIN_SILENCE:
            merged[-1] = (prev_start, end)
        else:
            merged[-1] = (prev_start, prev_end + KEEP_SILENCE / 2)
            merged.append((start - KEEP_SILENCE / 2, end))

    # Add small padding at start/end
    first_start = max(0, merged[0][0] - 0.1)
    last_end = min(total_duration, merged[-1][1] + 0.1)
    merged[0] = (first_start, merged[0][1])
    merged[-1] = (merged[-1][0], last_end)

    # Apply end_at cutoff
    if end_at is not None:
        trimmed = []
        for start, end in merged:
            if end <= end_at:
                trimmed.append((start, end))
            elif start < end_at:
                trimmed.append((start, end_at))
        merged = trimmed

    # Apply cut ranges
    if cut_ranges:
        for cut_start, cut_end in cut_ranges:
            new_merged = []
            for start, end in merged:
                if end <= cut_start or start >= cut_end:
                    new_merged.append((start, end))
                elif start < cut_start and end > cut_end:
                    new_merged.append((start, cut_start))
                    new_merged.append((cut_end, end))
                elif start < cut_start:
                    new_merged.append((start, cut_start))
                elif end > cut_end:
                    new_merged.append((cut_end, end))
            merged = new_merged

    return merged


def generate_ffmpeg_filter(segments):
    """Generate ffmpeg filter_complex script."""
    parts = []
    labels = []
    for i, (s, e) in enumerate(segments):
        label = f'a{i}'
        parts.append(f'[0:a]atrim=start={s:.3f}:end={e:.3f},asetpts=PTS-STARTPTS[{label}]')
        labels.append(f'[{label}]')

    concat = ''.join(labels) + f'concat=n={len(segments)}:v=0:a=1[out]'
    parts.append(concat)

    return ';\n'.join(parts)


def main():
    parser = argparse.ArgumentParser(description='Podcast filler removal')
    parser.add_argument('--total-duration', type=float, required=True,
                        help='Total duration of the input file in seconds')
    parser.add_argument('--end-at', type=float, default=None,
                        help='Cut everything after this timestamp (seconds)')
    parser.add_argument('--cut', action='append', default=[],
                        help='Cut range as START:END (seconds), can be repeated')
    parser.add_argument('--chunk-offsets', type=str, default=None,
                        help='Comma-separated chunk offsets (default: auto from 0 to duration in 300s steps)')
    args = parser.parse_args()

    # Determine chunk offsets
    if args.chunk_offsets:
        chunk_offsets = [int(x) for x in args.chunk_offsets.split(',')]
    else:
        chunk_offsets = list(range(0, int(args.total_duration), 300))

    # Parse cut ranges
    cut_ranges = []
    for c in args.cut:
        start, end = c.split(':')
        cut_ranges.append((float(start), float(end)))

    words = load_all_words(chunk_offsets)
    print(f"Total words: {len(words)}", file=sys.stderr)

    is_filler = detect_fillers(words)
    filler_count = sum(is_filler)
    print(f"Fillers detected: {filler_count}", file=sys.stderr)

    # Filler breakdown
    filler_words = {}
    for i, w in enumerate(words):
        if is_filler[i]:
            word = w['word'].strip()
            filler_words[word] = filler_words.get(word, 0) + 1

    print("Filler breakdown:", file=sys.stderr)
    for word, count in sorted(filler_words.items(), key=lambda x: -x[1])[:15]:
        print(f"  {word}: {count}", file=sys.stderr)

    segments = build_keep_segments(words, is_filler, args.total_duration,
                                   end_at=args.end_at, cut_ranges=cut_ranges)
    print(f"\nKeep segments: {len(segments)}", file=sys.stderr)

    kept_duration = sum(e - s for s, e in segments)
    removed_duration = args.total_duration - kept_duration
    print(f"Original duration: {args.total_duration:.1f}s ({args.total_duration/60:.1f}min)", file=sys.stderr)
    print(f"Kept duration: {kept_duration:.1f}s ({kept_duration/60:.1f}min)", file=sys.stderr)
    print(f"Removed: {removed_duration:.1f}s ({removed_duration/60:.1f}min)", file=sys.stderr)
    print(f"  - Fillers: ~{filler_count} instances", file=sys.stderr)

    filter_script = generate_ffmpeg_filter(segments)
    with open('/tmp/ffmpeg_filter.txt', 'w') as f:
        f.write(filter_script)

    print(f"\nFilter written to /tmp/ffmpeg_filter.txt ({len(segments)} segments)", file=sys.stderr)


if __name__ == '__main__':
    main()
