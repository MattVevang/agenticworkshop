# 🃏 Model Baseball Cards

> **Gotta run 'em all!** This is your collector's guide to every AI model loaded on our workshop machine. Each model has different strengths, weaknesses, and personalities — just like baseball players on a roster. As you work through the labs, you'll get to try each one and see how they perform. Flip through these cards to learn what makes each model unique!

**🖥️ Our Hardware:** NVIDIA RTX 5090 · 32 GB VRAM · Running locally via [Ollama](https://ollama.com)

---

## 🦙 Llama 3.2 1B — *"The Speedster"*

> *"I'm not the smartest, but I'll be done before you finish reading this."*

| | |
|---|---|
| **Creator** | Meta |
| **Parameters** | 1.3 billion |
| **Disk Size** | 1.2 GB |
| **Personality** | The scrappy underdog — tiny but lightning fast |

### Stat Line

| ⚡ Speed | 🎯 Quality | 🎨 Creativity | 🧠 Reasoning |
|:---------:|:----------:|:--------------:|:------------:|
| ★★★★★ | ★★☆☆☆ | ★★☆☆☆ | ★☆☆☆☆ |

### 💪 Strengths

- **Blazing fast** — ~741 tok/s, responses appear almost instantly
- **Tiny footprint** — only 1.6 GB VRAM, leaves room for other models
- **Great for demos** — perfect for showing what a "small brain" looks like

### 😅 Weaknesses

- Frequently gets facts wrong or makes things up
- Struggles with anything requiring multi-step thinking

### 🎯 Best Workshop Use

Use Llama 3.2 1B in the **drag race** (Lab 2) to see what happens when an AI has very few parameters. Compare its answers to the 3B and 8B siblings to see how much size matters — all from the same Llama family.

### 📋 Used In

- **Lab 2** — Model Showdown: Llama Drag Race (Exercises 1, 2, 3, 4)
- **Lab 5** — Creative & Multimodal AI (Exercise 7: code quality comparison)

---

## 🦙 Llama 3.2 3B — *"The Workshop Default"*

> *"Small enough to be fast, big enough to be useful."*

| | |
|---|---|
| **Creator** | Meta |
| **Parameters** | 3 billion |
| **Disk Size** | 2.0 GB |
| **Personality** | The reliable sophomore — surprisingly capable for the size |

### Stat Line

| ⚡ Speed | 🎯 Quality | 🎨 Creativity | 🧠 Reasoning |
|:---------:|:----------:|:--------------:|:------------:|
| ★★★★☆ | ★★★☆☆ | ★★★☆☆ | ★★☆☆☆ |

### 💪 Strengths

- **Fast and capable** — ~424 tok/s, sweet spot between speed and smarts
- **Meta's latest small model** — benefits from cutting-edge training techniques
- **Low resource usage** — only 2.3 GB VRAM, leaves plenty of headroom
- **Great concurrent performance** — 5 simultaneous users under 1.4s

### 😅 Weaknesses

- Still trips up on complex reasoning or nuanced questions
- Can be repetitive in longer outputs

### 🎯 Best Workshop Use

This is the workshop's **default model**. When a lab says "pick a model" and you're not sure, llama3.2:3b is the go-to. It's fast, reliable, and handles everything from creative writing to code generation well enough for classroom use.

### 📋 Used In

- **Lab 1** — Non-Determinism (primary model)
- **Lab 2** — Model Showdown: Llama Drag Race (Exercises 1, 2, 3, 4)
- **Lab 3** — Prompt Engineering (suggested model)
- **Lab 5** — Creative & Multimodal AI (Parts 1 & Exercise 7)
- **Lab 7** — Bias and Fairness (suggested model)
- **Lab 8** — Real-World Scenarios (suggested model)
- **Lab 9** — Agents & Tools (the no-tools foil on port 3000)

---

## 🦙 Llama 3.1 8B — *"The Big Sibling"*

> *"Same family, bigger brain. You'll see the difference."*

| | |
|---|---|
| **Creator** | Meta |
| **Parameters** | 8 billion |
| **Disk Size** | 4.7 GB |
| **Personality** | The honors student — noticeably sharper than the younger siblings |

### Stat Line

| ⚡ Speed | 🎯 Quality | 🎨 Creativity | 🧠 Reasoning |
|:---------:|:----------:|:--------------:|:------------:|
| ★★★☆☆ | ★★★★☆ | ★★★★☆ | ★★★☆☆ |

### 💪 Strengths

- **Best quality in the Llama family lineup** — handles nuance, edge cases, and complex prompts
- **Still fast** — ~254 tok/s, plenty responsive for interactive use
- **Moderate VRAM** — 4.8 GB, easily fits alongside other models
- **Fair comparison** — same Llama family as the 1B and 3B

### 😅 Weaknesses

- Noticeably slower than the smaller siblings (the point of the drag race!)
- Not the best at deep math or multi-step logic puzzles

### 🎯 Best Workshop Use

Use Llama 3.1 8B as the "big" model in the **drag race** (Lab 2). It's the same family as the 1B and 3B, so when you compare quality, you know size is the main variable — not different training data or architecture.

### 📋 Used In

- **Lab 2** — Model Showdown: Llama Drag Race (Exercises 1, 2, 3, 4)

---

## 🌪️ Mistral 7B — *"The Hallucinator"*

> *"I'll confidently tell you things that never happened."*

| | |
|---|---|
| **Creator** | Mistral AI |
| **Parameters** | 7 billion |
| **Disk Size** | 4.4 GB |
| **Personality** | The confident storyteller — always has an answer, even when it shouldn't |

### Stat Line

| ⚡ Speed | 🎯 Quality | 🎨 Creativity | 🧠 Reasoning |
|:---------:|:----------:|:--------------:|:------------:|
| ★★★☆☆ | ★★★★☆ | ★★★★☆ | ★★★☆☆ |

**🌟 Bonus Stat:** 🤥 Hallucination — ★★★★★ (reliably makes things up when asked about fake topics)

### 💪 Strengths

- **Jack of all trades** — handles writing, questions, analysis, and more
- **Reliably hallucinates** — 100% hallucination rate on our validated fake prompts
- **Well-tested** — one of the most popular open-source models in the world

### 😅 Weaknesses

- States wrong things with absolute certainty (which is actually the point in Lab 4!)
- Not the best at deep math or multi-step logic puzzles

### 🎯 Best Workshop Use

Mistral is the **hallucination lab model**. It's specifically chosen for Lab 4 because it reliably generates confident but fictional content when asked about made-up topics — the Llama models are too cautious and catch the fakes.

### 📋 Used In

- **Lab 4** — Hallucination Detection (validated — reliably hallucinated on 100% of test prompts)

---

## 👁️ LLaVA 7B — *"The One Who Can See"*

> *"Send me a picture. I dare you."*

| | |
|---|---|
| **Creator** | LLaVA Team (University of Wisconsin–Madison) |
| **Parameters** | 7 billion |
| **Disk Size** | 4.7 GB |
| **Personality** | The specialist with a superpower — the only model that can look at images |

### Stat Line

| ⚡ Speed | 🎯 Quality | 🎨 Creativity | 🧠 Reasoning |
|:---------:|:----------:|:--------------:|:------------:|
| ★★★☆☆ | ★★★☆☆ | ★★★☆☆ | ★★★☆☆ |

**🌟 Bonus Stat:** 👁️ Vision — ★★★★☆

### 💪 Strengths

- **Multimodal!** — can analyze images, diagrams, screenshots, and photos
- **Unique ability** — the only model on our machine that can "see"
- **Surprisingly good** at describing what's happening in an image

### 😅 Weaknesses

- Text-only responses are not as strong as other models at the same size
- Can misread small details or text within images

### 🎯 Best Workshop Use

Use LLaVA whenever a lab involves **images**. It's the only model that can process visual input — upload a photo or diagram and ask it questions. This is your go-to for multimodal experiments.

### 📋 Used In

- **Lab 5** — Creative & Multimodal AI (Part 2: image analysis)

---

## 🧰 Qwen 3.6 35B — *"The Agent"*

> *"Hold on — let me look that up."*

| | |
|---|---|
| **Creator** | Alibaba (Qwen team) |
| **Parameters** | ~35 billion |
| **Disk Size** | ~24 GB |
| **Personality** | The resourceful one — the only model here that can reach *outside itself* |

### Stat Line

| ⚡ Speed | 🎯 Quality | 🎨 Creativity | 🧠 Reasoning |
|:---------:|:----------:|:--------------:|:------------:|
| ★★☆☆☆ | ★★★★★ | ★★★★☆ | ★★★★★ |

**🌟 Bonus Stat:** 🌐 Tools & Web Search — ★★★★★ (the only model that can call tools and search the live web)

### 💪 Strengths

- **Tool-capable** — supports *native function calling*, so it can decide to use tools on its own
- **Searches the live web** — answers current-events questions its training data can't possibly contain, with citations
- **Top-tier reasoning** — the strongest "thinker" on the machine, great at multi-step problems
- **Grounded answers** — can look something up and *confirm* it instead of guessing

### 😅 Weaknesses

- **The big one** — by far the largest model here, so it's noticeably **slower** and uses most of the GPU
- Tools only help when there's something to look up — for offline tasks the smaller models are plenty
- Like any model, it can still be wrong — always check the sources it cites

### 🎯 Best Workshop Use

This is the **star of [Lab 9: Agents & Tools](../labs/lab-09-agents-and-tools.md)**. It runs on the
**separate tool-enabled instance (port 3001)**, *not* the usual port-3000 dropdown. Use it to show
how a model with a **web-search tool** transforms from a "brain in a jar" into an **agent** that can
pull in real, current information — the big "AI isn't so dumb after all" reveal.

### 📋 Used In

- **Lab 9** — Agents & Tools (the tool-enabled model, on port 3001)

---

## 🗺️ Which Model Should I Use?

Not sure which model to pick? Use this quick decision chart:

```
🤔 What do you need?
│
├─ ⚡ "I need an answer RIGHT NOW"
│   └─➤ llama3.2:1b (lightning fast)
│
├─ 🤷 "I'm not sure / just exploring"
│   └─➤ llama3.2:3b (the safe default)
│
├─ 👁️ "I want to analyze an IMAGE"
│   └─➤ llava:7b (the only one that can!)
│
├─ 💻 "I need CODE or want quality + speed"
│   └─➤ llama3.2:3b (fast, good quality)
│
├─ 🤥 "I want to see AI HALLUCINATE"
│   └─➤ mistral:7b (reliably makes things up)
│
├─ 🧠 "I want the BEST quality"
│   └─➤ llama3.1:8b
│
├─ 🌐 "I need CURRENT info or web search"
│   └─➤ qwen3.6:35b — on the TOOLS instance, port 3001 (see Lab 9)
│
└─ 🏎️ "I want to COMPARE model sizes"
    └─➤ Try the same prompt on 1B → 3B → 8B!
```

### Quick Reference Table

| Model | Size | Speed | Best For | Vibe |
|-------|------|-------|----------|------|
| `llama3.2:1b` | 1.2 GB | 🐇🐇🐇 | Speed demos, drag race small | The scrappy underdog |
| `llama3.2:3b` | 2.0 GB | 🐇🐇 | **Default workshop model** — general use | The reliable workhorse |
| `llama3.1:8b` | 4.7 GB | 🐇 | Drag race large, quality | The big sibling |
| `mistral:7b` | 4.4 GB | 🐇 | Hallucination lab (Lab 4 only) | The confident storyteller |
| `llava:7b` | 4.7 GB | 🐇 | Image analysis (multimodal) | The one with eyes |
| `qwen3.6:35b` | ~24 GB | 🐢 | Web search + tools — **port 3001** (Lab 9) | The agent |

> 🧰 **Note:** `qwen3.6:35b` runs on the **separate tool-enabled instance (port 3001)**, so it
> won't appear in the normal port-3000 model dropdown — it's used only in Lab 9. See
> [`docker/tools/README.md`](../docker/tools/README.md).

### ⚡ Benchmark Data (RTX 5090, 32 GB VRAM)

| Model | Avg Response | 5 Users Concurrent | Tokens/sec | VRAM |
|-------|-------------|-------------------|-----------|------|
| `llama3.2:1b` | 0.3s | max 1.1s | ~741 | ~1.6 GB |
| `llama3.2:3b` | 0.5s | max 1.4s | ~424 | ~2.3 GB |
| `llama3.1:8b` | 0.8s | max 2.5s | ~254 | ~4.8 GB |
| `mistral:7b` | 1.1s | max 1.1s | ~257 | ~8.3 GB |
| `llava:7b` | ~1.5s | — | ~250 | ~8.4 GB |

> 💡 Cold-load from NVMe: **~1–1.5 seconds** for any model. VRAM persistence is NOT needed for fast responses.

### 💾 Total VRAM Budget: 32 GB

Our RTX 5090 has 32 GB of VRAM. With workshop tuning (`OLLAMA_MAX_LOADED_MODELS=2`), up to 2 models share VRAM at once — Ollama automatically unloads the oldest model when a new one is needed. Cold loads from NVMe take only ~1 second, so students won't notice the swap.

---

*Now go collect some experiences with each model! The best way to learn is to try the same question on different models and compare. 🃏✨*
