import utils.session
import subprocess
import os

HTML_PATH = os.path.abspath(r"c:\Users\skahi\Downloads\sahi\Sahi_Trading_App_Client_Proposal.html")
PDF_PATH = os.path.abspath(r"c:\Users\skahi\Downloads\sahi\Sahi_Trading_App_Client_Proposal.pdf")
PDF_ANALYSIS_PATH = os.path.abspath(r"c:\Users\skahi\Downloads\sahi\analysis\Sahi_Trading_App_Client_Proposal.pdf")

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Sahi-Style High-Performance Trading Platform — Master Client Proposal</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

  @page {
    size: A4;
    margin: 18mm 15mm 20mm 15mm;
    @bottom-right {
      content: counter(page);
      font-family: 'Inter', sans-serif;
      font-size: 8.5pt;
      color: #64748b;
    }
    @bottom-left {
      content: "CONFIDENTIAL & PROPRIETARY — Sahi-Style Trading App Project Proposal";
      font-family: 'Inter', sans-serif;
      font-size: 7.5pt;
      color: #94a3b8;
    }
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #1e293b;
    background: #ffffff;
    font-size: 9.5pt;
    line-height: 1.55;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  /* Cover Page */
  .cover-page {
    page-break-after: always;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 40px 25px;
    background: linear-gradient(135deg, #090d16 0%, #0f172a 50%, #1e1b4b 100%);
    color: #ffffff;
    border-radius: 8px;
    position: relative;
    overflow: hidden;
  }

  .cover-page::before {
    content: "";
    position: absolute;
    top: -100px;
    right: -100px;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(99, 102, 241, 0.25) 0%, rgba(99, 102, 241, 0) 70%);
    border-radius: 50%;
  }

  .cover-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.15);
    padding-bottom: 20px;
  }

  .cover-badge {
    display: inline-block;
    padding: 6px 14px;
    background: rgba(99, 102, 241, 0.25);
    border: 1px solid rgba(129, 140, 248, 0.4);
    border-radius: 20px;
    font-size: 8pt;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #a5b4fc;
  }

  .cover-body {
    margin-top: 40px;
  }

  .cover-title {
    font-size: 28pt;
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -0.5px;
    color: #ffffff;
    margin-bottom: 15px;
  }

  .cover-title span {
    background: linear-gradient(90deg, #38bdf8 0%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .cover-subtitle {
    font-size: 13pt;
    font-weight: 400;
    color: #94a3b8;
    line-height: 1.45;
    max-width: 650px;
    margin-bottom: 30px;
  }

  .cover-highlights {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
    margin-top: 35px;
  }

  .highlight-card {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 16px;
    backdrop-filter: blur(10px);
  }

  .highlight-card .h-num {
    font-size: 18pt;
    font-weight: 800;
    color: #38bdf8;
    margin-bottom: 4px;
  }

  .highlight-card .h-label {
    font-size: 8pt;
    color: #cbd5e1;
    font-weight: 500;
    line-height: 1.3;
  }

  .cover-footer {
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    padding-top: 20px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    font-size: 8.5pt;
    color: #94a3b8;
  }

  .cover-meta strong {
    color: #f8fafc;
  }

  /* Page Break & Structural Classes */
  .page-break {
    page-break-after: always;
  }

  .avoid-break {
    page-break-inside: avoid;
  }

  /* Headings */
  h1.section-title {
    font-size: 18pt;
    font-weight: 800;
    color: #0f172a;
    border-bottom: 2.5px solid #4f46e5;
    padding-bottom: 8px;
    margin-top: 28px;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  h1.section-title .sec-num {
    background: #4f46e5;
    color: #ffffff;
    font-size: 11pt;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 6px;
  }

  h2 {
    font-size: 13pt;
    font-weight: 700;
    color: #1e293b;
    margin-top: 18px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  h2::before {
    content: "";
    width: 4px;
    height: 16px;
    background: #6366f1;
    border-radius: 2px;
    display: inline-block;
  }

  h3 {
    font-size: 10.5pt;
    font-weight: 600;
    color: #334155;
    margin-top: 14px;
    margin-bottom: 6px;
  }

  p {
    margin-bottom: 10px;
    color: #334155;
    text-align: justify;
  }

  /* Callout & Alert Boxes */
  .callout-box {
    background: #f8fafc;
    border-left: 4px solid #4f46e5;
    padding: 12px 16px;
    border-radius: 0 8px 8px 0;
    margin: 14px 0;
    font-size: 9pt;
  }

  .callout-box.strategic {
    background: #f0fdf4;
    border-left-color: #16a34a;
  }

  .callout-box.warning {
    background: #fffbeb;
    border-left-color: #d97706;
  }

  .callout-box.critical {
    background: #fef2f2;
    border-left-color: #dc2626;
  }

  .callout-title {
    font-weight: 700;
    font-size: 9.5pt;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .callout-box.strategic .callout-title { color: #15803d; }
  .callout-box.warning .callout-title { color: #b45309; }
  .callout-box.critical .callout-title { color: #b91c1c; }

  /* Tables */
  table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0 20px 0;
    font-size: 8.5pt;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    overflow: hidden;
  }

  table.data-table th {
    background: #0f172a;
    color: #ffffff;
    font-weight: 600;
    padding: 9px 11px;
    text-align: left;
    font-size: 8.5pt;
    letter-spacing: 0.3px;
  }

  table.data-table td {
    padding: 8px 11px;
    border-bottom: 1px solid #e2e8f0;
    color: #334155;
    vertical-align: top;
  }

  table.data-table tr:nth-child(even) td {
    background: #f8fafc;
  }

  table.data-table tr:hover td {
    background: #f1f5f9;
  }

  table.data-table .cost-col {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    color: #0f172a;
    text-align: right;
    white-space: nowrap;
  }

  table.data-table th.cost-col {
    text-align: right;
  }

  table.data-table tr.total-row td {
    background: #eef2ff !important;
    font-weight: 700;
    color: #1e1b4b;
    border-top: 2px solid #6366f1;
    font-size: 9pt;
  }

  /* Badge / Pill */
  .pill {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 12px;
    font-size: 7.5pt;
    font-weight: 600;
    text-transform: uppercase;
  }

  .pill.mand { background: #fee2e2; color: #991b1b; }
  .pill.opt { background: #e0f2fe; color: #075985; }
  .pill.gov { background: #fef3c7; color: #92400e; }
  .pill.tech { background: #ede9fe; color: #5b21b6; }
  .pill.ai { background: #dcfce7; color: #166534; }

  /* Two Column Layout */
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 12px 0;
  }

  .card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 14px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  }

  .card-header {
    font-weight: 700;
    font-size: 10pt;
    color: #0f172a;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 6px;
    margin-bottom: 8px;
  }

  /* Key Feature list */
  ul.feature-list {
    list-style: none;
    margin: 8px 0;
  }

  ul.feature-list li {
    position: relative;
    padding-left: 18px;
    margin-bottom: 6px;
    font-size: 9pt;
    color: #334155;
  }

  ul.feature-list li::before {
    content: "✔";
    position: absolute;
    left: 0;
    color: #10b981;
    font-weight: bold;
    font-size: 8.5pt;
  }

  /* Flow Steps */
  .flow-step {
    display: flex;
    gap: 12px;
    margin-bottom: 10px;
    align-items: flex-start;
  }

  .step-circle {
    background: #4f46e5;
    color: #ffffff;
    font-weight: 700;
    font-size: 8pt;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-top: 2px;
  }

  .step-content {
    flex-grow: 1;
    font-size: 9pt;
  }

  .step-content strong {
    color: #0f172a;
  }

  /* Executive Signature Block */
  .signature-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
    margin-top: 40px;
    padding-top: 25px;
    border-top: 1px dashed #cbd5e1;
  }

  .sign-line {
    border-top: 1px solid #94a3b8;
    margin-top: 45px;
    padding-top: 6px;
    font-size: 8.5pt;
    color: #475569;
  }
</style>
</head>
<body>

<!-- ================= COVER PAGE ================= -->
<div class="cover-page">
  <div class="cover-header">
    <div class="cover-badge">ENTERPRISE CLIENT PROPOSAL</div>
    <div style="font-size: 9pt; color: #cbd5e1;">Project Reference: FINTECH-SAHI-2026</div>
  </div>

  <div class="cover-body">
    <div style="color: #38bdf8; font-weight: 700; font-size: 11pt; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 8px;">
      Master Engineering & Compliance Blueprint
    </div>
    <h1 class="cover-title">
      Sahi-Style High-Performance<br>
      <span>Next-Gen Stock & Options</span><br>
      Trading Platform
    </h1>
    <div class="cover-subtitle">
      A comprehensive technical specification, regulatory road-map, third-party vendor ecosystem, and transparent investment breakdown for building an institutional-grade retail trading application.
    </div>

    <div class="cover-highlights">
      <div class="highlight-card">
        <div class="h-num">60 FPS</div>
        <div class="h-label">In-House Canvas Engine<br>Sub-16ms Tick Rendering</div>
      </div>
      <div class="highlight-card">
        <div class="h-num">14-Step</div>
        <div class="h-label">Paperless Digital KYC<br>Digio + HyperVerge AI</div>
      </div>
      <div class="highlight-card">
        <div class="h-num">Kyro AI</div>
        <div class="h-label">Natural Language Indicators<br>Single-Screen Scalper 2.0</div>
      </div>
    </div>
  </div>

  <div class="cover-footer">
    <div class="cover-meta">
      <div>Prepared For: <strong>Executive Board & Project Sponsors</strong></div>
      <div>Entity Scope: <strong>SEBI Registered Stock Broker / Fintech Partner</strong></div>
      <div>Target Segments: <strong>NSE & BSE Equity, F&O, MCX Commodities</strong></div>
    </div>
    <div style="text-align: right;">
      <div>Document Version: <strong>2.0 (Verified via JADX v0.8.0 Decompile)</strong></div>
      <div>Date: <strong>November 2026</strong></div>
      <div>Classification: <strong>Strictly Confidential</strong></div>
    </div>
  </div>
</div>

<!-- ================= TABLE OF CONTENTS & EXECUTIVE BRIEF ================= -->
<div class="page-break">
  <h1 class="section-title"><span class="sec-num">00</span> Executive Brief & Table of Contents</h1>

  <div class="callout-box strategic">
    <div class="callout-title">🎯 Executive Project Vision</div>
    The objective of this initiative is to engineer a flagship Indian retail trading platform identical in speed, ergonomics, and capabilities to <strong>Sahi (Aaritya Broking Pvt Ltd)</strong>. Modern Indian options traders and scalpers demand ultra-low latency, single-screen execution (Scalper 2.0), automated risk guards (PnL Protect), and natural-language indicator generation (Kyro AI). This document provides the complete end-to-end blueprint, covering every legal approval, document checklist, technical specification, and itemized financial budget required to launch successfully.
  </div>

  <h2>Table of Contents</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 10%;">Section</th>
        <th style="width: 45%;">Module Description</th>
        <th style="width: 30%;">Key Takeaways</th>
        <th style="width: 15%;">Page / Target</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>01</strong></td>
        <td><strong>Pre-requisites, Licenses & Government Approvals</strong></td>
        <td>SEBI, NSE, BSE, MCX, CDSL, Net Worth ₹1 Cr+, VAPT</td>
        <td>Section 1</td>
      </tr>
      <tr>
        <td><strong>02</strong></td>
        <td><strong>Legal Documentation & Regulatory Readiness</strong></td>
        <td>Checklist of documents required prior to launch</td>
        <td>Section 2</td>
      </tr>
      <tr>
        <td><strong>03</strong></td>
        <td><strong>End-to-End User KYC & Onboarding Journey</strong></td>
        <td>14-step flow decoded from Sahi: Digio, HyperVerge, DDPI</td>
        <td>Section 3</td>
      </tr>
      <tr>
        <td><strong>04</strong></td>
        <td><strong>Technical Architecture & Core Feature Stack</strong></td>
        <td>Flutter 12 packages, Canvas 60fps, Go OMS/RMS, Kafka</td>
        <td>Section 4</td>
      </tr>
      <tr>
        <td><strong>05</strong></td>
        <td><strong>Kyro AI & Machine Learning Integration</strong></td>
        <td>18 system indicators, LLM-based SahiScript generation</td>
        <td>Section 5</td>
      </tr>
      <tr>
        <td><strong>06</strong></td>
        <td><strong>Comprehensive Itemized Costing & Budget</strong></td>
        <td>Development, Third-Party APIs, Cloud, Exchange, Compliance</td>
        <td>Section 6</td>
      </tr>
      <tr>
        <td><strong>07</strong></td>
        <td><strong>Model A vs. Model B Strategic Comparison</strong></td>
        <td>Own Broker License (₹4.5–8.0 Cr) vs. Partner API (₹1.5–3.5 Cr)</td>
        <td>Section 7</td>
      </tr>
      <tr>
        <td><strong>08</strong></td>
        <td><strong>Project Execution Roadmap & Payment Milestones</strong></td>
        <td>Phase-by-phase timeline, deliverables, sign-off</td>
        <td>Section 8</td>
      </tr>
    </tbody>
  </table>

  <h2>Two Business Routes Explained (Quick Executive Overview)</h2>
  <div class="two-col">
    <div class="card">
      <div class="card-header">Model A: Full SEBI Stock Broker (Like Sahi)</div>
      <p style="font-size: 8.5pt;">You incorporate a Private Limited company, apply for a SEBI Trading Member license, acquire direct NSE, BSE, and MCX memberships, register as a CDSL DP, and run an in-house Order Management System (OMS).</p>
      <ul class="feature-list" style="font-size: 8.5pt;">
        <li>100% control over brokerage revenue and float income</li>
        <li>Direct connectivity to stock exchange matching engines</li>
        <li>Requires ₹1 Crore+ net worth certificate & exchange deposits</li>
        <li>Time to Market: <strong>10 – 14 Months</strong> | Year 1: <strong>₹4.5 – ₹8.0 Cr</strong></li>
      </ul>
    </div>
    <div class="card">
      <div class="card-header">Model B: Fintech Partner / Sub-Broker Terminal</div>
      <p style="font-size: 8.5pt;">You build the custom Flutter mobile app, chart engine, Kyro AI, and UI/UX, while routing execution through an established broker's open APIs (Zerodha Kite, Dhan API, or Shoonya).</p>
      <ul class="feature-list" style="font-size: 8.5pt;">
        <li>Zero SEBI licensing wait time; launch in under 5 months</li>
        <li>No capital lock-in for exchange Base Minimum Capital (BMC)</li>
        <li>Shared brokerage revenue model (20%–40% share)</li>
        <li>Time to Market: <strong>4 – 6 Months</strong> | Year 1: <strong>₹1.5 – ₹3.5 Cr</strong></li>
      </ul>
    </div>
  </div>
</div>

<!-- ================= SECTION 1: PRE-REQUISITES & GOVT APPROVALS ================= -->
<div class="page-break">
  <h1 class="section-title"><span class="sec-num">01</span> Pre-requisites, Licenses & Government Approvals</h1>

  <p>To operate a compliant stock trading platform in India, strict regulatory clearances must be obtained from statutory bodies under the <strong>Securities and Exchange Board of India (SEBI)</strong> and respective stock exchanges. Below is the comprehensive matrix of mandatory pre-requisites and government approvals:</p>

  <table class="data-table">
    <thead>
      <tr>
        <th>Regulatory Body</th>
        <th>License / Approval Required</th>
        <th>Category</th>
        <th>Mandatory Requirement & Net Worth</th>
        <th>Estimated Time</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>MCA (Govt of India)</strong></td>
        <td>Private Limited Incorporation</td>
        <td><span class="pill mand">Mandatory</span></td>
        <td>Registered Indian corporate entity with "securities / broking" in MOA object clause. Minimum 2 directors.</td>
        <td>15 – 20 Days</td>
      </tr>
      <tr>
        <td><strong>SEBI</strong></td>
        <td>Stock Broker Registration (Form A)</td>
        <td><span class="pill mand">Mandatory</span></td>
        <td>Base Net Worth of ₹1.00 Crore for Trading Member. Audited balance sheet signed by CA. Clean promoter track record.</td>
        <td>3 – 5 Months</td>
      </tr>
      <tr>
        <td><strong>NSE (National Stock Exchange)</strong></td>
        <td>Trading Membership (CM & F&O)</td>
        <td><span class="pill mand">Mandatory</span></td>
        <td>Admission fee + Base Minimum Capital (BMC) of ₹10L–₹25L maintained as FDR or Bank Guarantee. CTCL mock trading sign-off.</td>
        <td>3 – 4 Months</td>
      </tr>
      <tr>
        <td><strong>BSE (Bombay Stock Exchange)</strong></td>
        <td>Deposit Based Membership (DBM)</td>
        <td><span class="pill opt">Recommended</span></td>
        <td>₹1.0 Lakh Earnest Money Deposit (EMD) + ₹10 Lakh initial deposit. Access to BSE Sensex / Bankex derivative contracts.</td>
        <td>2 – 3 Months</td>
      </tr>
      <tr>
        <td><strong>MCX (Multi Commodity Exchange)</strong></td>
        <td>Commodity Broker Membership</td>
        <td><span class="pill opt">Optional Ph 1</span></td>
        <td>Allows trading in Crude Oil, Gold, Silver, Natural Gas. Minimum capital deposit of ₹5L–₹8L.</td>
        <td>2 – 3 Months</td>
      </tr>
      <tr>
        <td><strong>CDSL / NSDL</strong></td>
        <td>Depository Participant (DP) Registration</td>
        <td><span class="pill mand">Mandatory</span></td>
        <td>Enables opening customer Demat accounts in-app. CDSL DP ID issuance (Sahi uses CDSL: IN-DP-780-2024).</td>
        <td>2 – 3 Months</td>
      </tr>
      <tr>
        <td><strong>CERT-In Empaneled Auditor</strong></td>
        <td>Pre-Launch VAPT Security Clearance</td>
        <td><span class="pill gov">Statutory</span></td>
        <td>Comprehensive Vulnerability Assessment and Penetration Testing of mobile app, API gateway, and cloud infrastructure.</td>
        <td>3 – 4 Weeks</td>
      </tr>
      <tr>
        <td><strong>UIDAI / KRA</strong></td>
        <td>KRA & DigiLocker Onboarding Agency</td>
        <td><span class="pill mand">Mandatory</span></td>
        <td>Empanelment with CVL KRA, NDML, or CKYC registry for paperless customer verification and record sharing.</td>
        <td>1 Month</td>
      </tr>
    </tbody>
  </table>

  <div class="callout-box warning">
    <div class="callout-title">⚠️ Statutory Personnel Requirement: Compliance Officer (NISM Certified)</div>
    Under SEBI (Stock Brokers) Regulations, 1992, every registered broker <strong>MUST appoint a full-time Compliance Officer</strong> who has cleared the <strong>NISM Series-VII: Securities Operations and Risk Management Certification</strong> and <strong>NISM Series-VIII: Equity Derivatives Certification</strong>. A Principal Officer with at least 5 years of financial market experience must also be designated.
  </div>

  <h2>Why Each Approval is Critical (The "Need" Analysis)</h2>
  <div class="two-col">
    <div class="card">
      <div class="card-header">1. SEBI Broker Registration (Form A)</div>
      <p style="font-size: 8.5pt;"><strong>The Need:</strong> Without SEBI registration, it is legally prohibited in India to onboard retail users, collect margin funds, or execute equity/derivative orders. Operating without it constitutes an illegal bucket shop (Dabba trading) carrying severe criminal penalties under the SCRA Act.</p>
    </div>
    <div class="card">
      <div class="card-header">2. CDSL Depository Participant (DP)</div>
      <p style="font-size: 8.5pt;"><strong>The Need:</strong> When a user buys equity delivery (CNC) or holds shares, those securities must sit in an electronic depository. Having a CDSL DP license allows your app to seamlessly create Demat accounts and trigger digital Demat Debit and Pledge Instructions (DDPI).</p>
    </div>
  </div>

  <div class="two-col">
    <div class="card">
      <div class="card-header">3. NSE/BSE CTCL & TAP Terminal Approvals</div>
      <p style="font-size: 8.5pt;"><strong>The Need:</strong> Exchanges require all proprietary algorithmic trading or automated retail Order Management Systems (OMS) to undergo TAP (Telecommunication Access Point) and CTCL (Computer to Computer Link) compliance audits to prevent errant orders from causing flash crashes.</p>
    </div>
    <div class="card">
      <div class="card-header">4. CERT-In Certified VAPT Audit</div>
      <p style="font-size: 8.5pt;"><strong>The Need:</strong> Financial applications holding bank account credentials, biometric signatures, and trading APIs are prime cyber-targets. SEBI mandates that a certified security audit report be submitted before go-live and repeated every quarter without fail.</p>
    </div>
  </div>
</div>

<!-- ================= SECTION 2: LEGAL DOCUMENTATION CHECKLIST ================= -->
<div class="page-break">
  <h1 class="section-title"><span class="sec-num">02</span> Legal Documentation & Readiness Checklist</h1>

  <p>To avoid bottlenecks during regulatory scrutiny, the following corporate, financial, and technical documents must be kept ready in advance by the client's legal counsel and financial auditors:</p>

  <h2>Corporate & Statutory Documentation</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 30%;">Document Name</th>
        <th style="width: 45%;">Description & Regulatory Purpose</th>
        <th style="width: 25%;">Issuing Authority</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>MOA & AOA</strong></td>
        <td>Memorandum and Articles of Association explicitly permitting financial services, share broking, and algorithmic trading activities in the main object clauses.</td>
        <td>MCA / ROC</td>
      </tr>
      <tr>
        <td><strong>Net Worth Certificate</strong></td>
        <td>Audited computation statement showing minimum net worth of ₹1.00 Crore (or higher based on segment selection) derived from unencumbered paid-up capital and free reserves.</td>
        <td>Practicing Chartered Accountant</td>
      </tr>
      <tr>
        <td><strong>Board Resolution for Brokerage</strong></td>
        <td>Certified board resolution approving application for SEBI and exchange memberships, authorizing designated directors, and naming the compliance team.</td>
        <td>Board of Directors</td>
      </tr>
      <tr>
        <td><strong>Directors' Fit & Proper Affidavit</strong></td>
        <td>Formal declaration under SEBI (Intermediaries) Regulations confirming no director or promoter has economic offense convictions, regulatory bans, or defaults.</td>
        <td>Notarized Affidavit</td>
      </tr>
      <tr>
        <td><strong>Premises Lease & Infrastructure Deed</strong></td>
        <td>Registered commercial office lease showing dedicated physical premises capable of hosting risk control terminals, compliance desks, and secure server enclosures.</td>
        <td>Commercial Landlord / Sub-Registrar</td>
      </tr>
    </tbody>
  </table>

  <h2>Technical & Cybersecurity Documentation</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 30%;">Technical Policy</th>
        <th style="width: 45%;">Content & Scope Required by SEBI</th>
        <th style="width: 25%;">Prepared By</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Comprehensive Cyber Security Policy</strong></td>
        <td>Document outlining ISO 27001 alignment, access controls, network segregation, zero-trust architecture, multi-factor authentication (MFA), and incident response protocols.</td>
        <td>CTO / CISO</td>
      </tr>
      <tr>
        <td><strong>Business Continuity & DR Plan</strong></td>
        <td>Disaster Recovery (DR) and Business Continuity Plan (BCP) ensuring Recovery Point Objective (RPO) < 15 mins and Recovery Time Objective (RTO) < 30 mins during exchange outages.</td>
        <td>DevOps & Infra Lead</td>
      </tr>
      <tr>
        <td><strong>System & Algorithmic Architecture Spec</strong></td>
        <td>Technical dossier explaining order throttling, exchange freeze limits, auto-squareoff mechanisms, margin validation logic, and WebSocket tick delivery pipelines.</td>
        <td>Lead Systems Architect</td>
      </tr>
      <tr>
        <td><strong>Data Localization Declaration</strong></td>
        <td>Affidavit affirming that all user financial records, transactions, Aadhaar XMLs, and telemetry reside exclusively in Indian cloud regions (e.g., AWS Mumbai ap-south-1).</td>
        <td>Cloud Architect / Legal</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ================= SECTION 3: DECODED 14-STEP ONBOARDING & KYC ================= -->
<div class="page-break">
  <h1 class="section-title"><span class="sec-num">03</span> End-to-End User KYC & Document Readiness</h1>

  <p>Our deep decompilation of Sahi's production APK revealed their exact <strong>14-Step Digital KYC Onboarding Flow</strong>. To provide an identical, zero-friction experience that converts retail traders within 5 minutes, the client app will integrate the exact same verified fintech partners:</p>

  <div class="avoid-break">
    <h2>The Decoded 14-Step Onboarding Architecture</h2>
    
    <div class="flow-step">
      <div class="step-circle">1</div>
      <div class="step-content"><strong>Mobile Number & Device Binding:</strong> High-speed 6-digit OTP verification via SMS gateway (Msg91/Twilio) with device hardware fingerprinting.</div>
    </div>
    <div class="flow-step">
      <div class="step-circle">2</div>
      <div class="step-content"><strong>DigiLocker Aadhaar e-KYC (Digio SDK):</strong> User authenticates via UIDAI DigiLocker gateway. Extracts verified legal name, date of birth, photo, and residential address in signed XML.</div>
    </div>
    <div class="flow-step">
      <div class="step-circle">3</div>
      <div class="step-content"><strong>PAN Verification & NSDL Validation:</strong> Real-time PAN lookup via NSDL API. Matches name and DOB against Aadhaar XML; handles mismatch logic (`nsdl_pan_dob_mismatch_error.json`).</div>
    </div>
    <div class="flow-step">
      <div class="step-circle">4</div>
      <div class="step-content"><strong>PAN-Aadhaar Linking Check:</strong> Statutory verification that the user's PAN is actively linked to Aadhaar per Income Tax Department rules (`aadhar_pan_linking.json`).</div>
    </div>
    <div class="flow-step">
      <div class="step-circle">5</div>
      <div class="step-content"><strong>Bank Verification via Penny Drop:</strong> Automated ₹1.00 credit to user's bank account via NPCI IMPS. Validates account holder name match using fuzzy logic (`bank_verification_screen.json`).</div>
    </div>
    <div class="flow-step">
      <div class="step-circle">6</div>
      <div class="step-content"><strong>Personal & Income Profile:</strong> Capture of marital status, occupation, and mandatory SEBI income brackets (&lt;1L, 1-5L, 5-10L, 10-25L, &gt;25L) (`personal_details.json`).</div>
    </div>
    <div class="flow-step">
      <div class="step-circle">7</div>
      <div class="step-content"><strong>Nominee Declaration:</strong> Digital nomination capture (up to 3 nominees with percentage allocation) compliant with SEBI circulars (`nominee_screen.json`).</div>
    </div>
    <div class="flow-step">
      <div class="step-circle">8</div>
      <div class="step-content"><strong>Live Selfie & AI Liveness Detection (HyperVerge):</strong> User captures selfie; HyperVerge AI assesses 3D liveness and computes face-match percentage against DigiLocker photo (`liveness_dark.png`).</div>
    </div>
    <div class="flow-step">
      <div class="step-circle">9</div>
      <div class="step-content"><strong>Digital Trackpad Signature:</strong> User draws signature on custom touch canvas (`trackpad_signature.json`). Converted to high-res transparent PNG for contract signing.</div>
    </div>
    <div class="flow-step">
      <div class="step-circle">10</div>
      <div class="step-content"><strong>F&O Segment Activation:</strong> Upload of 6-month bank statement (PDF parser with bank statement analyzer), latest ITR, or salary slip for derivatives trading clearance.</div>
    </div>
    <div class="flow-step">
      <div class="step-circle">11</div>
      <div class="step-content"><strong>Aadhaar e-Sign on KYC Contract (Digio SDK):</strong> Automated generation of SEBI Rights & Obligations KYC PDF. User signs with Aadhaar OTP via NSDL/CDSL e-Sign gateway (`esign.json`).</div>
    </div>
    <div class="flow-step">
      <div class="step-circle">12</div>
      <div class="step-content"><strong>DDPI Authorization:</strong> Demat Debit and Pledge Instruction digital mandate authorization. Eliminates TPIN requirement when selling equity delivery (`ddpi_faq.json`).</div>
    </div>
    <div class="flow-step">
      <div class="step-circle">13</div>
      <div class="step-content"><strong>e-Mandate / UPI Autopay:</strong> Optional setup of instant bank mandate for automated trading account fund top-ups via NPCI UPI (`com.digio.esignMandate`).</div>
    </div>
    <div class="flow-step">
      <div class="step-circle">14</div>
      <div class="step-content"><strong>Instant Account Provisioning & CDSL Allocation:</strong> Automated Demat allocation, welcome tour, and notification dispatch (`quick_tour.json`).</div>
    </div>
  </div>

  <h2>Confirmed Vendor Integrations (from Sahi APK Analysis)</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Vendor / SDK</th>
        <th>Function in Sahi</th>
        <th>Pricing Model</th>
        <th>Why We Recommend It</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Digio SDK</strong></td>
        <td>DigiLocker, Aadhaar e-Sign, DDPI, e-Mandate</td>
        <td>₹15 – ₹25 per complete KYC</td>
        <td>De facto industry standard; zero-drop-off native Flutter SDK.</td>
      </tr>
      <tr>
        <td><strong>HyperVerge HyperKYC</strong></td>
        <td>3D Liveness Detection & Face Matching</td>
        <td>₹10 – ₹18 per verification</td>
        <td>Eliminates fraud; prevents spoofing and bot account creation.</td>
      </tr>
      <tr>
        <td><strong>RazorpayX / Cashfree</strong></td>
        <td>Penny Drop Bank Verification & UPI Pay-In</td>
        <td>₹2 – ₹5 / lookup | 0% UPI</td>
        <td>99.9% uptime for instant fund additions via GPay, PhonePe, Paytm.</td>
      </tr>
      <tr>
        <td><strong>Freshchat (Freshworks)</strong></td>
        <td>In-App Customer Support & AI FAQ Bot</td>
        <td>$19 – $49 / agent / month</td>
        <td>13 native Android activities confirmed in Sahi APK for support ticketing.</td>
      </tr>
      <tr>
        <td><strong>MoEngage</strong></td>
        <td>User Engagement & Event-Driven Push</td>
        <td>Volume tiered (SaaS)</td>
        <td>Nudges inactive users, delivers price triggers, sends margin calls.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ================= SECTION 4: TECHNICAL ARCHITECTURE & CORE FEATURES ================= -->
<div class="page-break">
  <h1 class="section-title"><span class="sec-num">04</span> Technical Architecture & Core Feature Stack</h1>

  <p>Our reverse engineering proved that Sahi achieved market-leading speed by abandoning off-the-shelf web-based charting (like TradingView embedded webviews) and implementing a <strong>100% native Flutter Canvas engine</strong> paired with a <strong>high-concurrency Go (Golang) microservices backend</strong>.</p>

  <h2>The 12 Sahi Modular Flutter Packages We Will Build</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 25%;">Package Name</th>
        <th style="width: 45%;">Engineering Scope & Deliverables</th>
        <th style="width: 30%;">Performance Benchmark</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>`packages/chart`</strong></td>
        <td>Custom Flutter `CustomPainter` canvas engine. Renders candlesticks, OHLC bars, volume histograms, multi-timeframe zoom/pan, and dynamic crosshairs directly on GPU.</td>
        <td>Constant 60 FPS; zero layout reflows; sub-16ms redraw on incoming ticks.</td>
      </tr>
      <tr>
        <td><strong>`packages/mscalper_train`</strong></td>
        <td><strong>Sahi Scalper 2.0 & Practice Terminal:</strong> Dual synced chart layout (Index + Option Contract), 1-Tap buy/sell execution, Exit at Market panic button, and full paper-trading playback simulator.</td>
        <td>Sub-second order trigger; zero confirmation modal latency.</td>
      </tr>
      <tr>
        <td><strong>`packages/ai_assistant`</strong></td>
        <td><strong>Kyro AI Assistant:</strong> Conversational technical indicator creator. Houses custom Lottie animations (`orb/glow`, `loader_loop`, `thinking_intro`).</td>
        <td>Generates runnable indicator math from plain English in &lt; 2.5 seconds.</td>
      </tr>
      <tr>
        <td><strong>`packages/sahiscript_ui`</strong></td>
        <td><strong>SahiScript Code Editor:</strong> PineScript-style custom domain language with syntax highlighting, custom emoji fonts (`SahiScriptEmoji.ttf`), and math evaluator.</td>
        <td>In-memory AST parsing and real-time chart overlay rendering.</td>
      </tr>
      <tr>
        <td><strong>`packages/system_indicators`</strong></td>
        <td><strong>18 Built-In AI & Quantitative Indicators:</strong> Lorentzian Classification, Nadaraya-Watson Envelopes, SuperTrend AI, OI-based Support/Resistance zones (`svgs.bin`).</td>
        <td>Pre-compiled binary format for instantaneous chart computation.</td>
      </tr>
      <tr>
        <td><strong>`packages/dls` & `dls_icons`</strong></td>
        <td>Design Language System providing deep OLED dark theme, high-contrast bullish (#26A69A) / bearish (#EF5350) tokens, and custom SVG icons.</td>
        <td>Zero design drift across screens; atomic design token system.</td>
      </tr>
      <tr>
        <td><strong>`packages/upi_apps`</strong></td>
        <td>Native Android & iOS UPI intent dispatcher targeting GPay, PhonePe, Paytm, and CRED apps directly without opening browser gateways.</td>
        <td>Zero payment gateway drop-off; instant callback balance credit.</td>
      </tr>
    </tbody>
  </table>

  <h2>High-Performance Backend Infrastructure</h2>
  <div class="two-col">
    <div class="card">
      <div class="card-header">1. Market Data Tick Engine (Go / C++)</div>
      <p style="font-size: 8.5pt;">Direct connection to exchange FIX/CTCL multicasts. Ingests raw binary ticks, normalizes to compact Protobuf packets, pushes to Apache Kafka, and fans out to 100,000+ client WebSockets via dedicated Go workers with sub-millisecond serialization.</p>
    </div>
    <div class="card">
      <div class="card-header">2. Order Management System (OMS)</div>
      <p style="font-size: 8.5pt;">Handles order routing, automated exchange freeze-limit splitting (e.g., Nifty 1800-lot quantity freeze limits), stop-loss trailing, and state persistence in ACID-compliant PostgreSQL with millisecond latency.</p>
    </div>
  </div>

  <div class="two-col">
    <div class="card">
      <div class="card-header">3. Risk Management System (RMS)</div>
      <p style="font-size: 8.5pt;">Performs real-time SPAN & Exposure margin checks before any order leaves the server. Includes <strong>PnL Protect</strong> logic: automatically disables trading and squares off open positions if user hits their self-imposed daily loss threshold.</p>
    </div>
    <div class="card">
      <div class="card-header">4. Time-Series OHLC Store (TimescaleDB)</div>
      <p style="font-size: 8.5pt;">Aggregates raw tick events into 1-second, 1-minute, 5-minute, and daily candles. Stores billions of historical data points with hypertable partitioning, allowing charts to pull 10 years of data in milliseconds.</p>
    </div>
  </div>
</div>

<!-- ================= SECTION 5: KYRO AI & MACHINE LEARNING INTEGRATION ================= -->
<div class="page-break">
  <h1 class="section-title"><span class="sec-num">05</span> Kyro AI & Machine Learning Integration</h1>

  <p>One of Sahi's most viral and defensible competitive moats is <strong>Kyro AI</strong> and its suite of <strong>18 Machine Learning Chart Indicators</strong>. We will engineer an identical AI architecture to provide your users with unmatched intelligence:</p>

  <h2>How Kyro Natural Language Indicator Creation Works</h2>
  <div class="flow-step">
    <div class="step-circle">1</div>
    <div class="step-content"><strong>User Natural Language Prompt:</strong> A trader types or speaks: <em>"Show me buy signals when 5-EMA crosses 20-EMA, but only if RSI is below 40 and Open Interest has increased by 10% today."</em></div>
  </div>
  <div class="flow-step">
    <div class="step-circle">2</div>
    <div class="step-content"><strong>AI Inference Gateway (Fine-Tuned LLM):</strong> Request is transmitted to our secure Python microservice. A fine-tuned LLM (Claude 3.5 Sonnet / Gemini Flash via secure API) translates the natural language into mathematical AST (Abstract Syntax Tree) in <strong>SahiScript</strong> format.</div>
  </div>
  <div class="flow-step">
    <div class="step-circle">3</div>
    <div class="step-content"><strong>Sandboxed Validation & Backtesting:</strong> Backend compiles the SahiScript, tests against the last 500 candles to verify zero divide-by-zero or infinite loop bugs, and generates historical win-rate stats.</div>
  </div>
  <div class="flow-step">
    <div class="step-circle">4</div>
    <div class="step-content"><strong>Instant GPU Chart Overlay:</strong> SahiScript bytecode is streamed to the Flutter mobile app. The Canvas engine immediately renders color-coded buy/sell arrows and zones on the active chart.</div>
  </div>

  <h2>The 18 Built-In Machine Learning Indicators Included</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 25%;">Indicator Category</th>
        <th style="width: 45%;">Mathematical Model & Algorithm</th>
        <th style="width: 30%;">Trader Utility</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Lorentzian Classification</strong></td>
        <td>Non-parametric machine-learning classifier utilizing Lorentzian metric spaces to identify directional trend regime changes.</td>
        <td>Provides high-probability intraday buy/sell confirmation for index options.</td>
      </tr>
      <tr>
        <td><strong>Nadaraya-Watson Envelopes</strong></td>
        <td>Kernel regression estimator mapping dynamic non-linear trendlines and volatility envelope bands with adaptive bandwidth smoothing.</td>
        <td>Prevents scalpers from chasing false breakouts; highlights mean-reversion zones.</td>
      </tr>
      <tr>
        <td><strong>AI SuperTrend Adaptive</strong></td>
        <td>Machine learning-optimized ATR multiplier dynamically adjusted based on real-time market volatility clusters.</td>
        <td>Trailing stop-loss guide that automatically widens in chop and tightens in trends.</td>
      </tr>
      <tr>
        <td><strong>Open Interest (OI) Heatmap</strong></td>
        <td>Multi-strike call/put open interest accumulation matrix rendered directly as a background heatmap behind price candles.</td>
        <td>Reveals institutional call writing & put support levels instantly without switching screens.</td>
      </tr>
      <tr>
        <td><strong>Market Sentiment Meter</strong></td>
        <td>Algorithmic analysis of advance-decline ratios, sector breadth, and index heavyweight momentum updated every 5 minutes.</td>
        <td>Gives scalpers an immediate macro bias (Strong Bullish, Neutral, Bearish).</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ================= SECTION 6: COMPREHENSIVE COSTING BREAKDOWN ================= -->
<div class="page-break">
  <h1 class="section-title"><span class="sec-num">06</span> Comprehensive Itemized Costing & Budget</h1>

  <p>Below is the complete, transparent, item-by-item investment ledger. Every cost is categorized with its regulatory, operational, or technical justification:</p>

  <h2>Table 6.1 — Regulatory, Legal & Statutory Expenses (One-Time)</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Expense Head</th>
        <th>Estimated Min (₹)</th>
        <th>Estimated Max (₹)</th>
        <th>Refundable?</th>
        <th>Why It Is Required (The Need)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Company Incorporation (Pvt Ltd)</td>
        <td class="cost-col">₹12,000</td>
        <td class="cost-col">₹25,000</td>
        <td>No</td>
        <td>Legal corporate entity required before applying for financial licenses.</td>
      </tr>
      <tr>
        <td>SEBI Application & Registration Fee</td>
        <td class="cost-col">₹1,18,000</td>
        <td class="cost-col">₹1,77,000</td>
        <td>No</td>
        <td>Official statutory fee paid to SEBI with Form A application (+18% GST).</td>
      </tr>
      <tr>
        <td>SEBI Legal Counsel & Filing Retainer</td>
        <td class="cost-col">₹3,00,000</td>
        <td class="cost-col">₹6,00,000</td>
        <td>No</td>
        <td>Specialist securities law firm to draft policies and manage SEBI queries.</td>
      </tr>
      <tr>
        <td>NSE Admission (CM & F&O Segments)</td>
        <td class="cost-col">₹8,00,000</td>
        <td class="cost-col">₹15,00,000</td>
        <td>Partially</td>
        <td>Mandatory admission fee for access to Equity and F&O trading rings.</td>
      </tr>
      <tr>
        <td>NSE Base Minimum Capital (BMC)</td>
        <td class="cost-col">₹10,00,000</td>
        <td class="cost-col">₹25,00,000</td>
        <td><strong>Yes (100%)</strong></td>
        <td>Lock-in deposit with exchange (FDR/BG). Returned if membership surrendered.</td>
      </tr>
      <tr>
        <td>BSE DBM Membership & Deposit</td>
        <td class="cost-col">₹10,50,000</td>
        <td class="cost-col">₹15,00,000</td>
        <td>Partially</td>
        <td>Required for BSE Sensex and stock derivative trading connectivity.</td>
      </tr>
      <tr>
        <td>CDSL DP Registration & Gateway</td>
        <td class="cost-col">₹1,50,000</td>
        <td class="cost-col">₹3,00,000</td>
        <td>Partially</td>
        <td>Enables app to open Demat accounts and execute CDSL e-DIS settlements.</td>
      </tr>
      <tr>
        <td>Pre-Launch CERT-In VAPT Audit</td>
        <td class="cost-col">₹2,50,000</td>
        <td class="cost-col">₹5,00,000</td>
        <td>No</td>
        <td>Mandatory security testing certificate submitted to SEBI before go-live.</td>
      </tr>
      <tr>
        <td>CA Net Worth Certificate & Audits</td>
        <td class="cost-col">₹50,000</td>
        <td class="cost-col">₹1,00,000</td>
        <td>No</td>
        <td>Certification proving ₹1.00 Crore+ unencumbered capital backing.</td>
      </tr>
      <tr>
        <td>Office Setup & Dedicated Leasehold</td>
        <td class="cost-col">₹2,00,000</td>
        <td class="cost-col">₹6,00,000</td>
        <td>Partially</td>
        <td>SEBI physical inspection requires designated commercial premises.</td>
      </tr>
      <tr class="total-row">
        <td>TOTAL REGULATORY & LEGAL</td>
        <td class="cost-col">₹39,30,000</td>
        <td class="cost-col">₹78,02,000</td>
        <td colspan="2"><em>*Includes ~₹25L–₹35L refundable deposits</em></td>
      </tr>
    </tbody>
  </table>

  <h2>Table 6.2 — Engineering & Technology Development Costs (One-Time)</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Development Module</th>
        <th>Estimated Min (₹)</th>
        <th>Estimated Max (₹)</th>
        <th>Duration</th>
        <th>Deliverables & Scope</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Flutter Mobile App (Android & iOS)</td>
        <td class="cost-col">₹22,00,000</td>
        <td class="cost-col">₹38,00,000</td>
        <td>6 Months</td>
        <td>Full Flutter app, design tokens, biometric login, portfolio, order book.</td>
      </tr>
      <tr>
        <td>Custom 60fps Canvas Charting Engine</td>
        <td class="cost-col">₹12,00,000</td>
        <td class="cost-col">₹22,00,000</td>
        <td>3.5 Months</td>
        <td>In-house CustomPainter engine; multi-timeframe candle math; GPU rendering.</td>
      </tr>
      <tr>
        <td>Sahi Scalper 2.0 & Practice Terminal</td>
        <td class="cost-col">₹8,00,000</td>
        <td class="cost-col">₹16,00,000</td>
        <td>2.5 Months</td>
        <td>Dual synced charts, 1-tap limits, best bid exit, paper trading simulator.</td>
      </tr>
      <tr>
        <td>Backend Order Engine (OMS) & RMS</td>
        <td class="cost-col">₹18,00,000</td>
        <td class="cost-col">₹32,00,000</td>
        <td>4 Months</td>
        <td>Go microservices, margin validation, freeze splitting, PostgreSQL ledgers.</td>
      </tr>
      <tr>
        <td>Exchange Tick Ingestion & WebSocket</td>
        <td class="cost-col">₹10,00,000</td>
        <td class="cost-col">₹18,00,000</td>
        <td>3 Months</td>
        <td>Kafka stream pipeline, tick normalizer, high-concurrency Go WebSocket.</td>
      </tr>
      <tr>
        <td>14-Step KYC & Digio/HyperVerge API</td>
        <td class="cost-col">₹5,00,000</td>
        <td class="cost-col">₹9,00,000</td>
        <td>2 Months</td>
        <td>DigiLocker, PAN NSDL, penny drop, 3D selfie liveness, Aadhaar e-Sign.</td>
      </tr>
      <tr>
        <td>Kyro AI & 18 Machine Learning Indicators</td>
        <td class="cost-col">₹12,00,000</td>
        <td class="cost-col">₹24,00,000</td>
        <td>3 Months</td>
        <td>Natural language indicator prompt compiler, SahiScript AST, Lorentzian math.</td>
      </tr>
      <tr>
        <td>Exchange CTCL/FIX Certification Testing</td>
        <td class="cost-col">₹6,00,000</td>
        <td class="cost-col">₹12,00,000</td>
        <td>2 Months</td>
        <td>Exchange sandbox mock trading rounds, conformance tests, TAP gateway.</td>
      </tr>
      <tr>
        <td>Web Trading Terminal (React/Next.js)</td>
        <td class="cost-col">₹10,00,000</td>
        <td class="cost-col">₹20,00,000</td>
        <td>3 Months</td>
        <td>Browser trading portal with synchronized watchlists, charts, and orders.</td>
      </tr>
      <tr>
        <td>Admin Panel, Backoffice & Risk Portal</td>
        <td class="cost-col">₹5,00,000</td>
        <td class="cost-col">₹10,00,000</td>
        <td>2 Months</td>
        <td>Operations dashboard, KYC manual verification fallback, margin monitor.</td>
      </tr>
      <tr class="total-row">
        <td>TOTAL DEVELOPMENT COST</td>
        <td class="cost-col">₹1,08,00,000</td>
        <td class="cost-col">₹2,01,00,000</td>
        <td colspan="2"><em>Complete Turnkey Product Delivery</em></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ================= SECTION 6 CONTINUED: OPERATIONAL & RECURRING COSTS ================= -->
<div class="page-break">
  <h1 class="section-title"><span class="sec-num">06.2</span> Operational, Cloud & Third-Party Recurring Costs</h1>

  <h2>Table 6.3 — Third-Party APIs, Feeds & Cloud Hosting (Annual Budget)</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Service / Infrastructure Component</th>
        <th>MVP Stage (Year 1)</th>
        <th>Growth Stage (100K Users)</th>
        <th>Why It Is Required</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>AWS Cloud Hosting (ap-south-1 Mumbai)</strong><br><small>EKS, RDS Postgres Multi-AZ, ElastiCache Redis, Kafka, CloudFront</small></td>
        <td class="cost-col">₹11,50,000 / yr</td>
        <td class="cost-col">₹1,35,00,000 / yr</td>
        <td>RBI mandates Indian data residency. Real-time WebSockets and multi-AZ failover require high-throughput AWS infrastructure.</td>
      </tr>
      <tr>
        <td><strong>NSE Market Data Feed (Direct or Vendor)</strong><br><small>Level 1 (LTP) & Level 2 (5-Depth Order Book)</small></td>
        <td class="cost-col">₹4,00,000 / yr</td>
        <td class="cost-col">₹25,00,000 / yr</td>
        <td>Official exchange license to redistribute live price ticks and market depth to retail client apps.</td>
      </tr>
      <tr>
        <td><strong>Digio SDK (e-Sign, DigiLocker, DDPI)</strong><br><small>Based on onboarding volume</small></td>
        <td class="cost-col">₹3,00,000 / yr<br><small>(~12,000 KYCs)</small></td>
        <td class="cost-col">₹18,00,000 / yr<br><small>(~80,000 KYCs)</small></td>
        <td>Pay-as-you-go per completed paperless onboarding. Direct integration with UIDAI, CDSL, and NSDL.</td>
      </tr>
      <tr>
        <td><strong>HyperVerge (AI Liveness & Face Match)</strong><br><small>Per verified selfie session</small></td>
        <td class="cost-col">₹1,80,000 / yr</td>
        <td class="cost-col">₹10,50,000 / yr</td>
        <td>Zero-drop AI biometric validation preventing fraudulent or proxy accounts.</td>
      </tr>
      <tr>
        <td><strong>Kyro AI Inference (LLM Token Budget)</strong><br><small>Claude 3.5 Sonnet / Gemini Flash API</small></td>
        <td class="cost-col">₹1,20,000 / yr</td>
        <td class="cost-col">₹8,00,000 / yr</td>
        <td>API token costs for translating user plain English requests into runnable SahiScript indicator code.</td>
      </tr>
      <tr>
        <td><strong>SMS Gateway & OTP Delivery (Msg91/Twilio)</strong><br><small>Login, trading OTP, trade confirmation alerts</small></td>
        <td class="cost-col">₹90,000 / yr</td>
        <td class="cost-col">₹6,00,000 / yr</td>
        <td>SEBI requires mandatory SMS notifications for all executed trades and fund transactions.</td>
      </tr>
      <tr>
        <td><strong>Customer Support (Freshchat / Freshworks)</strong><br><small>SaaS subscription for agent seats</small></td>
        <td class="cost-col">₹1,80,000 / yr</td>
        <td class="cost-col">₹5,40,000 / yr</td>
        <td>Multi-channel in-app chat ticketing system confirmed in Sahi's native Android build.</td>
      </tr>
      <tr>
        <td><strong>MoEngage (Push & Retargeting)</strong><br><small>User engagement & retention SaaS</small></td>
        <td class="cost-col">₹1,50,000 / yr</td>
        <td class="cost-col">₹7,50,000 / yr</td>
        <td>Drives active trading days through automated notifications (e.g. expiring options, margin alerts).</td>
      </tr>
      <tr>
        <td><strong>Sentry & New Relic (APM & Crash Replay)</strong><br><small>Developer monitoring suite</small></td>
        <td class="cost-col">₹2,40,000 / yr</td>
        <td class="cost-col">₹7,20,000 / yr</td>
        <td>Captures UI frame drops, network timeouts, and app crashes across device models.</td>
      </tr>
      <tr>
        <td><strong>Quarterly CERT-In VAPT Audits</strong><br><small>4 statutory audits per year</small></td>
        <td class="cost-col">₹8,00,000 / yr</td>
        <td class="cost-col">₹16,00,000 / yr</td>
        <td>Mandatory SEBI regulatory filing to ensure zero unpatched cybersecurity vulnerabilities.</td>
      </tr>
      <tr class="total-row">
        <td>TOTAL RECURRING / OPERATIONAL</td>
        <td class="cost-col">₹36,10,000 / yr</td>
        <td class="cost-col">₹2,38,60,000 / yr</td>
        <td><em>*Scales dynamically with user base</em></td>
      </tr>
    </tbody>
  </table>

  <h2>Table 6.4 — Core Human Capital & Team Salaries (Pre-Launch to Year 1)</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Core Position</th>
        <th>Headcount</th>
        <th>Monthly Salary (₹)</th>
        <th>Annual Total (₹)</th>
        <th>Core Responsibility</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Chief Technology Officer (CTO)</strong></td>
        <td>1</td>
        <td class="cost-col">₹3,50,000</td>
        <td class="cost-col">₹42,00,000</td>
        <td>Overall architectural authority; exchange TAP sign-off.</td>
      </tr>
      <tr>
        <td><strong>Compliance Officer (NISM VII & VIII)</strong></td>
        <td>1</td>
        <td class="cost-col">₹80,000</td>
        <td class="cost-col">₹9,60,000</td>
        <td>Statutory SEBI liaison, daily reporting, client grievance handling.</td>
      </tr>
      <tr>
        <td><strong>Lead Flutter Mobile Engineer</strong></td>
        <td>1</td>
        <td class="cost-col">₹1,80,000</td>
        <td class="cost-col">₹21,60,000</td>
        <td>Maintains `packages/chart`, `mscalper_train`, and mobile UX.</td>
      </tr>
      <tr>
        <td><strong>Senior Go (Golang) Backend Engineer</strong></td>
        <td>2</td>
        <td class="cost-col">₹3,20,000 (total)</td>
        <td class="cost-col">₹38,40,000</td>
        <td>Maintains low-latency OMS, RMS, and WebSocket feed pipeline.</td>
      </tr>
      <tr>
        <td><strong>DevOps / Site Reliability Engineer</strong></td>
        <td>1</td>
        <td class="cost-col">₹1,40,000</td>
        <td class="cost-col">₹16,80,000</td>
        <td>Manages AWS Kubernetes (EKS), zero-downtime CI/CD, and WAF.</td>
      </tr>
      <tr>
        <td><strong>Customer Support & Operations</strong></td>
        <td>2</td>
        <td class="cost-col">₹70,000 (total)</td>
        <td class="cost-col">₹8,40,000</td>
        <td>Handles Freshchat tickets, manual KYC escalations, and fund payouts.</td>
      </tr>
      <tr class="total-row">
        <td>TOTAL TEAM PAYROLL (8 Members)</td>
        <td>8</td>
        <td class="cost-col">₹11,40,000 / mo</td>
        <td class="cost-col">₹1,36,80,000 / yr</td>
        <td><em>*Baseline lean team for Year 1</em></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ================= SECTION 7: STRATEGIC MODEL COMPARISON ================= -->
<div class="page-break">
  <h1 class="section-title"><span class="sec-num">07</span> Strategic Route: Model A vs. Model B</h1>

  <p>To provide complete clarity on capital allocation and time-to-market, the table below highlights the operational and financial contrast between launching as an independent broker versus starting via an established partner API:</p>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 25%;">Evaluation Metric</th>
        <th style="width: 37%;">Model A: Independent SEBI Broker<br><small>(Full Sahi Infrastructure Replica)</small></th>
        <th style="width: 38%;">Model B: Partner / Sub-Broker Terminal<br><small>(Powered by Zerodha / Dhan APIs)</small></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Capital Expenditure (Year 1)</strong></td>
        <td class="cost-col" style="text-align: left;"><strong>₹4.50 – ₹8.00 Crore</strong><br><small>(Includes ₹30L+ refundable deposits)</small></td>
        <td class="cost-col" style="text-align: left;"><strong>₹1.50 – ₹3.50 Crore</strong><br><small>(Zero exchange deposit requirements)</small></td>
      </tr>
      <tr>
        <td><strong>Time to Market</strong></td>
        <td><strong>10 – 14 Months</strong> (governed by SEBI inspection and exchange queue)</td>
        <td><strong>4 – 6 Months</strong> (ready as soon as Flutter app & UI are completed)</td>
      </tr>
      <tr>
        <td><strong>Regulatory Burden</strong></td>
        <td>High: Daily trade reporting, quarterly VAPT, monthly compliance certificates.</td>
        <td>Minimal: Primary compliance, margin reporting, and audit handled by parent broker.</td>
      </tr>
      <tr>
        <td><strong>Net Worth Mandatory Rule</strong></td>
        <td>₹1.00 Crore+ certified unencumbered net worth locked in company.</td>
        <td>Zero statutory net worth lock-in.</td>
      </tr>
      <tr>
        <td><strong>Brokerage Monetization</strong></td>
        <td>100% of ₹10/order flat fee retained + interest float on client balances + MTF margin revenue.</td>
        <td>Revenue share model: Receive 20% to 40% sharing of generated brokerage volume.</td>
      </tr>
      <tr>
        <td><strong>Custom Feature Flexibility</strong></td>
        <td>100% freedom: Can execute proprietary Scalper 2.0 freeze-splitting and custom matching.</td>
        <td>Constrained by parent broker's API rate limits (e.g. 10–20 orders/sec limits).</td>
      </tr>
      <tr>
        <td><strong>Recommended Use-Case</strong></td>
        <td>Funded startups or existing financial institutions with ₹10 Cr+ capital backing.</td>
        <td>Early-stage founders validating product-market fit with active scalpers rapidly.</td>
      </tr>
    </tbody>
  </table>

  <div class="callout-box strategic">
    <div class="callout-title">💡 Phased Strategic Recommendation</div>
    We recommend a <strong>Two-Stage Phased Approach</strong>: Launch <strong>Model B (Partner Terminal)</strong> in Month 4 to start onboarding traders, testing the custom 60fps chart engine, and capturing active F&O scalpers. In parallel, initiate the SEBI corporate paperwork. Once you hit <strong>25,000 active traders</strong>, seamlessly transition users to your own SEBI license (Model A) without altering their user experience.
  </div>
</div>

<!-- ================= SECTION 8: ROADMAP, MILESTONES & SIGN-OFF ================= -->
<div class="page-break">
  <h1 class="section-title"><span class="sec-num">08</span> Execution Roadmap, Milestones & Sign-Off</h1>

  <p>The project will execute across 6 distinct engineering milestones with clear deliverables and acceptance criteria:</p>

  <table class="data-table">
    <thead>
      <tr>
        <th>Milestone</th>
        <th>Timeline</th>
        <th>Engineering Deliverables</th>
        <th>Payment Tranche</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Milestone 1: Architecture & UI/UX</strong></td>
        <td>Month 1</td>
        <td>Figma high-fidelity prototypes of all 45 screens (Scalper 2.0, Option Chain, Kyro AI); AWS cloud VPC setup; base Flutter project structure.</td>
        <td class="cost-col">20% Upon Sign-Off</td>
      </tr>
      <tr>
        <td><strong>Milestone 2: Chart Engine & Scalper</strong></td>
        <td>Month 2 – 3</td>
        <td>Delivery of `packages/chart` (CustomPainter 60fps canvas) and `packages/mscalper_train` (Scalper practice terminal with paper simulator).</td>
        <td class="cost-col">20% Upon Demo</td>
      </tr>
      <tr>
        <td><strong>Milestone 3: Backend OMS & Market Feed</strong></td>
        <td>Month 4 – 5</td>
        <td>Go WebSocket market tick server, Kafka streaming pipeline, PostgreSQL ledger, and real-time margin computation engine.</td>
        <td class="cost-col">20% Upon UAT</td>
      </tr>
      <tr>
        <td><strong>Milestone 4: 14-Step KYC & Fintech APIs</strong></td>
        <td>Month 6</td>
        <td>Digio (DigiLocker/e-Sign), HyperVerge (3D Liveness), NSDL PAN lookup, penny drop bank verification, and direct UPI intent payment integration.</td>
        <td class="cost-col">15% Upon Integration</td>
      </tr>
      <tr>
        <td><strong>Milestone 5: Kyro AI & 18 Indicators</strong></td>
        <td>Month 7 – 8</td>
        <td>Natural language indicator generator, SahiScript evaluator, Lorentzian Classification & Nadaraya-Watson indicator suite.</td>
        <td class="cost-col">15% Upon Demo</td>
      </tr>
      <tr>
        <td><strong>Milestone 6: Security Audit & Store Launch</strong></td>
        <td>Month 9 – 10</td>
        <td>CERT-In VAPT audit remediation, Google Play Store financial app clearance, Apple App Store approval, and production go-live.</td>
        <td class="cost-col">10% Final Sign-Off</td>
      </tr>
    </tbody>
  </table>

  <h2>Executive Project Sign-Off & Authorization</h2>
  <p>This master proposal constitutes the complete structural and commercial blueprint for engineering the Sahi-Style High-Performance Trading Platform. Both parties confirm alignment on project objectives upon execution:</p>

  <div class="signature-grid">
    <div>
      <div style="font-weight: 700; color: #0f172a; margin-bottom: 4px;">For the Development & Engineering Partner</div>
      <div style="font-size: 8.5pt; color: #64748b;">Technical Solutions & Delivery Lead</div>
      <div class="sign-line">Authorized Signatory & Date</div>
    </div>
    <div>
      <div style="font-weight: 700; color: #0f172a; margin-bottom: 4px;">For the Client / Project Sponsor</div>
      <div style="font-size: 8.5pt; color: #64748b;">Managing Director / Authorized Representative</div>
      <div class="sign-line">Authorized Signatory & Date</div>
    </div>
  </div>
</div>

</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[+] Wrote HTML template to: {HTML_PATH}")

# Convert HTML to PDF using Chrome Headless
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={PDF_PATH}",
    HTML_PATH
]

print("[+] Rendering PDF with Chrome Headless...")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0 and os.path.exists(PDF_PATH):
    size_kb = round(os.path.getsize(PDF_PATH) / 1024, 1)
    print(f"[+] Successfully generated master PDF: {PDF_PATH} ({size_kb} KB)")
    
    # Also copy to analysis directory
    import shutil
    shutil.copy2(PDF_PATH, PDF_ANALYSIS_PATH)
    print(f"[+] Mirrored PDF to analysis folder: {PDF_ANALYSIS_PATH}")
else:
    print(f"[-] Error generating PDF. Return code: {res.returncode}")
    print("Stderr:", res.stderr)
