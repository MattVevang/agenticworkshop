# 🚀 Open WebUI — Quick Reference Card

Everything you need to know to start chatting with AI models in the workshop.

---

## 🌐 Opening Open WebUI

1. Open a web browser (Chrome, Firefox, or Edge)
2. Go to: **`http://[server-ip]:3000`** (your instructor will give you the actual IP address)
3. Log in with the credentials provided by your instructor

> **Tip:** Bookmark this page so you can get back quickly!

[Screenshot: Open WebUI login page]

---

## 💬 Starting a New Chat

1. Click the **"New Chat"** button in the top-left corner (or the `+` icon)
2. Type your message in the text box at the bottom
3. Press **Enter** or click the **Send** button

[Screenshot: New chat button and message input area]

> **Tip:** Each chat is a separate conversation. The model doesn't remember things from other chats!

---

## 🔄 Switching Models

1. Look at the **model dropdown** at the top of the chat
2. Click it to see all available models
3. Select the model you want to use

[Screenshot: Model selection dropdown showing available models]

**Models you might see:**

| Model | Size | Good For |
|-------|------|----------|
| `tinyllama:1.1b` | ~640 MB | Fast responses, simple tasks — great for testing |
| `llama3.2:3b` | ~2 GB | Good balance of speed and quality |
| `mistral:7b` | ~4 GB | Strong general-purpose model |
| `llava:7b` | ~5 GB | Can understand images (multimodal!) |

> **Tip:** Bigger models are smarter but slower. Start small and size up if you need better answers!

---

## ⚙️ Adjusting Settings

### Temperature

1. Click the **settings/parameters icon** (gear or sliders icon near the model dropdown)
2. Find the **Temperature** slider
3. Adjust it:
   - **0.0–0.3** → Focused & factual (good for homework help, code)
   - **0.4–0.7** → Balanced (good default)
   - **0.8–1.5** → Creative & unpredictable (good for stories, brainstorming)

[Screenshot: Temperature slider in settings panel]

> **Tip:** If the AI keeps giving boring answers, turn the temperature up. If it's being too wild, turn it down.

---

## 🖼️ Uploading Images (Multimodal Models)

Some models (like `llava`) can look at images!

1. Make sure you've selected a **multimodal model** (e.g., `llava:7b`)
2. Click the **attachment/upload icon** (📎) next to the message input
3. Select an image from your computer
4. Type your question about the image (e.g., "What's in this image?" or "Describe what you see")
5. Press **Enter**

[Screenshot: Image upload button and image attached to a message]

> **Note:** Regular text-only models (like `tinyllama`, `mistral`) can't see images — they'll ignore them or give an error.

---

## 💡 Tips for Getting Good Results

### Be Specific
- ❌ "Tell me about space"
- ✅ "Explain how black holes form in 3 sentences, for a high school student"

### Give It a Role
- ✅ "You are a friendly science tutor. Explain photosynthesis step by step."

### Ask for a Format
- ✅ "Give me a comparison of Python vs JavaScript as a bullet-point list"
- ✅ "Write this as a table with pros and cons"

### Iterate
- If the first answer isn't great, follow up! Say "Make it shorter," "Explain it simpler," or "Give me an example."

### Use System Prompts
- Some models support a system prompt — this sets the AI's personality/instructions for the whole chat
- Try: "You are a sarcastic but helpful coding tutor who explains things with memes"

---

## 🔧 Troubleshooting

### "The response is really slow..."
- You're probably using a large model. Try switching to a smaller one (e.g., `tinyllama:1.1b`)
- The server might be busy if many students are using it at once — be patient!
- First response after switching models is often slow because the model has to load into memory

### "The model isn't responding at all..."
- Check that you're connected to the right URL
- Try refreshing the page
- Make sure you've selected a model from the dropdown
- Ask your instructor — the server might need a restart

### "The model says weird/wrong things..."
- That's hallucination! AI doesn't always get facts right
- Try rephrasing your question with more context
- Lower the temperature for more focused answers
- Cross-check important facts with a real source

### "I can't upload images..."
- Make sure you're using a multimodal model (like `llava`)
- Check that the file is a common image format (PNG, JPG, GIF, WebP)
- Try a smaller image if the upload seems stuck

### "The response cut off in the middle..."
- The model may have hit its token limit
- Type "continue" or "keep going" to have it pick up where it left off
- Try asking for a shorter response: "Explain in 5 sentences or less"

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| **Enter** | Send message |
| **Shift + Enter** | New line (without sending) |
| **Ctrl + Shift + O** | Open settings |
| **Ctrl + Shift + Backspace** | Delete current chat |

---

*Have fun exploring! Remember — there are no dumb questions, but there are definitely funny prompts. Try some! 🎉*
