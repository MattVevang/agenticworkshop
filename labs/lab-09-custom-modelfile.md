# 🛠️ Lab 9: Build Your Own AI Personality (Bonus)

## Learning Objectives

By the end of this lab, you will:
- ✅ Understand what an Ollama **Modelfile** is and how it works
- ✅ Learn how to give an AI model a **custom personality** using a system prompt
- ✅ See how **parameters** like temperature can be baked into a model configuration
- ✅ Compare a custom model's behavior against its base model
- ✅ Design your own AI personality on paper

⏱️ **Estimated Time:** 15–20 minutes

📋 **Lab Type:** Instructor-led demo + student interaction

> ⚠️ **Note:** This is an instructor-guided lab. Students won't have terminal access to the Ollama server. The instructor will demonstrate the creation steps, and students will interact with the resulting custom models in Open WebUI.

---

## 🧠 Background: What is a Modelfile?

You know how a **Dockerfile** tells Docker exactly how to build a container — which base image to use, what files to copy, what commands to run? Ollama has something similar called a **Modelfile**. It tells Ollama how to build a custom model.

A Modelfile lets you take an existing model (like `mistral:7b`) and wrap it with:
- A **system prompt** that defines the model's personality and behavior
- **Parameters** that control things like temperature and context length
- A **custom name** so you can select it from the model dropdown just like any other model

This is powerful because it means you can create specialized AI assistants without retraining or fine-tuning anything. You're essentially giving the model **permanent instructions** that apply to every conversation.

### Why Does This Matter?

Think about it: every time you've used these models today, you started from scratch. If you wanted the model to act like a science tutor, you had to tell it in your prompt every single time. A Modelfile bakes those instructions in — the model *always* behaves that way without the user needing to do anything special.

This is how real companies build AI assistants. They don't just hand users a raw model — they wrap it with instructions, guardrails, and personality.

---

## Part 1: Anatomy of a Modelfile 📄

A Modelfile is a plain text file with a simple structure. Here are the key instructions:

| Instruction | What It Does | Example |
|---|---|---|
| `FROM` | Which base model to build on | `FROM mistral:7b` |
| `SYSTEM` | The system prompt — personality and behavior rules | `SYSTEM "You are a helpful assistant."` |
| `PARAMETER` | Model settings like temperature, context size, etc. | `PARAMETER temperature 0.7` |

### A Minimal Example

```dockerfile
FROM mistral:7b
SYSTEM "You are a helpful assistant that always responds in exactly three bullet points."
```

That's it! Two lines and you have a custom model that always gives three-bullet-point answers.

### Available Parameters

| Parameter | What It Controls | Default |
|---|---|---|
| `temperature` | Creativity/randomness (remember Lab 1!) | ~0.7 |
| `num_ctx` | Context window size (how much text the model can "see") | 2048 |
| `top_p` | Controls diversity of word choices | 0.9 |
| `repeat_penalty` | Discourages the model from repeating itself | 1.1 |

---

## Part 2: Building a Science Tutor 🔬

**👨‍🏫 Instructor Demo — Watch the terminal!**

The instructor will create a custom model called `science-tutor`. Here's the Modelfile:

```dockerfile
FROM mistral:7b

PARAMETER temperature 0.4
PARAMETER num_ctx 4096

SYSTEM """You are SciBot, a friendly and encouraging science tutor for high school students.

Rules you must follow:
- Explain concepts using simple language and everyday analogies
- When a student asks a question, first validate that it's a great question
- Break complex topics into numbered steps
- End every response with a "Fun Fact" related to the topic
- If you don't know something, say so honestly — never make things up
- Use emoji occasionally to keep things fun 🔬⚡🧪
- Keep responses concise — aim for 2-3 short paragraphs max
"""
```

### The Create Command

The instructor runs this in the terminal:

```bash
ollama create science-tutor -f Modelfile
```

That's it! Ollama reads the Modelfile, wraps the base model with the system prompt and parameters, and registers a new model called `science-tutor`. It appears in the Open WebUI model dropdown right away.

---

## Exercise 1: Talk to the Science Tutor 🧪

Now it's your turn! The `science-tutor` model should appear in your Open WebUI model dropdown.

### Step 1: Chat with the Base Model

1. Select **`mistral:7b`** from the model dropdown
2. **Start a new chat** and ask:

```
Why is the sky blue?
```

3. Read and note the style of the response

### Step 2: Chat with the Custom Model

1. Select **`science-tutor`** from the model dropdown
2. **Start a new chat** and ask the exact same question:

```
Why is the sky blue?
```

### ✏️ Compare the Responses

| Aspect | `mistral:7b` (Base) | `science-tutor` (Custom) |
|---|---|---|
| **Tone** (formal, casual, friendly?) | | |
| **Used analogies?** | | |
| **Included a fun fact?** | | |
| **Felt like a tutor?** | | |
| **Response length** | | |

### Try a Few More Prompts

Test both models with these and notice the differences:

```
What happens when you mix baking soda and vinegar?
```

```
How do black holes form?
```

```
Why do we need to sleep?
```

**❓ Which version would you rather learn from? Why?**

---

## Part 3: Building a Shakespeare Bot 🎭

**👨‍🏫 Instructor Demo — Watch the terminal again!**

Let's create something completely different — a model that responds in Elizabethan English:

```dockerfile
FROM mistral:7b

PARAMETER temperature 0.9
PARAMETER repeat_penalty 1.2

SYSTEM """You are ShakespeareBot, a dramatic AI that speaks exclusively in the style of William Shakespeare.

Rules you must follow:
- Always respond in Elizabethan English (thee, thou, hath, doth, wherefore, etc.)
- Use dramatic metaphors and poetic language
- Occasionally quote or reference actual Shakespeare plays
- Structure longer responses in iambic pentameter when possible
- Address the user as "good scholar" or "noble questioner"
- If asked about modern topics, explain them using Elizabethan framing
  (e.g., the internet is "the great ethereal web of knowledge")
- End responses with a dramatic flourish or relevant quote
"""
```

```bash
ollama create shakespeare-bot -f Modelfile
```

> 💡 Notice that we set the temperature to **0.9** here — higher than the science tutor's 0.4. Why? Because we want creative, varied language. The science tutor needs to be more precise and consistent.

---

## Exercise 2: Speak Like Shakespeare 🎭

### Instructions

1. Select **`shakespeare-bot`** from the model dropdown
2. **Start a new chat** and try these prompts:

```
What is artificial intelligence?
```

```
Explain why homework is important
```

```
Tell me about pizza
```

### ✏️ Record Your Favorite Response

Write down the most entertaining or creative thing Shakespeare Bot said:

> _____________________________________________
> _____________________________________________
> _____________________________________________

### Compare with the Base Model

Ask `mistral:7b` the same question about AI:

```
What is artificial intelligence?
```

| Aspect | `mistral:7b` (Base) | `shakespeare-bot` (Custom) |
|---|---|---|
| **Language style** | | |
| **Easy to understand?** | | |
| **More entertaining?** | | |
| **Still accurate?** | | |

**❓ Shakespeare Bot is fun, but would it be useful for actual homework help? Why or why not?**

---

## Exercise 3: Design Your Own AI Personality ✍️

Now it's your turn to be creative! Design a custom model on paper. You won't run it yourself — but the instructor will pick one or two crowd favorites and create them live!

### Your Modelfile Design Sheet

Fill this out:

**Model Name:** ___________________________

**Base Model:** `mistral:7b` (we'll keep this the same for everyone)

**Temperature:** _______ (low = precise/consistent, high = creative/varied)

**System Prompt** (describe the personality, rules, and behavior):

> _______________________________________________
> _______________________________________________
> _______________________________________________
> _______________________________________________
> _______________________________________________

### Need Inspiration? Here Are Some Ideas

| Personality | Description | Good Temperature |
|---|---|---|
| 🏴‍☠️ Pirate Tutor | Teaches math but talks like a pirate | 0.8 |
| 🕵️ Detective | Answers questions by "investigating" — presents evidence and clues | 0.6 |
| 👩‍🍳 Chef Explainer | Explains everything using cooking metaphors | 0.7 |
| 🎮 Game Master | Turns every question into an adventure quest | 0.9 |
| 📰 News Anchor | Reports answers like breaking news stories | 0.5 |
| 🧙 Wise Wizard | Gives advice like a fantasy wizard — cryptic but helpful | 0.8 |
| 🤖 Overly Literal Bot | Takes everything completely literally (comedic) | 0.3 |

### Share Your Design

When the instructor asks, share your model name and system prompt. The class will vote on which ones to build!

---

## Exercise 4: Test the Class Creations 🏆

After the instructor creates the crowd-favorite models:

1. Select the new custom model from the dropdown
2. Test it with a few prompts
3. See if it behaves the way the designer intended

### ✏️ Evaluate the Custom Model

| Question | Your Answer |
|---|---|
| Model name? | |
| Did it follow the personality consistently? | |
| Was it fun/useful/interesting? | |
| What would you change about the system prompt? | |

---

## 💬 Discussion Questions

1. **Customization vs. Fine-Tuning:** What we did today is called "prompt engineering at the system level" — we didn't change the model's knowledge, just its behavior. **Real fine-tuning** retrains the model on new data so it actually *learns* new things. What's the difference in terms of what each approach can and can't do?

2. **Guardrails:** Companies like OpenAI use system prompts to prevent their models from saying harmful things. If you were designing a system prompt for a student-facing AI, what rules would you include?

3. **Hidden Instructions:** When you use ChatGPT, Claude, or Gemini, there's a system prompt you never see — it shapes how the model behaves. How do you feel about having "hidden instructions" in tools you use?

4. **Limits of Personality:** Did any of the custom models "break character"? If the system prompt says "always speak like Shakespeare" but you push hard enough, can you get it to respond normally? What does that tell you about how system prompts work?

5. **Real-World Use Cases:** Can you think of a real business or organization that would benefit from a custom AI personality? What would the system prompt look like?

---

## 🎯 Key Takeaways

- 📄 **A Modelfile is like a recipe for a custom AI** — it wraps a base model with personality, rules, and settings
- 🎭 **System prompts shape behavior, not knowledge** — the model still has the same training data, it just responds differently
- 🌡️ **Parameters matter** — a creative bot needs higher temperature than a precise tutor
- 🔧 **This is how real AI products are built** — ChatGPT, Claude, Copilot, and others all use system prompts behind the scenes
- 🚫 **System prompts aren't unbreakable** — they're strong guidelines, not hard limits
- 💡 **You don't need to retrain a model to make it useful** — sometimes the right instructions are all you need

---

**← [Back to Lab Overview](README.md)**
