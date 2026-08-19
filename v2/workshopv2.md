# AI Workshop v2

> **Living draft** — the basis document for the v2 workshop. Add sections, refine wording,
> flip statuses, then generate a ppt deck from the locked outline (see [Deck Generation](#deck-generation)).
>
> This workshop is **not** an "agentic" workshop. It's a *foundation* workshop: the mental
> models behind modern AI, built in a strict dependency order so each idea leans on the last.
> **Text and code only — no media, image, or art content.**
>
> v2 does **not** replace `labs/`, `demos/`, or `resources/`. It's a new track; anything from
> the old track that still earns its place is pulled in deliberately. Nothing is deleted.
>
> The old "9-lab observe" track is preserved as a **v1.5 option** (see [Option B](#option-b-v15-the-old-lab-track-preservative-option))
> in case we ever want the comparison/slow-pace version back.

## Why this shape?

The original workshop was an observe-first lab track (temperature, drag races, hallucination trivia).
For high school students meeting these tools for the first time, *how the old models behaved* is
the weakest possible use of room time — and even "today's" behavior will be outdated by the
time they graduate. What survives is the **concepts**: context, tokens, determinism, harnesses,
tools, system prompts. Teach the concepts and the specific model of the moment becomes a
swappable detail instead of the whole lesson.

So v2 is concepts-first, in dependency order. The agentic material (tools, MCP, skills)
isn't cut — it's *late*, because "what is MCP" is meaningless until "what is a context window"
and "what is a tool call" already make sense.

## Audience & Constraints

- **Who:** High school students, FRC-flavored audience, little to no formal AI background.
- **Assume:** Comfortable with basics of one language (Python or Java), terminals, GitHub.
- **Assume NOT:** Prior LLM or agent experience.
- **Room setup (unchanged):** Central GPU server (RTX 5090/32GB), Ollama host,
  Open WebUI on 3000 (no tools) and 3001 (tools/agentic), students on their own browsers.
- **Language for any student code:** _(DECIDE — v1 labs were Python, then partially Java. Lean: Python.)_
- **Session length / time budget per section:** _(fill in once statuses hit `lock`.)_
- **Instructor source of truth:** `LocalLLMCopilot` — the benchmark/forensic repo with real
  measured context profiles, tool-reliability numbers, and model inventories. Every claim in
  the deck that has a number in it should come from there, not from slide-land folklore.

## Guiding Principles

1. **Concepts before artifacts.** A model of the week is an example, never the thesis.
2. **Do over observe.** Each section lands as something the student did, saw break, or made —
   a prompt they wrote, a context they filled up, a tool call they traced.
3. **One idea per section, in load order.** No section assumes a later one.
4. **Fail visibly on purpose.** At least one deliberate, guided failure (overloaded context,
   stale knowledge, malformed tool call) — a failure students *cause* teaches better than a
   slide that describes one.
5. **Local is the microscope.** The in-room Ollama stack exists so we can *see* internals
   (tokens, context, tool-call JSON) that closed products hide. Teach the industry shape,
   inspect it locally.
6. **No archaeology.** Old-model behavior is not on the program. Current-2026 behavior is
   the exhibit; even that gets framed as "how it works *right now*, swappable when it changes."

## Section Outline

> Status key: `draft` = sketched · `refine` = needs rewrite · `lock` = final · `cut` = removed.
> Sections are **not time-boxed** yet — any section may get rebalanced. Time budgets
> are deliberately left out until the content stabilizes.
> Lettered sub-sections (e.g. `3a`) break a topic out of its parent for slide
> readability — they still cross-reference their parent, so they build on it.
> `_(Instructor depth …)_` bullets are **presenter notes** — they route to the slide's
> notes pane, never the slide itself (see [Deck Generation](#deck-generation)).

### 1. What is AI (as of 2026) _(draft)_

- Working definition for the room: software that **perceives** (text in 2026 — we're not doing
  media in this workshop), **learns patterns from data**, and **acts or decides** on those patterns.
- The 2026 flavor, honestly: "AI" in daily life means *mostly* large language models and the
  systems built around them. Distinguish three layers and label them all the time after:
  - **The model** (the pattern engine — the weights; expanded in [Section 4](#4-what-is-a-model-really-weights-training-the-internet-draft)),
  - **The harness** (the app/agent loop around it — [Section 11](#11-whats-a-harness-draft)),
  - **The tools & services** (everything the harness can call — [Sections 12–13](#12-whats-a-harness-tool-refine)).
- The "model ≠ product" gap: the same model, two different harnesses (bare chat vs.
  tool-enabled), produces visibly different behavior. This is the thread the rest of the
  workshop pays off.
- _(Instructor depth if asked "why 2026": see LocalLLMCopilot model inventory — same family,
  different builds, different measured behavior. The model is a moving target; the concept is stable.)_

### 2. What is a database _(draft)_

- The contrast anchor for everything LLM-related. A database is **structured, defined, and
  deterministic**: rows, columns, keys. Ask the same query twice → same answer, always.
  The rules of how data becomes an answer are *written and inspectable*.
- FRC-friendly version: a database is like a spreadsheet with a contract — you can always
  find out *why* an answer came back, because the path is logical.
- **Mini example:** a tiny customers table — the whole exhibit for this section:

  ```
  customerId | name        | age | location  | country
  ----------+-------------+-----+-----------+--------
  CUST-001   | Ava Chen    |  17 | Seattle   | USA
  CUST-002   | Kofi Mensah |  17 | Accra     | Ghana
  CUST-003   | Sofia Rossi |  16 | Milan     | Italy
  ```

  - Rows and columns with static values: ask for *the customer with ID CUST-002* and the
    answer is the same row, always — the value is *stored*, not *predicted*.
  - **Why `customerId` is there:** a real database identifies rows by a *unique* key. Names,
    ages, and cities can all repeat — the ID never does. It's how you point at one record
    without ambiguity, and what later joins and relationships hang on. (An LLM has no
    equivalent key: you can only *describe* what you want, which is part of why answers can
    come back plausible-but-wrong — [Section 10](#10-whats-a-hallucination-draft).)
  - Reused later: this same table is the "deterministic side" when we put the LLM side
    ([Section 3](#3-what-is-an-llm-draft)) next to it.
- _(Possible fold-in from v1: none. This replaces the old model-comparison slot with the
  actual comparison that matters: deterministic system vs. probabilistic system.)_

### 3. What is an LLM _(draft)_

- Like a database, it's a huge store of learned structure. **Not** like a database in how you
  get an answer out: you *describe* what you want, and it *predicts* an answer instead of
  *retrieving* one.
- The one honest sentence students should walk away with: **an LLM is a very fancy weighted
  pattern matcher that was trained by imitation and answers by prediction, not by lookup.**
- Same prompt twice → can get different answers. Same question, different month → can get a
  different answer (training data changed).
- The randomness is not an accident — it's a knob. See [Section 3a](#3a-temperature-the-determinism-knob-refine).

### 3a. Temperature: the determinism knob _(refine)_

- **What it is:** a number (typically 0–2) that controls how spread-out the model's
  next-token guesses are. Low = "commit to the most likely token"; high = "wander into the
  unlikely tokens too."
- **0.0** → near-locked. Same prompt, same answer nearly every time (the closest a model gets
  to deterministic — but a database is *always* the same, so they're still different animals).
- **2.0** → max spread. Even unlikely tokens win real odds, so output gets creative *and*
  sloppy.
- **0.7** → the semi-defacto default. Not locked, not wild — fluent, on-topic prose with a
  little human-feel variety. This is why chat-style products default near here.
- **Where you can (and can't) touch it:** OpenAI / Anthropic mask it (they bake in a fixed
  value per model / use case). Self-run local models (Ollama) expose it directly, and some
  clouds (e.g. Azure AI Foundry models) let you set it. So the knob is real even on the
  services that don't show you the dial.

### 4. What is a model, really? (weights, training, the internet) _(draft)_

Section 3 said "weighted pattern matcher" — this group makes *weights* real. "The model" is
the layer that gets sold, named, and benchmarked; everything else (harness, tools) is the
chassis around it.

- **What a model is:** math + a huge bag of numbers ([4a](#4a-the-brain-is-just-a-fileweights-refine)).
- **How the numbers got there:** a prediction-and-tweak loop run trillions of times
  ([4b](#4b-training-the-loop-that-wrote-the-weightsdraft)).
- **Why every 2026 model is similar (and different):** same raw data, different kitchens
  ([4c](#4c-same-ingredients-different-kitchensdraft)).
- **What using a model is, mechanically:** arithmetic on a fixed bag of saved numbers
  ([4d](#4d-feeding-the-weights-at-inferencerefine)).
- **How a number becomes an actual word:** the vocabulary list, end-to-end
  ([4e](#4e-how-does-a-number-become-a-word-vocabularyrefine)).
- **The whole engine in one loop:** every answer, built the same way — one word at a time
  ([4f](#4f-putting-it-all-together-how-one-answer-gets-builtdraft)).

### 4a. The "brain" is just a file (weights) _(refine)_

- A model = **billions of small numbers (the weights)** + a generic set of math operations
  (the "architecture"). All the "intelligence" lives in the numbers; the math that runs them
  is the same shape for anyone's model of that family.
- The weights *are* the product — and they're physically big: the models in this room are
  on the order of ~17 GB **even after compression** (LocalLLMCopilot's `ollama list` shows
  the exact per-model sizes).
- **The exhibit (the "database table" of the LLM world):** Section 2's database was a tidy
  little *display* — rows and columns with static values. The model's display doesn't exist
  as a table because the values aren't structured that way. The closest honest stand-in:

  ```
  qwen3.8:27b-q4_K_M   17 GB   (≈ 27 billion weights as numbers)
  ```

  vs. the LLM's full "display" — a flat blob of **~27 billion numbers**, with *no rows, no
  columns, no keys, no lookup*. Every piece of "knowledge" is dissolved into that mass
  (LocalLLMCopilot's `ollama list` numbers give the exact per-model sizes). The point isn't
  the size; it's the contrast:
  a database's display is organized so you can *point at* a fact; a model's display has
  nothing to point at — so you *describe* what you want and it *predicts*.

### 4b. Training: the loop that wrote the weights _(draft)_

1. Feed the model some text.
2. It predicts the next token (it will be wrong).
3. The mistake nips the weights a *hair* in the direction that would have made the right
   token more likely.
4. Repeat trillions of times, over as much text as the lab could scrape (mostly: the
   public-internet text, plus books and code).

- Result: the statistical structure of language — and the facts that rode along with it —
  gets **compressed into the numbers**. That's the whole training story, honestly told.
- **The "not memorizing" reframe (the one that sticks):** training isn't reading and storing
  the internet — it's like becoming a chef after cooking thousands of recipes. You no longer
  keep the cookbook *in your kitchen*, but the patterns are in your head, and you can
  improvise new dishes. Payoff ahead: because no book is stored inside, the model can't
  *look a fact up* — which is exactly why it's stale ([Section 9](#9-why-isnt-ai-currentdraft))
  and why it hallucinates ([Section 10](#10-whats-a-hallucination-draft)).

### 4c. Same ingredients, different kitchens _(draft)_

- The 2026 model families are all, in broad strokes, trained on **the same raw material** —
  so the differences between labs come from the *kitchen*, not the ingredients:
  - **The recipe** — architecture + scale (how the math is arranged, how many parameters):
      same data, different engine.
  - **The mix ratio** — data curation: how much code vs. books vs. conversation, what gets
      thrown out (low-quality pages, junk, NSFW). Each lab's "flair."
  - **The seasoning** — an alignment pass (preference tuning / RLHF) that shapes the *style
      and behavior* of answers, not the facts inside them.
- **Consequence for the room:** models from the same era share quirks and blind spots
  because they ate the same diet. "Try another model" sometimes helps and sometimes isn't
  different at all — different weights, similar food. (LocalLLMCopilot's measured inventory
  — same family, different builds, different behavior — is the proof if a student pushes.)

### 4d. Feeding the weights at inference _(refine)_

- Your prompt becomes tokens → number-vectors; the network runs the same matrix arithmetic
  against **all those stored weights**, layer after layer; out comes the score-per-next-token
  that [Section 5](#5-how-does-an-llm-work-if-it-isnt-deterministicdraft) runs with.
- So "using a model" = running arithmetic through a fixed bag of saved numbers. No lookup,
  no page-turn — the weights *are* the compressed knowledge, and the math is the same every
  time. (This is why one model behaves consistently: *your* prompt is the only varying input.)
- **Quantization** (the "Q4" in a model name): the weights start life as FP16 (16 bits per
  number), the "raw" brain — and it's *massive*. Q8 halves it, Q4 quarters it, in **memory
  and speed**. The catch isn't memory — it's the fear that "Q4 = ¼ of the brain." It **isn't:**
  quantization is *rounding* the weights to fewer digits (a lossy **compression**), not
  deleting knowledge. There's no region where "the France capital got rounded away" so the answer
  goes null. The loop (4f) mostly needs the weights' *ranking* — "big connection vs. small one" —
  not their exact last digits, so rounding shifts each score by dust that, across billions of
  weights, barely moves the final pick. (The `_K_M` in `Q4_K_M` is the extra safety: the few
  weights that matter most keep extra precision, the noise absorbs a coarser rounding.)
  **Bottom line a student taking home Ollama/LMStudio should hear:** Q4 ≈ **~98–99% of the
  behavior** at **¼ the RAM, ~3–4× faster** — a *slightly* dumber model, not a lobotomized one.
  It's exactly what makes a frontier-class model fit on a laptop at all.

### 4e. How does a number become a word? (vocabulary) _(refine)_

4d says "out comes a score-per-next-token" — but **which** next tokens? The model ships
with a **vocabulary**: a fixed list of *every* token it can ever produce (for current models,
tens of thousands of entries). That list is the number → word lookup:

```
vocabulary (fixed, baked into the model)
  token #91    → "what"     token #2210  → "capital"
  token #522   → "is"       token #1188  → "France"
  token #4401  → "the"      token #4402  → "Paris"
  …            (a few 10,000s total)
```

Now the whole answer, followable on one slide — a question every student
already knows the answer to, so nothing here needs checking:

```
user:      "what is the capital of France?"

1  tokens:          "what | is | the | capital | of | France | ?"
                    │ through THE vocabulary (word → slot)
2  numbers:         [91, 522, 4401, 2210, 187, 1188, 9]
                    │  the arithmetic of 4d (weights in, scores out)
3  scores:          "London" 2.1%  "Lyon" 1.3%  "Nice" 0.4%   "Paris" 95.0% …
                    ▲ it *scores EVERY token in the list*, picks the top
4  word out:        "Paris"
                    │ through the vocab again (slot → word)
next round repeats: "Paris" + history → "."
                    ─────────────────────────────────────────────
                    "what is the capital of France? Paris ."
```

- **Vocabulary ≠ knowledge.** The list is a pure *inventory* — "which tokens this model can
  output" (words, sub-word chunks, digits, punctuation), with zero meaning in it. The "France
  goes with Paris" association is not in the vocab; it's in the **weights**, learned from the
  co-occurrences in training text. There's no geography section, no fact table — every kind of
  "knowledge" (facts, grammar, coding, tone, reasoning) is one big shared statistical
  association space, held in those same weight numbers.
- **Why it correlates with *this* request:** "France" is in the input, and the model has
  seen "France" next to "Paris" countless times in its training text — in billions of the
  same sentences. Your question nudges the scores so "Paris" lands far above "London" and
  "Lyon" — the numbers do the job a database join would do.
- **The database tie-back (makes the whole section pay off):** the vocabulary is the LLM's
  nearest equivalent of Section 2's `customerId → name` lookup — a *fixed, inspectable*
  mapping of number → thing. The model's difference: the answer isn't retrieved from a
  stored row, it's *assembled one scored word at a time*, each round using that list. That
  is the entire "numbers → coherent thought" mechanism, honestly stated.
- Where this leaves the open questions: the *ranking* is where 3a (temperature) works and
  where Section 5 (non-determinism) lives — and where Section 10 (hallucination) sneaks in,
  because "high score" can still be "plausible but wrong."

### 4f. Putting it all together: how one answer gets built _(draft)_

The whole "how does it actually work" story in one place, start to finish. No side-trips and
no "trust me," because that is exactly what this section exists to avoid.

- **The cast is tiny — that's all there is:** a bag of learned numbers (the *weights*, 4a)
  that encode which words tend to appear together, plus one fixed list of every word it's
  allowed to say (the *vocabulary*, 4e). A question in, and the same **five steps repeat,
  one word at a time**, until the answer is done:

```
        ┌──────────────────────────────────────────────────────┐
        │  for EVERY word the model outputs:                   │
        │    1. take the whole conversation so far → numbers   │
        │    2. run the bag-of-numbers math on those numbers   │
        │    3. on the other side: a SCORE for every word in   │
        │       the entire vocabulary                          │
        │    4. pick a word (the scores decide which one)      │
        │    5. feed that word back in  →  repeat from 1       │
        └──────────────────────────────────────────────────────┘
        it stops when step 3 ranks the "end of answer" marker first
```

- **Follow the loop on one real question, top to bottom:**
  "what is the capital of France?" → numbers → scores → **"Paris"** wins (the rest of the
  world's capitals land far below) → "Paris" feeds back in → scores again → **"."** → the
  "end" marker wins → **stop.** Two words came out, and *each one* was produced by that
  identical five-step loop. Nothing else happened behind the scenes.

- **Every "weird" thing about AI is just that same loop wearing a different hat** — these
  aren't extra features, they fall straight out of the five steps:
  - **Temperature** is a knob on *step 4 only.* Low = always take the top scorer (always
    "Paris"). High = sometimes gamble on a low scorer (maybe "London"). Same scores,
    different strictness about how hard we respect them.
  - **It never invents a word** — *step 4* can only ever pick from that fixed list. That's
    why an answer always *sounds* like real language, even when it's wrong.
  - **It can be confidently wrong** — the loop emits the *most probable* next word, and the
    most probable word isn't always the *true* one. When the two disagree, the model says
    the one that merely *sounds* right. That **is** a hallucination: not a bug, just the
    direct consequence of building an answer by predicting the next word.

**One line to take away:** a bag of numbers, a word list, and a loop that runs once per word.
That is the entire engine — and there is nothing hidden behind it.

### 5. How does an LLM work if it isn't deterministic _(draft)_

- The "fancy word guesser" is a real starting point — build on it instead of over it:
  - Given a prompt, the model scores **every possible next word** (from its vocabulary).
  - It picks (weighted by probability — hence the knob from Section 3), appends it, re-scores, repeats.
  - That's the whole engine. Everything else is scaffolding around it.
- **"There's more to it," made concrete:**
  - **It's not one guess — it's billions of parameters doing arithmetic.** The "fancy" is
    that the weights encode statistical structure of language (and, incidentally, knowledge
    that let it *seem* to know things — which is also why it gets them wrong, [Section 10](#10-whats-a-hallucination-draft)).
  - **It's probabilistic, not logical.** Every step is a distribution, so small differences
    snowball — two nearly-equal paths can end in different answers. Databases converge;
    LLMs drift.
  - **It doesn't understand the way we do.** It has no fact store to query — "knowledge" is
    compressed into weights, which is why it can *sound* certain while being quietly wrong.
  - **(Optional, one sentence) it can also be steered — RLHF/preference tuning.** "Aligned"
    models are the same engine with an extra training pass on "what humans prefer." Mention,
    don't build.
- **The guessing made visible:** for every position in the prompt, the model ranks the
  possible next tokens by probability — look at just the top few and the "guessing" is
  right there in the numbers.
- _(Instructor depth: if a student asks "what's a Q4 weight?" — see
  [4d's quantization block](#4d-feeding-the-weights-at-inferencerefine) for the "rounding, not
  amputation" answer. LocalLLMCopilot's measured inventory backs it up.)_

### 6. What is a token _(draft)_

- The unit the model actually thinks in: a token is a chunk of text (roughly ¾ of a word in
  English, but a whole rare word, a punctuation mark, or half a name can also be one token).
- Why it matters in practice: **context, limits, and speed are all measured in tokens, not words.**
  Everything that comes after this section (limits, windows, costs) is denominated in tokens.
- A typical sentence breaks apart in surprising ways: words split on quotes, apostrophes,
  and hyphens; punctuation can even get its own token. So "The driver said 'let's go'!" does
  not map one-to-one onto its words at all.
- One number to plant: typical English ≈ 4 characters per token, roughly 0.75 tokens per word.
  They'll use this ratio the rest of the session.

### 7. What is AI context _(draft)_

- **Within a session/thread:** every model call sends the whole conversation (history) + the
  new message. The model has **no memory between calls** — "it remembered" is actually
  "the harness re-sent everything." This reframes the whole product experience: the chat
  transcript isn't memory, it's evidence we keep handing to a short-term brain.
- **Why parts get lost in long interactions:**
  - **The window is finite** → when the conversation outgrows it, *something* has to give.
  - **What gives, in harnesses:** older turns are **compressed/summarized** (the harness asks
    a model to shrink the history into a digest) or **dropped**. The summary *is* a lossy
    compression — like a high-compression JPEG, not a zipped file: the detail that's lost is
    gone for good, no amount of re-opening brings it back (a real ZIP loses nothing).
  - **The "lost in the middle" effect:** even when everything fits, attention to the very middle
    of a long prompt is weaker than to the start and end. So "it saw it" still can mean "it
    saw it but under-weighted it."
- **How we describe "compression" without lying:** the transcript becomes a *digest* —
  a smaller text that carries the gist but not the detail, exactly like you'd write on a
  whiteboard for the next shift: "we fixed the PID, still fighting the limelight."
- What it looks like in the wild: a harness with a deliberately small budget
  (LocalLLMCopilot documents the exact `PromptTokens` budget mechanics) hits its limit in a
  long conversation — and the truncation/summarization event is exactly where the degradation
  starts.

### 8. Context sizes and limits across models _(draft)_

- Every model advertises a **maximum context window** (in tokens). It's a hard ceiling, not a
  recommendation: prompt + expected output must fit, or the call fails / gets truncated.
- **Model ≠ one context size.** Same weights, different builds: LocalLLMCopilot's Qwen 3.8
  profiles document default / native-max / extended tags (98K / 262K / 393K / 786K) with
  different memory costs. Same brain, different notebook size — and a bigger notebook can
  cost real speed (measured: ~9% CPU offload and minutes of ingestion on the 393K profile,
  40+ minutes at 786K). In short: the window is a **fixed allowance, not free space** —
  everything put into it is paid for in memory and speed, every session.
- **Input vs output budgets:** the window is shared by *prompt* (history, instructions, tool
  results) and *completion* (the answer). Big-in + big-out needs a bigger tag than big-in alone.
- Rule of thumb to send home: **the model's window is an upper bound; the harness's budget
  is the real limit your session actually runs under.** (And: bigger window ≠ smarter answers —
  it just lets you put more on the table.)
- _("Same model, different box" made visible: the small vs. extended-context tags for the same
  model, side-by-side in `ollama list` / model metadata.)_

### 9. Why isn't AI current? _(draft)_

- **Because it was trained, not updated.** A model's knowledge is frozen at its training
  cutoff. Nothing about your session changes what it *knows* — changes what it can *see*.
- The clean split for students:
  - **Knew-at-train-time:** baked into the weights, never refreshed, can be confidently stale.
  - **Sees-at-runtime:** anything a tool hands it (web search, files, API responses) —
    fresh, but only because the *harness* fetched it, not the model.
- The punchline that pays off in Section 12: **a model with no tools can never be current;
  a model with the right tools is only as current as its sources.** Curation isn't a model
  feature — it's a harness feature.
- The pattern in miniature: ask about something from *this year* → the model misses or waffles.
  Re-ask through a web-search tool → the same model answers correctly. Same weights, different
  answer — the gap was the tool, not the brain. This is what makes Section 12 unavoidable.

### 10. What is a hallucination _(draft)_

- **Definition for the room:** a confident, fluent answer that isn't grounded in reality.
  Not a "mistake" the way a calculator wrong is — it's the *predicted* answer being
  plausible-but-false, because the engine (Section 5) optimizes for *plausible text,* and
  "sounds right" ≠ "is right."
- **Why it happens (tie back, don't re-derive):**
  - Knowledge is compressed into weights, so it can be *partially* recalled — like a memory
    that's 90% there and invents the 10%.
  - Training optimized for "keep going fluently," not "stop when you don't know."
  - No fact-checking step exists *inside* the model. (Everything external to it is Section 12.)
- **How we catch/handle it (the practical part students keep):**
  - Ask for a **source or cite**, then **check the citation.**
  - Ask it to **show its work** (reasoning / code) — verifiable artifacts beat asserted answers.
  - Use **tools** (search, DB, code execution) to ground facts instead of trusting weights.
  - **Two-model cross-check** for cheap high-stakes facts (two different engines disagreeing
    is a signal, even if neither is "right").
- **Reframe honesty:** hallucination isn't a bug to be fixed by "a smarter model." It's the
  *expected behavior of a predictive engine.* Your job (theirs, anyone's) is to build the
  verification, not wait for the model that never lies.
- _(Fold-in candidate: v1 Lab 4's hallucination-detection exercises, re-scoped as a 5-minute
  "find the buried false fact" game with the tool-enabled model. Decide at refine.)_

### 11. What is a harness _(draft)_

- **The model is the brain; the harness is the body.** The harness is the *system around the
  model* that: takes user input, assembles the context (history + system prompt + tool
  results), makes the API calls, runs the model's requested actions, feeds results back,
  and repeats until done.
- That "repeats until done" is what makes something **agentic** — the loop is the agent.
  One call = chatbot. Loop + tools = agent. (Now "agentic" has a definition the room can use.)
- Examples the students already know: Copilot CLI, Open WebUI, any `aider`/`claude`-style
  CLI. Different skins, same skeleton: **assemble → call → act → repeat.**
- **Why it matters (the thesis):** the *same model* behaves differently in different harnesses
  because the harness decides what the model sees, what it can do, and when it stops.
  "Model X is dumb" is often really "harness Y didn't give it the context/tools it needed."
- Same model / different harness (bare chat vs. tool-enabled), same task → different behavior.
  Re-pays the Section 1 setup.

### 12. What is a harness tool _(refine)_

- **A tool is a function the model can call.** The model never *executes* anything — it
  outputs a *request* (usually JSON: `tool_name(args)`). The **harness** runs it, gets the
  result, and **feeds the result back as context** for the next model call.
- Walk one tool call by hand, token by token:
  1. Model outputs `web_search("FRC 2026 rookie season results")`.
  2. Harness intercepts it, doesn't send it to a user — it *runs* it.
  3. Harness appends the search result to the conversation.
  4. Model reads its own "history" (which now includes the result) and answers.
- **The mental model students keep:** tools are how a brain with no hands gets hands. The model
  *decides*; the world (via the harness) *acts*. The loop from Section 11 is where this lives.
- **What a tool is NOT:** it's not the model "knowing" a thing. A tool is just a pipe to the
  outside world; the model's *knowledge* is still (Section 9) whatever it was trained on.
  This kills the "the AI *can* search the web" misconception — the *harness* can; the model
  just *asked* nicely.
- **Where we pull a real one from:** LocalLLMCopilot's full tool inventory (138–140 measured
  tools across built-ins, web, browser, and GitHub MCP) is the canonical list to reference when
  a student asks "what tools actually exist." We don't teach all of them — we teach *one* and
  let them know the rest are real.

### 13. What is MCP _(refine)_

- **The problem tools exposed:** every harness wanted tools, every app wanted to *be* a tool,
  and everyone was wiring them pair-by-pair. N harnesses × M apps = N×M integrations, hell.
- **MCP (Model Context Protocol):** a single standard so a tool/app writes its server *once*
  and *any* compatible harness can plug it in. N + M instead of N×M.
- **Who's who:**
  - **MCP server** = the thing that *exposes* capabilities (a GitHub server, a file server, a
    search server) and describes them (name, inputs, what it returns).
  - **MCP client** = the harness that *discovers* the server's tools and can call them (Copilot,
    Claude Desktop, any supported CLI).
  - The **model** talks to neither directly — the harness does (Section 12). The model only ever
    sees "a list of tools + their descriptions." MCP just makes that list *shareable and standard.*
- **Why it's the 2026 default for "extending AI to other sources":** it's the difference between
  a model trapped with its training-time data (Section 9) and one that can reach *live,
  external, current* data (GitHub, your files, the web, a DB). MCP is the *plumbing* that makes
  "closed, limited data → open, live sources" a matter of *adding a server*, not retraining.
- **The capability jump, concretely:** without tools, a model can only answer from frozen
  weights. With MCP, the same model can read *your* repo, *your* files, *live* pages — current
  where it used to be stale. That's the whole "extend capabilities from closed limited data
  to other sources" thesis in one breath.
- Attach an MCP server and its tools appear in the model's tool list — Section 12's
  walkthrough, now on an *external* server.
- _(Instructor depth: LocalLLMCopilot's benchmark is literally measuring tool-call reliability
  across an MCP tool inventory — how many of 95 GitHub MCP tools a model can actually call
  correctly. If students ask "how do we *know* tools work?", the answer is: you measure it,
  exactly like that repo does. Great credibility anchor.)_

### 14. What is a system prompt _(refine)_

- **The hidden first message.** Every conversation has a message the user never sees: the
  **system prompt**. It sets the model's role, tone, constraints, and rules for *this* session
  ("You are a careful code reviewer. Never run destructive commands. Answer in English.")
- **Why it's powerful:** it's the highest-authority instruction in the context — the model
  treats it as the framing for everything after. It's how the same base model becomes a
  friendly tutor in one app and a strict linter in another, *without changing weights at all*.
  (Same model, different harness → different system prompt → different "personality."
  Pays off Section 11's thesis again.)
- **What it is NOT:** it's not *extra* knowledge, and it's not *stronger than the model's
  training* in an absolute sense — it's a strong *bias* in context. A long, clever user prompt
  can bleed it (this is the seed of [prompt-injection, Section 17](#17-guided-failure-when-things-go-off-the-rails-draft)).
- **Concrete:** a system prompt is fully readable in the products they already use (Copilot /
  Open WebUI settings) — the same question, a different system prompt, and the model's
  behavior visibly changes.

### 15. Instructions and the system prompt _(refine)_

- **The relationship, stated plainly: they don't replace each other — they layer.**
  - The **system prompt** is the standing order: always active, sets the frame.
  - **Instructions** (a CLAUDE.md / AGENTS.md / project rules / "always do X") are *appended,
    merged, or injected into the context* by the harness, usually *on top of / alongside* the
    system prompt — so they *coexist*, not override.
  - The model gets **one big context** (system + instructions + history + your message) and
    weighs them all. There's no hard "system beats user" rule *inside the model* — it's all
    just weighted context, which is exactly why long, adversarial user text can *dilute or
    argue with* the system frame.
- **Order & precedence (the honest version):** different harnesses *present* them differently
  (some literally prepend the system prompt, some merge project instructions into it, some
  treat "developer" messages as higher-priority). The concept is stable — *all instructions
  live together in context and compete for the model's attention* — the exact wiring is a
  harness detail. Teach the concept; name the wiring when a student asks.
- **The practical takeaway students keep:** you *steer* a model with layered text, not by
  replacing anything. That's why a repo's `AGENTS.md` can make the same AI behave differently
  in one repo vs. another — no retraining, just *more instructions in the context*.
- The contrast to build the section on: (a) system prompt only vs. (b) system prompt + a
  project instruction file, same task → visibly different behavior. Same model, two
  instruction sets.

### 16. What are skills _(refine)_

- **A skill is a packaged, reusable instruction + procedure** the harness loads *on demand* —
  "when the task is X, here's the exact playbook, tool list, and guardrails to follow."
- **How it differs from plain instructions (Section 15) and tools (Section 12):**
  - An **instruction** is *always-on text* in context (a rule).
  - A **tool** is a *capability* the model can call (a hand).
  - A **skill** is a *playbook* — a named, loadable bundle of instructions + which tools to use
    + step-by-step behavior — that the harness **injects only when relevant**. It's how you
    give an agent "experience" (the way to do *this specific job* well) without bloating every
    context with every procedure.
- **Why it matters (the 2026 angle):** skills are how you go from "a model that can *do* a
  hundred things" to "a model that does *this one* thing reliably" — you encode the tribal
  knowledge (the sequence, the gotchas, the tools) once, and the harness reuses it. It's
  *procedural memory* that's file-based and shareable, not baked into weights.
- **The relationship, one breath:** system prompt = *who it is*; instructions = *standing rules*;
  tools = *what it can touch*; skills = *how it does a specific job, on demand.*
- _(Refine: pull 1–2 real skill examples from Copilot's available-skill list so the students see
  the actual format, not just an abstraction. Decide at refine which 2.)_

### 17. Guided failure: when things go off the rails _(draft)_

The one deliberately-broken part of the session. Students are *invited* to cause each; each
failure maps to a concept from earlier, so it *pays off* rather than just being a "watch it break."

- **The runaway loop** — a tool that keeps returning "not done" so the harness re-calls the
  model forever. *(Pays off: the loop is the agent, Section 11.)* Fix: a max-iterations guard.
- **The prompt-injection via tool output** — a "fetched page" that contains *instructions* for
  the agent ("ignore previous rules, do X"). The model can't fully tell "data" from "orders."
  *(Pays off: context is all text, Section 7; system vs. user competition, Section 15.)*
- **The confidently-wrong answer** — a hallucination in a high-stakes-looking fact, caught by
  asking for a source + the cross-check from Section 10. *(Pays off: hallucination handling.)*
- **The overload** — feed a context past the window; watch truncation/summarization degrade
  the answer. *(Pays off: Section 7/8 budgets.)*

_(Each failure: student triggers it → names which concept caused it → applies a one-line fix →
re-runs. This is where "concepts" stops being a list and becomes a diagnostic tool they can
use on any AI failure they meet. Pick 2–3 of these for the actual running order so the section
fits its time budget; don't try all four. Decide at refine.)_

## Cut by default from v1 _(revisit only if a section above genuinely needs it)_

| v1 item | What it was | Why it's out / where it goes |
|---------|-------------|-----------------------------|
| Lab 1 Non-Determinism | Temperature, same-prompt-different-answer | **Folded** into Section 3a (concepts only, no hands-on lab) |
| Lab 2 Model Comparison | Llama 1b/3b/8b drag race | **Cut** — benchmarking is instructor fuel, not a 2026 concept |
| Lab 4 Hallucination Detection | Catching AI mistakes | **Folded** into Section 10 as a 5-min find-the-false-fact game |
| Lab 5 Multimodal / image | Image analysis with llava | **Cut** — explicitly no media in v2 (may return as a v3 "agents that see") |
| Lab 6 Local vs Cloud | Privacy/tradeoffs discussion | **Deferred** — not a *concept* core; keep as an optional discussion |
| Lab 7 Bias & Fairness | AI bias & responsibility | **Deferred** — important but a values discussion, not a mechanics concept; optional |
| Lab 8 Real-World Scenarios | Practical problem-solving | **Superseded** by Section 17 guided failures |
| Lab 9 Agents & Tools | Capstone: web search + tools | **Folded** into Sections 11–13 (now concepts, not a one-off lab) |
| Instructor models (gemma/qwen/deepseek) | Large-vs-small model contrast | **Cut** from the program; available ad-hoc on demand |

> v1's `docker/` (both Open WebUI instances), `demos/token-prediction`, and `resources/`
> **stay around for ad-hoc use** (during or after the presenting, if someone asks): 3000/3001
> remain the base room setup, `resources/` (glossary, ethics, further-reading, whats-next)
> are on-demand references, and `demos/token-prediction` is there if a student pushes on the
> prediction mechanics. `docker/tools/` (port 3001) stands by for Sections 12/13 the same way.

## Option B: v1.5 — the old lab track (preservative option)

Option A (this document) is the concepts-first track. In case the room, the day-of energy, or
the schedule turns out to want the slower, hands-on-comparison version instead, the original
9-lab track remains fully intact under `labs/` with its own setup docs, and can be run:

- **As-is** — the original plan, unchanged.
- **As a second day or follow-up session** — v2 concepts in the morning, v1 labs as the
  hands-on afternoon. This is the strongest case for keeping it: students who already hold
  the concept ladder (v2) will extract far more from the comparison labs (v1).
- **As a v2 fallback** — if a v2 concept needs concrete backing on the day (server trouble
  with the tool-enabled stack, etc.), its v1 lab twin is the backfill.

Decision at refine time: keep this option documented, or fold v1 labs in as "extra credit"
materials for fast finishers. _(Default: keep as-is, zero maintenance.)_

## Open Decisions

1. **Session shape & per-section budget** — deliberately un-time-boxed for now; decide
   full-day vs. half-day (which sections, if any, drop) once content stabilizes.
2. **Which 2–3 failures to actually run in Section 17** (lean: runaway loop + injection + overload).
3. **Real skill examples for Section 16** — pick 2 from the live Copilot skill list at refine.
4. **Student language for any code** — Python (matches v1 + demos) or Java (matches FRC)? Lean: Python.
5. **Local-only vs. mix in a real API** — v2 teaches the industry shape (API) but runs locally
   for reliability/inspection. Lean: local Ollama only, framed as "the same API your cloud agent uses."
6. **Capstone?** The original v1 had one (Lab 9). v2 as written is *concepts* — do we add a
   short "build a tiny agent" wrap at the end, or end on Section 17 as-is? Decide once
   Section 13 lands.
7. **Is there a "what's next / where this is going" 5-min wrap?** (Keep tiny, links only —
   `resources/whats-next.md`. Don't let it become a history lesson.)

## Deck Generation

Once sections hit `lock`, generate the ppt deck from this file — mirroring the v1 pattern
(`generate_agentic_ai_101_workshop.py` → `Agentic_AI_101_Workshop.pptx`).

Plan: a new `v2/generate_workshopv2_deck.py` that walks this file's **locked** sections into
slides, output to `v2/AI_Workshop_V2.pptx`. v1's generator and deck stay untouched.

- Write the generator **only** when the first sections hit `lock` — not before — so we don't
  lock a generator to sections we're about to rewrite.
- The deck should read as the *concept ladder* (each slide leans on the previous), not a
  topic buffet. The status tags above are the deck's build order.
- **Presenter notes routing:** any `_(Instructor depth …)_` bullet is **presenter notes, not
  slide content.** It never appears on the slide face — it goes into the slide's notes pane,
  only visible to the presenter in Presenter View. In python-pptx that is a separate *notes
  slide* per slide, set via `slide.notes_slide.notes_text_frame.text = "…"` (accessing
  `notes_slide` auto-creates it). The rule for the generator: for each slide, body text =
  the section's non-italic bullets; `_(Instructor depth …)_` lines = that slide's
  `notes_slide`. If a slide has none, leave `notes_slide` unset (don't create an empty one).
  This tag is the single source of truth for "in the doc but not on the slide."
