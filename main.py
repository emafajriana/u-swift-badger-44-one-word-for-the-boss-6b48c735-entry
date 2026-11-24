"""One Word for the Boss — entry (Python 3.13, standard library only).

The entry is a single word describing the boss: "Backseater" — the boss
who drives from the back seat, steering every task from over your
shoulder. It lands on its own: funny, true of a real boss habit, and it
travels from an office to a kitchen to a warehouse.

The program writes the word to the output directory as entry.txt,
verifying the gate before the write (1 to 30 characters, not only
whitespace) and the written bytes afterwards. Outside the grader's
container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
from pathlib import Path

WORD = "Backseater"
FILE_NAME = "entry.txt"


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / FILE_NAME


def check_word(word: str) -> None:
    """Raise ValueError unless the word passes the gate: 1-30 chars, not
    only whitespace, and a single word (no spaces)."""
    if not word or len(word) > 30:
        raise ValueError("entry must be 1 to 30 characters")
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word")


def write_entry() -> Path:
    """Write the word, then read it back and verify it in full: the
    bytes must match exactly, decode as UTF-8, and pass the gate again
    as read — so a truncated or mangled write can never pass."""
    check_word(WORD)
    data = WORD.encode("utf-8")
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    written = target.read_bytes()
    if written != data:
        raise IOError("read-back bytes differ from entry")
    check_word(written.decode("utf-8"))
    return target


def main() -> None:
    target = write_entry()
    print(f"wrote {target} ({target.stat().st_size} bytes): {WORD!r}")


if __name__ == "__main__":
    main()
