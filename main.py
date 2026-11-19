# World News — 19 November 2026: copy the bundled entry image to the output dir.
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(here, "entry.png"), os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
