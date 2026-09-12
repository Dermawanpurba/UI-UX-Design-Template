# UI/UX Design Catalog & Single-File index.html Prompt Studio

Platform mandiri (*standalone single-file*) untuk eksplorasi **60 Gaya Desain UI/UX Modern**, ekstraksi kebutuhan klien dengan **Template Kuesioner Standar 10 Dimensi**, serta generator **Master 1-Shot Single `index.html` Implementation Prompt**.

---

## 🎯 Fokus Utama: 1 Berkas Utuh `index.html`

Studio ini dirancang untuk menghasilkan prompt yang memerintahkan AI menyusun **1 berkas tunggal `index.html`** mandiri (bukan 9 PRD markdown terpisah) yang siap langsung dijalankan di browser:
- Struktur HTML5, CSS Styling, dan Logika JS murni dalam 1 file.
- Tanpa dependensi bundler atau build step (Zero Build Step).
- Mengintegrasikan 10 dimensi kebutuhan klien: logika bisnis, rumus kalkulasi manual, validasi, manajemen data lokal (*localStorage*), dan modal cetak resmi (*print-ready*).

---

## 🚀 Fitur Unggulan

1. **Katalog 60 Gaya Desain UI/UX Modern**:
   - Visual preview kartu artisan dengan generator SVG dinamis.
   - Filter 6 kategori: *Modern, Glass & Blur, Minimal, Bold & Vibrant, Neon & Futuristic, Classic & Retro*.
   - Pencarian cerdas dan instan berdasarkan nama dan deskripsi gaya.
   - Fitur Simpan Favorit dan Riwayat Akses tersimpan di `localStorage`.
   - Fitur Komparasi Dua Gaya Desain berdampingan.

2. **Template Kuesioner Standar 10 Dimensi (Anti-Slop)**:
   - Terstruktur dalam 10 Dimensi: Identitas & Domain, Persona & Pain Points, First 5-Minute Action, Modul & Lifecycle, Rumus Manual & Validasi Khusus, Entitas Data, Matriks RBAC, Format Cetak Resmi SPK/PO, Gaya UI/UX, dan Infrastruktur.
   - **4 Preset 1-Click Load**:
     - *Preset 1*: CMMS Alat Berat & Fleet Maintenance (PT Surya Saga Utama)
     - *Preset 2*: B2B E-Commerce & Sparepart Supply Chain
     - *Preset 3*: Corporate Showcase & Holding
     - *Preset 4*: HRIS, Absensi Roster & Payroll
   - **Tombol Salin Kuesioner**: Sekali klik untuk menyalin seluruh format pertanyaan ke clipboard untuk dikirim ke klien (WhatsApp/Email).

3. **Multi-Tab Output Prompt**:
   - **Tab 1: Master 1-Shot `index.html` (Utama)**: Prompt komprehensif untuk langsung menghasilkan 1 file `index.html` lengkap siap pakai.
   - **Tab 2: Ringkasan Kuesioner (PRD Singkat)**: Rangkuman terstruktur hasil kuesioner sebagai dokumentasi pendamping.
   - **Tab 3: Arsitektur & Data Spec**: Rincian skema entitas data dan algoritma formula untuk referensi teknis.

---

## 📁 Struktur Berkas

```text
c:/xampp/htdocs/UI UX Design/
├── index.html                  # Aplikasi antarmuka utama mandiri (Pure HTML/CSS/JS)
├── TEMPLATE_PERTANYAAN_PRD.md  # Format kuesioner wawancara standar 10 dimensi
├── PROMPT_AI_GENERATOR.md      # Panduan master prompt 1-shot index.html
└── README.md                   # Dokumentasi proyek ini
```

---
*Dikembangkan dengan standar arsitektur Senior Software Engineer dan UI/UX Pro Max.*
