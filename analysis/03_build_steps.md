# Sahi Trading App — Step-by-Step Build Guide
## How to Build a Trading App Like Sahi from Scratch

> **Disclaimer:** This guide is for educational and technical reference purposes. Building a SEBI-registered stock broker requires significant capital, legal expertise, and regulatory compliance. Consult qualified legal and financial advisors before proceeding.

---

## Phase 1: Legal & Regulatory Setup (Months 1–4)

This is the most critical and time-consuming phase. Without SEBI registration, you cannot legally operate as a stockbroker in India.

---

### Step 1.1: Company Incorporation (Private Limited)

**Objective:** Establish the legal entity that will apply for SEBI registration.

**Sub-steps:**
1. **Choose company name** — Check availability on MCA (mca.gov.in). Avoid names with "Stock", "Broker", "Investment" without pre-approval.
2. **Obtain Digital Signature Certificates (DSC)** — For all directors (Class 3 DSC required). Vendor: eMudhra, Sify, Capricorn. Cost: ₹1,500–₹3,000/director.
3. **Apply for Director Identification Numbers (DIN)** — Via MCA portal (SPICe+ form). Included in incorporation.
4. **File SPICe+ Form (Simplified Proforma for Incorporating Company)** — Online on MCA portal. Includes:
   - Name reservation (RUN-Web)
   - Incorporation application
   - PAN & TAN application
   - GST registration (optional at this stage)
   - EPFO and ESIC registration
5. **Draft Memorandum of Association (MOA) and Articles of Association (AOA)** — Include objects clause specifically mentioning stock broking, commodity broking, depository participant services. Critical: SEBI will verify MOA objects.
6. **Minimum paid-up capital:** ₹1,00,000 (one lakh) for Pvt Ltd. However, SEBI requires minimum net worth of ₹1 crore for stock broker. Plan paid-up capital of ₹5–10 crore.
7. **Registered office address** — Need proof of registered office (rent agreement + NOC from owner). Cannot be a virtual office for SEBI application.
8. **Bank account opening** — After incorporation certificate received. Use a nationalized bank (SBI, PNB preferred by SEBI). Required for:
   - Net worth certificate
   - FDR for Base Minimum Capital

**Estimated Time:** 7–15 working days after document submission.  
**Cost:** ₹8,000–₹15,000 (professional fees + MCA filing fees).  
**Potential Blockers:**
- Name rejection by MCA (have 3 alternative names ready)
- DSC procurement delays
- Registered office proof issues

**Tools & Vendors:**
- MCA Portal: [mca.gov.in](https://mca.gov.in)
- Professional: Company Secretary (CS) firm for drafting and filing
- DSC vendor: eMudhra, Sify Technologies

---

### Step 1.2: SEBI Stock Broker Registration

**Objective:** Obtain SEBI Certificate of Registration as a Stock Broker.

**Sub-steps:**
1. **Identify segments to apply for:**
   - NSE Capital Market (CM) — equity cash
   - NSE Futures & Options (F&O)
   - BSE Cash + F&O
   - MCX (apply separately via MCX)
   Each segment requires separate membership and has its own net worth requirement.

2. **Prepare net worth documentation:**
   - Minimum net worth: ₹1 crore (for NSE CM + F&O combined)
   - Audited balance sheet certified by CA (within 3 months)
   - Fixed Deposits as Base Minimum Capital (BMC)

3. **SEBI Online Registration (SEBI Intermediary Portal):**
   - URL: [siportal.sebi.gov.in](https://siportal.sebi.gov.in)
   - Application form: Stockbroker registration (Form A)
   - Upload all required documents

4. **Required documents for SEBI application:**
   - Certificate of Incorporation
   - MOA & AOA
   - PAN of company
   - Board resolution authorizing application
   - Net worth certificate (CA certified)
   - Audited financial statements
   - Details of directors (KYC, DIN, educational qualifications)
   - Office address proof (owned/rented with lease agreement)
   - No Objection from landlord
   - Details of key management persons (KMPs)
   - NISM Series-VII (Securities Operations & Risk Management) or Series-VIII (Equity Derivatives) certification for designated persons
   - IT policy document
   - Investor grievance redressal mechanism details

5. **NISM Certifications (Mandatory for Key Personnel):**
   - All directors and designated persons must pass NISM exams
   - NISM Series VII: Equity Derivatives (F&O segment)
   - NISM Series VIII: Securities Operations
   - NISM Series X-A: Investment Adviser (if applicable)
   - Duration: Each exam takes 1–3 months of preparation. Schedule early.

6. **Physical inspection by SEBI/NSE team** — SEBI or the exchange (acting as SEBI agent) will inspect your office. Ensure:
   - Proper trading setup (servers, UPS, internet redundancy)
   - Compliance manuals ready
   - Disaster recovery plan documented
   - Compliance officer present

7. **Registration fee payment:** ₹1,00,000 + GST via NEFT to SEBI account.

8. **Timeline:** SEBI processing takes 90–120 days from complete application submission.

**Potential Blockers:**
- Net worth shortfall (plan for ₹1.5–2 crore liquid capital)
- NISM exam failures (retakes cost time)
- SEBI queries requiring document resubmission (add 30–60 days)
- Infrastructure not meeting SEBI inspection standards

---

### Step 1.3: NSE Membership Application

**Objective:** Become an NSE Trading Member in Capital Market and/or F&O segment.

**Sub-steps:**
1. **Apply to NSE Membership Department:**
   - Download NSE membership application form from nseindia.com
   - Submit filled form with all enclosures

2. **NSE membership requirements (CM Segment):**
   - Net worth: ₹1 crore minimum (NSE CM alone)
   - Base Minimum Capital (BMC): ₹10 lakhs in FDR/cash
   - Interest-free security deposit: ₹1 crore (for professional clearing)
   - NSE Admission fee: ₹5–10 lakhs (one-time, non-refundable)

3. **Additional for F&O Segment:**
   - Net worth: Additional ₹50 lakhs (total ₹1.5 crore for CM + F&O)
   - Additional BMC deposit
   - F&O segment admission fee: ₹3–7 lakhs

4. **Clearing Mechanism — Two Options:**
   - **Self-clearing:** Requires NSE Clearing membership (higher capital ~₹50 crore+). Not practical for new entrants.
   - **Professional Clearing Member (PCM):** Tie up with an existing clearing member (e.g., Edelweiss, Kotak Securities). They clear your trades. PCM charges: 0.01–0.05% of turnover + monthly fee ₹50k–₹2 lakhs.

5. **CTCL (Computer to Computer Link) Setup:**
   - After NSE membership, apply for CTCL approval
   - NSE provides API/FIX gateway access for your OMS to connect
   - Requires: CTCL application, system audit certificate, datacenter agreement
   - Use NSE co-location facility (Equinix Mumbai/NSE datacenter) for lowest latency

6. **NSE System Audit:**
   - Your trading system must pass NSE's technical audit before live access
   - Hire a SEBI-empanelled system auditor (e.g., EY, KPMG, local firms)
   - Cost: ₹2–5 lakhs for audit
   - Timeline: 30–60 days after application

7. **Mock Trading Environment (CTCL-UAT):**
   - NSE provides a mock/UAT trading environment
   - Test your OMS extensively here before going live
   - Minimum 3–6 months of mock trading recommended

**Estimated Timeline:** 4–6 months from application to live trading access.

---

### Step 1.4: BSE Membership Application

**Objective:** Obtain BSE Trading Membership.

**Sub-steps:**
1. **BSE Membership Type:**
   - **Trading Member (TM):** Only trading rights, must use a Professional Clearing Member
   - **Trading-cum-Clearing Member (TCM):** Trading + self-clearing (higher capital)

2. **BSE Admission Process:**
   - Apply online via BSE's member portal (membership.bseindia.com)
   - Submit documents similar to NSE membership

3. **BSE Financial Requirements:**
   - Deposit-Based Membership (DBM): ₹10–15 lakhs earnest money (refundable on exit)
   - Security deposit: ₹25–50 lakhs (in FDR)
   - Annual subscription: ₹50,000–₹1,50,000/year per segment

4. **BSE BOLT+ System:**
   - BSE's trading system (similar to NSE's CTCL)
   - Obtain BOLT+ API access after membership
   - Requires similar system audit and UAT testing

5. **Advantage of BSE Membership:**
   - Access to SME platform (IPO subscriptions)
   - Broader instrument coverage
   - Some institutional clients prefer BSE for certain instruments

---

### Step 1.5: MCX Membership (Optional — Phase 2)

**Objective:** Access commodity derivatives (Crude Oil, Gold, Silver).

**Sub-steps:**
1. **MCX Membership Application:**
   - Apply to Multi Commodity Exchange (mcxindia.com)
   - Separate from SEBI stock broker registration
   - MCX is regulated by SEBI (post 2015 FMC merger)

2. **MCX Financial Requirements:**
   - MCX Membership fee: ₹5–8 lakhs (one-time)
   - Security deposit: ₹25–50 lakhs
   - Net worth: ₹1 crore (already satisfied by SEBI stock broker reg.)

3. **MCX CTCL Access:**
   - Apply for CTCL access (commodity segment)
   - Different FIX/API protocol from NSE/BSE — requires separate integration
   - MCX also has a co-location facility

4. **Recommended Timing:** Defer MCX to Phase 2 (after equity trading is live) to reduce initial complexity and capital requirements.

---

### Step 1.6: CDSL/NSDL DP Registration

**Objective:** Become a Depository Participant to open demat accounts for customers.

**Sub-steps:**
1. **Choose Depository:**
   - **CDSL:** (Central Depository Services Ltd) — More common for retail, lower entry cost
   - **NSDL:** (National Securities Depository Ltd) — Higher entry cost, preferred by HNIs/institutions
   - Sahi uses CDSL (IN-DP-780-2024)

2. **CDSL DP Registration Process:**
   - Apply to CDSL via their online portal
   - Documents: SEBI stock broker registration certificate, company incorporation docs, KYC of directors, IT policy, net worth certificate
   - CDSL charges one-time DP admission fee
   - Annual DP subscription charges

3. **CDSL Requirements:**
   - Minimum net worth for DP: ₹50 lakhs (standalone DP)
   - Stock broker DP: ₹10 lakhs additional net worth over stock broker minimum
   - Infrastructure: DP back-office software (CDSL-empanelled vendors: Tradesmart, Tata Consultancy, etc.)

4. **DP Back-Office Software:**
   - You need CDSL-approved DP software to access CDSL's CASDAS system
   - Options: Procure from CDSL-empanelled vendors or build integration via CDSL API
   - Cost: ₹2–5 lakhs/year for SaaS-based DP back-office

5. **CDSL API Integration:**
   - CDSL provides API for:
     - Account opening (EKYC demat account)
     - Holdings fetch (CDSL-TPIN or CDSL DDPI for selling)
     - DIS (Delivery Instruction Slip) processing
   - For digital account opening: CDSL's eAsaan platform

---

### Step 1.7: Clearing Member Agreement

**Sub-steps:**
1. Identify and negotiate with a Professional Clearing Member (PCM)
2. Typical PCMs: Edelweiss Securities, Kotak Securities, IIFL, Globe Capital
3. Sign PCM agreement specifying:
   - Clearing charges (% of turnover)
   - Exposure limit granted to you
   - Margin deposit with PCM (₹25–100 lakhs as security)
   - SLA for trade confirmation and reporting
4. PCM provides your client an additional layer of SEBI oversight

---

### Step 1.8: Compliance Officer Appointment

**Requirements:**
- Dedicated compliance officer (NISM certified, preferably a CS or MBA-Finance)
- Responsible for: SEBI filings, exchange reports, investor grievances, internal audit coordination
- Salary: ₹6–15 lakhs/year
- Must have NISM Series X-B or equivalent certification

**Responsibilities:**
- Monthly/quarterly reports to NSE, BSE, SEBI
- STR (Suspicious Transaction Reporting) to FIU-IND
- Maintaining client KYC records
- Ensuring PMLA (Prevention of Money Laundering Act) compliance

---

### Step 1.9: Net Worth Certificate

- Prepared by a SEBI-empanelled Chartered Accountant
- Certified on company letterhead
- Must reflect minimum ₹1 crore+ tangible net worth
- Updated every 6 months for SEBI submissions

---

### Step 1.10: VAPT (Vulnerability Assessment and Penetration Testing)

- **SEBI Circular SEBI/HO/ITD/ITD_VAPT/P/CIR/2023:** Mandates quarterly VAPT for all market infrastructure institutions and trading members
- **Scope:** Trading application, mobile app, API endpoints, backend servers
- **Vendor:** Must be CERT-In empanelled cybersecurity firm (CertIn list available on cert-in.org.in)
- **Timeline:** First VAPT before going live; subsequent tests quarterly
- **Cost:** ₹3–6 lakhs per audit (scope-dependent)
- **Deliverable:** VAPT report + Compliance Certificate submitted to exchange

---

## Phase 2: Business & Product Planning (Months 1–2, Parallel with Legal)

### Step 2.1: Define Target User Persona

**Primary Persona: "The Active Day Trader"**
- Age: 24–45
- Trading experience: 2–10 years
- Trades: 5–20 trades/day in equity intraday and F&O
- Device: Android (70%+ of Indian traders)
- Pain points: Slow order execution, laggy charts, complex UI
- Goals: Fast order placement, real-time P&L visibility, reliable platform

**Secondary Persona: "The Options Trader / Scalper"**
- Focus on Bank Nifty, Nifty weekly options
- Needs dual-chart view (index + option)
- Obsessed with option chain Greeks
- Executes 20–100 micro trades/day

**Research Methods:**
- Survey 200+ active traders on pain points
- Interview 20 users (Zerodha, Dhan, Groww users)
- Analyze App Store reviews of competitors

---

### Step 2.2: Feature Prioritization (MVP vs Full)

**MVP (Month 1 launch feature set):**
- [ ] Login / OTP authentication
- [ ] Watchlist (real-time quotes)
- [ ] Basic chart (candlestick, 5 timeframes)
- [ ] Market order + Limit order
- [ ] Portfolio / Holdings view
- [ ] Order history
- [ ] Basic account settings

**Phase 2 (Month 3–6):**
- [ ] Option chain with Greeks
- [ ] Advanced chart indicators (20+)
- [ ] Scanners (5–10)
- [ ] Scalper terminal (basic)
- [ ] Push notifications + price alerts

**Phase 3 (Month 6–12):**
- [ ] AI indicators (Lorentzian, Nadaraya-Watson)
- [ ] Kyro natural language indicator builder
- [ ] Full Scalper 2.0
- [ ] Strategy Builder
- [ ] MCX commodities

---

### Step 2.3: Competitive Analysis

| Feature | Zerodha Kite | Dhan | Groww | Upstox | **Sahi** |
|---------|-------------|------|-------|--------|---------|
| Brokerage F&O | ₹20/order | ₹20/order | ₹20/order | ₹20/order | **₹10/order** |
| Custom Chart Engine | ✗ (TradingView) | ✗ (TV) | ✗ (TV) | ✗ (TV) | **✓ (In-house)** |
| AI Indicators | ✗ | ✗ | ✗ | ✗ | **✓ (18+)** |
| Scalper Terminal | ✗ | ✓ (basic) | ✗ | ✗ | **✓ (Scalper 2.0)** |
| MCX Commodities | ✓ | ✓ | ✗ | ✓ | **✓** |
| Free Account Opening | ✓ | ✓ | ✓ | ✓ | **✓** |

**Key Differentiator:** Sahi's 10/order brokerage vs ₹20 from all competitors + proprietary charting = cost + speed moat.

---

### Step 2.4: Revenue Model

**Primary Revenue (Brokerage):**
- ₹10/executed order in F&O
- ₹10 or 0.05% for equity (lower applies)
- With 10,000 active traders doing 10 orders/day:
  - Daily brokerage: 10,000 × 10 × ₹10 = ₹10,00,000/day = ₹240 Cr/year gross brokerage

**Secondary Revenue:**
- Margin funding (interest on borrowed margin): 18–24% p.a.
- Subscription plans (advanced AI features, Scalper Pro tier)
- Referral commissions from third-party products (mutual funds, insurance)
- Research reports and advisory (if Research Analyst reg. obtained)
- Exchange incentives (market-maker rebates for high volume brokers)

---

### Step 2.5: Brand Identity

**Naming Considerations:**
- Short, memorable (4–6 letters)
- Domain available (.com preferred)
- Not already trademarked in Class 36 (financial services)

**Design:**
- Logo: Simple wordmark or minimal icon (avoid complex gradients for small screen)
- Color palette: Dark background (#0D0D0D), accent neon (green #00FF88 or orange #FF6B35)
- Typography: Clean sans-serif (Inter, Manrope)
- Tagline: "Trade at the speed of thought" or equivalent

---

### Step 2.6: UI/UX Wireframes

**Tools:**
- Figma (primary wireframing and prototyping)
- Maze or UserTesting for usability testing prototypes
- Lottie for micro-animations

**Key Screens to Prototype:**
1. Home / Watchlist
2. Chart screen
3. Order placement dialog (critical — 1 tap to order)
4. Option chain
5. Scalper terminal
6. Portfolio / P&L
7. KYC onboarding flow (7–10 screens)
8. Settings

---

## Phase 3: Team Building (Months 1–3)

### Step 3.1: CTO / Lead Backend Engineer
- **Skills:** Go or Java, distributed systems, low-latency networking, FIX protocol, PostgreSQL, Kafka
- **Experience:** 8–12 years, ideally fintech (HFT, NSE, exchange tech)
- **Salary:** ₹30–80 lakhs/year
- **Priority:** HIRE FIRST — everything depends on this person

### Step 3.2: Android Developer (Kotlin Specialist)
- **Skills:** Kotlin, Jetpack Compose or XML + DataBinding, MVVM, custom canvas rendering, WebSocket
- **Experience:** 4–7 years Android, ideally with trading/fintech app
- **Salary:** ₹18–36 lakhs/year
- **Note:** Custom chart engine is the hardest part — find someone with game development or custom view rendering experience

### Step 3.3: iOS Developer (Swift)
- **Defer to Phase 2** unless iOS market share in target segment is significant
- **Skills:** Swift, SwiftUI + UIKit, Metal for charting
- **Salary:** ₹18–36 lakhs/year

### Step 3.4: DevOps / Infrastructure Engineer
- **Skills:** AWS, Kubernetes (EKS), Kafka, PostgreSQL DBA, CI/CD (GitHub Actions), Terraform, monitoring (Datadog/CloudWatch)
- **Experience:** 5–8 years
- **Salary:** ₹15–30 lakhs/year
- **Critical for:** Zero-downtime deployments during market hours, database failover

### Step 3.5: Compliance Officer / CA
- **Mandatory for SEBI application**
- NISM certified, ideally CS (Company Secretary) background
- Handles: SEBI filings, exchange reports, PMLA, audit coordination
- Salary: ₹6–15 lakhs/year

### Step 3.6: UI/UX Designer
- **Skills:** Figma, Motion design (Lottie), Design systems
- **Experience:** 3–6 years, fintech portfolio preferred
- **Salary:** ₹10–24 lakhs/year

### Step 3.7: Data Engineer (Market Data)
- **Skills:** Kafka, TimescaleDB/InfluxDB, FIX protocol, Python/Go
- **Responsibility:** Build and maintain market data pipeline (NSE/BSE tick ingest → OHLC → client delivery)
- **Salary:** ₹18–36 lakhs/year

### Step 3.8: QA Engineer
- **Skills:** Appium, Espresso, JUnit, load testing (k6, Locust)
- **Focus:** Trading flow testing (order placement under market stress), regression
- **Salary:** ₹8–18 lakhs/year

---

## Phase 4: Infrastructure Setup (Months 3–4)

### 4.1: AWS Account & VPC Setup
```
AWS Organization (management account)
├── Production Account
│   ├── VPC: 10.0.0.0/16
│   │   ├── Public Subnet: Load Balancers, NAT Gateway
│   │   ├── Private Subnet: EKS Nodes, RDS, ElastiCache
│   │   └── Isolated Subnet: Databases (no internet)
│   └── Regions: ap-south-1 (Mumbai) primary
└── Staging Account (identical architecture, smaller instances)
```

**Setup Steps:**
1. Enable AWS Organizations (multi-account setup)
2. Configure VPC with proper subnetting (CIDR planning)
3. Setup NAT Gateway for outbound traffic from private subnets
4. Configure VPC Flow Logs to S3 + CloudWatch
5. Enable AWS GuardDuty (threat detection — mandatory for fintech)
6. Enable AWS Security Hub + Config rules
7. Setup AWS WAF on Application Load Balancer

### 4.2: Database Setup

**PostgreSQL (RDS):**
```bash
# Multi-AZ RDS PostgreSQL 16
aws rds create-db-instance \
  --db-instance-identifier sahi-prod-postgres \
  --db-instance-class db.r6g.xlarge \
  --engine postgres --engine-version 16.1 \
  --multi-az \
  --storage-type gp3 --allocated-storage 500 \
  --backup-retention-period 30 \
  --deletion-protection
```

**Redis (ElastiCache):**
- Cluster mode enabled, Multi-AZ
- Instance: cache.r6g.large (4 nodes for HA)
- Use for: WebSocket session state, real-time P&L, order book cache

**TimescaleDB:**
- Hosted on EC2 (not RDS — TimescaleDB needs custom extension)
- Or use Timescale Cloud (managed service)
- Used for: OHLC historical data (billions of rows)

### 4.3: Kubernetes Cluster (EKS)

```hcl
# Terraform configuration
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  cluster_name    = "sahi-prod"
  cluster_version = "1.29"
  node_groups = {
    trading_critical = {
      instance_types = ["c6i.2xlarge"]  # High CPU for order processing
      min_size = 3; max_size = 10
    }
    market_data = {
      instance_types = ["c6i.4xlarge"]  # High throughput for tick processing
      min_size = 2; max_size = 6
    }
    general = {
      instance_types = ["t3.xlarge"]
      min_size = 2; max_size = 20
    }
  }
}
```

### 4.4: Kafka Setup (Amazon MSK)

```bash
# Amazon Managed Streaming for Kafka
# Topics to create:
# - market.ticks.nse (partitions: 50, retention: 1 hour)
# - market.ticks.bse (partitions: 20)
# - market.ticks.mcx (partitions: 10)
# - orders.placed (partitions: 20, retention: 7 days)
# - orders.updates (partitions: 20, retention: 7 days)
# - risk.alerts (partitions: 5)
# - audit.events (partitions: 10, retention: 90 days)
```

### 4.5: CI/CD Pipeline (GitHub Actions)

```yaml
# .github/workflows/deploy.yml
on:
  push:
    branches: [main]
jobs:
  build-test-deploy:
    steps:
      - name: Run unit tests
      - name: Run integration tests
      - name: Build Docker image
      - name: Push to ECR
      - name: Deploy to EKS (blue-green)
      - name: Run smoke tests
      - name: Notify Slack
```

**Critical rule:** NEVER deploy to production during market hours (9:00 AM – 3:45 PM IST). All deployments must happen in maintenance windows (after 4 PM or pre-market at 8 AM).

### 4.6: Monitoring Stack
- **Sentry:** Application crash reporting (SDK in Android + backend services)
- **Datadog or Grafana/Prometheus:** Infrastructure metrics, custom trading metrics (order latency, tick lag, WebSocket subscriber count)
- **PagerDuty or OpsGenie:** Alert routing and on-call escalation
- **ELK Stack (Elasticsearch + Logstash + Kibana):** Log aggregation and audit trail

---

## Phase 5: Backend Development (Months 3–8)

### 5.1: Authentication Service
**Technology:** Go + PostgreSQL + Redis

**Features to build:**
1. **Phone OTP login:**
   - Phone number entry → trigger OTP via Msg91/AWS SNS
   - OTP verification → generate JWT (access token 15 min) + refresh token (30 days)
   - Store refresh token in Redis with device fingerprint
2. **Biometric auth handshake:**
   - First login: OTP → app stores encrypted credential reference
   - Subsequent logins: biometric unlock → retrieve credential → server validates session
3. **2FA for sensitive actions** (withdrawal, profile change): Re-OTP required

**Endpoints:**
```
POST /auth/otp/send       → sends OTP
POST /auth/otp/verify     → verifies OTP, returns JWT
POST /auth/token/refresh  → refresh access token
POST /auth/logout         → invalidate refresh token
GET  /auth/session        → validate session status
```

### 5.2: KYC Service

**Integrations required:**
1. **UIDAI Aadhaar OTP KYC** — via an authorized KUA (KYC User Agency):
   - Certified KUAs: CAMS Finserv, Karvy, CDSLVentures
   - Cost per KYC: ₹15–₹25
   - API: UIDAI's AADHAAR XML API (requires UIDAI agreement and AUA/KUA licensing)

2. **DigiLocker API** (alternative to UIDAI direct):
   - User logs in to DigiLocker, shares Aadhaar XML
   - More user-friendly, UIDAI compliant
   - Cost: ~₹0 (free API but requires NIC agreement)

3. **PAN Verification:**
   - NSDL Pan Verification API or third-party: Surepass, Signzy, IDfy
   - Cost per call: ₹3–₹5

4. **Bank Account Verification (Penny Drop):**
   - Deposit ₹1 to user's bank → verify name matches KYC name
   - Providers: Razorpay, Cashfree, NPCI NACH
   - Cost: ₹3–₹5 per verification

5. **CKYC (Central KYC) Registry:**
   - Check if user is already CKYC registered (most bank account holders are)
   - If yes: fetch CKYC data, skip re-verification
   - If no: create new CKYC record after completing KYC

6. **Face Match / Liveness:**
   - Compare selfie with Aadhaar photo
   - Providers: AWS Rekognition, IDfy, Hyperverge
   - Liveness detection to prevent spoofing

**KYC Data Storage:**
- All KYC documents (scanned PAN, Aadhaar XML, selfie, bank proof) stored encrypted in S3
- Encryption keys managed by AWS KMS
- KYC data never in clear text in database (only encrypted references)

### 5.3: Market Data Feed Service

**Architecture:**
```
Exchange NSE (FIX/CTCL) → Feed Handler (Go) → Normalizer → Kafka
                                                               │
                                                    ┌──────────▼────────────┐
                                                    │ OHLC Builder (Go)     │
                                                    │ (builds 1m, 5m candles│
                                                    │  in real-time)        │
                                                    └──────────┬────────────┘
                                                               │
                                                    ┌──────────▼────────────┐
                                                    │ WebSocket Server (Go) │
                                                    │ Push ticks to clients │
                                                    └───────────────────────┘
```

**Technical Details:**
- Feed handler connects to NSE's CTCL box via FIX 4.2/4.4 protocol
- Receives: `MarketDataSnapshotFullRefresh (W)` and `MarketDataIncrementalRefresh (X)` messages
- Normalizes to internal Protobuf schema
- Publishes to Kafka with instrument token as partition key
- OHLC builder consumes Kafka, builds candles, writes to TimescaleDB
- WebSocket server: each connection has a subscription set; filtered push from Kafka consumer

**WebSocket Subscription Model:**
```json
// Client sends:
{"action": "subscribe", "instruments": [256265, 260105, 884737]}

// Server pushes:
{"token": 256265, "ltp": 24156.50, "oi": 14523200, "vol": 8432100, "ts": 1730123456789}
```

**Scalability:** One WebSocket server process handles 10,000–50,000 concurrent connections. Use multiple processes behind a sticky load balancer (by user ID hash).

### 5.4: Order Management System (OMS)

**Flow:**
```
Client → API Gateway → OMS API → RMS validation → Exchange CTCL → Order ACK
                                                                      │
                                  Client ◄── WebSocket update ────────┘
```

**Order States:**
```
PENDING → VALIDATED → SENT_TO_EXCHANGE → OPEN (partial) → COMPLETE / REJECTED / CANCELLED
```

**Critical Requirements:**
- End-to-end latency target: <100ms (client → exchange acknowledgment)
- ACID transactions: Every order state change in PostgreSQL within a transaction
- Idempotency: Duplicate order prevention (unique client order ID per request)
- Rate limiting: Prevent runaway orders (max N orders/second per user)

**Endpoints:**
```
POST /orders/place      → place new order
PUT  /orders/{id}       → modify order
DELETE /orders/{id}     → cancel order
GET  /orders            → list orders (with filters)
GET  /orders/{id}       → single order status
GET  /trades            → executed trades
GET  /positions         → current positions (intraday)
GET  /holdings          → demat holdings (via CDSL)
```

### 5.5: Risk Management System (RMS)

**Pre-order checks (all must pass before order goes to exchange):**
1. **Available margin:** Funds available ≥ required margin for the order
2. **Exposure limit:** Total exposure ≤ SEBI/exchange mandated limit
3. **Instrument allowed:** Instrument in allowed list (e.g., ban period securities blocked)
4. **Order size limit:** Single order quantity ≤ exchange freeze quantity
5. **Price range check:** Order price within ±20% of LTP (prevent fat-finger)
6. **Daily loss limit:** If client has lost > configured limit, block further orders (optional)

**Auto Squareoff (Intraday):**
- At 3:15 PM IST, begin squaring off all MIS (intraday) positions
- Priority: largest loss positions first
- Use IOC (Immediate or Cancel) market orders for guaranteed fill
- Send notification to client before squareoff

### 5.6: Notification Service

**Push Notifications via FCM:**
```go
// Firebase Admin SDK
message := &messaging.Message{
    Token: userFCMToken,
    Notification: &messaging.Notification{
        Title: "Order Executed",
        Body:  "Bought 50 NIFTY 24000 CE @ 145.50",
    },
    Data: map[string]string{
        "type": "ORDER_EXECUTED",
        "orderId": "ORD20241030123456",
    },
    Android: &messaging.AndroidConfig{
        Priority: "high",
    },
}
```

**Alert Types:**
- Order placed / executed / rejected / cancelled
- Price alert triggered (user-set price levels)
- Auto squareoff warning (15 min before)
- Margin shortfall warning
- "Buzzing stock" (unusual volume/momentum)

---

## Phase 6: Exchange Connectivity (Months 5–8)

### 6.1: NSE CTCL/FIX Integration

**Technical Stack:**
- **FIX Engine:** QuickFIX/Go (open source) or Commercial: Rapid Addition, Cameron FIX
- **NSE CTCL:** NSE's proprietary variant of FIX 4.2 (with custom tags)
- **Co-location:** NSE data center in Mumbai (Equinix or NSE's own facility)

**Setup Steps:**
1. Obtain CTCL approval from NSE (after NSE membership)
2. Procure co-location rack space at NSE's data center (~₹3–8 lakhs/year)
3. Set up FIX engine connecting to NSE's matching engine
4. Implement all required message types:
   - `NewOrderSingle (D)` — place order
   - `OrderCancelRequest (F)` — cancel order
   - `OrderCancelReplaceRequest (G)` — modify order
   - `ExecutionReport (8)` — order updates
   - `OrderCancelReject (9)` — cancel rejection
5. Test in NSE's UAT environment (mock trading) — minimum 3 months
6. Get NSE system audit sign-off

### 6.2: Disaster Recovery

- **Primary datacenter:** AWS Mumbai (ap-south-1)
- **DR datacenter:** AWS Hyderabad (ap-south-2) — warm standby
- **RPO (Recovery Point Objective):** ≤5 minutes (max data loss)
- **RTO (Recovery Time Objective):** ≤15 minutes (time to recover)
- **DB replication:** PostgreSQL streaming replication + pg_basebackup to DR
- **Failover testing:** Mandatory quarterly DR drill

---

## Phase 7: Android App Development (Months 4–10)

### 7.1: Project Setup

```
sahi-android/
├── app/                  # Main app module
├── core/
│   ├── network/          # OkHttp, Retrofit, WebSocket
│   ├── database/         # Room, DataStore
│   ├── domain/           # Use cases, entities
│   └── common/           # Utilities, extensions
├── feature/
│   ├── auth/             # Login, OTP, biometric
│   ├── kyc/              # KYC onboarding
│   ├── watchlist/        # Watchlist screens
│   ├── chart/            # Chart engine module
│   ├── orders/           # Order placement
│   ├── optionchain/      # Options chain
│   ├── scalper/          # Scalper 2.0 terminal
│   ├── portfolio/        # Holdings, P&L
│   ├── scanners/         # Market scanners
│   └── settings/         # Profile, settings
└── build-logic/          # Gradle convention plugins
```

**Gradle Setup (Version Catalog):**
```toml
[versions]
kotlin = "2.0.0"
compose = "1.6.0"
coroutines = "1.8.0"
retrofit = "2.11.0"
okhttp = "4.12.0"
hilt = "2.51"
room = "2.6.1"
```

### 7.2: Custom Chart Engine

This is the most complex and differentiating part of the Android app.

**Architecture:**
```kotlin
class ChartView @JvmOverloads constructor(context: Context, attrs: AttributeSet? = null) 
    : View(context, attrs) {

    private val candleRenderer = CandleStickRenderer()
    private val indicatorRenderer = IndicatorOverlayRenderer()
    private val crosshairRenderer = CrosshairRenderer()
    private val touchHandler = ChartTouchHandler(this)
    
    // Data
    var data: List<OHLCV> = emptyList()
        set(value) { field = value; recalculateViewport(); invalidate() }
    
    override fun onDraw(canvas: Canvas) {
        // 1. Draw grid lines
        // 2. Draw volume bars
        // 3. Draw candles (hardware accelerated)
        // 4. Draw indicator overlays
        // 5. Draw S/R levels
        // 6. Draw crosshair (if active)
        // Target: <16ms for 60fps
    }
}
```

**Performance Targets:**
- 1,000 candles rendering: <8ms
- WebSocket tick → chart update: <16ms (one frame)
- Smooth 60fps zoom/pan on budget Android devices (Snapdragon 695+)

**Key Technical Challenges:**
- Coordinate space transformations (price space ↔ pixel space)
- Efficient viewport management (only render visible candles)
- Hardware-accelerated canvas (use `android:hardwareAccelerated="true"`)
- Touch gesture detection (GestureDetector + ScaleGestureDetector)
- Indicator computation on background thread, render on main thread

### 7.3: WebSocket Client

```kotlin
class MarketDataWebSocketClient(private val okHttpClient: OkHttpClient) {
    
    private var webSocket: WebSocket? = null
    private val _tickFlow = MutableSharedFlow<Tick>(replay = 0, extraBufferCapacity = 1000)
    val tickFlow: SharedFlow<Tick> = _tickFlow
    
    fun connect() {
        val request = Request.Builder()
            .url("wss://stream.sahi.com/market-data")
            .addHeader("Authorization", "Bearer $jwtToken")
            .build()
        webSocket = okHttpClient.newWebSocket(request, listener)
    }
    
    fun subscribe(tokens: List<Int>) {
        val msg = json.encodeToString(SubscribeRequest(tokens))
        webSocket?.send(msg)
    }
    
    private val listener = object : WebSocketListener() {
        override fun onMessage(webSocket: WebSocket, bytes: ByteString) {
            val tick = Tick.parseFrom(bytes.toByteArray())  // Protobuf
            _tickFlow.tryEmit(tick)
        }
    }
}
```

### 7.4: Order Placement UI

**Design Principles for Order Dialog:**
- Open with quantity pre-filled (last used or lot size)
- LTP displayed prominently
- BUY (green) / SELL (red) buttons large and easy to tap
- Order type (Market/Limit/SL) switcher
- Confirmation step: optional (power users disable it)
- Error states: clear, actionable (e.g., "Insufficient margin: ₹12,450 short")

---

## Phase 8: Testing & QA (Months 9–11)

### 8.1: Unit Testing
- Framework: JUnit 5 + Mockito/MockK + Turbine (Flow testing)
- Coverage target: 80%+ for business logic layers (ViewModel, Repository, Use Cases)
- CI: Run on every pull request

### 8.2: Integration Testing
- Backend: Test full order flow end-to-end in staging environment
- Mock NSE CTCL with a test double
- Test all KYC integration points with sandbox credentials

### 8.3: UI Testing (Espresso)
- Automate critical user journeys:
  - Login → place order → verify in order book
  - KYC onboarding (9 steps)
  - Chart interactions (zoom, crosshair, indicator toggle)

### 8.4: Load Testing

**WebSocket Server Load Test:**
```bash
# k6 load test: 50,000 concurrent WebSocket connections
k6 run --vus 50000 --duration 30m websocket_loadtest.js
```

**Targets:**
- 10,000 concurrent WebSocket connections: <5ms server-side message latency
- 100,000 concurrent: horizontal scaling with multiple WS server pods
- Order throughput: 10,000 orders/second (peak market open)

### 8.5: SEBI-Mandated VAPT
- Conduct before go-live
- Scope: all internet-facing endpoints, mobile app (APK static + dynamic analysis), internal network
- Remediate all critical and high severity findings before submission
- Keep medium findings with accepted risk documentation

---

## Phase 9: SEBI/Exchange Approval & Go-Live (Months 11–12)

### 9.1: Exchange Inspection
- NSE will inspect trading systems before granting live access
- Provide: system architecture document, DR plan, VAPT report, system audit certificate

### 9.2: Mock Trading Certification
- Complete mock trading on NSE's UAT environment
- Run complete order lifecycle: place → execute → cancel → modify
- Test auto squareoff, OMS fail scenarios, connectivity loss

### 9.3: Play Store Submission
- Google requires financial app policy compliance:
  - Provide SEBI registration certificate to Google
  - Disclose all fees and brokerage clearly in store listing
  - Privacy policy must cover financial data handling
  - App must not have false claims (no "guaranteed returns")
- Review time: 3–7 days (standard), longer if clarifications needed

### 9.4: Soft Launch (Beta)
- 500–1,000 invite-only beta users
- Duration: 4–6 weeks
- Focus: real trading flow, margin issues, notification delivery, crash rates
- Monitor Sentry for crash-free rate (target: >99.5%)

### 9.5: Public Launch
- Press release + PR outreach (ET Markets, Economic Times, Livemint)
- Social media: Twitter/X financial community, Trading communities (TradingView, NSE community)
- Referral program: ₹200 per referred account that trades

---

## Phase 10: Post-Launch Operations

### 10.1: 24/7 Monitoring & On-Call
- On-call rotation: minimum 2 engineers always on-call
- PagerDuty escalation policy: 5 min alert → 15 min page → 30 min CEO page
- Market hours war room: 9 AM – 4 PM IST dedicated monitoring

### 10.2: Daily Reconciliation
- Every evening: reconcile trades with NSE/BSE/MCX
- Verify: all executed orders in OMS match exchange trade confirmations
- CDSL end-of-day position reconciliation
- P&L reconciliation (client-facing vs actual)
- Discrepancy resolution: report to compliance officer, escalate as needed

### 10.3: Monthly SEBI Compliance Reports
- Monthly Net Position Report (client segment-wise)
- Investor Grievance Report (time to resolution metrics)
- STR (Suspicious Transaction Reports) to FIU-IND if applicable
- Margin Utilization Reports

### 10.4: Quarterly VAPT Audits
- Mandatory per SEBI circular
- Submit report to NSE/BSE within 30 days of audit completion
- Remediate critical/high findings within 30 days of report

### 10.5: Feature Roadmap & App Updates
- 2-week sprint cycles
- Release cadence: bi-weekly app updates (Play Store)
- A/B test major UX changes before full rollout
- Feature flags for gradual rollout (use Firebase Remote Config or LaunchDarkly)
