#!/usr/bin/env python3
"""
One-shot characters.md generator for foundation phase.
Reads seed.txt + voice.md + world.md + CRAFT.md, calls writer model.
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / ".env")

from api_client import call_model

_WRITER_SYSTEM = (
    "You are a character designer for literary fiction with deep knowledge of "
    "wound/want/need/lie frameworks, Sanderson's three sliders, and dialogue "
    "distinctiveness. You create characters who feel like real people with "
    "contradictions, secrets, and speech patterns you can hear. "
    "You never use AI slop words. You write in clean, direct prose."
)

def call_writer(prompt, max_tokens=16000):
    return call_model(prompt, system=_WRITER_SYSTEM, max_tokens=max_tokens)

seed = (BASE_DIR / "seed.txt").read_text()
world = (BASE_DIR / "world.md").read_text()

# Voice Part 2 only
voice = (BASE_DIR / "voice.md").read_text()
voice_lines = voice.split('\n')
part2_start = next(i for i, l in enumerate(voice_lines) if 'Part 2' in l)
voice_part2 = '\n'.join(voice_lines[part2_start:])

prompt = f"""Build a complete character registry for this fantasy novel. This is CHARACTERS.MD --
the definitive reference for WHO exists in this story, what drives them, how they speak,
and what secrets they carry.

SEED CONCEPT:
{seed}

WORLD BIBLE (the world these characters inhabit):
{world}

VOICE IDENTITY (the novel's tone):
{voice_part2}

CHARACTER CRAFT REQUIREMENTS (from CRAFT.md):

### The Three Sliders (Sanderson)
Every character has three independent dials (0-10):
  PROACTIVITY -- Do they drive the plot or react to it?
  LIKABILITY  -- Does the reader empathize with them?
  COMPETENCE  -- Are they good at what they do?
Rule: compelling = HIGH on at least TWO, or HIGH on one with clear growth.

### Wound / Want / Need / Lie Framework
A causal chain:
  GHOST (backstory event) -> WOUND (ongoing damage) -> LIE (false belief to cope)
    -> WANT (external goal driven by Lie) -> NEED (internal truth, opposes Lie)
Rules: Want and Need must be IN TENSION. Lie statable in one sentence.
  Truth is its direct opposite.

### Dialogue Distinctiveness (8 dimensions)
1. Vocabulary level  2. Sentence length  3. Contractions/formality
4. Verbal tics  5. Question vs statement ratio  6. Interruption patterns
7. Metaphor domain  8. Directness vs indirectness
Test: Remove dialogue tags. Can you tell who's speaking?

BUILD THE REGISTRY WITH AT LEAST THESE ARCHETYPES (derive names, details, and
specifics from the seed and world above):

1. **Protagonist** (POV character)
   - Full wound/want/need/lie chain
   - Three sliders with justification
   - Arc type (positive/negative/flat)
   - Detailed speech pattern (8 dimensions)
   - Physical habits and tells
   - At least 2 secrets
   - Key relationships mapped

2. **Key family members or close relationships** (1-2 characters)
   - Same depth as protagonist
   - What they know and what they're hiding
   - Their relationship to the central conflict

3. **Antagonist** (primary opposition)
   - Not a villain -- someone whose interests conflict with the protagonist's
   - Their own wound/want/need/lie (they should be understandable)
   - As fully realized as the protagonist

4. **Institutional/systemic antagonist** (optional, if the world supports it)
   - The system personified
   - They believe they're doing the right thing

5. **Mentor or ally** (1-2 characters)
   - An outsider perspective on the system
   - What they represent thematically

6. **At least 1-2 additional characters** the story needs
   - Derive from the seed's premise and the world's factions/society

FOR EACH CHARACTER INCLUDE:
- Name, age, role
- Ghost/Wound/Want/Need/Lie chain (for major characters)
- Three sliders (proactivity/likability/competence) with numbers and justification
- Arc type and arc trajectory
- Speech pattern (all 8 dimensions, with example lines)
- Physical appearance (specific, not generic)
- Physical habits and unconscious tells
- Secrets (what the reader doesn't learn immediately)
- Key relationships (mapped to other characters)
- Thematic role (what question does this character embody?)

IMPORTANT:
- Characters must INTERCONNECT. Their wants should conflict with each other.
- Every secret should be something that would CHANGE the story if revealed.
- Speech patterns must be distinct enough to pass the no-tags test.
- The protagonist's habits should connect to their abilities or wound.
- The antagonist should be as fully realized as the protagonist -- a worthy opponent.
- All names and details must come from the seed and world docs, not from templates.
- Target ~3000-4000 words. Dense character work, not padding.
"""

print("Calling writer model...", file=sys.stderr)
result = call_writer(prompt)
print(result)
