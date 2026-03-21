#!/usr/bin/env python3
"""Generate remaining chapters + foreshadowing ledger."""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / ".env")

from api_client import call_model

_WRITER_SYSTEM = (
    "You are a novel architect continuing an outline. Write in the same format "
    "as the preceding chapters. Every chapter needs: POV, Location, Save the Cat beat, "
    "% mark, Emotional arc, Try-fail cycle, Beats, Plants, Payoffs, Character movement, "
    "The lie, Word count target."
)

def call_writer(prompt, max_tokens=16000):
    return call_model(prompt, system=_WRITER_SYSTEM, max_tokens=max_tokens)

part1 = open('/tmp/outline_output.md').read()
mystery = (BASE_DIR / "MYSTERY.md").read_text()

prompt = f"""Here is the first part of a chapter outline for a novel. The outline was cut off before
completion. Continue from where it left off, complete the remaining chapters through the end
of Act III, then write the Foreshadowing Ledger.

THE OUTLINE SO FAR:
{part1}

THE CENTRAL MYSTERY (for reference):
{mystery}

REMAINING STRUCTURE NEEDED:

Continue with the Save the Cat beats that haven't been covered yet. The remaining
chapters should include:
- Complete any chapter that was cut off mid-entry
- Dark Night of the Soul — protagonist processes what they've learned
- Break Into Three — new information or perspective changes everything
- Gathering forces / making a plan (1-2 chapters)
- The climax — protagonist answers the central question using the world's established systems
- Aftermath and resolution
- Final Image (mirror of Opening Image, showing transformation)

Then write:

## Foreshadowing Ledger

| # | Thread | Planted (Ch) | Reinforced (Ch) | Payoff (Ch) | Type |
|---|--------|-------------|-----------------|-------------|------|

Include at LEAST 15 threads. Types: object, dialogue, action, symbolic, structural.
Plant-to-payoff distance must be at least 3 chapters.

REMEMBER:
- The climax must use the world's established rules/systems to resolve
- The Stability Trap: not everything resolves cleanly
- The protagonist's lie must be fully shattered by the climax
- Final Image should mirror Ch 1's Opening Image but show transformation
- At least one quiet chapter in the back half
- All specifics (names, locations, plot beats) must come from the outline so far and the mystery doc
"""

print("Calling writer model...", file=sys.stderr)
result = call_writer(prompt)
print(result)
