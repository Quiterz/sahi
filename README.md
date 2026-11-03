# 🏦 Sahi Trading App — Complete Analysis & Clone Blueprint

> **Target:** Sahi Trading Platform (https://www.sahi.com/)  
> **Corporate Entity:** Aaritya Broking Private Limited  
> **SEBI Registration:** INZ000317632 (NSE: 90375 | BSE: 6867 | MCX: 57630 | CDSL DP: IN-DP-780-2024)  
> **Reverse Engineered Target:** `base.apk` (v1.0, Build 964, SHA-256: `9fff890ca793882e229d29a17b7c87931056556d6df3e88524ff037bb715e19f`)  
> **Analysis Engine:** `jadx-headless-mcp v0.8.0` + REA static analysis

---

## 📄 Client Proposal Master Document (Single PDF)

👉 **[Download / View Master Client Proposal PDF](./Sahi_Trading_App_Client_Proposal.pdf)** *(1.3 MB, Full-Fledged Multi-Page Enterprise Proposal)*

Includes:
- **Part 1:** Mandatory Pre-requisites & Government Approvals (SEBI, NSE, BSE, MCX, CDSL, VAPT, Net Worth ₹1 Cr+)
- **Part 2:** Legal Documentation & Regulatory Readiness Checklist
- **Part 3:** Decoded 14-Step User KYC & Onboarding Journey (Digio, HyperVerge, Penny Drop, DDPI)
- **Part 4:** Complete Technical Stack & 12 Flutter Modules (`chart` 60fps canvas, `mscalper_train`, Kyro AI)
- **Part 5:** Itemized Cost Breakdown (Development, Third-Party APIs, Cloud, Exchange, Compliance, Team)
- **Part 6:** Strategic Route Comparison: Model A (Own SEBI License) vs Model B (Partner API Model)
- **Part 7:** Project Roadmap, Milestones & Payment Schedule

---

## 📑 Repository Structure

```
sahi/
├── README.md                            # Master overview & index (this file)
├── Sahi_Trading_App_Client_Proposal.pdf # Master Single PDF for Client Proposal
├── Sahi_Trading_App_Client_Proposal.html# HTML Source for the PDF Document
├── generate_proposal_pdf.py             # Script to regenerate PDF via Chrome Headless
├── .gitignore                           # Ignores apk/ directory & binaries
└── analysis/
    ├── Sahi_Trading_App_Client_Proposal.pdf # Mirror copy of Master PDF
    ├── 01_app_overview.md               # Product identity, features, and regulatory breakdown
    ├── 02_technical_architecture.md     # Backend microservices, OMS, RMS, and WebSocket design
    ├── 03_build_steps.md                # 10-phase detailed engineering master plan
    ├── 04_cost_summary.md               # Quick phase-wise capital investment summary
    ├── 05_build_roadmap.md              # Detailed implementation guide with code samples
    ├── 06_libraries_stack.md            # Detected libraries and recommended production tech stack
    ├── 07_cost_breakdown.md             # 11 comprehensive cost tables (from legal to marketing)
    ├── 08_decompiled_deep_findings.md   # [BREAKTHROUGH] Decompiled Flutter structure, Digio & HyperVerge
    └── decompiled/                      # Extracted metadata from JADX decompilation
        ├── AndroidManifest_decoded.json # Fully decoded AndroidManifest.xml
        ├── app_info.json                # Package details, SDK versions, permissions
        ├── main_classes.json            # Core application entry classes
        └── keyword_search.json          # Code search hits for endpoints & libraries
```

---

## 🔍 Key Reverse Engineering Discoveries

### 1. Framework & UI Architecture
* **Frontend:** Built with **Flutter (Dart)** with target Android 15/16 SDK (`compileSdkVersion 36`, `targetSdkVersion 36`).
* **Chart Engine (`packages/chart`):** In-house custom Canvas charting engine built in Flutter rendering 60 FPS tick-by-tick candles without webview overhead.
* **Kyro AI Assistant (`packages/ai_assistant`):** Natural language indicator generator with custom Lottie animations (`thinking_intro.json`, `orb/glow`).
* **SahiScript (`packages/sahiscript_ui`):** Proprietary scripting language and code editor for custom technical indicators.
* **Practice Terminal (`packages/mscalper_train`):** Dedicated paper-trading sandbox with trade playback, simulation, and 1-tap execution.

### 2. Third-Party Vendor Stack (Confirmed via Code & Manifest)
* **KYC, e-Sign & Mandates:** **Digio** (`in.digio.sdk`, `com.ecs.dbsekycapi.ESignActivity`, `com.digio.esignMandate`) — handles Aadhaar e-Sign, Digilocker, and DDPI.
* **AI Liveness & Face Match:** **HyperVerge** (`co.hyperverge.hyperkyc`) — handles AI OCR and biometric liveness checks.
* **Customer Support:** **Freshworks / Freshchat** (13 dedicated in-app activities).
* **Push & User Engagement:** **MoEngage** (`com.moengage.flutter` v10.9.0).
* **Crash & Performance:** **New Relic** (Session Replay & APM) + **Sentry Android SDK**.
* **Attribution:** **AppsFlyer** (`assets/com/appsflyer/internal/*`).
* **Payments:** Direct Android Intent to **Google Pay, PhonePe, Paytm, CRED** + Digio UPI.

---

## 📚 Complete Documentation Index

| Document | Description |
|---|---|
| **[08. Decompiled Deep Findings](./analysis/08_decompiled_deep_findings.md)** | **[CORE FINDINGS]** Full JADX decompilation report: Flutter modular packages, Digio/HyperVerge integration, and decoded 14-step onboarding flow. |
| **[01. App Overview & Identity](./analysis/01_app_overview.md)** | Business model, brokerage structure (₹10/order flat), exchange credentials, and feature breakdown. |
| **[02. Technical Architecture](./analysis/02_technical_architecture.md)** | Microservice architecture, low-latency market data pipeline (Kafka/WebSocket), and database design. |
| **[03. Step-by-Step Build Guide](./analysis/03_build_steps.md)** | Detailed 10-phase roadmap covering regulatory setup, team hiring, infra, exchange integration, and testing. |
| **[04. Cost Summary Tables](./analysis/04_cost_summary.md)** | Consolidated phase-by-phase financial summary for executive planning. |
| **[05. Implementation Roadmap](./analysis/05_build_roadmap.md)** | Detailed engineering guide with production code patterns (Go WebSocket server, Flutter Canvas chart, Order models). |
| **[06. Libraries & Recommended Stack](./analysis/06_libraries_stack.md)** | Complete library inventory and suggested tech stack for building an identical trading platform. |
| **[07. Complete Cost Breakdown](./analysis/07_cost_breakdown.md)** | 11 comprehensive cost tables covering legal, dev, team, AWS infrastructure, exchange feeds, and marketing. |

---

## 💰 Capital & Cost Summary

```
┌──────────────────────────────────────┬──────────────────────┬─────────────────┐
│ Business Model                       │ Year 1 Investment    │ Time to Market  │
├──────────────────────────────────────┼──────────────────────┼─────────────────┤
│ 1. Partner / Sub-Broker Model        │ ₹1.5 – 3.5 Crore     │ 4 – 6 Months    │
│    (Built on Zerodha / Dhan APIs)    │                      │                 │
│ 2. Own SEBI Stock Broker Entity     │ ₹4.5 – 8.0 Crore     │ 12 – 18 Months  │
│    (Self-Clearing, NSE/BSE/MCX)      │                      │                 │
└──────────────────────────────────────┴──────────────────────┴─────────────────┘
```

> **Strategic Recommendation:** To minimize early capital burn and regulatory lag, initiate development with **Flutter + Digio + Broker APIs (Zerodha/Dhan)** to launch within 6 months. Once product-market fit (PMF) is proven with 25K+ active traders, transition to an independent SEBI Stock Broker license.

---

*Analysis performed using static and headless decompilation tools (`jadx-headless-mcp`). All trademarks and brand names belong to their respective owners.*

