"""Entry point: deliver this entry's picture to /output/entry.png."""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join("/output", "entry.png")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
