# Sahi Trading App — Deep Analysis Report
## App Overview & Product Identity

**App Name:** Sahi  
**Company:** Aaritya Broking Private Limited  
**Website:** https://www.sahi.com/  
**APK File:** base.apk (SHA-256: 9fff890ca793882e229d29a17b7c87931056556d6df3e88524ff037bb715e19f, 55.3 MB)  
**Platform:** Android (native Kotlin)  
**Target Market:** Active Indian retail traders — equity, F&O, and MCX commodity traders  
**Positioning:** Ultra-fast, low-latency, single-screen trading platform for scalpers and options traders

---

## Regulatory & Legal Identity

| Detail | Value |
|--------|-------|
| Corporate Entity | Aaritya Broking Private Limited |
| SEBI Stock Broker Reg. | INZ000317632 |
| NSE Member ID | 90375 |
| BSE Member ID | 6867 |
| MCX Member ID | 57630 |
| CDSL DP Registration | IN-DP-780-2024 |
| Research Analyst Reg. | INH000022172 |
| KYC Mode | Paperless, Aadhaar-linked digital e-KYC |

---

## Core Product Features

### 1. Trading Instruments Supported
- **Equity (NSE/BSE):** Intraday + Delivery (CNC)
- **Futures & Options (F&O):** Nifty, Bank Nifty, FinNifty, Midcap Nifty
- **Commodities (MCX):** Crude Oil, Gold, Silver, Natural Gas (full-size, mini, micro contracts + commodity options)
- **IPOs:** Initial Public Offerings subscription
- **ETFs:** Exchange Traded Funds

### 2. Charting & Market Data Engine
- **In-house native charting** — NOT TradingView (custom-built for lower latency)
- **60% faster rendering** than competitor platforms (claimed)
- **20+ real-time live scanners** running throughout market session:
  - Volume spike scanners
  - 52-week high/low breakout scanners
  - Top gainers/losers
  - RSI extreme scanners
  - OI surge scanners
- **Low-latency tick-by-tick data** via WebSocket streams from NSE/BSE/MCX
- **Drag-and-drop Stop Loss / Target** directly on chart

### 3. Sahi Scalper 2.0 (Flagship Feature)
The premium single-screen options trading terminal:
- **Dual synced charts:** Index + Option chart simultaneously (e.g., Nifty spot + Nifty 24000 CE)
- **Synced crosshairs** across all open chart windows
- **1-tap order execution** from charts and option chains
- **Smart Limit Exits:** Best Bid, LTP, Midpoint options
- **Auto-Split:** Splits large orders automatically at exchange freeze limits
- **Funds Pill:** Real-time margin display within the scalper UI
- **Trailing Stop-Loss (TSL):** Automated profit-locking feature
- **Floating "Sahi Pulse":** PiP (Picture-in-Picture) P&L overlay — stays visible when switching screens

### 4. Sahi AI & Machine Intelligence
- **18 built-in AI/ML indicators** directly on charts (no external plugins needed):
  - Lorentzian Classification
  - Nadaraya-Watson Envelopes
  - SuperTrend AI variants
- **AI Bullish/Bearish Market Sentiment:** Updated every 5 minutes
- **Kyro:** Natural language indicator builder — users describe strategy in plain English, AI generates indicator
- **AI Key Levels:** OI-identified support & resistance zones overlaid on charts
- **Buzzing Stocks:** Real-time unusual volume/momentum alerts

### 5. Options Chain & Greeks
- **Customizable option chain** with live data:
  - Greeks: Delta, Gamma, Theta, Vega
  - Max Pain levels
  - Open Interest (OI) profiles and trends
  - Volume Put-Call Ratio (PCR)
  - OI-based support/resistance

### 6. Options Strategy Builder
- Multi-leg strategy construction
- Payoff graphs
- Probability-of-profit calculations
- Execute strategy directly from builder

### 7. Watchlists & Portfolio
- Real-time watchlists with 1-tap order placement
- Portfolio P&L tracking
- Holdings management (demat view)
- Order history and trade book

### 8. KYC & Account Onboarding
- 100% paperless digital onboarding
- Aadhaar OTP-based e-KYC
- PAN verification
- Bank account linking (cancelled cheque/passbook upload)
- Income proof for F&O activation
- CDSL Demat account creation in-app

### 9. Brokerage Model
- **Free account opening:** ₹0
- **AMC (Annual Maintenance Charge):** ₹0
- **Equity Delivery/Intraday:** ₹10 or 0.05% per executed order (lower applies)
- **F&O (Futures & Options):** Flat ₹10 per executed order
- **Government levies apply:** STT, GST (18%), stamp duty, SEBI turnover charges

### 10. Notifications & Alerts
- Price alerts (set from charts or watchlist)
- Order execution push notifications
- Market opening/closing alerts
- Buzzing stock alerts

---

## User Experience (UX) Design Principles
1. **Speed-first design** — every interaction optimized for sub-second response
2. **Single-screen paradigm** — minimize screen switching during live trading
3. **Dark-mode native** — eye-friendly for long trading sessions
4. **Persistent session state** — remembers instruments, quantities, indicator configs across logins
5. **Mobile-first** — Android native (Kotlin), optimized for phone form factor

---

## APK Technical Summary (from REA static analysis)
| Property | Value |
|----------|-------|
| Format | APK (ZIP container) |
| Total Files | 6,355 entries |
| APK Size | 55.3 MB (57,980,795 bytes) |
| Signing | APK Signing Block present |
| AndroidManifest.xml | 68,516 bytes (binary encoded) |
| DEX Files | Multiple (multi-DEX enabled) |
| Native Libraries | Present (`.so` files) |
| Encryption | None detected |

---

## Key Libraries Identified (from META-INF and resource analysis)

### AndroidX / Jetpack Libraries
| Library | Purpose |
|---------|---------|
| androidx.activity | Activity management |
| androidx.appcompat | Backward compatibility |
| androidx.biometric | Biometric authentication (fingerprint/face) |
| androidx.camera (camera2, core, lifecycle, video, view) | Camera access (KYC document scan) |
| androidx.constraintlayout | Complex UI layouts |
| androidx.coordinatorlayout | Material design coordination |
| androidx.credentials | Credential manager API |
| androidx.databinding | Data binding framework |
| androidx.datastore | Preferences & data storage |
| androidx.drawerlayout | Navigation drawer |
| androidx.dynamicanimation | Physics-based animations |
| androidx.emoji2 | Emoji rendering |
| androidx.exifinterface | Image EXIF metadata |
| androidx.fragment | Fragment-based navigation |
| androidx.graphics.shapes | Adaptive icon shapes |
| androidx.lifecycle (viewmodel, livedata, runtime, process, service) | MVVM architecture |
| androidx.navigation (fragment, runtime, ui) | Navigation component |
| androidx.preference | Settings/preferences screens |
| androidx.profileinstaller | Baseline profiles for startup performance |
| androidx.recyclerview | List/grid rendering |
| androidx.browser | Chrome Custom Tabs (web content) |
| androidx.cardview | Card UI components |

### Third-Party Libraries Detected
| Library | Evidence | Purpose |
|---------|----------|---------|
| **Sentry** | `sentry_edit_text_border.xml`, `sentry_logo_dark.xml`, `sentry_oval_button_ripple_background.xml` | Crash reporting & error monitoring |
| **NPCI / UPI** | `npci_img.xml` (30KB SVG) | UPI payment integration |
| **Kotlin Coroutines** | `DebugProbesKt.bin` | Async/concurrent programming |
| **Material Design** | `mtrl_*` resources (extensive) | Google Material Design components |
| **AdServices / Privacy Sandbox** | `ads-adservices-java` version files | Google Privacy Sandbox / Ad targeting |
| **Biometric Auth** | `androidx.biometric` | Fingerprint/face login |
| **Camera2 / CameraX** | Camera library chain | Document scanning for KYC |

### Architecture Patterns (Inferred)
- **MVVM** with ViewModel + LiveData (confirmed by library set)
- **Kotlin Coroutines + Flow** for async state management
- **Navigation Component** for screen routing
- **DataStore** for local preference persistence (replacing SharedPreferences)
- **DataBinding** for view binding

---

## Website Analysis (sahi.com)
The website mirrors the app's positioning with:
- **Landing page:** Hero section showcasing Scalper 2.0 with video demos
- **Feature pages:** Charts, scanners, AI indicators, option chain
- **Pricing page:** Transparent brokerage calculator
- **Blog/Academy:** Trading education content (SEO/acquisition)
- **App download:** Direct APK + Play Store + iOS App Store links
- **Compliance footer:** SEBI, NSE, BSE, MCX, CDSL registrations listed
