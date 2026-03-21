#!/usr/bin/env python3
"""
Build a condensed arc summary for full-novel evaluation.
For each chapter: first 150 words, last 150 words, plus any dialogue.
Gives the reader panel enough to evaluate the ARC without 72k tokens.
"""
import os
import re
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / ".env")

CHAPTERS_DIR = BASE_DIR / "chapters"

from api_client import call_model

_WRITER_SYSTEM = "You summarize novel chapters precisely. State what HAPPENS, what CHANGES, and what QUESTIONS are left open. No evaluation. No praise. Just events and shifts."

def call_writer(prompt, max_tokens=4000):
    return call_model(prompt, system=_WRITER_SYSTEM, max_tokens=max_tokens)

def extract_key_passages(text):
    """Get opening, closing, and best dialogue from a chapter."""
    words = text.split()
    opening = ' '.join(words[:150])
    closing = ' '.join(words[-150:])
    
    # Extract dialogue lines
    dialogue = re.findall(r'["""]([^"""]{20,})["""]', text)
    # Pick up to 3 longest dialogue lines
    dialogue.sort(key=len, reverse=True)
    top_dialogue = dialogue[:3]
    
    return opening, closing, top_dialogue

def main():
    summaries = []
    
    ch_files = sorted(CHAPTERS_DIR.glob("ch_*.md"))
    for path in ch_files:
        ch = int(path.stem.split('_')[1])
        text = path.read_text()
        wc = len(text.split())
        opening, closing, dialogue = extract_key_passages(text)
        
        # Get a 100-word summary from the model
        summary = call_writer(
            f"Summarize this chapter in exactly 3 sentences. What happens, what changes, what question is left open.\n\nCHAPTER {ch}:\n{text}",
            max_tokens=200
        )
        
        entry = f"""### Chapter {ch} ({wc} words)
**Summary:** {summary}

**Opening:** {opening}...

**Closing:** ...{closing}

**Key dialogue:**
"""
        for d in dialogue:
            entry += f'> "{d}"\n\n'
        
        summaries.append(entry)
        print(f"Ch {ch}: summarized ({wc}w)")
    
    # Load canon and seed for dynamic premise
    canon_path = BASE_DIR / "canon.md"
    seed_path = BASE_DIR / "seed.txt"
    canon_text = canon_path.read_text() if canon_path.exists() else ""
    seed_text = seed_path.read_text() if seed_path.exists() else ""

    # Derive title from seed.txt first line
    title = "Untitled Novel"
    if seed_text.strip():
        first_line = seed_text.strip().split('\n')[0].strip().lstrip('# ')
        if first_line:
            title = first_line

    # Calculate total word count
    ch_files = sorted(CHAPTERS_DIR.glob("ch_*.md"))
    total_wc = sum(len(f.read_text().split()) for f in ch_files)

    # Build premise from seed + canon
    premise_source = seed_text[:500] if seed_text else "(No seed.txt found)"

    # Assemble
    full = f"""# {title.upper()}
## Full-Arc Summary for Reader Panel

This document contains chapter summaries, opening/closing passages,
and key dialogue. Total novel: {total_wc:,} words.

PREMISE (from seed):
{premise_source}

CANON SUMMARY (from canon.md):
{canon_text[:1500] if canon_text else "(No canon.md found)"}

---

"""
    full += '\n---\n\n'.join(summaries)
    
    out_path = BASE_DIR / "arc_summary.md"
    out_path.write_text(full)
    print(f"\nSaved to {out_path} ({len(full.split())} words)")

if __name__ == "__main__":
    main()
