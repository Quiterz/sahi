# Sahi Trading App — Complete Cost Breakdown
## Building a SEBI-Registered Trading App Like Sahi

> All costs in Indian Rupees (INR) unless noted. Figures are estimated ranges for 2025-2026.  
> Exchange rates used: 1 USD ≈ ₹84

---

## Phase-Wise Total Investment Summary

| Phase | Category | Min (₹) | Max (₹) | When |
|-------|---------|---------|---------|------|
| Phase 1 | Legal & Regulatory | 45,00,000 | 90,00,000 | Month 1–4 |
| Phase 2 | Product Design & Planning | 4,00,000 | 10,00,000 | Month 1–2 |
| Phase 3 | Team Hiring (Year 1) | 2,16,00,000 | 4,56,00,000 | Month 1–12 |
| Phase 4 | Infrastructure Setup (Year 1) | 3,00,000 | 8,40,000 | Month 3–12 |
| Phase 5–6 | Backend + Exchange Dev | 60,00,000 | 1,30,00,000 | Month 3–10 |
| Phase 7 | Android App Development | 25,00,000 | 60,00,000 | Month 4–10 |
| Phase 8 | Testing & QA | 8,00,000 | 20,00,000 | Month 9–11 |
| Phase 9 | App Store + Launch | 1,50,000 | 4,00,000 | Month 11–12 |
| Phase 10 | Marketing (Year 1) | 29,00,000 | 1,38,00,000 | Month 10–12 |
| | **GRAND TOTAL YEAR 1** | **~₹3.9 Cr** | **~₹8.1 Cr** | |

> **Note:** This assumes a full SEBI-registered broker with self-clearing. The "alternative approach" (partner model) brings this down to ₹1.5–3.5 Cr.

---

## TABLE 1 — One-Time Regulatory & Legal Costs

| Cost Item | Min (₹) | Max (₹) | Refundable? | Notes |
|-----------|---------|---------|------------|-------|
| Company Registration (MCA, Pvt Ltd) | 8,000 | 15,000 | No | Includes govt fees + CA/CS |
| SEBI Registration Application Fee | 1,00,000 | 1,50,000 | No | + 18% GST |
| SEBI Registration Processing | 5,00,000 | 8,00,000 | No | Legal/CA assistance |
| NSE Admission Fee (CM Segment) | 5,00,000 | 10,00,000 | Partially | Membership deposit |
| NSE Admission Fee (F&O Segment) | 3,00,000 | 7,00,000 | Partially | |
| NSE Base Minimum Capital (BMC) | 10,00,000 | 25,00,000 | Yes (on exit) | FDR / BG required |
| BSE DBM Earnest Money Deposit | 1,00,000 | 1,00,000 | No | Non-refundable with app |
| BSE Deposit Based Membership | 9,00,000 | 14,00,000 | Yes (on exit) | |
| BSE Admission/Processing Fee | 50,000 | 1,00,000 | No | + GST |
| MCX Membership Fee | 5,00,000 | 8,00,000 | Partially | Optional initially |
| MCX Base Capital | 3,00,000 | 5,00,000 | Yes (on exit) | |
| CDSL DP Registration | 1,00,000 | 2,00,000 | Partially | |
| CDSL Annual Connectivity Fee | 50,000 | 1,00,000 | No | Per year |
| Net Worth Certificate (CA) | 50,000 | 1,00,000 | No | From SEBI-registered CA |
| VAPT Audit (CERT-in empaneled firm) | 2,00,000 | 6,00,000 | No | Initial pre-launch audit |
| Legal counsel + SEBI compliance setup | 2,00,000 | 5,00,000 | No | Law firm retainer |
| KYC Registration Agency (KRA) setup | 25,000 | 50,000 | No | CVL/NDML KRA empanelment |
| GST Registration | 5,000 | 10,000 | No | |
| Office setup (registered address) | 1,00,000 | 5,00,000 | No | SEBI requires physical inspection |
| **SUBTOTAL** | **₹49.88 L** | **₹1.00 Cr** | | |

---

## TABLE 2 — Development Costs (One-Time, Year 1)

| Item | Min (₹) | Max (₹) | Tech Stack | Duration |
|------|---------|---------|-----------|---------|
| Android App (MVP features) | 15,00,000 | 30,00,000 | Kotlin | 6 months |
| Android App (Advanced: scalper, AI, options) | 10,00,000 | 20,00,000 | Kotlin | +4 months |
| iOS App (optional Phase 1) | 12,00,000 | 25,00,000 | Swift | 6 months |
| Web Trading Platform (browser) | 15,00,000 | 35,00,000 | React/Next.js | 8 months |
| Backend — Auth + KYC Service | 5,00,000 | 12,00,000 | Go | 2 months |
| Backend — Market Data WebSocket Service | 8,00,000 | 18,00,000 | Go | 3 months |
| Backend — OMS (Order Management System) | 12,00,000 | 28,00,000 | Go/Java | 4 months |
| Backend — RMS (Risk Management System) | 5,00,000 | 12,00,000 | Go | 2 months |
| Backend — Portfolio + Funds Service | 4,00,000 | 8,00,000 | Go/Node | 2 months |
| Backend — Notification Service | 1,50,000 | 4,00,000 | Node.js | 1 month |
| Custom Chart Engine (Android) | 10,00,000 | 25,00,000 | Kotlin/Canvas | 4 months |
| Option Chain + Strategy Builder | 6,00,000 | 15,00,000 | Kotlin | 2 months |
| Scalper Terminal (advanced UI) | 8,00,000 | 20,00,000 | Kotlin | 3 months |
| Scanner Engine (20+ real-time scanners) | 5,00,000 | 12,00,000 | Backend | 2 months |
| AI/ML Indicators (18 built-in indicators) | 8,00,000 | 20,00,000 | Python | 3 months |
| Kyro — Natural language indicator builder | 4,00,000 | 12,00,000 | Python + LLM API | 2 months |
| Exchange Connectivity (NSE CTCL/FIX) | 8,00,000 | 20,00,000 | C++/Go | 3 months |
| Exchange Connectivity (BSE BOLT) | 4,00,000 | 10,00,000 | | 2 months |
| Exchange Connectivity (MCX CTCL) | 3,00,000 | 8,00,000 | | 2 months |
| Admin Panel + Operations Dashboard | 4,00,000 | 10,00,000 | React | 2 months |
| DevOps — CI/CD, IaC, monitoring setup | 3,00,000 | 8,00,000 | | 2 months |
| QA — Test automation, load testing | 4,00,000 | 10,00,000 | | Ongoing |
| UI/UX Design (all screens, design system) | 4,00,000 | 10,00,000 | Figma | 3 months |
| **SUBTOTAL (own license broker)** | **₹1.54 Cr** | **₹3.72 Cr** | | |
| **SUBTOTAL (partner API model)** | **₹40 L** | **₹1.20 Cr** | | Less OMS/RMS/Exchange |

---

## TABLE 3 — Team Salaries (Monthly, INR)

| Role | Min/month (₹) | Max/month (₹) | Annual Min (₹) | Annual Max (₹) |
|------|--------------|--------------|---------------|---------------|
| CTO / VP Engineering | 3,00,000 | 8,00,000 | 36,00,000 | 96,00,000 |
| Senior Android Developer | 1,50,000 | 3,00,000 | 18,00,000 | 36,00,000 |
| Senior iOS Developer | 1,50,000 | 3,00,000 | 18,00,000 | 36,00,000 |
| Senior Backend Engineer (Go) × 2 | 2,40,000 | 5,00,000 | 28,80,000 | 60,00,000 |
| DevOps/Infrastructure Engineer | 1,20,000 | 2,50,000 | 14,40,000 | 30,00,000 |
| ML/Data Engineer (AI features) | 1,50,000 | 3,00,000 | 18,00,000 | 36,00,000 |
| Exchange Integration Engineer | 1,50,000 | 3,50,000 | 18,00,000 | 42,00,000 |
| QA Engineer | 70,000 | 1,50,000 | 8,40,000 | 18,00,000 |
| UI/UX Designer | 80,000 | 2,00,000 | 9,60,000 | 24,00,000 |
| Compliance Officer (NISM certified) | 50,000 | 1,25,000 | 6,00,000 | 15,00,000 |
| Customer Support × 2 | 40,000 | 80,000 | 9,60,000 | 19,20,000 |
| Business Development / Marketing | 80,000 | 2,00,000 | 9,60,000 | 24,00,000 |
| **TOTAL MONTHLY** | **~₹15.3 L** | **~₹35.5 L** | | |
| **TOTAL ANNUAL (12 months)** | | | **₹1.84 Cr** | **₹4.26 Cr** |

> Team size grows with user base. Year 1 team: ~10–12 people. Year 2: 20–30 people.

---

## TABLE 4 — Annual Recurring Infrastructure Costs (AWS, India Region)

### Stage A: MVP (0–20K active users)
| Service | Monthly (₹) | Annual (₹) |
|---------|------------|-----------|
| EC2 (API servers, 2 × m6i.xlarge) | 30,000 | 3,60,000 |
| RDS PostgreSQL (db.r6g.large, Multi-AZ) | 18,000 | 2,16,000 |
| ElastiCache Redis (cache.r6g.large) | 12,000 | 1,44,000 |
| EKS cluster (managed) | 12,000 | 1,44,000 |
| S3 + CloudFront (storage + CDN) | 5,000 | 60,000 |
| Application Load Balancer | 3,500 | 42,000 |
| VPC + NAT Gateway | 4,000 | 48,000 |
| CloudWatch Logs + Monitoring | 3,000 | 36,000 |
| AWS Shield Standard | 0 | 0 |
| Data transfer (egress) | 8,000 | 96,000 |
| **Monthly Total** | **~₹95.5K** | |
| **Annual Total** | | **~₹11.5 L** |
| **+ GST 18%** | | **~₹13.6 L** |

### Stage B: Growth (100K–500K active users)
| Service | Monthly (₹) | Annual (₹) |
|---------|------------|-----------|
| EC2 + EKS (auto-scaling, 10–30 nodes) | 3,00,000 | 36,00,000 |
| RDS PostgreSQL (Multi-AZ, r6g.4xlarge) | 1,20,000 | 14,40,000 |
| ElastiCache Redis Cluster (6 nodes) | 80,000 | 9,60,000 |
| TimescaleDB / ScyllaDB (time-series) | 60,000 | 7,20,000 |
| Kafka (MSK, 3 brokers) | 40,000 | 4,80,000 |
| CloudFront CDN (high traffic) | 50,000 | 6,00,000 |
| WAF + Shield Advanced | 1,60,000 | 19,20,000 |
| Data egress (WebSocket heavy) | 2,00,000 | 24,00,000 |
| Dedicated WebSocket servers | 1,00,000 | 12,00,000 |
| **Monthly Total** | **~₹11 L** | |
| **Annual Total** | | **~₹1.33 Cr** |
| **+ GST 18%** | | **~₹1.57 Cr** |

---

## TABLE 5 — Annual Recurring Regulatory & Compliance Costs

| Item | Annual Min (₹) | Annual Max (₹) | Notes |
|------|---------------|---------------|-------|
| NSE Annual Subscription (CM + F&O) | 2,00,000 | 5,00,000 | Per segment |
| BSE Annual Subscription | 1,00,000 | 2,50,000 | |
| MCX Annual Subscription | 80,000 | 1,50,000 | |
| NSE Market Data Feed (Level 1) | 3,75,000 | 10,00,000 | Included with CTCL or separate |
| NSE Market Data Feed (Level 2 / full depth) | 15,00,000 | 35,00,000 | For advanced features |
| CDSL Annual Connectivity/DP Fee | 50,000 | 1,00,000 | |
| SEBI Turnover Fee | Variable | Variable | ₹10/crore of turnover |
| VAPT Quarterly Audits (4 × ₹2.5L avg) | 8,00,000 | 20,00,000 | CERT-in certified firms |
| Legal / Compliance Retainer | 3,00,000 | 8,00,000 | Law firm + CA |
| Insurance (cyber liability, E&O) | 1,00,000 | 3,00,000 | Recommended |
| KRA Annual Fee | 25,000 | 50,000 | |
| SEBI Inspection readiness | 1,00,000 | 3,00,000 | Documentation, audits |
| **Annual Total (minimal segment)** | **~₹40 L** | |
| **Annual Total (full segments)** | | **~₹89 L** |

---

## TABLE 6 — Third-Party Services Annual Costs

| Service | Provider | Annual Min (₹) | Annual Max (₹) |
|---------|---------|---------------|---------------|
| Sentry (crash monitoring) | Sentry.io | 1,20,000 | 3,60,000 |
| SMS OTP Gateway | Msg91 / Twilio | 60,000 | 3,00,000 |
| Firebase (push notifications) | Google | 0 | 1,20,000 |
| Digilocker / Aadhaar KYC | IDfy / Hyperverge | 3,00,000 | 10,00,000 |
| PAN Verification API | Razorpay/Cashfree | 50,000 | 2,00,000 |
| Bank Penny Drop API | Razorpay/Cashfree | 30,000 | 1,00,000 |
| Video KYC (IPV) | IDfy | 2,00,000 | 8,00,000 |
| Payment Gateway (UPI) | Razorpay | 0 | 50,000 |
| Customer Support (Intercom/Freshdesk) | | 1,20,000 | 4,80,000 |
| Domain + SSL certificates | | 20,000 | 60,000 |
| Play Store Developer Account | Google | 2,500 | 2,500 |
| App Store Developer Account | Apple | 8,500 | 8,500 |
| PagerDuty (on-call) | | 1,50,000 | 3,60,000 |
| Datadog / New Relic APM | | 1,80,000 | 6,00,000 |
| NSE Historical Data API | TrueData / GlobalDatafeeds | 30,000 | 3,00,000 |
| LLM API (for Kyro AI feature) | OpenAI / Google | 1,00,000 | 5,00,000 |
| **Annual Total** | | **~₹17 L** | **~₹55 L** |

---

## TABLE 7 — Marketing & User Acquisition

| Channel | Annual Min (₹) | Annual Max (₹) | Expected CAC (Cost per Acquired User) |
|---------|---------------|---------------|--------------------------------------|
| Google Search Ads | 6,00,000 | 30,00,000 | ₹200–₹600 |
| YouTube Video Ads | 4,00,000 | 20,00,000 | ₹150–₹400 |
| Meta (Facebook/Instagram) Ads | 3,00,000 | 15,00,000 | ₹200–₹500 |
| Trading YouTube Influencers | 4,00,000 | 20,00,000 | ₹50–₹200 (high ROI) |
| Twitter/X Trading Community | 1,00,000 | 5,00,000 | ₹100–₹300 |
| Referral Program (₹50/referral) | 2,50,000 | 10,00,000 | ₹50 per referred user |
| Content Marketing + SEO | 2,00,000 | 8,00,000 | Long-term organic |
| Webinars + Trading education | 1,00,000 | 5,00,000 | High conversion |
| App Store Optimization (ASO) | 50,000 | 2,00,000 | Organic Play Store traffic |
| Brand partnerships (Telegram channels) | 2,00,000 | 8,00,000 | |
| PR + Media coverage | 2,00,000 | 5,00,000 | Press releases |
| **Annual Total** | **~₹28 L** | **~₹1.28 Cr** | |
| **Target: 50K registered users** | ₹56/user avg | ₹256/user avg | |

---

## TABLE 8 — Alternative: Partner API / Sub-Broker Model (No Own SEBI License)

If you build a trading terminal as a **sub-broker** or **authorized person** of an existing broker (e.g., Zerodha, Dhan, Shoonya), using their APIs:

| Item | Cost | Notes |
|------|------|-------|
| Sub-broker agreement | ₹0–₹2L | One-time, varies by broker |
| NISM Certification | ₹3,000 per person | For authorized persons |
| Zerodha Kite Connect API | ₹0–₹2,000/month | Developer plan |
| Dhan API License | Negotiable | |
| App Development (front-end only) | ₹25L–₹80L | No OMS/RMS/exchange needed |
| Team (smaller) | ₹8L–₹15L/month | 4–6 people |
| Infrastructure | ₹20K–₹1L/month | Much simpler backend |
| **TOTAL YEAR 1 (partner model)** | **₹1.5 Cr – ₹3.5 Cr** | vs ₹4–8 Cr for own license |
| **Revenue share** | 20%–40% to parent broker | Significant revenue cut |
| **Regulatory barrier** | Minimal | Much faster to market |
| **Control over product** | Limited | Cannot build own OMS/data |

---

## TABLE 9 — Revenue Model & Break-Even Analysis

### Revenue Sources
| Revenue Stream | Per Transaction | Scale (50K users, ₹500 Cr ADT) |
|----------------|----------------|-------------------------------|
| Brokerage (₹10/order, avg 3 orders/day/user) | ₹10 | ~₹4.5 Cr/month |
| STT (not broker revenue, pass-through) | — | — |
| Interest on client funds (float) | 6–7% per year | ₹30L–₹50L/month at scale |
| Margin Trade Funding (MTF) interest | 18% per year | Growing segment |
| Premium subscriptions (AI features) | ₹199–₹999/month | ₹50L–₹5 Cr/month at scale |
| **Monthly Revenue (50K users, 50% active)** | | **~₹5–10 Cr/month** |

### Break-Even Timeline
| Metric | Value |
|--------|-------|
| Monthly operational cost | ₹2–4 Cr |
| Required monthly revenue to break even | ₹2–4 Cr |
| Required active users for break-even | ~20,000–40,000 |
| Estimated time to break-even | 18–30 months from launch |

---

## TABLE 10 — Funding Requirements

| Funding Round | Suggested Amount | When | Purpose |
|---------------|-----------------|------|---------|
| Bootstrapped / Angel | ₹3–5 Crore | Pre-launch | Regulatory + MVP development |
| Seed Round | ₹10–25 Crore | Month 6–12 | Full team + marketing + scale |
| Series A | ₹50–150 Crore | Month 18–24 | Aggressive user acquisition, iOS, AI |

### Startup Credit Programs (Apply Early!)
| Program | Credits Available | Apply When |
|---------|-----------------|------------|
| AWS Activate (startup tier) | Up to $5,000 | Anytime |
| AWS Activate (portfolio tier, with VC) | Up to $100,000 | After seed round |
| Google for Startups Cloud | Up to $200,000 | Anytime |
| Microsoft for Startups | Up to $150,000 | Anytime |
| Sentry Startup Program | 6 months free | After company registration |
| Firebase Spark Plan | Free tier forever | Immediately |

---

## TABLE 11 — Competitor Funding & Valuation Benchmarks

| Broker | Funding Raised | Valuation (approx) | Users |
|--------|---------------|-------------------|-------|
| Zerodha | Bootstrapped | ₹70,000 Cr+ | 1.5 Cr+ |
| Groww | ~$900M raised | $3B valuation | 5 Cr+ |
| Upstox | ~$280M raised | $3.4B valuation | 1 Cr+ |
| Dhan | Raised undisclosed | Emerging | 10L+ |
| Angel One | Public (listed) | ₹15,000 Cr | 70L+ |
| **Sahi (reference)** | Raised (undisclosed) | Early stage | Growing |

---

## ⚠️ Key Financial Risks to Plan For

1. **Regulatory risk:** SEBI can tighten broker margins; F&O segment is under scrutiny
2. **Exchange concentration:** 70%+ Indian traders are in NSE F&O — NSE membership is critical path
3. **Latency penalty:** Every 1ms latency disadvantage = potential user churn from scalpers
4. **Customer fund segregation:** SEBI requires broker funds separate from client funds (bank guarantees)
5. **VAPT failure:** A failed security audit means operational suspension — budget for quarterly audits
6. **Data localization:** RBI mandates Indian user data stays in India — no US-only cloud deployment
7. **Payment float rules:** Brokers cannot earn more than prescribed rate on client idle funds

---

## 💡 Cost Optimization Tips

1. **Use startup credit programs** (AWS/GCP) to save ₹50L–₹1.5 Cr in Year 1 cloud costs
2. **Start with NSE CM + F&O only**, skip BSE and MCX initially (add later)
3. **Partner with CDSL first** — faster, cheaper than NSDL for new brokers
4. **Use off-the-shelf OMS** initially (providers like Omnesys, Sievert) — saves 6 months and ₹50L
5. **Use TrueData** for historical chart data initially instead of direct NSE historical feed
6. **License TradingView charts initially** (cheaper than building custom engine) — upgrade to custom later
7. **Use managed Kubernetes (EKS)** instead of self-managed — saves DevOps time
8. **Defer iOS app** to Month 12–18 — Android covers 95% of Indian active traders
9. **AI features in Phase 2** — build basic execution first, add AI indicators after PMF

