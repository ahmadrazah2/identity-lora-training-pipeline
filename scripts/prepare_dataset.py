#!/usr/bin/env python3
"""Resize a folder of images to a shared pixel budget without cropping.

The original aspect ratio is preserved. Each output dimension is rounded to a
multiple of 32 so that the images work cleanly with aspect-ratio bucketing.
Original files are never modified.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image


SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def snapped_size(
    width: int,
    height: int,
    pixel_side: int,
    max_side: int,
    multiple: int,
) -> tuple[int, int]:
    """Return a same-ratio size near pixel_side squared, with no cropping."""
    ratio = width / height
    target_width = math.sqrt(pixel_side * pixel_side * ratio)
    target_height = target_width / ratio
    scale = min(max_side / max(target_width, target_height), 1.0)

    def snap(value: float) -> int:
        return max(multiple, round(value * scale / multiple) * multiple)

    return snap(target_width), snap(target_height)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Folder containing source images")
    parser.add_argument("destination", type=Path, help="New output folder")
    parser.add_argument("--prefix", default="subject_01", help="Output filename prefix")
    parser.add_argument("--pixel-side", type=int, default=1024)
    parser.add_argument("--max-side", type=int, default=1536)
    parser.add_argument("--multiple", type=int, default=32)
    parser.add_argument("--quality", type=int, default=95)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.source.is_dir():
        raise SystemExit(f"Source folder does not exist: {args.source}")
    if args.destination.exists() and any(args.destination.iterdir()):
        raise SystemExit(
            f"Destination is not empty; refusing to overwrite: {args.destination}"
        )

    args.destination.mkdir(parents=True, exist_ok=True)
    sources = sorted(
        path
        for path in args.source.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    )
    if not sources:
        raise SystemExit(f"No supported images found in: {args.source}")

    rows: list[tuple[str, str, str, str]] = []
    for index, source in enumerate(sources, start=1):
        with Image.open(source) as image:
            image = image.convert("RGB")
            width, height = image.size
            new_width, new_height = snapped_size(
                width,
                height,
                args.pixel_side,
                args.max_side,
                args.multiple,
            )
            output_name = f"{args.prefix}_{index:03d}.jpg"
            image.resize(
                (new_width, new_height), Image.Resampling.LANCZOS
            ).save(args.destination / output_name, "JPEG", quality=args.quality)
            rows.append(
                (
                    output_name,
                    source.name,
                    f"{width}x{height}",
                    f"{new_width}x{new_height}",
                )
            )

    source_map = args.destination / "_source_map.tsv"
    with source_map.open("w", encoding="utf-8") as handle:
        handle.write("new_name\toriginal_name\toriginal_size\tnew_size\n")
        for row in rows:
            handle.write("\t".join(row) + "\n")

    print(f"Wrote {len(rows)} images to {args.destination}")
    print(f"Source map: {source_map}")


if __name__ == "__main__":
    main()
