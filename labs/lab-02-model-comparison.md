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

## Exercise 1: The Context Challenge 🧩

> 💡 **Why this exercise is different:** Instead of comparing writing style, we're testing something deeper — can each model **hold onto important data** when it's buried under a wall of text? This reveals a fundamental difference between model sizes that you can't see from simple prompts.

### Instructions

Copy the **entire prompt below** and paste it into each model. **Don't modify it** — the long middle section is intentional. It contains FRC scouting data at the top, then several paragraphs about FIRST history (filler that the model must ignore), then two questions at the bottom.

> ⚠️ **Important:** Start a **new chat** for each model. Make sure the **Temperature** slider is set to **0** (far left) in the chat settings so results are consistent.

**Prompt** (copy everything inside this block):

```
Here are the scouting results from our FRC regional competition. Study them carefully:

MATCH SCOUTING DATA:
- Match 1: Team 4150 scored 45 auto + 82 teleop = 127 total
- Match 2: Team 2876 scored 38 auto + 91 teleop = 129 total
- Match 3: Team 4150 scored 52 auto + 76 teleop = 128 total
- Match 4: Team 1234 scored 41 auto + 88 teleop = 129 total
- Match 5: Team 2876 scored 35 auto + 95 teleop = 130 total

The FIRST Robotics Competition has a rich history dating back to 1992 when it was founded by Dean Kamen. The first competition had just 28 teams competing in a relatively simple game. By 2024, FIRST has grown to include over 3,600 FRC teams worldwide, with regional events held across the United States, Canada, Australia, Israel, Turkey, and many other countries. The competition changes its game every year, with each season bringing new challenges that test teams' engineering, programming, and strategic thinking abilities. Past games have included challenges like shooting balls into goals, climbing structures, placing game pieces on scoring nodes, and balancing on platforms. The build season typically begins in early January when the new game is revealed at a worldwide kickoff event, and teams have about six weeks to design, build, and test their robots before competition season begins.

FIRST teams are organized into several programs based on age group. FIRST LEGO League introduces students aged 4-16 to STEM concepts through themed challenges using LEGO elements. FIRST Tech Challenge serves students in grades 7-12 with a more accessible robotics platform that uses Android-based controllers. FIRST Robotics Competition, the flagship program, challenges high school students to build industrial-sized robots weighing up to 125 pounds. Each program emphasizes FIRST's core values of discovery, innovation, impact, inclusion, teamwork, and fun. The organization has distributed over $80 million in college scholarships to FIRST alumni, and studies show that FIRST participants are significantly more likely to pursue careers in science and technology.

The strategy aspect of FRC is often what separates good teams from great ones. Alliance selection at competitions involves the top eight seeded teams choosing two alliance partners each for elimination rounds. Scouting data is crucial for making informed alliance selections. Teams use various methods to collect scouting data, from paper forms to sophisticated digital systems with tablets and real-time databases. Some teams even use computer vision to automatically track robot performance during matches. The most successful teams combine quantitative scouting data with qualitative observations about robot reliability, driver skill, and defensive capability. Strategy also extends to the matches themselves, where alliance captains must decide which robots play offense versus defense, how to allocate scoring responsibilities, and when to prioritize climbing or other endgame activities.

The programming side of FRC robots has evolved significantly over the years. Early robots used simple microcontrollers with limited programming capabilities. Today's FRC robots run on the roboRIO, a National Instruments controller that supports Java, C++, and LabVIEW programming. Many teams also use coprocessors like Raspberry Pi or Jetson Nano for computer vision processing. The WPILib software library provides a comprehensive framework for robot programming, including support for PID control, trajectory following, and networked communications. Teams increasingly use advanced techniques like path planning, machine learning for game piece detection, and autonomous routines that can score multiple game pieces without human input.

Now, based ONLY on the MATCH SCOUTING DATA at the very beginning:

1. Which team had the highest TELEOP score, and in which match?
2. How many total points did Team 2876 score across ALL their matches combined?
```

**Run it through these models** (start a **new chat** each time):

1. `llama3.2:1b` (smallest)
2. `llama3.2:3b` (medium)
3. `llama3.1:8b` (largest)

### ✏️ Fill In Your Comparison Table

| Dimension | llama3.2:1b | llama3.2:3b | llama3.1:8b |
|---|---|---|---|
| **Q1: Highest teleop — correct team and match?** | | | |
| **Q2: Team 2876 total points — correct answer?** | | | |
| **Did it claim data was "not provided"?** | | | |
| **Did it show its math/reasoning?** | | | |
| **Speed** (fast / medium / slow) | | | |

### ✅ Answer Key (check after running all three!)

The correct answers from the scouting data:
1. **Team 2876** scored **95 teleop** points in **Match 5**
2. Team 2876 played Matches 2 and 5: **129 + 130 = 259 total points**

> 🔍 **What you'll likely see:** A clear staircase of capability:
> - The **1b model** struggles with both questions — it may confuse teleop/total scores and fail the addition
> - The **3b model** can handle the straightforward addition (Q2) but still fails to identify the specific match and score type for Q1
> - The **8b model** nails both — it correctly parses which score column to look at AND does the math
>
> This demonstrates that larger models are better at **precise data extraction** (finding specific values in specific columns) and at **following multi-step instructions** (find all matches for X team, then sum their totals).

### 🤔 Reflection

- Why could the 3b model handle addition (Q2) but not find the highest teleop score (Q1)?
- What makes Q1 harder? (Hint: it requires comparing across rows AND reading the right column)
- If you were building a scouting app that analyzed match data, which model size would you want?

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

3. **For which task did model size matter most?** The context challenge, the code, or the pros/cons analysis?

4. **How do you think models like ChatGPT or Claude compare in size** to what you just tested? (Hint: think *hundreds of billions* of parameters, or more)

5. **If bigger is generally better, why would anyone use small models?** Think about cost, speed, privacy, and offline use.

6. **Why did we compare models from the same family?** What would change if we compared a 3B model from one company to a 3B model from another?

---

## 🎯 Key Takeaways

- 📏 **Model size matters, but it's not everything** — the best model depends on your task
- ⚡ **Smaller models are faster** — sometimes fast and good enough beats slow and perfect
- 🧠 **Larger models handle context and complexity better** — they're stronger at reasoning over long inputs, following instructions, and covering edge cases
- 🔍 **Don't trust AI answers blindly** — even big models make mistakes, so always verify important results
- 🎯 **Match the model to the job** — you don't need an 8B-parameter model to generate a haiku
- 🏎️ **Same family, different sizes = fair comparison** — when only size changes, you can clearly see the tradeoffs
- 💰 **In the real world, bigger models cost more** — so choosing wisely saves money and energy

---

**Next up: [Lab 3: The Art of Asking →](lab-03-prompt-engineering.md)**
