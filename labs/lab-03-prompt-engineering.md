# 🎨 Lab 3: The Art of Asking

## Learning Objectives

By the end of this lab, you will:
- ✅ Understand that **how you ask** matters just as much as **what you ask**
- ✅ Learn the key ingredients of a great prompt
- ✅ Be able to transform vague prompts into specific, effective ones
- ✅ Use a repeatable framework for writing good prompts

⏱️ **Estimated Time:** 20 minutes

🤖 **Suggested Model:** `llama3.2:3b`

---

## 🧠 Background: Why Prompts Matter

Imagine you walk up to someone and say "tell me about stuff." You'd get a confused look, right? But if you said "Can you explain to me how electric cars work, focusing on batteries, in about 2 minutes?" — you'd get a much better answer.

AI works the same way. The quality of your **prompt** (the text you type in) directly controls the quality of the response you get. This is such a big deal that **"prompt engineering"** is an actual job title now.

### 🏗️ The Prompt Blueprint

Great prompts usually include some combination of these ingredients:

| Ingredient | What It Does | Example |
|---|---|---|
| **Role** | Tells the AI *who* to be | "You are a biology teacher..." |
| **Task** | What you actually want done | "...write a summary of photosynthesis..." |
| **Context** | Background info or audience | "...for 9th-grade students..." |
| **Format** | How the output should look | "...as a bulleted list..." |
| **Constraints** | Limits and requirements | "...in under 150 words, using simple language." |

**Formula:** `Role + Task + Context + Format + Constraints = 🔥 Prompt`

You don't need *all* of these every time, but the more you include, the better your results tend to be.

---

## Exercise 1: Bad Prompt vs. Good Prompt — Writing ✍️

### Step 1: Try the Bad Prompt

Start a **new chat** and type:

```
write about dogs
```

Read the response. It's probably... fine? But unfocused, generic, and maybe not what you needed.

### Step 2: Try the Good Prompt

Start a **new chat** and type:

```
Write a 200-word informative paragraph about how guide dogs are trained, aimed at a high school audience. Include at least 2 specific training techniques.
```

### ✏️ Compare

| Dimension | Bad Prompt | Good Prompt |
|---|---|---|
| **Was it useful/informative?** | | |
| **Was it focused on a topic?** | | |
| **Was the length appropriate?** | | |
| **Did it include specific details?** | | |
| **Would you use it in a school paper?** | | |

**❓ What made the good prompt better? Which ingredients from the Blueprint did it use?**

<details>
<summary>💡 Click to check your answer</summary>

The good prompt used:
- **Task:** Write an informative paragraph
- **Context:** About guide dog training, for a high school audience
- **Constraints:** 200 words, at least 2 specific techniques

</details>

---

## Exercise 2: Bad Prompt vs. Good Prompt — Code 💻

### Step 1: Try the Bad Prompt

New chat:

```
fix this code
```

The model has no code to fix! Notice what it does — it might make something up, ask you questions, or just give generic advice.

### Step 2: Try the Good Prompt

New chat:

```
Review this Java method for bugs. The method should take an array of doubles and return the average, but it crashes on empty arrays. Suggest a fix with explanation.

public static double average(double[] numbers) {
    double total = 0;
    for (double num : numbers) {
        total += num;
    }
    return total / numbers.length;
}
```

### ✏️ Compare

| Dimension | Bad Prompt | Good Prompt |
|---|---|---|
| **Did the AI understand what you needed?** | | |
| **Did it give actionable advice?** | | |
| **Could you directly use the response?** | | |

**❓ What ingredients made the good prompt work?**

<details>
<summary>💡 Click to check your answer</summary>

The good prompt used:
- **Task:** Review for bugs, suggest a fix
- **Context:** Java method, should return the average, crashes on empty arrays
- **Format:** Fix with explanation
- **Constraints:** Included the actual code

</details>

---

## Exercise 3: Bad Prompt vs. Good Prompt — Role Playing 🎭

### Step 1: Try the Bad Prompt

New chat:

```
tell me about history
```

Yeah... that's the entire history of everything. Good luck with that.

### Step 2: Try the Good Prompt

New chat:

```
You are a history teacher preparing a 2-minute summary of the causes of World War I for 10th graders. Focus on the 3 most important causes and use simple language.
```

### ✏️ Compare

| Dimension | Bad Prompt | Good Prompt |
|---|---|---|
| **Was the response focused?** | | |
| **Appropriate for a student audience?** | | |
| **Well-organized?** | | |
| **Useful for studying?** | | |

**❓ Which Blueprint ingredients were used? Why does giving the AI a "role" help?**

<details>
<summary>💡 Click to check your answer</summary>

The good prompt used:
- **Role:** History teacher
- **Task:** Prepare a 2-minute summary of WWI causes
- **Context:** For 10th graders
- **Constraints:** 3 most important causes, simple language

Giving a role helps because it sets the *tone*, *expertise level*, and *perspective* for the response.

</details>

---

## Exercise 4: Upgrade These Prompts 🔧

Now it's your turn! Take each bad prompt below and rewrite it using the Blueprint. Then test both versions and compare.

### Prompt A

**Bad version:**
```
write a poem
```

**Your upgraded version:** *(Write it below, then test both)*

```
[Your improved prompt here]
```

> 💡 Hint: What kind of poem? About what? How long? What mood? For what audience?

---

### Prompt B

**Bad version:**
```
help me study
```

**Your upgraded version:**

```
[Your improved prompt here]
```

> 💡 Hint: Study what subject? What's the exam format? What do you struggle with? What should the AI produce — flashcards, a summary, practice questions?

---

### Prompt C

**Bad version:**
```
make a website
```

**Your upgraded version:**

```
[Your improved prompt here]
```

> 💡 Hint: What kind of website? What technology? What features? What should it look like? How much code?

---

## Exercise 5 (Bonus): The Mega Prompt 🚀

Try building the most detailed, effective prompt you can using all five Blueprint ingredients. Pick any topic you're interested in.

**Template to fill in:**

```
You are a [ROLE].

Your task is to [TASK].

Context: [CONTEXT — who is this for, what's the situation?]

Format: [FORMAT — list, essay, code, table, dialogue?]

Constraints:
- [CONSTRAINT 1]
- [CONSTRAINT 2]
- [CONSTRAINT 3]
```

Test your mega prompt and see if the response matches what you had in mind!

---

## 💬 Discussion Questions

1. **Which ingredient made the biggest difference?** Role, task, context, format, or constraints?

2. **Is there such a thing as a prompt that's *too* detailed?** What might happen if your prompt is 500 words long?

3. **How does prompt engineering compare to Google search skills?** Are they similar or different?

4. **Should AI companies make models that work well with bad prompts?** Or is learning to prompt well a skill everyone should develop?

5. **Think about a real task you do for school.** How would you prompt an AI to help you with it? (Remember: AI should help you learn, not do your work for you!)

---

## 🎯 Key Takeaways

- 🎯 **Vague prompts get vague answers** — specificity is your best friend
- 🏗️ **Use the Blueprint:** Role + Task + Context + Format + Constraints
- 🎭 **Giving the AI a role** changes the tone, expertise, and perspective of the response
- 📏 **Constraints prevent rambling** — tell the AI how long, how many, or what to focus on
- 🔄 **Prompt engineering is iterative** — your first prompt doesn't have to be perfect, refine and retry
- 💼 **This is a real-world skill** — companies hire prompt engineers, and knowing how to talk to AI tools effectively makes you more productive

---

**Next up: [Lab 4: Catching AI Lies →](lab-04-hallucination-detection.md)**
