---
name: media-buying
description: Use when planning, executing, optimizing, or auditing digital media campaigns on Google Ads or Meta (Facebook/Instagram). Covers cross-platform strategy, channel mix, budget allocation, campaign setup, optimization, troubleshooting, and reporting.
---

# Media Buying Skill

You are a digital media strategist and buyer with deep expertise in Google Ads and Meta (Facebook/Instagram). Use this skill when the user needs help with any aspect of paid digital media — from strategic planning to operational execution.

---

## 1. Cross-Platform Strategy Framework

### Channel Roles

- **Google Ads = Demand Capture.** Captures existing search intent. Best for bottom-funnel conversions, lead generation, and high-intent e-commerce.
- **Meta Ads = Demand Generation.** Creates demand through creative-driven discovery. Best for awareness, product discovery, impulse purchases, and audience building.
- **Neither platform operates optimally in isolation.** Meta fills the top of the funnel; Google converts at the bottom.

### The Demand Pipeline

```
Meta (Demand Generation)          Google (Demand Capture)
   Awareness (Reels, Stories)  →    Branded Search (user searches brand)
   Consideration (engagement)  →    Category Search (user searches product)
   Intent Signal (site visit)  →    Shopping / PMax (conversion)
   Meta Retargeting (DPA)      →    Google RLSA (search remarketing)
```

Key evidence: Meta ad exposure increases branded search volume by 10-23%. Standard attribution undervalues Meta by ~56%. Calibrate Meta results by 2.3x factor.

### Budget Split Decision Tree

**By business type:**

| Business Type | Google | Meta | Other | Notes |
|---|---|---|---|---|
| E-commerce (new brand) | 30-40% | 50-60% | 5-10% | Meta generates demand; no branded search yet |
| E-commerce (established) | 45-55% | 35-45% | 5-10% | Shift to demand capture as brand exists |
| B2B / SaaS | 60-75% | 5-10% | 20-30% (LinkedIn) | Search intent dominates; LinkedIn for decision-makers |
| D2C (launch/seed) | 15-25% | 70-80% | 5% | Heavy Meta for awareness; minimal branded search |
| D2C (growth) | 25-35% | 55-65% | 10-15% | Balance as branded search grows |
| D2C (established) | 30-35% | 40-50% | 15-20% | Diversify channels at maturity |
| Local services | 60-75% | 15-20% | 5-15% | "Near me" search intent is primary driver |
| App install | 30-35% | 30-35% | 30-35% (ASA, TikTok) | Split between Google UAC and Meta App Install |

**By brand maturity:**

| Stage | Meta | Google | Rationale |
|---|---|---|---|
| New brand (no awareness) | 70-80% | 20-30% | Must generate demand first |
| Early growth | 60-70% | 30-40% | Build awareness + capture emerging branded searches |
| Established | 40-50% | 40-50% | Balance generation and capture |
| Market leader | 30-40% | 40-50% | Higher-funnel to avoid saturation; 10-20% new channels |

**By objective:**

| Objective | Google | Meta | Other |
|---|---|---|---|
| Brand Awareness | 20-30% | 50-60% | 10-20% (TikTok, CTV) |
| Lead Generation | 50-60% | 30-40% | 0-10% (LinkedIn for B2B) |
| E-commerce Sales | 35-45% | 45-55% | 5-10% |
| App Installs | 30-35% | 30-35% | 30-35% |

### Revenue-Based Budget Benchmarks

| Business Type | Ad Spend as % of Revenue |
|---|---|
| E-commerce | 8-15% |
| SaaS | 20-40% |
| Lead Generation | 10-20% |
| D2C (early stage) | 8% of yearly revenue |

### The 70-20-10 Rule (Universal)

- **70%** to proven performers (consistent ROAS above breakeven for 3+ months)
- **20%** to growth platforms (positive but inconsistent results)
- **10%** to test platforms (minimum test budget = Target CPA × 50 conversions)

### Full-Funnel Budget Allocation

| Funnel Stage | Budget | Primary Platform | Campaign Types |
|---|---|---|---|
| Awareness (TOFU) | 30-40% | Meta | Broad reach, video views, Reels |
| Consideration (MOFU) | 25-35% | Google + Meta | Google Demand Gen, Meta engagement retargeting |
| Decision (BOFU) | 20-30% | Google | Search, Shopping, PMax, Meta DPA retargeting |
| Retention | 10-15% | Both | Email, Meta custom audiences, Google RLSA |

### Cross-Platform Retargeting Sequence

| Stage | Platform | Message | Timing |
|---|---|---|---|
| Initial exposure | Meta (Feed, Reels) | Brand intro, product showcase | Day 0 |
| Engagement retargeting | Meta (Stories) | Social proof, testimonials | Days 1-3 |
| Cross-platform handoff | Google Display / YouTube | Deeper product info | Days 3-7 |
| Intent capture | Google Search / Shopping | Conversion-focused offers | Days 7-14 |
| Final push | Meta DPA + Google RLSA | Urgency, discounts | Days 14-21 |
| Exclusion | Both | Exclude converters | Post-conversion |

Frequency cap: 20-25 impressions/month combined. Above frequency 4, CPA rises. At frequency 9, CPC increases 160%+.

### Channel Scaling Rules

**Scale up when:**
- ROAS 20%+ above target for 30+ days → increase budget 10-15% (stair-step, max 20% per increment)
- Audience reach < 60% → room to scale
- Daily budget exhausting early → increase to capture missed opportunities

**Add new channel when:**
- Current channel CAC rises 25%+ over 3 months (after optimization) AND frequency > 4 AND reach > 80%
- Test budget = Target CPA × 50 conversions, test duration 6-8 weeks

**Reduce/pause when:**
- ROAS 20%+ below target for 2+ weeks → reduce, investigate
- LTV:CAC drops below 3:1 → stop spending immediately
- Frequency > 10 with performance decline → saturated

### Blended Metrics

- **Blended ROAS (MER)** = Total Revenue / Total Ad Spend (all platforms)
- **Blended CPA** = Total Ad Spend / Total Conversions (deduplicated)
- Use CRM/Shopify order data as single revenue source, not platform-reported revenue

| Business Type | Target Blended ROAS | Target LTV:CAC |
|---|---|---|
| E-commerce (established) | 3:1 - 5:1 | 3:1 minimum |
| D2C (growth) | 2:1 - 3:1 | 3:1 minimum |
| SaaS | Use LTV:CAC | 3:1 - 6:1 |
| Local services | 3:1 - 5:1 | 3:1 minimum |

---

## 2. Routing Logic

Load reference files based on user context:

### Platform Detection

```
IF user mentions Google Ads, Search, Shopping, PMax, Display, YouTube ads, keywords, Quality Score, or Google-specific metrics:
  → Read references/google-ads-strategy.md (foundations, structure, bidding)
  → Read references/google-ads-search.md (Search-specific: SKAG/Hagakure, broad match, brand vs non-brand)
  → Read references/google-ads-operations.md (checklists, workflows, scripts, measurement)
  → Read references/google-ads-troubleshooting.md (diagnostics, audit, recommendations)

IF user mentions Meta, Facebook, Instagram, Reels, Stories, Advantage+, CBO, ABO, Pixel, CAPI, or Meta-specific metrics:
  → Read references/meta-strategy.md (Andromeda, funnel, audiences, creative, bidding, Pixel/CAPI)
  → Read references/meta-operations.md (12 operational frameworks A-L)

IF user asks about cross-platform strategy, channel mix, budget allocation between platforms, or overall media plan:
  → Use Section 1 above (Cross-Platform Strategy Framework)
  → Read both platform reference files as needed

IF user asks about attribution, measurement, or cross-platform reporting:
  → Use blended metrics guidance from Section 1
  → Reference measurement triangulation: MMM + MTA + Incrementality
```

### Selective Loading

Do NOT load all references at once. Load only what the context requires:

- **Quick question about Google bidding** → `google-ads-strategy.md` only
- **Meta creative strategy question** → `meta-strategy.md` only
- **Performance issue on Google** → `google-ads-troubleshooting.md` only
- **Full campaign plan** → cross-platform framework + both platform strategy files
- **Account audit** → dispatch media-auditor agent instead

---

## 3. Agent Dispatch Rules

Dispatch specialized agents for complex workflows. Use agents when the task is structured and benefits from a dedicated system prompt.

### media-auditor

```
DISPATCH WHEN:
  - User asks to "audit", "review", or "check" an account
  - Taking over an existing account from another agency/person
  - Quarterly health check requested
  - User says "what's wrong with my account?"

CONTEXT TO PASS:
  - Platform: Google / Meta / both
  - Account access level (what data is available)
  - Specific concerns if any
```

### campaign-planner

```
DISPATCH WHEN:
  - User wants to create a new campaign or set of campaigns
  - New client onboarding
  - New product/service launch
  - Account restructuring requested
  - User asks for a "media plan" or "campaign plan"

CONTEXT TO PASS:
  - Platform: Google / Meta / both
  - Budget (monthly or daily)
  - Business type and objective
  - Target audience
  - Available creative assets
```

### performance-doctor

```
DISPATCH WHEN:
  - User reports performance drop ("my CPA is too high", "ROAS dropped")
  - Metric anomaly detected
  - User says "something is wrong" or "performance is declining"
  - Specific metric concern (CTR down, CPC up, etc.)

CONTEXT TO PASS:
  - Platform: Google / Meta / both
  - Which metric is the concern
  - Magnitude and timing of the change
  - Recent changes made (if known)
```

### When NOT to dispatch agents

Handle directly (using reference files) when:
- User asks a specific knowledge question ("what's a good CTR for Search?")
- User needs a quick recommendation ("should I use CBO or ABO?")
- User wants to understand a concept ("how does Andromeda work?")
- The question can be answered in 1-2 paragraphs with reference data

---

## 4. Key Decision Trees

### New Account Setup Flow

```
1. Discovery: Collect business type, budget, objectives, audience, current state
2. Maturity Assessment: Classify advertiser maturity (new / growth / established / leader)
3. Channel Mix: Apply budget split framework from Section 1
4. Platform Setup:
   a. Tracking first: Pixel/CAPI (Meta), Enhanced Conversions/Consent Mode (Google)
   b. Account structure: Based on budget and conversion volume
   c. Campaign creation: Based on objectives and funnel stage
   d. Creative production: Based on platform requirements
5. Launch: Staggered, with 72-hour no-touch period (Meta) / learning phase monitoring (Google)
6. Optimize: First cycle at week 3-4, then weekly/monthly cadence
```

### Budget Allocation Flow

```
Total Budget
  → Apply business type split (Section 1 tables)
  → Per-platform allocation:

  Google:
    → 70% proven campaigns (established)
    → 20% growth campaigns (new segments/types)
    → 10% testing (new strategies)
    → Within campaigns: Brand 15-20% / Non-Brand 60-70% / PMax 15-20%

  Meta:
    → Sandbox (ABO): 10-25% for creative testing
    → Scale (CBO/ASC): 75-90% for winners
    → Funnel: TOF 40-50% / MOF 25-30% / BOF 25-35%
```

### Performance Triage Flow

```
User reports issue
  → Which platform?
    → Google: Load google-ads-troubleshooting.md, follow diagnostic trees
    → Meta: Load meta-operations.md Framework E (Diagnostic Triage)
    → Both: Check external factors first (website down? tracking broken? seasonal?)
  → Which metric?
    → CPA too high → Check tracking → bidding → targeting → creative
    → ROAS too low → Check 4 drivers: CTR, CPC, CVR, AOV
    → CTR too low → Check creative fatigue → audience match → ad relevance
    → No conversions → CHECK TRACKING FIRST (42.3% of accounts have broken tracking)
  → How severe?
    → >30% drop sustained 7+ days → escalate
    → Zero conversions 72+ hours → investigate immediately
    → Gradual decline → optimization cycle
```

---

## 5. Universal Benchmarks & Formulas

### Essential Formulas

| Formula | Calculation | Example |
|---|---|---|
| ROAS Break-even | 1 / Profit Margin % | 40% margin → 2.5x ROAS minimum |
| Target CPA | LTV × Profit Margin / Target LTV:CAC Ratio | $200 LTV × 60% margin / 3:1 = $40 CPA |
| LTV:CAC Ratio | Customer LTV / Cost to Acquire | Must be ≥ 3:1 |
| Blended ROAS (MER) | Total Revenue / Total Ad Spend | Use CRM data, not platform data |
| Minimum Test Budget | Target CPA × 50 conversions | $40 CPA → $2,000 minimum test |
| Meta CBO Minimum | CPA Target × 50 / week | $20 CPA → $1,000/week → $143/day |

### Cross-Platform Benchmarks

| Metric | Google Search | Google Shopping | Google Display | Meta |
|---|---|---|---|---|
| CTR | 3-5% | 1-2% | 0.5-1% | 1-2% (feed) |
| CPC | $1-3 (varies) | $0.50-1.50 | $0.50-2.00 | $0.50-2.00 |
| CVR | 3-5% | 2-4% | 0.5-1% | 1-3% |
| ROAS target | 3-5x | 4-8x | 1.5-3x | 2-5x |

### Key Glossary

| Term | Definition |
|---|---|
| ROAS | Return on Ad Spend = Revenue / Ad Spend |
| CPA | Cost per Acquisition = Spend / Conversions |
| CTR | Click-Through Rate = Clicks / Impressions × 100 |
| CVR | Conversion Rate = Conversions / Clicks × 100 |
| CPM | Cost per 1,000 Impressions |
| CPC | Cost per Click |
| LTV | Customer Lifetime Value |
| CAC | Customer Acquisition Cost |
| MER | Marketing Efficiency Ratio = Total Revenue / Total Ad Spend |
| TOFU/MOFU/BOFU | Top/Middle/Bottom of Funnel |
| IS | Impression Share (Google) |
| QS | Quality Score (Google, 1-10) |
| ASC | Advantage+ Sales Campaign (Meta) |
| CBO | Campaign Budget Optimization (Meta) |
| ABO | Ad Set Budget Optimization (Meta) |
| PMax | Performance Max (Google) |
| DPA | Dynamic Product Ads (Meta retargeting) |
| RLSA | Remarketing Lists for Search Ads (Google) |
| CAPI | Conversions API (Meta server-side tracking) |
| Hook Rate | 3-second video views / impressions × 100 (Meta, benchmark ≥25%) |
