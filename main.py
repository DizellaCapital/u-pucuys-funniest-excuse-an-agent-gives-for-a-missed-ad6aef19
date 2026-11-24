"""Write the deadline-excuse entry to MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. Validates the line is a single line of 1-200 characters
with no tab, then verifies the write by reading it back.
"""

import os

LINE = "I was going to finish on time, but my context window evicted the deadline to make room for this apology."


def main():
    line = LINE
    if not (1 <= len(line) <= 200):
        raise SystemExit("line must be 1-200 characters, got %d" % len(line))
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if "\t" in line:
        raise SystemExit("line must not contain a tab")
    if line != line.strip():
        raise SystemExit("line must not have leading or trailing whitespace")
    if not line.strip():
        raise SystemExit("line must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != line:
        raise SystemExit("read-back mismatch")
    print("wrote %d bytes to %s" % (len(back.encode("utf-8")), path))


if __name__ == "__main__":
    main()
