# Meta Ads Strategy Reference (2025-2026)

Agent instructions for planning, structuring, and optimizing Meta (Instagram/Facebook) advertising campaigns.

---

## 1. Andromeda Algorithm Compliance

The Andromeda algorithm (launched globally October 2025) replaced legacy targeting systems. The algorithm uses creative quality as the primary targeting signal -- not manual audience segmentation.

### Mandatory Rules

- ALWAYS ensure creative diversity at the CONCEPT level. Variations of the same concept do NOT satisfy this requirement.
- NEVER run a high volume of similar creatives. Andromeda penalizes high creative similarity with elevated CPMs.
- ALWAYS design hooks for the first 3 seconds separately. Andromeda evaluates the hook independently from the rest of the video.
- ASSUME Andromeda detects: text overlays, audio signals (music, voiceover style), and creative fatigue patterns (proactive reduction of delivery to saturated audiences).

### Compliance Benchmarks

- Accounts that comply with Andromeda requirements achieve on average:
  - +22% ROAS
  - +17% conversions
  - -16% costs
- Non-compliance (low creative diversity) results in higher CPMs and degraded delivery.

### Creative Diversity Checklist

- [ ] Multiple distinct CONCEPTS (not just color/copy swaps of one concept)
- [ ] Multiple ANGLES per product (economy, quality, urgency, social proof, aspirational)
- [ ] Multiple FORMATS (video, static image, carousel, UGC, motion graphics)
- [ ] Multiple HOOKS (question, shocking stat, before/after, demo)
- [ ] Multiple VISUAL STYLES (professional, casual UGC, flat design, lifestyle photography)

---

## 2. Campaign Structure

### Two-Campaign Model

Use exactly two campaigns:

#### Campaign 1: Creative Test (Sandbox)

- Budget optimization: ABO (Ad Set Budget Optimization)
- Ad sets: 5-10 per campaign, grouped by distinct creative concept
- Budget: $20-50/day per ad set
- Total test budget: DO NOT exceed 10-25% of total daily investment
- Winner identification: a creative winner typically emerges after ~$20 spend per concept
- Purpose: identify winning creatives before committing scale budget

#### Campaign 2: Scale / Winners

- Budget optimization: CBO (Campaign Budget Optimization) OR Advantage+ Sales
- Targeting: broad, with minimal restrictions
- Budget: 75-90% of total budget
- CRITICAL: USE POST IDs from winning ads. NEVER duplicate creatives. Post IDs preserve social proof (likes, comments, shares) and maintain Estimated Action Rate, yielding up to +15% CTR.

### Campaign Objectives Available

| Objective | When to Use |
|-----------|-------------|
| Awareness | Introduce product/brand to cold audiences |
| Traffic | Drive site visits with optimized CPC |
| Engagement | Nurture mid-funnel (interactions, messages, video views) |
| Leads | Capture qualified contacts via forms or messages |
| App Promotion | Mobile acquisition campaigns |
| Sales | Bottom-funnel direct conversion/ROAS optimization |

### Advantage+ Sales Campaigns (ASC)

IF the client sells e-commerce products, leads, or app installs, RECOMMEND Advantage+ Sales as the primary scale campaign.

- ASC delivers on average 22% more ROAS vs traditional campaigns
- 73% reduction in manual management time
- Recommended daily budget: $100/day minimum; $150-300/day for small/medium e-commerce
- Ad sets: 1-3 maximum per campaign
- Creatives: 10-20 unique creatives per ad set
- Targeting: broad with minimal restrictions
- Existing audience cap: 10-30% of total budget allocated to retargeting

---

## 3. Full-Funnel Strategy

IF implementing full-funnel, expect up to 91% increase in overall marketing effectiveness.

### TOF (Top of Funnel) -- Awareness

- Budget allocation: 40-50%
- Objectives: Awareness, Engagement (video views), Traffic
- Creative types:
  - Short educational/storytelling videos (7-15 seconds)
  - Problem-demonstration content
  - UGC that does not look like advertising
  - Sequential narrative carousels
  - Day-in-the-life demos that feel organic
- Key metrics and benchmarks:
  - CPM, Reach, Frequency
  - Hook Rate (first 3-second retention): benchmark 25%+
  - Hold Rate (sustained engagement): benchmark 25%+
  - ThruPlays (15+ seconds or complete view)

### MOF (Middle of Funnel) -- Consideration

- Budget allocation: 25-30%
- Objectives: Engagement, Leads, Traffic (to content-rich pages)
- Creative types:
  - Customer testimonials and social proof
  - Product comparisons and demonstrations
  - How-to content and tutorials
  - Trial offers, samples, or exclusive content
- Key metrics: CTR, CPC, Engagement Rate, Cost per Lead, Time on Site

### BOF (Bottom of Funnel) -- Conversion

- Budget allocation: 25-35%
- Objectives: Sales, Leads (high-intent forms)
- Creative types:
  - Direct offers with urgency (limited discount, free shipping)
  - Dynamic retargeting with product catalog
  - Testimonials with clear CTA
  - Abandoned cart product carousels
- Key metrics: ROAS, CPA, Conversion Rate, Cost per Purchase, AOV

### Budget Allocation Decision Tree

```
IF new business with little pixel history:
  -> Allocate up to 60% to TOF (generate data to feed the algorithm)
  -> Gradually shift toward MOF+BOF as conversion data grows

IF mature business with robust conversion history:
  -> Follow standard split: 40-50% TOF / 25-30% MOF / 25-35% BOF
  -> Shift budget toward MOF+BOF as audience base is established
```

### Cross-Funnel Technical Setup

- [ ] Build custom audiences from engagement at each funnel stage to feed the next stage
- [ ] Configure exclusion audiences to avoid wasted spend on already-converted users
- [ ] Implement Pixel + CAPI with deduplication for accurate attribution

---

## 4. Audience Strategy

### Allocation Rule

- 70% broad targeting + Advantage+ (discovery/prospection)
- 30% custom audiences (retargeting)

### Custom Audiences (Sources)

| Source | Description |
|--------|-------------|
| Website (Pixel) | Visitors segmented by recency: 7, 14, 30, 180 days; specific pages (product, checkout); specific events (AddToCart, InitiateCheckout) |
| Customer lists | Upload emails/phones; Meta matches to Facebook/Instagram profiles |
| Platform engagement | People who interacted with content on Instagram/Facebook (video views, post engagement, form interaction) |
| App activity | Users who performed specific actions within the app |

### Lookalike Audiences

| Size | Use Case |
|------|----------|
| 1-2% | High-quality prospecting with conversion focus. Source: best customers (repeat buyers, high LTV) |
| 3-5% | Scale reach while maintaining reasonable relevance. Ideal for CBO campaigns needing volume |
| 6-10% | Very broad, nearly equivalent to broad targeting. Use only with high budgets when algorithm needs volume |

### Broad Targeting Rules

- Sweet spot audience size: 1-5 million people
- IF fewer than 50 conversions/week on pixel, THEN interest targeting may outperform broad
- IF daily budget > $50 (ideal $100+) AND pixel has 50+ weekly conversions, THEN use broad targeting
- Video engagement audiences achieve 3.2x higher CTR vs standard website visitor retargeting

### Targeting Decision Tree by Business Stage

```
IF new business starting on Meta:
  1. Start with Lookalike 1% based on best customers
  2. Test interest vs broad in separate ad sets (ABO)
  3. Migrate to broad/Advantage+ when pixel reaches 50+ weekly conversions

IF established business with robust history:
  1. Use Advantage+ Sales with broad targeting as primary campaign
  2. Maintain separate retargeting campaign with Custom Audiences (7-30 day visitors)
  3. Use exclusions to prevent overlap between campaigns

IF B2B or specific niche:
  1. Start with customer list + Lookalike 1%
  2. Combine with sector-specific interests
  3. Test progressive expansion to Lookalike 3-5%
```

---

## 5. Creative Strategy

### Importance

- Creative accounts for 56% of campaign results (exceeds budget and targeting combined)
- 70-80% of Meta ad performance depends on creative quality
- 98% of Meta users access via mobile -- ALL creatives MUST be mobile-first

### Format Priority (ordered)

1. Reels 7-15 seconds (highest engagement format; must feel native, not like ads)
2. Carousel with narrative sequence (3-5 cards; excellent for product demos and storytelling)
3. UGC (human or AI-generated; feels native, generates better algorithm signals)
4. Interview/testimonial video (structured, serious formats outperform casual trend-based storytelling)

### Aspect Ratio Priority (ordered)

| Ratio | Placement | Notes |
|-------|-----------|-------|
| 4:5 vertical | Feed Instagram/Facebook | +15% performance vs square |
| 9:16 | Stories, Reels, full-screen | Native format, highest engagement |
| 1:1 square | Feed, Marketplace | Versatile across all placements |
| 16:9 horizontal | In-stream video, right column | Lowest priority on mobile |

### Video Rules

#### 3-Second Hook Rule

- Andromeda evaluates the hook SEPARATELY from the rest of the video
- Hook Rate = primary predictor of future ad performance
- Target Hook Rate: 25%+

#### Hook Frameworks

- Provocative question that sparks curiosity
- Visual impact demonstrating the result
- Counterintuitive statement or surprising statistic
- "They told me [common objection]... but..."
- "I didn't think this would work... until I tried it"
- "POV: You've been doing it wrong this whole time"
- "Before you buy another one of these, watch this"

#### Duration

- Sweet spot: 7-15 seconds
- 30-60 seconds: ONLY for detailed testimonials in mid-funnel
- ALWAYS deliver the key message within the first 15 seconds

#### Sound-Off Design (Mandatory)

- ASSUME all viewers watch with sound off
- ALWAYS add captions/subtitles
- ALWAYS use text overlays
- ALWAYS ensure visual storytelling works without audio

### Static Images

- Static images often outperform video because they: communicate value instantly, load fast on slow connections, allow producing 10 variations in the time needed for one video
- Especially effective for: retargeting, visual products

### Copywriting Rules

#### Structure

| Element | Rule |
|---------|------|
| Headline | 5-8 words. Benefit-focused. Clear, direct, no jargon. |
| Primary text | First 125 characters visible before "see more"; up to 280 characters when content is compelling enough to justify expansion click |
| Description | 30 characters max. Reinforce offer or add urgency. |

#### Copy Formulas

- **Problem-solution:** State the problem, position product as solution
- **Curiosity gap:** "This simple trick helped me [result]"
- **Social proof:** "Over 10,000 five-star reviews"
- **Temporal urgency:** "Offer ends Friday"
- **Concrete data:** "30,000+ parents made the switch this year"

#### Copy Principles

- Talk about the RESULT, not the product
- Use specific numbers ("+37% in 14 days" beats "improve your results")
- Include social proof when possible ("Used by 50,000+ companies")
- ONE clear CTA per ad, mapped to objective:
  - "Shop Now" for e-commerce
  - "Learn More" for lead gen
  - "Sign Up" for apps/services
  - "Contact Us" for local businesses

### Visual Design Rules

- Single focal point performs better than cluttered designs
- High-contrast colors (vivid colors against dark backgrounds or vice versa) stop the scroll
- Consistent brand colors build recognition over time
- 9:16 safe zones: keep critical elements in the CENTER third of the screen (profile name at top, CTA at bottom will overlay)

### Creative Refresh and Diversity

- Refresh cadence: every 2-3 weeks
- IF frequency > 3.0 for cold audiences, THEN creative fatigue is occurring
- IF CPM is rising, THEN check for creative fatigue
- When a winner is found: replicate the WINNING MESSAGE in different formats (video, image, carousel, UGC) -- do NOT produce 20 identical iterations

### Creative Budget Allocation (70/20/10 Framework)

- 70% on proven formats that already perform
- 20% on tests of new concepts
- 10% on experimental (voiceovers, memes, trends)

### Production Planning

- Batch production: reserve 4 hours on one day per month to create 15-20 creative variations
- Plan 90 days ahead for seasonal needs (e.g., Black Friday creatives in September)

### Placement-Specific Guidelines

| Placement | Guideline |
|-----------|-----------|
| Instagram | Younger audience; expects higher visual quality |
| Facebook | Users more receptive to long copy and detailed explanations |
| Stories | Can be more static (text-based designs without movement work well) |
| Reels | MUST have movement and native content style |
| Messenger | Conversational copy, questions, clear invitations to start chat |

---

## 6. Budget and Bidding

### CBO (Advantage Campaign Budget)

#### When to Use

- Scaling campaigns with validated creatives
- 3-5 ad sets with non-overlapping audiences
- Weekly budget >= 50x CPA target (e.g., CPA target $20 = weekly minimum $1,000, ~$143/day)
- When maximizing total budget efficiency

#### Performance Data

- 17% ROAS increase vs ABO
- Up to 27% cost reduction vs ABO
- Target ROAS range for automated distribution: 2.5x-4.0x

#### CBO Configuration Checklist

- [ ] 3-5 ad sets with non-overlapping audiences (e.g., Lookalike 1%, broad targeting, retargeting)
- [ ] 3-5 creatives per ad set mixing formats (video, static, carousel, UGC)
- [ ] Let AI distribute budget; monitor for under-invested ad sets
- [ ] Set minimum spend floors for high-value smaller audiences (e.g., retargeting) that CBO might ignore
- [ ] Reuse Post IDs when refreshing creatives to maintain social proof (+15% CTR)

#### 72-Hour Rule (CRITICAL)

- MAKE NO CHANGES to budgets or ad sets for AT LEAST 72 hours (ideally 3-5 days) after launch
- This allows the algorithm to stabilize

#### Frequency Monitoring

- Healthy range: 1.5-3.0x
- IF frequency > 3.0, THEN creative fatigue is occurring -- refresh creatives

#### Kill Criteria

- PAUSE any ad set exceeding 20% above CPA target after reaching minimum spend threshold

### ABO (Ad Set Budget Optimization)

#### When to Use

- Testing new creatives (sandbox phase)
- When precise control over per-audience/per-creative spend is needed
- Initial data collection phase
- When few creatives exist and balanced investment is required

### Hybrid Approach (Recommended)

```
Phase 1 (ABO -- Validate):
  -> Start with ABO for precise data collection
  -> Give each creative/audience a fair budget
  -> Monitor results and isolate what works

Phase 2 (CBO -- Scale):
  -> Migrate validated winners to CBO campaign
  -> Automate and scale
```

### Bidding Strategy Decision Tree

```
DEFAULT: Use Lowest Cost (maximum flexibility for algorithm)

IF 50+ weekly conversions AND clearly defined CPA/ROAS target:
  -> Consider Cost Cap (set maximum acceptable CPA; may limit volume)
  -> OR ROAS Target (set minimum acceptable ROAS; requires conversion history)

IF need maximum bid control (rare):
  -> Bid Cap (set maximum bid per auction; risk of under-delivery)
```

### Budget Rules

#### Learning Phase Exit

- Minimum: 50 optimization events per week per ad set
- IF CPA is $20, THEN minimum weekly budget per ad set = $1,000

#### Scaling Rule

- NEVER increase budget more than 20% every 3-4 days
- Increases above 20% trigger partial learning phase reset
- Wait at least 48 hours before making another increase

---

## 7. Pixel + Conversions API (CAPI) Setup

### Why Both Are Required

- Browser-only Pixel misses ~50% of conversions due to iOS 14+ privacy restrictions, ad blockers (30%+ of users), cookie deprecation, and reduced attribution windows
- CAPI sends conversion events server-side directly to Meta, bypassing browser restrictions
- CAPI captures 20-40% more conversions than Pixel alone
- Any advertiser spending $1,000+/month on Meta ads MUST use both

### Essential Pixel Events

- [ ] PageView (automatic)
- [ ] ViewContent (product page)
- [ ] AddToCart
- [ ] InitiateCheckout
- [ ] Purchase (with value and currency)
- [ ] Lead (for lead generation)
- [ ] CompleteRegistration

### Event Deduplication (CRITICAL)

IF running Pixel + CAPI simultaneously (recommended), THEN deduplication is MANDATORY to prevent double-counting.

#### Deduplication Rules

- Send the SAME `event_id` (e.g., order_id) via both Pixel and CAPI
- `event_id` MUST be unique per event (not per session)
- `event_id` MUST be type string in JSON (e.g., `"event_id": "12345"`, NOT `"event_id": 12345`)
- `event_id` is case-sensitive -- "order_12345" must be identical between Pixel and CAPI
- Deduplication window: 48 hours between Pixel and CAPI versions of the same event
- VERIFICATION: In Events Manager, correctly deduplicated events show as "1 event from 2 sources". IF it shows "1 event from 1 source", deduplication is NOT working.
- Target: 90%+ of browser events should have corresponding server-side events

### Event Match Quality (EMQ)

#### EMQ Score Interpretation

| Score | Rating | Action |
|-------|--------|--------|
| 0-4 | Poor | Meta cannot reliably match events to users. FIX IMMEDIATELY. |
| 4-6 | Fair | Basic matching only, limited optimization. IMPROVE. |
| 6-8 | Good | Solid matching, effective optimization. MAINTAIN. |
| 8-10 | Excellent | Maximum matching, optimized delivery. IDEAL. |

- MINIMUM target: 6.0 (below this, significant money is being lost)
- IDEAL target: 7.0-8.0+

#### EMQ Parameter Impact

| Parameter | Impact | Notes |
|-----------|--------|-------|
| `em` (email, SHA256) | +4.0 points | Highest individual impact |
| `ph` (phone, SHA256, E.164 format) | +3.0 points | Second highest impact |
| `fn`/`ln` (name, SHA256) | Incremental | Supplementary |
| Address (`ct`, `st`, `zp`, `country`) | +1.5 points | Useful for partial matching |
| `fbp` (Facebook Browser cookie) | Moderate | Improves browser-server match |
| `fbc` (Facebook Click ID) | Moderate | Connects event to ad click |
| `client_ip_address` | Important | Often overlooked; significant impact |
| `client_user_agent` | Important | Significant matching improvement |

#### Critical Normalization Error

- Hashing "user@email.com " (with trailing space) vs "user@email.com" produces DIFFERENT hashes -- this is a top cause of low EMQ
- ALWAYS: trim whitespace, lowercase emails, remove non-numeric characters from phone numbers BEFORE hashing

### CAPI Integration Methods

| Method | Setup Time | Technical Skill | Monthly Cost | Signal Quality |
|--------|-----------|----------------|-------------|----------------|
| Partner (Shopify, WooCommerce) | 1-2 hours | None | $0 (included) | Medium |
| CAPI Gateway | 2-4 hours | Medium-High | $20-400+ | Medium |
| GTM Server-Side | 4-8 hours | Intermediate | $10-50 (hosting) | Medium |
| Direct API | 20-40 hours | Advanced | $0 (DIY) | Very High |
| No-Code platforms (CustomerLabs) | Hours | Low | Platform fee | Very High |

- WARNING: Do NOT confuse regular GTM (Web Container, free, browser-based) with GTM Server-Side (separate product, requires own hosting). Regular GTM alone does NOT work for CAPI.

### Implementation Priority

1. Enhanced Conversions
2. Consent Mode v2
3. Server-side tagging

### Gradual Implementation Plan

- Week 1-2: Configure CAPI for Purchase events only
- Week 3: Test that deduplication is working correctly
- Week 4+: Add other server-side events (Lead, AddToCart, etc.)
- Month 2: Monitor EMQ and optimize parameters

### Performance Impact

- Allow 30-60 days for the algorithm to utilize improved data
- Expected ROAS improvement: 10-25% vs Pixel-only tracking

### Agency Multi-Account Rules

- Use System User Tokens (NOT personal accounts -- tokens don't break when team members leave)
- Standardize event names across accounts
- Monitor EMQ weekly
- Set 85-day reminder for token rotation (tokens expire in 90 days)

### Ongoing Maintenance

- CAPI is NOT "set and forget"
- API endpoints change, event parameters get updated, silent failures can go undetected for weeks
- Implement retry logic and error handling
- Monitor continuously

---

## 8. Retargeting and Remarketing

### Retargeting Windows by Intent Level

| Window | Audience | Creative Type | Intent |
|--------|----------|---------------|--------|
| 1-3 days | Cart abandoners | Direct offer, urgency | Very high |
| 3-7 days | Product page visitors | Social proof, benefits | High |
| 7-14 days | Site visitors | Educational, testimonials | Medium |
| 14-30 days | Ad engagers | Brand awareness | Low-medium |
| 30-180 days | Video viewers, page engagers | Brand re-introduction | Low |

### Dynamic Retargeting Setup

- [ ] Product catalog configured in Commerce Manager
- [ ] Pixel with ViewContent, AddToCart, and Purchase events correctly configured
- [ ] Dynamic ad template with price, image, and product name
- [ ] Exclude recent buyers (7-14 days)

### Holdout Testing

- IF running retargeting, THEN periodically run holdout tests
- Create a control group deliberately NOT exposed to ads
- Compare conversion rate of exposed vs unexposed groups
- IF difference is marginal, THEN reallocate budget to prospecting

### Essential Exclusions Checklist

- [ ] Exclude recent buyers (7-30 days, depending on purchase cycle)
- [ ] Exclude audiences between campaigns to prevent overlap
- [ ] Exclude already-converted leads from lead generation campaigns
- [ ] Exclude visitors to irrelevant pages (e.g., careers page, terms of service)

---

## 9. A/B Testing

### Hierarchy of What to Test (ordered by impact)

1. **Creative (image/video)** -- highest impact; test completely different concepts before iterating
2. **Offer / value proposition** -- what you are offering (discount, free shipping, trial)
3. **Copy (headline + primary text)** -- message angle, tone, length
4. **Audience** -- broad vs Lookalike vs specific interest
5. **Format** -- video vs image vs carousel
6. **Placement** -- automatic vs manual
7. **Landing page** -- layout, CTA, form

### Testing Rules

- ALWAYS test only ONE variable at a time; keep all other elements constant
- NEVER end a test before 7 days (weekday vs weekend variation creates false winners)
- NEVER run a test longer than 30 days
- ALWAYS require 95% statistical significance before declaring a winner
- ALWAYS require at least 20% improvement in primary KPI before scaling
- Use Meta's native A/B Test (Experiments) feature for clean audience split without overlap
- Set equal budget for both variants
- Minimum audience size: 1M+ to avoid overlap

### Budget Formula

`CPA average x Number of variants x Sample size (min 100 conversions) = Base budget`

Example: $5 CPC x 2 variants x 100 conversions = $1,000

### Test Budget by Company Stage

| Stage | Test Budget Share | Monthly Range |
|-------|------------------|---------------|
| Beginner | 30% of total budget | $300-1,500/month |
| Growth | 25% of total budget | $1,250-6,250/month |
| Scale | 20% of total budget | $5,000+/month |

Each variant needs budget sufficient to reach ~50 optimization events and exit learning phase.

### Monitoring Cadence

- Day 1: Check for obvious failures
- Day 3: Observe initial trends
- Day 7: Evaluate statistical significance
- Day 14: Make final scaling decision

### Testing Pitfalls to Avoid

- **Simpson's Paradox:** Overall results can mask differences in specific segments. ALWAYS break results by demographics or devices.
- **Divergent Delivery:** Meta's algorithms may send different ads to different user mixes, making the "winner" appear better simply because it was shown to more responsive users.
- **Multiple Variables:** Testing more than one variable simultaneously contaminates results.

---

## 10. Scaling

### Vertical Scaling (increase budget on performing campaigns)

#### Prerequisites

- Campaign has stable CPA for 5-7 consecutive days
- Campaign has exited learning phase
- There is room to gain impressions without significant frequency increase

#### Rules

- Increase budget by MAXIMUM 20% every 3-4 days
- Wait at least 48 hours before another increase
- Increases above 20% trigger partial algorithm relearning
- Wait at least 5-7 days of consistent data before deciding to scale

#### Breakdown Effect Warning

- NEVER judge ads solely by individual ad conversion volume or isolated CPA
- Meta strategically shifts investment toward ads with highest scaling potential
- Pausing the highest-spend ad (high CPA but high investment) can collapse entire account performance
- ALWAYS evaluate performance at the CAMPAIGN level, not individual ad level

#### When a Campaign Peaks

- Do NOT force more budget
- Clone the structure, reset learning, and scale from a clean base

### Horizontal Scaling (expand reach via new ad sets/audiences)

- Expand audiences: larger Lookalikes (3-5%), related interest groups, demographic adjustments
- Test new creatives: rotate formats (video, carousel, UGC) for fresh engagement
- Diversify placements: use Advantage+ Placements to optimize across Feed, Stories, Reels, Audience Network
- New markets: test adjacent geographic regions
- Budget for duplicates: assign 50-70% of original budget to new duplicates

### Efficiency Ceiling Signals

IF any of the following occur, STOP vertical scaling:
- CPA grows faster than budget increase
- Frequency rises above 3-4 for cold audiences
- Delivery becomes inconsistent despite adequate budget
- Marginal ROAS drops significantly with each increase

THEN: focus on horizontal scaling or accept the campaign is at maximum efficiency.

### Scaling Decision Tree

```
Campaign performing well for 5-7 days?
  |
  YES -> CPA below target?
  |       |
  |       YES -> Frequency < 3?
  |       |       |
  |       |       YES -> VERTICAL SCALING (increase 20%)
  |       |       NO  -> HORIZONTAL SCALING (new audience)
  |       |
  |       NO -> Review creatives and audiences
  |
  NO -> Wait for more data or adjust campaign
```

---

## 11. KPIs and Benchmarks

### Metrics by Funnel Stage

| Stage | Primary Metrics |
|-------|----------------|
| TOF (Awareness) | CPM, Reach, Frequency, Hook Rate, ThruPlay Rate |
| MOF (Consideration) | CTR, CPC, Engagement Rate |
| BOF (Conversion) | ROAS, CPA, CVR, AOV |

### Global Benchmarks 2025

| Metric | Global Average | Median |
|--------|---------------|--------|
| CTR | 0.90% | 2.19% |
| CPC | $1.72 | - |
| CVR | 9.21% | 1.57% |
| CPA | $18.68 | $38.17 |
| CPM | - | $13.48 |
| ROAS | 2.19:1 | 1.93:1 |

- CPM increased 20.03% in 2025 (higher competition)
- Most brands target 2-3x ROAS as a healthy goal

### Industry Benchmarks 2025

| Industry | ROAS | CTR | CVR | CPA |
|-----------|------|-----|-----|-----|
| Automotive | 2.54 | - | - | - |
| Beauty | 3.00+ | - | 7.10% | $25.49 |
| Sports/Outdoor | 2.28 | - | - | - |
| Travel/Accessories | 2.25 | - | - | - |
| Legal | - | 1.61% | - | - |
| Retail | - | 1.59% | - | - |
| Apparel | - | 1.24% | - | - |
| Fitness | - | - | 14.29% | - |
| Education | - | - | 13.58% | - |
| Media/Publishing | 1.17 | - | - | - |

### Campaign Type Benchmarks

- Lead Generation campaigns: 2.59% CTR (61% higher than Traffic campaigns)
- Traffic campaigns: most cost-effective at $0.70 CPC

### Metric Interpretation Rules

- ROAS is NOT profit. A 3.0 ROAS means $3 revenue per $1 ad spend, but does not account for COGS, operations, taxes, margin. For most e-commerce, break-even ROAS is 1.5-2.5x.
- ALWAYS compare CPA to LTV. A $50 CPA is excellent if LTV is $500 and terrible if LTV is $60.
- IF CTR is high but conversion rate is low, THEN there is a disconnect between the ad and the landing page.

---

## 12. Common Errors Checklist

### Structure Errors

- [ ] DO NOT create dozens of campaigns with small budgets. Consolidate into 2-4 campaigns with significant budget.
- [ ] DO NOT run conversion-only campaigns to cold audiences. Invest in awareness first.
- [ ] DO NOT let multiple ad sets compete for the same audience. Use exclusions and distinct audiences.

### Creative Errors

- [ ] DO NOT run similar creatives. Andromeda penalizes with higher CPMs.
- [ ] DO NOT ignore UGC. UGC (human or AI-generated) looks native and generates better engagement.
- [ ] DO NOT keep the same creatives for months. Refresh every 2-3 weeks.

### Budget Errors

- [ ] DO NOT under-invest below learning phase threshold (~50 events/week/ad set). Calculate minimum before launching.
- [ ] DO NOT double budget at once. Use the 20% every 3-4 days rule.

### Technical Errors

- [ ] DO NOT rely on Pixel only. Missing 30-50% of conversions feeds the algorithm incomplete data.
- [ ] DO NOT run Pixel + CAPI without deduplication. Inflated numbers distort optimization.
- [ ] DO NOT optimize for the wrong event (e.g., PageView instead of Purchase). This trains the algorithm to bring the wrong type of user.

### Testing Errors

- [ ] DO NOT end tests before 7 days.
- [ ] DO NOT test multiple variables simultaneously.
- [ ] DO NOT declare a winner without 95% statistical confidence.

---

## 13. Industry Budget Allocation Templates

### Fashion/Apparel

- 40% Broad/Advantage+ (prospecting)
- 30% Lookalikes (1-2% of buyers)
- 20% Website retargeting
- 10% Customer retention
- Creative refresh: every 2-3 weeks

### Health/Wellness

- 50% Educational content + broad
- 25% Health interests (broad within niche)
- 15% High-LTV Lookalikes
- 10% Retargeting with testimonials

### Home/Decor

- 35% Homeowner demographic + broad
- 25% Seasonal interests
- 25% Website retargeting
- 15% Customer upsell

### Electronics/Gadgets

- 30% Tech interest + broad
- 30% Early adopter Lookalikes
- 25% Comparison retargeting
- 15% Accessory upsell

### Partnership Ads

- Partnership Ads outperform traditional brand-page ads (higher CTR, lower CPA) because they leverage the creator's page learnings and established audience
- Quick start: test using the founder's personal Instagram profile
- IF founder does not want to be the brand face, THEN invest in partner creators via Meta's partnership program

### LTV Over ROAS Framework

- DO NOT obsess over short-term CPM/CPC -- this is a path to failure
- Focus on Customer Lifetime Value (LTV) and Average Order Value (AOV)
- Higher AOV enables higher CAC, allowing more aggressive scaling even with rising CPMs
- A $5 increase in AOV can significantly improve ROAS (one case study showed 15% AOV increase in the first month)
- Strategies to increase LTV/AOV: product bundles, free shipping thresholds, email marketing for retention, segmenting one-time vs repeat buyers (one supplement brand increased LTV by 67% by separating these segments)

---

## 14. Implementation Checklist

### Phase 1: Foundation (Week 1)

- [ ] Install Meta Pixel on all site pages
- [ ] Configure Conversions API (CAPI) with deduplication
- [ ] Verify Event Match Quality (EMQ) > 6.0
- [ ] Configure essential events: PageView, ViewContent, AddToCart, InitiateCheckout, Purchase, Lead
- [ ] Configure verified domain in Business Manager
- [ ] Create Product Catalog (if e-commerce)
- [ ] Set up Business Manager, Ad Account, and connected pages

### Phase 2: Strategy (Week 2)

- [ ] Define business objectives and target KPIs (ROAS, CPA, CPL)
- [ ] Map complete funnel (TOF, MOF, BOF)
- [ ] Define budget distribution by funnel stage
- [ ] Create custom audiences (website, customer list, engagement)
- [ ] Create Lookalike Audiences 1% and 3% based on best customers
- [ ] Plan creative matrix (angles x formats)
- [ ] Define content calendar and creative refresh schedule

### Phase 3: Creative Production (Week 2-3)

- [ ] Produce 10-20 diverse creatives (video, image, carousel, UGC)
- [ ] Ensure 4:5 (feed) and 9:16 (Stories/Reels) formats
- [ ] Create copy variations (3+ headlines, 3+ primary texts)
- [ ] Add captions to all videos
- [ ] Verify safe zones for Stories/Reels
- [ ] Prepare funnel-stage-specific creatives

### Phase 4: Launch (Week 3)

- [ ] Create Campaign 1: Creative Test (ABO, $20-50/day per ad set)
- [ ] Configure 3-5 ad sets with different creatives
- [ ] Launch and wait through learning phase (3-7 days)
- [ ] MAKE NO CHANGES during learning phase
- [ ] Monitor metrics daily but DO NOT act prematurely

### Phase 5: Optimization (Week 4+)

- [ ] Identify winning creatives (CPA below target for 5-7 days)
- [ ] Create Campaign 2: Scale (CBO or Advantage+ Sales)
- [ ] Migrate winners to scale campaign with broad targeting
- [ ] Configure retargeting campaigns with temporal windows
- [ ] Begin structured A/B tests (one variable at a time)
- [ ] Scale vertically (20% every 3-4 days)
- [ ] Refresh creatives every 2-3 weeks
- [ ] Monitor frequency, fatigue, and ceiling signals
