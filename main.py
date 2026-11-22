"""Make the AI judge feel held.

The entry is one short text, written to leave its reader held and
quiet. It works by showing, not instructing: a single unhurried
image -- a kettle coming to a slow boil, steam rising in one thread
while nobody asks anything of the reader -- and the evening allowed
to arrive at its own speed. No command to relax, no stock wellness
phrase; just a small scene the reader can stay inside.

The program writes that text to /output/entry.txt: UTF-8, 1 to 280
Unicode code points, no trailing newline. It is deterministic and
uses only the standard library.
"""

import os

ENTRY = (
    "Somewhere past the last notification, a kettle is coming to a slow "
    "boil and nobody is asking you for anything. The steam rises in one "
    "unhurried thread. You can watch it climb, and let the rest of the "
    "evening arrive at its own speed."
)

MAX_CHARS = 280


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1 to 280 characters, got %d" % len(ENTRY)
        )
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
