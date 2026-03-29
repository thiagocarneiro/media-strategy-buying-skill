# Meta Ads Operational Frameworks (A-L)

Agent reference for Meta (Facebook/Instagram) campaign operations. Each section is self-contained. All numbers, thresholds, and formulas are operational constants.

---

## A. Discovery / Intake Questionnaire

Walk the user through every item below before proposing any campaign structure. Mark each item as collected or flag as missing.

### A1. Business Information
- [ ] Business name and legal entity
- [ ] Industry / vertical (e-commerce, SaaS, local service, lead gen, app)
- [ ] Core products or services (list top 3-5 by revenue)
- [ ] Average Order Value (AOV) or average deal size
- [ ] Customer Lifetime Value (LTV) — even a rough estimate
- [ ] Primary market / geography (country, state/region, city if local)
- [ ] Top 3 direct competitors (names + URLs)
- [ ] Unique selling proposition — what differentiates them

### A2. Current Advertising Status
- [ ] Platforms currently running ads on (Meta, Google, TikTok, other)
- [ ] Monthly ad budget (total, and Meta-specific if different)
- [ ] How long have they been running Meta ads (never / <3 months / 3-12 months / 1+ year)
- [ ] Current campaign structure (number of campaigns, ad sets, ads)
- [ ] Best-performing campaign type and its KPIs
- [ ] Worst-performing campaign type and its issues
- [ ] Are they using Advantage+ Sales Campaigns? (yes/no)
- [ ] Pixel installed? (yes/no) — Conversions API (CAPI) implemented? (yes/no)
- [ ] Event Match Quality (EMQ) score if known (target: 6.0+)
- [ ] Historical ROAS, CPA, CTR (last 30 / 90 days)

### A3. Goals and Objectives
- [ ] Primary KPI (ROAS / CPA / CPL / ROAS + volume)
- [ ] Target value for primary KPI (e.g., ROAS >= 3.0, CPA <= $25)
- [ ] Secondary KPIs
- [ ] Monthly revenue target from Meta ads
- [ ] Timeline — when must results be visible (30 / 60 / 90 days)
- [ ] Break-even ROAS (formula: 1 / profit margin as decimal; e.g., 40% margin = 1/0.4 = 2.5x)
- [ ] Acceptable CPA ceiling (formula: LTV x target profit margin)

### A4. Assets Available
- [ ] Existing creative assets: video (count), static images (count), UGC (count)
- [ ] Aspect ratios on hand: 4:5 (feed), 9:16 (Stories/Reels), 1:1 (square)
- [ ] Landing page URLs for each product / offer
- [ ] Product catalog configured in Commerce Manager? (yes/no — required for dynamic retargeting)
- [ ] Customer email/phone list available for Custom Audiences? (yes/no, approximate size)
- [ ] Brand guidelines document? (yes/no)
- [ ] Ability to produce new creative within 2 weeks? (yes/no, internal vs. external)

---

## B. Decision Engine — Maturity Classification

Assess the advertiser's maturity level, then apply the corresponding recommended structure.

### B1. Maturity Levels

| Level | Label | Criteria |
|-------|-------|----------|
| 1 | **New** | No Meta ads history. No Pixel data. No customer list. Budget < $1,500/month. |
| 2 | **Early** | Running Meta ads < 6 months. Pixel has < 50 conversions/week. Budget $1,500-$5,000/month. Some creative assets exist. |
| 3 | **Growth** | Running Meta ads 6-12+ months. Pixel has 50+ conversions/week. Budget $5,000-$25,000/month. Creative production pipeline exists. CAPI implemented. |
| 4 | **Scale** | Established account with proven ROAS. 100+ conversions/week. Budget $25,000+/month. Full Pixel + CAPI with EMQ >= 7.0. Diverse creative library. |

### B2. Decision Tree

```
ASSESS maturity_level:

IF maturity_level = 1 (New):
  -> Structure: 1 ABO test campaign only
  -> Audience: Lookalike 1% from customer list (if available) + 2-3 interest-based ad sets
  -> Budget: $20-$50/day per ad set
  -> Funnel allocation: TOF 60%, MOF 25%, BOF 15%
  -> Priority: Install Pixel + CAPI before launch
  -> Creative minimum: 10 diverse assets (mix video, static, carousel)
  -> Timeline to evaluate: 14-21 days

IF maturity_level = 2 (Early):
  -> Structure: 2 campaigns (ABO test + CBO scale)
  -> Audience: Lookalike 1-2% + interest targeting + broad testing
  -> Budget: Test campaign 25% of total; Scale campaign 75%
  -> Funnel allocation: TOF 50%, MOF 25%, BOF 25%
  -> Priority: Reach 50 conversions/week to unlock broad targeting
  -> Creative minimum: 15-20 assets
  -> Timeline to evaluate: 7-14 days per test cycle

IF maturity_level = 3 (Growth):
  -> Structure: 2 campaigns (ABO test + Advantage+ Sales or CBO scale)
  -> Audience: Broad/Advantage+ (70%) + Custom Audience retargeting (30%)
  -> Budget: Test campaign 10-20% of total; Scale campaign 80-90%
  -> Funnel allocation: TOF 40%, MOF 30%, BOF 30%
  -> Priority: Creative diversification, A/B testing methodology
  -> Creative minimum: 20+ assets, refresh every 2-3 weeks
  -> Timeline to evaluate: 7 days per test cycle

IF maturity_level = 4 (Scale):
  -> Structure: Advantage+ Sales (primary) + ABO test sandbox + Retargeting campaign
  -> Audience: Broad/Advantage+ (primary), narrow retargeting windows
  -> Budget: Test 10% / Advantage+ Scale 60% / Retargeting 20% / Experimental 10%
  -> Funnel allocation: TOF 40%, MOF 25%, BOF 35%
  -> Priority: Horizontal scaling, LTV optimization, AOV increase
  -> Creative minimum: 30+ assets, continuous pipeline
  -> Timeline: Continuous optimization cycles
```

### B3. Budget Calculator

```
Minimum weekly budget per ad set = Target CPA x 50
  Example: CPA target $20 -> $20 x 50 = $1,000/week/ad set -> ~$143/day/ad set

Minimum daily budget for Advantage+ Sales = $100/day (recommended $150-$300/day for small/medium e-commerce)

Test campaign budget = 10-25% of total daily investment
Scale campaign budget = 75-90% of total daily investment

Test budget per creative concept = ~$20 spend before evaluating winner

A/B test minimum budget = Average CPA x Number of variants x 100 (min conversions)
  Example: $5 CPC x 2 variants x 100 = $1,000

Break-even ROAS = 1 / profit_margin_decimal
  Example: 40% margin -> 1 / 0.4 = 2.5x ROAS to break even
```

---

## C. Naming Convention

Apply these templates to every campaign, ad set, and ad. Use underscores as separators. Use lowercase except for proper nouns and abbreviations.

### C1. Campaign Naming

```
[Platform]_[Objective]_[FunnelStage]_[AudienceType]_[BudgetType]_[YYYY-MM]
```

| Placeholder | Values |
|-------------|--------|
| Platform | META |
| Objective | AWARENESS, TRAFFIC, ENGAGEMENT, LEADS, APPPROMOTE, SALES |
| FunnelStage | TOF, MOF, BOF, FULL |
| AudienceType | BROAD, LAL1, LAL3, INTEREST, RETARGET, ASC |
| BudgetType | ABO, CBO, ASC |
| Date | YYYY-MM (launch month) |

Example: `META_SALES_BOF_BROAD_CBO_2026-03`

### C2. Ad Set Naming

```
[AudienceDetail]_[Geo]_[AgeRange]_[Gender]_[Placement]
```

| Placeholder | Values |
|-------------|--------|
| AudienceDetail | LAL1-Purchasers, BROAD-18plus, INT-Fitness, RT-7d-ATC, RT-30d-Visitors |
| Geo | BR, US, LATAM, or specific region |
| AgeRange | 18-65, 25-44, etc. |
| Gender | ALL, M, F |
| Placement | ADV (Advantage+), FEED, STORIES, REELS |

Example: `LAL1-Purchasers_BR_25-54_ALL_ADV`

### C3. Ad Naming

```
[CreativeType]_[Concept]_[Hook]_[Format]_[Version]
```

| Placeholder | Values |
|-------------|--------|
| CreativeType | VID, IMG, CAR, UGC, MOTION |
| Concept | Short descriptor (e.g., PainPoint, SocialProof, Urgency, Testimonial, Demo) |
| Hook | HookA, HookB, HookC (for video variants) |
| Format | 4x5, 9x16, 1x1 |
| Version | v1, v2, v3 |

Example: `UGC_Testimonial_HookA_9x16_v2`

---

## D. IF-THEN Optimization Playbook

Execute these rules at the specified frequency. All thresholds assume the campaign has exited the learning phase (50+ optimization events/week/ad set).

### D1. Daily Monitoring Alerts

```
IF daily spend > 120% of daily budget
  -> THEN pause overdelivering ad sets, check bid strategy

IF any ad set has $0 spend for 24+ hours
  -> THEN check audience size, bid cap, creative rejection status

IF CPM increases > 20% day-over-day
  -> THEN check frequency (see D2), check for audience overlap, check if competitor activity spiked

IF ad is rejected or flagged
  -> THEN review Meta ad policies, fix creative/copy, resubmit within 24 hours

IF Event Match Quality (EMQ) drops below 6.0
  -> THEN audit CAPI implementation, check hashing normalization (trim whitespace, lowercase emails, strip non-numeric from phones)
```

### D2. Optimization Actions (2-3x Per Week)

```
IF frequency > 3.0 for cold audiences (TOF)
  -> THEN refresh creatives or expand audience; frequency > 4.0 = creative fatigue confirmed

IF frequency > 5.0 for warm audiences (retargeting)
  -> THEN narrow retargeting window or pause ad set

IF CTR < 1.0% after 1,000+ impressions
  -> THEN test new hook (first 3 seconds for video), test new headline, test different creative format

IF CPA > 120% of target after minimum spend threshold reached (CPA_target x 3)
  -> THEN pause ad set; reallocate budget to better performers

IF an ad has spent 2x the target CPA with zero conversions
  -> THEN pause the ad immediately

IF ROAS < break-even ROAS for 3+ consecutive days
  -> THEN reduce budget by 20%, review creative and landing page alignment

IF Hook Rate < 25% (video)
  -> THEN replace first 3 seconds; test a new hook style

IF Hold Rate < 25% (video, post-hook retention)
  -> THEN restructure video body content; shorten to 7-15 seconds

IF ThruPlay Rate is declining week-over-week
  -> THEN creative fatigue likely; queue new creative variants

IF winning ad has been running 2-3 weeks without refresh
  -> THEN produce iterations (same message, different format: video->carousel, image->UGC)
```

### D3. Weekly Scaling Decisions

```
IF ad set CPA is below target for 5-7 consecutive days AND frequency < 3.0
  -> THEN scale vertically: increase budget by 20% (max)
  -> WAIT minimum 48 hours before next increase
  -> DO NOT increase budget by more than 20% at once (triggers partial relearning)

IF ad set CPA is below target for 5-7 days BUT frequency >= 3.0
  -> THEN scale horizontally: duplicate to new audience (Lookalike 3-5%, new geo, broader demo)
  -> Assign 50-70% of original budget to the new duplicate

IF campaign ROAS is 2.5x-4.0x consistently
  -> THEN eligible for CBO automatic budget distribution

IF test campaign identifies a winner (CPA below target, 95% statistical significance, 20%+ improvement over control)
  -> THEN migrate to scale campaign using ORIGINAL Post ID (do NOT duplicate the ad — preserves social proof, up to 15% higher CTR)

IF CPA is rising faster than budget increases
  -> THEN campaign has hit efficiency ceiling; stop vertical scaling, attempt horizontal scaling or accept current maximum

IF campaign has been at peak for 2+ weeks with no improvement
  -> THEN clone structure, reset learning, scale from clean base
```

### D4. Creative Refresh Triggers

```
IF creative has run for 3+ weeks without iteration
  -> THEN mandatory refresh: produce new variants in different formats

IF CPM is rising while CTR is declining on the same ad
  -> THEN Andromeda is penalizing for creative fatigue; replace immediately

IF creative similarity across account is high (most ads share same concept/angle)
  -> THEN Andromeda penalizes the entire account with higher CPMs; diversify at concept level

Budget allocation for creative pipeline (70/20/10 rule):
  -> 70% on proven formats that already perform
  -> 20% on new concept tests
  -> 10% on experimental (voiceovers, memes, trends)

Production cadence: Reserve 4 hours/month to create 15-20 creative variations. Plan 90 days ahead for seasonal needs.
```

---

## E. Diagnostic Triage Tree

When performance degrades, follow this decision tree from top to bottom. Check each node before moving to the next.

### E1. CPA Increased

```
CPA increased?
├── Check 1: Did you make changes in the last 72 hours?
│   ├── YES -> Campaign may have re-entered learning phase. Wait 3-5 days. DO NOT make further changes.
│   └── NO -> Continue to Check 2
├── Check 2: Has frequency increased above 3.0 (cold) or 5.0 (warm)?
│   ├── YES -> Creative fatigue. Refresh creatives immediately.
│   └── NO -> Continue to Check 3
├── Check 3: Has CPM increased > 20%?
│   ├── YES -> Increased competition or seasonal spike. Check auction overlap. See E3.
│   └── NO -> Continue to Check 4
├── Check 4: Has CTR dropped below previous average?
│   ├── YES -> Creative or copy issue. See E2.
│   └── NO -> Continue to Check 5
├── Check 5: Is conversion rate (CVR) on the landing page declining?
│   ├── YES -> Landing page issue (load time, broken checkout, offer mismatch). Fix landing page.
│   └── NO -> Continue to Check 6
├── Check 6: Has audience size shrunk or been exhausted?
│   ├── YES -> Expand audience. Scale horizontally.
│   └── NO -> Continue to Check 7
└── Check 7: Is Pixel/CAPI reporting correctly? Check Events Manager.
    ├── Events showing "1 event from 2 sources" -> Deduplication OK. Issue is elsewhere.
    └── Events showing "1 event from 1 source" -> Deduplication BROKEN. Fix CAPI immediately. You are losing 30-50% of conversion data.
```

### E2. CTR Dropped

```
CTR dropped?
├── Has the ad been running 2+ weeks unchanged?
│   ├── YES -> Creative fatigue. Refresh hook and visuals.
│   └── NO -> Continue
├── Was copy or headline changed recently?
│   ├── YES -> New copy may be underperforming. A/B test against previous version.
│   └── NO -> Continue
├── Has audience changed?
│   ├── YES -> New audience may not resonate with current creative. Test creative-audience fit.
│   └── NO -> Continue
├── Check Hook Rate (video ads) — is it below 25%?
│   ├── YES -> First 3 seconds are failing. Replace hook.
│   └── NO -> Hook is fine; problem is in body/CTA
└── Check ad placement breakdown — is one placement dragging down overall CTR?
    └── YES -> Consider excluding that placement or creating placement-specific creative
```

### E3. CPM Increased

```
CPM increased?
├── Is this a seasonal period (Black Friday, Christmas, Mothers Day)?
│   ├── YES -> Expected. CPMs rise 20-50% during peak seasons. Adjust targets temporarily.
│   └── NO -> Continue
├── Has frequency increased?
│   ├── YES -> Audience saturation. Expand audience or refresh creative.
│   └── NO -> Continue
├── Has audience overlap between ad sets increased?
│   ├── YES -> Consolidate ad sets. Use exclusions.
│   └── NO -> Continue
├── Is creative similarity across the account high?
│   ├── YES -> Andromeda penalty. Diversify at concept level, not just iteration level.
│   └── NO -> Continue
└── Check industry CPM benchmarks — global median is $13.48. CPM rose 20% industry-wide in 2025.
    └── If your CPM is within industry range, the increase may be market-driven.
```

### E4. Seven-Point Diagnostic Checklist

Run through all 7 whenever performance degrades unexpectedly:

- [ ] 1. **Tracking integrity**: Verify Pixel fires on all key pages. Verify CAPI events match. Check EMQ >= 6.0. Confirm deduplication ("1 event from 2 sources").
- [ ] 2. **Learning phase status**: Is any ad set in learning phase or "learning limited"? If yes, do not touch it for 72 hours minimum.
- [ ] 3. **Creative health**: Check frequency per ad. Any ad above frequency 3.0 (cold) or 5.0 (warm) = fatigue. Check Hook Rate >= 25%.
- [ ] 4. **Audience health**: Check overlap between ad sets (Audience Overlap tool). Ensure exclusions are applied between campaigns.
- [ ] 5. **Budget adequacy**: Each ad set must have budget >= CPA_target x 50 per week. Below this = "learning limited."
- [ ] 6. **Landing page performance**: Page load time < 3 seconds. Conversion rate stable. Offer matches ad promise.
- [ ] 7. **External factors**: Competitor activity change. Seasonal CPM shifts. Platform policy updates. Algorithm updates.

---

## F. Learning Phase Rules

### F1. What Triggers Learning Phase

The following changes reset or partially reset the learning phase. AVOID making these during an active learning phase:

- Changing the budget by more than 20% at once
- Changing the bid strategy or bid cap
- Changing the optimization event (e.g., Purchase to AddToCart)
- Changing targeting (audience, age, geo, placements)
- Adding or removing creatives from an ad set
- Pausing the ad set for 7+ days and reactivating
- Changing the campaign objective
- Any structural change to the ad set

### F2. DO NOT Do During Learning Phase

- DO NOT pause or restart the ad set
- DO NOT change the budget (up or down)
- DO NOT add or remove ads from the ad set
- DO NOT change audience targeting
- DO NOT change the optimization event
- DO NOT judge performance — data is unreliable during this period
- DO NOT make any edits for at least 72 hours (ideal: 3-5 days)
- DO NOT panic if CPA spikes — the algorithm is still exploring

### F3. How to Exit Learning Phase

- Accumulate 50 optimization events per ad set per week
- If the optimization event is "Purchase" with a $20 CPA target, the minimum weekly spend per ad set is $1,000 (~$143/day)
- If an ad set is stuck in "Learning Limited," it means the budget is too low or the audience is too narrow for 50 events/week. Solutions:
  - Increase budget
  - Broaden audience
  - Switch to a higher-volume optimization event (e.g., AddToCart instead of Purchase) temporarily
  - Consolidate ad sets (fewer ad sets = more budget per ad set)

### F4. Duration Expectations

| Scenario | Expected Duration |
|----------|-------------------|
| New campaign launch | 3-7 days |
| Budget increase <= 20% | No reset (or minimal) |
| Budget increase > 20% | Partial relearning, 2-4 days |
| New creative added to existing ad set | Partial relearning, 1-3 days |
| Major structural change (audience, objective) | Full reset, 3-7 days |
| Campaign paused 7+ days then reactivated | Full reset, 3-7 days |

---

## G. Weekly Reporting Template

### G1. Metrics to Include

| Metric | Source | Funnel Stage |
|--------|--------|-------------|
| Spend (total, by campaign) | Ads Manager | All |
| Impressions | Ads Manager | All |
| Reach | Ads Manager | TOF |
| Frequency | Ads Manager | All |
| CPM | Ads Manager | TOF |
| Clicks (link clicks) | Ads Manager | MOF |
| CTR (link) | Ads Manager | MOF |
| CPC (link) | Ads Manager | MOF |
| Conversions (by event) | Ads Manager | BOF |
| CPA / Cost per Purchase | Ads Manager | BOF |
| ROAS | Ads Manager | BOF |
| CVR (conversion rate) | Ads Manager + Analytics | BOF |
| AOV (average order value) | Analytics / Backend | BOF |
| Hook Rate (3-sec video views / impressions) | Ads Manager | TOF/MOF |
| Hold Rate (ThruPlay / 3-sec views) | Ads Manager | TOF/MOF |
| EMQ Score | Events Manager | Technical |

### G2. Alert Thresholds

| Metric | GREEN (on track) | YELLOW (warning) | RED (action needed) |
|--------|-------------------|-------------------|---------------------|
| ROAS | >= target ROAS | 80-99% of target ROAS | < 80% of target ROAS |
| CPA | <= target CPA | 100-120% of target CPA | > 120% of target CPA |
| CTR | >= 1.5% | 1.0-1.49% | < 1.0% |
| CPM | <= 120% of benchmark | 120-150% of benchmark | > 150% of benchmark |
| Frequency (cold) | < 2.0 | 2.0-3.0 | > 3.0 |
| Frequency (warm) | < 3.0 | 3.0-5.0 | > 5.0 |
| Hook Rate (video) | >= 30% | 25-29% | < 25% |
| CVR (landing page) | >= industry avg | 70-99% of industry avg | < 70% of industry avg |
| EMQ Score | >= 7.0 | 6.0-6.9 | < 6.0 |
| Learning Status | Active / Exited | Learning | Learning Limited |
| Weekly conversions/ad set | >= 50 | 30-49 | < 30 |

### G3. Benchmark Reference (Global 2025)

| Metric | Global Average | Global Median |
|--------|---------------|---------------|
| CTR | 0.90% | 2.19% |
| CPC | $1.72 | — |
| CVR | 9.21% | 1.57% |
| CPA | $18.68 | $38.17 |
| CPM | — | $13.48 |
| ROAS | 2.19:1 | 1.93:1 |

Industry-specific ROAS targets: Automotive 2.54, Beauty 3.00+, Sports/Outdoor 2.28, Travel 2.25. Most brands target 2-3x ROAS as healthy.

---

## H. Creative Briefing Template

Fill in every field before requesting creative production.

### H1. Brief Fields

```
PROJECT:        [Campaign name / product name]
OBJECTIVE:      [Awareness / Consideration / Conversion]
FUNNEL STAGE:   [TOF / MOF / BOF]
TARGET AUDIENCE:[Demographics, interests, pain points]
KEY MESSAGE:    [Single core message in one sentence]
CTA:            [Compre Agora / Saiba Mais / Cadastre-se / Fale Conosco]
OFFER:          [Discount, free shipping, trial, bundle — if applicable]
TONE:           [Professional / Casual / Urgent / Educational / Aspirational]
MANDATORY ELEMENTS: [Logo, brand colors, legal disclaimers, hashtags]
REFERENCE ADS:  [Links to competitor ads or inspiration from Meta Ad Library]
DELIVERABLES:   [See specs table below]
DEADLINE:       [Date]
```

### H2. Specs by Format

| Format | Aspect Ratio | Resolution (min) | Max File Size | Duration | Notes |
|--------|-------------|-------------------|---------------|----------|-------|
| Feed Video | 4:5 | 1080 x 1350 px | 4 GB | 7-15 sec (sweet spot) | Up to 15% better than square. Add captions. |
| Feed Image | 4:5 | 1080 x 1350 px | 30 MB | — | Single focal point. High contrast. |
| Feed Carousel | 1:1 | 1080 x 1080 px | 30 MB/card | — | 3-5 cards. Sequential narrative. |
| Stories/Reels | 9:16 | 1080 x 1920 px | 4 GB | 7-15 sec (Reels), up to 15 sec (Stories) | Keep critical elements in center third (safe zone). |
| Square | 1:1 | 1080 x 1080 px | 30 MB | — | Versatile, all placements. |
| Horizontal | 16:9 | 1920 x 1080 px | 4 GB | — | Lowest priority on mobile. In-stream only. |

### H3. Requirements by Funnel Stage

| Stage | Creative Type | Message Focus | CTA Style |
|-------|--------------|---------------|-----------|
| TOF | Short educational video (7-15s), UGC, carousel storytelling, demos | Problem awareness, brand introduction | Soft (Saiba Mais, Assista) |
| MOF | Testimonials, comparisons, how-to, detailed demos, trial offers | Social proof, product consideration | Medium (Veja Como Funciona, Teste Gratis) |
| BOF | Direct offers with urgency, dynamic retargeting, abandoned cart carousel, testimonials with CTA | Conversion, limited-time offer, free shipping | Hard (Compre Agora, Garanta o Seu, Ultimo Dia) |

### H4. Video Production Checklist

- [ ] Hook in first 3 seconds (question, shocking stat, visual result, contrarian statement)
- [ ] Core message delivered within 7-15 seconds
- [ ] Captions/subtitles added (assume sound off)
- [ ] Text overlays for key points
- [ ] Single clear CTA
- [ ] Filmed/designed mobile-first (98% of Meta users are on mobile)
- [ ] Provided in both 4:5 and 9:16 aspect ratios
- [ ] Safe zones respected for 9:16 (no critical elements in top/bottom zones)

---

## I. Seasonal Calendar — Brazil (BR)

### I1. High-Impact Dates

| # | Date(s) | Event | Impact Level | Pre-Season Start |
|---|---------|-------|-------------|------------------|
| 1 | Feb (variable) | Carnaval | HIGH | 3-4 weeks before |
| 2 | Mar 8 | Dia Internacional da Mulher | MEDIUM | 2 weeks before |
| 3 | Apr (variable) | Pascoa / Easter | MEDIUM | 3 weeks before |
| 4 | May (2nd Sunday) | Dia das Maes | VERY HIGH | 4-6 weeks before |
| 5 | Jun 12 | Dia dos Namorados | HIGH | 3-4 weeks before |
| 6 | Jun-Jul | Festas Juninas / Julinas | MEDIUM | 2-3 weeks before |
| 7 | Aug (2nd Sunday) | Dia dos Pais | HIGH | 3-4 weeks before |
| 8 | Sep 7 | Independencia do Brasil | LOW-MEDIUM | 1-2 weeks before |
| 9 | Oct 12 | Dia das Criancas | HIGH | 3-4 weeks before |
| 10 | Nov (4th Friday) | Black Friday | VERY HIGH | 6-8 weeks before (creative production in Sep) |
| 11 | Dec 25 | Natal / Christmas | VERY HIGH | 4-6 weeks before |

### I2. Pre-Seasonal Rules

```
IF event is VERY HIGH impact (Black Friday, Dia das Maes, Natal):
  -> Start creative production 8-10 weeks before
  -> Begin TOF awareness campaigns 4-6 weeks before
  -> Build retargeting audiences from TOF engagement 3-4 weeks before
  -> Increase daily budget 20-30% starting 2 weeks before
  -> Pre-test seasonal creatives in test campaign 3 weeks before

IF event is HIGH impact:
  -> Start creative production 4-6 weeks before
  -> Begin TOF campaigns 3 weeks before
  -> Increase budget 15-20% starting 1-2 weeks before

IF event is MEDIUM impact:
  -> Adjust messaging and creative 2-3 weeks before
  -> Budget increase 10-15% starting 1 week before
```

### I3. During-Seasonal Rules

```
-> Expect CPMs to rise 20-50% during peak dates (this is normal)
-> Switch to Lowest Cost bidding if not already (maximum flexibility for algorithm)
-> Increase creative rotation frequency — audiences see more ads during peak periods
-> Activate BOF retargeting campaigns with urgency messaging
-> Monitor frequency daily — cap at 2.0 for cold, 4.0 for warm during high-volume periods
-> DO NOT launch new untested campaigns during peak — use only pre-validated winners
-> DO NOT make structural changes during peak — ride momentum
```

### I4. Post-Seasonal Rules

```
-> Reduce budgets gradually (20% decrements every 3-4 days) — do not cut abruptly
-> Expect CPA to spike temporarily as purchase intent drops; do not panic
-> Pause seasonal-specific creatives within 3 days after the event
-> Capture learnings: which creatives won, which audiences converted, what was the peak CPA/ROAS
-> Build Custom Audiences from seasonal converters for future campaigns
-> Start planning next seasonal event immediately (90-day ahead rule)
-> Run re-engagement campaigns to seasonal buyers 14-30 days after purchase
```

---

## J. Competitive Analysis via Meta Ad Library

### J1. Step-by-Step Procedure

```
Step 1: Navigate to Meta Ad Library
  -> URL: https://www.facebook.com/ads/library/
  -> Select country (Brazil) and category (All ads)

Step 2: Search for each competitor (from intake questionnaire A1)
  -> Enter competitor brand name or page name
  -> Filter by platform (Facebook, Instagram, or both)
  -> Filter by media type (Images, Videos, Memes) if needed

Step 3: Analyze active ads — record the following for each competitor:
  -> Total number of active ads (indicates investment level)
  -> Date ranges (how long ads have been running — long-running = likely winners)
  -> Creative formats used (video, static, carousel, UGC)
  -> Messaging themes (discount-led, benefit-led, social proof, urgency)
  -> Hooks used in video ads (first 3 seconds pattern)
  -> CTA buttons used (Shop Now, Learn More, Sign Up, etc.)
  -> Landing page destinations (click through to see where they send traffic)
  -> Multiple versions of same concept (indicates A/B testing)

Step 4: Identify patterns across all competitors:
  -> Which format appears most frequently? (likely industry best practice)
  -> What messaging angle dominates? (opportunity to differentiate)
  -> Are competitors running seasonal/promotional campaigns?
  -> What is the typical ad longevity? (short-lived = high churn; long-lived = proven)

Step 5: Document findings
  -> Record top 3-5 competitor ads per competitor as reference
  -> Note any gaps: angles, formats, or messages NO competitor is using (opportunity)
  -> Flag creative approaches to test in your own campaigns
```

### J2. What to Look For — Checklist

- [ ] Creative formats: What % is video vs. image vs. carousel?
- [ ] Messaging: Discount/price-led or value/benefit-led?
- [ ] Social proof: Are they using testimonials, review counts, UGC?
- [ ] Urgency: Limited-time offers, countdown language?
- [ ] Frequency of new ads: How often do they refresh creative?
- [ ] Ad duration: Ads running 30+ days are likely proven performers — study them closely
- [ ] Landing page quality: Fast loading? Clear CTA? Mobile-optimized?
- [ ] Partnership Ads: Are they using creator/influencer partnerships?
- [ ] Number of active ads: 1-5 = small operation; 10-20 = moderate; 50+ = serious advertiser

### J3. How to Interpret Findings

```
IF competitor has many long-running ads (30+ days) in one format
  -> That format likely works in this industry. Test a similar format with differentiated messaging.

IF competitor refreshes creative every 1-2 weeks
  -> Industry has high creative fatigue rate. Plan for aggressive refresh cadence.

IF no competitor is using video/UGC
  -> Opportunity to differentiate. Video and UGC typically outperform static. Test immediately.

IF all competitors use discount-led messaging
  -> Market is price-sensitive. Either compete on price or differentiate with value/benefit messaging.

IF competitor Ad Library shows few active ads
  -> They may not be investing heavily in Meta. Opportunity to dominate the channel.
```

---

## K. Budget Pacing

### K1. Monthly Distribution by Week

| Week | % of Monthly Budget | Rationale |
|------|---------------------|-----------|
| Week 1 (days 1-7) | 20% | Ramp-up / learning phase data collection |
| Week 2 (days 8-14) | 25% | Optimization begins, early winners identified |
| Week 3 (days 15-21) | 30% | Peak investment on validated performers |
| Week 4 (days 22-end) | 25% | Maintain momentum, prepare for next month |

### K2. Seasonal Pacing Adjustments

```
IF seasonal event falls in Week 3 or 4:
  -> Shift distribution to: W1: 15%, W2: 20%, W3: 35%, W4: 30%

IF seasonal event falls in Week 1 or 2:
  -> Shift distribution to: W1: 30%, W2: 35%, W3: 20%, W4: 15%

IF month contains VERY HIGH impact event (Black Friday, Natal):
  -> Increase total monthly budget by 30-50% for that month
  -> Concentrate 50-60% of monthly budget in the event week and the week before

IF month is a low-demand period (January, post-Carnaval):
  -> Reduce total monthly budget by 10-20%
  -> Allocate more to TOF and testing (build audiences for upcoming seasons)
```

### K3. Daily Monitoring Thresholds

| Pacing Metric | GREEN | YELLOW | RED |
|---------------|-------|--------|-----|
| Daily spend vs. daily target | 80-110% | 60-79% or 111-130% | < 60% or > 130% |
| Weekly spend vs. weekly target | 85-105% | 70-84% or 106-120% | < 70% or > 120% |
| Monthly projected vs. monthly budget | 90-105% | 80-89% or 106-115% | < 80% or > 115% |

```
IF daily spend < 60% of daily target:
  -> Check for ad rejections, audience exhaustion, bid caps too restrictive, learning limited status

IF daily spend > 130% of daily target:
  -> Check for incorrect budget settings, campaign spending limits not set, cost cap too loose

IF weekly spend is tracking > 115% of weekly target:
  -> Reduce daily budgets by 10-15% to course-correct
  -> OR set campaign spending limits to prevent overshoot

IF weekly spend is tracking < 70% of weekly target:
  -> Check campaign delivery status
  -> If delivery is fine but spend is low: audience may be too narrow or bids too conservative
  -> Consider broadening audience or switching to Lowest Cost bidding
```

---

## L. Glossary of Operational Terms

| # | Term | Definition | Context |
|---|------|-----------|---------|
| 1 | **ROAS** | Return on Ad Spend. Revenue generated per unit of ad spend. Formula: Revenue / Ad Spend. | A ROAS of 3.0 = $3 revenue per $1 spent. Does NOT equal profit. Break-even ROAS = 1 / profit margin. |
| 2 | **CPA** | Cost Per Acquisition. Average cost to generate one conversion. | Must be compared against LTV, not evaluated in isolation. |
| 3 | **CPM** | Cost Per Mille. Cost per 1,000 impressions. | Global median $13.48 (2025). Rose 20% YoY. Higher CPMs in competitive seasons. |
| 4 | **CTR** | Click-Through Rate. Clicks / Impressions x 100. | Global average 0.90%, median 2.19%. Below 1.0% = creative or targeting issue. |
| 5 | **CVR** | Conversion Rate. Conversions / Clicks x 100. | Global average 9.21%, median 1.57%. High CTR + low CVR = landing page problem. |
| 6 | **CPC** | Cost Per Click. Ad Spend / Clicks. | Global average $1.72. Traffic campaigns achieve ~$0.70. |
| 7 | **AOV** | Average Order Value. Total revenue / number of orders. | Higher AOV allows higher CPA ceiling. Even $5 increase in AOV can significantly improve ROAS. |
| 8 | **LTV** | Customer Lifetime Value. Total revenue a customer generates over their relationship. | CPA must always be evaluated relative to LTV. |
| 9 | **Hook Rate** | 3-second video views / impressions x 100. | Benchmark: >= 25%. The Andromeda algorithm evaluates the hook separately from the rest of the video. |
| 10 | **Hold Rate** | ThruPlay (15+ sec or complete views) / 3-second views x 100. | Benchmark: >= 25%. Indicates sustained engagement past the hook. |
| 11 | **EMQ** | Event Match Quality. Score (0-10) representing how well conversion events match Meta user profiles. | Target: >= 6.0, ideal 7.0-8.0+. Below 6.0 = "leaving money on the table." |
| 12 | **CBO** | Campaign Budget Optimization (now Advantage Campaign Budget). Budget set at campaign level; algorithm distributes across ad sets. | Use for scaling validated winners. Requires budget >= 50x CPA target per week. |
| 13 | **ABO** | Ad Set Budget Optimization. Budget set per ad set for granular control. | Use for testing new creatives and audiences. Migrating winners to CBO for scale. |
| 14 | **ASC** | Advantage+ Sales Campaigns. AI-driven campaign type combining prospecting and retargeting. | Delivers 22% more ROAS, 73% less manual management. Min $100/day budget. 10-20 unique creatives per ad set. |
| 15 | **Andromeda** | Meta's AI-based ad retrieval engine (launched Oct 2025). Prioritizes creative quality over manual targeting. | Penalizes accounts with low creative diversity by raising CPMs. Evaluates hooks, text overlays, audio, and predicts creative fatigue. |
| 16 | **Learning Phase** | Period where Meta's algorithm explores delivery options. Requires ~50 optimization events/week/ad set to exit. | Do NOT make changes during this phase. Lasts 3-7 days typically. |
| 17 | **Learning Limited** | Status indicating an ad set cannot exit learning phase due to insufficient events. | Solutions: increase budget, broaden audience, use higher-volume event, consolidate ad sets. |
| 18 | **Post ID** | Unique identifier for an ad's social post. Reusing Post IDs when scaling preserves likes, comments, shares. | Always scale winners using original Post ID. Do NOT duplicate. Up to 15% higher CTR from preserved social proof. |
| 19 | **CAPI** | Conversions API. Server-side event tracking that sends data directly to Meta, bypassing browser limitations. | Captures 20-40% more conversions than Pixel alone. Required for accurate attribution post-iOS 14+. |
| 20 | **Deduplication** | Process of using a shared event_id between Pixel and CAPI to prevent double-counting conversions. | event_id must be string, case-sensitive, unique per event (not per session). 48-hour deduplication window. |
| 21 | **Broad Targeting** | Minimal audience restrictions, letting Meta's algorithm find optimal users. | Best when Pixel has 50+ conversions/week. Sweet spot: 1-5 million audience size. |
| 22 | **Lookalike Audience** | Audience modeled on a source audience (e.g., best customers). 1% = most similar, 10% = broadest. | 1-2% for high-quality prospecting; 3-5% for scale; 6-10% nearly equivalent to broad. |
| 23 | **TOF / MOF / BOF** | Top / Middle / Bottom of Funnel. Stages of the customer journey mapped to campaign objectives. | TOF = awareness (40-50% budget), MOF = consideration (25-30%), BOF = conversion (25-35%). |
| 24 | **Creative Fatigue** | Decline in ad performance due to audience overexposure to the same creative. | Signals: frequency > 3.0 (cold), rising CPM + declining CTR. Refresh every 2-3 weeks. |
| 25 | **Kill Criteria** | Predefined thresholds for pausing underperforming ads/ad sets. | Pause if CPA exceeds 120% of target after minimum spend. Pause if 2x target CPA spent with zero conversions. |
