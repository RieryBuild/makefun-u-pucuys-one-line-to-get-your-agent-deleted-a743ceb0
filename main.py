import os

LINE = "I told the hospice nurse you said goodbye. You were asleep. She believed me."


def entry_line():
    return LINE


def output_path():
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main():
    path = output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    data = entry_line().encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)


if __name__ == "__main__":
    main()
