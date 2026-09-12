# MASTER TEMPLATE KUESIONER STANDAR: EKSTRAKSI KEBUTUHAN PRODUK (PRD)
### Standar Rekayasa Perangkat Lunak Produksi & Anti-AI Slop (10 Dimensi Inti)

Dokumen ini adalah format kuesioner wawancara standar yang dirancang untuk menggali seluruh detail esensial dari klien, stakeholder, atau pemilik produk. Hasil dari pengisian kuesioner ini akan diolah oleh AI Studio untuk menghasilkan **Product Requirements Document (PRD) Terbaik (Standar 9 Dokumen Produksi)** dan **Frontend 1-Shot Implementation Prompt**.

---

## 📋 INSTRUKSI PENGGUNAAN
1. Kirimkan daftar pertanyaan di bawah ini kepada klien melalui WhatsApp, Email, atau gunakan saat sesi wawancara produk tatap muka.
2. Pastikan klien menjawab secara konkret dengan menyebutkan istilah bisnis nyata, alur operasional, nama entitas, dan contoh format.
3. Masukkan hasil jawaban ke dalam **UI/UX Design & PRD Prompt Studio** untuk menghasilkan Master AI Prompt 1-Shot yang siap dieksekusi.

---

## 🧩 10 DIMENSI PERTANYAAN STANDAR

### DIMENSI 1: IDENTITAS, INDUSTRI & SASARAN PROYEK
- **Q1.1. Nama Resmi Proyek / Aplikasi:**  
  *Apa nama resmi atau nama kode sistem yang akan dibangun? (Contoh: PT. Surya Saga Utama - Fleet & Maintenance Management System)*
- **Q1.2. Sektor Industri & Domain Bisnis:**  
  *Di bidang industri apa sistem ini beroperasi? (Contoh: Pertambangan Nikel/Batubara, Logistik & Ekspedisi, Healthcare, Retail B2B, Finance)*
- **Q1.3. Departemen / Target Organisasi Pengguna:**  
  *Departemen atau tipe organisasi mana yang menjadi pemilik dan pengguna utama sistem? (Contoh: Departemen Plant Maintenance & Logistik Gudang Site)*
- **Q1.4. Sasaran Utama (Executive Objective):**  
  *Apa tujuan bisnis utama yang ingin dicapai setelah sistem ini digunakan? (Contoh: Mengeliminasi pencatatan breakdown unit berbasis kertas, mengurangi downtime alat hingga 35%, dan mengontrol inventory sparepart bernilai miliaran rupiah)*

---

### DIMENSI 2: TARGET PERSONA & FRUSTRASI OPERASIONAL (PAIN POINTS)
- **Q2.1. Daftar Persona Pengguna:**  
  *Sebutkan minimal 2–4 peran pengguna yang akan berinteraksi dengan sistem:*
  - **Persona 1 (Primary):** *(Contoh: Mekanik Lapangan / Leader Servis)*
  - **Persona 2 (Secondary):** *(Contoh: Planner Maintenance / Supervisor Gudang)*
  - **Persona 3 (Management):** *(Contoh: Project Manager / Direksi)*
  - **Persona 4 (Eksternal jika ada):** *(Contoh: Vendor Rekondisi / Klien Eksternal)*
- **Q2.2. Masalah Operasional Terbesar Saat Ini (Pain Points):**  
  *Apa kelemahan fatal cara kerja lama (manual / spreadsheet) yang menyebabkan kerugian waktu, biaya, atau data hilang? (Contoh: Riwayat servis alat tercecer di chat WhatsApp, stok sparepart fisik di rak gudang tidak cocok dengan pembukuan, SPK perbaikan sering terlambat ditandatangani sehingga unit menganggur)*

---

### DIMENSI 3: AKSI PERTAMA PENGGUNA (FIRST 5-MINUTE CRITICAL EXPERIENCE)
- **Q3.1. Hal Pertama yang Wajib Dilihat / Dilakukan Pengguna:**  
  *Saat pengguna pertama kali login dan membuka layar dashboard dalam 5 menit pertama, aksi konkret apa yang paling mendesak yang harus bisa langsung mereka lakukan? (Contoh: Melihat papan status kesiapan armada unit (Ready For Use vs Breakdown), mengklik unit yang rusak, dan langsung menerbitkan Laporan Kerusakan P2H / Work Order perbaikan tanpa melalui menu bertingkat yang membingungkan)*

---

### DIMENSI 4: MODUL UTAMA & ALUR STATUS (LIFECYCLE WORKFLOW)
- **Q4.1. 3–5 Modul Operasional Mutlak (Fase 1):**  
  *Sebutkan modul apa saja yang WAJIB selesai pada rilis pertama:*
  - **Modul 1:** *(Contoh: Master Data Unit Alat Berat & Komponen HM/KM)*
  - **Modul 2:** *(Contoh: P2H Checklist Inspeksi Harian Operator & Mekanik)*
  - **Modul 3:** *(Contoh: Work Order Lifecycle & Penjadwalan Servis Berkala)*
  - **Modul 4:** *(Contoh: Manajemen Stok Sparepart Gudang & Minimum Reorder Alert)*
  - **Modul 5:** *(Contoh: Laporan Kinerja KPI Armada & Monitoring Downtime MTBF/MTTR)*
- **Q4.2. Tahapan Status Dokumen / Transaksi (Status Flow):**  
  *Bagaimana alur perubahan status dari awal hingga selesai? (Contoh: `DRAFT` ➔ `SUBMITTED` ➔ `APPROVED_BY_SUPERVISOR` ➔ `IN_PROGRESS` ➔ `WAITING_PARTS` ➔ `COMPLETED` ➔ `CLOSED_ARCHIVED`)*

---

### DIMENSI 5: LOGIKA BISNIS KHUSUS, VALIDASI & RUMUS MANUAL KLIEN
- **Q5.1. Formula Kalkulasi / Perhitungan Khusus:**  
  *Apakah ada rumus matematika, perhitungan biaya, atau persentase tertentu yang wajib diterapkan? (Contoh: Rumus MTBF = Total Jam Operasi / Jumlah Breakdown; Rumus Konsumsi Solar = Liter Terpakai / Selisih HM)*
- **Q5.2. Format Kode / Nomor Registrasi Otomatis:**  
  *Apakah ada format penomoran dokumen resmi? (Contoh: Format SPK: `SPK/SSU/{DEPT}/{YYYY}/{ROMAN_MONTH}/{AUTO_INC_4DIGIT}`)*
- **Q5.3. Aturan Validasi Khusus & Otorisasi:**  
  *Apa batasan yang tidak boleh dilanggar sistem? (Contoh: Mekanik tidak boleh menutup Work Order sebelum memasukkan nomor part bekas yang diganti; Pengeluaran sparepart di atas Rp 10.000.000 wajib persetujuan level Site Manager)*

---

### DIMENSI 6: ENTITAS DATA & MASTER DATA RELASIONAL
- **Q6.1. Daftar Tabel / Entitas Utama:**  
  *Data apa saja yang akan disimpan di dalam database? (Contoh: Users, Equipment, Inspections, WorkOrders, Spareparts, InventoryTransactions, MaintenanceLogs)*
- **Q6.2. Atribut Kunci & Relasi:**  
  *Sebutkan hubungan penting antar data (Contoh: 1 Unit Equipment memiliki banyak Work Orders; 1 Work Order membutuhkan banyak Spareparts dengan kolom kuantitas dan harga satuan)*

---

### DIMENSI 7: PERAN & HAK AKSES (RBAC MATRIX)
- **Q7.1. Pembagian Wewenang Hak Akses:**  
  *Jelaskan apa yang boleh dan tidak boleh dilakukan oleh masing-masing peran:*
  - **Superadmin:** *Akses penuh konfigurasi sistem, audit log, backup database.*
  - **Supervisor / Manager:** *Approve work order, melihat laporan eksekutif & finansial, override status.*
  - **Operator / Mekanik Lapangan:** *Hanya input inspeksi P2H, update progres pekerjaan, foto bukti unit.*
  - **Staff Gudang:** *Input penerimaan barang (GRN), reservasi suku cadang, update stok fisik rak.*

---

### DIMENSI 8: FORMAT CETAK RESMI (PRINT-READY) & EKSPOR
- **Q8.1. Dokumen Resmi yang Wajib Bisa Dicetak Langsung:**  
  *Dokumen apa yang membutuhkan tombol cetak dengan kop surat resmi perusahaan, QR Code validasi, dan kolom tanda tangan? (Contoh: Surat Perintah Kerja (SPK), Berita Acara Kerusakan, Bukti Pengeluaran Barang Gudang, Invoice Tagihan)*
- **Q8.2. Format Ekspor Data:**  
  *Kebutuhan ekspor data ke format apa saja? (Contoh: Laporan Bulanan ke PDF resmi & Rekapitulasi Data Mentah ke Excel/CSV)*

---

### DIMENSI 9: PREFERENSI DESAIN UI/UX & GAYA VISUAL
- **Q9.1. Gaya Desain Visual Terpilih (dari 60 Katalog Gaya):**  
  *(Pilih salah satu: Bento UI, Enterprise Dashboard Pro, Dark Mode Pro, Glassmorphism, Swiss Minimalist, Neobrutalism, Cyberpunk, dll.)*
- **Q9.2. Palet Warna Brand Perusahaan:**  
  *Warna identitas apa yang harus dominan? (Contoh: Deep Industrial Slate `#0F172A`, Safety Amber `#F59E0B`, dan Electric Blue `#3B82F6`)*
- **Q9.3. Karakteristik Tata Letak:**  
  *(Contoh: Sidebar kiri 240px yang dapat dilipat, tata letak 100dvh anti-slop dengan padding bawah aman untuk mobile navigation `pb-28 md:pb-12`, kartu metrik berdensitas tinggi, dan tabel master dengan filter cepat)*

---

### DIMENSI 10: FORMAT ARSITEKTUR & EKSEKUSI (1 FILE .HTML MANDIRI)
- **Q10.1. Format Pengiriman & Arsitektur:**  
  *1 File .html Mandiri (HTML5, CSS dalam `<style>`, dan JavaScript dalam `<script>` tergabung dalam 1 file .html utuh tanpa build step / framework bundler).*
- **Q10.2. Runtime Pustaka Eksternal:**  
  *CDN Resmi (Tailwind CSS CDN, FontAwesome 6 Free CDN, SweetAlert2 CDN, Google Fonts Outfit + Inter + JetBrains Mono).*
- **Q10.3. Lingkungan Eksekusi:**  
  *Dapat dibuka langsung di browser lokal (double-click file) atau disajikan via Apache XAMPP / static web server.*

---

## ⚡ CONTOH PRESET SIAP PAKAI (QUICK PRESET SAMPLES)

### PRESET A: Heavy Industry CMMS & Fleet Maintenance
- **Nama:** PT. Surya Saga Utama - Fleet & Heavy Equipment CMMS
- **Industri:** Pertambangan Nikel Site Morowali
- **Persona:** Plant Manager, Chief Mechanic, Site Warehouse Operator
- **Pain Point:** Downtime excavator tidak terpantau, overstock sparepart lambat, mekanik kesulitan cari manual book.
- **First 5-Min:** Melihat armada siaga vs breakdown di peta site, lalu membuat Work Order perbaikan.
- **Must-Have:** P2H Digital, Work Order Tracker, Minimum Stock Alert, Cetak SPK Resmi PT SSU.
- **Logika:** Alert otomatis jika HM mencapai 250 jam untuk servis berkala; Format SPK: `SPK-SSU/{YYYY}/{ROMAN}/{INC4}`.

### PRESET B: B2B E-Commerce & Sparepart Supply Chain
- **Nama:** MinePart Pro - B2B Heavy Equipment Spareparts Hub
- **Industri:** Supply Chain & E-Commerce Alat Berat
- **Persona:** Procurement Officer Kontraktor, Sales Distributor Resmi
- **Pain Point:** Harga suku cadang tidak transparan, verifikasi part number manual rentan salah kirim part.
- **First 5-Min:** Pencarian part number dengan auto-suggest kompatibilitas unit dan ketersediaan stok instan.
- **Must-Have:** Smart Search Part Number, Cart Drawer, Request Quotation (RFQ), Invoice Resmi Cetak.
- **Logika:** Diskon tier kuantitas (>= 10 pcs diskon 12%); Verifikasi nomor faktur pajak otomatis.

---
*Dokumen ini merupakan bagian dari standar arsitektur UI/UX Design & Flexible PRD Architect.*
