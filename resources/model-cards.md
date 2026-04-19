# 🃏 Model Baseball Cards

> **Gotta run 'em all!** This is your collector's guide to every AI model loaded on our workshop machine. Each model has different strengths, weaknesses, and personalities — just like baseball players on a roster. As you work through the labs, you'll get to try each one and see how they perform. Flip through these cards to learn what makes each model unique!

**🖥️ Our Hardware:** NVIDIA RTX 5090 · 32 GB VRAM · Running locally via [Ollama](https://ollama.com)

---

## 🏎️ TinyLlama 1.1B — *"The Speedster"*

> *"I'm not the smartest, but I'll be done before you finish reading this."*

| | |
|---|---|
| **Creator** | TinyLlama Project |
| **Parameters** | 1.1 billion |
| **Disk Size** | 637 MB |
| **Personality** | The scrappy underdog — tiny but lightning fast |

### Stat Line

| ⚡ Speed | 🎯 Quality | 🎨 Creativity | 🧠 Reasoning |
|:---------:|:----------:|:--------------:|:------------:|
| ★★★★★ | ★★☆☆☆ | ★★☆☆☆ | ★☆☆☆☆ |

### 💪 Strengths

- **Blazing fast** — responses appear almost instantly
- **Tiny footprint** — barely uses any GPU memory, leaving room for bigger models
- **Great for demos** — perfect for showing what a "small brain" looks like

### 😅 Weaknesses

- Frequently gets facts wrong or makes things up
- Struggles with anything requiring multi-step thinking

### 🎯 Best Workshop Use

Use TinyLlama when you want to see what happens when an AI has very few parameters. It's the "control group" — compare its answers to bigger models to see how much size matters.

### 📋 Used In

- **Lab 2** — Model Showdown (Exercises 1, 2, 4)
- **Lab 5** — Creative & Multimodal AI (Exercise 7: code quality comparison)

---

## 🦙 Llama 3.2 3B — *"The Balanced Rookie"*

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

- **Fast and capable** — a sweet spot between speed and smarts
- **Meta's latest small model** — benefits from cutting-edge training techniques
- **Low resource usage** — leaves plenty of VRAM headroom

### 😅 Weaknesses

- Still trips up on complex reasoning or nuanced questions
- Can be repetitive in longer outputs

### 🎯 Best Workshop Use

A great step up from TinyLlama — use this when you want quick answers that are noticeably better without waiting around. Perfect for rapid experimentation.

### 📋 Used In

- **Lab 2** — Model Showdown (Exercises 1, 3)

---

## 🌪️ Mistral 7B — *"The All-Star"*

> *"Need something done? I'm your model."*

| | |
|---|---|
| **Creator** | Mistral AI |
| **Parameters** | 7 billion |
| **Disk Size** | 4.4 GB |
| **Personality** | The reliable veteran — solid at everything, star at nothing specific |

### Stat Line

| ⚡ Speed | 🎯 Quality | 🎨 Creativity | 🧠 Reasoning |
|:---------:|:----------:|:--------------:|:------------:|
| ★★★☆☆ | ★★★★☆ | ★★★★☆ | ★★★☆☆ |

### 💪 Strengths

- **Jack of all trades** — handles writing, questions, analysis, and more
- **Great quality-to-size ratio** — punches above its weight class
- **Well-tested** — one of the most popular open-source models in the world

### 😅 Weaknesses

- Not the best at deep math or multi-step logic puzzles
- Can occasionally hallucinate confidently (states wrong things with certainty)

### 🎯 Best Workshop Use

This is the workshop's **default model**. When a lab says "pick a model" and you're not sure, Mistral is a safe bet. It's the baseline we compare other models against.

### 📋 Used In

- **Lab 1** — Non-Determinism (primary model)
- **Lab 2** — Model Showdown (Exercises 1, 2, 4)
- **Lab 3** — Prompt Engineering (suggested model)
- **Lab 4** — Hallucination Detection (suggested model)
- **Lab 5** — Creative & Multimodal AI (Parts 1 & Exercise 7)

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

- Text-only responses are not as strong as Mistral at the same size
- Can misread small details or text within images

### 🎯 Best Workshop Use

Use LLaVA whenever a lab involves **images**. It's the only model that can process visual input — upload a photo or diagram and ask it questions. This is your go-to for multimodal experiments.

### 📋 Used In

- **Lab 5** — Creative & Multimodal AI (Part 2: image analysis)

---

## 🧪 Qwen 3.5 9B — *"The Brain"*

> *"Let me think about that... okay, here's a thorough answer."*

| | |
|---|---|
| **Creator** | Alibaba Cloud |
| **Parameters** | 9 billion |
| **Disk Size** | 6.6 GB |
| **Personality** | The honor student — methodical, thorough, and annoyingly good |

### Stat Line

| ⚡ Speed | 🎯 Quality | 🎨 Creativity | 🧠 Reasoning |
|:---------:|:----------:|:--------------:|:------------:|
| ★★★☆☆ | ★★★★☆ | ★★★★☆ | ★★★★☆ |

### 💪 Strengths

- **Strong reasoning** — handles logic, analysis, and multi-step problems well
- **High-quality writing** — produces clear, well-structured responses
- **Versatile** — great at creative tasks AND analytical ones

### 😅 Weaknesses

- Slower than the smaller models — you'll notice the wait
- Uses more VRAM, so it takes a moment to load

### 🎯 Best Workshop Use

Reach for Qwen when you need **quality answers** — especially for exercises that test reasoning, analysis, or structured writing. It's the model to beat in head-to-head comparisons.

### 📋 Used In

- **Lab 2** — Model Showdown (Exercises 3, 4)
- **Lab 3** — Prompt Engineering (suggested model)
- **Lab 4** — Hallucination Detection (suggested model)
- **Lab 5** — Creative & Multimodal AI (Parts 1 & 3)

---

## 🔗 DeepSeek-R1 14B — *"The Thinker"*

> *"Hold on, let me reason through this step by step..."*

| | |
|---|---|
| **Creator** | DeepSeek |
| **Parameters** | 14 billion |
| **Disk Size** | 9.0 GB |
| **Personality** | The philosopher — shows its work and thinks out loud |

### Stat Line

| ⚡ Speed | 🎯 Quality | 🎨 Creativity | 🧠 Reasoning |
|:---------:|:----------:|:--------------:|:------------:|
| ★★☆☆☆ | ★★★★☆ | ★★★☆☆ | ★★★★★ |

**🌟 Bonus Stat:** 🔗 Chain-of-Thought — ★★★★★

### 💪 Strengths

- **Chain-of-thought reasoning** — literally shows you its thinking process in `<think>` tags
- **Excellent at logic and math** — the best reasoner on our machine
- **Educational gold** — students can watch *how* an AI thinks, not just what it says

### 😅 Weaknesses

- **Slow** — all that thinking takes time, especially for complex problems
- Responses can be very long because it includes its reasoning steps
- Not the best at creative or casual conversation

### 🎯 Best Workshop Use

Use DeepSeek-R1 when you want to **see an AI think**. Its chain-of-thought output is fascinating — you can literally watch it reason through problems step by step. Amazing for understanding *how* AI models solve problems.

### 📋 Used In

- **Lab 2** — Model Showdown (Exercises 1, 3, 4)

---

## 💻 Phi-4 14B — *"The Coder"*

> *"Describe what you want. I'll write the code."*

| | |
|---|---|
| **Creator** | Microsoft |
| **Parameters** | 14 billion |
| **Disk Size** | 9.1 GB |
| **Personality** | The tech nerd — happiest when writing code or solving technical problems |

### Stat Line

| ⚡ Speed | 🎯 Quality | 🎨 Creativity | 🧠 Reasoning |
|:---------:|:----------:|:--------------:|:------------:|
| ★★☆☆☆ | ★★★★☆ | ★★★☆☆ | ★★★★☆ |

**🌟 Bonus Stat:** 💻 Code — ★★★★★

### 💪 Strengths

- **Excellent at code generation** — Python, JavaScript, HTML/CSS, and more
- **Strong technical reasoning** — great at explaining how things work
- **Microsoft's training data** — benefits from extensive code and STEM datasets

### 😅 Weaknesses

- **Slow** — 14B parameters means longer wait times
- Can be overly technical or verbose in non-code responses

### 🎯 Best Workshop Use

Phi-4 is your go-to for anything **code-related**. When a lab asks you to generate, debug, or explain code, Phi-4 will give you the best results. Also great for STEM questions.

### 📋 Used In

- **Lab 2** — Model Showdown (Exercises 2, 4)
- **Lab 5** — Creative & Multimodal AI (Part 3: code generation)

---

## 🗺️ Which Model Should I Use?

Not sure which model to pick? Use this quick decision chart:

```
🤔 What do you need?
│
├─ ⚡ "I need an answer RIGHT NOW"
│   └─➤ tinyllama:1.1b
│
├─ 🤷 "I'm not sure / just exploring"
│   └─➤ mistral:7b (the safe default)
│
├─ 👁️ "I want to analyze an IMAGE"
│   └─➤ llava:7b (the only one that can!)
│
├─ 💻 "I need CODE"
│   └─➤ phi4:14b
│
├─ 🧠 "I have a hard LOGIC or MATH problem"
│   └─➤ deepseek-r1:14b
│
├─ ✍️ "I need high-quality WRITING or ANALYSIS"
│   └─➤ qwen3.5:9b
│
├─ ⚖️ "I want good quality but faster"
│   └─➤ llama3.2:3b
│
└─ 🔬 "I want to COMPARE models"
    └─➤ Try the same prompt on 2-3 different models!
```

### Quick Reference Table

| Model | Size | Speed | Best For | Vibe |
|-------|------|-------|----------|------|
| `tinyllama:1.1b` | 637 MB | 🐇🐇🐇 | Speed demos, baseline comparison | The scrappy underdog |
| `llama3.2:3b` | 2.0 GB | 🐇🐇 | Quick experiments, fast iteration | The balanced rookie |
| `mistral:7b` | 4.4 GB | 🐇 | General use, the default pick | The reliable all-star |
| `llava:7b` | 4.7 GB | 🐇 | Image analysis (multimodal) | The one with eyes |
| `qwen3.5:9b` | 6.6 GB | 🐢 | Quality writing & reasoning | The honor student |
| `deepseek-r1:14b` | 9.0 GB | 🐢🐢 | Chain-of-thought, logic, math | The philosopher |
| `phi4:14b` | 9.1 GB | 🐢🐢 | Code generation, STEM | The tech nerd |

### 💾 Total VRAM Budget: 32 GB

Our RTX 5090 has 32 GB of VRAM. Only one model runs at a time (by default), and Ollama handles loading/unloading automatically. Bigger models use more VRAM and take a few seconds longer to load — but once they're running, they stay in memory until you switch.

---

*Now go collect some experiences with each model! The best way to learn is to try the same question on different models and compare. 🃏✨*
