# Sahi Trading App — Comprehensive Cost Breakdown
## Full Investment Analysis for Building a SEBI-Registered Trading App in India

> **Currency:** All amounts in Indian Rupees (INR). USD equivalents approximate at ₹84/$1.  
> **Note:** All figures are estimates based on market research as of 2024–2025. Actual costs vary by vendor, location, and negotiation. Consult CA/CS professionals for current regulatory fee schedules.

---

## Table 1: One-Time Regulatory & Legal Costs (INR)

| Cost Item | Min (₹) | Max (₹) | Notes |
|-----------|---------|---------|-------|
| Company Registration (MCA SPICe+) | 8,000 | 15,000 | Pvt Ltd incorporation incl. DIN, PAN, TAN |
| CS / Legal Professional Fee (incorporation) | 15,000 | 50,000 | Company Secretary firm for drafting MOA/AOA |
| Digital Signature Certificates (3 directors) | 4,500 | 9,000 | Class 3 DSC; eMudhra/Sify |
| SEBI Registration Application Fee | 1,00,000 | 1,50,000 | + 18% GST = ₹1.18L – ₹1.77L |
| NSE Admission Fee — CM Segment | 5,00,000 | 10,00,000 | One-time, non-refundable |
| NSE Admission Fee — F&O Segment | 3,00,000 | 7,00,000 | Separate from CM segment |
| NSE Base Minimum Capital (BMC) — CM | 10,00,000 | 25,00,000 | FDR lock-in with NSE Clearing |
| NSE BMC — F&O Segment | 10,00,000 | 15,00,000 | Additional FDR for F&O |
| NSE Professional Clearing Member (PCM) Deposit | 25,00,000 | 1,00,00,000 | Margin with PCM (refundable) |
| NSE System Audit (SEBI empanelled firm) | 2,00,000 | 5,00,000 | Mandatory before CTCL live |
| BSE Deposit-Based Membership (DBM) Earnest Money | 10,00,000 | 15,00,000 | Refundable earnest money |
| BSE Security Deposit | 25,00,000 | 50,00,000 | FDR with BSE Clearing |
| BSE Admission Fee (CM + F&O) | 2,00,000 | 5,00,000 | One-time |
| MCX Membership Fee (one-time) | 5,00,000 | 8,00,000 | Optional Phase 1; defer to Phase 2 |
| MCX Security Deposit | 10,00,000 | 25,00,000 | FDR with MCX |
| CDSL DP Registration Fee | 1,00,000 | 2,00,000 | Depository Participant admission |
| CDSL Security Deposit | 2,00,000 | 5,00,000 | With CDSL |
| Net Worth Certificate (CA — SEBI empanelled) | 50,000 | 1,00,000 | Must be current (within 3 months) |
| VAPT Security Audit (initial, pre-launch) | 3,00,000 | 6,00,000 | CERT-In empanelled firm mandatory |
| NISM Exam Fees (4 employees × 2 exams) | 40,000 | 80,000 | ₹1,000–₹1,500 per exam attempt |
| Legal counsel — SEBI application support | 2,00,000 | 5,00,000 | Specialist SEBI compliance lawyer |
| Trademark Registration (logo + name, Class 36) | 10,000 | 25,000 | IP India filing; ₹4,500 + professional |
| NSE Co-location Setup (one-time hardware) | 3,00,000 | 8,00,000 | Servers in NSE datacenter for CTCL |
| Office Setup (compliance-grade infrastructure) | 3,00,000 | 10,00,000 | UPS, internet redundancy, CCTV for SEBI inspection |
| **TOTAL REGULATORY & LEGAL (One-Time)** | **~₹1.22 Cr** | **~₹2.98 Cr** | |
| **TOTAL excl. refundable deposits** | **~₹45L** | **~₹90L** | Refundable: PCM + NSE/BSE/MCX FDRs |

> **Note on Capital Lock-In:** A significant portion (₹75L–₹2Cr) is refundable FDR/security deposits with exchanges. This capital is blocked but not spent. Net of deposits, out-of-pocket regulatory cost is ₹45–90 lakhs.

---

## Table 2: Development Costs — Year 1 (INR)

| Item | Min (₹) | Max (₹) | Notes |
|------|---------|---------|-------|
| Android App Development (12 months, 1–2 devs) | 15,00,000 | 30,00,000 | Kotlin specialist(s) |
| iOS App Development (12 months, 1 dev) | 12,00,000 | 24,00,000 | Optional Phase 1; defer to save costs |
| Backend Services — Auth, KYC, Portfolio (12 mo.) | 20,00,000 | 40,00,000 | 2–3 senior backend engineers (Go/Java) |
| **Custom Chart Engine** (specialist work) | 10,00,000 | 25,00,000 | Most technically complex module; may need game dev expertise |
| **OMS (Order Management System)** | 15,00,000 | 35,00,000 | Core trading system; mission-critical reliability |
| **RMS (Risk Management System)** | 8,00,000 | 18,00,000 | Real-time margin, exposure limits, auto-squareoff |
| **Market Data Feed System** (NSE/BSE/MCX tick) | 8,00,000 | 20,00,000 | FIX protocol, Kafka pipeline, WebSocket server |
| KYC Integration (UIDAI/DigiLocker/PAN/Bank) | 3,00,000 | 8,00,000 | Per-call API costs PLUS integration dev cost |
| AI/ML Features (Kyro, 18 AI indicators, sentiment) | 12,00,000 | 35,00,000 | ML engineer + model training + inference infra |
| Option Chain + Strategy Builder | 5,00,000 | 12,00,000 | Greeks calculation, payoff graph engine |
| Market Scanners (20+ real-time scanners) | 3,00,000 | 8,00,000 | Scanner rule engine, filter logic |
| Push Notification Service (FCM + alert engine) | 1,00,000 | 3,00,000 | Alert scheduling, delivery pipeline |
| Admin Panel (broker back-office) | 3,00,000 | 8,00,000 | Client management, KYC review, compliance reports |
| QA Engineering & Test Automation | 5,00,000 | 12,00,000 | Unit + integration + load testing |
| UI/UX Design (Figma, animations, design system) | 4,00,000 | 10,00,000 | Designer cost for 12 months |
| DevOps & Infrastructure as Code (Terraform, K8s) | 5,00,000 | 12,00,000 | Setup + ongoing automation |
| Third-Party Library/SDK Licenses | 1,00,000 | 3,00,000 | FIX engine license (if commercial), analytics SDKs |
| Security Implementation (SSL pinning, encryption) | 1,00,000 | 3,00,000 | Specialized security review |
| **TOTAL DEVELOPMENT (Year 1)** | **~₹1.31 Cr** | **~₹3.06 Cr** | |

> **Tip:** Open-source FIX engine (QuickFIX/Go) reduces licensing cost but requires experienced engineers. Commercial FIX engines (Rapid Addition, QuantHouse) cost ₹10–50 lakhs/year but reduce dev time.

---

## Table 3: Annual Recurring Infrastructure Costs (INR/Year)

### 3A: Cloud Infrastructure (AWS Mumbai)

| Infrastructure Component | MVP Stage (₹/yr) | Growth Stage (₹/yr) | Notes |
|--------------------------|-----------------|--------------------|----|
| EKS (Kubernetes) — compute | 3,60,000 | 60,00,000 | 3×t3.xlarge MVP → 20×c6i.2xlarge at scale |
| RDS PostgreSQL (Multi-AZ) | 1,80,000 | 12,00,000 | db.t3.large MVP → db.r6g.4xlarge at scale |
| ElastiCache Redis (cluster) | 1,20,000 | 8,40,000 | cache.t3.medium → cache.r6g.large cluster |
| Timescale / ScyllaDB (EC2) | 1,20,000 | 18,00,000 | 2×c6i.large → 6×c6i.4xlarge HA cluster |
| Amazon MSK (Kafka) | 1,20,000 | 9,60,000 | 3-broker small → 9-broker large cluster |
| Application Load Balancer + WAF | 60,000 | 3,60,000 | Traffic volume dependent |
| S3 (KYC documents + assets) | 12,000 | 2,40,000 | Storage + requests |
| CloudFront CDN | 24,000 | 3,60,000 | Data transfer dependent |
| AWS GuardDuty + Security Hub | 24,000 | 1,20,000 | Security compliance |
| CloudWatch + Logs | 24,000 | 3,60,000 | Retention + ingestion |
| Bandwidth / Data Transfer | 60,000 | 12,00,000 | WebSocket + REST outbound |
| NAT Gateway | 24,000 | 1,20,000 | Outbound private subnet |
| **AWS Sub-Total** | **~₹11L/yr** | **~₹1.36Cr/yr** | |

### 3B: Exchange & Market Data Fees

| Fee Item | Min (₹/yr) | Max (₹/yr) | Notes |
|----------|-----------|-----------|-------|
| NSE Market Data Feed — Level 1 (Best bid/ask) | 3,75,000 | 6,00,000 | Approx. ₹31,250–₹50,000/month |
| NSE Market Data Feed — Level 2 (Full order book) | 18,00,000 | 35,00,000 | Required for depth; charged per segment |
| NSE Annual Subscription (CM Segment) | 60,000 | 1,00,000 | Annual renewal |
| NSE Annual Subscription (F&O Segment) | 60,000 | 1,00,000 | |
| BSE Annual Subscription | 50,000 | 1,50,000 | Per segment |
| MCX Annual Subscription + Data | 2,00,000 | 5,00,000 | Commodity segment |
| NSE Co-location Rack (annual) | 3,00,000 | 8,00,000 | Physical rack rental in NSE datacenter |
| Exchange Connectivity (leased lines) | 1,20,000 | 3,60,000 | Dedicated lines to NSE/BSE |
| **Exchange & Data Sub-Total** | **~₹29.65L/yr** | **~₹61.1L/yr** | |

### 3C: Third-Party SaaS & APIs

| Service | Min (₹/yr) | Max (₹/yr) | Notes |
|---------|-----------|-----------|-------|
| Sentry (crash monitoring, Pro plan) | 1,20,000 | 3,60,000 | Business plan for team + quotas |
| Firebase (FCM notifications) | 0 | 1,20,000 | Spark (free) → Blaze (pay as you go) |
| SMS Gateway — OTP (Msg91 / AWS SNS) | 60,000 | 3,00,000 | ₹0.15–₹0.25 per OTP; 100k–500k OTPs/month |
| DigiLocker / Aadhaar KYC API | 1,00,000 | 3,00,000 | Per KYC completed; ~₹15–₹25/user |
| PAN Verification API (NSDL/Surepass) | 30,000 | 1,00,000 | ₹3–₹5 per verification |
| Bank Penny Drop (Razorpay/Cashfree) | 30,000 | 1,00,000 | ₹3–₹5 per verification |
| CKYC Registry API | 50,000 | 1,50,000 | Per-check + per-upload |
| Face Match / Liveness (Hyperverge/AWS Rekognition) | 50,000 | 2,00,000 | Per KYC image processed |
| UPI Payment Gateway (Razorpay / Cashfree) | 60,000 | 3,00,000 | MDR on deposits (0.5–2%) or flat fee |
| Domain & SSL Certificate (Wildcard) | 20,000 | 60,000 | Domain renewal + Cloudflare/DigiCert SSL |
| Intercom / Freshdesk (customer support CRM) | 1,20,000 | 4,80,000 | Per agent seat, per month |
| Datadog / Grafana Cloud (observability) | 1,20,000 | 6,00,000 | Infrastructure + APM metrics |
| PagerDuty / OpsGenie (alerting) | 60,000 | 2,40,000 | On-call management |
| LaunchDarkly / Firebase Remote Config (feature flags) | 0 | 2,40,000 | Firebase free; LaunchDarkly Pro ₹2L+ |
| Google Play Store Developer Account | 7,500 | 7,500 | One-time ₹7,500 (included here annually) |
| Apple App Store Developer Program | 7,500 | 8,500 | $99/year |
| CDSL DP Back-Office Software (SaaS) | 2,00,000 | 5,00,000 | Annual licence for DP operations software |
| **SaaS & APIs Sub-Total** | **~₹10.35L/yr** | **~₹40.65L/yr** | |

### 3D: Compliance & Legal Recurring

| Item | Min (₹/yr) | Max (₹/yr) | Notes |
|------|-----------|-----------|-------|
| VAPT Security Audits (quarterly × 4) | 8,00,000 | 20,00,000 | CERT-In empanelled, SEBI mandatory |
| Annual System Audit (SEBI empanelled CA firm) | 2,00,000 | 4,00,000 | Mandatory for trading members |
| Legal Retainer (SEBI compliance lawyer) | 2,40,000 | 6,00,000 | ₹20k–₹50k/month |
| CA Retainer (net worth, financials, GST) | 1,20,000 | 3,60,000 | ₹10k–₹30k/month |
| SEBI Annual Turnover Fee | Variable | Variable | ~₹2 per ₹1 crore of client turnover |
| Exchange Annual Transaction Charges | Variable | Variable | Charged per trade executed |
| FIU-IND (PMLA compliance software) | 60,000 | 2,00,000 | Reporting tool subscription |
| SEBI Investor Education Fund Contribution | Variable | Variable | % of brokerage; mandatory |
| **Compliance Sub-Total** | **~₹14.2L/yr** | **~₹35.6L/yr** | |

### Summary — Total Annual Recurring Costs

| Category | MVP Stage (₹/yr) | Growth Stage (₹/yr) |
|----------|-----------------|---------------------|
| Cloud Infrastructure (AWS) | ₹11L | ₹1.36 Cr |
| Exchange & Market Data | ₹29.65L | ₹61.1L |
| Third-Party SaaS & APIs | ₹10.35L | ₹40.65L |
| Compliance & Legal | ₹14.2L | ₹35.6L |
| **GRAND TOTAL** | **~₹65L/yr** | **~₹2.73 Cr/yr** |

---

## Table 4: Team Salaries (Monthly, INR) — Full In-House Team

| Role | Min (₹/month) | Max (₹/month) | Annual (Min) | Annual (Max) | Notes |
|------|--------------|--------------|-------------|-------------|-------|
| CTO / VP Engineering | 3,00,000 | 8,00,000 | ₹36L | ₹96L | Most critical hire; fintech/HFT background |
| Senior Android Developer (Kotlin) | 1,50,000 | 3,50,000 | ₹18L | ₹42L | Custom view + chart engine expertise |
| Senior iOS Developer (Swift) | 1,50,000 | 3,50,000 | ₹18L | ₹42L | Phase 2; defer if budget constrained |
| Senior Backend Engineer — Go/Java (×2) | 2,00,000 | 4,00,000 | ₹48L | ₹96L | Each; OMS/RMS/feed expertise |
| DevOps / SRE Engineer | 1,20,000 | 2,80,000 | ₹14.4L | ₹33.6L | AWS, K8s, Kafka expert |
| Data / ML Engineer | 1,50,000 | 3,50,000 | ₹18L | ₹42L | Market data pipeline + AI features |
| QA Engineer (Automation) | 70,000 | 1,60,000 | ₹8.4L | ₹19.2L | Espresso, Appium, load testing |
| UI/UX Designer | 80,000 | 2,00,000 | ₹9.6L | ₹24L | Figma + motion design |
| Compliance Officer (CS/MBA) | 50,000 | 1,50,000 | ₹6L | ₹18L | NISM certified; SEBI filings |
| Customer Support Executive (×2) | 30,000 | 60,000 | ₹7.2L | ₹14.4L | Each; trading support knowledge |
| Product Manager | 1,00,000 | 2,50,000 | ₹12L | ₹30L | Fintech PM with trading background |
| Marketing Manager | 60,000 | 1,50,000 | ₹7.2L | ₹18L | Digital + community marketing |
| **TOTAL TEAM — MONTHLY** | **~₹18.1L** | **~₹40.5L** | | | |
| **TOTAL TEAM — ANNUAL** | **~₹2.17 Cr** | **~₹4.86 Cr** | | | Incl. PF, gratuity, health insurance |

> **Employer's Additional Burden:** Add 20–25% to gross salary for PF (12%), gratuity (4.81%), health insurance, and leave encashment. Actual annual cost per employee = salary × 1.22–1.25.

---

## Table 5: Marketing & User Acquisition (Annual INR)

| Channel | Phase 1 (₹/yr) | Phase 2 (₹/yr) | Notes |
|---------|---------------|---------------|-------|
| Google Search Ads (fintech keywords) | 6,00,000 | 30,00,000 | High CPC; target "best trading app" keywords |
| Meta/Instagram Ads (financial audience) | 4,00,000 | 20,00,000 | Video ads showcasing Scalper 2.0 |
| YouTube Ads + Creator Sponsorships | 3,00,000 | 15,00,000 | Trading YouTubers (CA Rachana Phadke, etc.) |
| Twitter/X Financial Community | 1,00,000 | 5,00,000 | Organic + promoted posts |
| Referral Program (cash incentive per account) | 5,00,000 | 20,00,000 | ₹200–₹500 per activated referred account |
| Content Marketing & SEO (blog, Academy) | 2,00,000 | 8,00,000 | Trading education articles; compound long-term |
| Webinars & Live Trading Sessions | 1,00,000 | 5,00,000 | YouTube Live + Zoom webinars |
| Influencer Partnerships (Twitter/YouTube) | 3,00,000 | 15,00,000 | Paid feature reviews, affiliate |
| App Store Optimization (ASO) | 30,000 | 1,00,000 | Keywords, screenshots, A/B testing |
| Trading community events & meetups | 1,00,000 | 4,00,000 | NSE/BSE investor meets, trader summits |
| PR & Media outreach (ET, Mint, MoneyControl) | 50,000 | 3,00,000 | Press release distribution, journalist relations |
| Brand partnerships (TradingView community, etc.) | 2,00,000 | 8,00,000 | Co-marketing with trading tools |
| **TOTAL MARKETING** | **~₹28.8L/yr** | **~₹1.34 Cr/yr** | |

> **Unit Economics Target:** Customer Acquisition Cost (CAC) < ₹500/active trader. Lifetime Value (LTV) of an active F&O trader at ₹10/order × 20 orders/day × 250 trading days = ₹50,000/year in brokerage. LTV:CAC ratio target: >30x.

---

## Table 6: Total Capital Required — Year-by-Year Summary

| Investment Category | Year 1 (Min) | Year 1 (Max) | Year 2 (Min) | Year 2 (Max) |
|---------------------|-------------|-------------|-------------|-------------|
| One-Time Regulatory & Legal | ₹45L | ₹90L | ₹2L | ₹5L |
| Refundable Exchange Deposits (blocked capital) | ₹75L | ₹1.95 Cr | ₹0 | ₹0 |
| Development (team + contractors) | ₹1.31 Cr | ₹3.06 Cr | ₹60L | ₹1.5 Cr |
| Team Salaries (Year 1 full, Year 2 ongoing) | ₹2.17 Cr | ₹4.86 Cr | ₹2.5 Cr | ₹6 Cr |
| Infrastructure (AWS + Exchange) | ₹40L | ₹80L | ₹1 Cr | ₹3 Cr |
| Compliance & Legal (recurring) | ₹14L | ₹36L | ₹18L | ₹45L |
| Marketing & Acquisition | ₹15L | ₹50L | ₹50L | ₹2 Cr |
| **TOTAL (excl. refundable deposits)** | **~₹4.22 Cr** | **~₹9.68 Cr** | **~₹4.8 Cr** | **~₹13 Cr** |
| **TOTAL (incl. refundable deposits)** | **~₹4.97 Cr** | **~₹11.63 Cr** | | |

### Minimum Viable Funding Requirement

| Stage | Amount | Purpose |
|-------|--------|---------|
| Seed (Month 0) | ₹3–5 Crore | Regulatory deposits + initial team (6 months) |
| Series A (Month 6) | ₹10–25 Crore | Scale team, marketing, infrastructure |
| Breakeven Point | ~₹15–25 Crore revenue | With 5,000+ active daily traders |

---

## Table 7: Alternative — Partner/White-Label Model (No Own SEBI License)

Instead of becoming a SEBI-registered broker yourself, you can build a trading terminal/front-end on top of an established broker's API. This is the **fastest and cheapest path** to market.

| Item | Cost | Notes |
|------|------|-------|
| Development (front-end Android + backend integration) | ₹25L – ₹80L | Smaller scope; no OMS/RMS/exchange connectivity needed |
| Team (smaller — 3–5 people) | ₹8L – ₹20L/month | No compliance officer or data engineer needed |
| Broker API License | ₹0 – ₹5L | Most broker APIs free; some charge platform fee |
| Infrastructure (no exchange feed servers) | ₹25K – ₹2L/month | Just app servers; broker provides data |
| Regulatory Barrier | **None** | You're not the broker — piggybacking on existing SEBI license |
| VAPT / Compliance | Minimal | Broker handles regulatory compliance; you do basic app security |
| **Realistic Total Year 1** | **₹1.5 – 3.5 Crore** | vs ₹5–12 Crore for full broker path |
| Time to Market | **3–6 months** | vs 12–18 months for full broker registration |

### Broker APIs Available for Integration

| Broker | API Name | Brokerage Model | Notable Features |
|--------|----------|----------------|-----------------|
| Zerodha | Kite Connect API | ₹2,000/month developer fee; ₹0–₹20/order for clients | Most popular, reliable |
| Dhan | Dhan API | Revenue sharing on brokerage | Commodity + equity |
| Shoonya (Finvasia) | Shoonya API | Zero brokerage; API free | Growing ecosystem |
| Fyers | Fyers API | ₹500–₹1,000/month | Historical data access |
| Alice Blue | ANT API | Revenue sharing | Good data quality |
| Upstox | Upstox API v3 | Revenue sharing | Backed by Ratan Tata |

**Limitation of Partner Model:**
- You cannot set your own brokerage (bound by the broker's pricing)
- Less control over execution quality and reliability
- Brand perception: users know you're built on another broker
- Revenue sharing reduces margins (you get 20–40% of brokerage collected)
- Broker can revoke API access (business risk)

---

## Table 8: NSE Market Data Feed — Detailed Pricing

| Data Feed Tier | Annual Cost (₹) | What You Get |
|---------------|----------------|-------------|
| Level 1 — Best Bid/Ask only | ₹3.75L – ₹6L | LTP, best bid, best ask; sufficient for basic watchlist |
| Level 2 — Full order book (20 levels) | ₹18L – ₹35L | Full depth of market; needed for advanced charts |
| Tick-by-Tick (all trades) | ₹35L – ₹60L+ | Every trade printed; needed for volume profile, footprint charts |
| Index Data (Nifty, BankNifty, etc.) | Bundled with CM feed | |
| F&O Data | Separate segment fee | Required for option chain |
| Historical OHLC Data (EOD) | ₹1L – ₹3L/yr | End-of-day; lower cost |
| Historical Tick-by-Tick (3 years) | ₹10L – ₹25L | One-time purchase |

> **NSE Vendor Access:** Alternatively, buy Level 2 data from an NSE-authorized data vendor (e.g., Globe Data Services, InfraComm) which may be cheaper (₹5–15L/year) but adds intermediary dependency and latency.

---

## Table 9: VAPT Mandatory Schedule & Costs

| Audit Type | Frequency | Cost (₹) | Requirement Source |
|-----------|-----------|---------|-------------------|
| Full VAPT (Web + Mobile + API + Network) | Quarterly (4×/year) | ₹2L – ₹5L per audit | SEBI Circular ITD/2023 |
| Mobile App Penetration Test | Quarterly | Included in Full VAPT | |
| Source Code Review (SAST) | Annual or with major release | ₹1L – ₹3L | Best practice |
| Vendor/Third-Party Risk Assessment | Annual | ₹50K – ₹2L | RBI/SEBI guidance |
| DR (Disaster Recovery) Drill | Quarterly | Internal cost only | Exchange mandate |
| Business Continuity Plan (BCP) Review | Annual | ₹50K – ₹1L (consultant) | SEBI |
| **Total Annual VAPT Spend** | | **₹8L – ₹20L/year** | |

**CERT-In Empanelled Vendors (Recommended):**
- Deloitte India
- KPMG India
- EY India
- Lucideus (Safe Security)
- Suma Soft
- Sattrix Information Security

> **Critical:** SEBI can suspend trading member operations for non-compliance with VAPT mandates. Do NOT skip or defer.

---

## Table 10: Compliance Reporting Obligations Calendar

| Report | Frequency | Submitted To | Notes |
|--------|-----------|-------------|-------|
| Net Position Report | Monthly | NSE / BSE | Client segment-wise positions |
| Margin Utilization Report | Daily (auto) | Exchange | Real-time margin monitoring |
| Client Funding Report | Monthly | NSE | Funds held with broker |
| Investor Grievance Report | Monthly | SEBI / Exchange | Complaints + resolution time |
| Suspicious Transaction Report (STR) | As needed | FIU-IND | PMLA mandate; within 7 days |
| System Audit Report | Annual | Exchange | SEBI empanelled auditor |
| VAPT Report | Quarterly | Exchange | CERT-In empanelled vendor |
| Half-Yearly Net Worth Certificate | Every 6 months | NSE / SEBI | CA certified |
| Annual Report (SEBI Annual Return) | Annual | SEBI | Audited financials + compliance |
| GST Returns (GSTR-1, GSTR-3B) | Monthly | GST Portal | Standard GST compliance |
| TDS Filings | Quarterly | Income Tax | On salary, professional fees |
| CDSL DP Compliance Report | Monthly | CDSL | DP operations summary |
| CKYC Uploads | As KYC completed | CKYC Registry | Within 10 days of account opening |

---

## Cost Optimization Strategies

### 1. Defer iOS to Phase 2
- Save ₹12–24 lakhs in Year 1 development
- Android covers 73%+ of Indian smartphone users
- Launch iOS at Month 10+ once Android app is stable

### 2. Use Managed Services over Self-Hosted
- Amazon RDS vs self-managed PostgreSQL: adds ₹1–3L/year but saves 1 DBA (saves ₹15–25L/year)
- Amazon MSK vs self-managed Kafka: similar trade-off

### 3. Start with PCM (Professional Clearing Member) vs Self-Clearing
- Self-clearing requires ₹50+ Crore additional net worth. Not feasible at launch.
- PCM costs 0.01–0.05% of turnover — acceptable at MVP scale.

### 4. Co-Locate Only for Order Routing; Use AWS for Everything Else
- NSE co-location (₹3–8L/year) only needed for the FIX order gateway server
- All other services (auth, market data WebSocket, API) run on AWS Mumbai

### 5. Outsource Non-Core Functions in Year 1
- Customer support: outsource to BPO at ₹15K/agent/month vs ₹30K in-house
- QA: outsource regression testing to QA firm at ₹2–4L/month
- Legal/compliance: retain a law firm vs hire full-time lawyer

### 6. Open-Source Where Possible
- QuickFIX/Go (FIX engine): free vs ₹10–50L for commercial
- Grafana + Prometheus (monitoring): free vs ₹6L+/year for Datadog Enterprise
- PostgreSQL + TimescaleDB: free vs ₹20L+/year for commercial time-series DB

---

## Break-Even Analysis

**Revenue Model Assumptions:**
- Average active trader: 10 orders/day, ₹10/order = ₹100/day brokerage
- Trading days/year: 250
- Revenue per active trader per year: ₹25,000

**Break-Even Calculation:**

| Monthly Operating Cost | Amount |
|------------------------|--------|
| Team (10 people) | ₹25,00,000 |
| Infrastructure | ₹8,00,000 |
| Exchange/data fees | ₹5,00,000 |
| Compliance | ₹3,00,000 |
| Marketing | ₹10,00,000 |
| **Total Monthly Burn** | **₹51,00,000** |

**Active Traders Needed for Break-Even:**
- Monthly revenue needed: ₹51 lakhs
- Revenue per trader/month: ₹2,083 (₹25,000/12)
- **Break-Even: ~2,450 consistently active traders**

**Industry Context:**
- Zerodha has ~7 million active clients
- Dhan: ~700K+
- A new broker realistically acquires 10,000–50,000 active traders in Year 1–2 with ₹1–3 Cr marketing spend
- At 10,000 active traders: ₹2.08 Cr/month revenue = profitable at MVP operating cost level
