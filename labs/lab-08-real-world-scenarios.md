# 🌍 Lab 8: Real-World AI Scenarios

[← Back to Lab Overview](README.md)

## Learning Objectives

By the end of this lab, you will:
- ✅ Use AI to solve **real problems you actually have** — not just toy examples
- ✅ Practice writing prompts for **practical, everyday tasks**
- ✅ Learn when AI output is **good enough to use** vs. when it needs heavy editing
- ✅ Build the habit of **customizing AI output** instead of accepting it blindly
- ✅ See AI as a **productivity tool**, not just a curiosity

⏱️ **Estimated Time:** 20 minutes

🤖 **Suggested Model:** `mistral:7b`

---

## 🧠 Background: AI as a Daily Tool

Up to this point in the workshop, you've been experimenting — testing what AI can and can't do, comparing models, catching hallucinations. That's important. But the real question is:

**Can AI actually help you get stuff done?**

The answer is yes — if you know how to ask. People use AI every day to draft emails, summarize articles, plan events, debug code, brainstorm ideas, and more. The key is treating AI like a **first draft machine**: it gives you a starting point that you then refine, fact-check, and personalize.

In this lab, every exercise is something you might genuinely use in your life **today**. Try each scenario with the example prompt first, then customize it for your own situation.

### The Real-World Workflow

```
1. Define what you need        →  What's the task?
2. Write a specific prompt      →  Give AI context, format, constraints
3. Get the first draft          →  AI generates something
4. Review and customize         →  YOU make it actually good
5. Use it (or iterate again)    →  Ship it or refine further
```

---

## Exercise 1: Build a Study Guide 📚

### Why This Matters

You have a test coming up. You have a textbook, notes, and slides — but no clear, organized summary of what you actually need to know. AI can help you build one in minutes instead of hours.

### Step 1: Try the Example Prompt

Start a **new chat** and type:

```
Create a study guide for a high school biology unit on cell structure and function. Include:
- A summary of the 5 most important concepts
- Key vocabulary with short definitions (10 terms)
- 3 common exam questions with brief answer outlines
- A "don't forget" section with things students often miss

Keep it concise — this should fit on 2 pages if printed.
```

Read the response. Notice how structured and useful it is compared to just asking "help me study biology."

### Step 2: Make It Yours

Now think about **your hardest class right now**. What topic or unit are you struggling with? Rewrite the prompt for your actual situation. For example:

- Swap "biology / cell structure" for your real subject and topic
- Add specific areas you're confused about
- Mention what format your test will be (multiple choice, essay, etc.)

Start a **new chat** and try your customized version.

### ✏️ Reflect

| Question | Your Answer |
|---|---|
| What subject/topic did you choose? | |
| Was the study guide accurate? (Spot-check 2–3 facts) | |
| What would you change or add? | |
| Would you actually use this to study? Why or why not? | |

---

## Exercise 2: Draft a Club Event Announcement 📢

### Why This Matters

You're in a club, team, or group and need to get the word out about an event. Writing announcements that are clear, engaging, and have all the details is harder than it sounds — especially when you're staring at a blank page. AI can get you 80% of the way there in seconds.

### Step 1: Try the Example Prompt

Start a **new chat** and type:

```
Write an announcement for a high school Coding Club's end-of-year hackathon. Details:
- Event: 4-hour hackathon, build anything you want
- Date: Saturday, June 14th, 10am - 2pm
- Location: School library, Room 204
- Free pizza and snacks provided
- Teams of 2-4, or come solo and find a team
- No experience needed — beginners welcome
- Sign up by June 10th with Mrs. Chen

Make it fun and energetic. Keep it under 150 words. Include a catchy opening line.
```

### Step 2: Make It Yours

Think about a **real event** you need to promote — it could be for a club, a team, a fundraiser, a party, or anything else. Rewrite the prompt with your actual details.

Tips for your custom prompt:
- Include the **tone** you want (formal, casual, hype, funny)
- Specify **where** this will be posted (Instagram caption, school announcements, flyer, group chat)
- Include **all the logistical details** so the AI doesn't make them up

Start a **new chat** and try it.

### ✏️ Reflect

| Question | Your Answer |
|---|---|
| What event did you write about? | |
| Could you post this as-is, or did it need edits? | |
| What did AI get right about the tone? | |
| What did you have to fix or change? | |

---

## Exercise 3: Debug Your Code 🐛

### Why This Matters

If you've ever written code — in a class, for a project, or just messing around — you know the frustration of a bug you can't find. AI is genuinely great at spotting common mistakes and explaining what went wrong. Professional developers use it every day.

### Step 1: Try the Example Prompt

Start a **new chat** and paste this:

```
I'm a high school student on an FRC robotics team and I code in Java. This code is supposed to ask the user for 5 test scores, then print the average. But it always prints 0 as the average. Can you find the bug and explain what's wrong?

import java.util.Scanner;

public class ScoreAverage {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int total = 0;
        int count = 0;

        for (int i = 0; i < 5; i++) {
            System.out.print("Enter score: ");
            int score = scanner.nextInt();
            total = total + score;
            count = count + 1;
        }

        int average = total / count;
        System.out.println("Your average is: " + average);
    }
}
```

Read the explanation. Did the AI correctly identify the issue? (Hint: integer division in Java truncates the decimal — `total / count` does integer math when both are `int`.)

### Step 2: Try It With Your Own Code

If you have a coding project — for a class, a personal project, or anything else — try pasting some code that isn't working and asking AI for help. Use a prompt structure like:

```
I'm working on [language/project]. This code is supposed to [what it should do],
but instead it [what's going wrong]. Here's the code:

[paste your code]

Can you find the bug, explain why it happens, and show me the fix?
```

> **Don't have code to debug?** That's fine — try asking AI to explain the bug in the example above in a different way, or ask it to add error handling to the corrected version.

### ✏️ Reflect

| Question | Your Answer |
|---|---|
| Did AI correctly identify the bug? | |
| Was the explanation clear enough to learn from? | |
| Did you try it with your own code? What happened? | |
| Would you trust AI-suggested code fixes without testing them? Why or why not? | |

---

## Exercise 4: Plan Something Fun 🏋️✈️

### Why This Matters

AI is surprisingly good at planning and organizing — workouts, trips, meal plans, schedules, you name it. It can take your constraints (time, budget, preferences) and generate a structured plan you can actually follow.

### Step 1: Pick Your Scenario

Choose **one** of the two options below (or do both if you have time):

#### Option A: Create a Workout Plan

Start a **new chat** and type:

```
Create a 4-week beginner workout plan for a high school student who wants to get stronger but only has 30 minutes, 3 days a week. No gym equipment — bodyweight exercises only.

For each workout, include:
- Warm-up (2 minutes)
- Main exercises with sets and reps
- Cool-down stretch

Make it progressively harder each week. Keep the language simple and motivating.
```

#### Option B: Plan a Trip Itinerary

Start a **new chat** and type:

```
Plan a 3-day weekend trip itinerary for a group of high school friends visiting Chicago on a $200 budget per person. Include:
- Where to stay (budget-friendly)
- Must-see spots and activities (mix of free and cheap)
- Where to eat (nothing over $15/meal)
- A realistic schedule with travel time between spots

Make it fun — we're 17, not 70.
```

### Step 2: Customize It

Now make it **your** plan:
- **Workout:** Adjust for your fitness level, available equipment, goals, and schedule
- **Trip:** Change the destination, budget, group size, and interests

Start a **new chat** and try your personalized version.

### ✏️ Reflect

| Question | Your Answer |
|---|---|
| Which option did you pick (workout / trip / both)? | |
| How realistic was the plan? | |
| What did AI get wrong or overlook? | |
| Did specifying constraints (budget, time, equipment) improve the output? | |

---

## Exercise 5: Summarize for a Presentation 📋

### Why This Matters

You have a class presentation next week. You found a great article, but it's 2,000 words long and you need the key points in 2 minutes. AI can read, extract, and reorganize information faster than you can skim.

### Step 1: Try the Example Prompt

Start a **new chat** and type:

```
Summarize the following topic as if you're preparing a 2-minute class presentation for high school students:

Topic: How CRISPR gene editing works and why it matters.

Give me:
- A 1-sentence "hook" to open the presentation
- 3 key points with 1-2 sentence explanations each
- 1 real-world example or application
- A closing statement that makes the audience think

Use simple, clear language — no jargon.
```

### Step 2: Try It With a Real Article

Find an article you actually need to read for a class (or copy-paste a few paragraphs from one). Then use a prompt like:

```
Summarize this article for a class presentation. Pull out the 3-4 most important points and explain each in 1-2 sentences a high school student would understand. End with one thought-provoking question for class discussion.

[paste article text or key paragraphs here]
```

> **Tip:** If the article is too long to paste, summarize the topic and key arguments yourself in a few sentences, then ask AI to help you structure it into presentation format.

### ✏️ Reflect

| Question | Your Answer |
|---|---|
| What topic did you summarize? | |
| Did the AI miss any important points? | |
| Was the "hook" actually good enough to use? | |
| How much editing would this need before you present it? | |

---

## Comparison: AI Output Quality Across Scenarios

Look back at all five exercises. How useful was AI for each type of task?

| Scenario | Usefulness (1-5) | Accuracy (1-5) | How Much Editing Needed? |
|---|---|---|---|
| Study Guide | | | None / Some / Major |
| Event Announcement | | | None / Some / Major |
| Code Debugging | | | None / Some / Major |
| Workout/Trip Plan | | | None / Some / Major |
| Presentation Summary | | | None / Some / Major |

**Which task was AI best at? Which needed the most human editing?**

Your answer: _______________________________________________

---

## 🌟 Bonus: Choose Your Own Adventure

You've tried five scenarios we picked. Now it's your turn.

**Think of a real problem or task in your life right now** where AI might help. It could be anything:

- Writing a college application essay draft
- Planning your weekly schedule
- Learning how to cook a specific recipe
- Writing a difficult text or email
- Translating something for a family member
- Brainstorming ideas for a project
- Creating flashcards for a test
- Writing a cover letter for a job application
- Anything else you genuinely need help with

### Your Task

1. **Identify the task** — what do you need done?
2. **Write the prompt** — use everything you've learned about giving AI role, context, format, and constraints
3. **Run it** and evaluate the output
4. **Refine** — send a follow-up message to improve the result

### ✏️ Record Your Adventure

| Item | Your Response |
|---|---|
| What real-world task did you choose? | |
| What prompt did you write? (summarize it) | |
| Rate the first response (1-5 stars) | |
| What follow-up prompt did you send to improve it? | |
| Rate the improved response (1-5 stars) | |
| Would you actually use this output in real life? | |

---

## 💬 Discussion Questions

1. **Which scenario felt most useful to you personally?** Do you think you'll actually use AI for that task going forward?

2. **AI gave you a "first draft" every time.** How much work was it to turn those drafts into something you'd actually use? Is that time savings worth it?

3. **Did you notice AI making assumptions** about your situation? (Example: suggesting exercises you can't do, restaurants that might not exist, or study tips for the wrong level.) How do you guard against that?

4. **Some people worry that using AI for schoolwork is "cheating."** Where do you draw the line between using AI as a tool (like a calculator or spell-check) and having AI do your work for you?

5. **If you had unlimited access to AI tools**, what's the first real problem in your life you'd throw at it?

---

## 🎯 Key Takeaways

- 🛠️ **AI is a practical tool** — it can help with real tasks like studying, writing, planning, coding, and organizing
- 📝 **Treat AI output as a first draft** — it gets you started fast, but you still need to review, fact-check, and personalize
- 🎯 **Specific prompts get specific results** — the more context and constraints you give, the more useful the output
- 🔄 **Iteration makes it better** — your first prompt rarely gives you the perfect answer; follow-up prompts refine the result
- 🧠 **You are still the expert on your life** — AI doesn't know your classes, your friends, your goals, or your preferences unless you tell it
- ⚖️ **Use it responsibly** — AI is a power tool, not a shortcut to skip learning; the goal is to work smarter, not to stop thinking

---

**Next up: [Lab 9 →](lab-09-future-of-ai.md)**
