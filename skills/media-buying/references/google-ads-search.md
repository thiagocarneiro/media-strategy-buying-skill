# Google Ads Search -- Agent Reference

---

## 1. Architecture Evolution Decision Tree

### BY CONVERSION VOLUME (per campaign per month)

```
WHEN conversions/month < 15:
  USE SKAG/STAG structure
  SET bidding = Manual CPC (Enhanced CPC discontinued for Search in 2024)
  LIMIT campaigns to 3-5 max
  DO NOT enable Smart Bidding -- insufficient data

WHEN conversions/month = 15-30:
  USE STAG structure (5-15 keywords per ad group, same intent)
  SET bidding = Maximize Conversions
  ENSURE all keywords in ad group answer the same user intent question
  ENSURE RSA is relevant to ALL keywords in the group

WHEN conversions/month = 30-50:
  USE Hagakure / Consolidated structure
  SET bidding = Target CPA or Target ROAS
  ORGANIZE ad groups by destination URL, not keyword groups
  REQUIRE 3,000+ impressions/week per ad group

WHEN conversions/month = 50-100:
  USE Consolidated structure with Broad Match
  SET bidding = Target CPA/ROAS + Broad Match
  MONITOR Search Terms Report weekly

WHEN conversions/month >= 100:
  USE Maximum consolidation + AI Max features
  SET bidding = Target ROAS + AI Max
  TARGET 6-10 campaigns total with clear strategic distinctions
```

### BY BUDGET

| Budget | Structure | Rules |
|---|---|---|
| < $5K/mo | SIAGs only + Brand campaign | Start simple, 3-5 campaigns max |
| $5K-$10K/mo | SIAGs + selective SKAGs | ADD SKAGs only for terms with 500+ impressions/week AND 2%+ of total conversions |
| $10K+/mo | Hybrid: Hagakure + SIAGs + SKAGs | USE Hagakure for URLs with 3,000+ imp/week; SIAGs for mid-volume; SKAGs for top converters |
| $50K+/mo | Full Hagakure with exceptions | CONSOLIDATE aggressively to 6-10 campaigns; leverage Smart Bidding at scale |

### CRITICAL RULE BEFORE SPLITTING CAMPAIGNS

BEFORE creating new campaigns or splitting existing ones, VERIFY: "Will each resulting campaign have enough conversions to exit learning phase and maintain stable performance?" The learning phase requires approximately 50 conversion events or 3 cycles to stabilize.

---

## 2. Hagakure Implementation

### Case Study Reference

- **Before:** 555 campaigns, 56,673 ad groups, 190,159 keywords
- **After:** 3 campaigns serving 75% of revenue
- **Result:** Search revenue EUR 180,000 to EUR 480,000 (+167% year-over-year)

### Hagakure Setup Checklist

- [ ] Organize ad groups by destination URL (NOT by keyword groups)
- [ ] Limit to maximum 20 keywords per ad group
- [ ] Prioritize Broad and Phrase Match for query amplitude
- [ ] Include DSA (or AI Max keywordless) in same campaign to capture uncovered queries
- [ ] REQUIRE Smart Bidding -- Hagakure is designed for automated bidding only
- [ ] REQUIRE native Google Ads conversion tags
- [ ] SET attribution to data-driven with 90-day conversion window
- [ ] ENABLE Enhanced Conversions
- [ ] VERIFY each ad group achieves 3,000+ impressions/week -- IF below threshold, merge with related ad group

### Modern 4-Layer Framework (2026)

```
LAYER 1 -- Brand Campaign:
  CREATE 1 campaign with 1-3 ad groups
  USE Exact Match for brand keywords
  SET bidding = Manual CPC or Maximize Clicks
  SET Impression Share target > 90% (ideally > 95%)
  SEPARATE budget for independent tracking

LAYER 2 -- Search Non-Brand:
  CONSOLIDATE by intent and bidding objective, NOT by product
  ASSIGN each campaign a distinct bidding strategy
  BUILD ad groups with 5-15 keywords sharing identical intent
  ALIGN RSAs with ad group intent

LAYER 3 -- Performance Max:
  POSITION as reach and discovery engine alongside Search
  SEGMENT by product margins, price ranges, or ROAS targets
  LIMIT to 25 asset groups per campaign max

LAYER 4 -- Specialized Campaigns:
  ADD only with clear strategic justification
  EXAMPLES: Demand Gen, Display remarketing, separate Shopping
  RULE: never add campaign types without specific purpose
```

---

## 3. Broad Match Behavior

### Signal Processing

Broad Match is the ONLY match type that uses ALL available signals. Smart Bidding evaluates 100+ contextual signals at auction time:

1. User location
2. Past search behavior
3. Device type (mobile, desktop, tablet)
4. Time of day / day of week
5. Landing page content (semantic analysis)
6. Ad group keyword clusters
7. Browsing behavior (sites visited)
8. Content engagement patterns
9. Local demand shifts
10. User demographics (age, gender, household income)
11. Audience list membership (remarketing, Customer Match, in-market)
12. Operating system
13. Browser
14. Previous interactions with advertiser
15. 11 additional Gemini 3 context signals (added 2025)

### Match Type Decision Tree

```
IF campaign conversions >= 50/month:
  USE Broad Match + Smart Bidding (Target CPA/ROAS)
  MONITOR Search Terms Report weekly
  APPLY audience signals as guardrails
  MAINTAIN active negative keyword management

IF campaign conversions = 30-50/month:
  USE Phrase Match + Smart Bidding
  PROMOTE proven winners to Exact Match
  REVIEW for Broad Match promotion when volume grows

IF campaign conversions < 30/month:
  USE Phrase Match + Exact Match
  SET Manual CPC
  BUILD volume before automating
```

### Broad Match Performance Benchmarks

- Switching Exact to Broad with tCPA = **+35% more conversions** on average
- 62% of Smart Bidding advertisers use Broad Match as primary type
- Upgrading tCPA to tROAS = +14% more conversion value at similar ROAS
- Smart Bidding Exploration: +18% unique query categories, +19% conversions
- Case studies: Meetic Group +70% conversions at same CPA; Tails.com +182% sign-ups, +258% clicks

### Broad Match Requirements Checklist

- [ ] 50+ monthly conversions
- [ ] Smart Bidding active (tCPA or tROAS)
- [ ] Robust conversion tracking (Enhanced Conversions enabled)
- [ ] Active negative keyword management
- [ ] Audience signals configured as guardrails
- [ ] Sufficient budget to allow learning

### WHEN Broad Match Performs Poorly -- DO NOT USE IF:

- < 15 conversions/month
- Incomplete or broken conversion tracking
- Manual CPC bidding (no Smart Bidding)
- No negative keyword hygiene
- Very niche or technical B2B with low search volume
- No audience signals configured
- Extremely limited budget

---

## 4. AI Max for Search

### Prerequisites Checklist

- [ ] Conversion tracking configured and functioning
- [ ] Minimum 30 conversions in the last 30 days
- [ ] Smart Bidding active (Maximize Conversions, Target CPA, or Target ROAS)
- [ ] At least 15 text ads with proven performance

### AI Max vs PMax vs Standard Search

| Aspect | AI Max for Search | Performance Max | Standard Search |
|---|---|---|---|
| Network | Search + Partners only | All Google channels | Search + Partners |
| Query transparency | Full visibility | Limited | Full visibility |
| Negative keyword support | Full | Limited | Full |
| Ideal for | Lead gen, B2B, services | E-commerce, multi-channel | Maximum control |
| Minimum conversions | 30 conv/30 days | 50 conv/30 days | None |

### Performance Benchmarks

- 892-account test: AI Max delivered **23% better CPA than PMax** maintaining 91% of reach
- Google-reported: **+14% more conversions** at similar CPA/ROAS
- For Exact/Phrase Match-heavy campaigns: up to **+27% uplift**
- 250-campaign study: **+13% revenue** but **+16% higher CPA** vs standard Search
- Non-branded campaigns show more volatile results unless messaging is clean

### Power Pack Budget Allocation (2026)

**E-commerce:**
| Campaign Type | % Budget | Function |
|---|---|---|
| Performance Max | 50-60% | Broad reach, all channels |
| AI Max for Search | 25-35% | High-intent search coverage |
| Demand Gen | 10-15% | Awareness and consideration |

**B2B / Services:**
| Campaign Type | % Budget | Function |
|---|---|---|
| Performance Max | 25-35% | Broad reach, all channels |
| AI Max for Search | 40-50% | High-intent search coverage |
| Demand Gen | 15-20% | Awareness and consideration |

### Testing Protocol

1. CREATE 50/50 traffic split using Google Ads Experiments (campaign with AI Max vs without)
2. RUN experiment for 4-6 weeks with sufficient conversion volume for statistical significance
3. EXPECT 10-20% improvement in conversions at similar CPA (for well-prepared accounts)
4. EXPECT flat performance with some incremental reach (for accounts with readiness gaps)
5. KEEP human-written ad copy -- it consistently outperforms automated content in AI Max

### WHEN TO USE AI Max

```
IF goal = scale beyond manual keyword management → USE AI Max
IF need = granular query-level reporting (advantage over PMax) → USE AI Max
IF vertical = lead gen, B2B, or services → USE AI Max
IF need = detailed query-level reporting → USE AI Max
```

### WHEN NOT TO USE AI Max

```
IF need = strict keyword control (compliance campaigns) → DO NOT USE
IF campaign = brand protection → DO NOT USE
IF keywords = highly technical/specific where expansion is harmful → DO NOT USE
IF account conversions < 30/month → DO NOT USE
```

### Brand Safety Controls (available since Feb 2026)

- SET term exclusions: terms AI Max must not use in generated copy
- SET messaging restrictions: tone and message guidelines
- SET URL exclusions: pages that must not receive traffic via Final URL Expansion
- SET brand exclusions: protected brand terms

### DSA to AI Max Transition

```
STEP 1: Activate AI Max keywordless features in existing Search campaigns
STEP 2: Treat as gradual transition, NOT abrupt migration
STEP 3: Wind down DSA campaigns by absorbing function into AI Max-enabled Search
STEP 4: DO NOT migrate DSA to PMax -- absorb into Search to preserve structure,
         search term transparency, and negative keyword architecture
```

---

## 5. Brand vs Non-Brand Management

### Performance Gap Reference

| Metric | Brand | Non-Brand | Gap |
|---|---|---|---|
| ROAS | ~1299% | ~68% | 19x difference |
| Conversion rate | 15-25% | 2-5% | 3-5x higher for brand |
| CPC | 50-70% cheaper than generic | Market rate | 2-3x cheaper for brand |
| Target Impression Share | > 95% | 70-80% | -- |
| Blended CVR (misleading) | 8-12% | Hidden in blended data | MASKS true performance |

### Mandatory Rules

```
ALWAYS separate Brand and Non-Brand into distinct campaigns.
NEVER blend brand and non-brand in the same campaign.

IF brand and non-brand are blended:
  Google's algorithm misinterprets easy brand conversions as overall success
  → causes aggressive bidding on underperforming generic terms
  → reporting becomes dangerously misleading
```

### Brand Campaign Setup

```
SET Impression Share target > 95%
SET bidding = Manual CPC with conservative bids (50-70% lower than generic terms)
MONITOR competitors bidding on brand terms via Auction Insights
IF competitors bid aggressively on your brand → MAINTAIN presence to protect CTR
ADD brand terms as negatives in ALL Non-Brand campaigns
ALLOCATE approximately 20% of total budget to Brand
```

### Non-Brand Campaign Setup

```
SET bidding = Target ROAS or Target CPA using NON-BRAND-ONLY performance data
SET Impression Share target = 70-80%
ALLOCATE approximately 80% of total budget to Non-Brand
SPLIT by intent: high-intent (transactional) vs exploratory (informational)
ALLOCATE 80-85% of Non-Brand budget to proven performers
RESERVE 15-20% for discovery (Broad Match) to find new terms
PROMOTE winning discovery terms to performance campaigns
```

### PMax Brand Exclusions -- IF-THEN Rules

```
IF running Performance Max campaigns:
  APPLY brand exclusions to prevent branded conversions from inflating profitability
  EXPECTED results:
    +5% new customer acquisition
    -7% costs
    +31% ROAS improvement
```

### Budget Testing Framework

- 70% to proven performers
- 20% to optimization of existing approaches
- 10% to testing new campaign types and features

---

## 6. Competitor Bidding Playbook

### Decision Framework

```
BID on competitor terms WHEN:
  - Product is comparable or superior to competitor
  - Budget can absorb 2-4x higher CPCs
  - Clear USP vs competitor exists
  - Dedicated comparison/competitor landing pages are ready
  - Operating in competitive B2B/SaaS with high CLV
  - Prepared for potential bidding war escalation

DO NOT BID WHEN:
  - Budget is constrained
  - No meaningful differentiation
  - Only generic homepage available (no comparison page)
  - Cannot sustain retaliatory bidding
  - Product is significantly inferior
```

### Setup Protocol

```
STEP 1: Identify direct competitors via sales/BD teams
STEP 2: CREATE dedicated "Competitors" campaign (separate from all other campaigns)
STEP 3: CREATE individual ad groups per competitor
STEP 4: CUSTOMIZE keywords and ad copy per competitor
STEP 5: SET bidding = Target Impression Share (NOT Maximize Conversions -- pushes CPCs too high)
         ALTERNATIVE: Max Clicks with max CPC caps
         DO NOT target 100% impression share -- leads to excessive costs
STEP 6: DIRECT traffic to competitor-specific landing pages
STEP 7: EXCLUDE competitor terms from all other campaigns via negative keywords
```

### Performance Expectations

- Expect CPCs 2-4x higher than non-brand generic (can fluctuate rapidly based on competitor's defensive bidding)
- Expect Quality Score of 1-4 (low relevance is inherent and expected)
- Strategy is only viable IF customer LTV justifies inflated CPA

### Evaluation Rules

```
EVALUATE after 2-3 months of running
IF unprofitable after 2-3 months → PAUSE immediately
DO NOT fall into sunk cost fallacy -- discontinue underperforming competitor campaigns
```

### Legal Constraints

- Bidding on competitor brand names as keywords: LEGAL and allowed by Google
- Using trademarked terms in ad copy (headlines, descriptions, display URLs): PROHIBITED without explicit permission
- Research competitor pain points on Reddit, niche forums, review sites (G2, Capterra) to guide messaging

---

## 7. Cannibalization Detection and Resolution

### Red Flags Checklist

WHEN any of these signals appear, INVESTIGATE for cannibalization:

- [ ] Inconsistent ad serving: different ads showing for the same query at different times
- [ ] Jumping ad positions: rapid position changes for specific keywords
- [ ] CPC rises without bid changes
- [ ] CTR declines unexpectedly
- [ ] Previously strong keywords suddenly underperforming
- [ ] Same search terms triggering ads from multiple campaigns
- [ ] Auction Insights showing own domain as competitor
- [ ] Impression Share falling without budget or rank cause

### Monitoring Cadence

```
FIRST 4-6 weeks of new campaigns:
  CHECK Search Terms Report every 3-5 days
  EXPORT data to spreadsheet for duplicate identification

AFTER stabilization:
  CHECK bi-weekly
```

### Resolution Tiers (apply in order)

```
TIER 1 -- Negative Keywords:
  CREATE shared negative keyword lists across campaigns
  ADD cross-campaign negatives to prevent overlap
  FOR PMax vs Search: add high-performance Search keywords as negatives
    in PMax (up to 10,000 negatives per PMax campaign)

TIER 2 -- Match Type Refinement:
  APPLY tiered priority: Exact [highest] → Phrase [moderate] → Broad [lowest]
  AUDIT where Broad/Phrase triggers queries intended for Exact ad groups

TIER 3 -- Geographic Exclusions:
  USE location exclusions and radius targeting to prevent regional overlap
  ENSURE campaign location settings are mutually exclusive

TIER 4 -- Campaign Priority / Consolidation:
  FOR Shopping: use campaign priority system + negatives
  FOR Search: consolidate campaigns with identical intent
  FOR smaller accounts: merge closely related services into single ad groups
```

### Critical Warning

Google's intent-based matching means even paused or unrelated keywords can interfere with ad delivery. DO NOT rely solely on Ad Preview Tool -- cross-verify against Auction Insights and actual performance data.

---

## 8. Search Terms Report Workflow

### Weekly Analysis Protocol

```
STEP 1: Export STR for last 7 days (or 14 days for smaller accounts)
STEP 2: Sort by spend (highest to lowest) -- focus on budget-consuming terms
STEP 3: Filter for zero conversions -- terms with spend but no conversion are negative candidates
STEP 4: Evaluate each term with spend > 50% of target CPA and 0 conversions
         (REQUIRE minimum 10 clicks for statistical significance)

  IF term is irrelevant to business → ADD as negative (Phrase or Exact)
  IF term is relevant but did not convert → KEEP in observation for 1-2 more weeks
  IF term is relevant with high CTR but no conversion → INVESTIGATE landing page

STEP 5: Identify high-performance new terms:
  IF term converts with CPA below target → CONSIDER adding as keyword
  IF term has above-average CTR → VALIDATE intent and landing page alignment
```

### Negative Keyword Decision Criteria

| Condition | Action |
|---|---|
| Term clearly irrelevant to business | ADD as negative immediately (Phrase Match) |
| Term with > 3x target CPA and 0 conversions | ADD as negative (Exact Match for precision) |
| Term with > 2x target CPA after 2 weeks | ADD as negative (evaluate Phrase vs Exact) |
| Term relevant but wrong audience | ADD as negative at campaign-level, NOT account-level |
| Recurring pattern of irrelevant terms | ADD root to shared negative list |

### Negative Keyword Architecture (3 Levels)

```
LEVEL 1 -- Shared Negative Lists (Account-level):
  INCLUDE universally irrelevant terms: "free", "jobs", "employment",
    "how to", "what is", "wikipedia", "DIY", "tutorial"
  LIMIT: up to 5,000 negatives per list, up to 20 lists per account
  WARNING: account-level negatives can silently block valid traffic

LEVEL 2 -- Campaign-level Negatives:
  USE for thematic separation between campaigns
  EXAMPLE: Non-Brand campaign negates brand terms
  ADD cross-negatives between campaigns to prevent cannibalization

LEVEL 3 -- Ad Group-level Negatives:
  USE for surgical exclusions within a campaign
  EXAMPLE: "python course online" ad group negates "in-person"
```

### Over-Negating Rule

```
IF account has 2,000+ negative keywords AND uses Smart Bidding with Broad/Phrase Match:
  RISK: blocking traffic the algorithm could convert
  ACTION: Review and consolidate negatives periodically
```

### N-Gram Analysis Protocol

```
STEP 1: Export all search terms for last 90 days
STEP 2: Decompose each term into:
  - Unigrams (1 word)
  - Bigrams (2 words)
  - Trigrams (3 words)
STEP 3: Aggregate metrics (impressions, clicks, cost, conversions) per n-gram
STEP 4: IF n-gram has high spend + zero conversions → CANDIDATE for negative
STEP 5: IF n-gram has high conversion rate → OPPORTUNITY for new keywords
```

### Visibility Limitation

Since 2020, Google hides "low volume" search terms for privacy reasons, concealing 20-40% of actual terms. N-gram analysis is critical to identify patterns in the visible data.

---

## 9. RSA Optimization

### Asset Performance Ratings -- IF-THEN Rules

```
IF asset rating = "Best" → DO NOT change; keep as-is
IF asset rating = "Good" → KEEP; monitor for changes
IF asset rating = "Low" → REPLACE with new variation
IF asset rating = "Learning" → WAIT 2-4 weeks before evaluating
```

### Headline/Description Diversity Rules

- MIX short and long headlines
- INCLUDE keyword-focused headlines, benefit-focused headlines, AND CTA headlines
- VARY value propositions across all 15 headlines
- TARGET Ad Strength of "Good" or "Excellent"
- Improving from "Poor" to "Excellent" generates **+12% more conversions** on average

### Pinning Strategy

```
GENERAL RULE: Unpinned RSAs perform significantly better across all key metrics.
MINIMIZE pinning wherever possible.

PIN brand name in Headline 1:
  ONLY WHEN compliance or branding absolutely requires it

PIN CTA in Headline 3 or Description 1:
  ONLY WHEN conversion is maximum priority

PIN legal disclaimers:
  WHEN legally mandatory

DO NOT PIN in any other scenario.
NEVER pin more than 2-3 positions simultaneously.
IF pinning is necessary: pin MULTIPLE assets to the same position
  (e.g., 3 headlines pinned to position 1) to allow variation.
```

### Ad Group Split/Merge Signals

```
SPLIT an ad group WHEN:
  - CTR disparity > 2x between keywords in same group
    (e.g., one keyword at 8% CTR, another at 2%)
  - Quality Score variance > 3 points between keywords
    (e.g., QS of 3 and QS of 8 in same group)
  - Keywords require different landing pages
  - Messaging must materially change for a subset
  - A subset of terms reaches 3,000+ impressions/week (warrants Hagakure treatment)

MERGE ad groups WHEN:
  - Each has < 15 conversions/month
  - Themes are close enough to share RSAs
  - Consolidation needed to feed Smart Bidding
  - Volume too low to learn (< 500 impressions/week for several weeks)
  - Search terms overlap heavily (> 30% overlap)

PAUSE an ad group WHEN:
  - CPA > 3x target CPA consistently for 30+ days
  - Zero conversions after spending 3x target CPA
  - CTR < 1% in Search (indicates low relevance)
  - Average Quality Score < 4 with no improvement trend
  - ROAS below 0.8x in last 14 days (pause bottom 20-25%)
  - REQUIRE minimum 1,000 impressions before pausing
```

### Bid and Budget Adjustment Rules

```
ADJUST bids by +/-15-25% based on last 7 days data
LIMIT to 2 bid changes per ad group per day maximum
WHEN a segment delivers ROAS above target for 3 consecutive days:
  REALLOCATE 10-20% of daily budget toward it
USE 28-day data export cycles for comprehensive audits
```

### Creative Testing Protocol

- ALLOCATE 80% impressions to winning creatives
- RESERVE 10-15% for fresh creative concepts
- TEST 3-4 creative variants per asset group
- EVALUATE after 7-14 days
- PAUSE bottom performers after minimum 1,000 impressions

---

## 10. Exact Match Close Variants

### Categories (cannot be opted out)

| Category | Description | Example |
|---|---|---|
| Misspellings | Typos, letter transpositions | [running shoes] matches "runnign shoes" |
| Singular/Plural | Number variations | [running shoes] matches "running shoe" |
| Stemmings | Root word variations | [running shoes] matches "run shoes" |
| Abbreviations | Shortened forms | [VR headset] matches "virtual reality headset" |
| Accents | Accent/diacritic variations | [cafe] matches "cafe" |
| Synonyms | Different words, same meaning | [swimming suit] matches "bathing suit" |
| Word reordering | Same meaning, different order | [women's jeans] matches "jeans for women" |
| Function words | Prepositions added/removed | [jeans for women] matches "jeans women" |
| Implied words | Contextually understood omissions | [daydream VR headset] matches "daydream headset" |
| Same intent | Fundamentally similar searches | [yosemite camping] matches "campsites in yosemite" |

### Key Facts

- Google's early tests: +3% more clicks and conversions on average from close variants
- Close variants CANNOT be disabled -- there is no opt-out option
- Even in 2026, Exact Match still provides the tightest control available
- Exact Match serves as a "profit anchor" for high-intent bottom-of-funnel queries

### Mitigation Rules

```
MONITOR Search Terms Report actively to catch unintended close variant matches
DEPLOY negative keywords strategically for unwanted variant matches
DO NOT load the same term across all three match types in one ad group
USE Exact Match in dedicated profit campaigns
USE Phrase Match in growth campaigns
USE Broad Match in test/discovery campaigns

IF account has high CPCs:
  PRIORITIZE accuracy over volume
  APPLY tighter negative management on close variant matches
```

### Recommended Campaign Architecture by Match Type

```
Profit campaigns → Exact Match (sniper: high-intent, proven converters)
Growth campaigns → Phrase Match (expand on proven themes)
Discovery campaigns → Broad Match (find new opportunities)
```

---

## 11. Impression Share Analysis Decision Tree

### Metric Definitions and Targets

| Metric | Definition | Brand Target | Non-Brand Target |
|---|---|---|---|
| Search IS | % of impressions received vs total eligible | > 95% | 70-80% |
| Search Top IS | % in top of page | > 90% | > 50% |
| Search Abs. Top IS | % in position 1 | Maximum priority | Contextual |
| Lost IS (Budget) | % lost due to insufficient budget | -- | -- |
| Lost IS (Rank) | % lost due to low Ad Rank | -- | -- |

### Diagnostic Decision Tree

```
IF Lost IS (Budget) > 20%:
  → Budget is the bottleneck
  IF budget can be increased → INCREASE gradually by 15-20%
  IF budget is fixed → REDUCE scope:
    - ADD more aggressive negatives
    - FOCUS on geos/times with best conversion rates
    - PAUSE keywords with highest CPA

IF Lost IS (Budget) <= 20%:
  CHECK Lost IS (Rank):
  IF Lost IS (Rank) > 30%:
    → Quality Score and/or bid is the problem
    IF QS < 6 → OPTIMIZE QS components (ad relevance, landing page, expected CTR)
    IF QS >= 6 → CONSIDER increasing bids (Smart Bidding adjusts automatically if ROAS allows)
  IF Lost IS (Rank) <= 30%:
    → IS is adequate; FOCUS on conversion rate optimization

IF both Lost IS (Budget) AND Lost IS (Rank) are elevated:
  → Dual problem: PRIORITIZE QS improvement first, THEN address budget
```
