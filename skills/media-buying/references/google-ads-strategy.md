# Google Ads Strategy Reference

## 1. Account Structure Decision Tree

WHEN defining account structure:
  - ALWAYS separate Brand vs Non-Brand campaigns
  - USE naming convention: `[Type]-[Product]-[Region]-[Match]` (e.g., `Search-OnlineCourses-BR-Exact`)
  - LIMIT to 7-10 ad groups per campaign; IF more needed, create additional campaign
  - KEEP 10-20 related keywords per ad group around a central theme
  - ENSURE each ad group has at least 1 RSA with Ad Strength "Good" or "Excellent"
  - PREFER simpler, consolidated structures when using Smart Bidding (more data for the algorithm)

WHEN monthly budget < $5,000:
  - USE 1-2 campaigns (Brand + main Non-Brand)
  - USE 3-5 ad groups per campaign
  - FOCUS exclusively on high-intent keywords

WHEN monthly budget $5,000-$50,000:
  - USE 4-8 campaigns (Brand, Non-Brand, Shopping, Performance Max, Remarketing)
  - USE 5-7 ad groups per campaign
  - SEGMENT by product/service category

WHEN monthly budget > $50,000:
  - USE 8-15+ campaigns with granular segmentation
  - SEPARATE campaigns by region, device, or audience
  - IMPLEMENT portfolio bidding strategies

---

## 2. Campaign Type Selection Matrix

### Objective-to-Campaign Mapping

| Business Objective | Primary Metric | Recommended Campaign Type |
|---|---|---|
| Online sales | ROAS, Revenue, Conversions | Search, Shopping, Performance Max |
| Qualified leads | CPA, Lead volume, Conversion rate | Search, Demand Gen |
| Brand awareness | Impressions, Reach, CPM | Display, Video, Demand Gen |
| Website traffic | CPC, CTR, Sessions | Search, Display |
| App promotion | Installs, CPI, In-app engagement | App Campaigns |

### Funnel Stage Rules

WHEN targeting Top of Funnel (Awareness):
  - USE Display, Video, and Demand Gen campaigns
  - TARGET cold audiences

WHEN targeting Mid Funnel (Consideration):
  - USE Search with informational keywords
  - USE Demand Gen with custom audiences

WHEN targeting Bottom of Funnel (Conversion):
  - USE Search with high purchase-intent keywords
  - USE Shopping and Performance Max

WHEN targeting Post-Conversion (Retention):
  - USE Remarketing and Customer Match
  - FOCUS on upsell and cross-sell

### Campaign-Specific Rules

#### Search Campaigns
- USE RSAs with all 15 headlines and 4 descriptions
- ORGANIZE ad groups by tight themes
- IMPLEMENT negative keywords from day 1
- ADD all relevant ad extensions (sitelinks, callouts, structured snippets, call)

#### Shopping Campaigns
- OPTIMIZE product titles first (most important feed factor)
- ADD GTINs whenever possible (correct GTINs yield +20% clicks on average)
- USE Custom Labels to segment by margin, seasonality, and performance
- KEEP product data updated and high quality in Merchant Center
- SUBDIVIDE product groups by: Category > Brand > Item ID

#### Performance Max (PMax)
- RUN for minimum 6 weeks before evaluating (ML learning period)
- PROVIDE audience signals: remarketing lists, Custom Intent, Customer Match, similar segments
- SUPPLY at least 20 diverse images, 6 videos, and 15 strategic headlines
- CONSOLIDATE PMax campaigns to maximize data for the algorithm
- SET initial daily budget at $50-$100 for testing
- DEFINE clear conversion goals with assigned values
- ADD up to 10,000 negative keywords per campaign for Search and Shopping
- USE up to 50 search themes per asset group
- MONITOR for brand cannibalization; exclude brand terms via scripts or brand exclusions
- EXPECT: PMax drives ~45% of conversions in Google Ads accounts; Customer Match signals reduce CPA by 30% in first 4 weeks; well-optimized PMax sees 20-35% ROAS improvement vs traditional structures

#### Demand Gen
- ADOPT at least 3 of 4 fundamental practices (yields 40%+ additional conversions):
  1. Audiences: optimized targeting, Lookalikes, new customer acquisition goals
  2. Bid & Budget: tCPA or tROAS with adequate budgets
  3. Creative: Ad Strength "Excellent" with comprehensive high-quality assets
  4. Data Strength: sitewide tagging with Google Tag Gateway + offline sources via Data Manager
- WAIT minimum 2 weeks or 50 conversions before making changes
- USE Creator Partnerships for Shorts (30% more conversion lift on average)

#### Display Campaigns
- USE Responsive Display Ads with multiple image, headline, and description variations
- TARGET by audiences (in-market, affinity, custom segments), NOT just topics/placements
- EXCLUDE low-quality placements and apps/games (consume budget without converting)
- COMBINE with remarketing for site visitor re-engagement

#### Video Campaigns (YouTube)
- In-stream skippable: user can skip after 5s
- In-stream non-skippable: 15 seconds, 100% view guaranteed
- Bumper ads: 6 seconds, reinforcement messaging
- In-feed: appear in YouTube search results

---

## 3. Bidding Strategy Progression

### Decision Tree by Conversion Volume

WHEN conversions/month < 15:
  - USE Manual CPC
  - DO NOT activate Smart Bidding

WHEN conversions/month 15-30:
  - SWITCH to Maximize Conversions

WHEN conversions/month 30-50:
  - SWITCH to Target CPA or Target ROAS

WHEN conversions/month 50-100:
  - USE Broad Match + Smart Bidding (official Google recommendation)
  - IF using conversion values: Maximize Conversion Value requires 50-60 conversions/30 days
  - IF below that threshold: stay on Maximize Conversions

WHEN conversions/month 100+:
  - IMPLEMENT Portfolio Bid Strategies across related campaigns
  - SET maximum CPC ceiling to prevent spikes
  - CONSIDER switching from Target CPA to Target ROAS (yields ~14% more conversion value at same ROAS)

### Bidding Strategy Reference Table

| Strategy | Type | Requirement | Use When |
|---|---|---|---|
| Manual CPC | Manual | None | New accounts, budget < $400/mo, < 15 conversions/mo |
| Enhanced CPC | Semi-auto | Conversion tracking | Transitioning from manual to automated |
| Maximize Clicks | Automated | None | Traffic objective, testing phase |
| Maximize Conversions | Smart Bidding | 15+ conversions/mo | Maximize conversion volume |
| Target CPA | Smart Bidding | 30+ conversions/mo | Control cost per acquisition |
| Maximize Conversion Value | Smart Bidding | 50-60 conversions/30 days + values | Maximize total revenue |
| Target ROAS | Smart Bidding | 30+ conversions/mo + values | Control return on ad spend |

### Critical Bidding Rules

- NEVER change budget or bid strategy abruptly; increase gradually by 15-20% at a time
- AFTER significant changes, WAIT 1-2 weeks (or one full conversion cycle) for algorithm to restabilize
- USE Broad Match + Smart Bidding ONLY with 50+ monthly conversions
- WHEN using Broad Match with Maximize Conversions: expect volume over quality; for better control, pair Broad Match with Target CPA or Target ROAS
- CONSIDER Smart Bidding Exploration to flex target ROAS within acceptable range (yields 18% more unique query categories with conversions and 19% more total conversions)

### Value-Based Bidding

- USE Conversion Value Rules to define different values based on audience, device, or location
- WHEN available, feed Smart Bidding with predicted Lifetime Value (LTV) instead of point-of-sale conversion value
- VALIDATE category-level LTV; high AOV does not always mean high LTV

---

## 4. Quality Score Optimization Playbook

### Quality Score Components Checklist

Quality Score (1-10) has three components. For each, target "Above Average":

**1. Expected CTR**
  - [ ] Organize keywords into tight thematic ad groups with dedicated ads
  - [ ] Test ad copy variations continuously to improve CTR
  - [ ] Use specific CTAs ("Request Free Quote" outperforms "Learn More")

**2. Ad Relevance**
  - [ ] Match headline copy to the search intent of the ad group's keywords
  - [ ] Use negative keywords to ensure ads show only for relevant searches
  - [ ] Keep each ad group focused on a single theme

**3. Landing Page Experience**
  - [ ] Page loads in < 3 seconds
  - [ ] Core Web Vitals: LCP < 2.5s, INP < 200ms, CLS < 0.1
  - [ ] Page is mobile-friendly (60%+ of search traffic is mobile)
  - [ ] Buttons and CTAs are at least 48x48 pixels
  - [ ] Content directly matches the ad's promise and search intent
  - [ ] No intrusive pop-ups on mobile

### Quality Score Impact on CPC

| Quality Score | CPC Impact |
|---|---|
| 1-3 | CPC increases up to 400% |
| 5 (average) | Baseline |
| 8 | CPC decreases ~30% |
| 8-10 | CPC decreases up to 50% |
| "Above average" in both LP experience AND ad relevance | CPC 36% below average |

### Rules
- TARGET Quality Score 7+ for core keywords
- IMPROVING from "Poor" to "Excellent" Ad Strength yields ~12% more conversions
- DO NOT obsess over Quality Score as a primary metric; use it as a diagnostic tool
- E-commerce sites meeting all Core Web Vitals see 15-30% conversion improvement (only 47% of sites meet these in 2026)

---

## 5. Budget Allocation Framework

### 70/20/10 Rule

| Allocation | % of Budget | Criteria |
|---|---|---|
| Proven campaigns | 70% | Consistent ROI history and stable conversions |
| Growth campaigns | 20% | New campaigns with promising signals, in optimization phase |
| Testing | 10% | New campaign types, experimental keywords, untested audiences |

### Allocation by Campaign Type

| Campaign Type | % Budget | Rationale |
|---|---|---|
| Search (Non-Brand) | 30-40% | Direct demand, high intent |
| Search (Brand) | 5-10% | Brand protection, low CPA |
| Shopping / PMax | 25-35% | E-commerce, direct product |
| Remarketing | 10-15% | High ROI, warm audience |
| Demand Gen / Display | 10-20% | Top of funnel, awareness |

### Match Type Budget Split

- Discovery campaigns (Broad Match): 15-20% of budget (radar for new opportunities)
- Performance campaigns (Phrase + Exact Match): 80-85% of budget (higher bids, conversion-optimized)

### Budget Optimization Rules

- REALLOCATE from underperformers to top performers: pull performance report, sort by CPA or ROAS, shift budget from expensive to efficient campaigns
- IF conversion data shows certain hours convert 2x more: increase bids during those periods, reduce during low-performance periods (dayparting)
- USE Seasonality Bid Adjustments for predictable events (Black Friday, holidays, etc.)
- USE Shared Budgets for campaigns competing for the same audience
- WHEN budget < $2,000/month: start with Phrase Match, promote winners to Exact Match; do NOT use Broad Match
- WHEN budget > $2,000/month with 30-50+ conversions: introduce Broad Match + Smart Bidding

---

## 6. Privacy/Compliance Setup Checklist

### Implementation Priority Order
1. Enhanced Conversions (highest ROI)
2. Consent Mode v2
3. Server-side tagging

### Consent Mode v2

- [ ] Implement via a compliant CMP (Consent Management Platform)
- [ ] DEFAULT all 4 parameters to 'denied':
  - `ad_storage` (advertising cookies)
  - `analytics_storage` (analytics cookies)
  - `ad_user_data` (user data for advertising)
  - `ad_personalization` (ad personalization)
- [ ] UPDATE parameters ONLY after explicit user action
- [ ] USE Advanced mode (recommended): allows Google tags to load in cookieless mode when users reject, sending anonymous pings
  - Advanced mode enables conversion modeling that recovers 30-50% of lost conversions
  - Basic mode blocks all tags until consent, resulting in ~69% data loss
- [ ] VERIFY minimum requirements for conversion modeling:
  - 700+ ad clicks per 7 days per country
  - 7 days of historical data
  - Consent rate > 20%
- [ ] NOTE: 67% of implementations fail to meet full compliance standards; verify thoroughly

IF operating in EEA: Consent Mode v2 is MANDATORY (since March 2024)

IF Remarketing or Customer Match is needed: ad_user_data consent is REQUIRED

### Enhanced Conversions

- [ ] Implement via Google Tag Manager (preferred) or API
- [ ] Collect data compliantly (user consent required)
- [ ] Monitor via Google Ads Diagnostics tab after 72 hours
- [ ] Verify: healthy implementation shows 50%+ of conversions as enhanced
- [ ] EXPECT 5-15% increase in reported conversions
- [ ] With server-side tagging: recovers 20-30% of lost conversions

CRITICAL: NEVER track the same conversion simultaneously in GA4 AND native Google Ads -- this causes double counting. Choose one primary source; set the other as "Secondary".

### Customer Match & Data Manager

- [ ] Upload first-party data (email, phone, address) for audience creation and lookalikes
- [ ] EXPECT 5.3% conversion uplift when list signals are applied to campaigns
- [ ] EXPECT match rates of 29-62% depending on data quality
- [ ] MIGRATE all Customer Match uploads to Data Manager API (Google Ads API uploads disabled April 1, 2026)
- [ ] SET refresh cycles: Customer Match lists have maximum duration of 540 days (since April 2025)

### Server-Side Tagging

- [ ] Implement via Google Tag Gateway
- [ ] Prioritize AFTER Enhanced Conversions and Consent Mode v2

### Confidential Matching
- Google uses Trusted Execution Environments (TEEs) to process first-party data securely
- Enables matching without raw data exposure

---

## 7. Ad Creation Rules

### Responsive Search Ads (RSAs)

ALWAYS provide:
- **15 headlines** (maximum allowed)
- **4 descriptions** (maximum allowed)

Headline Rules:
- VARY headline length (short and long resonate with different users)
- FOCUS on user benefits, not product features
- USE specific CTAs ("Request Free Quote" > "Learn More")
- MATCH copy to the keyword intent of the ad group

Pinning Strategy:
- PIN sparingly (e.g., brand name in Headline 1)
- DO NOT over-pin; excessive pins limit Google's optimization ability

Ad Strength:
- TARGET "Good" or "Excellent"
- Improving from "Poor" to "Excellent" yields ~12% more conversions on average

### Ad Extensions (Assets) Priority

| Extension | Priority | When to Use |
|---|---|---|
| Sitelinks | HIGH -- always use | All campaigns |
| Callouts | HIGH | All campaigns (e.g., "Free Shipping", "24h Support") |
| Call Extensions | HIGH | Local businesses |
| Location Extensions | HIGH | Physical stores |
| Lead Form Extensions | HIGH | Lead generation |
| Price Extensions | MEDIUM-HIGH | Products/services with listed prices |
| Image Extensions | MEDIUM-HIGH | All campaigns |
| Structured Snippets | MEDIUM | Category/service lists |
| Promotion Extensions | SEASONAL | Sales and specific discounts |

### Creatives for Display and Demand Gen

- PROVIDE maximum variations of images in different aspect ratios (1:1, 1.91:1, 4:5)
- INCLUDE videos (especially for Demand Gen; Creator Partnerships yield 30% more conversion lift)
- ALLOW 3-4 weeks for performance to stabilize before optimizing creatives
- TEST different messages: main benefit, social proof, urgency, comparison

---

## 8. Audience/Remarketing Setup Guide

### Audience Segment Types

| Segment | Use Case | Funnel Position |
|---|---|---|
| Remarketing | Re-engage site/app visitors | Bottom of funnel |
| Customer Match | Upsell, lookalikes, exclusions | All funnel stages |
| In-Market | Users actively researching category | Mid/bottom of funnel |
| Affinity | Users with declared interests | Top of funnel |
| Custom Segments | Combine keywords, URLs, and apps | Refined prospecting |
| Lookalike/Similar | Expand from best customers | Prospecting |

### Remarketing Segmentation Rules

WHEN visitor is general site visitor:
  - USE awareness messaging
  - SET membership window: 30-90 days

WHEN visitor viewed product page:
  - USE product-specific messaging
  - SET membership window: 14-30 days

WHEN visitor abandoned cart:
  - USE incentive offer (discount, free shipping)
  - SET membership window: 7-14 days

WHEN visitor is a past buyer:
  - USE upsell/cross-sell messaging
  - SET membership window: 30-180 days

### Membership Duration by Sale Cycle

| Product Type | Membership Duration |
|---|---|
| Impulse purchase | 7-14 days |
| Medium consideration services | 30-60 days |
| High-value products / B2B | 90-180 days |

### Audience Layering Rules

- COMBINE In-Market + Demographics for interest AND profile targeting
- COMBINE Affinity + Remarketing for visitors who also have category affinity

### Exclusion Rules

ALWAYS exclude:
  - Users who already converted (avoid re-spending on existing customers)
  - Quick bounces (visited < 10 seconds)
  - Company employees

---

## 9. Industry Benchmarks

### Search Benchmarks by Industry (2025)

| Industry | CTR | CPC (USD) | CVR | CPL (USD) |
|---|---|---|---|---|
| **Overall Average** | **6.66%** | **$5.26** | **7.52%** | **$70.11** |
| Arts & Entertainment | 13.10% | $1.60 | 8.41% | $19.03 |
| Automotive Repair | 6.90% | $3.84 | 14.67% | $28.50 |
| Education | 6.41% | $5.71 | 11.38% | $50.18 |
| Finance & Insurance | 8.33% | $3.46 | 2.55% | $83.93 |
| Health & Fitness | 7.18% | $5.00 | 6.80% | $73.53 |
| Home Improvement | 6.37% | $7.85 | 7.33% | $107.10 |
| Attorneys & Legal | 5.97% | $8.58 | 5.09% | $131.63 |
| Real Estate | 8.43% | $2.53 | 3.28% | $100.48 |
| Restaurants & Food | 7.58% | $2.05 | 7.09% | $28.91 |
| Travel | 8.73% | $2.12 | 5.75% | $36.87 |

KEY TREND: CTR rose across all 14 industries, but CVR dropped in 13 of 14 industries (-9.28% overall). Landing page optimization is the highest-leverage area.

### General Benchmark Targets

| Metric | Benchmark |
|---|---|
| Search CTR | 3-5% |
| Display CTR | 0.5-1% |
| Search Conversion Rate | 3-5% |
| Display Conversion Rate | 0.5-1% |
| Brand Impression Share | > 90% |
| Non-Brand Impression Share | > 60% |
| Quality Score (core keywords) | 7+ |

### ROAS Benchmarks

| Context | ROAS Benchmark |
|---|---|
| Overall Google Ads average | 2:1 (200%) |
| Google Search Network | 8:1 |
| "Good" target | > 3:1 |
| DTC / E-commerce target | 3:1 to 5:1 |
| B2B SaaS | ~1.55:1 |
| Strong performance | 5:1 |
| Exceptional performance | > 10:1 |

Break-even ROAS formula: `BER = 1 / Gross Margin`
- Example: 40% margin = break-even ROAS of 2.5x

### KPIs by Campaign Type

| Campaign Type | Primary KPIs |
|---|---|
| Search | CTR, CPC, Conversion Rate, CPA, ROAS, Impression Share |
| Shopping | ROAS, CPC, Conversion Rate, Impression Share, Benchmark CTR vs competitors |
| Performance Max | Total conversions, Conversion Value, ROAS, CPA, Asset Group performance |
| Demand Gen | Conversions, CPA, CTR, View Rate (video), CPM, Conversion Lift |
| Display | Impressions, Reach, Frequency, CTR, View-Through Conversions, CPM |
| Video/YouTube | View Rate, CPV (Cost Per View), Watch Time, Brand Lift, Conversion Lift |

### Reporting Layers

- Executives: ROAS, CPA, total conversions, budget utilized
- Campaign managers: CTR, Quality Score, Impression Share, Search Terms
- Monthly reviews: YoY trends, device splits, geographic breakdowns
- USE Looker Studio with native Google Ads connector

---

## 10. Keyword Strategy Rules

### Match Type Selection

WHEN budget < $2,000/month:
  - USE Phrase Match primarily
  - PROMOTE winners to Exact Match
  - DO NOT use Broad Match

WHEN budget $2,000-$10,000/month with < 30 conversions:
  - USE Phrase Match + selective Exact Match
  - DO NOT use Broad Match

WHEN 30-50+ conversions/month:
  - INTRODUCE Broad Match + Smart Bidding
  - MAINTAIN Phrase and Exact for proven performers

TREND: Phrase Match expected to be deprecated; prepare for Exact + Broad only.

### Match Type Reference

| Match Type | Syntax | Behavior | When to Use |
|---|---|---|---|
| Exact Match | [keyword] | Same meaning or same intent | Proven high-performance keywords |
| Phrase Match | "keyword" | Keyword meaning + word order | Balance between control and reach |
| Broad Match | keyword | Related intent (broadest) | With Smart Bidding and 50+ conversions/mo |

### Negative Keywords Architecture

1. **Master Negative List:** Universal irrelevant terms (e.g., "free", "jobs", "how to") -- apply to ALL campaigns
2. **Campaign-level lists:** Thematic negatives (e.g., separate brand from non-brand)
3. **Ad group-level negatives:** Surgical exclusions for tight themes

Limits: Up to 5,000 negatives per list, up to 20 lists per account.

### Negative Keyword Maintenance

- BUILD negative lists BEFORE activating campaigns (proactive, not reactive)
- REVIEW Search Terms Report WEEKLY (biweekly for smaller accounts)
- SORT by spend, FILTER by zero conversions
- ADD irrelevant terms immediately

---

## 11. Conversion Tracking Setup

### Implementation Steps

1. Define conversion actions (purchases, leads, calls, etc.)
2. Install Global Site Tag (gtag.js) or Google Tag Manager
3. Configure Event Snippets for each conversion action
4. Assign conversion values (fixed or dynamic)
5. Configure Enhanced Conversions for improved accuracy
6. Link Google Analytics 4

### Attribution Model Rules

ONLY two attribution models remain (2026):

| Model | Use When |
|---|---|
| Data-Driven Attribution (DDA) | DEFAULT -- use for most accounts |
| Last Click | Accounts with very few data points or simplified analysis |

### Conversion Window Rules

| Business Type | Click-Through Window | View-Through Window |
|---|---|---|
| E-commerce (impulse) | 7-14 days | 1 day |
| Services / B2B | 30-90 days | 7 days |
| Real estate / Automotive | 60-90 days | -- |

---

## 12. Optimization Cadence

### Routine Schedule

| Frequency | Actions |
|---|---|
| Daily | Check budget (campaigns limited?), alerts, spend anomalies |
| Weekly | Search Terms Report + add negatives, review ad group performance, adjust manual bids |
| Biweekly | Analyze ad performance, pause underperformers, test new ads |
| Monthly | Review campaign structure, analyze audiences, reallocate budget, report KPIs, audit settings |
| Quarterly | Strategic review, evaluate new campaign types, seasonality, competitiveness |

### A/B Testing Rules

- TEST only one variable at a time
- WAIT at least 4 weeks and sufficient conversions
- WAIT for learning phase to end before concluding
- REQUIRE consistent performance over several consecutive days

### Testing Priority (highest to lowest impact)

1. Bid strategy
2. Landing pages
3. Ad copy (headlines, CTAs, value propositions)
4. Match types (broad vs phrase vs exact in specific contexts)
5. Audiences (segments, layering, exclusions)
6. Extensions (which combinations generate most qualified clicks)

---

## 13. Landing Page Rules

### Performance Thresholds

- Page load time MUST be < 3 seconds (1 second delay on mobile reduces conversions up to 20%)
- Core Web Vitals: LCP < 2.5s, INP < 200ms, CLS < 0.1
- Only 47% of sites meet these thresholds in 2026; those that do see 15-30% conversion improvement

### CTA Rules

- USE a single primary CTA (single CTA pages convert 13.5% vs 10.5% for 5+ CTAs -- 32% improvement)
- PERSONALIZE CTAs (personalized CTAs perform 202% better than generic)
- ADD urgency where appropriate (can increase conversion by 332%)
- PLACE CTA in 3 positions: above the fold, mid-page (after building value), end of page
- MAKE buttons at least 48x48 pixels on mobile
- DO NOT use pop-ups that block content on mobile

### Content Rules

- MATCH landing page message exactly to the ad's promise and search intent
- KEEP forms minimal: name + email + phone is usually sufficient for leads
- INCLUDE social proof: testimonials, reviews, client logos, satisfaction numbers
- DO NOT send traffic to the homepage; use dedicated landing pages

### Conversational CTAs (2025-2026 Trend)

- Chat-based CTAs convert 3x better than traditional forms
- Chatbot conversion rates exceed 40%
- CONSIDER integrating chatbots or conversational forms as alternatives to static forms

### Dynamic Landing Pages

- IF account has volume: use dynamic landing pages personalizing headline by keyword, images by location, offers by audience segment
- AI-powered personalization benchmarks: healthcare sees 184% more conversion, e-commerce sees 247% more conversion
- CAUTION: Google incorporates on-site behavior in landing page scoring; thin content, keyword stuffing, or auto-substituted text blocks can HURT Quality Score

---

## 14. Scripts and Automation

### High-Value Scripts (2026)

1. Budget pacing alerts
2. Disapproval monitoring
3. Broken URL detection
4. Search Terms mining for negatives
5. Performance anomaly detection

### Technical Limits

- 30 minutes execution time per run
- 10,000 get/mutate operations quota
- GAQL-based queries are significantly faster than iterator approaches

### Automation Rules

- Native automated rules handle ~80% of standard automation tasks
- USE scripts for multi-variable conditions, cross-campaign operations, and external data integration
- 63% of active advertisers use 1-5 scripts; PPC specialists average 3.8 scripts per account

---

## 15. Starter vs Scale Playbooks

### For New Accounts (Starter)

1. START with: Search Brand + Search Non-Brand + Remarketing
2. IMPLEMENT perfect conversion tracking before anything else
3. USE Manual CPC first; only migrate to Smart Bidding with sufficient data
4. BUILD negative keyword lists from day 1
5. CREATE dedicated landing pages (never send traffic to homepage)
6. EXPECT 2-3 months for consistent results

### For Scaling Accounts

1. LAUNCH Performance Max with rich assets: 20+ images, videos, varied headlines
2. ADD Demand Gen for top of funnel (especially with Creator Partnerships)
3. IMPLEMENT Target ROAS with portfolio strategies
4. BUILD first-party data stack: Customer Match + Enhanced Conversions + Data Manager API
5. ESTABLISH systematic A/B testing culture
6. DEPLOY Google Ads Scripts for repetitive routines

---

## 16. Common Errors and Corrections

### Tracking Errors

| Error | Action |
|---|---|
| Inconsistent conversion tracking | AUDIT and standardize attribution, counting, and windows |
| Using low-quality conversion actions | SET primary conversions ONLY for real-value actions |
| Not implementing Enhanced Conversions | IMPLEMENT for all main conversion actions |
| Tracking same conversion in GA4 AND Google Ads | CHOOSE one primary source; set the other as "Secondary" |

### Keyword Errors

| Error | Action |
|---|---|
| No proactive negative keywords | BUILD lists pre-launch + review weekly |
| Broad Match without robust Smart Bidding | USE Broad Match ONLY with 30+ conversions/mo and Smart Bidding |
| Ignoring Search Terms Report | REVIEW weekly (mandatory) |

### Structure and Bidding Errors

| Error | Action |
|---|---|
| Disorganized account structure | RESTRUCTURE following account structure decision tree |
| Smart Bidding with insufficient data | START with Manual CPC until minimum volume is reached |
| Abrupt budget/bid changes | ADJUST gradually by 15-20% |
| Over-aggressive CPA optimization | BALANCE CPA with total conversion volume |

### Creative Errors

| Error | Action |
|---|---|
| Few assets in PMax/Demand Gen | PROVIDE maximum variations (20+ images, 6+ videos, 15 headlines) |
| Ignoring Quality Score | MONITOR as diagnostic; optimize the three components |
| Not testing creatives | TEST continuously with at least 4 weeks per test |
| Landing page misaligned with ad | ALIGN messaging between ad copy and landing page |

### Management Errors

| Error | Action |
|---|---|
| "Set and forget" | FOLLOW the optimization cadence schedule |
| Not verifying settings consistency | AUDIT campaign settings monthly |
| Testing multiple variables at once | TEST one variable per experiment |

---

## 17. Essential Formulas

```
ROAS = Conversion Revenue / Ad Spend
CPA = Total Spend / Number of Conversions
CTR = (Clicks / Impressions) x 100
Conversion Rate = (Conversions / Clicks) x 100
ROI = ((Revenue - Total Cost) / Total Cost) x 100
Break-even ROAS = 1 / Gross Margin
```
