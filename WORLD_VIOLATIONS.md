# World-Building Violations Audit

## Summary
**36 violations found across 16 chapters.**

Source of truth: `world.md`, `characters.md`, `seed.txt`.
Rules checked: (1) No sound communication, (2) Cephalopods don't stand/walk, (3) All tech is biological, (4) Aquatic environment, (5) Humans are vermin, (6) Telepathy translates as familiar voices, (7) Cephalopod names are mathematical notation.

---

## Chapter-by-Chapter

### Ch 1
No violations. Establishes world rules correctly — bioluminescent + telepathic communication, familiar-voice translation (mother/grandmother/ex), tentacles, fluid environment, implant process. Reference chapter.

---

### Ch 2
- Line: `"*Smart one. Let's see how smart you become.*"` arrives as `"information-voice. Not voice. Signal. Pure meaning without the accommodation of spoken language."` — **RULE 6 VIOLATION:** Earlier in the same chapter the familiar-voice translation (Aleksei/brother) is used correctly. Here the same communication from 0.3̅ is rendered as a generic information-signal with no familiar-voice framing. The rule requires ALL cephalopod-to-human communication to arrive filtered through the human's emotional associations. Pick one rendering and hold it.

---

### Ch 3
- Line: `"suspended in the medium like a message in a bottle. An actual bottle. Plastic. Human-made."` — **RULE 3 VIOLATION:** The cephalopod is apparently using a human-made plastic bottle as a nutrient delivery container. All cephalopod technology is biological — grown, not built. Non-biological materials have no place in cephalopod operational use. (Human artifacts the squids collected for study is fine; using one as lab equipment is not.)

---

### Ch 4
- Line: `"A sound—not quite sound. More like the feeling of sound, or the idea of it. It came from everywhere and nowhere. It resolved into words. 'Welcome. You are safe. You are valuable research subjects.'"` — **RULE 6 VIOLATION:** Telepathic communication arriving as a generic broadcast voice rather than filtered through Dylan's personal emotional associations (mother, grandmother, ex). This is the first real communication he receives; it should already be processed through his implant as a familiar voice.
- Line: `"the voice from everywhere said: 'Twenty-six hours. Your neurological integration is progressing normally.'"` — **RULE 6 VIOLATION:** Same as above. Anonymous omnidirectional voice. The implant should not produce a generic AI-announcement register; it should hijack known voices.
- Line: `"The voice spoke again. 'You will be brought to integration chambers once your physiology demonstrates baseline stability. For now, rest. Hydration systems are integrated into the chamber walls. Consume as needed.'"` — **RULE 6 VIOLATION:** Third instance in the same chapter of cephalopod telepathy arriving as an impersonal, institutional announcement rather than a voice from Dylan's memory. Completely contradicts the unsettling wrongness of the familiar-voice mechanic established in Ch 1.

---

### Ch 5
- Line: `"Irina sat on her cot across from his, hands clasped between her knees."` — **RULE 4 BORDERLINE VIOLATION:** "Cot" implies terrestrial dry-surface furniture. The world allows terrariums as semi-natural environments, but the use of "cot" implies a wholly non-aquatic setup with human furnishings. Minor but worth standardizing.
- Line: `"His knees gave out. He hit the floor hard enough to knock wind that was already compromised out of whatever remained of his lungs."` — **RULE 4 BORDERLINE VIOLATION:** "Floor" and "knock wind out of his lungs" presupposes an air-filled, gravity-defined terrestrial space. Consistent with a terrarium setup, but directly contradicts the aquatic default.

---

### Ch 6
- Line: `"0.3̅'s communication came through layers of distortion. Irina received it as her sister's voice"` — **RULE 6 + CHARACTER CONSISTENCY VIOLATION (SIGNIFICANT):** Two problems in one line. (1) Irina has no sister. `characters.md` is explicit: she has one sibling, an **older brother named Aleksei**, established in Ch 1 and Ch 2 as the voice she hears. There is no sister in the character registry. (2) The voice has already been established as Aleksei's in Chapters 1 and 2. Switching to a sister who doesn't exist breaks both the world rule and the character file. This needs to be corrected to Aleksei.

---

### Ch 7
- Line: `"Come. There's a pool. You'll need water soon. The membrane needs it."` — **RULE 4 VIOLATION:** 0.3̅ saying "there's a pool" and leading Dylan to it confirms the default corridor environment is **not aquatic**. If the ship's corridors were underwater, there would be no need to go *to* a pool. The corridors are effectively dry or air-filled, which directly contradicts "no dry corridors" in `world.md`.
- Line: `"He followed her out of the chamber, down corridors that pulsed with bioluminescence, through spaces that seemed to shift their geometry when he wasn't looking directly at them."` — **RULE 4 VIOLATION:** Dylan walks through dry ship corridors without a bio-suit, before full conversion. The ship's internal spaces should be aquatic. Even at this stage he only has partial membrane; he should not be walking through unrestricted aquatic corridors unaided — but more importantly, the corridors are described as walkable, not submerged.
- Line: `"He stepped into the pool and the membrane across his skin lit up"` — **RULE 4 VIOLATION:** "Stepped into" a pool implies transitioning from a non-aquatic environment to an aquatic one. Confirms the corridor Dylan just walked through was dry. This is structurally backwards from the world: the whole ship is aquatic; the terrarium is the exception.

---

### Ch 8
- No hard violations. The observation chamber's "pool" addition is consistent with the terrarium concept. Assembly-line mockup is ambiguous (could be grown), not flagged as clear violation.

---

### Ch 9
- Line: `"A voice came through the pod wall— The sentences fell into equations, numbers threading through the words like beads on a string. *7.3 to 4.2 ratio* the mother-voice said"` — **RULE 6 INCONSISTENCY:** Chapters 1, 2 established the voice Irina hears from 0.3̅ as her **brother Aleksei's voice**. Chapter 6 incorrectly rendered it as her "sister's voice" (who doesn't exist). Here it becomes "the mother-voice." This is the third different familiar-voice designation for the same cephalopod communicating with the same human. The rule allows for variation across different cephalopods, but **0.3̅'s signal** should have a consistent translation register for Irina. Establish one and hold it.

---

### Ch 10
- Line: `"The pods hissed. The suspension fluid began draining"` — **RULE 1 MINOR VIOLATION:** Pods "hissing" implies audible sound production from a mechanical seal or valve mechanism. In a fully biological ship, sound wouldn't be a design output — biological membranes dilate silently. Minor but consistent with the no-mechanical-sound principle.

---

### Ch 11 *(WORST CHAPTER — 6 violations)*
- Line: `"The floor was soft under his feet, yielding like wet moss."` — **RULE 4 VIOLATION:** Raj is walking on a floor on the **bridge** of the cephalopod ship. The bridge is the operational center of a living aquatic vessel. There should be no floor that humans walk on — the environment should be fully submerged aquatic. Raj's bio-suit is accumulating but he is explicitly standing and walking.
- Line: `"Grandma stood closest."` — **RULE 2 VIOLATION:** 0.3̅ is described as **standing**. Cephalopods don't stand. They float, drift, hover, hang, extend. "Stood closest" implies upright bipedal orientation. This is one of the hardest rules in the world bible and it's violated outright in the description of the most important cephalopod character.
- Line: `"Raj crossed the bridge."` — **RULE 4 VIOLATION:** Walking across the bridge. Ship bridge is aquatic. Raj should be swimming, floating, or propelled — not "crossing" a space as though walking.
- Line: `"Grandma said through the external speakers, the cephalopod translation device that rendered her telepathic transmission into human sound."` — **RULES 1 AND 3 DOUBLE VIOLATION (MOST EGREGIOUS IN NOVEL):** Two fundamental world rules broken in one sentence. (1) There are **no external speakers** in cephalopod civilization — sound is not a communication medium. (2) A "cephalopod translation device" is **mechanical technology** — but all cephalopod technology is biological, grown, not built. A device that converts telepathic transmission to audible sound would be as alien to cephalopod civilization as a squid using a rotary dial telephone. This passage needs a complete rewrite. The correct mechanism is: Raj's implant processes 0.3̅'s bioluminescent/telepathic signal and renders it as his grandmother's voice inside his skull. No device. No speakers.
- Line: `"Her beak curved. That was a smile."` — **HUMANOID TREATMENT VIOLATION:** Interpreting a cephalopod's beak movement as a "smile" is a human facial-expression attribution. Cephalopods communicate through bioluminescence and telepathy; their physical anatomy should not map onto human emotional expressions. A curved beak might be incidental anatomy, but framing it as a deliberate smile gives 0.3̅ a human emotional facial register she shouldn't have.
- Line: `"Raj stood at the center of the bridge, chitinous nodes gleaming faintly"` — **RULE 4 VIOLATION:** Fourth standing reference in this chapter. Raj is human-with-growing-bio-suit, but the bridge is aquatic space. "Stood at the center" implies a stationary upright posture on a dry surface.

---

### Ch 12
- Line: `"Irina found him on the observation deck, standing motionless beneath the bioluminescent panels."` — **RULE 4 VIOLATION:** The observation deck is ship infrastructure; if this is an aquatic space, humans should be floating/hovering in their bio-suits, not "standing motionless." If it's a terrarium-style space, that needs to be established as such — but here it's framed as part of the ship proper.
- Line: `"He turned back to the observation panel."` — **RULE 4 MINOR VIOLATION:** Consistent with standing-on-a-surface terrestrial behavior in an aquatic space.

---

### Ch 13
No hard violations. 0.3̅ POV — bioluminescent communication correctly rendered between cephalopods. Administrative language is appropriately mathematical. 0.3̅'s chromatophores/bioluminescence handle all internal communication correctly.

---

### Ch 14
- Line: `"Pieter sat on what approximated a bench, though the surface yielded and reshaped itself constantly"` — **RULE 4 BORDERLINE:** Bench-like furniture in a cephalopod holding space. The terrarium exception could cover this, but a dedicated holding chamber for a human should more explicitly be designated as semi-natural/terrarium space. As written, the chamber is presented as standard ship space with human-style seating.
- Line: `"*I am Δ∇² + 3(#FF4500)*, the sharp-edged squid announced. *You will address me as Delta. I manage this vessel. Grandma manages the research. You will not interfere with either.*"` — **RULE 6 VIOLATION:** Delta Del's telepathic communication to the newly-implanted Pieter arrives as straightforward text with no familiar-voice rendering. Per the world rules, even the very first cephalopod communication a human receives should come filtered through their emotional associations — Delta Del's signal should arrive as the voice of someone Pieter knew from his life in Pretoria (a Party official, a church elder, an army officer). The wrongness of that mismatch is the horror of the mechanic.

---

### Ch 15
- Line: `"The observation chamber smelled like ozone and something else—the sharp bite of blood that had oxidized too long in recycled air."` — **RULE 4 VIOLATION:** "Recycled air" explicitly confirms the observation chamber is an air-filled, non-aquatic space in which cephalopods also operate. While the terrarium concept supports human-breathable spaces, the cephalopods (Pieter, Irina, 0.3̅) are all present and interacting in what is described as an air-recycled atmosphere. The cephalopods should not be comfortable in air — they're aquatic caste. This needs the environment framing clarified: if it's a terrarium/observation bay the cephalopods access through membrane barriers, that architecture needs to be established clearly, not just air-filled space everyone wanders through.

---

### Ch 16 *(SECOND WORST — 4 violations)*
- Line: `"'Ready?' Her voice came through a speaker, filtered and flattened. He was still just an organism that made sounds with its mouth."` — **RULES 1 AND 3 VIOLATION:** Second instance of a "speaker" device (first was Ch 11). A mechanical speaker converting cephalopod communication to audible sound violates both the no-sound-communication rule and the all-technology-is-biological rule. 0.3̅ communicating with Xi Pei before his implant has taken hold should be handled differently — perhaps visual bioluminescence that the implant (even in its first moments of integration) begins to partially translate, or simply as alien light-patterns he can't yet parse. Not a speaker.
- Line: `"he could hear the classical music playing somewhere in the deeper decks of the ship, the music that no one had told them about, the music that had been there all along, threading through the background hum of the environment systems like a thought that the ship itself was thinking."` — **RULE 1 MAJOR VIOLATION:** Classical music on a cephalopod ship. This is one of the most deeply wrong things in the manuscript. Cephalopod civilization has **no sound-based culture**. There would be no music — no melody, no rhythm in the sonic sense, no instruments, no audio aesthetic. Their "music" would be bioluminescent pattern — visual fractals, color harmonics, mathematical rhythm expressed in light. A cephalopod ship would not have classical music threading through its decks any more than it would have a radio tower. This passage needs to be reconceived entirely: if the intent is to suggest the ship has an ambient "cultural signal" leaking through its systems, it should be rendered as bioluminescent pulse, telepathic background tone, or mathematical resonance — not audio music.
- Line: `"Xi Pei stood in the observation space—the shelf carved into the wall where they kept him while the others were processed."` — **RULE 4 MINOR:** Standing in a shelf-space. Consistent with terrestrial human-space, but the "shelf carved into the wall" language implies a dry, carved recess rather than an aquatic environment.
- Line: `"He moved to the table. [...] He lay back."` — **RULE 4:** The implantation table in the implantation chamber — if this is in the ship proper it should be an aquatic space. Xi Pei lies down on a table and the procedure takes place. But there's no indication this is a flooded room; it reads as a dry operating table environment.

---

### Ch 17
No hard violations. Irina in suspension pod — correctly presented as fluid environment. Network monitoring described through bioluminescent color (green frequencies, orange-red for Delta Del). The chapter's reliance on "listen" as a metaphor for receiving telepathic signal is a minor tone concern but not a world-rule violation.

---

### Ch 18
- Line: `"Xi Pei planted his feet on the bridge deck. Slick residue glued his toes under suit membrane, flux-thick."` — **RULE 4 VIOLATION:** Xi Pei on the bridge, feet planted on the deck. Even with bio-suit, "planted feet on deck" implies standing on a flat floor rather than moving through aquatic medium. If the bridge is the aquatic operations center it should be, this needs different physical language: anchored tentacle-grip via bio-suit, tethered, neutrally buoyant, not feet on floor.

---

### Ch 19
No hard violations. 0.3̅ POV — "propelled away from the bridge cluster," "tentacles coiled tight," "jetted closer to the observation window," — correct cephalopod movement. Bioluminescent communication between cephalopods correctly rendered. Chapter is one of the strongest for world-rule compliance.

---

### Ch 20
- Line: `"Xi Pei planted his feet wider on the observation deck. The floor membrane clung to his soles, warm and tacky, like fresh epoxy on a factory cleanroom tile."` — **RULE 4 VIOLATION:** Feet planted on deck floor. The "floor membrane clung to his soles" suggests a tactile terrestrial experience. The analogy to a factory cleanroom tile underscores how air-filled and non-aquatic this environment feels.
- Line: `"Saline mist hung in the air, sharp against his sinuses, carrying the tang of iodine and something fermented"` — **RULE 4 PARTIAL VIOLATION:** "Saline mist in the air" suggests a humid, misted non-submerged environment. The observation deck is misted rather than flooded. While this could be a partially-aquatic transitional space for bio-suited humans, it's inconsistent with the established world rule that the cephalopod environment is fully underwater/aquatic.

---

### Ch 21
- Line: `"Footsteps echoed above. Not squid pads. Drone barbs scraping."` — **RULES 1 AND 4 VIOLATION:** "Footsteps echoed" implies (a) a non-aquatic walkable surface, (b) audible echo in a space that should be water-filled. In an aquatic environment, the drones wouldn't produce footstep sounds. The "scraping" of drone barbs in water would produce vibration, not echo. The language is terrestrial action-movie language dropped into an aquatic alien ship.

---

## Priority Fix List (Most Egregious First)

| Priority | Chapter | Violation | Rule |
|----------|---------|-----------|------|
| 🔴 1 | Ch 11 | "Grandma said through the external speakers, the cephalopod translation device that rendered her telepathic transmission into human sound." | Rules 1 + 3 |
| 🔴 2 | Ch 16 | "he could hear the classical music playing somewhere in the deeper decks of the ship" | Rule 1 |
| 🔴 3 | Ch 16 | "'Ready?' Her voice came through a speaker, filtered and flattened." | Rules 1 + 3 |
| 🔴 4 | Ch 11 | "Grandma stood closest." | Rule 2 |
| 🔴 5 | Ch 6 | "Irina received it as her sister's voice" — Irina has no sister (brother is Aleksei) | Rule 6 + character registry |
| 🟠 6 | Ch 4 | Three instances of generic "voice from everywhere" rather than familiar-voice telepathy | Rule 6 |
| 🟠 7 | Ch 11 | "Her beak curved. That was a smile." | Anti-humanoid principle |
| 🟠 8 | Ch 7 | "Come. There's a pool" + dry corridors + "stepped into the pool" | Rule 4 |
| 🟠 9 | Ch 9 | "the mother-voice" (3rd different familiar voice for same character/cephalopod pair) | Rule 6 consistency |
| 🟡 10 | Ch 14 | Delta Del's full speech to Pieter rendered without familiar-voice filter | Rule 6 |

---

## Chapters Clean (No Violations)
- Ch 1 (reference chapter — world rules established correctly)
- Ch 8 (some borderline language but no outright violations)
- Ch 13 (0.3̅ POV — strong adherence)
- Ch 17 (Irina in suspension — strong adherence)
- Ch 19 (0.3̅ POV — best chapter for world-rule compliance)

## Chapters With Violations (Ranked Worst to Best)
1. **Ch 11** — 6 violations (external speakers, standing cephalopod, dry bridge, smile attribution)
2. **Ch 16** — 4 violations (classical music, speaker, dry environment)
3. **Ch 4** — 3 violations (all Rule 6 — generic voice)
4. **Ch 7** — 3 violations (dry corridors, "stepped into pool")
5. **Ch 6** — 1 significant violation (non-existent sister + familiar voice inconsistency)
6. **Ch 2, 3, 5, 9, 10, 12, 14, 15, 18, 20, 21** — 1–2 violations each
