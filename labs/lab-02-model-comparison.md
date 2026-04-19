# ⚔️ Lab 2: Model Showdown — The Llama Drag Race

## Learning Objectives

By the end of this lab, you will:
- ✅ Understand that different-sized models produce **very different results** for the same prompt
- ✅ See the tradeoff between model size, **speed**, and **quality** in a fair comparison
- ✅ Be able to make informed decisions about which model to use for a given task

⏱️ **Estimated Time:** 15–20 minutes

---

## 🧠 Background: Why Are There So Many Model Sizes?

You wouldn't use a Formula 1 car to get groceries, and you wouldn't take a minivan to a race track. AI models are the same — they come in different sizes for different jobs.

**Model size** is measured in **parameters** (think of them as the model's "brain cells"):

| Model | Parameters | Speed | Analogy |
|---|---|---|---|
| `llama3.2:1b` | 1.3 billion | ⚡ ~741 tok/s | A smart calculator |
| `llama3.2:3b` | 3 billion | ⚡ ~424 tok/s | A helpful intern |
| `llama3.1:8b` | 8 billion | ⚡ ~254 tok/s | A solid generalist |

More parameters generally means: better reasoning, more knowledge, more nuance — but also **slower responses** and **more computing resources**.

> 🏎️ **Why this comparison is fair:** All three models come from the **same Llama family** by Meta. Same training approach, same architecture — the **only major difference is size**. This is a true drag race: small vs. medium vs. large from the same team.

Let's see this in action.

---

## Exercise 1: Explain It to a Kid 👶

### Instructions

You're going to run the **exact same prompt** through 3 different Llama models and compare the results.

**Prompt** (copy this exactly each time):

```
Explain quantum computing to a 10-year-old in about 100 words
```

**Run it through these models** (start a **new chat** each time and select the model from the dropdown):

1. `llama3.2:1b` (smallest)
2. `llama3.2:3b` (medium)
3. `llama3.1:8b` (largest)

### ✏️ Fill In Your Comparison Table

| Dimension | llama3.2:1b | llama3.2:3b | llama3.1:8b |
|---|---|---|---|
| **Response quality** (1–5) | | | |
| **Speed** (fast / medium / slow) | | | |
| **Actually understandable by a 10-year-old?** (yes / kinda / no) | | | |
| **Used a good analogy?** (yes / no, what was it?) | | | |
| **Approximately correct word count?** | | | |
| **Style notes** (robotic? natural? fun?) | | | |

### 🤔 Reflection

- Which model gave the best explanation? Was it the biggest one?
- Did the smallest model manage to produce something useful at all?
- How big was the speed difference between smallest and largest?

---

## Exercise 2: Code Challenge 💻

This exercise tests how well models can write actual working code.

**Prompt** (same for all models):

```
Write a Java method called isPrime that takes an integer and returns true if it's prime, false otherwise. Include comments explaining each step.
```

**Run it through these models:**

1. `llama3.2:1b`
2. `llama3.2:3b`
3. `llama3.1:8b`

### ✏️ Fill In Your Comparison Table

| Dimension | llama3.2:1b | llama3.2:3b | llama3.1:8b |
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

Some prompts need models to handle complexity and present balanced viewpoints. Let's see if size matters for nuance.

**Prompt:**

```
What are the pros and cons of social media for teenagers? Give 3 specific pros and 3 specific cons with brief explanations for each.
```

**Run it through these models:**

1. `llama3.2:1b`
2. `llama3.2:3b`
3. `llama3.1:8b`

### ✏️ Fill In Your Comparison Table

| Dimension | llama3.2:1b | llama3.2:3b | llama3.1:8b |
|---|---|---|---|
| **Followed the format?** (3 pros, 3 cons) | | | |
| **Points are specific?** (not just vague fluff) | | | |
| **Balanced or biased?** | | | |
| **Quality of explanations** (1–5) | | | |
| **Speed** | | | |
| **Overall best response?** | | | |

---

## Exercise 4 (Bonus): Speed Test ⚡

If you have time, let's get a rough feel for speed differences across the family.

**Prompt** (use for all models):

```
Write a 200-word essay about why sleep is important for teenagers
```

**Rough-time each model** (use your phone timer or just count seconds):

| Model | Parameters | Approximate Time |
|---|---|---|
| `llama3.2:1b` | 1.3B | |
| `llama3.2:3b` | 3B | |
| `llama3.1:8b` | 8B | |

> 💡 **What you should see:** The 1B model responds almost instantly, the 3B takes a beat, and the 8B takes a couple seconds. Watch the streaming text — can you *see* the speed difference?

**❓ Is there a clear correlation between model size and response time?**

---

## 💬 Discussion Questions

1. **Was the biggest model always the best?** Were there cases where a smaller model gave a perfectly good answer?

2. **If you were building an app that needed to respond instantly** (like autocomplete), would you use the 8B model? Why or why not?

3. **For which task did model size matter most?** The kid explanation, the code, or the pros/cons analysis?

4. **How do you think models like ChatGPT or Claude compare in size** to what you just tested? (Hint: think *hundreds of billions* of parameters, or more)

5. **If bigger is generally better, why would anyone use small models?** Think about cost, speed, privacy, and offline use.

6. **Why did we compare models from the same family?** What would change if we compared a 3B model from one company to a 3B model from another?

---

## 🎯 Key Takeaways

- 📏 **Model size matters, but it's not everything** — the best model depends on your task
- ⚡ **Smaller models are faster** — sometimes fast and good enough beats slow and perfect
- 🧠 **Larger models handle nuance and complexity better** — they're stronger at reasoning, following instructions, and covering edge cases
- 🎯 **Match the model to the job** — you don't need an 8B-parameter model to generate a haiku
- 🏎️ **Same family, different sizes = fair comparison** — when only size changes, you can clearly see the tradeoffs
- 💰 **In the real world, bigger models cost more** — so choosing wisely saves money and energy

---

**Next up: [Lab 3: The Art of Asking →](lab-03-prompt-engineering.md)**
