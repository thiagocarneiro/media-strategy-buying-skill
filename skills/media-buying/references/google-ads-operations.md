# Google Ads Operations Reference

Agent instructions for Google Ads campaign management, optimization, and measurement.

---

## 1. Weekly Optimization Checklist

Execute every item weekly unless a different frequency is noted.

| # | Action | Threshold / Trigger | Frequency |
|---|--------|---------------------|-----------|
| 1 | Review Search Terms Report | IF search term spend > 50% of CPA target AND conversions = 0 AND clicks >= 10 --> ADD as negative keyword | Weekly |
| 2 | Check budget pacing | IF campaign spending < 80% OR > 120% of daily budget --> INVESTIGATE delivery issues | Daily |
| 3 | Analyze Impression Share | IF Lost IS (Budget) > 20% --> EVALUATE budget increase. IF Lost IS (Rank) > 30% --> OPTIMIZE Quality Score | Weekly |
| 4 | Review low-performance keywords | IF keyword CPA > 2x target AFTER completing 1 full conversion lag cycle AND clicks >= 20 --> PAUSE or REDUCE bid | Weekly |
| 5 | Check ad disapprovals | IF any ad disapproved --> FIX immediately | Daily |
| 6 | Verify conversion tracking | IF conversions = 0 for 48h+ on active campaign --> INVESTIGATE tag implementation | Daily |
| 7 | Review Display placements | IF placement spend > $50 AND conversions = 0 --> EXCLUDE placement | Biweekly |
| 8 | Analyze Quality Score | IF keyword QS < 5 --> OPTIMIZE ad relevance + landing page experience | Weekly |
| 9 | Check CPC anomalies | IF CPC increased > 25% without market change --> INVESTIGATE cause | Weekly |
| 10 | Monitor competition (Auction Insights) | IF new competitor with IS > 30% --> EVALUATE competitive response | Biweekly |

### Negative Keyword Decision Rules

| Condition | Action |
|-----------|--------|
| Term clearly irrelevant to business | ADD as negative immediately (Phrase Match) |
| Term with spend > 3x CPA target AND 0 conversions | ADD as negative (Exact Match) |
| Term with spend > 2x CPA target after 2 weeks | ADD as negative (evaluate Phrase vs Exact) |
| Relevant term but wrong audience | ADD as negative at campaign-level only |
| Recurring pattern of irrelevant terms | ADD root to shared negative list |

---

## 2. Monthly Optimization Workflow

### Week 1 -- Performance Analysis

- [ ] Pull full prior-month report vs previous month and YoY
- [ ] Analyze KPIs per campaign: CPA, ROAS, conversions, CTR, CPC
- [ ] Identify top 3 and bottom 3 campaigns by efficiency
- [ ] Calculate real contribution margin: (Revenue - Ad Cost - COGS)

### Week 2 -- Structure Optimization

- [ ] Re-evaluate ad group structure (consolidate or split per signals below)
- [ ] Review and update RSAs (replace "Low" rated assets)
- [ ] Test new ad extensions
- [ ] Update negative keyword lists with month's learnings

### Week 3 -- Budget and Bidding

- [ ] REALLOCATE budget: MOVE from campaigns with CPA > 2x target TO campaigns with CPA < target
- [ ] Evaluate bidding strategy transitions (IF conversion volume changed)
- [ ] Verify bid adjustments (geo, device, schedule) with last month's data
- [ ] Assess which campaigns are ready to scale or need pullback

### Week 4 -- Testing and Experimentation

- [ ] Define hypothesis for next month's A/B test
- [ ] Configure experiment (bid strategy, landing page, or ad copy)
- [ ] Evaluate prior test results (minimum 4 weeks of data required)
- [ ] Document learnings for future reference

---

## 3. Campaign Launch Workflows

### 3.1 Search Campaign Launch

#### Days 0-2: Preparation and Build

- [ ] Define SMART objective and target KPIs (CPA, ROAS, volume)
- [ ] Verify conversion tracking (manually test one conversion)
- [ ] Confirm Enhanced Conversions is active
- [ ] Calculate daily budget: `(CPA target x desired volume) / 30`
- [ ] Prepare dedicated landing pages (one per ad group)
- [ ] Create campaign: type Search, network Search Only (NO Display expansion)
- [ ] Configure geographic and language targeting
- [ ] Select bidding strategy (see Bidding Strategy Decision Tree below)
- [ ] Create thematic ad groups (5-15 keywords per group)
- [ ] Create RSAs: 15 headlines + 4 descriptions per ad group
- [ ] Add all relevant extensions (sitelinks, callouts, structured snippets)
- [ ] Apply shared negative lists + proactive specific negatives
- [ ] Configure ad schedule (if historical data exists)

#### Pre-Launch Checks

- [ ] ALL URLs return 200 (no 404s)
- [ ] Negative keywords DO NOT conflict with positive keywords
- [ ] ALL RSAs have Ad Strength >= "Good"
- [ ] Campaign settings verified: network, geo, language, devices
- [ ] Correct conversion actions set as primary

#### Days 3-7: Launch + Intensive Monitoring

- [ ] Activate campaign
- [ ] Monitor daily: impressions, clicks, CTR, spend
- [ ] Verify conversions are tracking (test a real conversion if possible)
- [ ] Review Search Terms Report DAILY during first week
- [ ] Add negatives reactively as needed
- [ ] DO NOT change bidding or budget during this phase (learning period)

#### Weeks 2-4: Initial Optimization

- [ ] Continue weekly Search Terms review
- [ ] Analyze performance by keyword and ad group
- [ ] IF keyword spend > 3x CPA target with 0 conversions --> PAUSE
- [ ] Evaluate Ad Strength; replace "Low" assets
- [ ] Check Quality Score; optimize below-average components
- [ ] Evaluate if conversion volume allows transition to Smart Bidding

#### Month 2+: Ongoing Optimization

- [ ] Follow weekly/monthly optimization routines (Sections 1-2)
- [ ] IF 50+ conversions/month --> EVALUATE expansion with Broad Match
- [ ] IF 30+ conversions/month --> CONSIDER activating AI Max
- [ ] Run first A/B test cycle (bid strategy or landing page)
- [ ] Reallocate budget from underperformers to top performers

### 3.2 Display Campaign Launch

#### Day 0: Preparation

- [ ] Define objective: awareness, remarketing, or prospecting
- [ ] Prepare visual assets:
  - MINIMUM: 5 images (landscape + square), 5 headlines, 5 descriptions
  - IDEAL: 10+ images in 3 aspect ratios, 15 headlines, 4 descriptions, logo
- [ ] Prepare landing pages
- [ ] Define audiences (remarketing lists, custom intent, in-market)

#### Day 1: Build

- [ ] Create Display campaign
- [ ] Set objective: Sales, Leads, or Awareness
- [ ] Bidding: Target CPA (if sufficient data) or Maximize Conversions
- [ ] Configure targeting:
  - Remarketing --> select remarketing audiences
  - Prospecting --> Custom Intent + contextual keywords
  - Awareness --> Affinity + Topic targeting
- [ ] Apply exclusions:
  - EXCLUDE apps and games (unless relevant to business)
  - EXCLUDE sensitive content categories
  - APPLY account-level placement exclusions
- [ ] Configure frequency capping (see frequency table below)
- [ ] Create Responsive Display Ads with all prepared assets
- [ ] Verify Ad Strength >= "Good"

#### Week 1: Monitoring

- [ ] Verify impressions are being served
- [ ] Monitor CTR (benchmark Display: 0.5-1%)
- [ ] Review Placement Report; exclude low-quality sites
- [ ] Check viewability metrics (Active View)
- [ ] DO NOT make significant changes (learning period)

#### Weeks 2-4: Optimization

- [ ] Analyze placement performance: EXCLUDE sites with spend and 0 conversions
- [ ] Review audience performance: identify best-performing segments
- [ ] Evaluate asset performance: replace "Low" rated assets
- [ ] Adjust frequency caps if needed
- [ ] Consider bid adjustments by audience segment

### Display Frequency Capping Reference

| Funnel Stage | Impressions/Day | Impressions/Week | Duration |
|--------------|-----------------|-------------------|----------|
| Awareness | 1-2 | 7-10 | 3-4 weeks |
| Consideration | 2-3 | 8-12 | 2-3 weeks |
| Conversion | 3-4 | 12-18 | 1-2 weeks |
| Retention | 0.5-1 | 3-5 | Ongoing |

Rule: First 3-5 impressions generate approximately 80% of conversion potential. Impressions 6-10 contribute only 15%.

---

## 4. Bid Adjustment Formulas

### Primary Formula (Performance-Based)

```
Bid Adjustment % = ((Device Metric / Campaign Average Metric) - 1) x 100
```

### CPA-Based Formula

```
Bid Adjustment % = ((Average CPA / Device CPA) - 1) x 100
```

Example: IF campaign average CPA = $50 AND mobile CPA = $75:
```
Adjustment = (($50 / $75) - 1) x 100 = -33%
```
Action: REDUCE mobile bids by 33%.

### Target-Based Formula

```
New Bid = Current Bid x (Target CPA / Current CPA)
```

### Incremental Adjustment (When Existing Adjustment Exists)

DO NOT simply add the new calculation. Use this method:

```
1. Multiply existing adjustment by new formula output (in decimal)
2. Add that product to the original adjustment

Example:
  Existing: +40%
  New calculation: +20%
  Incremental: 0.40 x 0.20 = 0.08 = +8%
  Final result: +48% (NOT +60%)
```

### Statistical Significance Requirements

| Metric | Minimum Required |
|--------|------------------|
| Clicks per segment | 100+ clicks |
| Conversions per segment | 30+ conversions |
| Time period | 30-90 days |
| Recalibration frequency | Every 1-4 weeks depending on volume |

Rule: DO NOT make bid adjustments based on fewer than 100 clicks per segment. For conversion-based adjustments, WAIT for 30+ conversions per device/location/schedule segment.

### Smart Bidding Compatibility

| Bidding Strategy | Bid Adjustments Supported? |
|------------------|---------------------------|
| Manual CPC | ALL adjustments (device, location, schedule, audience) |
| Target CPA | ONLY device adjustments (modifies CPA target, not bid) |
| Target ROAS | ONLY device adjustments (modifies ROAS target, not bid) |
| Maximize Conversions | NO bid adjustments supported |
| Maximize Conv. Value | NO bid adjustments supported |

Rule: Under Smart Bidding, Google handles signal-based optimization automatically. Location, time-of-day, and audience bid adjustments have NO effect. Only device bid adjustments of -100% (full exclusion) are honored.

### Bid Adjustment Ranges

| Type | Range | Level |
|------|-------|-------|
| Device | -100% to +900% | Campaign or Ad Group |
| Location | -90% to +900% | Campaign |
| Ad Schedule | -90% to +900% | Campaign |
| Audiences | -90% to +900% | Campaign or Ad Group |

Note: Setting device to -100% = opting out of that device entirely.

### When to Use Adjustments vs Separate Campaigns

- USE bid adjustments WHEN performance difference between segments is moderate (< 2x CPA difference)
- USE separate campaigns WHEN device performance differs dramatically (2x+ CPA difference) OR different creative/landing page strategies are needed per segment

---

## 5. Budget Pacing Calculations

### Monthly Pacing Formula

```
Expected Spend = (Monthly Budget / Days in Month) x Days Elapsed
Pacing Ratio = Actual Spend / Expected Spend
```

### Pacing Alert Thresholds

| Pacing Ratio | Status | Action |
|--------------|--------|--------|
| < 0.85 | UNDERPACING | INVESTIGATE delivery issues, CHECK bids, CHECK targeting |
| 0.85 - 1.15 | ON TRACK | Monitor normally |
| > 1.15 | OVERPACING | REDUCE bids or daily budget cap |

### Pacing Monitoring Checkpoints

Track spend at 50%, 90%, and 100% of monthly budget cap with automated alerts. Recommended: hourly checks during active campaign hours.

---

## 6. Budget Reallocation Framework

### 6.1 The 20% Scaling Rule

NEVER increase budget by more than 20% at a time.

| Budget Level | Scaling Approach |
|--------------|------------------|
| Under $100/day | More flexible; larger proportional jumps OK (e.g., $25 --> $50) |
| $100-$1,000/day | STRICT 20% adherence required |
| $1,000+/day | 20% rule is CRITICAL for success |

Warning: A 50% increase from $1,000 to $1,500/day can make learning phase pronounced and inefficient; campaign may never stabilize back to target metrics.

### 6.2 Five-Step Stair-Step Scaling Process

```
Step 1: ESTABLISH baseline in "Money Zone" (campaign meeting target KPIs)
Step 2: INCREASE budget by 20%
Step 3: ACCEPT temporary CPA spike during learning phase
Step 4: WAIT 1-2 weeks for re-optimization
Step 5: ASSESS stability --> IF stable, REPEAT from Step 2
```

IF CPA continues rising beyond 2 weeks --> STOP scaling, PULL BACK to previous level.
IF dramatic conversion or traffic drops --> STOP scaling, INVESTIGATE.

### 6.3 Budget Reallocation Thresholds

| Condition | Action |
|-----------|--------|
| ROAS drops below 3x for more than $500 spend | REDUCE budget by 30% |
| ROAS exceeds 6x for more than 100 conversions | INCREASE budget by up to 50% (max 2x original daily) |
| IS Lost (Budget) > 20% with proven ROI | Campaign NEEDS more budget |
| CPA rising for 2+ weeks after budget change | PULL BACK to previous level |
| Campaign in learning phase | DO NOT make additional changes |

### 6.4 Portfolio Budget Allocation (70/20/10 Rule)

| Allocation | Purpose | Description |
|------------|---------|-------------|
| 70% | Proven performers | Campaigns with consistent ROI meeting targets |
| 20% | Optimization | Enhancement of existing approaches and incremental scaling |
| 10% | Testing | New campaign types, features, experimental approaches |

### 6.5 Scale-Ready Criteria

BEFORE scaling any campaign, verify ALL of the following:

- [ ] Campaign has been running for 30+ days minimum
- [ ] Achieved target CPA/ROAS consistently for 2+ weeks
- [ ] Conversion volume is 15+ per week (Smart Bidding stability)
- [ ] Impression Share Lost (Budget) > 10% (room to grow)
- [ ] Quality Scores averaging 7+ on key terms
- [ ] No significant conversion lag issues
- [ ] Landing page performance stable

### 6.6 When to Pull Back Spend

PULL BACK when ANY of the following is true:

- CPA exceeds 150% of target for 7+ consecutive days
- ROAS drops below 50% of target for 7+ consecutive days
- Conversion volume drops > 40% without seasonal explanation
- New competitor significantly disrupts auction (check Auction Insights)
- Landing page/product issues affecting conversion
- Budget depletes before noon consistently (underfunded)

### 6.7 Budget Reallocation Between Campaigns

```
Efficiency Score = (Conversions x Value per Conversion) / Cost
```

- Campaigns with Score > average --> CANDIDATES to receive additional budget
- Campaigns with Score < 50% of average --> CANDIDATES for reduction

### 6.8 When to Scale (Increase Budget)

- CPA consistently < target for 2+ weeks
- Lost IS (Budget) > 20% (unmet demand exists)
- Conversion volume increasing without CPA degradation
- Maximum increment: 15-20% per adjustment

### 6.9 When to Reduce Budget

- CPA > 2x target for 2+ weeks without improvement trend
- ROAS below break-even for 3+ weeks
- Zero conversions after spending 5x CPA target
- Gradual reduction: 15-20% per adjustment, monitor for 1 week

---

## 7. Google Ads Scripts Catalog

### 7.1 Essential Monitoring Scripts (Priority: Deploy First)

| Script | Purpose | Schedule |
|--------|---------|----------|
| **Budget Pacing Alert** | Detects over/underspending vs monthly targets. Tracks at 50%, 90%, 100% of monthly cap. Configurable 15% variance threshold. | Hourly during active hours |
| **Disapproved Ads Alert** | Notifies of policy violations before campaigns lose delivery | Every 2 hours (regulated industries) |
| **Broken URL/Link Checker** | Detects 404 pages preventing budget waste | Daily |
| **Account Anomaly Detector** | Flags significant performance deviations from 28-day baseline | Hourly or daily |
| **Change History Alerts** | Monitors unauthorized account modifications | Daily |

Rule: ANY account spending over $5,000/month MUST have at minimum a budget monitor and disapproval alert running at all times.

### 7.2 Anomaly Detection Thresholds

Compares last 7 days against 28-day baseline using percentage deviation from each campaign's own baseline.

| Metric | Variance Threshold |
|--------|-------------------|
| CTR | > 20% deviation --> INVESTIGATE |
| CPA | > 25% deviation --> INVESTIGATE |
| Conversion volume | > 30% deviation --> INVESTIGATE |

### 7.3 Search Campaign Scripts

| Script | Purpose |
|--------|---------|
| **N-Gram Analysis** | Breaks search queries into 1-3 word fragments, aggregates metrics, identifies waste patterns. 1-2 word n-grams for finding negatives; 3-4 word for keyword opportunities. |
| **Search Query Mining** | Identifies non-converting search terms (5+ clicks, 0 conversions) for negative keyword implementation |
| **Keyword CPA Tier** | Organizes keywords by cost-per-acquisition tiers |
| **Quality Score Analysis** | Identifies QS improvement opportunities to reduce CPCs |
| **Ad Copy Performance Matrix** | Analyzes RSA headlines/descriptions with CTR and CVR data |
| **Landing Page + Ad Mismatch Detector** | Flags URL inconsistencies harming Quality Score |

### 7.4 Display/PMax Scripts

| Script | Purpose |
|--------|---------|
| **PMax Insights** | Extracts buried performance data from PMax campaigns |
| **PMax Non-Converting Search Terms Alert** | Suggests wasteful queries for exclusion |
| **PMax Brand Traffic Analyzer** | Reveals brand vs non-brand traffic split and true ROAS |
| **PMax Placement Exclusion Suggestions** | Surfaces low-quality placements for removal |
| **PMax Asset Performance Dump** | Shows which creative elements drive results |

### 7.5 Technical Limits

| Constraint | Limit |
|------------|-------|
| Execution time per run | 30 minutes maximum |
| Get operations per run | 10,000 |
| Mutate operations per run | 10,000 |
| Max results per iterator selector | 50,000 |
| Authorized scripts per account | 250 |

### 7.6 Script Deployment Rules

1. ALWAYS test in Preview mode before deploying
2. Test bid-modifying scripts on 5-10% of campaigns first (use labels)
3. Monitor for 1 week before expanding account-wide
4. Include ownership, purpose, schedule, and last-reviewed date in script headers
5. Check run history for silent failures every 30 days
6. IF deploying user leaves the account, scripts silently stop -- VERIFY script ownership on any team changes

---

## 8. Advanced Measurement

### 8.1 Conversion Lag by Industry

| Industry/Type | 80% of conversions in | 95% of conversions in |
|---------------|------------------------|------------------------|
| E-commerce (impulse) | 1-2 days | 3-5 days |
| SaaS / Services | 3-7 days | 14-21 days |
| B2B / Enterprise | 7-14 days | 30-60 days |
| Real Estate / Auto | 14-30 days | 60-90 days |

### Conversion Lag Rules

- NEVER optimize based on data less than 1 full conversion lag cycle old
- IF 80% of conversions take 7 days --> WAIT at least 7 days before evaluating any change
- The 80% rule: IF 80% of conversions come in within 7 days, then pulling a report at day 3 is inherently misleading
- USE rolling 30 or 60-day periods for performance analysis
- Compare "Conversions" vs "Conversions (by conversion time)" columns to match identical periods
- Smart Bidding accounts for conversion lag internally, but dashboard data misleads humans -- DO NOT override Smart Bidding decisions based on incomplete recent data

### How to Measure Conversion Lag

1. Navigate to Tools & Settings --> Attribution --> Path metrics
2. Review "days/hours to conversion" distribution
3. Identify at how many days 80% and 95% of conversions are reported

### Attribution Window Recommendation

- DEFAULT: Use 30-day click-through window
- ONLY reduce to 7 days IF data shows > 90% of conversions occur within 7 days
- For long-cycle journeys (B2B, high-value), 7-day window undercounts legitimate conversions

### 8.2 Incrementality Testing

#### Test Types

| Test Type | Method | When to Use |
|-----------|--------|-------------|
| **Conversion Lift (User-Based)** | Google randomizes test/control groups at user level | Sufficient volume (thousands of users) |
| **Conversion Lift (Geo-Based)** | Divides geographic markets into treatment and control | Supports offline data; minimum 14 days duration |
| **GeoLift (Open Source)** | Meta-developed framework using advanced statistical models | Budgets > $50K/month where test investment is justified |

#### Setup Process

1. Navigate to Experiments in Google Ads
2. Select "Conversion Lift"
3. Define experiment parameters (test/control split, duration)
4. Ensure sufficient conversion volume (generally 100+ conversions minimum)
5. Wait for statistically significant results (typically 2-4 weeks)

#### Interpretation Rules

- USE incremental cost per conversion (iCPC) rather than raw lift percentages
- Reframe results as in-platform incrementality, not total business impact
- Pressure-test against adjacent data (CRM, revenue trends, downstream metrics)
- Limitation: Google tests measure only in-platform outcomes; they miss downstream effects like store visits, brand lift, or retention

### 8.3 Offline Conversion Tracking (GCLID Flow)

```
Click on ad --> Lead fills out form (GCLID captured) -->
CRM logs lead --> Sale happens offline -->
Conversion uploaded back to Google Ads
```

#### Setup Steps

1. **Enable auto-tagging**: Account Settings --> Auto-tagging --> Enable
2. **Capture GCLID on website**: Add JavaScript to capture GCLID from URL parameter; store in hidden form field or cookie; pass to CRM on form submission
3. **Create conversion action**: Goals --> Conversions --> New conversion action --> "Import" --> "Other data sources or CRMs"; configure name, category, value, count, attribution
4. **Store GCLID in CRM**: Create custom field for GCLID; map form submission to CRM record
5. **Upload conversions**: Prepare CSV with columns: Google Click ID, Conversion Name, Conversion Time, Conversion Value; upload via Goals --> Conversions --> Uploads
6. **Automate uploads**: Use Google Ads API, Zapier, or CRM-native integration; upload daily or near real-time

#### Constraints

- Conversions uploaded more than **90 days** after the click WILL NOT be imported
- GCLID has a 90-day expiration
- Conversion name in CSV MUST match exactly what is defined in Google Ads
- Ensure GDPR/privacy compliance throughout

### 8.4 Enhanced Conversions for Leads (ECL)

Upgraded version of offline conversion import using first-party data (email, phone) instead of browser-dependent GCLID.

Benefits over standard GCLID import:
- More durable across devices and browsers
- Supports engaged-view conversions
- Enables cross-device conversion tracking
- More privacy-compliant

Setup: Implement via Google Tag Manager, gtag.js, or Google Ads API. REQUIRES hashing PII data (SHA-256) before sending to Google.

---

## 9. Auction Insights Interpretation

### Key Metrics

| Metric | Definition | What It Tells You |
|--------|-----------|-------------------|
| **Impression Share (IS)** | % of eligible impressions you received | Your share of the market |
| **Overlap Rate** | How often competitor's ad appeared when yours did | High overlap (60%+) = true paid search competitor |
| **Position Above Rate** | How often competitor ranked higher than you | Competitive threat level |
| **Top of Page Rate** | How often your ad appeared above organic results | Visibility level |
| **Abs. Top of Page Rate** | How often your ad was in position #1 | Most expensive position; validate with ROAS |
| **Outranking Share** | % of times you ranked higher OR showed when competitor didn't | Direct competitive win rate |

### Critical Thresholds

| Threshold | Significance |
|-----------|-------------|
| IS below 10% | Auction Insights data becomes UNAVAILABLE |
| 15%+ metric shift | Significant enough to warrant investigation |
| IS Lost (Budget) > 20% | Visibility is incomplete; data interpretation unreliable |
| Competitor IS change > 15% | REQUIRES competitive response analysis |

### Interpretation Rules

| Scenario | Meaning | Action |
|----------|---------|--------|
| High Overlap + Low Position Above | You dominate this competitor | MAINTAIN current approach; monitor |
| High Overlap + High Position Above | Competitive threat | INVESTIGATE Quality Score, extensions, offers (NOT just bids) |
| Low IS + High IS Lost (Budget) | Budget exhaustion | INCREASE daily budget IF campaign is profitable |
| Low IS + High IS Lost (Rank) | Quality/bid issue | IMPROVE QS before increasing bids |
| New competitor with rising IS | Market entry threat | RESEARCH their ads, DIFFERENTIATE offers |
| Competitor IS declining | Opportunity | CONSIDER capturing their lost share |

### Data Limitations

- No bid, budget, or creative visibility within the report
- Only shows competitors bidding on identical keywords
- USE 30-90 day windows; 7-day windows create false signals
- April 2025 policy update: each placement (top/bottom) counts as separate impression -- competitor IS may appear inflated due to double-serving

### Strategic Actions

**Weekly:**
- Monitor competitive metrics during high-competition periods
- Research top competitors' ads via incognito searches and Google Ads Transparency Center

**Monthly:**
- Track 30-90 day trends (avoid short-term volatility)
- Calculate cost-per-conversion by position before pursuing Abs. Top placement
- Identify less-competitive keyword territories as revenue opportunities

---

## 10. Conflict Resolution Hierarchy

WHEN contradictory signals appear simultaneously, apply this priority order (highest first):

```
1. TRACKING HEALTH    --> IF conversion tracking is broken, STOP everything until fixed
2. CPA/ROAS HEALTH   --> Financial efficiency takes priority over volume
3. CONVERSION VOLUME  --> Growth is valid ONLY IF CPA is healthy
4. IMPRESSION SHARE   --> Visibility is secondary to efficiency
```

### Common Conflict Scenarios

| Conflict | Resolution |
|----------|-----------|
| Lost IS (Budget) high + CPA > target | PRIORITIZE CPA. DO NOT increase budget. FIRST optimize efficiency (negatives, landing pages, QS). ONLY expand budget when CPA returns to target. |
| CTR high + Conversion Rate low | PRIORITIZE conversion rate. Traffic is arriving but not converting. INVESTIGATE landing page, audience quality, message alignment. |
| QS high + CPA high | INVESTIGATE landing page and audience. Good QS means relevance is OK, but page doesn't convert or audience is wrong. |
| Paused keywords + conversion volume falling | RE-EVALUATE pause. CHECK if conversion lag was masking conversions. CONSIDER reactivating with lower bid. |

---

## 11. Escalation Protocols

The agent MUST escalate to human review for the following -- DO NOT take autonomous action:

| Trigger | Reason |
|---------|--------|
| Budget change > 30% of current value | Significant financial impact |
| Pausing campaign representing > 25% of total spend | Risk of critical volume loss |
| Performance degraded > 30% WoW without identifiable cause | Possible external factors (site down, competition, seasonality) |
| Recommendation to restructure entire account | High-complexity change with learning reset |
| Zero conversions for 72h+ on previously active campaign | Possible tracking, site, or policy issue |
| Conflict between advertiser objectives and performance data | Strategic decision, not operational |
| Launching new campaign type (PMax, Demand Gen) | Requires strategic alignment |

---

## 12. Pre-Action Validation Protocol

BEFORE executing ANY change, verify:

1. **Sufficient data?** Minimum conversions/clicks for significance (see thresholds in each section)
2. **No conflict with recent change?** IF change made in last 14 days on same campaign --> WAIT for learning phase to end
3. **Safe magnitude?** Budget/bid changes limited to 15-20% per adjustment
4. **Reversible?** PREFER reversible actions (bid adjustments, negatives) OVER irreversible ones (pausing campaigns, deleting keywords)
5. **Documented?** RECORD each change with date, reason, and metrics that motivated the action

---

## 13. Bidding Strategy Decision Tree

```
Conversions/month per campaign?
|
+-- < 15 conversions/month
|   IF objective = traffic --> Maximize Clicks (with CPC cap)
|   IF objective = conversion --> Manual CPC
|   IF new account --> Manual CPC for 2-4 weeks, then reassess
|
+-- 15-30 conversions/month
|   IF CPA target defined --> Maximize Conversions (no target)
|   IF budget flexible --> Maximize Conversions to accumulate data
|
+-- 30-50 conversions/month
|   IF conversion values defined --> Target ROAS
|   IF CPA target clear --> Target CPA
|   IF neither --> Maximize Conversions with monitoring
|
+-- 50-100 conversions/month
|   IF e-commerce --> Maximize Conversion Value + Target ROAS
|   IF lead gen --> Target CPA
|   IF multiple campaigns --> Portfolio Bid Strategy
|
+-- 100+ conversions/month
    IF priority = efficiency --> Target ROAS (strict)
    IF priority = volume --> Target ROAS (flexible/exploration)
    IF multiple campaigns --> Portfolio Strategy mandatory
```

### Conversion Volume Thresholds for Structure Decisions

| Conversions/Month per Campaign | Recommended Structure | Bidding Strategy |
|-------------------------------|----------------------|------------------|
| < 15 | SKAG/STAG with Manual CPC | Manual CPC |
| 15-30 | STAG with Smart Bidding | Maximize Conversions |
| 30-50 | Hagakure / Consolidated | Target CPA or Target ROAS |
| 50-100 | Consolidated with Broad Match | Target CPA/ROAS + Broad Match |
| 100+ | Maximum consolidation + AI Max | Target ROAS + AI Max features |

Rule: Learning phase requires approximately 50 conversion events or 3 cycles to stabilize. BEFORE creating new campaigns or splitting existing ones, verify: "Will each resulting campaign have sufficient conversions to exit learning phase?"

---

## 14. Key Benchmark Reference Tables

### CPC Benchmarks (2026)

| Industry | Average CPC (Search) |
|----------|---------------------|
| Legal | $8.58 |
| Dental Services | $7.85 |
| Education | $6.23 |
| Finance | $3.46 |
| Arts & Entertainment | $1.60 |
| E-commerce | $1.16 |
| Overall Average | $2.69 |

### CTR Benchmarks (2026)

| Industry | Search CTR |
|----------|-----------|
| Arts & Entertainment | 13.10% |
| Sports & Recreation | 9.19% |
| Finance & Insurance | 8.33% |
| Overall Average | 6.66% |
| Display Average | 0.46% |

Red flag: Under 1% CTR on Search is problematic.

### Conversion Rate Benchmarks (2026)

| Industry | Average CVR |
|----------|------------|
| Automotive Repair/Service | 14.67% |
| Animals & Pets | 13.07% |
| Overall Search Average | 4.40% |
| Display Average | 0.59% |

### CPA Benchmarks (2026)

| Industry | Avg CPA (Search) |
|----------|-----------------|
| B2B/Business Services | $116.13 |
| Legal/Attorneys | $86.00 |
| Finance & Insurance | $81.93 |
| Education | $72.70 |
| E-commerce/Retail | $45.27 |
| Overall Average CPL | $70.11 |

### Quality Score Impact

For each Quality Score point above 5, CPA drops by approximately 16%.

Improving landing page experience from "Average" to "Above Average" reduces CPC by 15-30% across entire account -- highest-leverage QS optimization.

---

## 15. Impression Share Analysis Decision Tree

```
Lost IS (Budget) > 20%?
|
+-- YES --> Budget is the bottleneck
|   IF budget can be increased --> INCREASE gradually (15-20%)
|   IF budget is fixed --> REDUCE scope: more aggressive negatives,
|       focus on best-converting geos/hours, pause high-CPA keywords
|
+-- NO --> Check Lost IS (Rank)
    |
    +-- Lost IS (Rank) > 30%?
    |   YES --> Quality Score and/or bid is the problem
    |       IF QS < 6 --> OPTIMIZE QS components
    |       IF QS >= 6 --> CONSIDER increasing bids
    |   NO --> IS is adequate, FOCUS on conversion rate
    |
    +-- Both low? --> Dual problem: PRIORITIZE QS first, then budget
```

### Impression Share Targets

| Campaign Type | Target |
|---------------|--------|
| Brand campaigns | IS > 90% (ideally > 95%) |
| Brand - Abs. Top IS | Maximum priority |
| Non-brand - Top IS | > 50% for core keywords |
