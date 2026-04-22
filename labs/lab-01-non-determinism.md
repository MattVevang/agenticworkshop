# 🎲 Lab 1: AI is NOT a Calculator

## Learning Objectives

By the end of this lab, you will:
- ✅ Understand that AI models are **non-deterministic** — the same input can produce different outputs
- ✅ Learn what **temperature** is and how it controls randomness
- ✅ Be able to explain *why* AI responses vary each time

⏱️ **Estimated Time:** 15–20 minutes

🤖 **Suggested Model:** `llama3.2:3b` (unless noted otherwise)

---

## 🧠 Background: What Does "Non-Deterministic" Mean?

When you type `2 + 2` into a calculator, you get `4`. Every single time. Forever. That's **deterministic** — same input, same output.

AI language models don't work like that. They don't "know" the answer to your question. Instead, they **predict** the most likely next word, one word at a time — and there's some randomness baked into that process. Think of it like this: the model is rolling weighted dice for every single word in the response.

This means: **Ask the same question twice, get two different answers.** Let's prove it.

---

## Exercise 1: The Haiku Test 🍕

### Instructions

1. Select **`llama3.2:3b`** from the model dropdown
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
| **0** | Always picks the most probable word. Removes the randomness. | Following the GPS exactly — no detours |
| **0.1–0.5** | Mostly sticks to likely words, small variation | Taking the suggested route but occasionally picking a side street |
| **0.7–1.0** (typical default) | Balanced between predictable and creative | Exploring the neighborhood — you'll get somewhere interesting |
| **1.5–2.0** | Wider exploration of word choices | Wandering further from the main road |

### The honest truth about temperature

**Temperature 0 vs. anything else is a dramatic, visible difference** — responses go from identical every time to varied every time. But the difference between moderate temperatures (like 0.7 vs. 1.5) is often subtle and hard to spot — even experts need to compare responses carefully. What matters most:

- **Zero = locked.** The model picks the same path every time.
- **Above zero = unlocked.** The model explores, and higher values allow *wider* exploration — but the effect is gradual, not dramatic.

> 💡 Temperature controls **variation**, not **accuracy**. A higher temperature doesn't make the AI more wrong — it makes it more willing to try different word choices.

---

## Exercise 4: The Lock-Down Demo 🔒 *(Instructor Demo)*

> ⚠️ **Important:** In our shared workshop setup, parameter changes can affect all users. Your instructor will demonstrate this live — watch carefully and follow along!

### Before the Demo — Make a Prediction! 🤔

Think back to Exercise 1: you asked for a haiku about pizza three times and got **different haiku each time**.

**❓ Your instructor is about to run the exact same prompt three more times, but with one change to the settings. Predict: will the responses be the same or different?**

### What the Instructor Will Do

**Part A — Temperature 0 (Locked Mode)**

1. Open a **new chat** with `llama3.2:3b`
2. Click the **⚙️ gear icon** (chat settings) → **Advanced Parameters** → set **Temperature to 0**
3. Type the same prompt from Exercise 1:

```
Write a haiku about pizza
```

4. Start a **new chat**, keep temperature at 0, type the same prompt again
5. Repeat one more time (3 total runs at temperature 0)

### ✏️ Record the Results

| Run | Haiku (Temperature 0) |
|---|---|
| 1st | |
| 2nd | |
| 3rd | |

**Were they identical? Word-for-word the same?** Compare carefully!

**Part B — Back to Default (Unlocked Mode)**

1. The instructor switches temperature **back to default** (~0.7)
2. Runs the same haiku prompt **2 more times** in new chats

| Run | Haiku (Default Temperature) |
|---|---|
| 4th | |
| 5th | |

**Did the variation come back?** Compare these to the three locked responses above.

### 💡 What Just Happened?

- At **temperature 0**, the model followed the exact same path through its word predictions every time — like a GPS that never deviates
- At **default temperature**, the randomness came back — the same randomness you experienced in Exercises 1–3
- **Temperature is the dial that controls the variation you've been observing this whole lab**

> ℹ️ *Note: Temperature 0 produced identical responses with `llama3.2:3b` in our testing. Different models may behave slightly differently — some aren't perfectly deterministic even at zero. The core lesson holds: lower temperature = less variation.*

---

## 💬 Discussion Questions

Take a few minutes to think about these (or discuss with a partner):

1. **If AI isn't deterministic, can you trust it to give you correct answers?** What does this mean for using AI on homework or important tasks?

2. **When would you *want* more variation?** When would you want less? Think of specific scenarios — like writing a poem vs. checking a math answer.

3. **Temperature controls variation, not accuracy.** If you set temperature to 2.0, does the AI become *wrong* more often, or just *different*? What's the difference?

4. **How is this different from a Google search?** When you search "capital of France," you always get "Paris." Why can't AI do that?

5. **If you were building an AI assistant for a hospital**, would you want temperature at 0 or 0.7? What about for an AI that writes jokes?

---

## 🎯 Key Takeaways

- 🎲 **AI is non-deterministic by default** — same prompt, different response every time
- 🌡️ **Temperature controls variation** — zero = locked (identical every time), above zero = unlocked (responses differ)
- 🔒 **Temperature 0 is the "off switch" for randomness** — the model picks the single most likely path
- 💡 **Temperature affects variation, not accuracy** — higher doesn't mean more wrong, just more different
- ⚖️ **Non-determinism is a feature, not a bug** — it's what makes AI creative and flexible
- 📏 **The gradient is subtle** — the difference between 0 and non-zero is dramatic, but 0.7 vs. 1.5 is hard to spot

---

## 🏠 Try This at Home: Temperature Experiment

> Want to explore temperature further? Here's how — on your own machine or personal account (not during the workshop, since our shared setup means settings changes affect everyone).

### What You'll Need

- Ollama or Open WebUI running locally, or any AI chat interface with parameter controls

### The Experiment

1. **Set temperature to 0** (look for a Settings/gear icon → Advanced Parameters → Temperature slider)
2. Run the haiku prompt 3 times in 3 new chats — you should see identical (or near-identical) responses
3. **Set temperature back to default** (~0.7–0.8)
4. Run the haiku prompt 3 more times — you should see variety again
5. **Try temperature 1.5 or 2.0** — the responses will still be coherent, but you may notice wider variety in word choices if you compare carefully

### What to Expect

The **big** visible difference is between 0 and everything else. The differences between moderate values (0.7 vs. 1.5 vs. 2.0) are **subtle** — you might need to run many trials and compare carefully to notice patterns. This is normal! Temperature is a statistical control, not a chaos switch.

### Why This Is Worth Trying

Even if the gradient is subtle, understanding temperature helps you:
- **Get consistent outputs** when you need them (temp=0 for code generation, data extraction)
- **Encourage creativity** when you want it (default or slightly higher for brainstorming)
- **Understand why AI tools behave the way they do** — most chatbots use temperature 0.7–1.0

---

**Next up: [Lab 2: Model Showdown →](lab-02-model-comparison.md)**
