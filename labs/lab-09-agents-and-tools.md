# 🧰 Lab 9: Agents & Tools

[← Back to Lab Overview](README.md)

## Learning Objectives

By the end of this lab, you will:
- ✅ Understand the difference between an AI **on its own** and an AI **with tools**
- ✅ See **native tool calling** in action — a model that decides to **search the web** by itself
- ✅ Watch an **AI agent** think, act, observe, and answer — with **citations**
- ✅ Understand how a single **tool** can *layer on top of* a model and unlock new abilities
- ✅ Challenge the idea that "AI is dumb" or "AI always gets it wrong"

⏱️ **Estimated Time:** 20–25 minutes

🤖 **Suggested Model:** `qwen3.6:35b` on the **tool-enabled instance (port 3001)**

📋 **Lab Type:** Hands-on (instructor-guided start)

> 🧑‍🏫 **Instructor setup (before class):** this lab uses a **second** Open WebUI instance that
> has web search + tools turned on. Start it and verify it once:
> ```powershell
> cd docker\tools
> docker compose up -d
> python demos/scripts/openwebui-tools-setup.py   # expect: ✅ PASS
> ```
> See [`docker/tools/README.md`](../docker/tools/README.md) for the full guide. The big model
> is **shared**, so it can feel slow when the whole class hits it at once — consider demoing
> Exercises 1–3 from the front, then letting students explore Exercises 4–5 in pairs or turns.

---

## 🧠 Background: A Brain in a Jar

So far in this workshop, every model you've used has been a **brain in a jar**.

It's smart — it learned from a huge amount of text — but it's *sealed off* from the world. It
can't look anything up. It can't check a fact. It can't see today's news, today's date, or
today's weather. Everything it "knows" was frozen in place when its training ended (its
**knowledge cutoff**). Ask it about something that happened *after* that, and it has only two
options: admit it doesn't know, or **make something up** (remember the hallucinations from
[Lab 4](lab-04-hallucination-detection.md)?).

That's where a lot of people get the idea that *"AI is dumb"* or *"AI just gets things wrong."*

But here's the plot twist this lab is about: **give that same brain a tool, and everything
changes.**

### What's a "tool"? What's an "agent"?

A **tool** is an ability you hand to the model — a button it can press to *reach outside
itself*. The most useful one is **web search**. Others include running code, reading a file,
doing math with a calculator, or calling an API.

An **agent** is what you get when a model can **use tools on its own** to accomplish a goal.
Instead of just predicting words, it runs a loop:

```
1. THINK    →  "To answer this, I need current information I don't have."
2. ACT      →  Calls a tool:  search_web("latest stable Python version")
3. OBSERVE  →  Reads the results that come back
4. (repeat if needed — search again, or open a page with fetch_url)
5. ANSWER   →  Replies using what it found — and cites the source
```

That ability to **look it up, check it, and confirm it** — instead of guessing — is exactly
what turns a "brain in a jar" into something genuinely useful. In this lab you'll see it
happen live.

---

## Exercise 1: Hit the Wall 🧱

First, let's prove the limitation. We'll ask a **no-tools** model questions it *cannot
possibly* answer correctly, because the answers live in the present.

### Instructions

Go to the **regular** workshop instance — **http://[server-ip]:3000** (the one you've used all
day). Select a small model like **`llama3.2:3b`**.

Start a **new chat** and ask **two or three** of these:

```
What is today's date?
```

```
Who is the current President of the United States, and what is a news story about them from this week?
```

```
What is the latest stable version of Python right now?
```

```
What is the current price of Bitcoin?
```

### The Catch

None of these models can know "right now." Watch *how* each one fails — it's revealing:

### ✏️ Record What Happened

| Question you asked | How did the model respond? (guessed / refused / made something up / gave an old answer) |
|---|---|
| | |
| | |
| | |

**❓ Did any model state an answer *confidently* that you suspect is out of date or invented?**

> 💡 This is the honest limit of a model on its own. It's not "dumb" — it just has **no way to
> reach the information**. Hold onto that thought.

---

## Exercise 2: Same Question, New Superpower 🦸

Now for the twist. We'll ask the **exact same question** — but to a model that has a **web
search tool**.

### Instructions

Open the **tool-enabled** instance in a new tab — **http://[server-ip]:3001**.

> This looks almost identical to the instance you've been using, but it's a *separate* one with
> tools switched on. It's running a bigger, **tool-capable** model.

1. Select **`qwen3.6:35b`** from the model dropdown
2. Make sure the **Web Search** toggle near the message box is **ON** (it should be on by
   default — look for a 🌐 globe / "Web Search" control)
3. Start a **new chat** and ask the **same** live-data question you used in Exercise 1:

```
What is today's date, and who is the current President of the United States? Include a recent news story about them.
```

Watch closely. You should see a status message like **"Searching the web…"**, and then an
answer that contains **numbered citations** like `[1]` `[2]` you can click.

### ✏️ Compare the Two Instances

| | Port 3000 (no tools) | Port 3001 (`qwen3.6:35b` + web search) |
|---|---|---|
| Did it know today's date? | | |
| Did it get the answer right? | | |
| Did it show sources / citations? | | |
| Would you trust the answer? | | |

**❓ Same kind of AI model — so what made the difference?** (Hint: it wasn't that one model is
"smarter." One of them could **look it up**.)

---

## Exercise 3: The Toggle *Is* the Lesson 🔀

Here's the cleanest way to see that the **tool** — not a different brain — is what changed
things. We'll flip web search **off and on** for the *same* model.

### Instructions

Stay on **http://[server-ip]:3001** with **`qwen3.6:35b`** selected.

**Round 1 — tool OFF:**
1. **Turn the Web Search toggle OFF**
2. Start a **new chat** and ask:

```
What was a major technology announcement this month?
```

**Round 2 — tool ON:**
1. **Turn the Web Search toggle back ON**
2. Start a **new chat** and ask the **exact same** question again.

### ✏️ Record What Happened

| | Tool OFF | Tool ON |
|---|---|---|
| Did it answer the question? | | |
| Did it search the web? | | |
| Did it cite a source? | | |
| How current did the answer feel? | | |

**❓ The model's "brain" was identical in both rounds. The only thing that changed was whether
it could reach a tool. What does that tell you about where the limitation really was?**

> 💡 **This is the whole idea of the lab in one toggle.** Intelligence wasn't the bottleneck —
> **access** was. Tools are a *layer* you add on top of a model, and that layer unlocks abilities
> the model never had on its own.

---

## Exercise 4: Watch the Agent Think 🔎

A real agent doesn't just do one search and stop. When a question is harder, it can search
**more than once**, **open a page** to read it in detail (`fetch_url`), and pull the pieces
together. Let's watch that happen.

### Instructions

On **http://[server-ip]:3001** with **`qwen3.6:35b`** (Web Search **ON**), start a **new chat**
and ask a question that needs **digging**, not just one quick lookup:

```
Compare the two most popular AI coding assistants right now: what are they called, who makes them, and what's one feature each one is known for? Cite your sources.
```

or pick your own research-style question:

```
What are three of the biggest news stories from this past week, and why does each one matter? Include a source for each.
```

As it works, **expand the status / "thinking" section** if the UI offers one. Look for:
- the **search queries** the model chose to run (it writes them itself!)
- whether it searched **more than once** or **opened a page**
- the **citations** in the final answer

### ✏️ Trace the Agent's Steps

| Question | Your Observation |
|---|---|
| What search term(s) did the model come up with on its own? | |
| Did it search just once, or refine and search again? | |
| How many sources did it cite? | |
| Did you click a citation? Did the source actually back up the claim? | |

**❓ Notice that *you* never told it to search, or what to search for. It figured that out
itself. That decision-making — "I need a tool, here's how I'll use it" — is what makes it an
*agent* instead of just a chatbot.**

---

## Exercise 5: Grounded vs. Guessing — Why Tools Mean *Better* Answers ✅

In [Lab 4](lab-04-hallucination-detection.md) you learned that models hallucinate — they state
made-up things confidently. Tools are one of the most powerful **cures** for that, because an
agent can **check itself** instead of guessing.

### Step 1 — Ask the no-tools instance (port 3000)

Pick a topic that's **factual and recent**. Start a **new chat** on **http://[server-ip]:3000**
with `llama3.2:3b`:

```
List the top 3 highest-grossing movies released in 2026 so far, with their box office totals.
```

It will likely **invent** titles and numbers — it has no way to know 2026 box office. Note how
confident it sounds anyway.

### Step 2 — Ask the tools instance (port 3001)

Same question, **http://[server-ip]:3001**, `qwen3.6:35b`, Web Search **ON**:

```
List the top 3 highest-grossing movies released in 2026 so far, with their box office totals. Cite your sources.
```

### Step 3 — Check the work

Click the citations on the port-3001 answer. Do the sources actually support the numbers?

### ✏️ Grounded vs. Guessed

| | Port 3000 (guessing) | Port 3001 (grounded in search) |
|---|---|---|
| Did the titles/numbers look real? | | |
| Could you *verify* the answer? | | |
| Did it admit any uncertainty? | | |
| Which answer would you actually use? | | |

**❓ An agent that can search can *confirm* a fact before stating it — or correct itself when the
search disagrees with its first guess. How does the ability to "look it up and double-check"
change how much you'd trust an AI?**

> 💡 This is the deeper point: giving a model tools doesn't just add features — it can make its
> answers **more honest and higher quality**, because the model can ground what it says in real,
> checkable sources instead of pattern-matching from memory.

---

## 🌟 Bonus: Stump-Proof a Question

Design a question that is **impossible** to answer without live data — something that changed
*this week* or even *today*.

1. **Write your question** (a current price, a score from a game last night, today's weather
   somewhere, the newest version of an app…)
2. **Predict:** will the no-tools model fail? Will the tools model succeed?
3. **Test both** (port 3000 vs port 3001) and see if you were right.

### ✏️ Your Experiment

| Item | Your Response |
|---|---|
| Your "live data" question | |
| Prediction (which instance gets it right?) | |
| What the no-tools model (3000) did | |
| What the tools model (3001) did | |
| Were you right? | |

---

## 🌐 Beyond the Workshop: Tools Are Everywhere

Web search is just **one** tool. The same idea — *give the model an ability and let it decide
when to use it* — is how modern AI assistants do real work:

| Tool the agent can call | What it unlocks |
|---|---|
| 🔎 **Web search** | Current events, prices, facts beyond the training cutoff (this lab!) |
| 📄 **Read / open a page or file** | Summarize a document, pull details from a website |
| 💻 **Run code** | Do real math, analyze data, test a program |
| 🛠️ **Edit files / call APIs** | Actually *change* things — write code, send a request, book a slot |

When you hear about "**AI agents**" or tools like GitHub Copilot that can write and run code,
this is what they mean: a capable model **plus a toolbox**, deciding for itself which tool to
reach for. You just saw the simplest version of it with your own eyes.

---

## 💬 Discussion Questions

1. **At the start of the day, did you think "AI is kind of dumb / it just makes things up"?**
   After seeing the tool-enabled model search and cite sources, has that view changed? How?

2. **In Exercise 3, the only thing that changed was a toggle.** Why is it important to
   understand that the *model* wasn't the problem — the missing *tool* was?

3. **Citations.** The tool-enabled model showed its sources. Why does that matter? Would you
   trust an AI answer *more* if it links to where it got the information?

4. **When do tools NOT help?** Can you think of a question where web search would make the
   answer *worse*, or where you still shouldn't fully trust it even with sources?

5. **Agents act on their own.** A web-search agent is pretty safe. But what about an agent that
   can run code, spend money, or send messages? What could go wrong, and what guardrails would
   you want?

6. **Big picture:** if a "brain in a jar" plus a few tools can do all this, what do you think AI
   assistants will be able to do in a few years — and what skills will *you* need to use them
   well?

---

## 🎯 Key Takeaways

- 🧠 **A model on its own is a "brain in a jar"** — smart, but sealed off from current, real-world information.
- 🧰 **Tools let a model reach outside itself** — web search is the clearest example, turning "I can't know that" into a sourced answer.
- 🔀 **The tool is a layer on top of the model** — in Exercise 3, the *same* brain went from clueless to correct just by toggling search on. Access, not intelligence, was the bottleneck.
- 🤖 **An agent decides for itself** when and how to use a tool (think → act → observe → answer) — you never had to tell it what to search.
- ✅ **Tools can make AI more honest** — an agent that can look something up and **confirm** it produces higher-quality, checkable answers instead of confident guesses.
- 🚫 **"AI is dumb / always wrong" doesn't hold up** — a lot of what looks like stupidity is really a *missing tool*. Give it the right tools and it changes the game.

---

**← [Back to Lab Overview](README.md)**
