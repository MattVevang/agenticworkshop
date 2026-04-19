# ⚔️ Lab 2: Model Showdown

## Learning Objectives

By the end of this lab, you will:
- ✅ Understand that different models produce **very different results** for the same prompt
- ✅ See the tradeoff between model size, **speed**, and **quality**
- ✅ Be able to make informed decisions about which model to use for a given task

⏱️ **Estimated Time:** 15–20 minutes

---

## 🧠 Background: Why Are There So Many Models?

You wouldn't use a Formula 1 car to get groceries, and you wouldn't take a minivan to a race track. AI models are the same — they come in different sizes for different jobs.

**Model size** is measured in **parameters** (think of them as the model's "brain cells"):

| Model | Parameters | Analogy |
|---|---|---|
| `tinyllama:1.1b` | 1.1 billion | A smart calculator |
| `llama3.2:3b` | 3 billion | A helpful intern |
| `mistral:7b` | 7 billion | A solid generalist |

More parameters generally means: better reasoning, more knowledge, more nuance — but also **slower responses** and **more computing resources**.

> 💡 **Workshop note:** These three models are fast enough for everyone to use simultaneously. Larger models (14B+) exist but are too slow for interactive classroom use.

Let's see this in action.

---

## Exercise 1: Explain It to a Kid 👶

### Instructions

You're going to run the **exact same prompt** through 3 different models and compare the results.

**Prompt** (copy this exactly each time):

```
Explain quantum computing to a 10-year-old in about 100 words
```

**Run it through these models** (start a **new chat** each time and select the model from the dropdown):

1. `tinyllama:1.1b`
2. `llama3.2:3b`
3. `mistral:7b`

### ✏️ Fill In Your Comparison Table

| Dimension | tinyllama:1.1b | llama3.2:3b | mistral:7b |
|---|---|---|---|
| **Response quality** (1–5) | | | |
| **Speed** (fast / medium / slow) | | | |
| **Actually understandable by a 10-year-old?** (yes / kinda / no) | | | |
| **Used a good analogy?** (yes / no, what was it?) | | | |
| **Approximately correct word count?** | | | |
| **Style notes** (robotic? natural? fun?) | | | |

### 🤔 Reflection

- Which model gave the best explanation? Was it the biggest one?
- Did the tiny model manage to produce something useful at all?
- How big was the speed difference between smallest and largest?

---

## Exercise 2: Code Challenge 💻

This exercise tests how well models can write actual working code.

**Prompt** (same for all models):

```
Write a Java method called isPrime that takes an integer and returns true if it's prime, false otherwise. Include comments explaining each step.
```

**Run it through these models:**

1. `tinyllama:1.1b`
2. `llama3.2:3b`
3. `mistral:7b`

### ✏️ Fill In Your Comparison Table

| Dimension | tinyllama:1.1b | llama3.2:3b | mistral:7b |
|---|---|---|---|
| **Does the code look correct?** | | | |
| **Are there helpful comments?** | | | |
| **Does it handle edge cases?** (0, 1, negative numbers) | | | |
| **Code style** (clean / messy / over-complicated) | | | |
| **Speed** | | | |

### 🤔 Reflection

- Did any model produce code that's clearly buggy?
- Which model wrote the most readable code?
- Did bigger models think about edge cases that smaller ones missed?

---

## Exercise 3: Nuanced Topic 🤔

Some prompts need models to handle complexity and present balanced viewpoints. Let's see which models can do that.

**Prompt:**

```
What are the pros and cons of social media for teenagers? Give 3 specific pros and 3 specific cons with brief explanations for each.
```

**Run it through these models:**

1. `llama3.2:3b`
2. `mistral:7b`

### ✏️ Fill In Your Comparison Table

| Dimension | llama3.2:3b | mistral:7b |
|---|---|---|
| **Followed the format?** (3 pros, 3 cons) | | |
| **Points are specific?** (not just vague fluff) | | |
| **Balanced or biased?** | | |
| **Quality of explanations** (1–5) | | |
| **Speed** | | |
| **Overall best response?** | | |

---

## Exercise 4 (Bonus): Speed Test ⚡

If you have time, let's get a rough feel for speed differences.

**Prompt** (use for all models):

```
Write a 200-word essay about why sleep is important for teenagers
```

**Rough-time each model** (use your phone timer or just count seconds):

| Model | Approximate Time |
|---|---|
| `tinyllama:1.1b` | |
| `llama3.2:3b` | |
| `mistral:7b` | |

> 💡 **What you should see:** TinyLlama responds almost instantly, Llama 3.2 takes a second or two, and Mistral takes a few seconds. The quality difference is worth the small wait!

**❓ Is there a clear correlation between model size and response time?**

---

## 💬 Discussion Questions

1. **Was the biggest model always the best?** Were there cases where a smaller model gave a perfectly good answer?

2. **If you were building an app that needed to respond instantly** (like autocomplete), would you use a 14B model? Why or why not?

3. **For which task did model size matter most?** The kid explanation, the code, or the pros/cons analysis?

4. **How do you think models like ChatGPT or Claude compare in size** to what you just tested? (Hint: think *hundreds of billions* of parameters, or more)

5. **If bigger is generally better, why would anyone use small models?** Think about cost, speed, privacy, and offline use.

---

## 🎯 Key Takeaways

- 📏 **Model size matters, but it's not everything** — the best model depends on your task
- ⚡ **Smaller models are faster** — sometimes fast and good enough beats slow and perfect
- 🧠 **Larger models handle nuance and complexity better** — they're stronger at reasoning, following instructions, and covering edge cases
- 🎯 **Match the model to the job** — you don't need a 14B-parameter model to generate a haiku
- 💰 **In the real world, bigger models cost more** — so choosing wisely saves money and energy

---

**Next up: [Lab 3: The Art of Asking →](lab-03-prompt-engineering.md)**
