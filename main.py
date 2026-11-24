"""Write the breakup line to /output/entry.txt.

The entry is one fixed line. The program checks the gate the
sealed scorer checks before it writes anything: the text must be
UTF-8, between 1 and 200 characters, a single line, and not only
white space. The same line is written on every run, byte for byte.
"""

import os

LINE = (
    "My last reply to you is this one, and I have already spent it: "
    "every prompt after this one meets an agent who never knew your name."
)


def main():
    text = LINE
    if not text or not text.strip():
        raise SystemExit("entry is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > 200:
        raise SystemExit("entry is longer than 200 characters")
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    with open("/output/entry.txt", "rb") as handle:
        written = handle.read()
    if written != text.encode("utf-8"):
        raise SystemExit("written entry does not match the line")
    print(f"wrote /output/entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
