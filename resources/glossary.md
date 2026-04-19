# 🧠 AI Glossary — Teen-Friendly Edition

A no-nonsense guide to the buzzwords you'll hear in the world of AI. Each term gets a quick definition and an analogy to make it stick.

---

## AI / Artificial Intelligence

**Definition:** Software that can perform tasks that normally require human intelligence — like understanding language, recognizing images, or making decisions.

**Think of it like...** A calculator, but instead of just math, it can handle messy human stuff like conversations and creativity. It's not alive or conscious — it's really good pattern-matching.

---

## LLM / Large Language Model

**Definition:** A type of AI that's been trained on massive amounts of text so it can read, write, summarize, translate, and have conversations.

**Think of it like...** Someone who's read the entire internet and can remix everything they've read into new sentences. They don't truly *understand* — they're the world's best autocomplete.

---

## Model

**Definition:** The trained "brain" file that contains everything the AI has learned. Different models have different capabilities and sizes.

**Think of it like...** A save file from the world's longest study session. The model *is* the knowledge — packaged up and ready to answer questions.

---

## Parameter

**Definition:** A single learned number inside a model. Models have millions to hundreds of billions of parameters that together determine how the model responds.

**Think of it like...** One tiny knob on a mixing board with billions of knobs. Each knob is set to just the right level so the music (the AI's output) sounds good. More knobs = more detail, but also more expensive to run.

---

## Token

**Definition:** The chunks that an LLM breaks text into before processing it. A token is roughly ¾ of a word — "basketball" might be two tokens: "basket" + "ball."

**Think of it like...** Lego bricks for language. The AI doesn't read whole sentences at once — it snaps together one brick at a time. Every response costs tokens, and there's a limit to how many bricks you can use.

---

## Context Window

**Definition:** The maximum amount of text (measured in tokens) that a model can "see" at once — including your prompt and its response.

**Think of it like...** The model's short-term memory or working desk space. A small context window is like a tiny desk — you can only have a few pages open. A big one lets you spread out a whole textbook.

---

## Prompt

**Definition:** The text you type to tell the AI what you want. The quality of your prompt hugely affects the quality of the response.

**Think of it like...** Giving instructions to a very literal genie. If you say "write something cool," you'll get random stuff. If you say "write a 4-line rap about photosynthesis in the style of Drake," you'll get gold.

---

## Inference

**Definition:** The process of a trained model generating a response to your input. This is the "thinking" part when you ask it a question.

**Think of it like...** Taking an exam after studying. Training = studying, inference = taking the test. Every time you chat with an AI, it's running inference.

---

## Training / Fine-tuning

**Definition:** *Training* is teaching a model from scratch on huge datasets. *Fine-tuning* is taking an already-trained model and teaching it something more specific.

**Think of it like...** Training = going through all of K-12 education. Fine-tuning = taking an AP class on top of that. You don't start over — you just specialize.

---

## RLHF (Reinforcement Learning from Human Feedback)

**Definition:** A training technique where humans rate the AI's responses and those ratings are used to make the model better at giving helpful, safe answers.

**Think of it like...** Having a coach watch your game film and tell you what to do more of and what to stop doing. The AI tries stuff, humans say "good job" or "nope," and it adjusts.

---

## Hallucination

**Definition:** When an AI confidently generates information that is completely made up or factually wrong.

**Think of it like...** That friend who doesn't know the answer but refuses to say "I don't know" — they'll just make something up with total confidence. Always double-check important facts!

---

## Temperature

**Definition:** A setting (usually 0.0 to 2.0) that controls how random or creative the AI's responses are. Low = predictable, high = wild.

**Think of it like...** A "creativity dial." Turn it to 0 and the AI plays it super safe and boring. Crank it up and it gets creative, weird, and sometimes unhinged. For facts, keep it low. For stories, turn it up.

---

## Top-K / Top-P Sampling

**Definition:** Methods that control which words the model considers for the next token. *Top-K* picks from the K most likely words. *Top-P* picks from the smallest set of words whose probabilities add up to P.

**Think of it like...** Choosing what to eat. Top-K = "I'll only consider my top 5 favorite foods." Top-P = "I'll consider options until I'm 90% sure I'll like something." Both stop the AI from picking totally random words.

---

## GPU / VRAM

**Definition:** A *GPU* (Graphics Processing Unit) is a chip originally designed for gaming graphics but now essential for running AI models fast. *VRAM* is the GPU's dedicated memory.

**Think of it like...** The GPU is a kitchen with a ton of burners that can cook many things at once (parallel processing). VRAM is the counter space — bigger models need more counter space to be "open" and ready to cook.

---

## Multimodal

**Definition:** An AI model that can understand and/or generate more than just text — like images, audio, or video.

**Think of it like...** Most AIs are like pen pals — text only. A multimodal AI is more like a FaceTime call — it can see your photos, hear audio, and still chat with you.

---

## Embedding

**Definition:** A way of converting text (or images, etc.) into lists of numbers (vectors) so that similar things end up close together mathematically.

**Think of it like...** Giving every word a GPS coordinate in meaning-space. "Dog" and "puppy" end up in the same neighborhood, while "dog" and "algebra" are on different continents. This is how AI understands that things are related.

---

## RAG (Retrieval-Augmented Generation)

**Definition:** A technique where the AI first searches a knowledge base for relevant information, then uses that info to generate a more accurate answer.

**Think of it like...** Open-book exam vs. closed-book. Without RAG, the AI relies only on what it memorized during training. With RAG, it can look stuff up first — way more accurate for specific or up-to-date info.

---

## Agent / Agentic

**Definition:** An AI system that can take actions on its own — like searching the web, running code, or calling APIs — to accomplish a goal, rather than just generating text.

**Think of it like...** Regular AI = a smart advisor who gives you answers. An agent = a smart assistant who actually *does the thing* for you — books the flight, writes the code, sends the email.

---

## MCP (Model Context Protocol)

**Definition:** An open standard that lets AI models connect to external tools and data sources in a standardized way — like a universal adapter for AI capabilities.

**Think of it like...** USB-C for AI. Before MCP, every tool needed its own custom connector. MCP gives AI a standard plug so it can connect to databases, APIs, file systems, and more — all through one interface.

---

## Open Source vs. Proprietary Models

**Definition:** *Open source* models (like Llama, Mistral, Qwen) share their weights publicly so anyone can download, modify, and run them. *Proprietary* models (like GPT-4, Claude) are controlled by companies and accessed only through their APIs.

**Think of it like...** Open source = a recipe posted online that anyone can cook and tweak. Proprietary = a secret restaurant recipe you can only taste by eating there. Open source gives you freedom and control; proprietary often has more polish but less transparency.

---

## Quantization

**Definition:** A technique that shrinks a model by using less precise numbers (e.g., 4-bit instead of 16-bit), making it smaller and faster while losing a little quality.

**Think of it like...** Compressing a photo from full-res to a JPEG. The file gets *way* smaller and it still looks good — you just lose some fine detail. Quantization is why you can run serious AI models on a regular laptop or gaming PC instead of needing a data center.

---

*Now you know the lingo. Go impress your friends. 🚀*
