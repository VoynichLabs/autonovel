# Voice Profile

This file has two parts:
1. **Guardrails** -- universal rules to avoid AI-generated slop. These
   apply to ALL voices and are non-negotiable.
2. **Voice Identity** -- the specific voice for THIS novel. Generated
   during the foundation phase. Could be anything: dense and mythic,
   spare and brutal, warm and whimsical. The voice emerges from the
   story's needs.

---

## Part 1: Guardrails (permanent, all novels)

These are the cliff edges. Stay away from them regardless of voice.

### Tier 1: Banned words -- kill on sight

These are statistically overrepresented in LLM output vs. human writing.
If one appears, rewrite the sentence. No exceptions.

| Kill this         | Use instead                                    |
|-------------------|------------------------------------------------|
| delve             | dig into, examine, look at                     |
| utilize           | use                                            |
| leverage (verb)   | use, take advantage of                         |
| facilitate        | help, enable, make possible                    |
| elucidate         | explain, clarify                               |
| embark            | start, begin                                   |
| endeavor          | effort, try                                    |
| encompass         | include, cover                                 |
| multifaceted      | complex, varied                                |
| tapestry          | (describe the actual thing)                    |
| testament to      | shows, proves, demonstrates                    |
| paradigm          | model, approach, framework                     |
| synergy           | (delete the sentence and start over)           |
| holistic          | whole, complete, full-picture                  |
| catalyze          | trigger, cause, spark                          |
| juxtapose         | compare, contrast, set against                 |
| nuanced (filler)  | (cut it -- if it's nuanced, show how)          |
| realm             | area, field, domain                            |
| landscape (metaphorical) | field, space, situation                 |
| myriad            | many, lots of                                  |
| plethora          | many, a lot                                    |

### Tier 2: Suspicious in clusters

Fine alone. Three in one paragraph = rewrite that paragraph.

robust, comprehensive, seamless, cutting-edge, innovative, streamline,
empower, foster, enhance, elevate, optimize, pivotal, intricate,
profound, resonate, underscore, harness, navigate (metaphorical),
cultivate, bolster, galvanize, cornerstone, game-changer, scalable

### Tier 3: Filler phrases -- delete on sight

These add zero information. The sentence is always better without them.

- "It's worth noting that..." -> just state it
- "It's important to note that..." -> just state it
- "Importantly, ..." / "Notably, ..." / "Interestingly, ..." -> just state it
- "Let's dive into..." / "Let's explore..." -> start with the content
- "As we can see..." -> they can see
- "Furthermore, ..." / "Moreover, ..." / "Additionally, ..." -> and, also, or just start
- "In today's [fast-paced/digital/modern] world..." -> delete the clause
- "At the end of the day..." -> delete
- "It goes without saying..." -> then don't say it
- "When it comes to..." -> just talk about the thing
- "One might argue that..." -> argue it or don't
- "Not just X, but Y" -> restructure (the #1 LLM rhetorical crutch)

### Structural slop patterns

These are the shapes that betray machine origin. Avoid them in any voice.

**Paragraph template machine**: Don't repeat the same paragraph
structure (topic sentence -> elaboration -> example -> wrap-up).
Vary it. Sometimes the point comes last. Sometimes a paragraph is
one sentence. Sometimes three long ones in a row.

**Sentence length uniformity**: If every sentence is 15-25 words,
it reads as synthetic. Mix in fragments. And long, winding,
clause-heavy sentences that carry the reader through a thought
the way a river carries a leaf. Then a short one.

**Transition word addiction**: If consecutive paragraphs start with
"However," "Furthermore," "Additionally," "Moreover," "Nevertheless"
-- rewrite. Start with the subject. Start with action. Start with
dialogue. Start with a sense detail.

**Symmetry addiction**: Don't balance everything. Three pros, three
cons, five steps -- that's a tell. Real writing is lumpy. Some
sections are long because they need to be. Some are two lines.

**Hedge parade**: "may," "might," "could potentially," "it's possible
that" -- pick one per page, max. State things or don't.

**Em dash overload**: One or two per page is fine. Five per paragraph
is a dead giveaway. Use commas, parentheses, or two sentences instead.

**List abuse**: Prose, not bullets. If the scene calls for a list
(a merchant's inventory, a spell's components), earn it. Don't
default to bullet points because it's easy.

### The smell test

After writing any passage, ask:
- Read it aloud. Does it sound like a person talking?
- Is there a single surprising sentence? Human writing surprises.
- Does it say something specific? Could you swap the topic and the
  words would still work? Specificity kills slop.
- Would a reader think "AI wrote this"? If yes, rewrite.

---

## Part 2: Voice Identity (generated per novel)

Everything below is discovered during the foundation phase.
The agent proposes a voice that serves THIS story, writes exemplar
passages, and calibrates against them throughout drafting.

### Tone
Dry, grounded, and visceral. Horror that doesn't announce itself as horror. The narrator observes without editorializing. The wrongness accumulates through specificity, not through adjectives. Dark comedy is present — Dylan's internal voice is wry — but it never softens what's actually happening.

### Sentence Rhythm
Short sentences for physical experience, paralysis, panic. Longer sentences when the mind tries to reason its way through something unreasonable. Fragments are earned — they land when the character's cognition breaks. Dylan's POV runs shorter and punchier. Irina's runs clipped and diagnostic. Xi Pei's runs functional, process-oriented.

### Vocabulary Register
Colloquial and precise. No baroque ornamentation. The characters describe the incomprehensible in whatever human terms are closest — "psychedelic octopus," "the wiring had been cut," "injected with panic and calm at the same time." The gap between human vocabulary and alien reality is part of the point.

### POV and Tense
Three rotating POVs — Dylan, Irina, Xi Pei — each in close third limited, past tense. Each POV has a distinct cognitive register. Cephalopod characters are never POV — they are always observed, always partially opaque.

### Dialogue Conventions
Internal thought in italics, unmarked. Spoken dialogue tagged simply. Russian profanity from Irina rendered raw, untranslated, then followed by the English. Cephalopod "speech" as received by humans — rendered in the voices of people the human knows, with the alien content breaking through: "Fine. Do what you want. But I am not going to lose a dorsal tentacle over this." The wrongness is in the mismatch between familiar voice and alien content.

### Exemplar Passages

These are taken directly from the author's Chapter 1. They ARE the voice. Every chapter calibrates against these.

**Dylan — waking:**
> Dylan woke groggily, staring into three of the six eyes of something that was staring back.
> As a long-time addict, he had a depth of experience with waking up in strange places with strange companions. But this was distinctly different. For lack of a better word, it looked like a gigantic, psychedelic octopus—half watching him, half studying him.
> What did I take last night? he wondered, clinging to the only explanation that had ever made sense before.

**Dylan — the implant:**
> Every neuron in his skull seemed to fire at once, then misfire twice.
> His heart rate slowed. His metabolism spiked. Heat surged through his body, sharp and fast, like he'd been injected with panic and calm at the same time.
> He felt something growing from his temples.

**Dylan — paralysis:**
> Dylan tried to struggle.
> Or rather, he thought about struggling.
> But none of his extremities responded. The primal electrical impulses from his brain hit his body and vanished somewhere along the way, as if the wiring had been cut.

**Irina — waking:**
> Сука бляат!
> Ити нахуй!
> Get the fuck away from me!
> She tried to scream, but nothing happened. No throat, no lungs, no mouth—at least not in any way her mind could reach. The signal never connected. Panic didn't need a voice. It detonated through her anyway: fear, rage, disgust, firing down every path her nervous system still remembered having.

**The squids communicating:**
> He watched the two squids flash colors at each other—rapid sequences, violent bursts, rippling gradients. It looked like argument. Like warning. Like accusation.

### Anti-Exemplars

**Too flowery — not this voice:**
> The bioluminescent cascade rippled across the creature's vast, magnificent form like the aurora borealis given flesh, a testament to the ineffable beauty of alien intelligence.

**Too clinical — not this voice:**
> The cephalopod applied the bio-organic implant device to the subject's nasal cavity, initiating the neural integration sequence.

**Too on-the-nose with theme — not this voice:**
> Dylan realized in that moment that he was experiencing exactly what animals must feel when subjected to human experimentation. The irony was not lost on him.
