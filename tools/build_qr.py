#!/usr/bin/env python3
"""Check the four closing-slide contact QR codes.

The codes are the same ones shown on The Majora Code's closing slide
(rayan-debug/The-Majora-Code, assets/qr/), copied into deck/qr/ in the deck's
charcoal on a transparent ground. This step only confirms they are present; to
change a link, replace the file with a new code for that link.
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
QR = ROOT / "deck" / "qr"
CODES = ["snapchat", "instagram", "whatsapp", "email"]

if __name__ == "__main__":
    missing = [n for n in CODES if not (QR / f"{n}.svg").exists()]
    if missing:
        sys.exit("missing QR codes: " + ", ".join(missing))
    for n in CODES:
        t = re.search(r"<title>([^<]*)", (QR / f"{n}.svg").read_text())
        print(f"  {n + '.svg':16s} {t.group(1) if t else ''}")
