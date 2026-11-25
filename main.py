"""One-Line Office Jokes — make.fun entry writer (stdlib only).

Writes the single-line entry to /output/entry.txt and verifies it.
"""

import os
import sys

ENTRY = "The water cooler bottle has been empty since Tuesday and everyone just walks past it \u2014 it's the longest-running team project in this office."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read back and verify byte-identical, gate-compliant output.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == ENTRY.encode("utf-8"), "entry.txt is not byte-identical to ENTRY"
    assert 1 <= len(ENTRY) <= 199, "entry must be 1-199 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip() != "", "entry must not be only whitespace"
    assert not ENTRY.endswith("\n"), "entry must not end with a newline"
    print("Wrote %d characters to %s" % (len(ENTRY), OUTPUT_PATH))
    print("Verified: byte-identical, single line, %d chars" % len(ENTRY))
    return 0


if __name__ == "__main__":
    sys.exit(main())
