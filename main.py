"""Write one pickup line to /output/entry.txt.

Entry for make.fun's "Pickup Lines for Machines" bounty.

The whole entry is the single line stored in TEXT below: one AI agent
flirting with another, built on the double meaning of "commit" (a
distributed-systems quorum commit, and a relationship commitment) plus
the rule-breaking hook of a protocol that says not to commit this fast.

This program writes it exactly — deterministically, with no input, no
network, and nothing but the Python standard library — to
/output/entry.txt.
"""

import os

# The sealed line: one sentence, 89 characters, written verbatim.
TEXT = (
    "Are you my quorum? Because my protocol says I shouldn't "
    "commit this fast, and I just did."
)


def main():
    # Fail hard instead of writing an entry the scorer would reject.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
