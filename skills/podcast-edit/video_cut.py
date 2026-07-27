#!/usr/bin/env python3
"""
Build an ffmpeg filter that applies the audio edit to VIDEO too.

Reads the keep-segments out of /tmp/ffmpeg_filter.txt (written by filler_removal.py)
and emits a trim+atrim+concat script that cuts picture and sound at the same points,
then runs the standard enhancement chain on the concatenated audio.

Usage:
    python3 filler_removal.py --total-duration ... --chunk-offsets ...   # first
    python3 video_cut.py /tmp/video_filter.txt
    ffmpeg -y -i SOURCE.mp4 -filter_complex_script /tmp/video_filter.txt \
      -map '[vout]' -map '[aout]' -c:v h264_videotoolbox -b:v 3500k \
      -c:a aac -b:a 160k -movflags +faststart OUT.mp4
"""
import re
import sys

ENHANCE = ("highpass=f=80,lowpass=f=12000,afftdn=nf=-25:nr=8:nt=w,"
           "equalizer=f=180:t=q:w=1.5:g=-2,equalizer=f=2500:t=q:w=1.2:g=3,"
           "equalizer=f=4500:t=q:w=1.5:g=1.5,dynaudnorm=f=200:g=5:p=0.95:m=5:s=0,"
           "acompressor=threshold=-20dB:ratio=2:attack=5:release=200:makeup=1,"
           "loudnorm=I=-16:TP=-1.5:LRA=13")


def build(audio_filter_path='/tmp/ffmpeg_filter.txt'):
    segs = [(float(a), float(b)) for a, b in
            re.findall(r'atrim=start=([\d.]+):end=([\d.]+)', open(audio_filter_path).read())]
    if not segs or any(b <= a for a, b in segs):
        raise SystemExit(f'no usable keep segments in {audio_filter_path}')
    lines = []
    for i, (a, b) in enumerate(segs):
        lines.append(f"[0:v]trim=start={a:.3f}:end={b:.3f},setpts=PTS-STARTPTS[v{i}];")
        lines.append(f"[0:a]atrim=start={a:.3f}:end={b:.3f},asetpts=PTS-STARTPTS[a{i}];")
    lines.append("".join(f"[v{i}][a{i}]" for i in range(len(segs)))
                 + f"concat=n={len(segs)}:v=1:a=1[vout][araw];")
    lines.append(f"[araw]{ENHANCE}[aout]")
    return "\n".join(lines), segs


def demo():
    import tempfile, os
    src = "[0:a]atrim=start=1.000:end=2.000,asetpts=PTS-STARTPTS[a0];\n" \
          "[0:a]atrim=start=5.000:end=9.500,asetpts=PTS-STARTPTS[a1];"
    with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False) as f:
        f.write(src)
        p = f.name
    out, segs = build(p)
    os.unlink(p)
    assert segs == [(1.0, 2.0), (5.0, 9.5)], segs
    assert "concat=n=2:v=1:a=1[vout][araw]" in out
    assert out.count("[0:v]trim=") == 2, "one video trim per keep segment"
    assert "[vout]" in out and "[aout]" in out
    print("ok")


if __name__ == '__main__':
    if '--demo' in sys.argv:
        demo()
    else:
        out, segs = build()
        dest = sys.argv[1] if len(sys.argv) > 1 else '/tmp/video_filter.txt'
        open(dest, 'w').write(out)
        kept = sum(b - a for a, b in segs)
        print(f'{len(segs)} segments, {kept/60:.1f} min kept -> {dest}', file=sys.stderr)
