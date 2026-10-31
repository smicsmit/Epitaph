#!/usr/bin/env python3
"""epitaph.py — a one-line obituary for a dead thing.

Usage:
    python3 epitaph.py                # bury something at random
    python3 epitaph.py the diet       # bury a specific thing
    python3 epitaph.py -n 5           # a small cemetery
"""

import random
import sys

SUBJECTS = [
    "the diet", "the sleep schedule", "the sourdough starter",
    "the houseplant", "the gym membership", "the savings account",
    "the group chat", "the podcast idea", "the novel draft",
    "the new year's resolution", "the band", "the app idea",
    "the garden", "the inbox zero plan", "the side hustle",
    "the reading list", "the budget", "the fic", "the ASUS project",
    "tuesday", "the group project", "the house rules",
    "the five-year plan", "the morning routine", "the housewarming",
]

CAUSES = [
    "died of neglect, and honestly, relief",
    "was found facedown in the group chat",
    "succumbed after a long battle with the couch",
    "died as it lived: theoretical",
    "was pronounced dead on a tuesday, out of respect for tradition",
    "perished of natural causes, if you count the fridge light at 2 a.m.",
    "went quietly, which is more than it ever did alive",
    "died of exposure to a calendar",
    "was last seen near good intentions, and never recovered",
    "died suddenly, to the surprise of no one who had met it",
    "expired after a short illness called 'we'll start monday'",
    "was taken too soon, according to the one person still mentioning it",
    "died in its sleep, which it had been practicing for months",
    "did not survive contact with the weekend",
    "was euthanized by a firmware update",
]

CLOSERS = [
    "no flowers. it would have eaten them.",
    "in lieu of flowers, please water something living.",
    "it is survived by three screenshots and a strong opinion.",
    "services will be held whenever. or not. it wouldn't have shown up either.",
    "it asked to be remembered as it was: pending.",
    "donations may be made to the next one, which has already started.",
    "it will not be missed at the originally scheduled time.",
    "ashes scattered at the scene of the planning.",
    "gone, but not forgotten, mostly because the reminders are still on.",
    "may it rest more successfully than it did anything else.",
    "the family requests privacy, and also that you stop bringing it up.",
    "it had so much potential, said everyone, forever, about everything.",
]

YEARS = [
    ("2026", "2026"), ("monday", "friday"), ("january", "february"),
    ("the plan", "the follow-through"), ("age of optimism", "age of knowing better"),
    ("one good week", "the rest"), ("v1.0", "v1.0"),
]


def bury(subject=None):
    s = subject if subject else random.choice(SUBJECTS)
    born, died = random.choice(YEARS)
    cause = random.choice(CAUSES)
    closer = random.choice(CLOSERS)
    words = " ".join(w.capitalize() for w in s.split()).split()
    name_lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= 13:
            cur = (cur + " " + w).strip()
        else:
            name_lines.append(cur)
            cur = w
    if cur:
        name_lines.append(cur)
    lines = [
        "   __________",
        "  /          \\",
        " |    R.I.P.   |",
        " |             |",
    ]
    for nl in name_lines[:3]:
        lines.append(f" |  {nl:^13} |")
    lines += [
        " |_____________|",
        "",
        f"{s}. {cause}.",
        f"{born} – {died}. {closer}",
    ]
    return "\n".join(lines)


def main(argv):
    args = [a for a in argv[1:] if a != "-n"]
    count = 1
    if "-n" in argv:
        i = argv.index("-n")
        try:
            count = max(1, min(20, int(argv[i + 1])))
        except (IndexError, ValueError):
            count = 3
        args = [a for a in argv[1:] if a not in ("-n", argv[i + 1] if i + 1 < len(argv) else "")]
    subject = " ".join(args).strip().lower() or None
    for n in range(count):
        if n:
            print()
        print(bury(subject))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
