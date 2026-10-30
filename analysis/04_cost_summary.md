# Sahi Trading App — Cost Summary (Phase-by-Phase)

> Detailed breakdown is in [07_cost_breakdown.md](./07_cost_breakdown.md)  
> This file provides a quick, consolidated summary.

---

## Total Investment Required (Year 1)

| Model | Min (₹) | Max (₹) |
|-------|---------|---------|
| Full SEBI-registered broker | 4,00,00,000 | 8,00,00,000 |
| Sub-broker / Partner API model | 1,50,00,000 | 3,50,00,000 |
| MVP only (basic features) | 2,00,00,000 | 4,00,00,000 |

---

## Phase-by-Phase Cost Breakdown

| Phase | What | Min (₹) | Max (₹) |
|-------|------|---------|---------|
| **Phase 1** | Legal + Regulatory (SEBI, NSE, BSE, MCX, CDSL, VAPT) | 49,88,000 | 1,00,00,000 |
| **Phase 2** | Product design + UX wireframes | 4,00,000 | 10,00,000 |
| **Phase 3** | Team salaries (Year 1, 10–12 people) | 1,84,80,000 | 4,26,00,000 |
| **Phase 4** | Infrastructure (AWS, Year 1, MVP scale) | 11,46,000 | 16,32,000 |
| **Phase 5–6** | Backend + Exchange connectivity dev | 60,00,000 | 1,30,00,000 |
| **Phase 7** | Android (+ iOS optional) app development | 25,00,000 | 60,00,000 |
| **Phase 8** | Testing, QA, security audit | 8,00,000 | 20,00,000 |
| **Phase 9** | App launch (store fees, beta testing) | 1,50,000 | 4,00,000 |
| **Phase 10** | Marketing (Year 1) | 28,00,000 | 1,28,00,000 |
| | **GRAND TOTAL** | **~₹4.72 Cr** | **~₹9.94 Cr** |

---

## One-Time Regulatory Costs (Detailed)

| Item | Min (₹) | Max (₹) | Refundable |
|------|---------|---------|-----------|
| Company Incorporation (MCA) | 8,000 | 15,000 | No |
| SEBI Application + Registration | 6,00,000 | 9,50,000 | No |
| NSE Admission (CM + F&O) | 8,00,000 | 17,00,000 | Partially |
| NSE Base Minimum Capital | 10,00,000 | 25,00,000 | Yes (on exit) |
| BSE Membership + Deposit | 10,50,000 | 15,00,000 | Partially |
| MCX Membership + Capital | 8,00,000 | 13,00,000 | Partially |
| CDSL DP Registration | 1,00,000 | 2,00,000 | Partially |
| VAPT Initial Audit | 2,00,000 | 6,00,000 | No |
| Net Worth Certificate | 50,000 | 1,00,000 | No |
| Legal Counsel | 2,00,000 | 5,00,000 | No |
| Office Setup | 1,00,000 | 5,00,000 | No |
| **TOTAL** | **~₹49.1 L** | **~₹99.65 L** | |

---

## Development Cost (One-Time)

| Component | Min (₹) | Max (₹) |
|-----------|---------|---------|
| Android App (full features) | 25,00,000 | 50,00,000 |
| iOS App | 12,00,000 | 25,00,000 |
| Backend (all services) | 40,00,000 | 1,00,00,000 |
| Custom Chart Engine | 10,00,000 | 25,00,000 |
| OMS + RMS | 17,00,000 | 40,00,000 |
| AI/ML Features | 12,00,000 | 32,00,000 |
| Exchange Connectivity | 15,00,000 | 38,00,000 |
| QA + DevOps + Design | 11,00,000 | 28,00,000 |
| **TOTAL** | **~₹1.42 Cr** | **~₹3.38 Cr** |

---

## Annual Recurring Costs

| Category | Annual Min (₹) | Annual Max (₹) |
|----------|---------------|---------------|
| Team Salaries | 1,84,80,000 | 4,26,00,000 |
| Infrastructure (AWS, MVP) | 11,46,000 | 16,32,000 |
| Infrastructure (AWS, Growth) | 1,59,60,000 | 3,54,00,000 |
| Regulatory (exchange fees, VAPT) | 40,00,000 | 89,00,000 |
| Third-party services | 17,00,000 | 55,00,000 |
| Marketing | 28,00,000 | 1,28,00,000 |
| **TOTAL (MVP stage)** | **~₹3.5 Cr/yr** | **~₹7.5 Cr/yr** |
| **TOTAL (Growth stage)** | **~₹5 Cr/yr** | **~₹12 Cr/yr** |

---

## NSE Market Data Feed Costs (Annual)

| Feed Type | Annual Cost (₹) | Use Case |
|-----------|----------------|---------|
| Level 1 (LTP, OHLC) — via CTCL | Included in membership | Basic charts, watchlist |
| Level 1 — Software vendor license | 3,75,000 – 10,00,000 | Redistribution to end users |
| Level 2 (Full order book depth) | 15,00,000 – 35,00,000 | Options chain depth, scalper |
| Historical Data (via vendor) | 30,000 – 3,00,000 | Chart history, backtesting |

---

## VAPT Compliance Schedule & Costs

| Audit | Frequency | Cost/Audit | Annual Total |
|-------|-----------|-----------|-------------|
| Application VAPT | Quarterly (min) | ₹2–6 L | ₹8–24 L |
| Network/Infrastructure VAPT | Quarterly | ₹1–3 L | ₹4–12 L |
| Mobile App Security Testing | Annual | ₹1.5–4 L | ₹1.5–4 L |
| **Annual VAPT Budget** | | | **₹13.5–40 L** |

---

## Compliance Reporting Calendar

| Frequency | Report | Filed With |
|-----------|--------|-----------|
| Daily | Trade reporting | NSE/BSE |
| Daily | Client fund reconciliation | Internal |
| Monthly | Client ledger statements | Clients |
| Monthly | Compliance certificate | SEBI |
| Quarterly | VAPT audit submission | SEBI |
| Quarterly | Net worth certificate | Exchanges |
| Annual | Audited financial statements | SEBI |
| Annual | SEBI registration renewal | SEBI |

---

## Quick Cost Comparison — Sahi vs Starting From Scratch

| Item | Sahi's Approx Investment | Starting From Scratch |
|------|------------------------|--------------------|
| Years building product | 3–4 years (est.) | 0 |
| Team size | 30–50 people (est.) | Start with 10 |
| Funding raised | Undisclosed (est. ₹30–100 Cr) | ₹4–10 Cr (Year 1) |
| SEBI registration | Already done | 3–6 months |
| Chart engine | In-house (4+ months work) | Use TradingView initially |
| AI features | 18 indicators + Kyro | Phase 2 |
| Users | Growing (est. 2L+) | 0 → target 50K Year 1 |

