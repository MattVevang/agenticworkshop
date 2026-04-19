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

## Exercise 4: Temperature in Action 🔥 *(Instructor Demo)*

> ⚠️ **Important:** In our shared workshop setup, temperature settings affect **all users at once**. To avoid disrupting everyone's experience, your instructor will demonstrate this live — watch carefully!
>
> Want to try it yourself? See the **"Try This at Home"** section at the end of this lab.

### What You'll See

Your instructor will run the same haiku prompt three times at **temperature 0** (fully deterministic), then three times at **default temperature** (~0.7).

### Watch For

| Temperature 0 | Default Temperature |
|---|---|
| Responses should be identical (or nearly so) | Responses should vary each time |
| Feels robotic, repetitive | Feels natural, creative |
| The model always picks the "safest" next word | The model explores different word choices |

### ✏️ Record the Instructor Demo Results

| Setting | Attempt 1 | Attempt 2 | Attempt 3 | Were they the same? |
|---|---|---|---|---|
| Temperature 0 | | | | |
| Default temp | | | | |

**❓ Can you see how temperature is the "dial" that controls the randomness you observed in Exercises 1–3?**

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

## 🏠 Try This at Home: Temperature Experiment

> Want to try the temperature experiment yourself? Here's how — on your own machine or personal account (not during the workshop, since our shared setup means settings changes affect everyone).

### What You'll Need

- Ollama or Open WebUI running locally, or any AI chat interface with parameter controls

### The Experiment

1. **Set temperature to 0** (look for a Settings/gear icon → Advanced Parameters → Temperature slider)
2. Run the haiku prompt 3 times in 3 new chats — you should see nearly identical responses
3. **Set temperature back to default** (~0.7–0.8)
4. Run the haiku prompt 3 more times — you should see variety again
5. **Crank temperature to 1.5 or 2.0** — watch things get weird and creative!

### Why This Is Worth Trying

This is one of the most powerful ways to intuitively understand how AI generates text. Temperature is the single setting that most affects whether AI output feels robotic, natural, or chaotic — and it's something you can control in most AI tools.

---

**Next up: [Lab 2: Model Showdown →](lab-02-model-comparison.md)**
