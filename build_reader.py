#!/usr/bin/env python3
"""Build a single-file reading page for the autonovel squid story."""

import os
import re
import html

CHAPTERS_DIR = os.path.expanduser("~/Documents/GitHub/autonovel/chapters")
OUTPUT_DIR = os.path.expanduser("~/Documents/GitHub/autonovel/reading")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "index.html")

NOVEL_TITLE = "Let's Get You Some Tentacles"
NOVEL_SUBTITLE = "A Science Fiction Novel"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def count_words(text):
    return len(text.split())


def md_to_html(text):
    """Convert markdown to HTML — chapter body only."""
    lines = text.split("\n")
    output = []
    in_para = False

    def close_para():
        nonlocal in_para
        if in_para:
            output.append("</p>")
            in_para = False

    def inline(s):
        # Escape HTML first
        s = html.escape(s)
        # Bold+italic ***
        s = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', s)
        # Bold **
        s = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', s)
        # Italic * or _
        s = re.sub(r'\*(.*?)\*', r'<em>\1</em>', s)
        s = re.sub(r'_(.*?)_', r'<em>\1</em>', s)
        # Em-dash cleanup
        s = s.replace("--", "—")
        return s

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        # Skip the top-level chapter title line (# Chapter N) — handled separately
        if re.match(r'^# ', line):
            close_para()
            i += 1
            continue

        # H2 — section/POV headers
        if re.match(r'^## ', line):
            close_para()
            heading_text = inline(line[3:].strip())
            output.append(f'<h2 class="section-head">{heading_text}</h2>')
            i += 1
            continue

        # H3
        if re.match(r'^### ', line):
            close_para()
            heading_text = inline(line[4:].strip())
            output.append(f'<h3 class="section-sub">{heading_text}</h3>')
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^---+$', line.strip()) or re.match(r'^\*\*\*+$', line.strip()):
            close_para()
            output.append('<hr class="section-break">')
            i += 1
            continue

        # Blank line
        if line.strip() == "":
            close_para()
            i += 1
            continue

        # Normal paragraph line
        if not in_para:
            output.append('<p>')
            in_para = True
        else:
            output.append(' ')
        output.append(inline(line))
        i += 1

    close_para()
    return "\n".join(output)


def get_chapter_title(text, ch_num):
    """Extract chapter title from first # heading."""
    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return f"Chapter {ch_num}"


def get_chapter_slug(ch_num):
    return f"chapter-{ch_num:02d}"


def load_chapters():
    chapters = []
    for n in range(1, 22):
        path = os.path.join(CHAPTERS_DIR, f"ch_{n:02d}.md")
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
        title = get_chapter_title(raw, n)
        word_count = count_words(raw)
        html_body = md_to_html(raw)
        chapters.append({
            "num": n,
            "slug": get_chapter_slug(n),
            "title": title,
            "word_count": word_count,
            "html_body": html_body,
        })
    return chapters


def build_toc(chapters):
    items = []
    for ch in chapters:
        wc = f"{ch['word_count']:,}"
        items.append(
            f'<li><a href="#{ch["slug"]}">'
            f'<span class="toc-num">Ch. {ch["num"]:02d}</span>'
            f'<span class="toc-title">{html.escape(ch["title"])}</span>'
            f'<span class="toc-wc">{wc} words</span>'
            f'</a></li>'
        )
    return "\n".join(items)


def build_chapter_sections(chapters):
    sections = []
    total = len(chapters)
    for idx, ch in enumerate(chapters):
        prev_link = ""
        next_link = ""
        if idx > 0:
            prev = chapters[idx - 1]
            prev_link = f'<a href="#{prev["slug"]}" class="nav-btn prev">&#8592; Ch. {prev["num"]:02d}</a>'
        else:
            prev_link = '<span class="nav-btn disabled"></span>'

        if idx < total - 1:
            nxt = chapters[idx + 1]
            next_link = f'<a href="#{nxt["slug"]}" class="nav-btn next">Ch. {nxt["num"]:02d} &#8594;</a>'
        else:
            next_link = '<span class="nav-btn disabled"></span>'

        toc_back = '<a href="#toc" class="nav-btn toc-back">&#8679; Contents</a>'

        sections.append(f"""
<section id="{ch['slug']}" class="chapter">
  <div class="chapter-header">
    <div class="chapter-num">Chapter {ch['num']}</div>
    <h1 class="chapter-title">{html.escape(ch['title'])}</h1>
    <div class="chapter-meta">{ch['word_count']:,} words</div>
  </div>
  <div class="chapter-body">
{ch['html_body']}
  </div>
  <nav class="chapter-nav">
    {prev_link}
    {toc_back}
    {next_link}
  </nav>
</section>
""")
    return "\n".join(sections)


def build_html(chapters):
    toc = build_toc(chapters)
    chapter_sections = build_chapter_sections(chapters)
    total_words = sum(ch['word_count'] for ch in chapters)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{NOVEL_TITLE}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Josefin+Sans:wght@300;400;600&display=swap" rel="stylesheet">
<style>
/* ── Reset & base ─────────────────────────────────── */
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
  --bg:        #0f0f13;
  --bg2:       #16161e;
  --bg3:       #1e1e2a;
  --accent:    #39ff14;
  --accent2:   #7affe0;
  --text:      #e2ddd5;
  --text-muted:#8a8480;
  --border:    #2a2a3a;
  --max-w:     680px;
  --font-body: 'EB Garamond', Georgia, serif;
  --font-ui:   'Josefin Sans', 'Helvetica Neue', sans-serif;
}}

html {{ scroll-behavior: smooth; }}

body {{
  background: var(--bg);
  color: var(--text);
  font-family: var(--font-body);
  font-size: 1.25rem;
  line-height: 1.75;
  -webkit-font-smoothing: antialiased;
}}

/* ── Cover ────────────────────────────────────────── */
#cover {{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 4rem 2rem;
  text-align: center;
  background: radial-gradient(ellipse at 50% 40%, #1a1a2e 0%, var(--bg) 70%);
  position: relative;
  overflow: hidden;
}}

#cover::before {{
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 20% 80%, rgba(57,255,20,0.04) 0%, transparent 50%),
    radial-gradient(circle at 80% 20%, rgba(122,255,224,0.04) 0%, transparent 50%);
  pointer-events: none;
}}

.cover-eyebrow {{
  font-family: var(--font-ui);
  font-size: 0.7rem;
  letter-spacing: 0.35em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 2rem;
}}

.cover-title {{
  font-family: var(--font-body);
  font-size: clamp(2.4rem, 6vw, 4.5rem);
  font-weight: 500;
  line-height: 1.1;
  letter-spacing: -0.01em;
  color: var(--text);
  max-width: 700px;
  margin-bottom: 1rem;
}}

.cover-subtitle {{
  font-family: var(--font-ui);
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 3rem;
}}

.cover-lede {{
  font-style: italic;
  font-size: 1.05rem;
  color: var(--text-muted);
  max-width: 520px;
  line-height: 1.65;
  margin-bottom: 3.5rem;
}}

.cover-stats {{
  font-family: var(--font-ui);
  font-size: 0.7rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 3rem;
}}

.cover-stats span {{
  color: var(--accent2);
}}

.btn-toc {{
  display: inline-block;
  font-family: var(--font-ui);
  font-size: 0.72rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  text-decoration: none;
  color: var(--bg);
  background: var(--accent);
  padding: 0.75rem 2rem;
  border-radius: 2px;
  transition: background 0.2s, transform 0.15s;
}}
.btn-toc:hover {{ background: var(--accent2); transform: translateY(-1px); }}

/* ── TOC ──────────────────────────────────────────── */
#toc {{
  max-width: 760px;
  margin: 0 auto;
  padding: 5rem 2rem 4rem;
}}

.toc-heading {{
  font-family: var(--font-ui);
  font-size: 0.7rem;
  letter-spacing: 0.35em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 2.5rem;
}}

#toc ul {{
  list-style: none;
}}

#toc li {{
  border-bottom: 1px solid var(--border);
}}

#toc li a {{
  display: flex;
  align-items: baseline;
  gap: 0.75rem;
  padding: 0.9rem 0;
  text-decoration: none;
  color: var(--text);
  transition: color 0.15s;
}}
#toc li a:hover {{ color: var(--accent); }}
#toc li a:hover .toc-num {{ color: var(--accent); }}

.toc-num {{
  font-family: var(--font-ui);
  font-size: 0.65rem;
  letter-spacing: 0.1em;
  color: var(--text-muted);
  min-width: 3.5rem;
  flex-shrink: 0;
  transition: color 0.15s;
}}

.toc-title {{
  flex: 1;
  font-size: 1.1rem;
}}

.toc-wc {{
  font-family: var(--font-ui);
  font-size: 0.62rem;
  letter-spacing: 0.05em;
  color: var(--text-muted);
  flex-shrink: 0;
}}

/* ── Chapter sections ─────────────────────────────── */
.chapter {{
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 5rem 2rem 3rem;
}}

.chapter + .chapter {{
  border-top: 1px solid var(--border);
  padding-top: 6rem;
}}

.chapter-header {{
  margin-bottom: 3.5rem;
  text-align: center;
}}

.chapter-num {{
  font-family: var(--font-ui);
  font-size: 0.65rem;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 1rem;
}}

.chapter-title {{
  font-family: var(--font-body);
  font-size: clamp(1.6rem, 4vw, 2.4rem);
  font-weight: 500;
  line-height: 1.2;
  color: var(--text);
  margin-bottom: 0.75rem;
}}

.chapter-meta {{
  font-family: var(--font-ui);
  font-size: 0.62rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text-muted);
}}

/* ── Body typography ─────────────────────────────── */
.chapter-body p {{
  margin-bottom: 1.25em;
  text-indent: 1.5em;
}}

.chapter-body p:first-of-type,
.chapter-body h2 + p,
.chapter-body h3 + p,
.chapter-body hr + p {{
  text-indent: 0;
}}

.chapter-body p:first-of-type::first-letter {{
  font-size: 3.5em;
  line-height: 0.8;
  float: left;
  margin: 0.05em 0.06em 0 0;
  color: var(--accent);
  font-weight: 500;
}}

.section-head {{
  font-family: var(--font-body);
  font-size: 1rem;
  font-weight: 500;
  font-style: italic;
  letter-spacing: 0.05em;
  color: var(--accent2);
  margin: 2.5em 0 1em;
}}

.section-sub {{
  font-family: var(--font-ui);
  font-size: 0.72rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin: 2em 0 1em;
}}

hr.section-break {{
  border: none;
  text-align: center;
  margin: 2.5em auto;
  color: var(--text-muted);
  overflow: visible;
  height: 1em;
}}

hr.section-break::after {{
  content: '· · ·';
  font-size: 1.1rem;
  letter-spacing: 0.4em;
  color: var(--text-muted);
}}

.chapter-body em {{ font-style: italic; }}
.chapter-body strong {{ font-weight: 600; color: var(--text); }}

/* ── Chapter nav ─────────────────────────────────── */
.chapter-nav {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 4rem;
  padding-top: 2rem;
  border-top: 1px solid var(--border);
  gap: 0.5rem;
}}

.nav-btn {{
  font-family: var(--font-ui);
  font-size: 0.65rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border: 1px solid var(--border);
  border-radius: 2px;
  color: var(--text-muted);
  background: var(--bg2);
  transition: color 0.15s, border-color 0.15s, background 0.15s;
  min-width: 6rem;
  text-align: center;
  display: inline-block;
}}
.nav-btn:hover {{ color: var(--accent); border-color: var(--accent); background: var(--bg3); }}
.nav-btn.toc-back {{ color: var(--accent2); border-color: var(--accent2); }}
.nav-btn.toc-back:hover {{ background: var(--bg3); }}
.nav-btn.disabled {{ opacity: 0; pointer-events: none; }}

/* ── Scrollbar ───────────────────────────────────── */
::-webkit-scrollbar {{ width: 6px; }}
::-webkit-scrollbar-track {{ background: var(--bg); }}
::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 3px; }}
::-webkit-scrollbar-thumb:hover {{ background: var(--text-muted); }}

/* ── Responsive ──────────────────────────────────── */
@media (max-width: 600px) {{
  body {{ font-size: 1.1rem; }}
  .chapter {{ padding: 3rem 1.25rem 2rem; }}
  #toc {{ padding: 3rem 1.25rem 2rem; }}
  .toc-wc {{ display: none; }}
  .chapter-body p:first-of-type::first-letter {{ font-size: 2.8em; }}
}}
</style>
</head>
<body>

<!-- COVER -->
<div id="cover">
  <div class="cover-eyebrow">A Novel</div>
  <h1 class="cover-title">{NOVEL_TITLE}</h1>
  <div class="cover-subtitle">{NOVEL_SUBTITLE}</div>
  <p class="cover-lede">Earth is a protected galactic nature preserve. A low-ranking cephalopod scientist breaks the law — and abducts three humans to prove they are more than vermin.</p>
  <div class="cover-stats">21 chapters &nbsp;·&nbsp; <span>{total_words:,}</span> words</div>
  <a href="#toc" class="btn-toc">Read</a>
</div>

<!-- TABLE OF CONTENTS -->
<nav id="toc">
  <div class="toc-heading">Table of Contents</div>
  <ul>
{toc}
  </ul>
</nav>

<!-- CHAPTERS -->
{chapter_sections}

</body>
</html>"""


def main():
    print("Loading chapters...")
    chapters = load_chapters()
    print(f"Loaded {len(chapters)} chapters.")

    print("Building HTML...")
    page = build_html(chapters)

    print(f"Writing to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(page)

    size_kb = os.path.getsize(OUTPUT_FILE) / 1024
    print(f"Done. File size: {size_kb:.1f} KB")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
