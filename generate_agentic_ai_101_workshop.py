#!/usr/bin/env python3
"""Generate an AI 101 + Agentic Tools workshop deck (.pptx).

Usage:
    pip install python-pptx
    python generate_agentic_ai_101_workshop.py

Output:
    Agentic_AI_101_Workshop.pptx (next to this script)
"""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt

# ---------------------------------------------------------------------------
# Theme: "Neon Mission Control"
# ---------------------------------------------------------------------------
BG = RGBColor(0x0B, 0x10, 0x1A)            # near-black blue
SURFACE = RGBColor(0x13, 0x1B, 0x2E)       # panel background
PRIMARY = RGBColor(0x22, 0xD3, 0xEE)       # cyan accent
SECONDARY = RGBColor(0xA7, 0x8B, 0xFA)     # purple accent
SUCCESS = RGBColor(0x22, 0xC5, 0x5E)       # green
WARN = RGBColor(0xF5, 0x9E, 0x0B)          # amber
DANGER = RGBColor(0xEF, 0x44, 0x44)        # red
TEXT = RGBColor(0xE5, 0xE7, 0xEB)          # light gray
MUTED = RGBColor(0x9C, 0xA3, 0xAF)         # muted gray
WHITE = RGBColor(0xFF, 0xFF, 0xFF)


def add_notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def add_background(slide, width, height):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, width, height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG
    bg.line.fill.background()

    # Accent blobs for a more visual theme.
    orb1 = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(10.8), Inches(-0.8), Inches(3.2), Inches(3.2))
    orb1.fill.solid()
    orb1.fill.fore_color.rgb = PRIMARY
    orb1.fill.transparency = 0.82
    orb1.line.fill.background()

    orb2 = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(-1.0), Inches(5.2), Inches(3.8), Inches(3.8))
    orb2.fill.solid()
    orb2.fill.fore_color.rgb = SECONDARY
    orb2.fill.transparency = 0.86
    orb2.line.fill.background()


def add_header(slide, width, title, subtitle=None):
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, width, Inches(0.95))
    bar.fill.solid()
    bar.fill.fore_color.rgb = SURFACE
    bar.line.fill.background()

    accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.18), Inches(0.95))
    accent.fill.solid()
    accent.fill.fore_color.rgb = PRIMARY
    accent.line.fill.background()

    box = slide.shapes.add_textbox(Inches(0.35), Inches(0.12), Inches(11.8), Inches(0.66))
    tf = box.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = title
    run.font.bold = True
    run.font.size = Pt(26)
    run.font.color.rgb = WHITE

    if subtitle:
        p2 = tf.add_paragraph()
        p2.space_before = Pt(0)
        p2.space_after = Pt(0)
        run2 = p2.add_run()
        run2.text = subtitle
        run2.font.size = Pt(12)
        run2.font.color.rgb = MUTED


def add_footer(slide, text):
    box = slide.shapes.add_textbox(Inches(0.5), Inches(7.05), Inches(12.2), Inches(0.3))
    tf = box.text_frame
    tf.paragraphs[0].alignment = PP_ALIGN.RIGHT
    run = tf.paragraphs[0].add_run()
    run.text = text
    run.font.size = Pt(10)
    run.font.color.rgb = MUTED


def add_panel(slide, left, top, width, height, fill=SURFACE, line=PRIMARY):
    panel = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    panel.fill.solid()
    panel.fill.fore_color.rgb = fill
    panel.line.color.rgb = line
    panel.line.width = Pt(1.3)
    return panel


def set_first_bullet(tf, text, size=Pt(18), bold=False, color=TEXT):
    p = tf.paragraphs[0]
    p.level = 0
    p.space_after = Pt(4)
    run = p.add_run()
    run.text = text
    run.font.size = size
    run.font.bold = bold
    run.font.color.rgb = color
    return p


def add_bullet(tf, text, level=0, size=Pt(16), bold=False, color=TEXT):
    p = tf.add_paragraph()
    # Keep PowerPoint-level indentation flat to avoid layout drift on blank slides.
    # Render nested structure with textual indent instead.
    p.level = 0
    p.space_after = Pt(4)
    run = p.add_run()
    prefix = ("    " * level) if level > 0 else ""
    run.text = f"{prefix}{text}"
    run.font.size = size
    run.font.bold = bold
    run.font.color.rgb = color
    return p


def add_title_slide(prs, blank):
    slide = prs.slides.add_slide(blank)
    add_background(slide, prs.slide_width, prs.slide_height)

    title_box = slide.shapes.add_textbox(Inches(0.9), Inches(1.7), Inches(11.8), Inches(2.0))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = "AI 101 + Agentic Tools Workshop"
    run.font.size = Pt(48)
    run.font.bold = True
    run.font.color.rgb = WHITE

    p2 = tf.add_paragraph()
    run2 = p2.add_run()
    run2.text = "From model basics to practical workflows for students"
    run2.font.size = Pt(24)
    run2.font.color.rgb = PRIMARY

    add_footer(slide, "Agentic Workshop Lab")
    add_notes(
        slide,
        "Visual idea: A futuristic classroom cockpit with holographic UI and students collaborating.\n"
        "Prompt seed: 'cinematic neon classroom mission control, teenagers learning AI, high contrast, wide shot'",
    )


def add_bullets_slide(prs, blank, title, bullets, image_hint):
    slide = prs.slides.add_slide(blank)
    add_background(slide, prs.slide_width, prs.slide_height)
    add_header(slide, prs.slide_width, title)

    panel = add_panel(slide, Inches(0.6), Inches(1.2), Inches(12.1), Inches(5.55), fill=SURFACE, line=PRIMARY)
    tf = panel.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.25)
    tf.margin_top = Inches(0.18)

    for i, item in enumerate(bullets):
        if isinstance(item, tuple):
            head, subs = item
            if i == 0:
                set_first_bullet(tf, head, size=Pt(20), bold=True, color=WHITE)
            else:
                add_bullet(tf, head, size=Pt(20), bold=True, color=WHITE)
            for sub in subs:
                add_bullet(tf, sub, level=1, size=Pt(14), color=TEXT)
        else:
            if i == 0:
                set_first_bullet(tf, item, size=Pt(18), color=TEXT)
            else:
                add_bullet(tf, item, size=Pt(18), color=TEXT)

    add_footer(slide, "AI 101 Workshop")
    add_notes(slide, f"Suggested image concept: {image_hint}")


def add_two_column_slide(prs, blank, title, left_title, left_points, right_title, right_points, image_hint):
    slide = prs.slides.add_slide(blank)
    add_background(slide, prs.slide_width, prs.slide_height)
    add_header(slide, prs.slide_width, title)

    left = add_panel(slide, Inches(0.6), Inches(1.25), Inches(5.85), Inches(5.35), fill=SURFACE, line=PRIMARY)
    right = add_panel(slide, Inches(6.85), Inches(1.25), Inches(5.85), Inches(5.35), fill=SURFACE, line=SECONDARY)

    tf_l = left.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = Inches(0.2)
    tf_l.margin_top = Inches(0.1)
    set_first_bullet(tf_l, left_title, size=Pt(21), bold=True, color=PRIMARY)
    for point in left_points:
        add_bullet(tf_l, point, size=Pt(14), color=TEXT)

    tf_r = right.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = Inches(0.2)
    tf_r.margin_top = Inches(0.1)
    set_first_bullet(tf_r, right_title, size=Pt(21), bold=True, color=SECONDARY)
    for point in right_points:
        add_bullet(tf_r, point, size=Pt(14), color=TEXT)

    add_footer(slide, "AI 101 Workshop")
    add_notes(slide, f"Suggested image concept: {image_hint}")


def add_model_size_metaphor_slide(prs, blank):
    slide = prs.slides.add_slide(blank)
    add_background(slide, prs.slide_width, prs.slide_height)
    add_header(slide, prs.slide_width, "Model Scale, Parameters, and Tradeoffs")

    explainer = add_panel(slide, Inches(0.6), Inches(1.2), Inches(12.1), Inches(1.35), fill=SURFACE, line=PRIMARY)
    tf = explainer.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.07)
    set_first_bullet(tf, "Parameter count is not IQ, but it affects capability range, latency, and cost.", size=Pt(17), bold=True, color=WHITE)
    add_bullet(tf, "Bigger models usually reason deeper and transfer better. Smaller models are faster and cheaper.", size=Pt(13), color=TEXT)

    # Visual metaphor cards
    big_card = add_panel(slide, Inches(0.8), Inches(2.85), Inches(5.8), Inches(3.35), fill=SURFACE, line=SUCCESS)
    tfb = big_card.text_frame
    tfb.word_wrap = True
    tfb.margin_left = Inches(0.2)
    tfb.margin_top = Inches(0.1)
    set_first_bullet(tfb, "Think-Book Model", size=Pt(24), bold=True, color=SUCCESS)
    add_bullet(tfb, "Deep context and nuance", size=Pt(14), color=TEXT)
    add_bullet(tfb, "Great for architecture, debugging, and tradeoffs", size=Pt(14), color=TEXT)
    add_bullet(tfb, "Higher cost + longer response time", size=Pt(14), color=TEXT)

    small_card = add_panel(slide, Inches(6.75), Inches(2.85), Inches(5.8), Inches(3.35), fill=SURFACE, line=WARN)
    tfs = small_card.text_frame
    tfs.word_wrap = True
    tfs.margin_left = Inches(0.2)
    tfs.margin_top = Inches(0.1)
    set_first_bullet(tfs, "Cliff-Notes Model", size=Pt(24), bold=True, color=WARN)
    add_bullet(tfs, "Quick, cheap, and responsive", size=Pt(14), color=TEXT)
    add_bullet(tfs, "Great for summaries, rewrites, lightweight tasks", size=Pt(14), color=TEXT)
    add_bullet(tfs, "Can miss subtle constraints in hard code tasks", size=Pt(14), color=TEXT)

    add_footer(slide, "AI 101 Workshop")
    add_notes(
        slide,
        "Visual concept to search/generate: side-by-side desk with a thick reference textbook vs slim cheat-sheet notebook.\n"
        "Message: both contain knowledge, but depth and reliability differ under pressure.",
    )


def add_tools_landscape_slide(prs, blank):
    slide = prs.slides.add_slide(blank)
    add_background(slide, prs.slide_width, prs.slide_height)
    add_header(slide, prs.slide_width, "Tool Landscape: Copilot vs Claude vs OpenCode-style Agents")

    cols = [
        ("GitHub Copilot", PRIMARY, [
            "Best inside developer workflow and repos",
            "Strong for inline coding, PR workflows, and agent handoff",
            "Great when GitHub context matters most",
        ]),
        ("Claude-style Assistant", SECONDARY, [
            "Strong long-form reasoning and explanation",
            "Useful for planning, docs, and architecture tradeoffs",
            "Great for teaching and concept walkthroughs",
        ]),
        ("OpenCode / DIY Agents", SUCCESS, [
            "Maximum control over models, tools, and infra",
            "Good for experimentation and custom orchestration",
            "Higher setup and governance overhead",
        ]),
    ]

    x = Inches(0.55)
    for title, color, points in cols:
        card = add_panel(slide, x, Inches(1.35), Inches(4.1), Inches(5.2), fill=SURFACE, line=color)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.18)
        tf.margin_top = Inches(0.08)
        set_first_bullet(tf, title, size=Pt(20), bold=True, color=color)
        for p in points:
            add_bullet(tf, p, size=Pt(13), color=TEXT)
        x += Inches(4.28)

    note = add_panel(slide, Inches(0.55), Inches(6.65), Inches(12.15), Inches(0.6), fill=BG, line=PRIMARY)
    nt = note.text_frame
    nt.margin_left = Inches(0.15)
    nt.margin_top = Inches(0.03)
    set_first_bullet(nt, "Pick tools by workflow fit, not by hype. Blended stacks often win.", size=Pt(12), bold=True, color=WHITE)
    add_footer(slide, "AI 101 Workshop")
    add_notes(
        slide,
        "Image idea: toolbelt metaphor with 3 labeled tools (integrated, reasoning-focused, customizable).\n"
        "Avoid framing as winner/loser; focus on use-case fit.",
    )


def add_mcp_slide(prs, blank):
    slide = prs.slides.add_slide(blank)
    add_background(slide, prs.slide_width, prs.slide_height)
    add_header(slide, prs.slide_width, "What is an MCP Server?")

    center = add_panel(slide, Inches(4.95), Inches(2.5), Inches(3.4), Inches(1.5), fill=SURFACE, line=PRIMARY)
    tcenter = center.text_frame
    tcenter.paragraphs[0].alignment = PP_ALIGN.CENTER
    run = tcenter.paragraphs[0].add_run()
    run.text = "AI Agent"
    run.font.size = Pt(26)
    run.font.bold = True
    run.font.color.rgb = WHITE

    spokes = [
        (Inches(0.9), Inches(1.5), "Filesystem\nTools"),
        (Inches(0.9), Inches(4.4), "Browser\nAutomation"),
        (Inches(9.25), Inches(1.5), "Tickets +\nDocs APIs"),
        (Inches(9.25), Inches(4.4), "Monitoring /\nTelemetry"),
    ]
    for x, y, label in spokes:
        box = add_panel(slide, x, y, Inches(3.1), Inches(1.35), fill=SURFACE, line=SECONDARY)
        tf = box.text_frame
        tf.paragraphs[0].alignment = PP_ALIGN.CENTER
        run = tf.paragraphs[0].add_run()
        run.text = label
        run.font.size = Pt(17)
        run.font.bold = True
        run.font.color.rgb = TEXT

        connector = slide.shapes.add_shape(
            MSO_SHAPE.LINE_INVERSE,
            x + Inches(1.55),
            y + Inches(0.68),
            Inches(3.35),
            Inches(1.3),
        )
        connector.line.color.rgb = PRIMARY
        connector.line.width = Pt(1.2)

    bottom = add_panel(slide, Inches(0.7), Inches(5.9), Inches(12.0), Inches(0.9), fill=SURFACE, line=SUCCESS)
    tfb = bottom.text_frame
    tfb.margin_left = Inches(0.2)
    tfb.margin_top = Inches(0.08)
    set_first_bullet(tfb, "MCP is a standard way to expose tools safely so agents can do real work, not just chat.", size=Pt(14), bold=True, color=SUCCESS)
    add_footer(slide, "AI 101 Workshop")
    add_notes(
        slide,
        "Image idea: hub-and-spoke system diagram with AI agent in center and tool systems around it.",
    )


def add_tokens_slide(prs, blank):
    slide = prs.slides.add_slide(blank)
    add_background(slide, prs.slide_width, prs.slide_height)
    add_header(slide, prs.slide_width, "Tokens, Context Windows, and Limits")

    left = add_panel(slide, Inches(0.6), Inches(1.25), Inches(6.0), Inches(5.45), fill=SURFACE, line=PRIMARY)
    tf_l = left.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = Inches(0.2)
    tf_l.margin_top = Inches(0.08)
    set_first_bullet(tf_l, "Token basics", size=Pt(22), bold=True, color=PRIMARY)
    add_bullet(tf_l, "A token is a chunk of text the model processes.", size=Pt(14))
    add_bullet(tf_l, "Input tokens + output tokens drive cost and limits.", size=Pt(14))
    add_bullet(tf_l, "Context window is the active working memory budget.", size=Pt(14))
    add_bullet(tf_l, "Long chats can force summarization/compression.", size=Pt(14))

    right = add_panel(slide, Inches(6.75), Inches(1.25), Inches(6.0), Inches(5.45), fill=SURFACE, line=DANGER)
    tf_r = right.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = Inches(0.2)
    tf_r.margin_top = Inches(0.08)
    set_first_bullet(tf_r, "When you exceed context", size=Pt(22), bold=True, color=DANGER)
    add_bullet(tf_r, "Older details get dropped or compressed.", size=Pt(14))
    add_bullet(tf_r, "Precision can degrade on long, complex tasks.", size=Pt(14))
    add_bullet(tf_r, "Symptoms: repeats, contradictions, missing constraints.", size=Pt(14))
    add_bullet(tf_r, "Fixes: restate constraints, chunk tasks, refresh summary.", size=Pt(14))

    add_footer(slide, "AI 101 Workshop")
    add_notes(
        slide,
        "Image idea: backpack with finite capacity; adding more items forces throwing old ones out.",
    )


def add_storyboard_slide(prs, blank):
    slide = prs.slides.add_slide(blank)
    add_background(slide, prs.slide_width, prs.slide_height)
    add_header(slide, prs.slide_width, "Imagery Storyboard Suggestions")

    prompts = [
        ("Model size metaphor", "thick reference book vs slim cliff-notes booklet on a desk, split-frame, high clarity"),
        ("Local vs cloud", "laptop with small on-device chip vs cloud datacenter pipeline, clean infographic style"),
        ("MCP concept", "AI hub connected to tools: browser, docs, terminal, monitoring, network graph style"),
        ("Context overflow", "container filling to limit and compressing old notes into a summary card"),
        ("Right model for task", "task board mapping quick tasks to small model and deep architecture to large model"),
    ]

    table_shape = slide.shapes.add_table(1 + len(prompts), 2, Inches(0.6), Inches(1.35), Inches(12.1), Inches(5.9))
    table = table_shape.table
    table.columns[0].width = Inches(3.1)
    table.columns[1].width = Inches(9.0)

    headers = ["Slide Idea", "Prompt Seed (edit for your image generator)"]
    for c, text in enumerate(headers):
        cell = table.cell(0, c)
        cell.fill.solid()
        cell.fill.fore_color.rgb = SURFACE
        cell.text = text
        p = cell.text_frame.paragraphs[0]
        p.runs[0].font.size = Pt(12)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = WHITE

    for r, (label, prompt) in enumerate(prompts, start=1):
        c0 = table.cell(r, 0)
        c0.fill.solid()
        c0.fill.fore_color.rgb = BG
        c0.text = label
        p0 = c0.text_frame.paragraphs[0]
        p0.runs[0].font.size = Pt(11)
        p0.runs[0].font.bold = True
        p0.runs[0].font.color.rgb = PRIMARY

        c1 = table.cell(r, 1)
        c1.fill.solid()
        c1.fill.fore_color.rgb = BG
        c1.text = prompt
        p1 = c1.text_frame.paragraphs[0]
        p1.runs[0].font.size = Pt(11)
        p1.runs[0].font.color.rgb = TEXT

    add_footer(slide, "AI 101 Workshop")
    add_notes(slide, "You can use these seeds in Midjourney, DALL-E, Stable Diffusion, or stock search queries.")


# ---------------------------------------------------------------------------
# New topic slides
# ---------------------------------------------------------------------------


def add_training_deep_dive_slide(prs, blank):
    """Slide: How Training Really Works (deeper dive)."""
    add_bullets_slide(
        prs, blank, "How Training Really Works",
        [
            ("Data Collection", [
                "Internet text, books, code repos \u2014 trillions of words scraped and cleaned."
            ]),
            ("Pretraining", [
                "Model learns to predict the next token across massive datasets.",
                "Like reading millions of books \u2014 you absorb grammar and style."
            ]),
            ("Fine-Tuning with Human Feedback (RLHF)", [
                "Humans rate outputs to steer the model toward helpful, safe responses."
            ]),
            ("Key Insight", [
                "Models learn patterns, not facts \u2014 they are pattern engines.",
                "You might misremember specific facts, but you \"get\" the language."
            ]),
        ],
        "data pipeline: books and code flowing through neural network into a glowing brain",
    )


def add_prediction_slide(prs, blank):
    """Slide: How Does Prediction Actually Work?"""
    add_bullets_slide(
        prs, blank, "How Does Prediction Actually Work?",
        [
            ("Token-by-Token Generation", [
                "Model picks the most likely next token, feeds it back, repeats.",
                "Like autocomplete on steroids \u2014 instead of one word, it keeps going."
            ]),
            ("Temperature Controls Randomness", [
                "Low temperature = focused, predictable output.",
                "High temperature = more creative, surprising results."
            ]),
            ("Top-K and Top-P Sampling", [
                "Only consider the top candidates for the next token.",
                "Balances quality and variety in responses."
            ]),
            "Live Demo: We have a token prediction demo that shows this in action!",
        ],
        "autocomplete cascade showing probability bars for next-token candidates",
    )


def add_hallucinations_slide(prs, blank):
    """Slide: Hallucinations \u2014 When AI Makes Stuff Up."""
    add_bullets_slide(
        prs, blank, "Hallucinations: When AI Makes Stuff Up",
        [
            ("What Happens", [
                "Model generates confident-sounding but factually wrong output."
            ]),
            ("Why It Happens", [
                "It predicts likely tokens, not verified facts \u2014 no fact-checker inside."
            ]),
            ("Examples You Might See", [
                "Fake book summaries, invented citations, wrong math steps."
            ]),
            ("How to Minimize", [
                "Be specific, ask for sources, fact-check, use smaller-scope questions."
            ]),
            "Trust but verify \u2014 treat AI like a smart but unreliable first draft.",
        ],
        "magnifying glass revealing cracks in a confident-looking AI-generated document",
    )


def add_multimodal_slide(prs, blank):
    """Slide: Why Can Some Models Generate Images?"""
    add_bullets_slide(
        prs, blank, "Why Can Some Models Generate Images?",
        [
            ("Text Models", [
                "Trained on text data only \u2014 read and write text, nothing else."
            ]),
            ("Multimodal Models (GPT-4o, Gemini)", [
                "Trained on text + image pairs \u2014 can understand photos you upload."
            ]),
            ("Image Generation (Stable Diffusion, DALL-E)", [
                "Totally different architecture \u2014 uses a diffusion process.",
                "Starts from noise, gradually refines into an image."
            ]),
            ("Key Insight", [
                "A model can only do what it was trained to do.",
                "Text model \u2260 image model \u2014 different tools for different jobs."
            ]),
        ],
        "split view: text tokens flowing through one model, pixel grids through another",
    )


def add_hardware_slide(prs, blank):
    """Slide: What Hardware Runs a Model?"""
    slide = prs.slides.add_slide(blank)
    add_background(slide, prs.slide_width, prs.slide_height)
    add_header(slide, prs.slide_width, "What Hardware Runs a Model?")

    explainer = add_panel(slide, Inches(0.6), Inches(1.2), Inches(12.1), Inches(1.35),
                          fill=SURFACE, line=PRIMARY)
    tf = explainer.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_top = Inches(0.07)
    set_first_bullet(tf, "GPUs power AI because they do massive parallel math. VRAM is the bottleneck.",
                     size=Pt(17), bold=True, color=WHITE)
    add_bullet(tf, "CPU = general-purpose brain.  GPU = thousands of simple cores doing math at once.",
               size=Pt(13), color=TEXT)

    rows_data = [
        ("1B params", "~2 GB", "Tiny tasks, mobile devices"),
        ("7B params", "~6 GB", "Good starter, fits most gaming GPUs"),
        ("14B params", "~10 GB", "Solid quality, needs mid-range GPU"),
        ("30B params", "~20 GB", "Near-cloud quality, high-end GPU"),
        ("70B+ params", "~48 GB+", "Top tier \u2014 multiple GPUs needed"),
    ]

    table_shape = slide.shapes.add_table(
        1 + len(rows_data), 3, Inches(0.8), Inches(2.85), Inches(11.7), Inches(3.0))
    table = table_shape.table
    table.columns[0].width = Inches(3.0)
    table.columns[1].width = Inches(3.0)
    table.columns[2].width = Inches(5.7)

    for c, text in enumerate(["Model Size", "VRAM Needed", "What That Means"]):
        cell = table.cell(0, c)
        cell.fill.solid()
        cell.fill.fore_color.rgb = SURFACE
        cell.text = text
        p = cell.text_frame.paragraphs[0]
        p.runs[0].font.size = Pt(13)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = WHITE

    for r, (size, vram, note) in enumerate(rows_data, start=1):
        for c, val in enumerate([size, vram, note]):
            cell = table.cell(r, c)
            cell.fill.solid()
            cell.fill.fore_color.rgb = BG
            cell.text = val
            p = cell.text_frame.paragraphs[0]
            p.runs[0].font.size = Pt(12)
            p.runs[0].font.color.rgb = TEXT
            if c == 0:
                p.runs[0].font.bold = True
                p.runs[0].font.color.rgb = PRIMARY

    callout = add_panel(slide, Inches(0.6), Inches(6.05), Inches(12.1), Inches(0.7),
                        fill=SURFACE, line=SUCCESS)
    tfc = callout.text_frame
    tfc.margin_left = Inches(0.2)
    tfc.margin_top = Inches(0.06)
    set_first_bullet(
        tfc,
        "Our workshop server: RTX 5090 with 32 GB VRAM \u2014 runs up to ~30B models comfortably.",
        size=Pt(14), bold=True, color=SUCCESS)

    add_footer(slide, "AI 101 Workshop")
    add_notes(slide, "Visual concept: GPU card with glowing VRAM chips, size comparison chart.")


def add_params_vs_tokens_slide(prs, blank):
    """Slide: Parameters vs Tokens \u2014 What's the Difference?"""
    add_two_column_slide(
        prs, blank, "Parameters vs Tokens: What's the Difference?",
        "Parameters (The Engine)",
        [
            "The model's learned knowledge \u2014 its neural weights.",
            "Fixed after training. Like the brain's connections.",
            "Parameter count = model size and capability.",
            "More parameters = deeper reasoning potential.",
            "Analogy: the size of the engine under the hood.",
        ],
        "Tokens (The Fuel)",
        [
            "Chunks of text flowing through at runtime.",
            "Like the words in a conversation \u2014 always changing.",
            "Token count = conversation length and cost.",
            "More tokens = longer context, higher price tag.",
            "Analogy: the fuel going through the engine.",
        ],
        "engine-vs-fuel metaphor: car engine cutaway on left, fuel gauge on right",
    )


def add_privacy_slide(prs, blank):
    """Slide: Privacy and Your Data \u2014 two columns with warning callout."""
    slide = prs.slides.add_slide(blank)
    add_background(slide, prs.slide_width, prs.slide_height)
    add_header(slide, prs.slide_width, "Privacy and Your Data")

    left = add_panel(slide, Inches(0.6), Inches(1.25), Inches(5.85), Inches(4.6),
                     fill=SURFACE, line=PRIMARY)
    right = add_panel(slide, Inches(6.85), Inches(1.25), Inches(5.85), Inches(4.6),
                      fill=SURFACE, line=SECONDARY)

    tf_l = left.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = Inches(0.2)
    tf_l.margin_top = Inches(0.1)
    set_first_bullet(tf_l, "Cloud AI Services", size=Pt(21), bold=True, color=PRIMARY)
    for pt in [
        "Your prompts may be logged by the provider.",
        "Some services use your data for training (check!).",
        "Subject to the provider's data policies.",
        "Consider carefully what you share.",
        "Great capability, but read the fine print.",
    ]:
        add_bullet(tf_l, pt, size=Pt(14), color=TEXT)

    tf_r = right.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = Inches(0.2)
    tf_r.margin_top = Inches(0.1)
    set_first_bullet(tf_r, "Local AI (Like Our Lab)", size=Pt(21), bold=True, color=SECONDARY)
    for pt in [
        "Data stays on this machine \u2014 nowhere else.",
        "No internet connection needed to run.",
        "Full control over your data and models.",
        "You manage everything (updates, security).",
        "Privacy by design, but more responsibility.",
    ]:
        add_bullet(tf_r, pt, size=Pt(14), color=TEXT)

    callout = add_panel(slide, Inches(0.6), Inches(6.05), Inches(12.1), Inches(0.7),
                        fill=SURFACE, line=WARN)
    tfc = callout.text_frame
    tfc.margin_left = Inches(0.2)
    tfc.margin_top = Inches(0.06)
    set_first_bullet(
        tfc,
        "Always read the privacy policy. Some services opt you INTO training by default.",
        size=Pt(14), bold=True, color=WARN)

    add_footer(slide, "AI 101 Workshop")
    add_notes(slide, "Visual concept: shield split between cloud data flow and locked local vault.")


def add_lab_intro_slide(prs, blank):
    """Slide: Welcome to the Lab!"""
    add_bullets_slide(
        prs, blank, "Welcome to the Lab!",
        [
            ("How to Connect", [
                "Open your browser \u2192 navigate to http://[server-ip]:3000",
                "No login required \u2014 just start chatting!"
            ]),
            ("Using the Interface", [
                "Model selector: pick different models from the dropdown.",
                "New chat: start fresh sessions for each exercise.",
                "Available models listed with descriptions in the sidebar."
            ]),
            ("What We'll Do", [
                "Hands-on exercises exploring different models and prompts.",
                "Compare outputs, speed, and quality across model sizes.",
                "Lab exercise guide available \u2014 follow along or explore!"
            ]),
        ],
        "students opening laptops and connecting to a glowing local server hub",
    )


def build_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    # 1
    add_title_slide(prs, blank)

    # 2
    add_bullets_slide(
        prs, blank, "Agenda",
        [
            "1. What AI is (and is not)",
            "2. How models are trained \u2014 from data to deployment",
            "3. How training and prediction really work",
            "4. Hallucinations \u2014 when AI makes stuff up",
            "5. Model types: text, multimodal, and image generation",
            "6. Model sizes, hardware, and choosing the right one",
            "7. Tokens, parameters, and context windows",
            "8. Agentic workflows, MCP, and tools",
            "9. Prompting patterns that work",
            "10. Hands-on lab \u2014 connect and experiment",
            "11. Safety, privacy, and responsible use",
            "12. Discussion and Q&A",
        ],
        "clean mission board agenda visual with neon accents",
    )

    # 3
    add_bullets_slide(
        prs, blank, "AI in Layers: The Stack View",
        [
            ("Layer 1 - Models", ["The reasoning engine that predicts next tokens based on learned patterns."]),
            ("Layer 2 - Runtime", ["Local or cloud infrastructure that executes the model safely and fast."]),
            ("Layer 3 - Tools", ["File, browser, terminal, APIs, and external systems agents can call."]),
            ("Layer 4 - Product UX", ["Copilot/assistant experiences where users actually interact."]),
            ("Layer 5 - Governance", ["Policies, security controls, logs, and cost guardrails."]),
        ],
        "stacked architecture diagram with five labeled layers and arrows",
    )

    # 4
    add_bullets_slide(
        prs, blank, "What is a Model?",
        [
            "A model is a trained pattern engine, not a database of perfect facts.",
            "It maps input context to likely output tokens.",
            "Strengths: pattern recognition, synthesis, drafting, code transformation.",
            "Weaknesses: can hallucinate, can miss hidden constraints, no guaranteed truth.",
            "Better framing: probabilistic assistant, not oracle.",
        ],
        "glass brain made of text fragments and vectors, educational infographic style",
    )

    # 5
    add_bullets_slide(
        prs, blank, "How Models are Built (High Level)",
        [
            ("Pretraining", ["Model learns language and code patterns from large datasets."]),
            ("Alignment / fine-tuning", ["Improves helpfulness, safety, and instruction following."]),
            ("Evaluation", ["Benchmarks + human feedback expose strengths and failure cases."]),
            ("Serving", ["Model is optimized, hosted, and monitored for real user workloads."]),
        ],
        "factory pipeline from data to trained model to deployment",
    )

    # 6 — How Training Really Works
    add_training_deep_dive_slide(prs, blank)

    # 7 — How Does Prediction Actually Work?
    add_prediction_slide(prs, blank)

    # 8 — Hallucinations
    add_hallucinations_slide(prs, blank)

    # 9 — Why Can Some Models Generate Images?
    add_multimodal_slide(prs, blank)

    # 10
    add_two_column_slide(
        prs, blank, "How Models Run: Local vs Cloud",
        "Local Model",
        [
            "Pros: privacy control, offline capability, predictable cost ceiling",
            "Pros: low-latency for small tasks when tuned well",
            "Cons: hardware limits, weaker large-model performance",
            "Cons: setup and maintenance burden",
        ],
        "Cloud Model",
        [
            "Pros: top-tier capability, elastic scaling, managed reliability",
            "Pros: easiest path to advanced multimodal and tool ecosystems",
            "Cons: usage-based cost and policy requirements",
            "Cons: network dependency",
        ],
        "split scene laptop edge device vs cloud datacenter pipeline",
    )

    # 7
    add_model_size_metaphor_slide(prs, blank)

    # 12 — What Hardware Runs a Model?
    add_hardware_slide(prs, blank)

    # 13
    add_two_column_slide(
        prs, blank, "Choose the Right Model for the Task",
        "Use Small/Fast Models For",
        [
            "Formatting, rewrite, summaries, classification",
            "Simple Q&A and low-risk automation",
            "High-volume tasks where latency matters",
            "Example: writing a haiku or polishing bullet points",
        ],
        "Use Larger Models For",
        [
            "Hard debugging and architecture design",
            "Cross-file code changes with nuanced constraints",
            "Multi-step reasoning with tradeoff analysis",
            "Example: designing robust auth refactors safely",
        ],
        "task-routing board with lightweight and heavyweight lanes",
    )

    # 9
    add_two_column_slide(
        prs, blank, "Coding vs General Document Creation",
        "Coding Work",
        [
            "Needs correctness, tests, constraints, and execution checks",
            "Tool use matters: terminal, repo search, CI feedback",
            "Errors can ship to production if unchecked",
        ],
        "Docs / Content Work",
        [
            "Needs clarity, tone, and audience fit",
            "Fast iteration with human review is usually enough",
            "Lower technical blast radius, but still fact-check important claims",
        ],
        "split keyboard-and-code panel versus notebook-and-editor panel",
    )

    # 10
    add_tools_landscape_slide(prs, blank)

    # 11
    add_mcp_slide(prs, blank)

    # 12
    add_tokens_slide(prs, blank)

    # 18 — Parameters vs Tokens
    add_params_vs_tokens_slide(prs, blank)

    # 19
    add_bullets_slide(
        prs, blank, "Prompting Patterns That Work in Class",
        [
            ("Pattern 1 - Give role + goal + constraints", [
                "Example: 'Act as a code reviewer; find security issues only; keep it concise.'"
            ]),
            ("Pattern 2 - Ask for options with tradeoffs", [
                "Prompts students to think, not just accept first output."
            ]),
            ("Pattern 3 - Iterate with evidence", [
                "Ask model to cite files, lines, or assumptions before finalizing."
            ]),
            ("Pattern 4 - Keep a running summary", [
                "Prevents context drift in long sessions."
            ]),
        ],
        "teacher and students at whiteboard refining prompts together",
    )

    # 20 — Welcome to the Lab!
    add_lab_intro_slide(prs, blank)

    # 21
    add_bullets_slide(
        prs, blank, "Live Lab Plan (Student-Friendly)",
        [
            "Demo A: ask agent for a simple content rewrite (fast model candidate).",
            "Demo B: ask agent to propose a multi-file code fix (larger model candidate).",
            "Compare quality, speed, and cost assumptions as a class.",
            "Inspect what tools were used and whether MCP access was needed.",
            "Debrief: where humans must stay in control.",
        ],
        "classroom lab with students observing terminal and PR diff screens",
    )

    # 15
    add_bullets_slide(
        prs, blank, "Safety and Reality Check",
        [
            "AI can accelerate work, but does not replace engineering judgment.",
            "Always verify claims, code behavior, and external facts.",
            "Treat model output as draft material until reviewed.",
            "Use least-privilege tool access and clear repo policies.",
            "Responsible teams optimize for quality + safety, not just speed.",
        ],
        "seatbelt-on-rocket metaphor for safe acceleration",
    )

    # 23 — Privacy and Your Data
    add_privacy_slide(prs, blank)

    # 24
    add_storyboard_slide(prs, blank)

    # 17
    add_bullets_slide(
        prs, blank, "Discussion and Q&A",
        [
            "What felt most surprising?",
            "Where would you trust AI today, and where not yet?",
            "What workflow would you test first in this repo?",
            "What guardrails would make you comfortable using agents?",
        ],
        "open mic classroom discussion circle, collaborative energy",
    )

    out_path = Path(__file__).parent / "Agentic_AI_101_Workshop.pptx"
    try:
        prs.save(str(out_path))
        print(f"Saved: {out_path}")
    except PermissionError:
        alt_path = Path(__file__).parent / "Agentic_AI_101_Workshop_updated.pptx"
        prs.save(str(alt_path))
        print(f"Saved (locked original, wrote alternate): {alt_path}")


if __name__ == "__main__":
    build_deck()
