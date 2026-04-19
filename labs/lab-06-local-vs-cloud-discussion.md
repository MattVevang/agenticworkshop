# ☁️ Lab 6: Local vs. Cloud AI

## Learning Objectives

By the end of this lab, you will:
- ✅ Understand the difference between **local AI** and **cloud AI**
- ✅ Be able to evaluate tradeoffs across **privacy, cost, speed, and quality**
- ✅ Make informed decisions about when to use each approach
- ✅ Think critically about **who sees your data** when you use AI tools

⏱️ **Estimated Time:** 15 minutes

📋 **Lab Type:** Discussion & worksheet (no prompting exercises)

---

## 🧠 Background: Two Ways to Run AI

Everything you've been doing today uses **local AI** — the models run on a physical server right here in this room. Your prompts never leave the building.

But most AI tools you've probably heard of — ChatGPT, Google Gemini, Claude, Copilot — are **cloud AI**. When you type a prompt, it travels over the internet to a data center, gets processed on powerful hardware, and the response comes back.

Both approaches work. Both have tradeoffs. Let's explore them.

### How It Works

```
LOCAL AI                          CLOUD AI
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│   You     │───▶│  Server  │    │   You     │───▶│ Internet │───▶│   Data   │
│  (laptop) │◀───│ (in room)│    │  (laptop) │◀───│          │◀───│  Center  │
└──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
  Your data stays here             Your data goes... somewhere
```

---

## The Comparison

| Dimension | 🏠 Local AI | ☁️ Cloud AI |
|---|---|---|
| **Privacy** | ✅ Data never leaves your network | ⚠️ Data sent to third-party servers |
| **Cost** | 💰 Hardware purchase upfront, then free to run | 💸 Pay per use (API) or monthly subscription |
| **Model Quality** | 🟡 Limited by your hardware (1B–14B params today) | 🟢 Access to largest models (100B+ params) |
| **Speed** | ⚡ No network latency, but limited by local GPU | 🔄 Network latency, but very powerful hardware |
| **Offline Use** | ✅ Works without internet | ❌ Requires internet connection |
| **Customization** | ✅ Full control — choose any open model, fine-tune | 🟡 Limited to what the provider offers |
| **Setup Difficulty** | 🔧 Requires technical setup | ✅ Just sign up and start |
| **Latest Models** | 🟡 Usually a few weeks/months behind | ✅ Access to bleeding-edge models immediately |
| **Scalability** | ❌ Limited by your hardware | ✅ Can handle huge workloads |

---

## Exercise 1: The Scenario Game 🎲

For each scenario below, decide: would **local AI** or **cloud AI** be the better choice? There's not always one right answer — discuss the tradeoffs.

### Scenario A: 🏥 Hospital Patient Records

> A hospital wants to use AI to analyze patient medical records and suggest possible diagnoses to help doctors work faster.

| Your Choice | Local / Cloud / Either |
|---|---|
| **Why?** | |
| **Privacy concerns?** | |
| **Quality needs?** | |

<details>
<summary>💡 Things to consider</summary>

Medical records are extremely sensitive (protected by laws like HIPAA in the US). Sending patient data to cloud servers raises serious privacy and legal concerns. However, the best diagnostic AI models are very large and may require cloud-level compute. Many hospitals are exploring **on-premise (local) AI** for this exact reason — or using cloud AI only with strict data agreements.

</details>

---

### Scenario B: 📝 Student Homework Help

> A student wants to use AI to help understand their homework — explain concepts, check practice problems, and suggest study strategies.

| Your Choice | Local / Cloud / Either |
|---|---|
| **Why?** | |
| **Privacy concerns?** | |
| **Quality needs?** | |

<details>
<summary>💡 Things to consider</summary>

Homework isn't usually sensitive data, so privacy is less critical. Cloud AI (like ChatGPT) is easy to access and provides high-quality responses. A local model could work too, but the quality difference might matter for complex subjects. For most students, cloud AI is the practical choice — unless you want to learn how to run models yourself!

</details>

---

### Scenario C: 📢 Marketing Copy

> A company wants to use AI to generate social media posts, ad copy, and email newsletters.

| Your Choice | Local / Cloud / Either |
|---|---|
| **Why?** | |
| **Privacy concerns?** | |
| **Quality needs?** | |

<details>
<summary>💡 Things to consider</summary>

Marketing content usually isn't sensitive, and quality/creativity matter a lot. Cloud AI gives access to the best models for creative writing. However, some companies worry about proprietary marketing strategies being sent to third parties. For most businesses, cloud AI is practical — but enterprises sometimes use local AI to keep product launch details confidential.

</details>

---

### Scenario D: 📰 Journalist with Leaked Documents

> A journalist receives leaked government documents and wants to use AI to summarize and find key themes in thousands of pages.

| Your Choice | Local / Cloud / Either |
|---|---|
| **Why?** | |
| **Privacy concerns?** | |
| **Quality needs?** | |

<details>
<summary>💡 Things to consider</summary>

This is a strong case for local AI. Leaked documents could endanger sources, reveal ongoing investigations, or have national security implications. Uploading them to any cloud service means a third party has access. Journalists handling sensitive material often use air-gapped computers and local tools. The quality tradeoff is worth the privacy guarantee.

</details>

---

### Scenario E: 🎮 Game Developer NPCs

> A game studio wants AI-powered NPCs (non-player characters) that respond dynamically to player dialogue in real-time during gameplay.

| Your Choice | Local / Cloud / Either |
|---|---|
| **Why?** | |
| **Privacy concerns?** | |
| **Quality needs?** | |

<details>
<summary>💡 Things to consider</summary>

Real-time gameplay requires low latency — you can't wait for a cloud API call every time a player talks to an NPC. This makes local AI (running on the player's machine or game server) essential. It also needs to work offline. The tradeoff is that the model needs to be small enough to run alongside the game itself. This is an active area of game development!

</details>

---

### Scenario F: 🏫 School District AI Policy

> A school district wants to provide AI tools for teachers and students across 50 schools.

| Your Choice | Local / Cloud / Either |
|---|---|
| **Why?** | |
| **Privacy concerns?** | |
| **Quality needs?** | |

<details>
<summary>💡 Things to consider</summary>

Schools deal with minors' data (protected by FERPA, COPPA). Cloud AI might process student data in ways that violate these laws. Running local AI across 50 schools requires significant hardware investment and IT support. Some districts are exploring hybrid approaches — local AI for sensitive tasks, cloud AI (with data agreements) for general use. This is a real policy debate happening right now!

</details>

---

## Exercise 2: The Privacy Question 🔒

### Think About This

When you use ChatGPT, Google Gemini, or any cloud AI:

1. **Your prompt** is sent to servers owned by a company (OpenAI, Google, Anthropic, etc.)
2. **Your prompt may be used** to train or improve future models (unless you opt out, where available)
3. **Your prompt is stored** in some form — even if temporarily — on those servers
4. **Employees at the company** may review conversations for safety or quality

### Your Worksheet

Answer these questions honestly:

| Question | Your Answer |
|---|---|
| Have you ever typed personal information into an AI chatbot? | |
| Did you think about where that data was going? | |
| Would you type your medical symptoms into ChatGPT? | |
| Would you paste your private journal entry for AI feedback? | |
| Would you upload a photo of yourself to an AI tool? | |
| Where do you think AI companies store your data? | |

**❓ Does thinking about this change how you'll use AI tools going forward?**

---

## Exercise 3: Build Your Decision Framework 🧭

Based on everything you've learned, fill in this framework for making local vs. cloud AI decisions:

### I would choose LOCAL AI when:

1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

### I would choose CLOUD AI when:

1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

### I would use EITHER when:

1. _______________________________________________
2. _______________________________________________

---

## 💬 Discussion Questions

1. **Today's workshop used local AI.** Did you feel limited by the model quality, or was it good enough for what we were doing?

2. **Should AI companies be required to delete your data** after processing your request? What are the pros and cons?

3. **Some countries are building regulations** around where AI data can be stored (data sovereignty). Why might a country want AI data to stay within its borders?

4. **As local AI models get better** (they're improving fast), do you think cloud AI will become less important? Or will cloud always have the edge?

5. **Right now, you used models with 1B–14B parameters locally.** The biggest cloud models have hundreds of billions. What happens when models that good can run on your phone?

---

## 🎯 Key Takeaways

- 🏠 **Local AI keeps your data private** — nothing leaves your machine or network
- ☁️ **Cloud AI offers better quality** — but at the cost of sending your data elsewhere
- 🔒 **Privacy isn't just about "having nothing to hide"** — it's about control over your information
- 💰 **Cost models are different** — local = upfront hardware, cloud = ongoing subscription
- 🚀 **The gap is shrinking** — local models are getting better fast, making local AI more viable every year
- 🤔 **There's no universal right answer** — the best choice depends on the specific situation, sensitivity of data, and quality requirements

---

**Next up: [Lab 7: Bias and Fairness in AI →](lab-07-bias-and-fairness.md)**
