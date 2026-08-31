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

## Late additions

### Grounding and tempering expectations

What is AI today? (fancy word guesser)

- It is an algorithm which attempts to perform an activity
- It is always triggered via some human action and follows its programming to perform
- that task.
  - It never just decides to do something on its own.  

What is AGI

- Insert definition of AGI
  - Sub text as applicable

Circle of money explained?

- Candid but find example image of the cash flow happening today between tech companies (the circular diagram where money is in this endless circle)

Comparison image of Azure services regarding the broad scope of Azure vs AI
  
- No AI is like another and they the things we have today as we know them are not the same
  - Something that OpenAI does well or poorly is not guaranteed to be the same with Anthropic for example
- Models all of which do something different from others
- Tools and harnesses all of which do something different from others
- Each company doing something typically has their own herbs and seasoning on something

Imagine the array of AI tools out there to physical ones like a hammer in your workbench.

- They all can hit something to some degree but some may hit harder and some do a better job or you learn the feel of the tool
in the hand after use and you can do better work with the same tool

Do you use AI today?

- Do you ever use spell check while writing a document or email?
- Have you ever searched for something online?
- ^ those may not feel like AI but those two are systems that use an algorithm.

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
2. **Concrete over abstract.** Each section lands as a specific, self-contained situation
   students can picture and re-verify themselves later — no hands-on lab, no live demo.
3. **One idea per section, in load order.** No section assumes a later one.
4. **Failures are content.** The ways things actually go off the rails (overloaded context,
   stale knowledge, malformed tool call) are taught as concepts and diagnostic patterns —
   what breaks, why, and the usual fix. Not as activities to run in the room.
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
> `> TODO (…)` blocks are instructions to the deck builder — never rendered as slides.
> **Audience contract:** the room has *no* prior LLM/agent experience (see Audience &
> Constraints — "Assume NOT"). Never claim students "already use" or "already know" a tool
> in this doc; say "the tools they'll meet" or name the product without asserting history.
> **Term discipline:** one term per concept, reused exactly — e.g., **compression**
> (lossy compression) is *the* word for summarizing history; never introduce synonyms
> (no "digest") that dilute the reinforced message.

### 1. What is AI (as of 2026) _(draft)_

- Working definition for the room: software that takes in information, uses patterns learned
  from data, and produces something useful from it: a prediction, recommendation, decision,
  or new content.
- The 2026 flavor this workshop focuses on is large language models and the systems built
  around them. AI is broader than LLMs, but these are the tools behind today's chat and
  coding assistants. Distinguish three layers and label them all the time after:
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
  designed for deterministic retrieval**: rows, columns, keys. Ask the same query against
  the same stored data → the same answer. The rules of how data becomes an answer are
  *written and inspectable*.
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
    answer is the same stored row — the value is *retrieved*, not *predicted*.
  - **Why `customerId` is there:** a real database can enforce a *unique* key. Names,
    ages, and cities can all repeat — this ID is defined not to. It's how you point at one
    record without ambiguity, and what later joins and relationships hang on. (An LLM has no
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
- Same prompt twice → can get different answers. The same product can also answer differently
  later because its model, instructions, tools, or data sources changed.
- The randomness is not an accident — it's a knob. See [Section 3a](#3a-temperature-the-determinism-knob-refine).

### 3a. Temperature: the determinism knob _(refine)_

- **What it is:** a decoding setting that controls how willing the system is to choose a
  less-likely next token. Low = "stay close to the highest scores"; high = "give the lower
  scores more of a chance."
- **Low temperature** → usually more repeatable and focused. Even a setting of 0 does not
  promise byte-for-byte identical answers every time.
- **High temperature** → more variation, which can mean more creativity and more mistakes.
- **The dial is not universal:** its range, default, and availability depend on the model
  and provider. Local runtimes such as Ollama commonly expose it; cloud APIs may expose,
  restrict, or ignore it for a particular model.

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

- A model = **billions of small numbers (the weights)** arranged inside a particular set of
  math operations (the "architecture"). The learned behavior is encoded in those numbers
  and in how the architecture uses them.
- The weights *are* the product — and they're physically big: the models in this room are
  on the order of ~17 GB **even after compression** (LocalLLMCopilot's `ollama list` shows
  the exact per-model sizes).
- **The exhibit (the "database table" of the LLM world):** Section 2's database was a tidy
  little *display* — rows and columns with static values. The model's display doesn't exist
  as a table because the values aren't structured that way. The closest honest stand-in:

  ```
  qwen3.8:27b-q4_K_M   17 GB   (≈ 27 billion weights as numbers)
  ```

  vs. the LLM's full "display" — **~27 billion numbers**, organized for the model's math but
  not as human-readable rows, keys, or facts. Every piece of "knowledge" is spread through
  that structure (LocalLLMCopilot's `ollama list` numbers give the exact per-model sizes).
  The point isn't the size; it's the contrast: a database is organized so you can *point at*
  a stored fact. A model has no `France → Paris` row to retrieve, so you *describe* what you
  want and it *predicts*.

### 4b. Training: the loop that wrote the weights _(draft)_

1. Feed the model some text.
2. It predicts the next token (it will be wrong).
3. The mistake nips the weights a *hair* in the direction that would have made the right
   token more likely.
4. Repeat on a huge training mixture that may include public text, licensed material,
   books, code, human examples, and synthetic examples.

- Result: the statistical structure of language — and the facts that rode along with it —
  gets **compressed into the numbers**. That's the whole training story, honestly told.
- **The "not a searchable copy" reframe (the one that sticks):** training isn't building a
  library where the model can reopen the original pages — it's like becoming a chef after
  cooking thousands of recipes. The patterns are in your head, and you can improvise new
  dishes, but you cannot point to the exact cookbook page. Models can memorize occasional
  examples, but they still have no reliable fact lookup. That's why they can be stale
  ([Section 9](#9-why-isnt-ai-currentdraft)) and hallucinate
  ([Section 10](#10-whats-a-hallucination-draft)).

### 4c. Same ingredients, different kitchens _(draft)_

- The 2026 model families draw from **many overlapping kinds of raw material**, but no two
  labs publish or use exactly the same mixture. Their differences come from both the
  ingredients and the *kitchen*:
  - **The recipe** — architecture + scale (how the math is arranged, how many parameters):
      similar task, different engine.
  - **The mix ratio** — data curation: how much code vs. books vs. conversation, what gets
      thrown out (low-quality pages, junk, NSFW). Each lab's "flair."
  - **The seasoning** — post-training (preference tuning / RLHF and related methods) that
      shapes style, safety, reasoning behavior, tool use, and when the model says "I don't know."
- **Consequence for the room:** models from the same era share quirks and blind spots
  because they ate the same diet. "Try another model" sometimes helps and sometimes isn't
  different at all — different weights, similar food. (LocalLLMCopilot's measured inventory
  — same family, different builds, different behavior — is the proof if a student pushes.)

### 4d. Feeding the weights at inference _(refine)_

- Your prompt becomes tokens → number-vectors; the network runs the same matrix arithmetic
  against **all those stored weights**, layer after layer; out comes the score-per-next-token
  that [Section 5](#5-how-does-an-llm-work-if-it-isnt-deterministicdraft) runs with.
- So "using a model" = running arithmetic through a fixed bag of saved numbers. No lookup,
  no page-turn — the weights hold learned patterns, while your prompt and the surrounding
  system decide what the model does with them.
- **Quantization** (the "Q4" in a model name): model weights are normally created and run at
  higher precision. Quantization rounds many of those numbers to fewer digits - a lossy
  **compression**, not deleting a quarter of the model's knowledge. There is no region where
  "the capital of France" gets cut out. Lower-precision files use much less weight memory and
  can run faster, although total RAM and speed also depend on context size, hardware, and the
  runtime. **Bottom line for a student taking home Ollama/LM Studio:** Q4 is usually a practical
  trade - a much smaller model file with some possible quality loss, not a lobotomized model.
  It is what makes many otherwise-too-large models usable on ordinary hardware.

### 4e. How does a number become a word? (vocabulary) _(refine)_

4d says "out comes a score-per-next-token" — but **which** next tokens? The model ships
with a **vocabulary**: a fixed list of the text pieces and special markers it can output.
That list is the number → token lookup:

```
vocabulary (fixed, baked into the model)
  token #91    → "what"     token #2210  → "capital"
  token #522   → "is"       token #1188  → "France"
  token #4401  → "the"      token #4402  → "Paris"
  …            (the total depends on the model)
```

Now the whole answer, followable on one slide — a question every student
already knows the answer to, so nothing here needs checking:

```
user:      "what is the capital of France?"

1  tokens:          "what | is | the | capital | of | France | ?"
                    │ through THE vocabulary (token → slot)
2  numbers:         [91, 522, 4401, 2210, 187, 1188, 9]
                    │  the arithmetic of 4d (weights in, scores out)
3  scores:          "London" 2.1%  "Lyon" 1.3%  "Nice" 0.4%   "Paris" 95.0% …
                    ▲ it *scores EVERY token in the list*, then chooses one
4  token out:       "Paris"
                    │ through the vocab again (slot → token)
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
  learned a very strong relationship between "France," "capital," and "Paris" from its
  training examples. Your question nudges the scores so "Paris" lands far above "London" and
  "Lyon" — the numbers do the job a database join would do.
- **The database tie-back (makes the whole section pay off):** the vocabulary is the LLM's
  nearest equivalent of Section 2's `customerId → name` lookup — a *fixed, inspectable*
  mapping of number → thing. The model's difference: the answer isn't retrieved from a
  stored row, it's *assembled one scored token at a time*, each round using that list. That
  is the entire "numbers → coherent thought" mechanism, honestly stated.
- Where this leaves the open questions: the *ranking* is where 3a (temperature) works and
  where Section 5 (non-determinism) lives — and where Section 10 (hallucination) sneaks in,
  because "high score" can still be "plausible but wrong."

### 4f. Putting it all together: how one answer gets built _(draft)_

The whole "how does it actually work" story in one place, start to finish. No side-trips and
no "trust me," because that is exactly what this section exists to avoid.

- **The simplified cast is tiny:** a bag of learned numbers (the *weights*, 4a), the model's
  architecture that runs the math, and one fixed vocabulary of tokens it can choose from
  (4e). A question goes in, and the same **five steps repeat, one token at a time**, until
  the answer is done:

```
        ┌──────────────────────────────────────────────────────┐
        │  for EVERY token the model outputs:                  │
        │    1. take the whole conversation so far → numbers   │
        │    2. run the bag-of-numbers math on those numbers   │
        │    3. on the other side: a SCORE for every token in  │
        │       the entire vocabulary                          │
        │    4. choose a token using those scores              │
        │    5. feed that token back in  →  repeat from 1      │
        └──────────────────────────────────────────────────────┘
        it stops when step 3 ranks the "end of answer" marker first
```

- **Follow the loop on one real question, top to bottom:**
  "what is the capital of France?" → numbers → scores → **"Paris"** wins (the rest of the
  world's capitals land far below) → "Paris" feeds back in → scores again → **"."** → the
  "end" marker wins → **stop.** Two visible tokens came out, and *each one* was produced by
  that identical five-step loop.

- **Every "weird" thing about AI is just that same loop wearing a different hat** — these
  aren't extra features, they fall straight out of the five steps:
  - **Temperature** influences *step 4.* Low = stay near the top scorers. High = give lower
    scorers more of a chance. Same scores, different strictness about how closely to follow them.
  - **It builds from fixed pieces** — *step 4* can only pick tokens from the vocabulary, but
    several tokens can combine into a new word, name, or code identifier.
  - **It can be confidently wrong** — the loop emits a probable next token, and the
    probable continuation isn't always the *true* one. When the two disagree, the model says
    the one that merely *sounds* right. That **is** a hallucination: not a bug, just the
    direct consequence of building an answer by predicting the next token.

**One line to take away:** learned numbers, a token list, and a prediction loop that runs
once per token. That is the useful mental model for how an answer is generated.

### 5. How does an LLM work if it isn't deterministic _(draft)_

- The "fancy word guesser" is a real starting point — build on it instead of over it:
  - Given a prompt, the model scores **every possible next token** (from its vocabulary).
  - It picks (weighted by probability — how spread out those odds are can be dialed, which is
    the whole temperature story), appends it, re-scores, repeats.
  - That's the core generation loop. The transformer architecture is what creates those scores.
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
- One number to plant: typical English ≈ 4 characters or 0.75 words per token - equivalently,
  about 1.33 tokens per word. It varies by model and text, but it is a useful rough estimate.

### 7. What is AI context _(draft)_

- **Within a session/thread:** the model has **no automatic memory between independent calls**.
  The product must make earlier information available again - commonly by re-sending messages,
  referencing stored conversation state, or retrieving saved memory. "It remembered" is
  really "the system supplied that information again." The transcript is not memory inside
  the weights; it is evidence repeatedly handed to a short-term brain.
- **Why parts get lost in long interactions:**
  - **The window is finite** → when the conversation outgrows it, *something* has to give.
  - **What gives, in harnesses:** older turns may be **compressed/summarized**, selectively
    retrieved, or dropped. Compression is lossy - like a high-compression JPEG, not a zipped
    file: details that were not preserved may be unavailable later.
  - **The "lost in the middle" effect:** many models have more trouble retrieving details from
    the middle of a long prompt than from the start or end. So "it fit in the window" does not
    always mean "the model used every detail equally well."
- **How we describe "compression" without lying:** older state becomes a *smaller
  representation* - often compressed text carrying the gist but not every detail, like you'd
  write on a whiteboard for the next shift: "we fixed the PID, still fighting the limelight."
- _(Instructor depth: what it looks like in the wild — a harness with a deliberately small
  budget (LocalLLMCopilot documents the exact `PromptTokens` budget mechanics) hits its limit
  in a long conversation, and the truncation/summarization event is exactly where the
  degradation starts.)_

### 7a. The Bob example: why the model "forgets" _(refine)_

- **The memory beat:** you tell a session, "My name is Bob." A few messages later you ask,
  "What is my name?" → **Bob.** That looks like memory. It isn't memory inside the model -
  the system supplied "My name is Bob" again as part of the session state.
- **The long-session beat:** then you do hours of back-and-forth coding. The transcript
  outgrows the window, so the harness **compresses** the old turns to stay under budget.
  The compression chases what the conversation has been about: hours of code → build
  errors and decisions survive, "My name is Bob" does not — like shift handover notes
  that say "PID fixed, still fighting the limelight" and never mention anyone's name.
- **The come-back beat:** you ask again, "What is my name?" The model has genuinely no idea.
  Not a mood swing — the sentence no longer exists in the context it receives, and it can't
  know what it isn't given.
- **What it means:** "forgetting" isn't the brain failing; it's the transcript. The
  compression keeps what looks important *to the conversation so far* — so facts that
  matter to you (a name, a preference, a constraint) matter to the model only while you
  keep saying them.

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
> **TODO (later-me — deck production, screenshot):** the "same model, different box" exhibit.
> Do **not** use a live or local `ollama list` — it differs per machine, so it wouldn't match
> the room. Instead screenshot the **Copilot CLI's model list**: every student's list is the
> same one, so anyone who goes home and opens it themselves sees exactly what we did. Place
> that screenshot as a static exhibit on the **next slide**.

### 9. Why isn't AI current? _(draft)_

- **Because a deployed model's weights are trained, then fixed.** Your conversation does not
  rewrite them. It changes what the model can *see now*, not what is baked into that model version.
- The clean split for students:
  - **Knew-at-train-time:** baked into the weights, never refreshed, can be confidently stale.
  - **Sees-at-runtime:** anything a tool hands it (web search, files, API responses) —
    fresh, but only because the *harness* fetched it, not the model.
- **The asterisk, because this is where "AI isn't current" misleads:** the never-current
  claim is about **the model by itself**, not **the services people actually open.** The online
  AI tools students will use (Copilot, ChatGPT, and the like) may bundle web search and similar
  tools, sometimes invoking them automatically, so the answer on your screen **can be current**
  even though the model underneath still has knowledge frozen months or years back. What a
  student touches is almost
  never the bare model — it's the service that wraps it: *fresh at the edges, stale at the core*.
  Both are true at once; the core — the baked-in, un-updated part — is the one to stay skeptical
  of, because it's the one that can be confidently wrong in the ways [Section 10](#10-whats-a-hallucination-draft) describes.
- The punchline that pays off in Section 12: **a model cannot independently fetch current
  information without an outside input path.** A user can paste in today's information, or
  a harness can retrieve it with tools - and the answer is only as current as those sources.
  Curation isn't a model feature; it is a system and source-selection feature.
- The pattern in miniature: ask about something from *this year* → the model misses or waffles.
  Re-ask through a web-search tool → the same model answers correctly. Same weights, different
  answer — the gap was the tool, not the brain. This is what makes Section 12 unavoidable.

### 10. What is a hallucination _(draft)_

- **Definition for the room:** an answer that sounds plausible but is false or unsupported
  by the evidence available to it. It may sound confident, but confidence is not required.
  It is not a "mistake" in the same way as entering the wrong equation into a calculator -
  it is the *predicted* answer being
  plausible-but-false, because the engine (Section 5) optimizes for *plausible text,* and
  "sounds right" ≠ "is right."
- **Why it happens (tie back, don't re-derive):**
  - Knowledge is compressed into weights, so it can be *partially* recalled — like a memory
    that's 90% there and invents the 10%.
  - Training optimized for "keep going fluently," not "stop when you don't know."
  - No fact-checking step exists *inside* the model. (Everything external to it is Section 12.)
- **How we catch/handle it (the practical part students keep):**
  - Ask for a **source or cite**, then **check the citation.**
  - Ask for **verifiable work**: code you can run, calculations you can repeat, or claims you
    can trace to a real source. A generated explanation by itself is not proof.
  - Use **tools** (search, DB, code execution) to ground facts instead of trusting weights.
  - **A second model can be a warning signal**, especially when the answers disagree, but
    agreement is not independent proof. Both models can share the same bad assumption.
- **Reframe honesty:** better models and grounding can reduce hallucinations, but no current
  model makes verification unnecessary. Your job (theirs, anyone's) is to verify important
  output, not wait for the model that never lies.

### 11. What is a harness _(draft)_

- **The model is the brain; the harness is the body.** The harness is the *system around the
  model* that: takes user input, assembles the context (history + system prompt + tool
  results), makes the API calls, runs the model's requested actions, feeds results back,
  and repeats until done.
- That "repeats until done" loop is the most common shape of something **agentic**: the
  system pursues a goal across multiple steps, often using tools and deciding what to do next.
  The loop is part of the harness; the configured goal-seeking system is the agent.
- The names they'll actually meet: Copilot CLI, Open WebUI, any `aider`/`claude`-style
  CLI. Different skins, same skeleton: **assemble → call → act → repeat.**
- **Why it matters (the thesis):** the *same model* behaves differently in different harnesses
  because the harness decides what the model sees, what it can do, and when it stops.
  "Model X is dumb" is often really "harness Y didn't give it the context/tools it needed."
- Same model / different harness (bare chat vs. tool-enabled), same task → different behavior.
  That's the same-model-different-behavior thread from the opening of this whole workshop —
  now the room knows exactly what keeps it.

### 12. What is a harness tool _(refine)_

- **A tool is a function the model can request.** The model never *executes* anything — it
  outputs a structured request (often represented like `tool_name(args)`). The **harness**
  decides whether to allow it, runs it, gets the
  result, and **feeds the result back as context** for the next model call.
- Walk one tool call by hand, token by token:
  1. Model outputs `web_search("FRC 2026 rookie season results")`.
  2. Harness intercepts it, doesn't send it to a user — it *runs* it.
  3. Harness appends the search result to the conversation.
  4. Model reads its own "history" (which now includes the result) and answers.
- **The mental model students keep:** tools are how a brain with no hands gets hands. The model
  proposes; the harness permits and acts. The loop from Section 11 is where this lives.
- **What a tool is NOT:** it's not the model "knowing" a thing. A tool is just a pipe to the
  outside world; the model's *knowledge* is still (Section 9) whatever it was trained on.
  This kills the "the AI *can* search the web" misconception — the *harness* can; the model
  just *asked* nicely.
- **Where we pull a real one from:** use the live Copilot CLI session as the exhibit when a
  student asks "what tools actually exist." The exact count changes with CLI version,
  permissions, enabled features, and MCP servers. We don't teach all of them - we teach *one*
  and let them see that the rest are real.

### 12a. A real inventory: the tools a harness actually mounts _(refine)_

- **Receipts, not abstraction:** the Copilot CLI exposes a real tool inventory. The exact
  names vary by version and configuration, but the capabilities fall into a few recognizable
  families - each one something the model itself cannot perform:

```
family                        representative tools
─────                         ────────────────────
shell execution               powershell, plus session start/read/stop
file operations               view · search · glob · apply_patch
web and external services     web fetch/search · browser · MCP tools
agent and task delegation     task · read_agent · write_agent · list_agents
specialized workflows         skills · code review · user approval
```

- **The depiction for this text-and-code workshop:** `view("config.py")` isn't the model
  opening a file by itself - it emits a structured request; the CLI's process does the reading,
  and the returned excerpt enters the model's context. Modern models can also accept other
  content types, but the same rule holds: they see only what the surrounding system supplies.
- **"How does it read files I've never showed it?" — trace `grep` end-to-end:**
  1. user: *"why is the build failing?"*
  2. model → `grep("ERROR", "build.log")` — that's *text* (a tool-call request).
  3. harness runs grep on the local machine; matching lines **come back into the context**.
  4. model reads them: *"the failure is in X, line 42"* → next call: `view("X", near 42)`.
  5. harness returns those lines; model → `edit(...)`; the result is fed back; it verifies.
  The file lives on the machine, **not in the model's weights**.
  The model "understands" it only because each tool result becomes new context for the next
  call, and it can keep iterating as long as it keeps calling. *That* iterate loop is what
  "agentic" means, mechanically.
- **The boundary:** only the excerpts returned by the tool enter the model's context; the
  unreturned parts of the local file do not. Repeated request → result rounds let it act on
  the file without permanently training that file into the weights. New *capability* is
  mounted by the harness, not retrained into the model.
- **It is inspectable:** the CLI's help and environment views show what is available in that
  session. The inventory is evidence of the model-versus-harness distinction, not a permanent
  master list that is identical on every machine.
  _(Instructor depth: use the current CLI help/reference and the room's configured session as
  the source of truth for the day of the workshop.)_

### 13. What is MCP _(refine)_

- **The problem tools exposed:** every harness wanted tools, every app wanted to *be* a tool,
  and everyone was wiring them pair-by-pair. N harnesses × M apps = N×M integrations, hell.
- **MCP (Model Context Protocol):** a shared standard so a tool/app can expose its capabilities
  once and compatible AI hosts can connect to it. The goal is closer to N + M reusable pieces
  than N×M custom pairings, even though authentication and configuration still take work.
- **Who's who:**
  - **MCP server** = the thing that *exposes* capabilities (a GitHub server, a file server, a
    search server) and describes them (name, inputs, what it returns).
  - **MCP host/client** = the AI application and its connection that discover and call those
    capabilities (Copilot, Claude Desktop, or another supported application).
  - The **model** talks to neither directly — the host does (Section 12). The model sees only
    the capabilities and results the host chooses to supply. MCP makes that connection
    *shareable and standard.*
- **Why it is a major 2026 standard for extending AI to other sources:** it helps connect a
  model to *live, external, current* data (GitHub, your files, the web, a DB). MCP is the
  *plumbing* that makes
  "closed, limited data → open, live sources" a matter of *adding a server*, not retraining.
- **The capability jump, concretely:** without tools, a model can only answer from frozen
  weights. With MCP, the same model can read *your* repo, *your* files, *live* pages — current
  where it used to be stale. That's the whole "extend capabilities from closed limited data
  to other sources" thesis in one breath.
- Attach and approve an MCP server, and the host can add its capabilities to what the model
  may use - Section 12's walkthrough, now backed by an *external* server.
- _(Instructor depth: LocalLLMCopilot's benchmark measures tool-call reliability across a
  versioned MCP inventory. If students ask "how do we *know* tools work?", the answer is:
  you measure it against the exact tool set and version, just like that repo does.)_

### 14. What is a system prompt _(refine)_

- **The highest-level session instructions.** Most AI products supply a **system prompt** or
  equivalent instructions that the user may not see. It sets the model's role, tone,
  constraints, and rules for *this* session
  ("You are a careful code reviewer. Never run destructive commands. Answer in English.")
- **Why it's powerful:** it's the highest-authority instruction in the context — the model
  treats it as the framing for everything after. It's how the *exact same model, in the
  exact same harness*, becomes a friendly tutor under one system prompt and a strict
  linter under another — *without changing weights at all*. Same model, same harness,
  different system prompt → different "personality."
- **What it is NOT:** it's not *extra* knowledge and it is not a security boundary by itself.
  Models can still fail to follow higher-authority instructions, which is why the harness
  also needs permissions and guardrails. This is the seed of
  [prompt injection, Section 17](#17-guided-failure-when-things-go-off-the-rails-draft).
- **Concrete:** when a product lets you view or edit these instructions - such as a locally
  controlled Open WebUI setup - the same question with a different system prompt produces
  visibly different behavior. Commercial products may keep some instructions hidden.

### 15. Instructions and the system prompt _(refine)_

- **The relationship, stated plainly: they don't replace each other — they layer.**
  - The **system prompt** is the higher-authority standing order: it sets the frame.
  - **Instructions** (a CLAUDE.md / AGENTS.md / project rules / "always do X") are loaded
    into the context by the harness at the authority level that product assigns them. They
    coexist with the system prompt rather than replacing it.
  - The model gets layered context (system + project instructions + history + your message),
    but the platform assigns those layers different authority. A user message is not supposed
    to override a higher-authority system rule, even though models can still fail to follow it.
- **Order & precedence (the honest version):** different harnesses expose different roles and
  wire project instructions differently. The stable concept is that instructions are layered,
  some layers outrank others, and the exact hierarchy is a harness/provider detail.
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
  - An **instruction** is a rule the harness loads when its scope applies.
  - A **tool** is a *capability* the model can call (a hand).
  - A **skill** is a *playbook* — a named, loadable bundle of instructions + which tools to use
    + step-by-step behavior — that the harness **injects only when relevant**. It's how you
    give an agent "experience" (the way to do *this specific job* well) without bloating every
    context with every procedure.
- **Why it matters (the 2026 angle):** skills are how you go from "a model that can *do* a
  hundred things" to "a model that does *this one* thing more consistently" — you encode the
  tribal knowledge (the sequence, the gotchas, the tools) once, and the harness reuses it. It's
  *procedural memory* that's file-based and shareable, not baked into weights.
- **The relationship, one breath:** system prompt = *who it is*; instructions = *standing rules*;
  tools = *what it can touch*; skills = *how it does a specific job, on demand.*
- _(Refine: pull 1–2 real skill examples from Copilot's available-skill list so the students see
  the actual format, not just an abstraction. Decide at refine which 2.)_

### 17. Guided failure: when things go off the rails _(draft)_

The ways things actually go off the rails — and why. These are real failure modes students
will meet in the wild, outside this room; each maps to a concept from earlier, so the list
doubles as a **diagnostic**: when something goes wrong, which concept explains it, and what
does the fix usually look like.

- **The runaway loop** — a tool that keeps returning "not done" so the harness re-calls the
  model forever. An agent loop needs an explicit reason to stop. Fix: a max-iterations guard,
  time budget, or other stopping rule.
- **The prompt-injection via tool output** — a "fetched page" that contains *instructions* for
  the agent ("ignore previous rules, do X"). Platforms do have higher- and lower-authority
  instruction channels, but a model can still mistake untrusted data for an order or fail to
  respect the boundary. Fix: treat tool output as untrusted, restrict permissions, validate
  proposed actions, and require approval for consequential changes.
- **The confidently-wrong answer** — a hallucination in a high-stakes-looking fact, caught
  by asking the model for its source and cross-checking it against something real.
- **The overload** — a context pushed past its fixed window: truncation or summarization
  kicks in, and the answer degrades.

**The whole section's payoff:** this is a diagnostic list — when something in the wild goes
off the rails, a student can name which concept explains it, and what the fix usually looks
like.

## Cut by default from v1 _(revisit only if a section above genuinely needs it)_

| v1 item | What it was | Why it's out / where it goes |
|---------|-------------|-----------------------------|
| Lab 1 Non-Determinism | Temperature, same-prompt-different-answer | **Folded** into Section 3a (concepts only, no hands-on lab) |
| Lab 2 Model Comparison | Llama 1b/3b/8b drag race | **Cut** — benchmarking is instructor fuel, not a 2026 concept |
| Lab 4 Hallucination Detection | Catching AI mistakes | **Folded** into Section 10 (concept only: spotting and verifying AI errors — no hands-on piece) |
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
- **`> TODO (…)` blocks are production instructions, not content.** They tell the deck
  builder what to do (e.g. insert a screenshot on the next slide) — they are never rendered
  onto a slide face or into notes.
- **Presenter notes routing:** any `_(Instructor depth …)_` bullet is **presenter notes, not
  slide content.** It never appears on the slide face — it goes into the slide's notes pane,
  only visible to the presenter in Presenter View. In python-pptx that is a separate *notes
  slide* per slide, set via `slide.notes_slide.notes_text_frame.text = "…"` (accessing
  `notes_slide` auto-creates it). The rule for the generator: for each slide, body text =
  the section's non-italic bullets; `_(Instructor depth …)_` lines = that slide's
  `notes_slide`. If a slide has none, leave `notes_slide` unset (don't create an empty one).
  This tag is the single source of truth for "in the doc but not on the slide."
