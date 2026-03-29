# Media Strategy & Buying Skill

A Claude Code plugin that equips AI agents with digital media strategy, buying, and optimization expertise for Google Ads and Meta (Facebook/Instagram).

## What It Does

This plugin gives Claude deep knowledge of paid digital media — from cross-platform strategic planning to platform-specific campaign execution, optimization, and troubleshooting. It covers the full spectrum of media buying: strategy, setup, operations, diagnostics, and auditing.

## Architecture

```
skills/media-buying/
├── SKILL.md                           # Main router + cross-platform strategy
└── references/
    ├── google-ads-strategy.md         # Account structure, campaign types, bidding, QS
    ├── google-ads-operations.md       # Weekly/monthly checklists, scripts, measurement
    ├── google-ads-search.md           # SKAG→Hagakure, broad match, brand management
    ├── google-ads-troubleshooting.md  # Diagnostic decision trees, audit checklist
    ├── meta-strategy.md              # Andromeda, funnel, creative, CBO/ABO, Pixel/CAPI
    └── meta-operations.md            # 12 operational frameworks (A-L)

agents/
├── media-auditor.md                   # Account audit (Google/Meta/both)
├── campaign-planner.md                # Campaign planning & structuring
└── performance-doctor.md             # Performance diagnosis & troubleshooting
```

### How It Works

1. **SKILL.md** is the entry point — it contains cross-platform strategy frameworks and routing logic
2. **Reference files** are loaded on-demand based on context (Google, Meta, or cross-platform)
3. **Agents** are dispatched for complex workflows (audits, campaign plans, performance diagnosis)

## Installation

```bash
/plugin install https://github.com/thiagocarneiro/media-strategy-buying-skill
```

## Usage

The skill activates automatically when you discuss digital media topics:

```
# Cross-platform strategy
"I have $50K/month budget for an e-commerce brand. How should I split between Google and Meta?"

# Google Ads specific
"How should I structure my Google Ads account for a $10K/month budget?"

# Meta specific
"What's the best campaign structure for testing creatives on Meta?"

# Auditing (dispatches media-auditor agent)
"Audit my Google Ads account"

# Campaign planning (dispatches campaign-planner agent)
"Create a campaign plan for a new D2C skincare brand launching on Meta and Google"

# Troubleshooting (dispatches performance-doctor agent)
"My CPA on Meta increased 30% this week — what's wrong?"
```

## Coverage

### Google Ads
- Account structure (SKAG, STAG, Hagakure) by budget and conversion volume
- Campaign types: Search, Shopping, PMax, Display, Video, Demand Gen, AI Max
- Bidding strategy progression (Manual → Smart Bidding → Portfolio)
- Quality Score optimization
- Search Terms analysis and N-gram workflows
- Brand vs Non-Brand management
- Budget pacing and reallocation (20% scaling rule)
- Google Ads Scripts catalog
- Complete audit checklist (9 phases)
- Conversion lag, incrementality testing, offline tracking
- Recommendations management (safe/dangerous/conditional)

### Meta (Facebook/Instagram)
- Andromeda algorithm compliance (creative diversity requirements)
- Campaign structure: Creative Test (ABO sandbox) + Scale (CBO/ASC)
- Full-funnel strategy (TOF/MOF/BOF allocation)
- Audience strategy (70% broad / 30% retargeting)
- Creative strategy (formats, hooks, copy, aspect ratios, refresh cadence)
- CBO vs ABO decision tree
- 12 operational frameworks: Discovery, Decision Engine, Naming Convention, IF-THEN Playbook, Diagnostic Triage, Learning Phase, Reporting, Creative Briefing, Seasonal Calendar, Competitive Analysis, Pacing, Glossary
- Pixel + CAPI setup with deduplication

### Cross-Platform
- Channel roles (demand capture vs generation)
- Budget split by business type, maturity, and objective
- Full-funnel integration (Meta TOF → Google BOF pipeline)
- Cross-platform retargeting sequences
- Channel scaling decision frameworks
- Blended metrics (MER, blended CPA)
- Attribution: MTA, MMM, incrementality testing
- Industry benchmarks by vertical

## License

MIT
