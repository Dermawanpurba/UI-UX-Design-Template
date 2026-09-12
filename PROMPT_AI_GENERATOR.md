# Master Prompt AI: 1-Shot Single-File index.html Application Generator
### (Ekstraksi Kuesioner 10 Dimensi & UI/UX Pro Max Anti-Slop Standard)

Dokumen ini berisi formula **Master Prompt AI 1-Shot** yang digunakan oleh studio antarmuka `UI UX Design`. Formula ini dirancang khusus untuk menghasilkan **1 berkas utuh `index.html` mandiri** (zero build step, no bundler) yang mengimplementasikan seluruh kebutuhan sistem, formula kalkulasi klien, validasi, manajemen data lokal (*reactive local state*), dan dokumen cetak resmi secara lengkap tanpa kode placeholder ("TODO").

---

## 🎯 TUJUAN UTAMA: 1 FILE `index.html` MANDIRI

Hasil eksekusi prompt ini ke AI (ChatGPT GPT-4o, Claude 3.7 Sonnet, Google Gemini, atau Antigravity) **BUKAN berupa 9 dokumen terpisah**, melainkan **1 single self-contained file `index.html`** yang langsung bisa dibuka dan dijalankan di browser manapun:
- **Struktur HTML5 Murni** di satu file.
- **CSS Styling** di dalam satu tag `<style>` di `<head>`.
- **Logika JavaScript & Manajemen State** di dalam satu tag `<script>` sebelum `</body>`.
- **Dependensi CDN Resmi**: Tailwind CSS CDN, FontAwesome 6 Free CDN, SweetAlert2 CDN, dan Google Fonts (`Outfit`, `Inter`, `JetBrains Mono`).
- **Zero Build Step**: Tidak memerlukan Vite, Webpack, Node.js runtime, atau framework bundler.

---

## 📋 FORMULA MASTER PROMPT 1-SHOT `index.html`

Salin teks di bawah ini ke ChatGPT, Claude 3.7 Sonnet, Google Gemini, atau Antigravity:

```text
You are an expert Principal Creative Front-End Developer, Software Architect, and Lead UI/UX Engineer.
Produce a single self-contained, production-ready `index.html` that completely implements the web application described below.

CRITICAL INSTRUCTIONS - 100% IN ONE FILE:
- Produce ONE SINGLE self-contained `index.html` file (zero build step, no framework bundler, no node_modules).
- All CSS styles must be in one `<style>` block inside `<head>`.
- All JavaScript logic and state management must be in one `<script>` block before `</body>`.
- Use official CDN libraries:
  * Tailwind CSS CDN (<script src="https://cdn.tailwindcss.com"></script>)
  * FontAwesome 6 Free CDN (<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">)
  * SweetAlert2 CDN (<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>)
  * Google Fonts: Outfit (Display Headings), Inter (UI controls & body), JetBrains Mono (Data tables, metrics & code)
- 100% complete executable code: NO placeholder comments ("// TODO", "// implement logic here"). Every function, modal, calculation, and component must be fully coded and functional.

======================================================================
1. IDENTITY, DOMAIN & TAXONOMY
======================================================================
- Application Name: [NAMA APLIKASI LENGKAP]
- Industry / Sector: [SEKTOR INDUSTRI & DOMAIN BISNIS]
- Taxonomy Category: [Website / Management WebApp / Transaction WebApp]
- Creative Engineering Archetype: [ARCHETYPE TERPILIH: Enterprise Dashboard / Transaction Store / Adaptive Studio / dll.]
- Core Executive Objective: [SASARAN UTAMA EKSEKUTIF]

======================================================================
2. SENSORY NARRATIVE & UI/UX PRO MAX DESIGN SYSTEM (ZERO AI SLOP)
======================================================================
- Selected Visual Style: [NAMA GAYA DESAIN DARI 60 KATALOG]
- Color Tokens: Primary [HEX 1], Secondary/Accent [HEX 2], Brand [BRAND COLORS]
- Base Canvas: Deep obsidian dark background (#07090E).
- Structural Surfaces: Cards and panels with #0D111A and #121826, bordered by 1px subtle lines (#1E293B) and gentle optical glow.
- 60-30-10 Color Rule: 60% base canvas, 30% structural surface, 10% high-impact accent CTA.
- ZERO AI SLOP LAWS:
  * NO generic AI purple/pink gradients. Use tailored corporate hues.
  * NO emojis as UI icons. Always use FontAwesome 6 SVGs (<i class="fa-solid fa-..."></i>).
  * NO unformatted raw numbers. Format currency ("Rp 1.500.000" / "$1,500.00") and integers with thousand separators.
  * NO dead ends: Include clean empty states with illustrations and "Tambah Data Baru" action when filters yield 0 records.
  * Mobile Safe Padding: Ensure layout uses 100dvh with `pb-28 md:pb-12` safe-area padding so bottom navigation bars never obscure buttons.

======================================================================
3. CLIENT REQUIREMENTS, BUSINESS LOGIC & DATA LIFECYCLE
======================================================================
- Target Personas & Users: [ROLE DAN PERSONA PENGGUNA]
- Core Pain Points Solved: [MASALAH OPERASIONAL NYATA YANG DISELESAIKAN]
- First 5-Minute Critical Action:
  [AKSI PERTAMA YANG WAJIB BISA DILAKUKAN PENGGUNA SAAT MEMBUKA APLIKASI]
- Mandatory Modules (Phase 1): [DAFTAR MODUL UTAMA]
- Lifecycle Status Flow: [CONTOH: DRAFT -> SUBMITTED -> APPROVED -> IN_PROGRESS -> COMPLETED]
- Client Manual Calculations, Formulas & Validations (MUST BE CODED 100%):
[CATATAN MANUAL KLIEN, RUMUS PERHITUNGAN, ATURAN OTORISASI, FORMAT KODE UNIK]
- Data Entities Managed in Reactive Local State: [TABEL DATA DAN ATRIBUT]
- Target Deployment Spec: Standalone Single-File index.html

======================================================================
4. MANDATORY INTERACTIVE FEATURES IN THE SINGLE INDEX.HTML:
======================================================================
1. Top Navigation / Sidebar Shell:
   - Official brand logo badge with gradient icon.
   - Application title, active module indicator, and responsive navigation links.
   - Interactive Role Switcher dropdown with immediate simulated view filtering.
   - Real-time live digital clock chip (WIB / UTC) ticking every second.

2. Executive KPI Metrics Cards:
   - 4 prominent KPI metric cards displaying realistic numbers.
   - Trend percentage badges (+12.4% / -3.8%) and SVG status indicators.

3. Master Data Interactive Table:
   - Real-time instant search input filtering by multiple columns.
   - Quick category / status filter dropdown.
   - Table rows with status badges, human-readable formatted timestamps, formatted numeric values, and action buttons ("Detail", "Edit", "Cetak").
   - Responsive table wrapper with sticky header and pagination controls (Prev, Next, Page Numbers).

4. Reactive Local State Management:
   - Pure Vanilla JS reactive state persisted in `localStorage` so added or edited data is remembered across page refreshes.
   - Pre-populate with 6-8 realistic initial records reflecting the domain.

5. Quick Action Modal / Drawer (Form Input & Automated Calculation):
   - Triggered by "+ Tambah Transaksi / Data Baru" button.
   - Interactive form inputs with client-side validation.
   - Automated real-time calculation fields applying client formula.
   - Form submission validates required fields, updates local state, re-renders the table, and displays a SweetAlert2 success notification!

6. Official Print-Ready Modal (Simulated Official Company Document):
   - Clicking "Cetak Dokumen" on any row opens a high-fidelity modal simulating the official company document (SPK / PO / Surat Jalan / Invoice).
   - Includes official company header (kop surat), dynamic registration number, QR Code verification stamp, date, itemized table, and signature blocks.
   - Styled with `@media print` rules so printing via browser (Ctrl+P) produces clean, professional letterhead paper output.

Produce the entire application completely inside a single ```html ... ``` code block. Do NOT truncate or omit any section.
```

---
*Dokumen ini merupakan panduan resmi arsitektur UI/UX Design Catalog & Single-File index.html Prompt Studio.*
