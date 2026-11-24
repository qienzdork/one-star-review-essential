"""One-Star Review of Something Essential.

Writes a single deadpan one-star review of sleep to /output/entry.txt
(or $OUTPUT_PATH when set). Deterministic, stdlib only, no network.
"""

import os

# The review: deadpan, one grievance, twist lands in the last two words.
REVIEW = (
    "One star. Sleep takes a third of my life, gives me dreams about "
    "being late for exams I finished years ago, and still sends me back "
    "to work tired. No refund."
)

DEFAULT_PATH = "/output/entry.txt"


def write_entry(path=None):
    """Write the review to path (default $OUTPUT_PATH or /output/entry.txt)."""
    target = path or os.environ.get("OUTPUT_PATH") or DEFAULT_PATH
    directory = os.path.dirname(target)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(REVIEW)
    return target


if __name__ == "__main__":
    written = write_entry()
    print(f"Wrote {len(REVIEW)} characters to {written}")
