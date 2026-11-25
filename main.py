"""One Line, One Laugh entry.

Writes a single funny line to entry.txt in the output directory.
The grader reads /output/entry.txt; MAKEFUN_OUTPUT_DIR overrides
the directory when the harness sets it.
"""

import os

LINE = "My doctor told me to cut back on screen time, so now I watch my phone in the mirror and call it self-reflection."

# Gate self-check: the entry must be 1 to 140 characters, one line.
assert 1 <= len(LINE) <= 140, "entry line outside the 1-140 character gate"
assert "\n" not in LINE, "entry must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
