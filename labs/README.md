# 🤖 Agentic AI 101 — Lab Exercises

Welcome to the hands-on lab portion of the workshop! In these labs, you'll interact directly with real AI models running **locally** on a server in this room — no cloud, no OpenAI, no data leaving the building.

---

## 🖥️ Getting Started: Accessing OpenWebUI

1. **Open your browser** (Chrome, Firefox, or Edge all work)
2. **Navigate to**: `http://[server-ip]:3000`
   > Your instructor will share the exact IP address.
3. **Log in** with the credentials provided by your instructor
4. You should see the **OpenWebUI chat interface** — it looks similar to ChatGPT

### Quick UI Walkthrough

| UI Element | What It Does |
|---|---|
| **Model Dropdown** (top of chat) | Select which AI model to talk to — this is important! Different labs use different models |
| **New Chat** button (sidebar or ➕ icon) | Starts a fresh conversation — **use this between exercises** |
| **Message box** (bottom) | Type your prompts here and hit Enter or click Send |
| **Chat history** (left sidebar) | Your past conversations are saved here |
| **Settings** ⚙️ | Access advanced options like temperature (we'll use this in Lab 1) |

### Available Models

These are the models loaded on the server that you can use:

| Model | Size | Best For |
|---|---|---|
| `tinyllama:1.1b` | 🟢 Tiny (1.1B params) | Speed demos, seeing what a tiny model can do |
| `llama3.2:3b` | 🟡 Small (3B params) | Quick general tasks |
| `mistral:7b` | 🟠 Medium (7B params) | Solid all-around performance |
| `qwen3.5:9b` | 🟠 Medium (9B params) | Strong general tasks |
| `deepseek-r1:14b` | 🔴 Large (14B params) | Reasoning and analysis |
| `llava:7b` | 🟠 Medium (7B params) | **Multimodal** — can analyze images! |
| `phi4:14b` | 🔴 Large (14B params) | Microsoft's model, good at code and reasoning |

> **💡 Tip:** Bigger ≠ always better. Part of this workshop is learning *when* to use which model.

---

## 📋 Lab Overview

| Lab | Title | Time | Type |
|---|---|---|---|
| [Lab 1](lab-01-non-determinism.md) | AI is NOT a Calculator | 15–20 min | Hands-on |
| [Lab 2](lab-02-model-comparison.md) | Model Showdown | 15–20 min | Hands-on |
| [Lab 3](lab-03-prompt-engineering.md) | The Art of Asking | 20 min | Hands-on |
| [Lab 4](lab-04-hallucination-detection.md) | Catching AI Lies | 20 min | Hands-on |
| [Lab 5](lab-05-creative-and-multimodal.md) | Creative & Multimodal AI | 20 min | Hands-on |
| [Lab 6](lab-06-local-vs-cloud-discussion.md) | Local vs. Cloud AI | 15 min | Discussion |

---

## ⚠️ Ground Rules

1. **Start a new chat** for each exercise unless told otherwise — this keeps things clean and prevents the model from using previous context
2. **Copy prompts exactly** when the lab says to — small changes can lead to very different results (which is actually one of the things you'll learn!)
3. **Don't share personal information** with the models — even though these run locally, it's a good habit
4. **Have fun and be curious** — there are no wrong answers here. The goal is to explore and understand how these tools work

---

## 🆘 Need Help?

- **Model isn't responding?** Try refreshing the page or selecting the model again from the dropdown
- **Response is really slow?** The larger models take more time — that's expected and part of what you'll explore
- **Getting errors?** Flag down your instructor

Ready? Start with **[Lab 1: AI is NOT a Calculator →](lab-01-non-determinism.md)**
