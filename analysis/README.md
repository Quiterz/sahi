# 🏦 Sahi Trading App — Complete Analysis & Build Guide

> **Project:** Reverse engineering analysis + complete clone-building roadmap  
> **Source:** Sahi Trading App (https://www.sahi.com/ | base.apk)  
> **Company:** Aaritya Broking Private Limited (SEBI Reg: INZ000317632)  
> **Analysis Date:** October 2026  
> **APK SHA-256:** `9fff890ca793882e229d29a17b7c87931056556d6df3e88524ff037bb715e19f`

---

## 📁 Folder Structure

```
sahi/
├── apk/
│   └── base.apk                        # Original APK (55.3 MB, SHA-256: 9fff890ca7...)
└── analysis/
    ├── README.md                        # Master Index & Overview
    ├── 01_app_overview.md               # Product features & regulatory identity
    ├── 02_technical_architecture.md     # System architecture, backend design, data flow
    ├── 03_build_steps.md                # 10-phase detailed build guide
    ├── 04_cost_summary.md               # Consolidated cost summary tables
    ├── 05_build_roadmap.md              # Detailed implementation guide with code samples
    ├── 06_libraries_stack.md            # Library inventory & recommended tech stack
    ├── 07_cost_breakdown.md             # Complete cost breakdown (11 detailed tables)
    └── 08_decompiled_deep_findings.md   # JADX deep decompilation findings & architecture
```

---

## 📋 Complete Document Index

1. **[08_decompiled_deep_findings.md](./08_decompiled_deep_findings.md)** — **[BREAKTHROUGH REPORT]** Exact findings from decompiling with JADX v0.8.0. Unveils Flutter modular architecture, Digio & HyperVerge KYC integration, SahiScript & Kyro AI implementation, and full 14-step onboarding journey.
2. **[01_app_overview.md](./01_app_overview.md)** — Comprehensive product overview, regulatory credentials, and feature matrix.
3. **[02_technical_architecture.md](./02_technical_architecture.md)** — Microservices, OMS, RMS, market data feed, and database infrastructure.
4. **[03_build_steps.md](./03_build_steps.md)** — Step-by-step master plan from Day 1 to launch.
5. **[04_cost_summary.md](./04_cost_summary.md)** — Quick phase-by-phase financial investment summary.
6. **[05_build_roadmap.md](./05_build_roadmap.md)** — Engineering implementation roadmap with Kotlin/Go/Flutter snippets.
7. **[06_libraries_stack.md](./06_libraries_stack.md)** — Third-party vendor comparison and SDK reference.
8. **[07_cost_breakdown.md](./07_cost_breakdown.md)** — 11 detailed tables covering every rupee from legal registration to deployment.

---

## 📊 Quick Summary — What Is Sahi?

| Property | Value |
|----------|-------|
| **Type** | SEBI-registered discount stock broker |
| **Entity** | Aaritya Broking Private Limited |
| **Tagline** | India's fastest trading app for active traders |
| **Target Users** | Intraday traders, options scalpers, F&O traders |
| **Platform** | Android (Kotlin native), iOS, Web |
| **Instruments** | Equity, F&O, MCX Commodities, ETFs, IPOs |
| **Brokerage** | ₹10 flat per order (F&O + intraday) |
| **Account Opening** | Free, paperless, Aadhaar-linked |
| **Unique Feature** | Options Scalper 2.0 + 18 AI indicators + Kyro |

---

## 📋 Document Index

### 1. [App Overview & Feature Analysis](./01_app_overview.md)
Complete product breakdown including:
- All trading features (scalper, charts, scanners, AI, options chain)
- Regulatory identity (SEBI reg numbers, exchange memberships)
- APK static analysis results (libraries, file count, structure)
- Website analysis
- Brokerage pricing model
- KYC onboarding process

### 2. [Technical Architecture](./02_technical_architecture.md)
Deep technical dive into:
- Mobile app architecture (Kotlin, MVVM, Jetpack)
- Backend system design (microservices, OMS, RMS)
- Real-time data flow (WebSocket, Kafka, NSE feed)
- Database stack (PostgreSQL, Redis, TimescaleDB)
- Security architecture (biometric, TLS, certificate pinning)
- Exchange connectivity (NSE FIX/CTCL, BSE BOLT, MCX)
- Third-party integrations (Sentry, NPCI/UPI, Firebase)

### 3. [Step-by-Step Build Guide](./03_build_steps.md)
10-phase development roadmap:
- Phase 1: SEBI/NSE/BSE/MCX registration process
- Phase 2: Product planning and UX design
- Phase 3: Team hiring and structure
- Phase 4: Infrastructure setup (AWS)
- Phase 5: Backend development (auth, KYC, OMS, RMS, data)
- Phase 6: Exchange connectivity
- Phase 7: Android app development
- Phase 8: Testing and QA
- Phase 9: App Store submission and launch
- Phase 10: Post-launch operations

### 4. [Cost Analysis (Summary)](./04_cost_breakdown.md)
Summary-level cost breakdown per phase

### 5. [Detailed Build Roadmap with Code](./05_build_roadmap.md)
Extremely detailed phase-wise guide with:
- Code examples in Kotlin, Go, Bash
- Architecture diagrams
- Infrastructure-as-code snippets
- Database schema guidance
- WebSocket implementation pattern
- Chart engine implementation
- Exchange FIX protocol integration guide

### 6. [Libraries & Tech Stack](./06_libraries_stack.md)
- All 40+ AndroidX libraries confirmed from APK analysis
- Third-party SDKs detected (Sentry, NPCI, Material Design, Camera, Biometric)
- Custom components identified (in-house chart engine)
- Recommended modern equivalent stack with exact versions
- Backend technology choices (Go, PostgreSQL, Redis, Kafka)
- Third-party API providers for India (KYC, payments, SMS)

### 7. [Complete Cost Breakdown Tables](./07_cost_breakdown.md)
11 detailed cost tables covering:
- One-time regulatory & legal costs (₹50L–₹1 Cr)
- Development costs (₹1.5Cr–₹3.7Cr for full build)
- Team salaries (₹1.8Cr–₹4.3Cr/year)
- Infrastructure costs (₹11L–₹1.6Cr/year, scale-dependent)
- Annual regulatory fees (₹40L–₹89L/year)
- Third-party services (₹17L–₹55L/year)
- Marketing budget (₹28L–₹1.28Cr/year)
- Alternative "partner model" (₹1.5Cr–₹3.5Cr total Year 1)
- Revenue model and break-even analysis
- Funding requirements
- Competitor benchmarks

---

## 💰 Cost At a Glance

| Scenario | Year 1 Total Investment |
|----------|------------------------|
| **Full SEBI-licensed broker** (own OMS, exchange membership) | **₹4–8 Crore** |
| **Sub-broker / Partner API model** (front-end on Zerodha/Dhan APIs) | **₹1.5–3.5 Crore** |
| **MVP only** (equity + basic charts, no AI, no scalper) | **₹2–4 Crore** |

---

## 🚀 Build Timeline

```
Month 1-2:   Legal entity + SEBI/exchange applications + UX design
Month 3-4:   Exchange approval + team hiring + infra setup
Month 5-8:   Backend development (auth, OMS, market data, KYC)
Month 7-10:  Android app development (chart engine, trading UI)
Month 9-11:  Integration testing + VAPT + mock trading certification
Month 11-12: App Store submission + beta launch
Month 12+:   Public launch + marketing + scale
```

---

## 🛠️ Tech Stack Summary

### Android App
| Layer | Technology |
|-------|-----------|
| Language | Kotlin |
| Architecture | MVVM + Clean Architecture |
| Async | Kotlin Coroutines + Flow |
| DI | Hilt |
| Navigation | Jetpack Navigation Component |
| Network | Retrofit + OkHttp |
| Local Storage | Room + DataStore |
| Charts | Custom Canvas (in-house, NOT TradingView) |
| Auth | BiometricPrompt + JWT |
| Camera | CameraX |
| Monitoring | Sentry |
| Push | Firebase FCM |

### Backend
| Layer | Technology |
|-------|-----------|
| Auth Service | Go + Gin |
| OMS/RMS | Go or Java |
| Market Data | Go + WebSocket |
| AI Service | Python + FastAPI |
| Database | PostgreSQL (ACID) |
| Cache | Redis |
| Time-Series | TimescaleDB / ScyllaDB |
| Queue | Apache Kafka |
| Infrastructure | AWS EKS (Kubernetes) |
| Monitoring | Sentry + CloudWatch |

---

## ⚠️ Key Risks & Blockers

| Risk | Severity | Mitigation |
|------|----------|-----------|
| SEBI/exchange approval takes 6+ months | 🔴 High | Start legal process on Day 1 |
| Exchange FIX/CTCL integration complexity | 🔴 High | Hire specialized exchange integration engineer |
| Custom chart engine takes 4+ months | 🟡 Medium | Start with TradingView, migrate to custom |
| VAPT audit failure delays launch | 🟡 Medium | Engage CERT-in firm early, fix proactively |
| Net worth requirement (₹1 Cr) | 🔴 High | Secure investor commitment before applying |
| 64-bit DEX limit (65K methods) | 🟢 Low | Multi-DEX enabled in Sahi APK |
| Market data feed NSE costs | 🟡 Medium | Budget ₹3.75L–₹35L/year |

---

## 📞 Key Regulatory Contacts

| Authority | Contact |
|-----------|---------|
| SEBI (for broker registration) | https://www.sebi.gov.in/registration.html |
| NSE Membership | https://www.nseindia.com/membership |
| BSE Membership | https://www.bseindia.com/markets/membership |
| MCX Membership | https://www.mcxindia.com/membership |
| CDSL (Depository) | https://www.cdslindia.com/BOs/dp-info |
| CERT-In (VAPT vendors) | https://www.cert-in.org.in/empanelled |

---

## 🔍 Analysis Methodology

### APK Analysis (Static)
- Tool: **REA (Reverse Engineering Agent)** MCP server
- Method: `inspect_artifact` → `inspect_analysis_view` → inventory analysis
- Coverage: 6,355 files, 2,157 archive entries examined
- Limitations: JADX (code decompiler) not available; code-level analysis limited to library detection from META-INF files and resources

### Website Analysis
- Tool: Web search + sahi.com direct content analysis
- Coverage: Feature pages, pricing page, legal/regulatory pages, blog

### Technology Stack Research
- Sources: Sahi.com, industry publications, Google Play store listing, regulatory filings, web research

---

*Analysis conducted using REA static analysis + web research. All cost figures are estimates based on publicly available data and industry benchmarks. Regulatory requirements are subject to change per SEBI/exchange circulars. Consult a SEBI-registered compliance professional before starting a broker entity.*
