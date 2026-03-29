# Google Ads: Troubleshooting, Audit & Recommendations

Agent reference for diagnosing performance issues, auditing accounts, and managing Google Ads recommendations.

---

## 1. Quick Diagnostic Flow

Follow this sequence top-down when investigating a performance problem:

```
Step 1: No impressions?
  -> Check budget, bidding, keywords, product approvals, payment status
  -> Allow 1 full week for new campaigns before troubleshooting

Step 2: Impressions but no clicks?
  -> Improve ad copy, strengthen CTAs, review targeting
  -> Benchmark: Search CTR 3-5%, Display CTR 0.5-1%
  -> Under 1% CTR on Search = red flag

Step 3: Clicks but no conversions?
  -> FIRST verify conversion tracking is firing correctly
  -> Fix landing page alignment, trust signals, page speed
  -> Benchmark: Conversion rate 2-5% (varies by industry)

Step 4: Add-to-carts but no purchases? (eCommerce)
  -> Simplify checkout, add express payment (PayPal, Apple Pay, Google Pay)
  -> Enable guest checkout, offer free shipping
  -> Express checkout reduces abandonment 30-50%

Step 5: Low conversion volume?
  -> Allow 3 months for algorithm learning
  -> Increase perceived value, optimize mobile experience
```

---

## 2. Performance Diagnostic Decision Trees

### 2.1 High CPC

2026 CPC benchmarks (Search):

| Industry | Avg CPC |
|---|---|
| Legal | $8.58 |
| Dental Services | $7.85 |
| Education | $6.23 |
| Finance | $3.46 |
| Arts & Entertainment | $1.60 |
| E-commerce | $1.16 |
| Overall Average | $2.69 |

Decision tree:

```
CPC above benchmark or historical?
  IF Quality Score < 5:
    Check Expected CTR:
      "Below Average" -> Rewrite headlines with keyword + benefit
      Keywords too generic -> Refine to more specific intent
    Check Ad Relevance:
      "Below Average" -> Reorganize ad groups thematically
      RSA missing keyword -> Add keyword to headlines
    Check Landing Page Experience:
      "Below Average" -> Optimize Core Web Vitals (LCP < 2.5s)
      Content irrelevant -> Align LP with ad group intent
      Poor mobile UX -> Mobile-first redesign
    NOTE: Improving LP experience from "Average" to "Above Average"
          reduces CPC by 15-30% across the account

  IF Quality Score 5-6:
    Improve the weakest QS component first
    Each QS point above 5 = ~16% CPA reduction

  IF Quality Score 7+:
    Check Auction Insights for increased competition
      YES -> Evaluate competing vs. shifting to less contested keywords
      NO -> Check bid strategy settings
    Broad Match too wide -> Refine with negatives or reduce to Phrase
    Bid strategy too aggressive -> Relax target CPA/ROAS by 10-15%

  IF Automated bidding in learning phase -> Wait 1-2 weeks

  ALWAYS: Review Search Terms report -> Add negative keywords for irrelevant terms
```

### 2.2 Low CTR

2026 CTR benchmarks (Search):

| Industry | Search CTR |
|---|---|
| Arts & Entertainment | 13.10% |
| Sports & Recreation | 9.19% |
| Shopping/Collectibles | 8.92% |
| Finance & Insurance | 8.33% |
| Overall Average | 6.66% |
| Display Average | 0.46% |

Decision tree:

```
CTR below benchmark?

  FOR Search campaigns:
    1. Check ad copy quality:
       -> Navigate: Campaigns > Ads > View Asset Details
       -> Identify underperforming headlines/descriptions
       -> Remove low-performing variations
       -> Add alternatives with clear CTAs ("Buy Now", "Get Free Quote", "Try Free")

    2. Check keyword-ad alignment:
       -> Are ad headlines reflecting search intent?
       -> Restructure broad ad groups into tighter groups
       -> Restructuring improves CTR by ~15%

    3. Check ad extensions:
       -> Ensure sitelinks, callouts, structured snippets are active
       -> Add call extensions, location extensions where applicable

    4. Check ad position:
       -> Review Impression Share Lost (Rank)
       -> Higher positions correlate with higher CTR

    5. Check match types:
       -> Too broad -> Refine with negatives

  FOR Display campaigns:
    -> Creatives outdated -> Refresh images and headlines
    -> Targeting too broad -> Refine audiences or add contextual
    -> Frequency too high -> Adjust frequency cap
    -> Low-quality placements -> Exclude irrelevant sites

  Wait 1-2 weeks for re-evaluation after changes
```

### 2.3 Low Conversion Rate

2026 CVR benchmarks:

| Industry | Average CVR |
|---|---|
| Automotive Repair/Service | 14.67% |
| Animals & Pets | 13.07% |
| Physicians & Surgeons | 11.62% |
| Real Estate | 3.28% |
| Finance & Insurance | 2.55% |
| Overall Search Average | 4.40% |
| Display Average | 0.59% |

Decision tree:

```
Conversion rate below benchmark or historical?

  FIRST: Check tracking
    -> Test a conversion manually. If it does not track, fix the tag.
    -> Verify via Google Tag Assistant

  IF tracking is intact:
    1. Check algorithm maturity (for new campaigns):
       Days 1-7: Inconsistent, higher costs -> NORMAL, do not intervene
       Days 8-14: Pattern emergence
       Weeks 3-4: Visible improvement
       Month 2: Significant efficiency gains
       Month 3+: Sustained optimization
       -> Allow 3 months for full optimization on new accounts

    2. Audit landing page:
       -> Page speed: LCP must be under 3 seconds (test on GTmetrix)
       -> Mobile optimization: buttons min 48x48px, no blocking pop-ups
       -> Trust signals: reviews, security badges, guarantees
       -> CTA clarity: position CTA above fold + middle + end
       -> Alignment: does page headline match ad headline?
       -> Bounce rate > 70% -> Improve above-fold content, speed, relevance
       -> Form too long -> Reduce to name + email + phone

    3. Simplify conversion path:
       -> Reduce form fields
       -> Add express payment options
       -> Enable guest checkout
       -> Offer free shipping (build cost into price)

    4. Review targeting quality:
       -> Search Terms report: are queries relevant?
       -> Audience segments: are they qualified?
       -> Negative keywords: are irrelevant clicks filtered?
       -> Low-converting geos -> Negative bid adjustment or exclude

    5. Check external factors:
       -> Seasonality? Adjust expectations
       -> Competitor launched better offer? Revise positioning
       -> Site issues (checkout, form broken)? QA the conversion flow
```

### 2.4 High CPA

2026 CPA benchmarks (Search):

| Industry | Avg CPA |
|---|---|
| B2B/Business Services | $116.13 |
| Legal/Attorneys | $86.00 |
| Finance & Insurance | $81.93 |
| Education | $72.70 |
| E-commerce/Retail | $45.27 |
| Overall Average CPL | $70.11 |

Decision tree:

```
CPA above target?

  IF CPA > 3x target -> EMERGENCY:
    -> Pause keywords/ad groups with CPA > 3x target
    -> Verify conversion tracking (lost conversions inflate apparent CPA)
    -> Reduce scope: focus only on proven high-intent keywords
    -> IF Smart Bidding: verify target CPA is realistic for the market

  IF CPA 1.5-3x target -> ACTIVE OPTIMIZATION:
    -> Identify top 20% keywords by CPA -> Allocate more budget
    -> Identify bottom 20% keywords by CPA -> Pause or reduce bid
    -> Review and optimize landing pages for conversion
    -> Add negatives to eliminate irrelevant traffic
    -> Check conversion lag (recent CPA looks worse than reality)

  IF CPA 1-1.5x target -> FINE TUNING:
    -> Adjust bid adjustments (geo, device, schedule)
    -> Test new ad copy variations
    -> A/B test landing pages
    -> Evaluate if target CPA can be relaxed to gain volume

  ALWAYS verify Target CPA settings:
    -> Historical CPA $80 with Target CPA $40 = too aggressive
    -> Set target within 10-20% of historical CPA
    -> Allow 7-14 days for learning after changes

  ALWAYS audit conversion tracking:
    -> Tags firing correctly? No double-counting?
    -> No recent changes that broke tracking?

  ALWAYS improve Quality Score:
    -> Each QS point above 5 = ~16% CPA reduction
    -> Priority: landing page > ad relevance > expected CTR

  ALWAYS refine targeting:
    -> Geographic: exclude low-value locations
    -> Device: adjust bids based on device conversion rates
    -> Schedule: reduce bids during low-converting hours
    -> Audiences: layer in high-intent audiences
```

### 2.5 Low ROAS

Decision tree:

```
ROAS below target?

  1. Check target ROAS settings:
     -> Target too aggressive? (e.g., 500% when historical is 300%)
     -> Fix: Lower to 80% of historical average
     -> Monitor for 1 week, then gradually increase
     -> Report values across all campaigns for 4 weeks or 3 conversion
        cycles (whichever is longer) before setting ROAS target

  2. Monitor the 4 ROAS drivers:
     -> CTR: ad engagement
     -> CPC: cost efficiency
     -> Conversion Rate: landing page effectiveness
     -> Average Order Value: product/offer quality
     -> A drop in ANY of these affects ROAS

  3. Check for ad fatigue:
     -> Rotate creatives regularly
     -> Introduce new offers and visuals
     -> Explore new ad formats

  4. Verify conversion data quality:
     -> Account for conversion lag
     -> Check attribution model
     -> Verify value tracking accuracy

  5. Check campaign settings:
     -> Search Partners enabled? Often delivers low-quality traffic -> review
     -> Display expansion enabled? Dilutes search performance -> disable
     -> Audience expansion too broad?

  6. Review competitive landscape:
     -> Auction Insights: new competitors entering?
     -> Seasonality effects?
     -> Industry pricing changes?
```

### 2.6 Low Impression Share

Decision tree:

```
Impression Share too low?

  DIAGNOSE: Budget vs Rank issue
    -> Check "Search Lost IS (Budget)" column
    -> Check "Search Lost IS (Rank)" column

  IF Lost IS (Budget) > 20% -> Budget is the bottleneck:
    -> Campaign profitable? -> Increase budget gradually (15-20%)
    -> Budget fixed? -> Reduce scope: more aggressive negatives,
       focus on best-converting geos/hours, pause high-CPA keywords
    -> Zero impressions after 7+ days? -> Double budget for 24h test

  IF Lost IS (Rank) > 30% -> Quality/bid issue:
    -> QS < 6? -> Optimize QS components
    -> QS >= 6? -> Consider increasing bids
    -> Improve ad relevance and landing page
    -> Add/improve ad extensions

  IF both are low -> Dual problem:
    -> Prioritize QS first, then budget

  Check keyword-level issues:
    -> Low volume keywords -> Broaden match types
    -> Poor relevance -> Align with landing page

  Check account issues:
    -> Product disapprovals -> Fix in Merchant Center
    -> Payment issues -> Contact Google Support
    -> Policy violations -> Review and fix ads
```

---

## 3. Complete Audit Checklist

### Audit frequency:

| Type | Frequency | Duration |
|---|---|---|
| Quick health check | Monthly | 30-60 min |
| Comprehensive audit | Quarterly | 2-4 hours |
| Full strategic audit | Annually or on account takeover | 4-8 hours |

### Common issues by frequency:

| Rank | Issue | Prevalence |
|---|---|---|
| 1 | Broken or missing conversion tracking | 42.3% of accounts |
| 2 | No negative keyword management | 26%+ budget wasted |
| 3 | Wrong bidding strategy for objective | -- |
| 4 | Enhanced CPC not migrated (deprecated early 2025) | -- |
| 5 | Auto-apply recommendations enabled without review | -- |
| 6 | Remarketing tags not firing (audience lists at 0) | -- |
| 7 | Search Partners enabled by default | -- |
| 8 | Display expansion enabled on Search campaigns | -- |
| 9 | No geographic exclusions | -- |
| 10 | Landing page misalignment with ad copy | -- |
| 11 | Keyword cannibalization across campaigns | -- |
| 12 | No ad extensions/assets active | -- |
| 13 | Outdated attribution models (not data-driven) | -- |
| 14 | PMax running without audience signals | -- |
| 15 | AI Max generating irrelevant expanded queries | -- |

### Phase 1 (P0 - CRITICAL): Tracking & Analytics

```
[ ] GA4 properly linked to Google Ads account
[ ] Conversion actions configured correctly
    - Not double-counting
    - Correct attribution model (data-driven recommended)
    - Correct counting method (one per click for leads, every for ecommerce)
    - Primary vs secondary conversion actions defined correctly
[ ] Google Ads tag implemented and firing
[ ] Enhanced Conversions enabled (first-party data)
[ ] Consent Mode v2 implemented (if EU/LGPD markets)
[ ] GCLID auto-tagging enabled
[ ] Cross-domain tracking configured (if applicable)
[ ] Google Tag Manager triggers verified
[ ] Remarketing tags firing correctly
    - CHECK: audience lists have users (NOT 0)
    - Accounts spending $50k/month have been found with remarketing lists
      at 0 users because the tag was not firing
[ ] Offline conversion import configured (if applicable)
[ ] Server-side tagging configured (if maturity allows)
```

IF GA4 data is incomplete or inaccurate, Google Ads automation will optimize on wrong signals. Fix this FIRST.

### Phase 2 (P1): Account Structure

```
[ ] Campaign naming conventions consistent
    - Format: [Type]_[Objective]_[Target]_[Status]
    - Example: Search_LeadGen_Brand_Active
[ ] Campaigns segmented by objective
    - Brand vs non-brand SEPARATED (mandatory)
    - Retargeting vs prospecting SEPARATED
[ ] Ad group structure checked for redundancy
    - Ad groups with same-intent themes, 5-15 keywords each
[ ] No keyword cannibalization between campaigns
    - Check: Search Terms showing same terms in different campaigns
    - Check: Same keywords in multiple campaigns
[ ] Budget-to-performance alignment verified
[ ] Appropriate campaign types for each objective
[ ] No deprecated formats (check for old ETA-only campaigns)
```

### Phase 3 (P1): Keyword Strategy

```
[ ] Keywords mapped to search intent (purchase, comparison, research)
[ ] Match type balance appropriate
    - Exact: control and efficiency
    - Phrase: flexibility
    - Broad: scale (ONLY with Smart Bidding)
[ ] Search Terms report reviewed (last 30-90 days)
    - Terms with spend > 50% CPA target and 0 conversions -> negative
    - Terms with > 3x CPA target and 0 conversions -> negative immediately
[ ] Negative keyword lists comprehensive and current
    - Branded vs non-branded lists separated
    - Applied to Display campaigns as well
    - Shared negative lists exist and are updated
    - IF > 2,000 negatives + Broad/Phrase Match + Smart Bidding:
      may be over-negating. Review and consolidate.
[ ] Duplicate keywords across ad groups/campaigns identified
[ ] Expired seasonal terms removed
[ ] Low-performing keywords paused (high cost, zero conversions)
[ ] Quality Scores reviewed -> target 7+ on key terms
    - QS < 5 = urgent improvement needed
```

### Phase 4 (P1): Ad Creative

```
[ ] All ads are RSAs (no legacy Expanded Text Ads)
[ ] RSAs have 15 headlines + 4 descriptions per ad group
[ ] Ad Strength is "Good" or "Excellent"
    - Improving from "Poor" to "Excellent" yields ~12% more conversions
[ ] Asset performance reviewed
    - "Best" assets -> keep, do not change
    - "Low" assets -> replace with new variations
    - "Learning" assets -> wait 2-4 weeks
[ ] Pin strategy verified (only pin for compliance/branding)
    - Unpinned RSAs perform significantly better
[ ] Ad extensions/assets active:
    - Sitelinks: 4+ with unique landing pages (mandatory)
    - Callout extensions
    - Structured snippets
    - Call extensions (if phone leads are valuable)
    - Location extensions (if applicable)
    - Price extensions (if applicable)
[ ] Ad policy compliance verified (no disapprovals)
[ ] Creative rotation schedule (refresh every 6-8 weeks, Display remarketing every 4-6 weeks)
```

### Phase 5 (P1): Bidding & Budget

```
[ ] Bidding strategy matches campaign objective AND conversion volume
    - < 15 conv/month: Manual CPC
    - 15-30 conv/month: Maximize Conversions
    - 30-50 conv/month: Target CPA or Target ROAS
    - 50-100 conv/month: Target CPA/ROAS + Broad Match
    - 100+ conv/month: Target ROAS + maximum consolidation
[ ] Smart Bidding has sufficient data
    - Minimum 15-30 conversions/month per campaign
    - PMax: 30+ conversions/month per asset group
    - Learning phase requires ~50 conversion events or 3 cycles
[ ] Target CPA/ROAS within 10-20% of historical performance
[ ] Budget pacing on track (not exhausting by noon)
    - Pacing ratio < 0.85 = UNDERPACING -> investigate delivery
    - Pacing ratio 0.85-1.15 = ON TRACK
    - Pacing ratio > 1.15 = OVERPACING -> reduce bids/caps
[ ] Impression Share Lost (Budget) acceptable (< 20% for core campaigns)
[ ] No campaigns stuck in "Learning" status indefinitely
[ ] Enhanced CPC migration complete (deprecated early 2025)
[ ] Budget scaling: max 20% increase at a time
```

### Phase 6 (P1): Landing Pages

```
[ ] No 404 errors or broken destination URLs
[ ] Page speed: LCP < 3 seconds
[ ] Mobile responsive and optimized
[ ] Content aligns with ad copy and keywords
[ ] Clear, compelling CTA above the fold
[ ] Trust signals present (reviews, badges, guarantees)
[ ] Form length appropriate (not too many fields)
[ ] Ad-to-landing-page message match verified
```

### Phase 7 (P2): Audiences & Targeting

```
[ ] Audience segments reviewed and updated
[ ] Audience exclusion lists current
    - Existing customers excluded from acquisition campaigns
    - Converters excluded from retargeting (or reduced bid)
[ ] Remarketing lists have active users (NOT at 0)
[ ] Geographic targeting appropriate
    - Exclude non-converting locations
    - Location option: verify "Presence" vs "Presence or Interest"
[ ] Demographic targeting reviewed
[ ] Audience overlap analyzed
[ ] PMax audience signals configured (high-LTV customers prioritized)
```

### Phase 8 (P1): Automation & Settings

```
[ ] Auto-apply recommendations: ALL DISABLED
[ ] Google Ads recommendations reviewed (not blindly accepted)
[ ] Search Partners setting reviewed (often low-quality traffic)
[ ] Display Network expansion DISABLED on Search campaigns
[ ] Automated rules reviewed for conflicts
[ ] Custom scripts verified after platform changes
[ ] Change history reviewed (identify unauthorized modifications)
[ ] Language targeting correct
[ ] Tracking templates verified and not outdated
```

### Phase 9 (P1): Performance Max Specific

```
[ ] PMax goals aligned with KPIs
[ ] Asset groups have audience signals configured
[ ] Brand exclusions in place (if brand captured elsewhere)
[ ] Campaign-level negative keywords applied (available since Jan 2025, up to 10,000)
[ ] Channel performance reporting reviewed
    - Which channels drive conversions?
    - Are low-quality placements excluded?
[ ] Search term insights monitored for irrelevant queries
[ ] Brand vs non-brand traffic split analyzed
    - Use PMax Brand Traffic Analyzer script to verify true ROAS
[ ] PMax not cannibalizing high-performance Search campaigns
    - Add high-performing Search keywords as negatives in PMax
```

### Post-Audit Implementation Priority

| Category | Impact | Effort | Timeline |
|---|---|---|---|
| Fix broken tracking | HIGH | LOW | Week 1-2 |
| Add negative keywords | HIGH | LOW | Week 1-2 |
| Fix wasted spend | HIGH | MEDIUM | Week 2-3 |
| Account restructuring | HIGH | HIGH | Week 3-4+ |
| New ad copy testing | MEDIUM | LOW | Routine |
| Platform migration | LOW | HIGH | Defer or test limited |

---

## 4. Recommendations Management

### CRITICAL RULE

Disable ALL auto-apply settings:
1. Go to Recommendations tab
2. Select "All Campaigns" view
3. Click "Auto-Apply Settings"
4. Ensure ALL boxes are unchecked

Dismissing recommendations increases Optimization Score identically to accepting them. A low Optimization Score does NOT mean poor performance. Never let score pressure drive decisions.

### SAFE to accept

| Recommendation | Rationale |
|---|---|
| Use Optimized Ad Rotation | Leverages Smart Bidding to prioritize better-performing ads |
| Upgrade Conversion Tracking | Implements data-driven attribution (exception: high-ticket B2B with extended cycles) |
| Remove blocking negatives | Fixes negatives that prevent ads from showing |
| Remove non-serving keywords | Cleans up dead keywords (review first; some may have strategic value) |
| Seller ratings | Shows rating stars in ads, improves CTR |
| Automated locations | Shows business location, safe for local businesses |
| Fix conversion tracking issues | Always prioritize |

### DANGEROUS - REJECT by default

| Recommendation | Risk |
|---|---|
| Add Responsive Search Ads (auto-generated) | Removes control over messaging; auto-created ads go live after 14 days if unchecked |
| Add new keywords / broad match keywords | Irrelevant traffic and wasted spend |
| Remove "redundant" keywords | May discard strategically valuable terms; automated elimination lacks business context |
| Remove conflicting negative keywords | May reintroduce traffic that was excluded intentionally |
| Display expansion | Mixes low-quality Display placements into Search campaigns |
| ALL bidding recommendations | Increases costs without guaranteed ROI; never let Google control bidding without review |
| Increase budgets | Typically delivers more conversions at much worse CPA |
| Loosen CPA/ROAS targets | Nearly always benefits Google's revenue, not advertiser ROI |
| Dynamic sitelinks | May redirect to irrelevant pages; uncontrolled destination selection |
| Improve Responsive Search Ads | Automatic changes without approval |
| Use Optimized Targeting (on remarketing) | Converts pure remarketing into lookalike, diluting audience quality |

### CONDITIONAL - evaluate case by case

| Recommendation | ACCEPT when | REJECT when |
|---|---|---|
| Search Partners | Small accounts with limited campaigns | Large accounts (often lower-quality traffic) |
| Optimized Targeting | Prospecting campaigns | Remarketing campaigns (converts to lookalike) |
| Store visits as goal | Brick-and-mortar businesses | E-commerce only businesses |
| Broad match expansion | Sufficient negative keyword coverage + Smart Bidding active | Limited budget or manual bidding |

### Review protocol

1. Review auto-apply settings monthly without exception
2. Access: Tools & Settings > Recommendations > Auto-apply
3. Disable ALL auto-apply options except those listed as "Safe"
4. Evaluate each recommendation against YOUR business goals, not Google's suggestions
5. Some agency partner programs incentivize high Optimization Scores -- this creates conflicts of interest

---

## 5. Escalation Protocols

### Escalate to human review -- do NOT act autonomously:

| Trigger | Reason |
|---|---|
| Budget change > 30% of current value | Significant financial impact |
| Pause campaign representing > 25% of total spend | Risk of losing critical volume |
| Performance degraded > 30% WoW with no identifiable cause | May be external factors (site down, competition, seasonality) |
| Recommendation to restructure entire account | High-complexity change with learning reset |
| Zero conversions for 72h+ on previously active campaign | Possible tracking, site, or policy issue -- investigate immediately |
| Conflict between advertiser objectives and performance data | Strategic decision, not operational |
| Launch of new campaign type (PMax, Demand Gen) | Requires strategic alignment |

### Pre-action validation checklist

Before executing ANY change, verify:

1. **Sufficient data?** Minimum conversions/clicks for significance (see thresholds per section)
2. **No conflict with recent change?** If a change was made in the last 14 days on the same campaign, wait for learning phase to complete
3. **Safe magnitude?** Budget/bid changes limited to 15-20% per adjustment
4. **Reversible?** Prefer reversible actions (bid adjustments, negatives) over irreversible ones (pause campaign, delete keywords)
5. **Documented?** Record each change with date, reason, and metrics that motivated the action

---

## 6. Conflict Resolution Hierarchy

When contradictory signals appear simultaneously, follow this priority order (highest first):

```
1. Tracking health     -> If conversion tracking is broken, STOP everything until fixed
2. CPA/ROAS health     -> Financial efficiency takes priority over volume
3. Conversion volume   -> Volume growth is only valid if CPA is healthy
4. Impression Share    -> Visibility is secondary to efficiency
```

### Common conflict resolution:

| Conflict | Resolution |
|---|---|
| Lost IS (Budget) high + CPA > target | Prioritize CPA. Do NOT increase budget. First optimize efficiency (negatives, landing pages, QS). Only expand budget when CPA returns to target. |
| CTR high + Conversion Rate low | Prioritize CR. Traffic is arriving but not converting. Investigate landing page, audience quality, and message alignment. |
| QS high + CPA high | Investigate landing page and audience. Good QS means relevance is OK, but the page is not converting or the audience is wrong. |
| Keywords paused + conversion volume falling | Re-evaluate pause. Verify conversion lag was not masking conversions. Consider reactivating with lower bid. |

---

## 7. Key Thresholds Reference Table

| Metric | Threshold | Action |
|---|---|---|
| Quality Score | < 5 | Urgent improvement needed |
| Quality Score | 7+ | Good; maintain |
| CTR (Search) | < 1% | Red flag; review ads immediately |
| CTR (Search) | 3-5%+ | Healthy range |
| CTR (Display) | < 0.5% | Investigate |
| Conversion Rate (Search) | < 1% | Landing page issues |
| Conversion Rate (Search) | 2-5% | Industry average |
| IS Lost (Budget) | > 20% | Needs budget increase (if profitable) |
| IS Lost (Rank) | > 30% | QS or bid issues |
| CPA Target setting | Within 10-20% of historical | Correct range |
| ROAS Target setting | 80% of historical average | Starting point |
| Budget increase | Max 20% at a time | Scaling rule |
| Learning phase | 1-2 weeks minimum | Do not change during this period |
| Conversion lag window | 30+ days for reporting | Minimum wait before optimizing |
| Smart Bidding minimum | 15-30 conversions/month | Required for stability |
| PMax minimum | 30 conversions/month per asset group | Required for optimization |
| Anomaly detection baseline | 28 days | Smooths weekly seasonality |
| Anomaly alert: CTR | > 20% deviation from baseline | Investigate |
| Anomaly alert: CPA | > 25% deviation from baseline | Investigate |
| Anomaly alert: Conv. volume | > 30% deviation from baseline | Investigate |
| Budget pacing: underpace | < 85% of expected | Investigate delivery |
| Budget pacing: overpace | > 115% of expected | Reduce bids/caps |
| Bid adjustment data | 100+ clicks per segment | Minimum for adjustments |
| Bid adjustment conversions | 30+ conversions per segment | Minimum for CPA-based adjustments |
| Offline conversion upload | Within 90 days of click | Google hard limit |
| QS impact on CPA | Each point above 5 | ~16% CPA reduction |
| LP experience improvement | Average to Above Average | 15-30% CPC reduction |
| Keywords per ad group | 5-15 | Split if more, merge if < 15 conv/month |
| Negative keyword limit | 5,000 per list, 20 lists per account | Shared negative lists |
| PMax negatives | Up to 10,000 per campaign | Campaign-level |
| Ad group pause threshold | CPA > 3x target for 30+ days | Or zero conversions after 3x CPA spend |
| Ad group pause threshold | CTR < 1% in Search | Low relevance indicator |
| Creative refresh | Every 6-8 weeks (high volume) | Every 4-6 weeks for remarketing |
| Zero conversions alert | 72h+ on active campaign | Investigate immediately |
