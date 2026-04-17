# Agentic Workshop Lab

Hands-on training repo for exploring modern agentic development workflows with GitHub Copilot and related tools.

## Purpose

This lab is designed for high school students who are:
- Curious about AI coding tools
- Skeptical and want to test claims directly
- Interested in seeing practical, real-time workflows

The goal is to make agentic tooling understandable, inspectable, and discussion-friendly.

## What we will cover

- **Foundations**: What "agentic" means and where it helps (and doesn't)
- **Live demos**: Using GitHub Copilot to plan, implement, and iterate
- **Prompting patterns**: How to ask better technical questions
- **Human-in-the-loop review**: Verifying output, not blindly accepting it
- **Responsible use**: Safety, quality, and bias-aware thinking

## Planned lab structure

We'll evolve this repository over time with:

- `labs/` - step-by-step exercises
- `demos/` - prepared demo scripts and prompts
- `examples/` - small reference projects
- `.github/` - issue templates, workflows, and Copilot instructions
- `resources/` - slides, links, and follow-up material

## Copilot cloud agent setup note

For **personal-account repositories**, Copilot cloud agent access is managed in GitHub account settings (UI), not currently through a public repository-level REST endpoint.

Use:

1. GitHub profile menu -> **Copilot settings**
2. **Cloud agent** policy
3. Set repository access to **All repositories** or **Only selected repositories**, then include this repo

## Current repository baseline

This repo is now initialized with high-level metadata for workshop use (description, discussions enabled, and starter topics), and this README serves as the initial scaffold.

## Regenerating the slide deck

To regenerate the workshop PowerPoint locally:

- (Optional) Create and activate a virtual environment:

  python -m venv .venv
  .\.venv\Scripts\activate  # Windows

- Install dependencies:

  pip install python-pptx

- Run the generator:

  python generate_agentic_ai_101_workshop.py

The script writes Agentic_AI_101_Workshop.pptx to the repository root. If PowerPoint has the file open, the script will instead write Agentic_AI_101_Workshop_updated.pptx. Close PowerPoint before regenerating to overwrite the primary file.

Recommendation: add "*.pptx" and "~$*" to .gitignore to avoid committing generated binaries.
