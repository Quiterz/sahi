# Sahi Trading App — Technical Architecture Deep Dive

## System Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    CLIENT LAYER                         │
│  Android App (Kotlin/Jetpack)  │  Web App (React/Next) │
└────────────────────┬────────────────────────────────────┘
                     │ HTTPS REST + WebSocket
┌────────────────────▼────────────────────────────────────┐
│                    API GATEWAY / LOAD BALANCER          │
│          (AWS ALB / Nginx / Cloudflare)                 │
└──────┬──────────────┬────────────────┬──────────────────┘
       │              │                │
┌──────▼──────┐ ┌─────▼──────┐ ┌──────▼──────┐
│  Auth        │ │  Trading    │ │  Market      │
│  Service     │ │  Engine     │ │  Data Feed   │
│  (Go/Node)   │ │  (Go/Java)  │ │  Service     │
└──────┬──────┘ └─────┬──────┘ └──────┬──────┘
       │              │                │
┌──────▼──────────────▼────────────────▼──────────────────┐
│                    DATA LAYER                           │
│  PostgreSQL │ Redis │ TimescaleDB │ Kafka │ S3/GCS      │
└─────────────────────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│              EXCHANGE CONNECTIVITY LAYER                │
│    NSE (FIX/NEAT)  │  BSE (BOLT)  │  MCX (CTCL)       │
└─────────────────────────────────────────────────────────┘
```

## Mobile App Architecture (Android)

### Language & Framework
- **Primary Language:** Kotlin (100% native)
- **Minimum SDK:** Android 6.0+ (inferred from library set)
- **Build System:** Gradle with multi-DEX support
- **Architecture Pattern:** MVVM (Model-View-ViewModel)

### Layer Breakdown

#### 1. Presentation Layer (UI)
- **Activity/Fragment** navigation via Jetpack Navigation Component
- **DataBinding** for declarative view binding
- **RecyclerView** for high-performance list rendering (watchlists, option chains, order books)
- **Custom Chart Engine** — proprietary in-house canvas rendering (NOT TradingView)
  - Renders candlestick, line, area charts
  - Low-latency tick updates (target <16ms frame time)
  - Touch-based interaction (pinch-to-zoom, pan, crosshair tap)
  - Overlay rendering (indicators, S/R levels, OI zones)
- **Material Design 3** components throughout
- **CoordinatorLayout + DrawerLayout** for screen structure

#### 2. ViewModel / State Management Layer
- **ViewModel** (lifecycle-aware, survives rotation)
- **LiveData / StateFlow** for reactive UI updates
- **Kotlin Coroutines** (DebugProbesKt.bin confirms coroutines usage)
- **DataStore** for persisting user preferences (watchlists, scalper settings, indicator configs)

#### 3. Domain/Business Logic Layer
- Order placement validation
- Risk management pre-checks (margin sufficiency)
- Scanner filter logic
- AI indicator computation (local ML inference or server-side)
- Option strategy payoff graph computation

#### 4. Data/Repository Layer
- **OkHttp/Retrofit** for REST API calls (historical data, orders, portfolio)
- **WebSocket client** (OkHttp WebSocket or custom) for live market ticks
- **Room** or direct SQLite for local caching
- **DataStore (Preferences Proto)** for settings persistence

#### 5. Security Layer
- **Biometric Auth** (fingerprint/face via BiometricPrompt API)
- **Credential Manager** for secure credential storage
- **SSL/TLS pinning** (inferred for financial app)
- **ProGuard/R8** code obfuscation (production APK)

### Key Native Components
- **Camera2/CameraX:** KYC document capture (PAN, Aadhaar, signature)
- **ExifInterface:** Image processing for uploaded KYC documents

---

## Backend Architecture

### Services Architecture (Microservices)

#### 1. Authentication Service
- **JWT-based** session tokens
- **OTP verification** via SMS gateway (Msg91/Twilio)
- **Aadhaar e-KYC** via UIDAI certified KUA
- **PAN verification** via NSDL/UTI API
- **Bank account verification** via Penny Drop API (Razorpay Thirdwatch / Cashfree)

#### 2. Market Data Feed Service
- **Direct exchange connection** to NSE, BSE, MCX via CTCL/FIX protocol
- **Tick normalizer:** Converts raw binary exchange messages to internal JSON/Protobuf format
- **WebSocket broadcast server:** Fans out normalized ticks to subscribed clients
- **OHLC aggregator:** Builds candles (1s, 1m, 5m, 15m, 1h, 1D) in real-time using stream processor
- **Time-series storage:** TimescaleDB or ScyllaDB for historical OHLC data

#### 3. Order Management System (OMS)
- Receives order requests from clients
- Validates against risk parameters (margin, exposure limits, SEBI regulations)
- Routes orders to exchange via broker's CTCL terminal or FIX engine
- Stores order state in PostgreSQL (ACID compliance for financial records)
- Publishes order updates back to client via WebSocket

#### 4. Risk Management System (RMS)
- Real-time margin checking
- Position limit enforcement (SEBI/exchange mandated)
- Intraday position squareoff automation (at market close or margin shortfall)
- F&O exposure limit checks

#### 5. Portfolio & Holdings Service
- Fetches CDSL holdings via CDSL API
- Calculates realized/unrealized P&L
- Manages fund transfer records

#### 6. KYC Service
- Aadhaar XML verification via DigiLocker
- CKYC (Central KYC) registry check and upload
- IPV (In-Person Verification) via selfie video
- Document upload to secure S3/GCS bucket

#### 7. AI/ML Service
- Market sentiment computation (updated every 5 min)
- Key level detection (support/resistance from OI data)
- Custom indicator execution engine (Kyro scripting runtime)
- Buzzing stocks signal generation

### Database Stack
| Database | Usage |
|----------|-------|
| PostgreSQL | User accounts, orders, trades, holdings, financial records (ACID) |
| Redis | WebSocket session registry, order book cache, real-time P&L |
| TimescaleDB or ScyllaDB | Historical OHLC candlestick data (time-series) |
| S3/GCS | KYC documents, app assets, APK distribution |
| Elasticsearch | Instrument search, logs, audit trail |

### Message Queue
- **Apache Kafka** (or AWS Kinesis) for high-throughput event streaming:
  - Market tick events
  - Order state change events
  - Risk alert events
  - Audit log events

### Infrastructure
- **Cloud Provider:** AWS (Mumbai region, ap-south-1) — inferred from Indian fintech standard
- **Containers:** Docker + Kubernetes (EKS) for service orchestration
- **CDN:** CloudFront or Cloudflare for static assets + DDoS protection
- **Monitoring:** Sentry (confirmed from APK) + CloudWatch/Datadog
- **Crash Reporting:** Sentry SDK (confirmed in APK)

---

## Real-Time Data Flow

```
NSE Exchange ──FIX/NEAT──► Feed Handler ──normalize──► Kafka Topic
                                                              │
                                                    ┌─────────▼──────────┐
                                                    │  WebSocket Server   │
                                                    │  (fan-out to 10k+  │
                                                    │   subscribers)      │
                                                    └─────────┬──────────┘
                                                              │ WebSocket
                                                    ┌─────────▼──────────┐
                                                    │   Android App       │
                                                    │   (Chart renders   │
                                                    │    at 60fps)        │
                                                    └────────────────────┘
```

## Security Architecture
1. **Transport Security:** TLS 1.3 for all API and WebSocket connections
2. **Certificate Pinning:** Expected for financial grade app (prevents MITM)
3. **Biometric Auth:** Android BiometricPrompt (fingerprint/face), no passwords stored on device
4. **Code Obfuscation:** R8/ProGuard applied (production APK shows obfuscated class names)
5. **VAPT Audits:** Mandatory for SEBI-registered brokers (quarterly)
6. **Data Localization:** All user/financial data stored in India (RBI mandate)
7. **Two-Factor Auth (2FA):** OTP-based on login and order placement

---

## Third-Party Service Integrations
| Service | Purpose |
|---------|---------|
| Sentry | Crash reporting & performance monitoring |
| NPCI/UPI | Fund deposit via UPI (PhonePe, GPay, etc.) |
| DigiLocker | Aadhaar XML for KYC |
| NSDL/UTI | PAN card verification |
| CDSL | Demat account and holdings |
| NSE/BSE/MCX | Exchange connectivity |
| SMS Gateway (Msg91/Twilio) | OTP delivery |
| Google Firebase | Push notifications (FCM), Analytics |
| Google AdServices | Privacy Sandbox integration |
| Play Store / App Store | App distribution |
