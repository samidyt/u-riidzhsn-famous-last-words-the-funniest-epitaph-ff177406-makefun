"""Famous Last Words: The Funniest Epitaph — make.fun entry.

Writes a single one-line tombstone epitaph of famous last words to
/output/entry.txt (gate: UTF-8 text, 1-150 characters, not only whitespace).
"""

import os

# The line turns on one double meaning: "the last word" is both winning an
# argument and the literal final word of a dying person — and the word
# itself, "oops", is the punchline. First-person dying speech, one short
# line, no stage directions, quotable on one read.
EPITAPH = "I finally got the last word in. It was 'oops.'"


MAX_CHARS = 150


def validate(text: str) -> str:
    """Enforce the competition gate: 1-150 chars, one line, not blank."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("epitaph must not be blank")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("epitaph must be a single line")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"epitaph is {len(stripped)} chars, over the 150 limit")
    return stripped


def main() -> None:
    epitaph = validate(EPITAPH)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(epitaph)


if __name__ == "__main__":
    main()
