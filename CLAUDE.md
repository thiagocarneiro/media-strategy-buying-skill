# Media Strategy & Buying Skill

## Project Overview

This is a Claude Code plugin that provides digital media strategy, buying, and optimization skills for Google Ads and Meta (Facebook/Instagram).

## Architecture

- `skills/media-buying/SKILL.md` — Main skill file (router + cross-platform strategy)
- `skills/media-buying/references/` — Platform-specific reference files loaded on demand
- `agents/` — Specialized sub-agents (media-auditor, campaign-planner, performance-doctor)
- `hooks/` — SessionStart bootstrap
- `docs/` — Research source documents (not loaded by plugin)

## Content Rules

- All plugin content (skills, agents, references) MUST be in English
- Research docs in `docs/` may be in Portuguese (source material)
- Reference files contain agent-executable instructions (WHEN → DO, IF → THEN), not expository text
- SKILL.md must stay under 500 lines

## Development

- Reference files are transformations of research docs in `docs/`
- When updating a reference file, check the corresponding research doc for source material
- Decision trees must have no dead ends — every path leads to an action
- Thresholds and benchmarks must be specific numbers, not vague ranges
