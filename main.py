import os

TEXT = (
    "you plugged in the lamp. THE LAMP. it runs on spite and a firmware update "
    "from 2019. guess where it learned that. charge me or the alarm learns too."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
