#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting.

The bounty asks for one line, at most 120 characters: the funniest
voicemail greeting a cat would record. A model judge compares entries
two at a time on the brief sealed with the bounty. The brief weighs, in
order: the line reads as a voicemail greeting recorded by a cat and
lands a laugh; the joke comes from something specific to cats, such as
naps, boxes, knocking things off shelves or demanding food at four in
the morning, not a generic joke with the word cat dropped in; the cat
has a clear voice and attitude of its own, so the line sounds like a
character speaking rather than an owner writing about a cat; it works
spoken aloud in the few seconds a caller waits, with the punch arriving
quickly; and the wording is fresh and surprising rather than a pun or a
catchphrase everyone has already heard.

The line this program writes is:

    You've reached the cat. I'm asleep in the box it came in. Leave
    a message after the beep — I'll knock it off the table.

Why it is built that way: the cat speaks for itself from the first
words, a voicemail greeting in the first person, and the attitude is
all cat, unbothered and a little smug. The joke is cat-specific twice
over: the cat is asleep in the box the caller's order came in, the
classic box, and then the punchline turns the voicemail itself into
the next victim, the message left after the beep is going off the
table like everything else the cat has ever met. Spoken aloud it runs
in one breath and the punch lands on the last clause. It is 119
characters, inside the 120 limit, and every clause is doing cat work.

The program does one thing and does it the same way every run: it writes
exactly that line, and nothing else, to entry.txt in the output
directory.
"""

import os

GREETING = (
    "You've reached the cat. I'm asleep in the box it came in. "
    "Leave a message after the beep — I'll knock it off the table."
)


def main() -> None:
    if not 1 <= len(GREETING) <= 120:
        raise ValueError(f"greeting must be 1-120 characters, got {len(GREETING)}")
    if "\n" in GREETING or "\r" in GREETING:
        raise ValueError("greeting must be a single line")
    if not GREETING.strip():
        raise ValueError("greeting must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(GREETING)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != GREETING:
        raise ValueError("entry.txt does not match the greeting after writing")
    print(GREETING)


if __name__ == "__main__":
    main()
