"""Say What Actually Broke — make.fun entry.

Writes one line of honest error copy to entry.txt: the database
row is gone because somebody ran DELETE without WHERE, and the
only backup is from last Tuesday.
"""

import os

LINE = (
    "Someone typed DELETE without WHERE and wiped your row. "
    "The backup is from last Tuesday — we have apologised to it as well."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
