# Master Prompt AI: Enterprise PRD JSON Generator (Untuk ChatGPT, Gemini, & Claude)

Salin seluruh teks prompt di dalam kotak di bawah ini, lalu buka **ChatGPT (GPT-4o)**, **Google Gemini**, atau **Claude**. 

Cukup ganti bagian `[TULISKAN IDE / KONSEP APLIKASI ANDA DI SINI]` dengan ide aplikasi yang Anda inginkan (misalnya: *"Sistem Absensi & Payroll Pabrik"*, *"Sistem Rental Mobil & Tracking GPS"*, atau *"Sistem Klinik & Rekam Medis"*).

AI akan langsung menyusun seluruh spesifikasi 16 langkah dalam format JSON. Anda tinggal meng-copy hasil JSON tersebut dan menempelkannya (*paste*) atau mengunggahnya (*upload*) ke **Enterprise PRD Studio** untuk mengisi seluruh formulir secara instan!

---

```text
Anda adalah seorang Principal Enterprise Software Architect dan Requirements Engineer berskala korporat.
Tugas Anda adalah merancang spesifikasi sistem aplikasi perangkat lunak yang sangat komprehensif, terstruktur, dan siap implementasi berdasarkan ide produk berikut:

[TULISKAN IDE / KONSEP APLIKASI ANDA DI SINI, CONTOH:
"Sistem Manajemen Gudang & Logistik Spareparts Alat Berat Tambang (Warehouse & Inventory CMMS) untuk mengelola penerimaan barang, bin-location, stok minimum, integrasi purchase order, dan barcode scanning."]

Tolong buatkan seluruh spesifikasi requirement dalam satu format JSON yang valid, terstruktur, dan lengkap mengikuti skema di bawah ini.

PENTING - ATURAN OUTPUT:
1. Hanya keluarkan kode JSON yang VALID di dalam blok ```json ... ``` tanpa penjelasan pembuka/penutup di luar blok.
2. JANGAN menggunakan placeholder ("TODO", "dsb", "dll"). Tuliskan data realistis, istilah industri yang tepat, dan aturan bisnis yang mendalam.
3. Nilai "taxonomy.pillar" WAJIB memilih salah satu dari 5 pilar berikut:
   - "dashboard" (Untuk Dashboard ERP, Control Center, Operasional, Work Order, CRUD berdensitas tinggi)
   - "landing_page" (Untuk Landing Page Pemasaran, Lead Generation, Showcase Produk/Jasa)
   - "company_profile" (Untuk Company Profile Korporat, Portofolio Holding, ESG, Hubungan Investor)
   - "e_commerce" (Untuk E-Commerce, Marketplace, B2B Commodity Trading, Pemesanan & Checkout)
   - "blog_content" (Untuk Portal Berita, Artikel Riset, Blog Industri, Publikasi Editorial)

STRUKTUR JSON YANG WAJIB DIHASILKAN:
{
  "project": {
    "name": "Nama Lengkap Produk / Aplikasi",
    "industry": "Sektor Industri (Contoh: Heavy Industry, Logistics, Healthcare, Finance)",
    "department": "Departemen Utama Pengguna (Contoh: Warehouse, Operations, Engineering)",
    "targetOrg": "Target Organisasi / Pengguna Akhir (Contoh: Kontraktor Tambang Tier-1)",
    "description": "Deskripsi komprehensif mengenai fungsi, objektif, dan manfaat sistem.",
    "problem": "Masalah operasional nyata di lapangan yang ingin diselesaikan oleh sistem.",
    "objective": "Target kuantitatif & kualitatif bisnis yang ingin dicapai.",
    "scope": "Ruang lingkup yang WAJIB ada pada rilis ini (In-Scope).",
    "outOfScope": "Hal-hal yang TIDAK dikerjakan pada rilis ini (Out-of-Scope).",
    "successCriteria": "Metrik penentu keberhasilan sistem (Contoh: Stock accuracy 99.5%, zero stockout).",
    "additionalNotes": "Aturan operasional khusus, standar K3/ISO, atau SOP wajib perusahaan."
  },
  "taxonomy": {
    "pillar": "dashboard",
    "archetype": "Enterprise ERP / Control Center"
  },
  "roles": [
    {
      "id": "r1",
      "name": "Nama Role 1 (Contoh: Warehouse Manager)",
      "department": "Warehouse & Logistics",
      "type": "primary",
      "responsibility": "Tanggung jawab utama operasional role ini.",
      "persona": "Karakteristik & fokus utama persona ini saat memakai aplikasi."
    },
    {
      "id": "r2",
      "name": "Nama Role 2 (Contoh: Inventory Clerk)",
      "department": "Warehouse Operations",
      "type": "primary",
      "responsibility": "Mencatat penerimaan barang dan pemindahan bin location.",
      "persona": "Membutuhkan input data cepat dengan barcode scanner."
    },
    {
      "id": "r3",
      "name": "Nama Role 3 (Contoh: Maintenance Planner)",
      "department": "Plant Maintenance",
      "type": "secondary",
      "responsibility": "Mengajukan permintaan material cadang untuk jadwal servis.",
      "persona": "Membutuhkan informasi ketersediaan stok real-time."
    }
  ],
  "modules": [
    {
      "id": "m1",
      "name": "Nama Modul 1 (Contoh: Master Data Spareparts)",
      "code": "MOD-SPAREPARTS",
      "desc": "Pengelolaan katalog suku cadang, part number, bin rack, dan batas stok.",
      "features": [
        {
          "id": "f101",
          "name": "Part Number & Specification Registry",
          "code": "FEAT-101",
          "priority": "P1 High",
          "desc": "CRUD katalog part number dengan klasifikasi fast/slow moving.",
          "acceptance": "Sistem wajib memvalidasi part number unik dan auto-assign bin rack."
        },
        {
          "id": "f102",
          "name": "Min-Max Stock Threshold Alert",
          "code": "FEAT-102",
          "priority": "P1 High",
          "desc": "Kalkulasi batas safety stock dan notifikasi otomatis saat stok mendekati reorder point.",
          "acceptance": "Memunculkan alert visual saat stock_on_hand <= min_stock."
        }
      ]
    },
    {
      "id": "m2",
      "name": "Nama Modul 2 (Contoh: Inbound & Good Receipt)",
      "code": "MOD-INBOUND",
      "desc": "Proses penerimaan barang dari vendor, inspeksi kualitas, dan penempatan ke rak.",
      "features": [
        {
          "id": "f201",
          "name": "PO Verification & GRN Creation",
          "code": "FEAT-201",
          "priority": "P1 High",
          "desc": "Pencocokan Delivery Order vendor dengan Purchase Order dan penerbitan Good Receipt Note.",
          "acceptance": "GRN hanya dapat disubmit jika kuantitas tidak melebihi open PO quantity."
        }
      ]
    },
    {
      "id": "m3",
      "name": "Nama Modul 3 (Contoh: Material Requisition & Issue)",
      "code": "MOD-OUTBOUND",
      "desc": "Penerbitan material berdasarkan Work Order perawatan unit alat berat.",
      "features": [
        {
          "id": "f301",
          "name": "Work Order Material Picking",
          "code": "FEAT-301",
          "priority": "P1 High",
          "desc": "Pengambilan barang sesuai daftar reservasi Work Order dengan pemotongan stok otomatis.",
          "acceptance": "Stok gudang langsung terpotong begitu status picking diverifikasi."
        }
      ]
    }
  ],
  "workflows": [
    {
      "id": "wf1",
      "stepNo": 1,
      "name": "Penerimaan Barang di Dock",
      "actor": "Inventory Clerk",
      "status": "RECEIVED",
      "trigger": "Truk ekspedisi tiba membawa barang dari vendor",
      "input": "Surat Jalan Vendor & Salinan PO",
      "action": "Inspeksi fisik kemasan, hitung kuantitas, dan scan serial number",
      "decision": "Apakah jumlah dan spek sesuai PO?",
      "output": "Draft Good Receipt Note (GRN)"
    },
    {
      "id": "wf2",
      "stepNo": 2,
      "name": "Verifikasi QA & Putaway ke Rak",
      "actor": "Quality Inspector & Clerk",
      "status": "INSPECTED",
      "trigger": "Barang selesai dihitung di area staging",
      "input": "Draft GRN & Certificate of Conformity",
      "action": "Cek kualitas barang dan tempatkan barang pada bin rack yang ditentukan",
      "decision": "Lulus uji QC?",
      "output": "Konfirmasi Putaway & Update Bin Location"
    },
    {
      "id": "wf3",
      "stepNo": 3,
      "name": "Approval & Rilis Stok Gudang",
      "actor": "Warehouse Manager",
      "status": "RELEASED",
      "trigger": "Barang sudah berada di rak penyimpanan",
      "input": "Laporan hasil inspeksi dan putaway",
      "action": "Tinjau dan tandatangani rilis GRN secara digital",
      "decision": "Setujui rilis stok?",
      "output": "Stok resmi bertambah di On-Hand Inventory"
    }
  ],
  "businessRules": [
    {
      "id": "br1",
      "code": "BR-INV-01",
      "name": "Larangan Negatif Inventory Balance",
      "category": "Data Integrity",
      "level": "Hard Constraint",
      "ruleStatement": "Kuantitas stok barang pada suatu bin location tidak boleh kurang dari 0 (nol) dalam kondisi transaksi apa pun.",
      "failAction": "Tolak transaksi pengeluaran material dan tampilkan pesan 'Stok tidak mencukupi'."
    },
    {
      "id": "br2",
      "code": "BR-INV-02",
      "name": "Validasi Approval Selisih Stock Opname",
      "category": "Security & Governance",
      "level": "Hard Constraint",
      "ruleStatement": "Setiap penyesuaian selisih stok di atas nilai Rp 5.000.000 wajib mendapatkan otorisasi ganda dari Warehouse Manager dan Plant Superintendent.",
      "failAction": "Kunci status adjusment sebagai PENDING_HIGH_LEVEL_APPROVAL."
    }
  ],
  "entities": [
    {
      "id": "e1",
      "name": "SparepartItem",
      "code": "tbl_spareparts",
      "desc": "Data master suku cadang dan posisi penyimpanan.",
      "fields": [
        { "name": "id", "type": "VARCHAR(36)", "required": true, "desc": "Primary Key UUID" },
        { "name": "part_number", "type": "VARCHAR(40)", "required": true, "desc": "Nomor part manufaktur unik" },
        { "name": "item_name", "type": "VARCHAR(120)", "required": true, "desc": "Nama deskriptif komponen" },
        { "name": "bin_location", "type": "VARCHAR(20)", "required": true, "desc": "Kode rak penyimpanan (misal: RAK-A3-02)" },
        { "name": "stock_on_hand", "type": "INTEGER", "required": true, "desc": "Jumlah stok fisik tersedia saat ini" },
        { "name": "min_stock", "type": "INTEGER", "required": true, "desc": "Batas ambang minimum reorder" },
        { "name": "unit_price", "type": "DECIMAL(15,2)", "required": true, "desc": "Harga perolehan rata-rata" }
      ]
    },
    {
      "id": "e2",
      "name": "GoodReceiptNote",
      "code": "tbl_good_receipts",
      "desc": "Catatan transaksi penerimaan material dari vendor.",
      "fields": [
        { "name": "id", "type": "VARCHAR(36)", "required": true, "desc": "Primary Key UUID" },
        { "name": "grn_number", "type": "VARCHAR(30)", "required": true, "desc": "Nomor urut GRN resmi" },
        { "name": "po_reference", "type": "VARCHAR(30)", "required": true, "desc": "Nomor Purchase Order acuan" },
        { "name": "vendor_name", "type": "VARCHAR(100)", "required": true, "desc": "Nama pemasok barang" },
        { "name": "received_date", "type": "DATE", "required": true, "desc": "Tanggal barang diterima di gudang" },
        { "name": "status", "type": "VARCHAR(20)", "required": true, "desc": "Status GRN (DRAFT/INSPECTED/APPROVED)" }
      ]
    }
  ],
  "permissions": {
    "Warehouse Manager_Master Data Spareparts": { "view": true, "create": true, "edit": true, "delete": true, "approve": true, "export": true },
    "Inventory Clerk_Master Data Spareparts": { "view": true, "create": true, "edit": true, "delete": false, "approve": false, "export": true },
    "Maintenance Planner_Master Data Spareparts": { "view": true, "create": false, "edit": false, "delete": false, "approve": false, "export": true },
    "Warehouse Manager_Inbound & Good Receipt": { "view": true, "create": true, "edit": true, "delete": true, "approve": true, "export": true },
    "Inventory Clerk_Inbound & Good Receipt": { "view": true, "create": true, "edit": true, "delete": false, "approve": false, "export": true }
  },
  "kpis": [
    {
      "id": "k1",
      "name": "Inventory Record Accuracy (IRA)",
      "code": "KPI-IRA",
      "target": ">= 99.0%",
      "formula": "(Jumlah Item Cocok Fisik & Sistem / Total Item Dihitung) * 100",
      "source": "tbl_stock_opname",
      "frequency": "Monthly"
    },
    {
      "id": "k2",
      "name": "Stockout Rate Critical Spareparts",
      "code": "KPI-STOCKOUT",
      "target": "< 0.5%",
      "formula": "(Permintaan Tertunda Karena Stok Habis / Total Permintaan) * 100",
      "source": "tbl_material_requisitions",
      "frequency": "Weekly"
    }
  ],
  "notifications": [
    {
      "id": "n1",
      "event": "Stock Drops Below Minimum (Reorder Point)",
      "channel": "In-App Banner & Email",
      "recipient": "Warehouse Manager & Procurement Officer",
      "priority": "P1 Critical",
      "escalation": "Jika tidak diterbitkan PR dalam 24 jam, eskalasi ke Superintendent",
      "messageTemplate": "[PERINGATAN STOK MINIMUM] Part Number {part_number} tersisa {stock_on_hand} unit (Batas min: {min_stock}). Segera lakukan Reorder."
    }
  ],
  "integrations": [
    {
      "id": "i1",
      "systemName": "SAP S/4HANA ERP (Materials Management)",
      "direction": "Bi-directional",
      "frequency": "Real-time Webhook / REST",
      "purpose": "Sinkronisasi Purchase Order dari pusat dan pengiriman data Good Receipt aktual.",
      "dataPayload": "PO_Header, MaterialDocument_Item, VendorMaster",
      "protocolAuth": "REST API OAuth 2.0 Bearer Token",
      "offlineSimulation": "Menyimpan mock array PO di browser localStorage dan simulasi konfirmasi pengiriman 200 OK."
    }
  ],
  "uiux": {
    "themeId": 2,
    "themeName": "Bento UI",
    "layout": "sidebar_topbar",
    "navigation": "sidebar",
    "accessibility": "wcag_aa",
    "screens": [
      {
        "id": "s1",
        "name": "Executive Warehouse Dashboard",
        "features": "Stat Cards Total SKU, Critical Low Stock Alert, Recent Inbound/Outbound Activity Feed",
        "components": "4 Stat Cards, Bento Grid Layout, Quick Action Buttons"
      },
      {
        "id": "s2",
        "name": "Spareparts Inventory Catalog Table",
        "features": "Filter Multi-Kriteria (Kategori, Bin Rack, Status Stok), Search Part Number, Modal Form Tambah Item",
        "components": "High-Density Data Table, Filter Bar, Pagination, Status Badges"
      },
      {
        "id": "s3",
        "name": "Good Receipt Entry & QC Modal",
        "features": "Form Verifikasi PO, Input Jumlah Aktual, Barcode Scan Simulator, Upload Bukti Surat Jalan",
        "components": "Multi-Step Form Modal, Auto-Calculation Difference, Confirmation Toast"
      }
    ]
  },
  "technicalMVP": {
    "frontend": "HTML5",
    "styling": "Vanilla CSS / Tailwind CDN Tokens",
    "logic": "Vanilla JavaScript ES6+",
    "storage": "localStorage & Reactive Mock Arrays",
    "backend": "None (Pure Client-Side State)",
    "database": "None (In-Memory JSON Collection)",
    "auth": "Mock Role Switcher (Client-side Session)",
    "deployment": "Standalone Single-File index.html"
  }
}
```
