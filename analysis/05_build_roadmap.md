# Sahi-Like Trading App — Complete Build Roadmap
## Step-by-Step Development Guide (Phase-Wise)

> **Total Timeline:** 12–18 months for a full-featured SEBI-registered trading app  
> **Minimum Timeline:** 6–8 months for a partner-API-based front-end terminal  

---

## PHASE 1: Legal & Regulatory Foundation (Months 1–4)

### Step 1.1 — Incorporate the Company
- Register a **Private Limited company** with MCA (Ministry of Corporate Affairs)
- Required documents: Identity proofs, address proofs, MOA/AOA (Memorandum/Articles of Association)
- Use professionals: CA + company secretary
- **Tool:** MCA21 portal (https://www.mca.gov.in)
- **Output:** Certificate of Incorporation, PAN, TAN, GST registration
- **Cost:** ₹8,000–₹15,000
- **Time:** 7–15 business days
- **Blocker:** Director DIN (Director Identification Number) must be in order

### Step 1.2 — SEBI Stock Broker Registration
This is the most critical and time-consuming step.
- **Eligibility:** Net worth ≥ ₹1 Crore (for Trading Member)
- **Application:** File SEBI Form A online via SEBI's SCORES portal
- **Documents Required:**
  - Certificate of Incorporation
  - MOA/AOA
  - Audited financial statements (Net Worth Certificate)
  - KYC of all directors and promoters
  - Infrastructure proof (office space, IT systems)
  - Appointment letter for Principal Officer and Compliance Officer
  - Bank account statements
  - Business plan
- **Exchange membership required FIRST:** SEBI registration follows exchange approval
- **Fee:** ₹1,00,000 application fee + 18% GST
- **Time:** 3–6 months (including SEBI inspection)
- **Blocker:** Exchange memberships must be obtained first (SEBI validates them)

### Step 1.3 — NSE Membership Application
- Apply for **NSE Trading Membership** in segments needed:
  - CM (Capital Market / Equity)
  - F&O (Futures & Options)
  - CD (Currency Derivatives, optional)
- **Process:**
  1. Submit application to NSE membership department
  2. Pay application processing fee (~₹5,000–10,000 + GST per segment)
  3. Pay admission fee (₹5L–₹10L per segment)
  4. Submit Base Minimum Capital (BMC) — via FDR or Bank Guarantee
  5. NSE inspection of systems and premises
  6. Mock trading certification (CTCL/NEAT system)
  7. Go-live approval
- **BMC Required:** ₹10L–₹25L (FDR/BG, returned if membership terminated)
- **Time:** 3–5 months

### Step 1.4 — BSE Membership Application
- Apply for **BSE Deposit Based Membership (DBM)**
- Segments: Equity (A, B, T), F&O
- **Earnest Money Deposit (EMD):** ₹1,00,000 (non-refundable with application)
- **Deposit:** ₹10,00,000 minimum (cash or FDR)
- **Annual subscription:** ₹1L+ per segment
- **Time:** 2–4 months (often concurrent with NSE)

### Step 1.5 — MCX Membership (Optional Phase 1)
- Required for commodity trading (Gold, Crude Oil, etc.)
- Similar process to NSE/BSE
- **Fee:** ₹5L–₹8L
- **Time:** 2–4 months
- Can be deferred to Phase 2 if initial focus is equity + F&O only

### Step 1.6 — CDSL/NSDL DP Registration
- **Depository Participant (DP)** registration to open Demat accounts for customers
- Choose **CDSL** (more common for new brokers) or NSDL
- **Registration:** IN-DP-XXX-YYYY
- **Fee:** ₹1L–₹2L
- **Time:** 2–3 months
- **API:** CDSL e-DIS API for Demat holdings access

### Step 1.7 — Appoint Compliance Team
- **Compliance Officer:** NISM certification required (NISM Series-VII exam)
- **Principal Officer:** Experience in securities market
- Compliance officer salary: ₹50,000–₹1,25,000/month
- Set up compliance calendar (monthly SEBI reports, quarterly VAPT, etc.)

### Step 1.8 — Net Worth Certificate
- Prepared by SEBI-registered Chartered Accountant
- Must show ≥ ₹1 Crore net worth for Trading Member
- Updated annually with audited financial statements
- **Cost:** ₹50,000–₹1,00,000

### Step 1.9 — VAPT Security Audit
- **Mandatory:** SEBI requires Vulnerability Assessment and Penetration Testing
- Must be done by **CERT-in empaneled** security firm
- **Frequency:** Quarterly (at minimum annually before operations)
- **Cost per audit:** ₹2L–₹6L
- **Annual cost:** ₹8L–₹24L
- Scope: Trading platform, mobile app, backend systems, admin panel

### Step 1.10 — KYC Registration Agency (KRA) Empanelment
- Register with a SEBI-recognized KRA (e.g., CVL KRA, NDML KRA)
- Enables CKYC data sharing and verification
- Required for paperless onboarding

---

## PHASE 2: Product Planning & Design (Months 1–2, Parallel)

### Step 2.1 — Define MVP Feature Set
Recommended MVP (Minimum Viable Product) for launch:
- ✅ User registration + e-KYC onboarding
- ✅ Watchlist (20 stocks)
- ✅ Real-time price streaming (LTP)
- ✅ Buy/Sell order placement (equity + F&O)
- ✅ Basic candlestick chart (1min, 5min, 1D)
- ✅ Portfolio & holdings view
- ✅ Order book and trade history
- ✅ Funds management (deposit via UPI)
- ✅ Push notifications (order execution, price alerts)
- ⬜ Options chain (Phase 2)
- ⬜ Scalper terminal (Phase 2)
- ⬜ AI indicators (Phase 2)
- ⬜ Scanner (Phase 2)

### Step 2.2 — Competitive Analysis
Study these competitors thoroughly:
| Platform | USP | Weakness |
|----------|-----|---------|
| Zerodha Kite | Market leader, reliable | Slow innovation, dated UI |
| Dhan | Fast UI, good charts | Relatively new, less trust |
| Upstox | Cheap | Average UX |
| Groww | Great UX, mutual funds | Not for active traders |
| **Sahi** | Speed + scalper + AI | New entrant |
| TradingView | Best charts | Not a broker |
| Sensibull | Best options UI | Not a broker, add-on |

Your differentiation: Define your single biggest USP before coding starts.

### Step 2.3 — Brand Identity
- **Name:** Short, memorable, Indian-cultural (Sahi = "correct/right" in Hindi)
- **Logo:** Simple, clean, works at 24px app icon size
- **Colors:** Dark theme primary (trading apps are dark), accent color for buy (green) and sell (red)
- **Typography:** Inter or Nunito for numbers (legibility is critical)
- **Tools:** Figma for design, Lottie for animations

### Step 2.4 — UX Wireframes
Critical screens to wireframe:
1. Splash + Login (OTP entry)
2. KYC onboarding (8-step flow)
3. Home / Dashboard
4. Watchlist (compact, sortable)
5. Stock detail + chart
6. Buy/Sell bottom sheet
7. Option chain
8. Scalper terminal (most complex)
9. Portfolio
10. Funds/Add money
11. Order history
12. Settings/Profile

**Tools:** Figma + FigJam for flows  
**Time:** 3–4 weeks with a dedicated designer

---

## PHASE 3: Team Hiring (Months 1–3)

### Priority Hiring Order:
1. **CTO / Lead Architect** (first hire — drives all technical decisions)
2. **Senior Backend Engineer** (OMS, auth, market data)
3. **Senior Android Developer** (Kotlin native)
4. **DevOps/Infrastructure Engineer**
5. **UI/UX Designer**
6. **QA Engineer**
7. **iOS Developer** (can be delayed to Phase 2)
8. **ML/Data Engineer** (for AI features, Phase 2)

### Where to Hire:
- **LinkedIn Jobs** — for senior roles
- **AngelList/Wellfound** — for startup-enthusiastic engineers
- **Instahyre** — for quick Indian tech hires
- **Network referrals** — best quality, lower risk

### Salary Benchmarks (2024-2026, Bangalore/Mumbai/Hyderabad):
| Role | CTC/Year |
|------|----------|
| CTO (5+ yr exp) | ₹36L – ₹96L |
| Sr. Backend (Go/Kotlin, 4+ yr) | ₹18L – ₹36L |
| Sr. Android Dev | ₹18L – ₹36L |
| DevOps (3+ yr) | ₹14L – ₹30L |
| ML Engineer | ₹18L – ₹36L |
| UI/UX Designer | ₹10L – ₹24L |
| QA Engineer | ₹8L – ₹18L |

---

## PHASE 4: Infrastructure Setup (Months 3–4)

### Step 4.1 — Cloud Account Setup
- Create **AWS account** (or GCP — AWS recommended for Indian fintech)
- Apply for **AWS Activate** startup credits (up to $100K with VC backing)
- Set up multi-account structure: Dev, Staging, Production accounts
- Enable **AWS Shield** (DDoS protection, mandatory for financial apps)

### Step 4.2 — Networking & VPC
- Create VPC with public/private subnets
- NAT Gateway for private subnet internet access
- Security groups for each service tier
- WAF (Web Application Firewall) rules

### Step 4.3 — Database Setup
```bash
# PostgreSQL (RDS multi-AZ for production)
aws rds create-db-instance \
  --db-instance-identifier sahi-prod-db \
  --db-instance-class db.r6g.xlarge \
  --engine postgres \
  --multi-az \
  --storage-type gp3

# Redis (ElastiCache cluster for real-time data)
aws elasticache create-replication-group \
  --replication-group-id sahi-redis \
  --cache-node-type cache.r6g.large \
  --num-cache-clusters 3

# TimescaleDB for OHLC time-series data
# Deploy on EC2 or use Timescale Cloud
```

### Step 4.4 — Kubernetes Cluster (EKS)
```bash
eksctl create cluster \
  --name sahi-prod \
  --region ap-south-1 \
  --nodegroup-name standard-workers \
  --node-type m6i.xlarge \
  --nodes 3 \
  --nodes-min 2 \
  --nodes-max 10 \
  --managed
```

### Step 4.5 — CI/CD Pipeline
- **GitHub** for version control (private repositories)
- **GitHub Actions** for CI/CD:
  - On PR: Run tests + static analysis
  - On merge to main: Deploy to staging
  - On tag release: Deploy to production
- **Docker** for containerization
- **Helm** for Kubernetes deployment charts

### Step 4.6 — Monitoring Stack
```yaml
# Services to set up:
- Sentry: crash reporting (Android SDK + backend SDK)
- CloudWatch: AWS infrastructure metrics + logs
- Grafana + Prometheus: application metrics dashboards
- PagerDuty: on-call alerting
- ELK Stack (Elasticsearch + Logstash + Kibana): log search + audit trail
```

---

## PHASE 5: Backend Development (Months 3–8)

### Step 5.1 — Authentication Service
```go
// Technology: Go (Golang) — high performance, low latency
// Framework: Echo or Gin
// Key functions:
func SendOTP(phone string) error       // Via Msg91/Twilio
func VerifyOTP(phone, otp string) bool // Redis TTL-based
func GenerateJWT(userID string) string // Access + refresh tokens
func VerifyBiometric(token string) bool // Biometric challenge response
```

#### OTP flow:
```
User enters phone → Backend sends OTP → User enters OTP → 
Backend verifies → Issue JWT access token (15min TTL) + 
refresh token (30 days TTL) → Store in secure device keystore
```

### Step 5.2 — KYC Service
Integration chain:
1. **Aadhaar e-KYC:** Via UIDAI-certified KUA (authorized user agency)
   - Options: SignDesk, IDfy, Hyperverge
   - Aadhaar OTP → XML download → Parse name, DOB, address
2. **PAN verification:** NSDL/UTI API or fintech aggregators (Razorpay, Cashfree)
3. **Bank account verification:** Penny drop (₹1 sent, account holder name verified)
4. **IPV (In-Person Verification):** Live selfie video capture + liveliness check
5. **CKYC upload:** Submit KYC data to CKYC registry

#### Document storage:
- Upload to **S3 bucket** with AES-256 encryption at rest
- Pre-signed URLs (24-hour expiry) for downloads
- Strict IAM policies (no public access)

### Step 5.3 — Market Data Feed Service
This is the most performance-critical service.

```
Exchange (NSE) 
    │ FIX/NEAT binary protocol
    ▼
Feed Handler (C++/Go, co-located near exchange)
    │ Normalize to internal Protobuf format
    ▼
Kafka Topic: "market-ticks"
    │ 
    ├──► OHLC Aggregator (builds candles, stores in TimescaleDB)
    │
    └──► WebSocket Broadcast Server (Go)
              │ WebSocket (WSS)
              ▼
         Client Apps (subscribe to specific instruments)
```

#### WebSocket server design:
```go
// Each client connection subscribes to instrument tokens
// Server maintains a map: instrumentToken → []WebSocketConnections
// On new tick from Kafka: fan out to all subscribers
// Target: 100,000 concurrent connections per server node
// Use goroutines + channels for non-blocking fan-out
```

### Step 5.4 — Order Management System (OMS)

```
Client places order
    ↓
API Gateway validates auth (JWT)
    ↓
OMS receives order request
    ↓
RMS validates: margin sufficient? exposure OK? SEBI limits? 
    ↓ (if approved)
Exchange adapter sends order via CTCL/FIX
    ↓
Exchange sends acknowledgement
    ↓
OMS stores order in PostgreSQL + publishes to Kafka
    ↓
WebSocket pushes order update to client
```

Key OMS fields: symbol, exchange, transaction_type (BUY/SELL), order_type (MARKET/LIMIT/SL/SL-M), product (CNC/MIS/NRML), quantity, price, trigger_price, validity, order_id, status

### Step 5.5 — Risk Management System (RMS)
```python
# Checks performed before order hits exchange:
def validate_order(order, user):
    margin_available = get_margin(user.id)
    margin_required = calculate_margin(order)
    
    if margin_available < margin_required:
        raise InsufficientMarginError()
    
    if order.quantity > exchange_freeze_limit[order.symbol]:
        # Auto-split into multiple orders
        return split_order(order)
    
    if user.exposure > user.allowed_exposure:
        raise ExposureLimitBreachedError()
    
    return order
```

### Step 5.6 — Portfolio Service
- Fetches **CDSL holdings** via CDSL e-DIS API
- Calculates **realized P&L** from trade history
- Calculates **unrealized P&L** using live LTP from market data
- Manages **fund balance** (ledger entries)

### Step 5.7 — Notification Service
```javascript
// Firebase Cloud Messaging (FCM)
const sendOrderNotification = async (userId, orderStatus) => {
  const fcmToken = await getFCMToken(userId);
  await admin.messaging().send({
    token: fcmToken,
    notification: {
      title: `Order ${orderStatus.type}`,
      body: `${orderStatus.symbol} ${orderStatus.status} @ ₹${orderStatus.price}`
    },
    data: { orderId: orderStatus.id, screen: 'orders' }
  });
};
```

---

## PHASE 6: Android App Development (Months 4–10)

### Project Structure (Clean Architecture + MVVM)
```
app/
├── src/main/
│   ├── java/com/yourbroker/app/
│   │   ├── core/           # Base classes, DI, extensions
│   │   ├── data/           # Repositories, data sources, models
│   │   │   ├── remote/     # API services (Retrofit), WebSocket
│   │   │   ├── local/      # Room DB, DataStore
│   │   │   └── repository/ # Single source of truth
│   │   ├── domain/         # Use cases, business logic
│   │   │   ├── usecase/    # PlaceOrderUseCase, GetPortfolioUseCase
│   │   │   └── model/      # Domain models
│   │   ├── presentation/   # ViewModels + UI
│   │   │   ├── auth/       # Login, KYC screens
│   │   │   ├── home/       # Dashboard, watchlist
│   │   │   ├── chart/      # Chart screen + engine
│   │   │   ├── scalper/    # Scalper terminal
│   │   │   ├── options/    # Option chain, strategy builder
│   │   │   ├── portfolio/  # Holdings, P&L
│   │   │   ├── orders/     # Order book, history
│   │   │   └── settings/   # Profile, preferences
│   │   └── di/             # Hilt dependency injection modules
│   └── res/
│       ├── layout/         # XML layouts
│       ├── drawable/       # Icons, drawables
│       └── values/         # Colors, strings, themes (dark)
build.gradle (app level)
build.gradle (project level)
```

### Key Dependencies (build.gradle)
```kotlin
dependencies {
    // Architecture
    implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:2.8.x")
    implementation("androidx.lifecycle:lifecycle-livedata-ktx:2.8.x")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.8.x")
    implementation("androidx.navigation:navigation-fragment-ktx:2.8.x")
    implementation("androidx.navigation:navigation-ui-ktx:2.8.x")
    
    // DI
    implementation("com.google.dagger:hilt-android:2.5x")
    kapt("com.google.dagger:hilt-compiler:2.5x")
    
    // Network
    implementation("com.squareup.retrofit2:retrofit:2.11.x")
    implementation("com.squareup.okhttp3:okhttp:4.12.x")
    implementation("com.squareup.okhttp3:logging-interceptor:4.12.x")
    
    // Local storage
    implementation("androidx.datastore:datastore-preferences:1.1.x")
    implementation("androidx.room:room-runtime:2.6.x")
    kapt("androidx.room:room-compiler:2.6.x")
    
    // UI
    implementation("com.google.android.material:material:1.12.x")
    implementation("androidx.constraintlayout:constraintlayout:2.1.x")
    implementation("androidx.recyclerview:recyclerview:1.3.x")
    
    // Camera (KYC)
    implementation("androidx.camera:camera-camera2:1.3.x")
    implementation("androidx.camera:camera-lifecycle:1.3.x")
    implementation("androidx.camera:camera-view:1.3.x")
    
    // Biometric auth
    implementation("androidx.biometric:biometric:1.2.x")
    
    // Images
    implementation("io.coil-kt:coil:2.7.x")
    
    // Monitoring
    implementation("io.sentry:sentry-android:7.x.x")
    
    // Firebase
    implementation("com.google.firebase:firebase-messaging-ktx:24.x.x")
    implementation("com.google.firebase:firebase-analytics-ktx:22.x.x")
}
```

### Step 6.1 — Authentication UI
```kotlin
// OTP Login Screen ViewModel
class LoginViewModel @Inject constructor(
    private val sendOtpUseCase: SendOtpUseCase,
    private val verifyOtpUseCase: VerifyOtpUseCase
) : ViewModel() {
    
    private val _uiState = MutableStateFlow<LoginUiState>(LoginUiState.Idle)
    val uiState: StateFlow<LoginUiState> = _uiState.asStateFlow()
    
    fun sendOtp(phoneNumber: String) = viewModelScope.launch {
        _uiState.value = LoginUiState.Loading
        sendOtpUseCase(phoneNumber)
            .onSuccess { _uiState.value = LoginUiState.OtpSent }
            .onFailure { _uiState.value = LoginUiState.Error(it.message) }
    }
}
```

### Step 6.2 — Custom Chart Engine
This is the hardest and most differentiating component:

```kotlin
class TradingChartView @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null
) : View(context, attrs) {
    
    private val candlePaint = Paint(Paint.ANTI_ALIAS_FLAG)
    private val gridPaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
        color = Color.parseColor("#333333")
        strokeWidth = 0.5f
    }
    
    // Price data
    private var candles: List<Candle> = emptyList()
    
    // Viewport (what range is visible)
    private var viewportStart = 0
    private var viewportEnd = 0
    
    // Scale (pixels per candle)
    private var candleWidth = 8f
    private var candleSpacing = 2f
    
    override fun onDraw(canvas: Canvas) {
        drawGrid(canvas)
        drawCandles(canvas)
        drawPriceAxis(canvas)
        drawTimeAxis(canvas)
        drawIndicators(canvas)
        drawCrosshair(canvas)
    }
    
    private fun drawCandles(canvas: Canvas) {
        candles.forEachIndexed { index, candle ->
            val x = indexToX(index)
            val topY = priceToY(maxOf(candle.open, candle.close))
            val bottomY = priceToY(minOf(candle.open, candle.close))
            val highY = priceToY(candle.high)
            val lowY = priceToY(candle.low)
            
            val isBullish = candle.close >= candle.open
            candlePaint.color = if (isBullish) Color.parseColor("#26A69A") 
                               else Color.parseColor("#EF5350")
            
            // Draw candle body
            canvas.drawRect(x - candleWidth/2, topY, x + candleWidth/2, bottomY, candlePaint)
            
            // Draw wick
            canvas.drawLine(x, highY, x, topY, candlePaint)
            canvas.drawLine(x, bottomY, x, lowY, candlePaint)
        }
    }
    
    // Live update: called when new tick arrives via WebSocket
    fun updateLastCandle(ltp: Float, volume: Long) {
        // Update the last candle without full redraw
        // Only invalidate the region containing the last candle
        invalidate()
    }
}
```

### Step 6.3 — WebSocket Client (Market Data)
```kotlin
class MarketDataWebSocket @Inject constructor(
    private val okHttpClient: OkHttpClient
) {
    private var webSocket: WebSocket? = null
    private val _tickFlow = MutableSharedFlow<MarketTick>()
    val tickFlow: SharedFlow<MarketTick> = _tickFlow.asSharedFlow()
    
    fun connect(authToken: String) {
        val request = Request.Builder()
            .url("wss://api.yourbroker.com/ws/v1/market")
            .addHeader("Authorization", "Bearer $authToken")
            .build()
        
        webSocket = okHttpClient.newWebSocket(request, object : WebSocketListener() {
            override fun onMessage(webSocket: WebSocket, bytes: ByteString) {
                // Parse binary market data packet
                val tick = parseTick(bytes)
                _tickFlow.tryEmit(tick)
            }
            
            override fun onClosed(webSocket: WebSocket, code: Int, reason: String) {
                // Auto-reconnect with exponential backoff
                reconnect()
            }
        })
    }
    
    fun subscribe(tokens: List<Int>) {
        val msg = buildJson { 
            put("action", "subscribe")
            put("tokens", tokens)
        }
        webSocket?.send(msg)
    }
}
```

### Step 6.4 — Order Placement
```kotlin
// Buy/Sell Bottom Sheet
class OrderPlacementFragment : BottomSheetDialogFragment() {
    
    private val viewModel: OrderViewModel by viewModels()
    
    private fun placeOrder() {
        val order = OrderRequest(
            symbol = args.symbol,
            exchange = args.exchange,
            transactionType = if (binding.buyBtn.isChecked) "BUY" else "SELL",
            orderType = when (binding.orderTypeChip.checkedChipId) {
                R.id.marketChip -> "MARKET"
                R.id.limitChip -> "LIMIT"
                else -> "SL"
            },
            product = when (binding.productChip.checkedChipId) {
                R.id.misChip -> "MIS"  // Intraday
                R.id.cncChip -> "CNC"  // Delivery
                else -> "NRML"         // F&O
            },
            quantity = binding.quantityInput.text.toString().toInt(),
            price = binding.priceInput.text.toString().toDoubleOrNull()
        )
        viewModel.placeOrder(order)
    }
}
```

---

## PHASE 7: Testing & QA (Months 9–11)

### Testing Pyramid
```
           ▲ E2E Tests (Espresso)
          ███ — Slow, test full user flows
         █████ 
        ███████ Integration Tests
       █████████ — Test service layers together
      ███████████
     ████████████████ Unit Tests
    ████████████████████ — Fast, test individual functions
```

### Critical Test Scenarios
1. **Order placement under network failure** — must not double-submit
2. **WebSocket reconnection** — data must resume correctly after disconnect
3. **Chart rendering performance** — must maintain 60fps with 500 candles
4. **Concurrent users** — load test WebSocket server at 10K, 50K, 100K connections
5. **KYC OCR accuracy** — document parsing correctness
6. **Biometric fallback** — device PIN fallback when biometric fails
7. **Payment reconciliation** — UPI credit must reflect in app balance
8. **Margin calculation accuracy** — must match exchange's calculation exactly

### Security Testing (VAPT Scope)
- SQL injection on all API endpoints
- Authentication bypass attempts
- JWT token manipulation
- WebSocket message injection
- Certificate pinning bypass attempts
- App reverse engineering resistance
- Data leakage in logs

---

## PHASE 8: Play Store & App Store Submission

### Play Store Requirements for Financial Apps
- **Proof of license:** SEBI registration certificate
- **Data safety form:** Declare all data collected and shared
- **Privacy policy:** Detailed, SEBI-compliant
- **Terms of service:** SEBI and exchange regulatory disclosures
- **Target API:** Must target Android 14+ (API 34+)
- **64-bit support:** Mandatory
- **App bundle:** Use AAB format (not APK) for Play Store
- **Review time:** 1–3 business days for new financial apps

### App Store (iOS) Requirements
- **App Review Guidelines Section 3.1:** Financial services category
- **KYC flow:** Must explain data usage clearly
- **Entitlements:** Push notifications, camera, biometric
- **TestFlight:** Use for beta distribution before public release
- **Review time:** 3–7 business days (can be longer for financial apps)

---

## PHASE 9: Launch Strategy

### Soft Launch (Month 11–12)
- Invite 100–500 beta users (existing traders from waitlist)
- Monitor crash rates (target: <0.1% crash-free sessions)
- Monitor order success rates (target: >99.9%)
- Gather NPS score (target: >50)

### Public Launch (Month 12+)
- Press release on financial media (Economic Times, Mint, Money Control)
- YouTube demo videos
- Referral program: "Invite a friend, both get free brokerage"
- Twitter/X trading community engagement
- Trading educator partnerships (YouTube channels with 100K+ subscribers)

---

## PHASE 10: Post-Launch Operations

### Daily Operations
- Market hours monitoring (9:00 AM – 3:45 PM IST)
- On-call engineer during market hours (mandatory)
- Daily reconciliation: broker ledger vs exchange ledger
- SEBI daily trade reporting

### Regulatory Compliance Calendar
| Frequency | Task |
|-----------|------|
| Daily | Trade reporting to NSE/BSE, client fund reconciliation |
| Weekly | Risk report review |
| Monthly | SEBI compliance filing, client ledger statements |
| Quarterly | VAPT security audit, SEBI inspection preparation |
| Annual | Audited financial statements, SEBI renewal |

### Scaling Plan (Users → Infrastructure)
| Users | Infrastructure Scale |
|-------|---------------------|
| 0–10K | 2 API servers, 1 DB (RDS), basic Redis |
| 10K–50K | Kubernetes autoscaling, Redis cluster, read replicas |
| 50K–200K | Multi-AZ everything, dedicated WebSocket nodes, CDN |
| 200K+ | Multi-region, dedicated market data infrastructure |

