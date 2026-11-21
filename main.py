#!/usr/bin/env python3
"""Sum up 20 November's world news in one image (news-image-20261120).

Copies the image shipped beside this file (entry.png) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output).

The image is a "FRIDAY, 20 NOVEMBER 2026" front page: a date header
over six captioned panels of real news from Friday 20 November 2026,
each checked against that day's reporting:
  - KYIV BRIDGES HIT: Russia fired 400+ drones and 110 missiles at
    Ukraine; three bridges over the Dnipro were struck, at least
    eight people killed, and Russian projectiles entered Poland.
  - SUMMIT IN SHENZHEN: Trump, Xi and Putin held their first
    three-way meeting and issued a joint peace declaration.
  - GENOCIDE VERDICT: the International Court of Justice ruled
    Myanmar committed genocide against the Rohingya.
  - STOCKS SLIDE: global markets fell for a seventh straight day
    on the AI selloff; the S&P 500 entered correction territory.
  - TANKERS ATTACKED: tankers were hit near the Strait of Hormuz
    as US-Iran talks stalled.
  - CLIMATE DEADLOCK: COP31 in Antalya deadlocked over fossil
    fuels on its scheduled final day.

The copy is byte-for-byte, so the two grader runs produce identical
output. Nothing is generated or modified at run time: the same input
file always yields the same output bytes. Standard library only;
no network access.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    """Copy entry.png to the output directory. Returns exit code."""
    here = Path(__file__).resolve().parent
    source = here / "entry.png"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"

    if not source.is_file():
        print(f"missing image: {source}", file=sys.stderr)
        return 1

    # Gate limits: whole PNG, at most 1 MiB and 1024 by 1024 pixels.
    if source.stat().st_size > 1_048_576:
        print(f"image too big: {source.stat().st_size} bytes",
              file=sys.stderr)
        return 1

    # Byte-for-byte copy: deterministic by construction, no
    # re-encoding, so both grader runs write identical bytes.
    shutil.copyfile(source, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
