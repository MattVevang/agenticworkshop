# 🎭 Lab 5: Creative & Multimodal AI

## Learning Objectives

By the end of this lab, you will:
- ✅ Explore AI's **creative writing** capabilities across different styles and genres
- ✅ Experiment with **multimodal AI** (models that can understand images)
- ✅ Test AI's ability to **generate code** and understand its limitations
- ✅ See how different models handle creative tasks differently

⏱️ **Estimated Time:** 20 minutes

---

## Part 1: Creative Writing 🖊️

AI isn't just for answering questions — it can be a surprisingly fun creative collaborator. Let's push its creativity.

### Exercise 1: Genre Remix 🎬

Take one premise and generate story openings in completely different genres. This shows how AI adapts tone, vocabulary, and style.

**Use `llama3.2:3b` for this section.**

#### Step 1: Science Fiction

New chat:

```
Write the opening paragraph (about 100 words) of a science fiction story with this premise: A teenager discovers they can pause time, but only for 30 seconds at a time.
```

#### Step 2: Horror

New chat:

```
Write the opening paragraph (about 100 words) of a horror story with this premise: A teenager discovers they can pause time, but only for 30 seconds at a time.
```

#### Step 3: Comedy

New chat:

```
Write the opening paragraph (about 100 words) of a comedy with this premise: A teenager discovers they can pause time, but only for 30 seconds at a time.
```

#### Step 4: Mystery/Thriller

New chat:

```
Write the opening paragraph (about 100 words) of a mystery/thriller with this premise: A teenager discovers they can pause time, but only for 30 seconds at a time.
```

### ✏️ Reflect

| Question | Your Answer |
|---|---|
| Which genre did the AI handle best? | |
| Did the tone actually change between genres? | |
| Which opening would you most want to keep reading? | |
| Did any of them feel "generic" or authentic? | |

---

### Exercise 2: Science Rap 🎤

Let's see if AI can get creative with both content and form.

New chat:

```
Write a 12-line rap verse about photosynthesis. It should be scientifically accurate, have a consistent rhyme scheme, and feel like it could actually be performed. Include at least 3 real science terms.
```

**❓ Does it rhyme? Is it scientifically accurate? Would you actually want to perform it?**

**Try a follow-up** (same chat):

```
Now rewrite it in the style of a lullaby instead
```

**❓ How did the tone shift? Same facts, totally different vibe?**

---

### Exercise 3: Historical Conversation 🗣️

New chat:

```
Write a short dialogue (about 200 words) between Marie Curie and Nikola Tesla meeting at a cafe in 1905. They're debating whether science or engineering will change the world more. Keep their personalities and speech patterns historically plausible.
```

### ✏️ Reflect

| Question | Your Answer |
|---|---|
| Did the characters feel distinct from each other? | |
| Were the historical details plausible? | |
| Was it entertaining to read? | |
| Did it capture their real areas of expertise? | |

---

## Part 2: Multimodal AI — Images + Text 🖼️

Time to try something different. The **`llava:7b`** model can understand images — you can upload a picture and ask questions about it.

### ⚠️ Switch Your Model

**Select `llava:7b` from the model dropdown** for this section.

### Exercise 4: Image Analysis

#### Step 1: Upload and Analyze

1. Start a **new chat** with `llava:7b`
2. Find an image to test with. Options:
   - Take a photo of the classroom with your phone and upload it
   - Use a screenshot of something on your screen
   - Search for an interesting image online and save/upload it
3. Upload the image to the chat (look for a 📎 or image upload button)
4. Type:

```
Describe what you see in this image in detail. What objects, people, or activities are visible?
```

### ✏️ Record Your Results

| Question | Your Observation |
|---|---|
| How accurate was the description? | |
| Did it miss anything obvious? | |
| Did it identify anything incorrectly? | |
| How much detail did it provide? | |

#### Step 2: Ask Follow-Up Questions

In the same chat, try asking:

```
What mood or atmosphere does this image convey?
```

Then try:

```
If you had to write a one-sentence caption for this image, what would it be?
```

---

### Exercise 5: Multimodal vs. Text-Only

Let's compare what happens when you describe an image to a text-only model vs. showing it to a multimodal model.

#### Option A: With Image (llava:7b)

1. Pick an interesting image (a complex scene works best)
2. Upload it to `llava:7b` and type:

```
What is happening in this image? List 5 specific observations.
```

#### Option B: Without Image (llama3.2:3b)

1. Switch to `llama3.2:3b` (text only)
2. In a new chat, try to describe the same image yourself and ask:

```
I have a photo that shows [your description of the image]. What do you think might be happening in this scene? List 5 possible observations.
```

**❓ How did the responses differ? Was the multimodal model's response more accurate? Did the text-only model "hallucinate" details about an image it never actually saw?**

---

## Part 3: Code Generation 💻

AI models can generate functional code — let's test the limits.

### Exercise 6: Interactive Web Page

**Use `llama3.2:3b` for this section** (handles code well and responds quickly).

New chat:

```
Create a simple HTML page with these features:
1. A heading that says "Color Randomizer"
2. A button labeled "Change Background"
3. When clicked, the button changes the page's background to a random color
4. Display the current color's hex code on the page

Put all HTML, CSS, and JavaScript in a single file.
```

### Testing the Code

1. Copy the generated HTML code
2. Open a text editor (Notepad works fine)
3. Paste the code and save as `colortest.html`
4. Open the file in your browser
5. Click the button — does it work?

### ✏️ Record Your Results

| Question | Your Observation |
|---|---|
| Did the code run without errors? | |
| Did the button actually change the background? | |
| Was the hex code displayed correctly? | |
| Was the code well-organized? | |

---

### Exercise 7: Code Quality Comparison

You already have a `llama3.2:3b` result from Exercise 6. Now run the same prompt with **`llama3.2:1b`** to see how the smallest model handles code generation. Compare it against your Exercise 6 result.

> 💡 If you want a fresh side-by-side comparison, rerun `llama3.2:3b` as well.

### ✏️ Compare

| Dimension | llama3.2:1b | llama3.2:3b |
|---|---|---|
| **Code runs without errors?** | | |
| **All features present?** | | |
| **Code is clean/readable?** | | |
| **Used modern best practices?** | | |

---

## 💬 Discussion Questions

1. **Was the AI "creative" in the genre exercise**, or was it just remixing patterns it saw in training data? What does "creativity" even mean for AI?

2. **Would you use AI as a writing collaborator?** Where's the line between "AI-assisted" and "AI-generated" writing?

3. **How useful was the multimodal model?** What real-world applications can you imagine for AI that understands images?

4. **The AI generated working code.** Does that mean it "understands" programming? What's the difference between generating code and understanding code?

5. **Could AI-generated code be dangerous?** What if it looks correct but has subtle security bugs?

---

## 🎯 Key Takeaways

- 🎨 **AI can adapt to different creative styles** — but it tends to lean on patterns and tropes from its training data
- 🖼️ **Multimodal models can see and describe images** — opening up applications beyond text
- 💻 **AI can generate working code** — but always test it yourself, especially for anything important
- 📏 **Larger models produce better code** — smaller models often miss features or introduce bugs
- 🤝 **AI is a creative collaborator, not a replacement** — the best results come from human + AI working together
- ✅ **Always verify AI output** — whether it's a "fact," a story detail, or a line of code

---

**Next up: [Lab 6: Local vs. Cloud AI →](lab-06-local-vs-cloud-discussion.md)**
