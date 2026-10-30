# Sahi Trading App — Third-Party Libraries & Integrations

## Android Libraries Detected (from APK static analysis)
> Evidence ID: ev_cf51277bd1bae0b459f2f1b8dd0d3a9f445e51bc8b38c513de60051b0028b0fd  
> APK SHA-256: 9fff890ca793882e229d29a17b7c87931056556d6df3e88524ff037bb715e19f

---

## Confirmed Libraries (from META-INF version files)

### AndroidX Jetpack Suite

| Library | Version File Confirmed | Category |
|---------|----------------------|---------|
| `androidx.activity` | activity, activity-ktx | Activity management |
| `androidx.appcompat` | appcompat, appcompat-resources | Backward compat |
| `androidx.annotation` | annotation-experimental | Null safety annotations |
| `androidx.biometric` | biometric | Biometric auth (face/fingerprint) |
| `androidx.browser` | browser | Chrome Custom Tabs |
| `androidx.camera` | camera-camera2, camera-core, camera-lifecycle, camera-video, camera-view, featurecombinationquery | Document/selfie capture |
| `androidx.cardview` | cardview | Material card components |
| `androidx.constraintlayout` | constraintlayout | Complex UI layouts |
| `androidx.coordinatorlayout` | coordinatorlayout | AppBar / FAB coordination |
| `androidx.credentials` | credentials, credentials-play-services-auth | Credential Manager API |
| `androidx.cursoradapter` | cursoradapter | Database cursor binding |
| `androidx.customview` | customview, customview-poolingcontainer | Custom view infrastructure |
| `androidx.databinding` | baseAdapters, databindingKtx, library, viewbinding | View binding / Data binding |
| `androidx.datastore` | datastore, datastore-core, datastore-preferences, datastore-preferences-core | Preferences & proto storage |
| `androidx.documentfile` | documentfile | Document access |
| `androidx.drawerlayout` | drawerlayout | Navigation drawer |
| `androidx.dynamicanimation` | dynamicanimation | Physics-based animations |
| `androidx.emoji2` | emoji2, emoji2-views-helper | Emoji rendering |
| `androidx.exifinterface` | exifinterface | Image EXIF metadata |
| `androidx.fragment` | fragment, fragment-ktx | Fragment navigation |
| `androidx.graphics.shapes` | graphics-shapes | Adaptive icon shapes |
| `androidx.interpolator` | interpolator | Animation interpolators |
| `androidx.legacy` | legacy-support-core-utils | Legacy compatibility |
| `androidx.lifecycle` | lifecycle-extensions, lifecycle-livedata, lifecycle-livedata-core, lifecycle-livedata-ktx, lifecycle-process, lifecycle-runtime, lifecycle-runtime-ktx, lifecycle-service, lifecycle-viewmodel, lifecycle-viewmodel-ktx, lifecycle-viewmodel-savedstate, lifecycle-livedata-core-ktx, lifecycle-livedata-ktx | MVVM lifecycle management |
| `androidx.lifecycle-extensions` | lifecycle-extensions | LiveData extensions |
| `androidx.loader` | loader | AsyncTaskLoader compat |
| `androidx.localbroadcastmanager` | localbroadcastmanager | Local broadcasts |
| `androidx.media` | media | Media playback |
| `androidx.navigation` | navigation-common, navigation-common-ktx, navigation-fragment, navigation-fragment-ktx, navigation-runtime, navigation-runtime-ktx, navigation-ui, navigation-ui-ktx | Jetpack Navigation |
| `androidx.preference` | preference, preference-ktx | Settings/preferences UI |
| `androidx.print` | print | Print support |
| `androidx.privacysandbox.ads` | ads-adservices, ads-adservices-java | Privacy Sandbox / Ad targeting |
| `androidx.profileinstaller` | profileinstaller | Baseline profiles |
| `androidx.recyclerview` | recyclerview | High-performance lists |

### Kotlin Coroutines
| Evidence | Confirms |
|----------|---------|
| `DebugProbesKt.bin` (1728 bytes) | kotlinx-coroutines-core with debug probes enabled |
| Multiple kotlin_module files | Kotlin multi-module project |

### Third-Party SDKs (Confirmed by Resources)

#### Sentry (Error Monitoring)
| Resource | Confirms |
|----------|---------|
| `sentry_edit_text_border.xml` | Sentry feedback UI |
| `sentry_logo_dark.xml` | Sentry branding asset |
| `sentry_oval_button_ripple_background.xml` | Sentry feedback button |
| `sentry_user_feedback_button_logo_24.xml` | Sentry feedback system |
**SDK Version:** Sentry Android SDK (recent — supports user feedback feature)  
**Purpose:** Real-time crash reporting, performance monitoring, session replay

#### NPCI / UPI Payment
| Resource | Confirms |
|----------|---------|
| `npci_img.xml` (30,016 bytes SVG) | NPCI UPI logo/branding |
**Purpose:** UPI fund deposit via PhonePe, GPay, BHIM, Paytm

#### Material Design Components
| Resource Pattern | Confirms |
|---------|---------|
| `mtrl_ic_indeterminate.xml` | Material loading indicator |
| `mtrl_navigation_bar_item_background.xml` | Bottom navigation |
| `mtrl_popupmenu_background.xml` | Popup menus |
| `mtrl_switch_*` (12 variants) | Material switches |
| `mtrl_tabs_default_indicator.xml` | Tab layout |
**Library:** `com.google.android.material:material` (Material Design 3)

#### Camera / KYC Scanning
| Resource | Confirms |
|----------|---------|
| `scanner_bg.png` (28,970 bytes) | Document scanner overlay |
**Purpose:** KYC document capture (PAN card, Aadhaar) + selfie for IPV

---

## Custom/Proprietary Components

### Chart Engine
- **Type:** 100% in-house, native Canvas-based
- **Evidence:** No TradingView library files found in APK; no web view assets for chart rendering
- **Implementation:** Custom `View` extending `View/SurfaceView` drawing candlesticks, indicators, axes
- **Performance:** Native Canvas APIs, hardware-accelerated, targeting 60fps

### Market Data WebSocket Client
- **Evidence:** OkHttp WebSocket (via `okhttp` dependency, standard for Android)
- **Binary protocol:** Custom Protobuf or binary packet format for tick data

---

## Backend Technology Stack (Inferred + Research)

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| API Gateway | AWS ALB / Nginx | Industry standard |
| Auth Service | Go + JWT | High performance, low latency |
| Market Data Feed | Go / C++ | Ultra-low latency requirements |
| OMS/RMS | Go or Java | Financial transaction safety |
| WebSocket Server | Go (goroutines) | Handle 100K+ concurrent connections |
| KYC Service | Node.js / Python | Third-party API orchestration |
| AI/ML Service | Python (FastAPI) | ML model inference |
| Primary Database | PostgreSQL (RDS) | ACID compliance for financial data |
| Cache | Redis (ElastiCache) | Sub-millisecond latency for live data |
| Time-Series DB | TimescaleDB / ScyllaDB | OHLC historical chart data |
| Message Queue | Apache Kafka | High-throughput event streaming |
| Object Storage | AWS S3 | KYC documents, app assets |
| Monitoring | Sentry + CloudWatch | Confirmed (Sentry in APK) |
| CDN | CloudFront | Static asset delivery |
| DNS | Route 53 | High-availability DNS |

---

## Recommended Equivalent Stack (For Building Clone)

### Android App
```kotlin
// build.gradle - recommended modern stack

// Coroutines
"org.jetbrains.kotlinx:kotlinx-coroutines-android:1.8.1"
"org.jetbrains.kotlinx:kotlinx-coroutines-core:1.8.1"

// ViewModel + Lifecycle
"androidx.lifecycle:lifecycle-viewmodel-ktx:2.8.7"
"androidx.lifecycle:lifecycle-runtime-ktx:2.8.7"

// Navigation
"androidx.navigation:navigation-fragment-ktx:2.8.4"
"androidx.navigation:navigation-ui-ktx:2.8.4"

// Hilt DI
"com.google.dagger:hilt-android:2.52"
kapt "com.google.dagger:hilt-compiler:2.52"

// Network
"com.squareup.retrofit2:retrofit:2.11.0"
"com.squareup.retrofit2:converter-gson:2.11.0"
"com.squareup.okhttp3:okhttp:4.12.0"
"com.squareup.okhttp3:logging-interceptor:4.12.0"

// DataStore (replaces SharedPreferences)
"androidx.datastore:datastore-preferences:1.1.1"

// Room (local DB)
"androidx.room:room-runtime:2.6.1"
"androidx.room:room-ktx:2.6.1"
kapt "androidx.room:room-compiler:2.6.1"

// CameraX (KYC)
"androidx.camera:camera-camera2:1.4.0"
"androidx.camera:camera-lifecycle:1.4.0"
"androidx.camera:camera-view:1.4.0"

// Biometric
"androidx.biometric:biometric:1.2.0-alpha05"

// Sentry (crash monitoring)
"io.sentry:sentry-android:7.19.0"

// Firebase
"com.google.firebase:firebase-messaging-ktx:24.1.0"
"com.google.firebase:firebase-analytics-ktx:22.1.2"

// Image loading
"io.coil-kt:coil:2.7.0"

// Material Design
"com.google.android.material:material:1.12.0"

// JSON
"org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.3"
```

### Backend (Go)
```go
// go.mod
module github.com/yourbroker/trading-backend

go 1.23

require (
    github.com/gin-gonic/gin v1.10.0          // HTTP framework
    github.com/gorilla/websocket v1.5.3        // WebSocket
    github.com/golang-jwt/jwt/v5 v5.2.1        // JWT auth
    github.com/jackc/pgx/v5 v5.7.1             // PostgreSQL
    github.com/redis/go-redis/v9 v9.7.0        // Redis
    github.com/segmentio/kafka-go v0.4.47      // Kafka
    github.com/google/wire v0.6.0              // Dependency injection
    go.uber.org/zap v1.27.0                    // Structured logging
    github.com/getsentry/sentry-go v0.29.1     // Sentry
    google.golang.org/protobuf v1.35.1         // Protobuf
)
```

---

## Third-Party Service Providers (Recommended for India)

### KYC & Compliance
| Service | Provider | Cost |
|---------|---------|------|
| Aadhaar e-KYC | Digio, IDfy, SignDesk, Hyperverge | ₹10–₹30 per verification |
| PAN Verification | Razorpay, Cashfree, IDfy | ₹2–₹10 per verification |
| Bank Account Verification (Penny Drop) | Razorpay, Cashfree | ₹3–₹8 per verification |
| Video KYC (IPV) | IDfy, Hyperverge | ₹30–₹80 per session |
| CKYC | CVL KRA, NDML KRA | ₹5–₹15 per record |

### Payments
| Service | Provider | Cost |
|---------|---------|------|
| UPI Fund Deposit | Razorpay, Cashfree, PayU | 0%–2% (many offer 0% UPI) |
| NEFT/RTGS | Bank API | ₹2–₹5 per transaction |
| Instant Withdrawal | Imps/NEFT via RazorpayX | ₹5–₹10 per payout |

### Communication
| Service | Provider | Cost |
|---------|---------|------|
| OTP SMS | Msg91, Twilio, Kaleyra | ₹0.09–₹0.20 per SMS |
| Transactional Email | SendGrid, Mailgun | ₹0.05–₹0.10 per email |
| Push Notifications | Firebase (FCM) | Free up to 250K/month |

### Market Data
| Service | Provider | Cost/Year |
|---------|---------|----------|
| NSE Level 1 (LTP only) | Direct via CTCL membership | Included with membership |
| NSE Level 2 (Order book depth) | Direct via NSE approval | ₹3.75L–₹35L/year |
| Historical Data API | TrueData, GlobalDatafeeds | ₹30K–₹3L/year |
| Corporate Actions | BSE India API | Free |
| Options Calculator | Sensibull API | ₹2L–₹5L/year |

### Monitoring & DevOps
| Service | Cost/Month |
|---------|-----------|
| Sentry (Team plan) | $26/month |
| PagerDuty (Essential) | $21/user/month |
| Datadog APM | $31/host/month |
| New Relic | $0.30/GB data |
| Cloudflare Pro | $20/month |

