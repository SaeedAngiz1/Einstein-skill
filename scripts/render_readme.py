"""Render the editable SVG into GitHub-friendly motion and a static poster.

Optional authoring tools: Playwright and FFmpeg (not skill dependencies).
    python -m pip install playwright
    python -m playwright install chromium
    python scripts/render_readme.py

On Windows, an installed Edge can be used with --channel msedge.
Frames stay in ignored dist/readme-frames for inspection.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--channel", help="Optional Playwright browser channel, e.g. msedge")
    args = parser.parse_args()
    if shutil.which("ffmpeg") is None:
        raise SystemExit("FFmpeg must be available on PATH to encode the animation.")
    frames = ROOT / "dist" / "readme-frames"
    frames.mkdir(parents=True, exist_ok=True)
    fps, seconds = 12, 12
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True, channel=args.channel)
        page = browser.new_page(viewport={"width": 1280, "height": 640}, device_scale_factor=1)
        page.goto((ROOT / "assets" / "hero.svg").as_uri())
        page.evaluate("document.fonts.ready")
        page.evaluate("document.documentElement.pauseAnimations()")
        page.evaluate("document.documentElement.setCurrentTime(1.5)")
        page.screenshot(path=str(ROOT / "assets" / "social-preview.png"), omit_background=True)
        for frame in range(fps * seconds):
            page.evaluate("time => document.documentElement.setCurrentTime(time)", frame / fps)
            page.screenshot(path=str(frames / f"frame-{frame:04d}.png"), omit_background=True)
            if frame % 36 == 0:
                print(f"Rendered {frame}/{fps * seconds} frames", flush=True)
        browser.close()
    destination = ROOT / "assets" / "hero-animated.gif"
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-framerate", str(fps), "-i", str(frames / "frame-%04d.png"),
        "-frames:v", str(fps * seconds), "-filter_complex",
        "scale=1120:-2:flags=lanczos,split[a][b];[a]palettegen=max_colors=192:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle",
        "-loop", "0", str(destination)
    ], check=True)
    print(f"Saved {destination.name}: {destination.stat().st_size / 1024:.0f} KiB", flush=True)
    print("Saved social-preview.png at 1280 x 640", flush=True)


if __name__ == "__main__":
    main()
