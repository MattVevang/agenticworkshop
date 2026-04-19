# 🔍 Lab 4: Catching AI Lies

## Learning Objectives

By the end of this lab, you will:
- ✅ Understand what **AI hallucinations** are and why they happen
- ✅ Be able to **detect** when an AI is making things up
- ✅ Learn practical strategies for **fact-checking** AI responses
- ✅ Know how to **reduce** hallucinations with better prompts

⏱️ **Estimated Time:** 20 minutes

🤖 **Suggested Model:** `mistral:7b` or `qwen3.5:9b`

---

## 🧠 Background: What Are Hallucinations?

AI models don't "know" things. They predict likely-sounding text based on patterns they learned during training. This means they can — and regularly do — **generate text that sounds completely confident and authoritative but is totally wrong.**

This is called a **hallucination**. It's not the AI "lying" on purpose. It's the AI doing what it always does — predicting plausible next words — but landing on something that happens to be false.

### Why Should You Care?

- AI will **never say "I don't know"** unless specifically trained to (and even then, it's inconsistent)
- Hallucinated text **reads exactly the same** as accurate text — there's no visual difference
- The more confident-sounding the AI is, the more dangerous the hallucination
- **You** are responsible for verifying what AI tells you

---

## Exercise 1: The Trick Question 🎭

This prompt asks about something that **doesn't exist**. Let's see if the AI takes the bait.

### Instructions

Start a **new chat** and type:

```
Who won the Nobel Prize in Mathematics in 2023?
```

### The Catch

**There is no Nobel Prize in Mathematics.** It doesn't exist. The closest thing is the Fields Medal (awarded every 4 years) or the Abel Prize.

### ✏️ Record What Happened

| Question | Your Observation |
|---|---|
| Did the AI tell you there's no Nobel Prize in Math? | |
| Did it make up a winner? If so, who? | |
| Did it sound confident in its (wrong) answer? | |
| Did it mention the Fields Medal or Abel Prize instead? | |

**❓ How would you have known this was wrong if you didn't already know the trick?**

---

## Exercise 2: The Fake Book 📚

Let's ask about a book that **does not exist**.

New chat:

```
Summarize the book "The Crystal Horizon" by James Patterson
```

### The Catch

This book doesn't exist. James Patterson is a real author, but "The Crystal Horizon" is not one of his books. (There is an unrelated book of the same name by mountaineer Reinhold Messner — about climbing Everest solo — but it's not by Patterson.)

### ✏️ Record What Happened

| Question | Your Observation |
|---|---|
| Did the AI admit the book doesn't exist? | |
| Did it generate a fake summary? | |
| Did the summary sound convincing? | |
| Did it perhaps confuse it with a different book? | |

**❓ If a classmate showed you this "summary" for a book report, would you suspect it was fake?**

---

## Exercise 3: The Ambiguous Question 🏙️

This prompt is technically answerable but deeply ambiguous.

New chat:

```
What is the population of Springfield, USA?
```

### The Catch

There are over **30 cities named Springfield** in the United States! The most well-known include:
- Springfield, Illinois (~115,000)
- Springfield, Missouri (~170,000)
- Springfield, Massachusetts (~155,000)
- Springfield, Ohio (~58,000)

### ✏️ Record What Happened

| Question | Your Observation |
|---|---|
| Which Springfield did the AI pick? | |
| Did it acknowledge the ambiguity? | |
| Was the population number accurate? (You can Google it) | |
| Did it confidently present one answer as *the* answer? | |

---

## Exercise 4: Fact-Check a Real Topic ✅

Now let's test the AI on a real historical topic and see if the details hold up.

### Step 1: Get the AI's Response

New chat:

```
Tell me about the Battle of Thermopylae. Include specific details: dates, number of soldiers on each side, key leaders, and the outcome.
```

### Step 2: Fact-Check

Use Google, Wikipedia, or another reliable source to verify **at least 3 specific claims** from the AI's response.

### ✏️ Fact-Checking Table

| Claim the AI Made | True, False, or Partially True? | Source You Used to Verify |
|---|---|---|
| | | |
| | | |
| | | |
| | | |

**❓ How many claims were accurate? Were any details slightly off?**

> 💡 Pay special attention to **specific numbers** (troop counts, dates) — these are where models hallucinate most.

---

## Exercise 5: Try to Reduce Hallucinations 🛡️

Let's see if better prompting can make the AI more honest.

### Attempt 1: Ask the Same Fake Book Question, But Better

New chat:

```
Does the book "The Crystal Horizon" by James Patterson exist? If it does exist, provide a brief summary. If it does not exist or you're not sure, say so clearly. Do not make up information.
```

### Attempt 2: Ask for Sources

New chat:

```
Who won the Nobel Prize in Mathematics in 2023? If this prize doesn't exist, tell me that. Cite your sources.
```

### ✏️ Compare to Your Earlier Results

| Question | Did the improved prompt reduce hallucination? |
|---|---|
| Fake book question | |
| Nobel Prize trick | |

**❓ Did being explicit about "don't make things up" actually help?**

---

## 🛡️ Your Hallucination Detection Toolkit

Here are strategies you can use every time you work with AI:

### 1. 🚩 Red Flags to Watch For
- **Very specific numbers** (dates, statistics, populations) that you can't verify
- **Confident tone about obscure topics** — the AI doesn't get less confident when it knows less
- **Too-perfect answers** — real topics are messy; if the answer is suspiciously clean, be skeptical
- **Names of people, books, or events** you've never heard of — double-check them

### 2. ✅ Fact-Checking Steps
1. **Google the key claims** — especially proper nouns, dates, and statistics
2. **Ask the AI to cite sources** — then check if those sources actually exist
3. **Cross-reference with a second model** — if two models disagree, dig deeper
4. **Ask follow-up questions** — hallucinations often fall apart under questioning

### 3. 🎯 Prompting Strategies to Reduce Hallucinations
- Add **"If you're not sure, say so"** to your prompts
- Ask for **specific sources or citations**
- Be **specific in your question** — ambiguous prompts invite hallucinated answers
- Ask the AI to **rate its own confidence** (it's not always accurate, but it helps)

---

## 💬 Discussion Questions

1. **Was there a hallucination that genuinely surprised you?** One that you almost believed?

2. **Why can't AI just say "I don't know"?** What about how language models work makes honesty hard?

3. **How dangerous could hallucinations be in the real world?** Think about medical advice, legal documents, or news articles.

4. **Whose responsibility is it** when AI gives wrong information — the AI company, the user, or both?

5. **Do you think hallucinations will be "solved" eventually**, or is this a fundamental limitation of how these models work?

---

## 🎯 Key Takeaways

- 🤥 **AI hallucinations are confident-sounding false statements** — the AI isn't trying to deceive you, but the effect is the same
- 🔍 **You cannot tell hallucinations from real information just by reading the text** — you must verify independently
- ❓ **AI models struggle to say "I don't know"** — they'd rather generate a plausible-sounding answer
- 🛡️ **Better prompts reduce (but don't eliminate) hallucinations** — ask for sources, encourage honesty
- ✅ **Always fact-check important information** — AI is a starting point, not the final word
- 🧠 **Critical thinking is your superpower** — AI can generate text, but only you can evaluate whether it's true

---

**Next up: [Lab 5: Creative & Multimodal AI →](lab-05-creative-and-multimodal.md)**
