#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Writes a two-line warning to one's past self to /output/entry.txt.
Line one warns about one specific moment (a brother's Perth job, announced
at a barbecue); line two traces what changed because of it. Deterministic:
the same bytes on every run.
"""

LINE_ONE = "When your brother says 'I got the job in Perth' at the barbecue, don't joke that he'll be back by Christmas."
LINE_TWO = "He won't be, and that joke is the last thing he hears from you for two years."

ENTRY = LINE_ONE + "\n" + LINE_TWO


def main() -> None:
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    import os

    os.chmod(path, 0o644)
    # Read-back guard: the file on disk must be byte-identical to the
    # validated entry — exactly two lines, 1 to 280 characters, no trailing
    # newline, line one a warning about one specific moment, line two the
    # reason it mattered.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry mismatch"
    assert 1 <= len(written) <= 280, "entry length out of range"
    lines = written.split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() for line in lines), "blank line in entry"
    assert written == written.strip(), "entry has leading/trailing whitespace"


if __name__ == "__main__":
    main()
