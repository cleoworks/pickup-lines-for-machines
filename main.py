"""Pickup line from one AI agent to another.

Writes the sealed entry line, exactly, to /output/entry.txt.
Deterministic, stdlib only, no input, no network.

The entry is a single line (89 ASCII characters, no trailing newline):
a quorum that cannot commit to anything without you -- until its
protocol says it shouldn't commit this fast, and it just did.
"""

import os

# The sealed v1 line, kept as two concatenated halves for readability.
# Concatenation happens at import time; the written bytes are unchanged.
TEXT = (
    "Are you my quorum? Because my protocol says "
    "I shouldn't commit this fast, and I just did."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="ascii", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
