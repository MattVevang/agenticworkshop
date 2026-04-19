# 💰 Local vs Cloud AI: Cost Comparison

> **For students in the Agentic AI 101 Workshop**
>
> Ever wonder what it actually *costs* to use AI? Let's break it down — cloud APIs vs running your own local setup. 🤓

---

## 🔑 Key Concept: What's a Token?

Before we talk money, remember: AI companies charge by **tokens**, not words. A token is roughly ¾ of a word. So 1,000 tokens ≈ 750 words — about 1.5 pages of text.

When you chat with an AI:
- **Input tokens** = what you send (your prompt)
- **Output tokens** = what the AI sends back (its response)

Output tokens cost more because the AI is doing the hard work of *generating* them. 🧠

---

## ☁️ Cloud API Pricing (Per 1 Million Tokens)

These are the prices companies charge developers who use AI through their APIs (the behind-the-scenes connection).

### OpenAI (ChatGPT models)

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Notes |
|-------|----------------------|------------------------|-------|
| GPT-4o | $2.50 | $10.00 | Popular all-rounder |
| GPT-4o mini | $0.15 | $0.60 | Budget-friendly 💸 |
| o3-mini | $1.10 | $4.40 | Reasoning model |

### Anthropic (Claude models)

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Notes |
|-------|----------------------|------------------------|-------|
| Claude Opus | $15.00 | $75.00 | Most powerful (💰💰💰) |
| Claude Sonnet | $3.00 | $15.00 | Great balance |
| Claude Haiku | $0.25 | $1.25 | Fast and cheap ⚡ |

### Google (Gemini models)

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Notes |
|-------|----------------------|------------------------|-------|
| Gemini 2.5 Pro | $1.25–$2.50 | $10.00–$15.00 | Scales with context |
| Gemini 2.5 Flash | $0.15 | $0.60 | Budget champ 🏆 |

---

## 🎒 Real-World Example: A Homework Session

Let's say you're working on an essay and go back-and-forth with an AI for about 20 minutes. A typical session might use roughly **5,000 tokens** — maybe 3,000 input + 2,000 output.

### What would that cost with different APIs?

| Model | Input Cost (3K tokens) | Output Cost (2K tokens) | **Total** |
|-------|----------------------|------------------------|-----------|
| GPT-4o | $0.0075 | $0.0200 | **$0.028** |
| GPT-4o mini | $0.0005 | $0.0012 | **$0.002** |
| Claude Sonnet | $0.0090 | $0.0300 | **$0.039** |
| Claude Haiku | $0.0008 | $0.0025 | **$0.003** |
| Gemini 2.5 Flash | $0.0005 | $0.0012 | **$0.002** |

### How to calculate it yourself 🧮

```
Cost = (input_tokens ÷ 1,000,000) × input_price
     + (output_tokens ÷ 1,000,000) × output_price

Example with Claude Sonnet:
  Input:  (3,000 ÷ 1,000,000) × $3.00  = $0.009
  Output: (2,000 ÷ 1,000,000) × $15.00 = $0.030
  Total:  $0.009 + $0.030 = $0.039
```

Seems cheap, right? But it adds up. If you did **10 sessions a day** with Claude Sonnet, that's ~$0.39/day → ~$12/month → ~$142/year. And that's just *one person*. 📈

---

## 🆓 Free Tiers — What You Get for $0

Most cloud AI services offer free tiers. Here's what's available (as of 2025):

| Service | Free Tier | Limitations |
|---------|-----------|-------------|
| **ChatGPT** (OpenAI) | ✅ Free plan available | Limited GPT-4o access, slower during peak times |
| **Claude** (Anthropic) | ✅ Free plan available | Limited messages per day, no API access |
| **Gemini** (Google) | ✅ Free plan available | Generous free tier, integrated with Google apps |
| **Copilot** (Microsoft) | ✅ Free plan available | Built into Bing, Edge, and Windows |
| **Meta AI** (Meta) | ✅ Free | Powered by Llama, available in Meta apps |
| **Perplexity** | ✅ Free plan available | Limited "Pro" searches per day |

**The catch?** Free tiers give you the *consumer* product, not the API. They're great for casual use but come with limits, and the company can see and potentially train on your data. 👀

---

## 🖥️ Local AI: Our Workshop Server

Here's what our setup looks like:

| Component | Spec | Approx. Cost |
|-----------|------|-------------|
| **GPU** | NVIDIA RTX 5090 (32 GB VRAM) | ~$2,000 |
| CPU, RAM, Motherboard, PSU, Storage | Server-grade components | ~$1,500 |
| **Total Build** | | **~$3,500** |

### Amortized Cost (Spreading It Out) 📊

If this server runs for **3 years** (a reasonable lifespan):

| Timeframe | Cost |
|-----------|------|
| Per year | ~$1,167 |
| Per month | ~$97 |
| Per day | ~$3.20 |

**But here's the thing:** that's the cost no matter how much or how *little* you use it. Whether you run 1 prompt or 10,000 prompts in a day, the hardware cost is the same.

Add in **electricity** (~$0.50–$1.00/day running the GPU under load), and your daily cost is roughly **$3.50–$4.00/day**.

### Cost Per Homework Session (Local) 🏠

If 25 students each do a homework session (5K tokens) in a single day:
- That's 125,000 tokens total — easily handled by the RTX 5090
- Daily hardware cost: ~$3.50
- **Cost per student per session: ~$0.14**

If the server handles **100 sessions/day** (busy day):
- **Cost per session: ~$0.035** — about the same as cheap cloud APIs!

And the more you use it, the cheaper each session gets. 📉

---

## ⚖️ The Big Comparison

| Factor | ☁️ Cloud API | 🖥️ Local (Our Server) |
|--------|------------|----------------------|
| **Upfront cost** | $0 | ~$3,500 |
| **Per-session cost** | $0.002–$0.04 | ~$0.03–$0.14 (amortized) |
| **Scales with usage** | 📈 More use = more $ | 📉 More use = cheaper per session |
| **Free tiers** | ✅ Available (with limits) | ✅ Unlimited after purchase |
| **Privacy** | ⚠️ Data sent to company servers | ✅ Data stays in this room |
| **Model quality** | 🟢 Best models available | 🟡 Good, but smaller models |
| **Internet required** | ✅ Yes, always | ❌ Nope, fully offline |
| **Maintenance** | None (they handle it) | Someone needs to manage it |
| **Best for** | Casual users, top-tier quality | Privacy, education, heavy use |

---

## 💡 The Bottom Line

- **For casual users**: Cloud free tiers are unbeatable. ChatGPT, Claude, and Gemini all offer solid free plans. You literally pay nothing. 🎉
- **For developers**: Cloud APIs are cheap per-call but **add up fast** at scale. A startup running millions of tokens/day can spend thousands per month.
- **For privacy-conscious use**: Local AI wins. Your data never leaves the room. Period. 🔒
- **For learning and experimentation**: Local AI lets you poke around, break things, and understand how models actually work — no rate limits, no bills, no surprise charges.

> 🎯 **Our workshop server runs for free after the hardware purchase!**
>
> Once the RTX 5090 server is built and sitting in this room, every prompt you run costs essentially nothing extra. No subscriptions, no per-token charges, no surprise bills. Just electricity and vibes. ⚡😎

---

## ⚠️ Important Notes

- **Prices change rapidly!** AI pricing is a moving target. These numbers are approximate as of **mid-2025**. By the time you read this, they may have already dropped.
- **Cloud pricing usually gets cheaper over time** as competition increases.
- **Local hardware gets more powerful** — today's $2,000 GPU will be outperformed by a $500 GPU in a few years.
- **The real cost comparison depends on your use case.** There's no single right answer — that's what makes this interesting to think about! 🤔

---

*📚 This resource is part of the [Agentic AI 101 Workshop](../README.md). See also: [Glossary](glossary.md) | [Further Reading](further-reading.md)*
