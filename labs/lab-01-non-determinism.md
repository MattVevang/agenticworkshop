# 🎲 Lab 1: AI is NOT a Calculator

## Learning Objectives

By the end of this lab, you will:
- ✅ Understand that AI models are **non-deterministic** — the same input can produce different outputs
- ✅ Learn what **temperature** is and how it controls randomness
- ✅ Be able to explain *why* AI responses vary each time

⏱️ **Estimated Time:** 15–20 minutes

🤖 **Suggested Model:** `mistral:7b` (unless noted otherwise)

---

## 🧠 Background: What Does "Non-Deterministic" Mean?

When you type `2 + 2` into a calculator, you get `4`. Every single time. Forever. That's **deterministic** — same input, same output.

AI language models don't work like that. They don't "know" the answer to your question. Instead, they **predict** the most likely next word, one word at a time — and there's some randomness baked into that process. Think of it like this: the model is rolling weighted dice for every single word in the response.

This means: **Ask the same question twice, get two different answers.** Let's prove it.

---

## Exercise 1: The Haiku Test 🍕

### Instructions

1. Select **`mistral:7b`** from the model dropdown
2. **Start a new chat** and type this prompt exactly:

```
Write a haiku about pizza
```

3. Read and note the response
4. **Start a new chat** (important!) and type the **exact same prompt** again:

```
Write a haiku about pizza
```

5. **Start a new chat** one more time and type it a **third time**:

```
Write a haiku about pizza
```

### ✏️ Record Your Results

| Attempt | Haiku You Received |
|---|---|
| 1st | |
| 2nd | |
| 3rd | |

**❓ Were they the same or different? How different were they?**

---

## Exercise 2: The Science Sentence 🔬

Repeat the same process — **3 new chats, same prompt each time**:

```
Explain gravity in one sentence
```

### ✏️ Record Your Results

| Attempt | Response |
|---|---|
| 1st | |
| 2nd | |
| 3rd | |

**❓ Did the explanations use different words? Different analogies? Was one more accurate than another?**

---

## Exercise 3: The Creativity Challenge 📎

One more round — **3 new chats, same prompt each time**:

```
List 5 creative uses for a paperclip
```

### ✏️ Record Your Results

| Attempt | The 5 Ideas |
|---|---|
| 1st | |
| 2nd | |
| 3rd | |

**❓ How much overlap was there between the lists? Did any responses surprise you?**

---

## 🌡️ Deep Dive: What is Temperature?

So *why* do responses vary? The main reason is a setting called **temperature**.

### How Temperature Works

When a model predicts the next word, it doesn't just pick the #1 most likely word. It calculates probabilities for *every possible word* and then **samples** from those probabilities. Temperature controls how this sampling works:

| Temperature | Behavior | Analogy |
|---|---|---|
| **0** | Always picks the most probable word. As deterministic as it gets. | Following the GPS exactly — no detours |
| **0.1–0.5** | Mostly sticks to likely words, small variation | Taking the suggested route but occasionally picking a side street |
| **0.7–1.0** (typical default) | Balanced between predictable and creative | Exploring the neighborhood — you'll get somewhere interesting |
| **1.5–2.0** | Very random, often chaotic | Closing your eyes and pointing at the map |

### Think of it like this:

Imagine the model is writing a story and needs the next word after "The cat sat on the..."

- **Temperature 0:** Always picks "mat" (most likely)
- **Temperature 0.7:** Usually picks "mat" but sometimes "couch," "roof," or "table"
- **Temperature 2.0:** Might pick "refrigerator," "cloud," or "existential crisis"

---

## Exercise 4: Temperature Experiment 🔥

Let's actually test this! We'll change the temperature setting and see what happens.

### How to Change Temperature in OpenWebUI

1. Click the **⚙️ Settings/gear icon** near the model dropdown or chat area  
2. Look for a **Temperature** slider or parameter setting  
3. You may find it under **Advanced Parameters** or **Model Settings**

> 💡 Your instructor can help you find this — the exact location depends on the OpenWebUI version.

### Step 1: Temperature = 0

1. Set temperature to **0**
2. **Start a new chat** and type:

```
Write a haiku about pizza
```

3. Note the response
4. **Start a new chat** (keep temperature at 0) and type the same prompt again
5. Repeat one more time (3 attempts total)

### ✏️ Record Your Results (Temperature 0)

| Attempt | Haiku |
|---|---|
| 1st | |
| 2nd | |
| 3rd | |

**❓ Were the responses identical or nearly identical this time?**

### Step 2: Temperature = Default

1. Set temperature back to the **default** (typically 0.7 or 0.8 — or just remove your override)
2. Repeat the same process: **3 new chats, same haiku prompt**

### ✏️ Record Your Results (Default Temperature)

| Attempt | Haiku |
|---|---|
| 1st | |
| 2nd | |
| 3rd | |

**❓ How do the temperature-0 results compare to the default results?**

---

## 💬 Discussion Questions

Take a few minutes to think about these (or discuss with a partner):

1. **If AI isn't deterministic, can you trust it to give you correct answers?** What does this mean for using AI on homework or important tasks?

2. **When would you *want* high randomness?** When would you want low randomness? Think of specific scenarios.

3. **If you asked an AI to help with a math problem**, should temperature be high or low? What about writing a creative story?

4. **How is this different from a Google search?** When you search "capital of France," you always get "Paris." Why can't AI do that?

5. **Does this make AI more or less useful than you expected?** Why?

---

## 🎯 Key Takeaways

- 🎲 **AI is non-deterministic by default** — same prompt, different response every time
- 🌡️ **Temperature controls randomness** — lower = more predictable, higher = more creative/chaotic
- 🔢 **Temperature 0 makes AI nearly deterministic** — but the responses might feel robotic
- 🧠 **AI predicts words probabilistically** — it doesn't "know" things the way a database does
- ⚖️ **This is a feature, not a bug** — non-determinism is what makes AI creative and flexible

---

**Next up: [Lab 2: Model Showdown →](lab-02-model-comparison.md)**
