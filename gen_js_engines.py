# -*- coding: utf-8 -*-
"""JS generator."""

def get_js_engines():
    return r"""
// ============================================================================
// ENTERPRISE PRD STUDIO - CORE REACTIVE ENGINES
// ============================================================================

// Helper for HTML escaping
function escapeHtml(str) {
    if (!str && str !== 0) return '';
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}

// 5 ARCHITECTURE PILLARS DEFINITION
const ARCHITECTURE_PILLARS = [
    {
        key: 'dashboard',
        name: 'Dashboard ERP & Control Center',
        badge: 'Enterprise Core',
        badgeClass: 'badge-indigo',
        icon: 'fa-chart-pie',
        iconColor: '#818CF8',
        iconBg: 'rgba(99, 102, 241, 0.15)',
        tagline: 'Operasional, Work Order, Master Data CRUD, Pemeliharaan, dan Metrik Analitik Terpusat.',
        description: 'Arsitektur berbasis tabel data berdensitas tinggi, modal form CRUD reaktif, filter multi-kriteria, kontrol hak akses (RBAC), alur persetujuan (approval workflows), serta kartu KPI status operasional.',
        archetype: 'Enterprise ERP / Control Center',
        recommendedModules: ['Master Data CRUD', 'Workflow Approval', 'Audit Trail', 'Filter & Export', 'KPI Widgets']
    },
    {
        key: 'landing_page',
        name: 'Landing Page & Pemasaran',
        badge: 'High Conversion',
        badgeClass: 'badge-amber',
        icon: 'fa-rocket',
        iconColor: '#F59E0B',
        iconBg: 'rgba(245, 158, 11, 0.15)',
        tagline: 'Lead Generation, Konversi Klien, Showroom Penawaran, dan Kampanye Produk.',
        description: 'Arsitektur berorientasi konversi tinggi dengan section hero dinamis, value proposition, grid fitur/keunggulan, kalkulator ROI, testimoni terpercaya, FAQ interaktif, dan formulir pendaftaran lead terintegrasi.',
        archetype: 'Conversion Landing Page',
        recommendedModules: ['Hero Section', 'Feature Grid', 'Social Proof', 'Lead Capture Form', 'Pricing Calculator']
    },
    {
        key: 'company_profile',
        name: 'Company Profile Korporat',
        badge: 'Corporate Identity',
        badgeClass: 'badge-cyan',
        icon: 'fa-building-columns',
        iconColor: '#38BDF8',
        iconBg: 'rgba(56, 189, 248, 0.15)',
        tagline: 'Identitas Korporasi, Legalitas & Tata Kelola, Portofolio Proyek, dan Hubungan Investor.',
        description: 'Arsitektur formal representasi holding/korporasi yang menyajikan profil kepemimpinan, sejarah perusahaan, sertifikasi standar mutu/K3, peta konsesi / jaringan kantor, dan formulir pengajuan kerjasama bisnis.',
        archetype: 'Corporate Holding Portal',
        recommendedModules: ['Corporate About', 'Leadership Bios', 'Project Showcase', 'ESG/Compliance', 'Contact Inquiry']
    },
    {
        key: 'e_commerce',
        name: 'E-Commerce & B2B Trading',
        badge: 'Transaction Engine',
        badgeClass: 'badge-emerald',
        icon: 'fa-cart-shopping',
        iconColor: '#10B981',
        iconBg: 'rgba(16, 185, 129, 0.15)',
        tagline: 'Katalog Produk / Komoditas, Keranjang Belanja, Transaksi, dan Checkout Terintegrasi.',
        description: 'Arsitektur e-commerce & marketplace transaksi dengan galeri katalog produk, filter spesifikasi dinamis, kuotasi harga multi-tier, keranjang belanja interaktif, tracking status pesanan, dan simulasi checkout.',
        archetype: 'B2B/B2C Commerce Engine',
        recommendedModules: ['Product Catalog', 'Search & Filter', 'Cart & Wishlist', 'Checkout Flow', 'Order Tracking']
    },
    {
        key: 'blog_content',
        name: 'Blog & Media Publikasi',
        badge: 'Content & Editorial',
        badgeClass: 'badge-rose',
        icon: 'fa-newspaper',
        iconColor: '#EC4899',
        iconBg: 'rgba(236, 72, 153, 0.15)',
        tagline: 'Publikasi Artikel, Berita Industri, Riset Pasar, dan Dokumentasi Pengetahuan.',
        description: 'Arsitektur editorial berbasis artikel dengan layout majalah/blog modern, kategorisasi konten mendalam, artikel pembaca (rich reader mode), tag pencarian, estimasi waktu baca, serta call-to-action buletin.',
        archetype: 'Editorial & Content Hub',
        recommendedModules: ['Article Grid', 'Category Filter', 'Reader View', 'Author Profiles', 'Newsletter Signup']
    }
];

function getPillarObj(key) {
    return ARCHITECTURE_PILLARS.find(p => p.key === key) || null;
}

function getPillarName(key) {
    const p = getPillarObj(key);
    return p ? p.name : '';
}

// 1. Centralized Single Source of Truth: Empty Workspace Template
function getEmptyProject() {
    return {
        project: {
            name: '',
            description: '',
            problem: '',
            objective: '',
            industry: '',
            department: '',
            targetOrg: '',
            scope: '',
            outOfScope: '',
            successCriteria: '',
            additionalNotes: ''
        },
        taxonomy: {
            pillar: '', // Default: not selected
            archetype: ''
        },
        users: [],
        roles: [],
        modules: [],
        features: [],
        workflows: [],
        businessRules: [],
        entities: [],
        permissions: {},
        kpis: [],
        notifications: [],
        integrations: [],
        uiux: {
            themeId: null,
            themeName: '',
            layout: 'sidebar_topbar',
            navigation: 'sidebar',
            accessibility: 'wcag_aa',
            screens: []
        },
        technicalMVP: {
            frontend: 'HTML5',
            styling: 'Vanilla CSS / Tailwind CDN Tokens',
            logic: 'Vanilla JavaScript ES6+',
            storage: 'localStorage & Reactive Mock Arrays',
            backend: 'None (Pure Client-Side State)',
            database: 'None (In-Memory JSON Collection)',
            auth: 'Mock Role Switcher (Client-side Session)',
            deployment: 'Standalone Single-File index.html'
        }
    };
}

let projectPRD = getEmptyProject();

let currentStep = 1;
let activeThemeCat = 'all';
let currentThemeQuery = '';

// ============================================================================
// INITIALIZATION & PRESETS
// ============================================================================
function initEnterprisePrdStudio() {
    loadProject(); // Load from localStorage if available
    initTaxonomyUI();
    initThemeCatalogUI();
    syncStep1Form();
    renderRoles();
    renderModulesAndFeatures();
    renderWorkflowNodes();
    renderBusinessRules();
    renderEntities();
    renderRbacMatrix();
    renderKpis();
    renderNotifications();
    renderIntegrations();
    renderScreens();
    updateUiMetadata();
    checkCompleteness();
    goToStep(1);
}

// Mining CMMS Preset Generator (Production Grade)
function loadMiningCmmsPreset() {
    projectPRD.project = {
        name: 'Mining Equipment CMMS & Fleet Maintenance',
        description: 'Pusat kendali pemeliharaan armada alat berat tambang (Excavator, Hauler, Dozer, Grader) untuk mengelola siklus hidup Work Order, inspeksi harian, penjadwalan PM, dan penugasan mekanik lapangan.',
        problem: 'Tingginya breakdown tak terencana (downtime armada mencapai 18.5%), pencatatan Work Order manual memicu hilangnya riwayat servis, serta minimnya integrasi alokasi suku cadang di gudang site.',
        objective: 'Menurunkan MTTR sebesar 30%, meningkatkan kepatuhan PM hingga >92%, mendigitalkan 100% penerbitan Work Order, dan mengeliminasi keterlambatan rilis unit ke pit front.',
        industry: 'Pertambangan Nikel & Batubara (Heavy Mining Industry)',
        department: 'Plant Maintenance, Reliability Engineering, Workshop',
        targetOrg: 'Kontraktor Tambang Tier-1 & Pemegang IUP Operasi Produksi',
        scope: 'Manajemen Work Order end-to-end, Preventive Maintenance (PM PS 250-2000 Jam), Registrasi Aset Alat Berat, Permintaan Suku Cadang Gudang, Penugasan Mekanik Lapangan, dan Dashboard Metrik MTTR/MTBF.',
        outOfScope: 'Penyusunan laporan keuangan buku besar (GL), penggajian payroll mekanik, dan tender pengadaan lelang unit alat berat baru skala besar.',
        successCriteria: 'Physical Availability (PA) armada mencapai >=90%, Mean Time To Repair (MTTR) < 2.5 jam, dan 100% Work Order terekam secara digital tanpa backlog tertunda.',
        additionalNotes: 'Setiap Work Order prioritas P0 (Breakdown Fatal) wajib memicu notifikasi darurat langsung ke Supervisor dan tidak boleh dirilis ke lapangan tanpa validasi ketersediaan mekanik lead.'
    };

    projectPRD.taxonomy.pillar = 'dashboard';
    projectPRD.taxonomy.subtypeId = 'db_cmms_maintenance';

    projectPRD.roles = [
        { id: 'r1', name: 'Maintenance Planner', department: 'Plant Planning', type: 'primary', responsibility: 'Menyusun job plan WO, mengalokasikan perkiraan manpower, dan reservasi suku cadang.', persona: 'Membutuhkan backlog visibility dan kemudahan penjadwalan PM mingguan.' },
        { id: 'r2', name: 'Maintenance Supervisor', department: 'Site Operations', type: 'primary', responsibility: 'Meninjau breakdown lapangan, menyetujui rilis WO, dan memvalidasi penyelesaian servis.', persona: 'Fokus pada ketersediaan unit (PA%) dan percepatan rilis alat berat ke pit.' },
        { id: 'r3', name: 'Field Mechanic Lead', department: 'Workshop & Pit Support', type: 'primary', responsibility: 'Mengeksekusi perbaikan unit, mencatat jam kerja mekanik, dan melaporkan temuan lapangan.', persona: 'Memerlukan antarmuka ringkas, checklist digital, dan form update status cepat.' },
        { id: 'r4', name: 'Reliability Engineer', department: 'Engineering', type: 'secondary', responsibility: 'Menganalisis akar masalah kerusakan (RCA), menghitung MTBF/MTTR, dan unit bad-actor.', persona: 'Mengandalkan visualisasi tren kegagalan komponen dan laporan riwayat breakdown.' },
        { id: 'r5', name: 'Warehouse Officer', department: 'Supply Chain', type: 'secondary', responsibility: 'Memverifikasi ketersediaan suku cadang dan menerbitkan barang (Material Issue).', persona: 'Membutuhkan referensi nomor WO yang valid sebelum mengeluarkan spare part kritis.' },
        { id: 'r6', name: 'Maintenance Manager', department: 'Executive Site Management', type: 'secondary', responsibility: 'Mengevaluasi performa bulanan, kepatuhan PM, serta mengotorisasi biaya overhaul besar.', persona: 'Memantau ringkasan KPI eksekutif dan anggaran belanja pemeliharaan.' }
    ];

    projectPRD.modules = [
        { id: 'm1', name: 'Work Order Management', description: 'Pencatatan, penjadwalan, penugasan, dan penutupan perintah kerja pemeliharaan.', submodules: 'WO Registry, WO Create & Triage, Execution Log, Quality Sign-off' },
        { id: 'm2', name: 'Preventive Maintenance (PM)', description: 'Otomatisasi jadwal servis berkala berdasarkan jam operasi alat (Hour Meter - HM).', submodules: 'PM Schedule Matrix, Service Checklist, Overdue Tracking' },
        { id: 'm3', name: 'Equipment Asset Register', description: 'Basis data master seluruh armada alat berat dan hierarki komponen kritis.', submodules: 'Asset Hierarchy, Telemetry Specs, Health Index' },
        { id: 'm4', name: 'Spare Parts & Material Request', description: 'Integrasi permintaan dan pengeluaran suku cadang untuk pemenuhan WO.', submodules: 'Material Requisition, Stock Checking, Parts Allocation' }
    ];

    projectPRD.features = [
        { id: 'f1', moduleId: 'm1', name: 'Multi-Criteria Work Order Filter', description: 'Memfilter daftar perintah kerja berdasarkan status (Open, Planned, In-Progress, Closed) dan prioritas.', priority: 'P0', primaryUser: 'Maintenance Planner', dependencies: 'Equipment Register', expectedOutcome: 'Daftar WO terfilter instan <100ms.' },
        { id: 'f2', moduleId: 'm1', name: 'Direct WO Creation & Assignment', description: 'Formulir pembuatan WO darurat dengan penugasan regu mekanik dan estimasi jam kerja.', priority: 'P0', primaryUser: 'Maintenance Supervisor', dependencies: 'Roles, Equipment Register', expectedOutcome: 'WO baru terbit dengan nomor unik tergenerasi.' },
        { id: 'f3', moduleId: 'm1', name: 'Interactive Work Order Status Transition', description: 'Simulasi alur perubahan status dari Planned &rarr; Released &rarr; Executing &rarr; Verified &rarr; Closed.', priority: 'P0', primaryUser: 'Field Mechanic Lead', dependencies: 'Business Rules', expectedOutcome: 'Status badge berubah seketika dan tercatat di timeline.' },
        { id: 'f4', moduleId: 'm2', name: 'PM Service Trigger by Hour Meter (HM)', description: 'Peringatan otomatis saat unit mendekati interval PS 250, 500, 1000, atau 2000 Jam.', priority: 'P0', primaryUser: 'Maintenance Planner', dependencies: 'Equipment Register', expectedOutcome: 'Penerbitan draft PM otomatis saat HM terpenuhi.' },
        { id: 'f5', moduleId: 'm2', name: 'Digital Inspection Checklist', description: 'Daftar periksa inspeksi kelaikan jalan (P2H) dengan opsi centang Pass/Fail dan upload temuan.', priority: 'P1', primaryUser: 'Field Mechanic Lead', dependencies: 'WO Management', expectedOutcome: 'Temuan fail otomatis memicu Corrective WO baru.' },
        { id: 'f6', moduleId: 'm3', name: 'Asset Equipment Master Hierarchy', description: 'Visualisasi induk armada, model unit, nomor lambung (Unit Code), dan lokasi pit front.', priority: 'P1', primaryUser: 'Reliability Engineer', dependencies: 'None', expectedOutcome: 'Profil aset detail dengan riwayat servis lengkap.' },
        { id: 'f7', moduleId: 'm4', name: 'Quick Spare Part Reservation for WO', description: 'Alokasi suku cadang kritis (filter, oli, hose, belt) terhubung langsung ke nomor Work Order.', priority: 'P1', primaryUser: 'Warehouse Officer', dependencies: 'WO Management', expectedOutcome: 'Saldo stok terpotong dan terdaftar di rincian WO.' }
    ];

    projectPRD.workflows = [
        { id: 'w1', stepNo: 1, name: 'Work Request Logged', trigger: 'Operator atau inspector mendeteksi kerusakan unit di lapangan', actor: 'Maintenance Supervisor', input: 'Nomor lambung unit, gejala kegagalan, lokasi pit', action: 'Mengisi form cepat laporan kerusakan di antarmuka lapangan', decision: 'Apakah breakdown bersifat darurat P0?', output: 'Notifikasi breakdown masuk ke papan kendali Planner', status: 'REQUESTED' },
        { id: 'w2', stepNo: 2, name: 'Review & Triage', trigger: 'Work Request baru muncul di antarmuka Planner', actor: 'Maintenance Planner', input: 'Data work request dan status ketersediaan unit cadangan', action: 'Memverifikasi tingkat keparahan dan mengklasifikasikan jenis pekerjaan (CM vs PM)', decision: 'Apakah perlu suku cadang mayor?', output: 'Kategori WO dan estimasi prioritas ditetapkan', status: 'TRIAGED' },
        { id: 'w3', stepNo: 3, name: 'Job Planning & Parts Reservation', trigger: 'WO terverifikasi pada tahap triage', actor: 'Maintenance Planner', input: 'Job standard template, estimasi jam perbaikan, kebutuhan suku cadang', action: 'Menetapkan standar prosedur instruksi kerja dan mereservasi part ke gudang', decision: 'Apakah part tersedia di rak gudang site?', output: 'Paket kerja lengkap dengan estimasi durasi pekerjaan', status: 'PLANNED' },
        { id: 'w4', stepNo: 4, name: 'Supervisor Approval', trigger: 'Paket perencanaan WO selesai disusun', actor: 'Maintenance Supervisor', input: 'Rincian alokasi biaya dan kebutuhan durasi downtime', action: 'Menyetujui rilis perintah kerja dan menjadwalkan jendela waktu perbaikan', decision: 'Disetujui untuk rilis perbaikan?', output: 'Otorisasi eksekusi WO terbit resmi', status: 'APPROVED' },
        { id: 'w5', stepNo: 5, name: 'Resource & Bay Scheduling', trigger: 'WO telah disetujui Supervisor', actor: 'Maintenance Planner', input: 'Ketersediaan bay workshop dan jadwal shift mekanik', action: 'Menetapkan regu mekanik pelaksana dan slot area perbaikan (Workshop Bay / Front Pit)', decision: 'Manpower mekanik memadai?', output: 'Jadwal eksekusi terkunci di kalender workshop', status: 'SCHEDULED' },
        { id: 'w6', stepNo: 6, name: 'Work Order Release', trigger: 'Jadwal shift mekanik dimulai', actor: 'Maintenance Supervisor', input: 'Kesiapan unit di lokasi perbaikan', action: 'Mengubah status WO menjadi Released dan menyerahkan perintah kerja ke Lead Mekanik', decision: 'Unit siap diservis?', output: 'Status WO berubah aktif untuk pengerjaan fisik', status: 'RELEASED' },
        { id: 'w7', stepNo: 7, name: 'Field Execution & Logging', trigger: 'Mekanik menerima perintah kerja', actor: 'Field Mechanic Lead', input: 'Suku cadang dari gudang dan instruksi teknis servis', action: 'Melakukan perbaikan fisik unit, mencatat jam kerja aktual, dan memasang spare part', decision: 'Apakah ditemukan kerusakan tambahan?', output: 'Log pengerjaan terisi dan unit selesai diperbaiki', status: 'IN_PROGRESS' },
        { id: 'w8', stepNo: 8, name: 'QC Verification & Sign-Off', trigger: 'Pekerjaan mekanik dilaporkan selesai', actor: 'Maintenance Supervisor', input: 'Laporan perbaikan fisik dan hasil uji fungsi alat berat (Test Run)', action: 'Memeriksa kelaikan teknis unit dan menandatangani verifikasi digital', decision: 'Apakah unit lolos standar uji kelaikan?', output: 'Pernyataan unit fit-to-work diterbitkan', status: 'VERIFIED' },
        { id: 'w9', stepNo: 9, name: 'Work Order Closed', trigger: 'Verifikasi kelaikan unit disetujui', actor: 'Maintenance Planner', input: 'Seluruh pencatatan jam kerja dan bukti pemakaian material', action: 'Menutup Work Order secara permanen dan memperbarui riwayat servis aset', decision: 'Semua administrasi lengkap?', output: 'Unit kembali beroperasi penuh di pit dan metrik MTTR diperbarui', status: 'CLOSED' }
    ];

    projectPRD.businessRules = [
        { id: 'br1', name: 'WO Cannot Release Without Assigned Manpower', description: 'Perintah kerja pemeliharaan dilarang keras berstatus Released apabila belum ada mekanik yang ditugaskan.', condition: 'Assigned Manpower == 0 OR Assigned Mechanics List is Empty', action: 'Kunci tombol rilis status dan tampilkan pesan validasi merah.', exception: 'Tidak ada pengecualian (Blocking Mutlak).', severity: 'Blocking' },
        { id: 'br2', name: 'Emergency P0 Breakdown Instant Dispatch', description: 'Work Order kerusakan tingkat fatal (P0) wajib langsung memicu sinyal dispatch darurat dan prioritas bay tertinggi.', condition: 'Priority == "P0" AND Status == "REQUESTED"', action: 'Beri penanda merah berkedip pada dashboard dan kirim alert notifikasi otomatis.', exception: 'Unit dalam status idle non-produksi.', severity: 'Blocking' },
        { id: 'br3', name: 'Material Requisition Requires Valid WO Number', description: 'Petugas gudang tidak diperbolehkan menerbitkan suku cadang tanpa mencantumkan nomor WO yang aktif.', condition: 'Material Request WO_Number is Empty OR Status == "CLOSED"', action: 'Tolak penerbitan barang (Reject Issue).', exception: 'Pengambilan konsumabel umum (baut standar / majun) di bawah nilai $50.', severity: 'Blocking' },
        { id: 'br4', name: 'Preventive Maintenance Overdue Escalation', description: 'Unit yang melebihi batas jadwal PM lebih dari 50 Jam Operasi (HM) wajib mendapat peringatan kuning.', condition: 'Current HM - Scheduled PM HM > 50', action: 'Tampilkan badge PM Overdue dan peringatan penurunan kondisi unit.', exception: 'Izin tertulis penundaan dari Maintenance Manager.', severity: 'Warning' },
        { id: 'br5', name: 'Work Order Closure Requires Completed Checklist', description: 'WO tidak dapat berstatus Closed jika rincian checklist perbaikan belum terisi lengkap.', condition: 'Checklist Items Incomplete > 0', action: 'Cegah aksi Close dan arahkan user melengkapi item inspeksi.', exception: 'WO dibatalkan resmi (Cancelled).', severity: 'Blocking' }
    ];

    projectPRD.entities = [
        {
            id: 'e1',
            name: 'Equipment',
            description: 'Master data unit armada alat berat operasional tambang.',
            type: 'Master',
            storage: 'tbl_equipments',
            fields: [
                { id: 'f101', name: 'id', type: 'String', required: 'true', defaultValue: 'UUID', validation: 'Primary Key', description: 'ID unik mesin' },
                { id: 'f102', name: 'unit_code', type: 'String', required: 'true', defaultValue: "''", validation: 'Unique, Min:4', description: 'Nomor lambung unit (e.g. EX-201, DT-705)' },
                { id: 'f103', name: 'category', type: 'Enum', required: 'true', defaultValue: "'Excavator'", validation: 'In: Excavator, Hauler, Dozer, Grader', description: 'Jenis alat berat' },
                { id: 'f104', name: 'current_hm', type: 'Decimal', required: 'true', defaultValue: '0.0', validation: 'Min:0', description: 'Hour Meter kumulatif saat ini' },
                { id: 'f105', name: 'status', type: 'Enum', required: 'true', defaultValue: "'OPERATIONAL'", validation: 'In: OPERATIONAL, BREAKDOWN, MAINTENANCE', description: 'Status kelaikan fisik' }
            ],
            relationships: [
                { targetEntity: 'WorkOrder', relationType: 'One-to-Many', foreignKey: 'equipment_id' }
            ]
        },
        {
            id: 'e2',
            name: 'WorkOrder',
            description: 'Transaksi perintah kerja pemeliharaan dan perbaikan aset.',
            type: 'Transactional',
            storage: 'tbl_work_orders',
            fields: [
                { id: 'f201', name: 'id', type: 'String', required: 'true', defaultValue: 'UUID', validation: 'Primary Key', description: 'ID unik internal' },
                { id: 'f202', name: 'wo_number', type: 'String', required: 'true', defaultValue: "''", validation: 'Unique, Regex:^WO-[0-9]{5}$', description: 'Nomor referensi resmi WO' },
                { id: 'f203', name: 'equipment_id', type: 'String', required: 'true', defaultValue: "''", validation: 'Foreign Key to Equipment', description: 'ID unit yang diperbaiki' },
                { id: 'f204', name: 'title', type: 'String', required: 'true', defaultValue: "''", validation: 'Min:5', description: 'Ringkasan deskripsi pekerjaan' },
                { id: 'f205', name: 'priority', type: 'Enum', required: 'true', defaultValue: "'P2'", validation: 'In: P0, P1, P2, P3', description: 'Tingkat kegentingan' },
                { id: 'f206', name: 'status', type: 'Enum', required: 'true', defaultValue: "'PLANNED'", validation: 'In: REQUESTED, PLANNED, APPROVED, IN_PROGRESS, CLOSED', description: 'Status tahap WO' },
                { id: 'f207', name: 'assigned_mechanic', type: 'String', required: 'false', defaultValue: "''", validation: 'Nullable', description: 'Nama mekanik penanggung jawab' },
                { id: 'f208', name: 'downtime_hours', type: 'Decimal', required: 'false', defaultValue: '0.0', validation: 'Min:0', description: 'Total durasi kerusakan (jam)' }
            ],
            relationships: [
                { targetEntity: 'Equipment', relationType: 'Many-to-One', foreignKey: 'equipment_id' },
                { targetEntity: 'WorkOrderPart', relationType: 'One-to-Many', foreignKey: 'work_order_id' }
            ]
        },
        {
            id: 'e3',
            name: 'SparePart',
            description: 'Katalog suku cadang dan saldo inventaris gudang site.',
            type: 'Master',
            storage: 'tbl_spare_parts',
            fields: [
                { id: 'f301', name: 'id', type: 'String', required: 'true', defaultValue: 'UUID', validation: 'Primary Key', description: 'ID internal suku cadang' },
                { id: 'f302', name: 'part_number', type: 'String', required: 'true', defaultValue: "''", validation: 'Unique', description: 'Nomor part OEM pabrikan' },
                { id: 'f303', name: 'name', type: 'String', required: 'true', defaultValue: "''", validation: 'Min:3', description: 'Nama komponen (e.g. Engine Oil Filter)' },
                { id: 'f304', name: 'stock_qty', type: 'Integer', required: 'true', defaultValue: '0', validation: 'Min:0', description: 'Jumlah saldo fisik saat ini' },
                { id: 'f305', name: 'min_stock', type: 'Integer', required: 'true', defaultValue: '5', validation: 'Min:1', description: 'Batas level pemesanan ulang (ROP)' }
            ],
            relationships: []
        },
        {
            id: 'e4',
            name: 'WorkOrderPart',
            description: 'Rincian alokasi suku cadang pada setiap perintah kerja.',
            type: 'Transactional',
            storage: 'tbl_wo_parts',
            fields: [
                { id: 'f401', name: 'id', type: 'String', required: 'true', defaultValue: 'UUID', validation: 'Primary Key', description: 'ID rincian part' },
                { id: 'f402', name: 'work_order_id', type: 'String', required: 'true', defaultValue: "''", validation: 'Foreign Key to WorkOrder', description: 'Tautan WO' },
                { id: 'f403', name: 'part_id', type: 'String', required: 'true', defaultValue: "''", validation: 'Foreign Key to SparePart', description: 'Tautan SparePart' },
                { id: 'f404', name: 'quantity_used', type: 'Integer', required: 'true', defaultValue: '1', validation: 'Min:1', description: 'Jumlah suku cadang dipasang' }
            ],
            relationships: [
                { targetEntity: 'WorkOrder', relationType: 'Many-to-One', foreignKey: 'work_order_id' }
            ]
        }
    ];

    projectPRD.kpis = [
        { id: 'k1', name: 'Mean Time To Repair (MTTR)', description: 'Rata-rata durasi penanganan perbaikan per kejadian breakdown unit.', formula: '(Total Downtime Hours / Jumlah Kasus Breakdown)', source: 'WorkOrder.downtime_hours', target: '< 2.5', unit: 'Jam', frequency: 'Mingguan', visualization: 'Line Trend' },
        { id: 'k2', name: 'Mean Time Between Failures (MTBF)', description: 'Rata-rata jam operasi produktif unit sebelum mengalami kerusakan berikutnya.', formula: '(Total Operating Hours / Jumlah Breakdown)', source: 'Equipment.current_hm & WorkOrder', target: '> 120', unit: 'Jam', frequency: 'Bulanan', visualization: 'Bar Chart' },
        { id: 'k3', name: 'Preventive Maintenance Compliance', description: 'Persentase servis PM yang terlaksana tepat waktu sesuai toleransi toleransi HM.', formula: '(PM Selesai Tepat Waktu / Total Jadwal PM) * 100', source: 'WorkOrder.status', target: '>= 92', unit: '%', frequency: 'Mingguan', visualization: 'Gauge Meter' },
        { id: 'k4', name: 'Physical Availability (PA)', description: 'Tingkat kesiapan fisik unit armada untuk dioperasikan oleh tim produksi pit.', formula: '((Total Jam - Downtime Jam) / Total Jam) * 100', source: 'Equipment & WorkOrder', target: '>= 90', unit: '%', frequency: 'Harian', visualization: 'Stat Card' },
        { id: 'k5', name: 'Backlog Man-Hours', description: 'Akumulasi estimasi jam kerja perbaikan yang belum dieksekusi oleh tim workshop.', formula: 'SUM(Estimated Labor Hours) WHERE Status IN ("PLANNED", "APPROVED")', source: 'WorkOrder', target: '< 40', unit: 'Jam', frequency: 'Mingguan', visualization: 'Bar Chart' }
    ];

    projectPRD.notifications = [
        { id: 'n1', name: 'Critical Breakdown P0 Logged', trigger: 'Penerbitan Work Order dengan prioritas P0', recipient: 'Maintenance Supervisor', channel: 'In-App Toast', priority: 'P1 Critical', escalation: 'Eskalasi ke Plant Manager jika tak direspon dalam 20 menit', template: '[BREAKDOWN P0] Unit {unit_code} mengalami kerusakan fatal di {location}. Segera kirim regu respon darurat.' },
        { id: 'n2', name: 'PM Service Overdue Alert', trigger: 'Unit melampaui jadwal PM lebih dari 50 HM', recipient: 'Maintenance Planner', channel: 'Email', priority: 'P2 High', escalation: 'Kirim notifikasi tembusan ke Superintendent', template: '[PM OVERDUE] Unit {unit_code} telah melewati batas servis berkala {pm_type}. Jadwalkan slot workshop segera.' },
        { id: 'n3', name: 'Work Order Awaiting Approval', trigger: 'WO berstatus PLANNED membutuhkan otorisasi', recipient: 'Maintenance Supervisor', channel: 'In-App Toast', priority: 'P3 Normal', escalation: 'Pengingat harian pada apel shift pagi', template: '[PERSETUJUAN WO] Terdapat WO #{wo_number} ({unit_code}) menunggu tanda tangan persetujuan rilis.' },
        { id: 'n4', name: 'Critical Spare Part Stockout Warning', trigger: 'Saldo stok suku cadang mencapai atau di bawah min_stock', recipient: 'Warehouse Officer', channel: 'In-App Toast', priority: 'P2 High', escalation: 'Otomatis buat draf permohonan PO pengadaan', template: '[STOK KRITIS] Suku cadang {part_number} tersisa {stock_qty} unit (di bawah batas minimum {min_stock}).' }
    ];

    projectPRD.integrations = [
        { id: 'i1', system: 'SAP S/4HANA Enterprise ERP', purpose: 'Sinkronisasi master aset alat berat dan pemotongan biaya pemakaian suku cadang ke pusat biaya (Cost Center).', direction: 'Bi-directional', data: 'AssetMaster, MaterialIssue, CostCenter, GL_Account', frequency: 'Batch Harian', auth: 'OAuth 2.0 REST API', mockNotes: 'Pada MVP, sediakan tombol simulasikan Sync SAP dengan toast feedback sukses dan log transaksi dummy.' },
        { id: 'i2', system: 'Modular Mining Dispatch (FMS)', purpose: 'Menerima data telemetri Hour Meter (HM) aktual dan status kesiapan unit (Ready / Breakdown) secara berkala.', direction: 'Inbound', data: 'UnitCode, GPS_Coordinates, CurrentHM, EquipmentState', frequency: 'Real-time Webhook', auth: 'API Key Header', mockNotes: 'Disimulasikan melalui random increment HM pada tabel aset saat user merefresh tampilan.' },
        { id: 'i3', system: 'Caterpillar VIMS / KOMTRAX IoT Telemetry', purpose: 'Menerima kode peringatan dini kerusakan sensor mesin (Fault Codes) secara langsung dari ECU alat berat.', direction: 'Inbound', data: 'FaultCode, EngineTemperature, OilPressure, SeverityLevel', frequency: 'Real-time Webhook', auth: 'MQTT / HTTPS Post', mockNotes: 'Disimulasikan dengan memunculkan badge fault code pada profil detail armada.' },
        { id: 'i4', system: 'Ditjen Minerba SIMBARA ESDM Gateway', purpose: 'Pelaporan rutin ketersediaan alat berat dan kelaikan operasional armada tambang sesuai regulasi teknis.', direction: 'Outbound', data: 'IUP_Number, TotalFleet, AvailabilityRate, IncidentReport', frequency: 'Batch Harian', auth: 'Government REST Gateway Token', mockNotes: 'Pada MVP, sediakan tombol cetak laporan format standar ESDM.' }
    ];

    projectPRD.uiux.themeId = 2; // Bento UI default
    projectPRD.uiux.themeName = 'Bento UI';
    projectPRD.uiux.layout = 'sidebar_topbar';
    projectPRD.uiux.screens = [
        { id: 's1', name: 'Executive Overview Dashboard', features: 'Visualisasi KPI utama, Ringkasan status armada, Backlog chart', components: 'Stat KPI Cards, Bar Chart breakdown, Quick Action WO, Recent activity stream' },
        { id: 's2', name: 'Work Order Management Table', features: 'Filter multi-kriteria, Pencarian nomor WO, Status badge, Quick action menu', components: 'Data table interaktif dengan sorting, badge prioritas, pagination, tombol status transition' },
        { id: 's3', name: 'Work Order Detail & Execution Modal', features: 'Checklist inspeksi digital, Form ganti status, Alokasi suku cadang, Logging jam mekanik', components: 'Modal dialog responsif dengan tab rincian part, timeline alur kerja, dan sign-off digital' },
        { id: 's4', name: 'Equipment Asset Register Grid', features: 'Katalog seluruh unit alat berat, HM tracker, Status operasional', components: 'Bento Grid kartu armada, gauge hour meter, riwayat perbaikan sebelumnya' },
        { id: 's5', name: 'Weekly Maintenance Planning Board', features: 'Penjadwalan PM mingguan, Alokasi slot workshop bay', components: 'Gantt schedule visual horizontal, drag-and-drop simulation, indikator beban teknisi' }
    ];

    // Initialize Default RBAC permissions
    initDefaultRbacMatrix();

    // Re-render all views
    syncStep1Form();
    renderRoles();
    renderModulesAndFeatures();
    renderWorkflowNodes();
    renderBusinessRules();
    renderEntities();
    renderRbacMatrix();
    renderKpis();
    renderNotifications();
    renderIntegrations();
    renderScreens();
    updateUiMetadata();
    checkCompleteness();

    Swal.fire({
        toast: true,
        position: 'top-end',
        icon: 'success',
        title: 'Preset Mining CMMS Diterapkan',
        text: 'Spesifikasi requirement 16-step lengkap telah diisi otomatis.',
        showConfirmButton: false,
        timer: 2500,
        background: '#0D111A',
        color: '#F8FAFC'
    });
}

// B2B Trading Preset Generator
function loadB2BTradingPreset() {
    projectPRD.project = {
        name: 'B2B Mineral & Coal Supply Trading Platform',
        description: 'Platform perdagangan digital komoditas batubara dan bijih nikel laterit dengan simulasi lelang spot, penyesuaian harga indeks kalori (GCV), dan verifikasi Certificate of Analysis (CoA) surveyor.',
        problem: 'Inefisiensi rantai transaksi lelang komoditas manual, keterlambatan pencocokan jadwal tongkang di jetty, dan sengketa penyesuaian mutu kadar mineral saat bongkar muat.',
        objective: 'Mempercepat siklus lelang komoditas dari 14 hari menjadi 3 hari, menjamin transparansi formula bonus-penalti kalori batubara, dan integrasi dokumen pengapalan Syahbandar.',
        industry: 'Perdagangan Komoditas Energi & Mineral (B2B Trading)',
        department: 'Commercial, Trading & Shipping, Quality Assurance',
        targetOrg: 'Trader Batubara, Pembangkit Listrik (PLTU), Pabrik Smelter Nikel',
        scope: 'Katalog Lelang Spot Komoditas, Kalkulator Formula Penyesuaian Harga Indeks, Verifikasi Dokumen CoA Surveyor, Booking Slot Dermaga Jetty, dan Penerbitan Sales Contract.',
        outOfScope: 'Kliring settlement perbankan internasional secara real-time dan pengelolaan armada kapal kargo milik pihak ketiga.',
        successCriteria: '100% kontrak jual-beli terverifikasi secara digital, zero dispute pada formula perhitungan penyesuaian kadar kalori batubara.',
        additionalNotes: 'Setiap penawaran lelang yang disetujui wajib melampirkan salinan Certificate of Analysis (CoA) dari lembaga surveyor terakreditasi KAN.'
    };

    projectPRD.taxonomy.pillar = 'e_commerce';
    projectPRD.taxonomy.subtypeId = 'ec_coal_b2b_spot_contract';

    projectPRD.roles = [
        { id: 'r1', name: 'Commercial Manager', department: 'Commercial & Sales', type: 'primary', responsibility: 'Menetapkan kuota alokasi penjualan komoditas dan memvalidasi kontrak final.', persona: 'Fokus pada marjin keuntungan dan mitigasi risiko fluktuasi harga acuan.' },
        { id: 'r2', name: 'Commodity Buyer', department: 'Procurement (Buyer)', type: 'primary', responsibility: 'Mengajukan penawaran lelang spot, memverifikasi spesifikasi teknis kalori batubara.', persona: 'Memerlukan transparansi kalkulasi bonus/penalti dan kepastian jadwal muat.' },
        { id: 'r3', name: 'QA / Lab Surveyor', department: 'Quality Assurance', type: 'primary', responsibility: 'Mengunggah hasil analisis proksimat laboratorium dan menerbitkan sertifikat CoA resmi.', persona: 'Menjamin validitas data parameter uji (GCV, Total Moisture, Ash, Sulfur).' },
        { id: 'r4', name: 'Shipping & Jetty Officer', department: 'Logistics Port', type: 'secondary', responsibility: 'Mengatur alokasi tongkang pemuatan dan pemantauan laju muat conveyor.', persona: 'Mencegah terjadinya denda demurrage kapal di pelabuhan muat.' }
    ];

    projectPRD.modules = [
        { id: 'm1', name: 'Commodity Listing & Auction', description: 'Katalog penawaran kargo batubara dan lelang kuota spot.', submodules: 'Cargo Registry, Live Bidding, Offer Evaluation' },
        { id: 'm2', name: 'Pricing & Quality Calculator', description: 'Simulasi penyesuaian harga berbasis indeks HBA/ICI dan parameter mutu CoA.', submodules: 'Index Engine, Penalty-Bonus Formula, Currency Adjuster' },
        { id: 'm3', name: 'Shipping & Jetty Coordination', description: 'Penjadwalan kedatangan tongkang dan dokumen perizinan pelabuhan muat.', submodules: 'Berth Allocation, Barge Tracking, Shipping Docs' }
    ];

    projectPRD.features = [
        { id: 'f1', moduleId: 'm1', name: 'Interactive Cargo Auction Bidding', description: 'Formulir pengajuan penawaran harga per metrik ton dengan simulasi kalkulasi total transaksi.', priority: 'P0', primaryUser: 'Commodity Buyer', dependencies: 'Commodity Listing', expectedOutcome: 'Penawaran tercatat di papan lelang dengan urutan peringkat harga tertinggi.' },
        { id: 'f2', moduleId: 'm2', name: 'Automated GCV Bonus & Penalty Calculator', description: 'Penghitungan penyesuaian harga otomatis saat kadar kalori aktual berbeda dari baseline kontrak.', priority: 'P0', primaryUser: 'Commercial Manager', dependencies: 'Quality Calculator', expectedOutcome: 'Kalkulasi nilai tagihan final terhitung otomatis dalam USD dan IDR.' },
        { id: 'f3', moduleId: 'm3', name: 'Surveyor CoA Digital Verification', description: 'Validasi dokumen Certificate of Analysis dengan badge verifikasi resmi surveyor independen.', priority: 'P0', primaryUser: 'QA / Lab Surveyor', dependencies: 'Auction Module', expectedOutcome: 'Badge terverifikasi aktif pada kargo yang bersangkutan.' }
    ];

    projectPRD.workflows = [
        { id: 'w1', stepNo: 1, name: 'Cargo Offer Published', trigger: 'Trader merilis kargo baru', actor: 'Commercial Manager', input: 'Tonase, baseline kalori, lokasi jetty', action: 'Menerbitkan penawaran lelang terbuka di portal', decision: 'Status kuota terpenuhi?', output: 'Kargo tampil di katalog lelang', status: 'PUBLISHED' },
        { id: 'w2', stepNo: 2, name: 'Bid Submission', trigger: 'Buyer berminat mengajukan harga', actor: 'Commodity Buyer', input: 'Harga penawaran per MT, target jadwal muat', action: 'Memasukkan nominal penawaran di form lelang', decision: 'Penawaran di atas batas floor price?', output: 'Penawaran tercatat di ranking sistem', status: 'BID_SUBMITTED' },
        { id: 'w3', stepNo: 3, name: 'Bid Acceptance & Contract Award', trigger: 'Masa lelang ditutup', actor: 'Commercial Manager', input: 'Daftar penawaran peringkat teratas', action: 'Memilih penawar terbaik dan menerbitkan kontrak proforma', decision: 'Buyer lolos verifikasi kredibilitas?', output: 'Surat penunjukan pemenang terbit', status: 'AWARDED' },
        { id: 'w4', stepNo: 4, name: 'CoA Verification & Settlement', trigger: 'Proses pemuatan tongkang selesai di jetty', actor: 'QA / Lab Surveyor', input: 'Hasil analisis laboratorium sampling', action: 'Mengunggah hasil CoA dan menghitung penyesuaian harga akhir', decision: 'Spesifikasi sesuai batas toleransi kontrak?', output: 'Faktur komersial final diterbitkan untuk pelunasan', status: 'SETTLED' }
    ];

    projectPRD.businessRules = [
        { id: 'br1', name: 'Bid Below Reserve Price Prohibited', description: 'Penawaran harga lelang di bawah harga patokan minimal (Floor Price) otomatis ditolak sistem.', condition: 'Offered Price < Reserve Price', action: 'Tolak pengajuan dan tampilkan peringatan bahwa harga di bawah patokan.', exception: 'Negosiasi tertutup khusus kargo surplus.', severity: 'Blocking' },
        { id: 'br2', name: 'Contract Award Requires Verified Surveyor CoA', description: 'Kontrak penjualan komoditas tidak dapat berstatus Final tanpa lampiran sertifikat mutu surveyor.', condition: 'CoA Attachment is Missing OR Verified == False', action: 'Kunci tombol persetujuan kontrak final.', exception: 'Kontrak estimasi sementara (Provisional Contract).', severity: 'Blocking' }
    ];

    projectPRD.entities = [
        {
            id: 'e1',
            name: 'CargoListing',
            description: 'Katalog kargo komoditas mineral/batubara yang ditawarkan.',
            type: 'Transactional',
            storage: 'tbl_cargo_listings',
            fields: [
                { id: 'f1', name: 'id', type: 'String', required: 'true', defaultValue: 'UUID', validation: 'Primary Key', description: 'ID kargo' },
                { id: 'f2', name: 'cargo_code', type: 'String', required: 'true', defaultValue: "''", validation: 'Unique', description: 'Kode lot kargo' },
                { id: 'f3', name: 'commodity_type', type: 'Enum', required: 'true', defaultValue: "'Coal'", validation: 'In: Coal, Nickel_Ore, Gold_Bullion', description: 'Jenis komoditas' },
                { id: 'f4', name: 'quantity_mt', type: 'Decimal', required: 'true', defaultValue: '50000.0', validation: 'Min:1000', description: 'Tonase kuota (Metrik Ton)' },
                { id: 'f5', name: 'baseline_spec', type: 'String', required: 'true', defaultValue: "'GAR 4200 kcal/kg'", validation: 'Min:3', description: 'Kadar mutu baseline' }
            ],
            relationships: []
        }
    ];

    projectPRD.kpis = [
        { id: 'k1', name: 'Average Bid Spread %', description: 'Selisih rata-rata antara harga penawaran awal dengan harga kontrak final.', formula: '((Final Price - Floor Price) / Floor Price) * 100', source: 'CargoListing & Bids', target: '> 8.5', unit: '%', frequency: 'Bulanan', visualization: 'Line Trend' },
        { id: 'k2', name: 'Jetty Turnaround Laytime', description: 'Rata-rata waktu pemuatan tongkang di dermaga jetty pemuatan.', formula: 'Total Hours Loading / Jumlah Tongkang', source: 'Shipping Module', target: '< 36', unit: 'Jam', frequency: 'Mingguan', visualization: 'Bar Chart' }
    ];

    projectPRD.notifications = [
        { id: 'n1', name: 'New Competitive Bid Placed', trigger: 'Buyer memasukkan penawaran baru dengan harga tertinggi', recipient: 'Commercial Manager', channel: 'In-App Toast', priority: 'P2 High', escalation: 'Kirim rangkuman email harian', template: '[LELANG AKTIF] Penawaran baru sebesar ${price}/MT dimasukkan untuk kargo {cargo_code}.' }
    ];

    projectPRD.integrations = [
        { id: 'i1', system: 'London Metal Exchange (LME) / ICI Price API', purpose: 'Penarikan data indeks harga komoditas global secara harian.', direction: 'Inbound', data: 'IndexCode, ClosingPrice, CurrencyRate', frequency: 'Batch Harian', auth: 'REST API Key', mockNotes: 'Disimulasikan dengan nilai indeks statis realistis di antarmuka.' }
    ];

    projectPRD.uiux.themeId = 18; // Corporate Clean
    projectPRD.uiux.themeName = 'Corporate Clean';
    projectPRD.uiux.layout = 'sidebar_topbar';
    projectPRD.uiux.screens = [
        { id: 's1', name: 'Commodity Trading Floor Dashboard', features: 'Live ticker harga, Daftar kargo aktif, Metrik lelang', components: 'Stat Cards, Grid Kargo, Filter Komoditas' },
        { id: 's2', name: 'Bidding & Auction Room', features: 'Formulir penawaran harga, Riwayat penawar, Timer hitung mundur', components: 'Tabel Bidding, Kalkulator bonus kalori, Tombol Submit Bid' }
    ];

    initDefaultRbacMatrix();
    syncStep1Form();
    renderRoles();
    renderModulesAndFeatures();
    renderWorkflowNodes();
    renderBusinessRules();
    renderEntities();
    renderRbacMatrix();
    renderKpis();
    renderNotifications();
    renderIntegrations();
    renderScreens();
    updateUiMetadata();
    checkCompleteness();

    Swal.fire({
        toast: true,
        position: 'top-end',
        icon: 'success',
        title: 'Preset B2B Trading Diterapkan',
        text: 'Spesifikasi platform lelang komoditas siap ditinjau.',
        showConfirmButton: false,
        timer: 2500,
        background: '#0D111A',
        color: '#F8FAFC'
    });
}

function resetProjectConfirm() {
    Swal.fire({
        title: 'Reset Seluruh Proyek?',
        text: 'Seluruh isian spesifikasi akan dikosongkan kembali ke awal.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#F43F5E',
        cancelButtonColor: '#1E293B',
        confirmButtonText: 'Ya, Kosongkan',
        cancelButtonText: 'Batal',
        background: '#0D111A',
        color: '#F8FAFC'
    }).then((result) => {
        if (result.isConfirmed) {
            projectPRD.project = {
                name: '', description: '', problem: '', objective: '',
                industry: '', department: '', targetOrg: '', scope: '',
                outOfScope: '', successCriteria: '', additionalNotes: ''
            };
            projectPRD.roles = [];
            projectPRD.modules = [];
            projectPRD.features = [];
            projectPRD.workflows = [];
            projectPRD.businessRules = [];
            projectPRD.entities = [];
            projectPRD.permissions = {};
            projectPRD.kpis = [];
            projectPRD.notifications = [];
            projectPRD.integrations = [];
            projectPRD.uiux.screens = [];

            syncStep1Form();
            renderRoles();
            renderModulesAndFeatures();
            renderWorkflowNodes();
            renderBusinessRules();
            renderEntities();
            renderRbacMatrix();
            renderKpis();
            renderNotifications();
            renderIntegrations();
            renderScreens();
            updateUiMetadata();
            checkCompleteness();
            goToStep(1);

            Swal.fire({
                toast: true,
                position: 'top-end',
                icon: 'info',
                title: 'Proyek Telah Dikosongkan',
                showConfirmButton: false,
                timer: 2000,
                background: '#0D111A',
                color: '#F8FAFC'
            });
        }
    });
}

// ============================================================================
// STEP CONTROLLER & NAVIGATION
// ============================================================================
function goToStep(step) {
    if (step < 1 || step > 16) return;

    // Read latest inputs if leaving step 1
    if (currentStep === 1) {
        saveStep1Inputs();
    }

    currentStep = step;

    // Update Sidebar navigation active classes
    for (let i = 1; i <= 16; i++) {
        const navEl = document.getElementById(`nav-step-${i}`);
        const panelEl = document.getElementById(`panel-step-${i}`);
        if (navEl) {
            if (i === step) navEl.classList.add('active');
            else navEl.classList.remove('active');
        }
        if (panelEl) {
            if (i === step) panelEl.classList.add('active');
            else panelEl.classList.remove('active');
        }
    }

    const stepCountBadge = document.getElementById('sidebar-step-count');
    if (stepCountBadge) stepCountBadge.textContent = `Step ${step} / 16`;

    // Scroll main viewport to top
    const mainView = document.querySelector('.main-viewport');
    if (mainView) mainView.scrollTop = 0;

    // Dynamically update top navbar AI button label to match active step
    const topAiBtnText = document.getElementById('top-btn-ai-text');
    if (topAiBtnText) {
        if (step <= 13) {
            topAiBtnText.textContent = `Isi Step ${step} by AI`;
        } else if (step === 14) {
            topAiBtnText.textContent = 'Audit PRD by AI';
        } else if (step === 15) {
            topAiBtnText.textContent = 'Refresh Dokumen PRD';
        } else if (step === 16) {
            topAiBtnText.textContent = 'Optimasi Prompt by AI';
        }
    }

    // Trigger step-specific logic
    if (step === 8) renderRbacMatrix();
    if (step === 14) checkCompleteness();
    if (step === 15) renderPrdDocument();
    if (step === 16) renderMvpPromptOutput();
}

function updateUiMetadata() {
    const topProjName = document.getElementById('top-project-name');
    if (topProjName) {
        topProjName.textContent = projectPRD.project.name || 'Proyek Baru (Kosong)';
    }

    // Update Subtitles in Sidebar
    const sub2 = document.getElementById('sub-step-2');
    const sub3 = document.getElementById('sub-step-3');
    const sub4 = document.getElementById('sub-step-4');
    const sub5 = document.getElementById('sub-step-5');
    const sub6 = document.getElementById('sub-step-6');
    const sub7 = document.getElementById('sub-step-7');
    const sub9 = document.getElementById('sub-step-9');
    const sub10 = document.getElementById('sub-step-10');
    const sub11 = document.getElementById('sub-step-11');
    const sub12 = document.getElementById('sub-step-12');

    if (sub2) sub2.textContent = projectPRD.taxonomy.pillar ? (getPillarName(projectPRD.taxonomy.pillar) || 'Pilar Terpilih') : 'Pilih 1 Pilar';
    if (sub3) sub3.textContent = `${projectPRD.roles.length} Role Terdaftar`;
    if (sub4) sub4.textContent = `${projectPRD.modules.length} Modul / ${projectPRD.features.length} Fitur`;
    if (sub5) sub5.textContent = `${projectPRD.workflows.length} Tahapan Alur`;
    if (sub6) sub6.textContent = `${projectPRD.businessRules.length} Aturan Bisnis`;
    if (sub7) sub7.textContent = `${projectPRD.entities.length} Entitas Data`;
    if (sub9) sub9.textContent = `${projectPRD.kpis.length} Metrik KPI`;
    if (sub10) sub10.textContent = `${projectPRD.notifications.length} Notifikasi`;
    if (sub11) sub11.textContent = `${projectPRD.integrations.length} Integrasi Sistem`;
    if (sub12) sub12.textContent = `${projectPRD.uiux.themeName} &bull; ${projectPRD.uiux.screens.length} Screens`;
}

// ============================================================================
// STEP 1: PROJECT DEFINITION CONTROLLER
// ============================================================================
function syncStep1Form() {
    const p = projectPRD.project;
    const fields = [
        ['p-name', p.name],
        ['p-industry', p.industry],
        ['p-dept', p.department],
        ['p-target-org', p.targetOrg],
        ['p-desc', p.description],
        ['p-problem', p.problem],
        ['p-objective', p.objective],
        ['p-scope', p.scope],
        ['p-out-scope', p.outOfScope],
        ['p-success', p.successCriteria],
        ['p-additional', p.additionalNotes]
    ];

    fields.forEach(([id, val]) => {
        const el = document.getElementById(id);
        if (el) el.value = val || '';
    });
}

function saveStep1Inputs() {
    const p = projectPRD.project;
    const getVal = id => {
        const el = document.getElementById(id);
        return el ? el.value.trim() : '';
    };

    p.name = getVal('p-name');
    p.industry = getVal('p-industry');
    p.department = getVal('p-dept');
    p.targetOrg = getVal('p-target-org');
    p.description = getVal('p-desc');
    p.problem = getVal('p-problem');
    p.objective = getVal('p-objective');
    p.scope = getVal('p-scope');
    p.outOfScope = getVal('p-out-scope');
    p.successCriteria = getVal('p-success');
    p.additionalNotes = getVal('p-additional');

    updateUiMetadata();
}

// ============================================================================
// STEP 2: 5 PILAR ARSITEKTUR (SUBTIPE DIHAPUS SEMUA)
// ============================================================================
function initTaxonomyUI() {
    renderPillarsLarge();
    updatePillarSummary();
}

function renderPillarsLarge() {
    const container = document.getElementById('pillars-large-container');
    if (!container) return;
    container.innerHTML = '';

    const activePillarKey = projectPRD.taxonomy.pillar || '';

    ARCHITECTURE_PILLARS.forEach(p => {
        const isSelected = p.key === activePillarKey;
        const card = document.createElement('div');
        card.className = 'pillar-card-hero' + (isSelected ? ' selected' : '');
        card.id = `pillar-card-${p.key}`;
        card.onclick = () => selectPillar(p.key);

        const modulesTags = p.recommendedModules.map(m =>
            `<span style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.08); font-size:10px; color:#CBD5E1; padding:2px 8px; border-radius:6px;">${escapeHtml(m)}</span>`
        ).join('');

        card.innerHTML = `
            <div>
                <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px;">
                    <div class="pillar-icon-box" style="background:${p.iconBg}; border:1px solid ${p.iconColor}40; color:${p.iconColor};">
                        <i class="fa-solid ${p.icon}"></i>
                    </div>
                    <span class="badge ${p.badgeClass}">${p.badge}</span>
                </div>
                <h3 class="font-outfit" style="font-size:16px; font-weight:800; color:#FFFFFF; margin-bottom:6px;">
                    ${escapeHtml(p.name)}
                </h3>
                <p style="font-size:11.5px; font-weight:600; color:${p.iconColor}; margin-bottom:8px; line-height:1.4;">
                    ${escapeHtml(p.tagline)}
                </p>
                <p style="font-size:11.5px; color:#94A3B8; line-height:1.5; margin-bottom:14px;">
                    ${escapeHtml(p.description)}
                </p>
            </div>
            <div>
                <div style="font-size:10.5px; color:#64748B; text-transform:uppercase; font-weight:700; margin-bottom:6px; letter-spacing:0.5px;">Modul Tipikal:</div>
                <div style="display:flex; flex-wrap:wrap; gap:4px; margin-bottom:14px;">
                    ${modulesTags}
                </div>
                <div style="display:flex; align-items:center; justify-content:space-between; padding-top:10px; border-top:1px solid #1E293B;">
                    <span style="font-size:11px; color:#64748B;">Archetype: <strong style="color:#CBD5E1;">${escapeHtml(p.archetype)}</strong></span>
                    <span style="font-size:11px; font-weight:700; color:${isSelected ? '#10B981' : '#6366F1'};">
                        ${isSelected ? '<i class="fa-solid fa-circle-check" style="margin-right:4px;"></i>Terpilih' : 'Pilih Pilar &rarr;'}
                    </span>
                </div>
            </div>
        `;

        container.appendChild(card);
    });
}

function selectPillar(key) {
    projectPRD.taxonomy.pillar = key;
    const p = getPillarObj(key);
    if (p) {
        projectPRD.taxonomy.archetype = p.archetype;
    }

    document.querySelectorAll('.pillar-card-hero').forEach(card => card.classList.remove('selected'));
    const target = document.getElementById(`pillar-card-${key}`);
    if (target) target.classList.add('selected');

    updatePillarSummary();
    updateUiMetadata();
    checkCompleteness();
    saveProject(false);

    Swal.fire({
        toast: true,
        position: 'top-end',
        icon: 'success',
        title: `Pilar Arsitektur Dipilih: ${p ? p.name : key}`,
        showConfirmButton: false,
        timer: 2000,
        background: '#0D111A',
        color: '#F8FAFC'
    });
}

function updatePillarSummary() {
    const p = getPillarObj(projectPRD.taxonomy.pillar);
    const titleEl = document.getElementById('active-pillar-title');
    const iconBox = document.getElementById('active-pillar-icon-box');
    const badgeEl = document.getElementById('active-pillar-badge');

    if (p) {
        if (titleEl) titleEl.textContent = `${p.name} - ${p.tagline}`;
        if (iconBox) {
            iconBox.innerHTML = `<i class="fa-solid ${p.icon}"></i>`;
            iconBox.style.color = p.iconColor;
            iconBox.style.background = p.iconBg;
            iconBox.style.borderColor = p.iconColor + '50';
        }
        if (badgeEl) {
            badgeEl.className = `badge ${p.badgeClass}`;
            badgeEl.textContent = p.badge.toUpperCase();
        }
    } else {
        if (titleEl) titleEl.textContent = 'Belum Dipilih (Klik salah satu pilar di atas)';
        if (iconBox) {
            iconBox.innerHTML = '<i class="fa-solid fa-cube"></i>';
            iconBox.style.color = '#818CF8';
            iconBox.style.background = 'rgba(99,102,241,0.18)';
            iconBox.style.borderColor = 'rgba(99,102,241,0.3)';
        }
        if (badgeEl) {
            badgeEl.className = 'badge badge-slate';
            badgeEl.textContent = 'BELUM DIPILIH';
        }
    }
}

// ============================================================================
// STEP 3: USERS & ROLES CONTROLLER
// ============================================================================
function renderRoles() {
    const container = document.getElementById('roles-cards-container');
    if (!container) return;
    container.innerHTML = '';

    if (projectPRD.roles.length === 0) {
        container.innerHTML = `
            <div style="grid-column:1/-1; padding:40px 20px; text-align:center; color:#64748B; background:#080C14; border-radius:12px; border:1px dashed #1E293B;">
                <i class="fa-solid fa-users" style="font-size:32px; color:#334155; margin-bottom:10px;"></i>
                <div style="font-size:14px; font-weight:700; color:#E2E8FF;">Belum Ada Role Didefinisikan</div>
                <div style="font-size:11.5px; margin:4px 0 16px;">Klik tombol "Tambah Role Baru" atau gunakan Template Preset.</div>
                <button type="button" class="btn btn-primary btn-sm" onclick="openRoleModal()">
                    <i class="fa-solid fa-plus"></i> Tambah Role Pertama
                </button>
            </div>
        `;
        return;
    }

    projectPRD.roles.forEach((r, idx) => {
        const card = document.createElement('div');
        card.className = 'card-box';
        card.style.padding = '14px 16px';
        card.style.marginBottom = '0';
        card.style.display = 'flex';
        card.style.flexDirection = 'column';
        card.style.justifyContent = 'space-between';

        const typeBadge = r.type === 'primary' ? '<span class="badge badge-emerald">Primary User</span>' : '<span class="badge badge-slate">Secondary</span>';

        card.innerHTML = `
            <div>
                <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
                    <div>
                        <div style="font-size:13.5px; font-weight:800; color:#FFFFFF;">${r.name}</div>
                        <div style="font-size:11px; color:#818CF8; font-weight:600;">${r.department || 'Operasional'}</div>
                    </div>
                    ${typeBadge}
                </div>
                <div style="font-size:11.5px; color:#94A3B8; line-height:1.5; margin:8px 0;">
                    <strong>Tanggung Jawab:</strong> ${r.responsibility || '-'}
                </div>
                ${r.persona ? `<div style="font-size:11px; color:#64748B; font-style:italic;">"${r.persona}"</div>` : ''}
            </div>
            <div style="display:flex; justify-content:flex-end; gap:6px; margin-top:12px; padding-top:8px; border-top:1px solid var(--border-color);">
                <button type="button" class="btn btn-secondary btn-sm" onclick="editRole('${r.id}')"><i class="fa-solid fa-pen-to-square"></i></button>
                <button type="button" class="btn btn-rose btn-sm" onclick="deleteRole('${r.id}')"><i class="fa-solid fa-trash-can"></i></button>
            </div>
        `;
        container.appendChild(card);
    });

    updateUiMetadata();
}

function openRoleModal(roleId = null) {
    const titleEl = document.getElementById('modal-role-title');
    const idInput = document.getElementById('modal-role-id');
    const nameInput = document.getElementById('m-role-name');
    const deptInput = document.getElementById('m-role-dept');
    const typeInput = document.getElementById('m-role-type');
    const respInput = document.getElementById('m-role-resp');
    const personaInput = document.getElementById('m-role-persona');

    if (roleId) {
        const r = projectPRD.roles.find(x => x.id === roleId);
        if (r) {
            titleEl.textContent = 'Edit Role Pengguna';
            idInput.value = r.id;
            nameInput.value = r.name;
            deptInput.value = r.department;
            typeInput.value = r.type || 'primary';
            respInput.value = r.responsibility || '';
            personaInput.value = r.persona || '';
        }
    } else {
        titleEl.textContent = 'Tambah Role Baru';
        idInput.value = '';
        nameInput.value = '';
        deptInput.value = '';
        typeInput.value = 'primary';
        respInput.value = '';
        personaInput.value = '';
    }

    openModal('modal-role');
}

function editRole(id) {
    openRoleModal(id);
}

function deleteRole(id) {
    projectPRD.roles = projectPRD.roles.filter(r => r.id !== id);
    renderRoles();
}

function saveRoleModal() {
    const id = document.getElementById('modal-role-id').value;
    const name = document.getElementById('m-role-name').value.trim();
    const dept = document.getElementById('m-role-dept').value.trim();
    const type = document.getElementById('m-role-type').value;
    const resp = document.getElementById('m-role-resp').value.trim();
    const persona = document.getElementById('m-role-persona').value.trim();

    if (!name) {
        Swal.fire({ icon: 'warning', title: 'Nama Role Wajib Diisi', background: '#0D111A', color: '#F8FAFC' });
        return;
    }

    if (id) {
        const r = projectPRD.roles.find(x => x.id === id);
        if (r) {
            r.name = name;
            r.department = dept;
            r.type = type;
            r.responsibility = resp;
            r.persona = persona;
        }
    } else {
        projectPRD.roles.push({
            id: 'r_' + Date.now(),
            name: name,
            department: dept,
            type: type,
            responsibility: resp,
            persona: persona
        });
    }

    closeModal('modal-role');
    renderRoles();
}

// ============================================================================
// STEP 4: MODULES & FEATURES CONTROLLER
// ============================================================================
function renderModulesAndFeatures() {
    const container = document.getElementById('modules-list-container');
    if (!container) return;
    container.innerHTML = '';

    if (projectPRD.modules.length === 0) {
        container.innerHTML = `
            <div style="padding:40px 20px; text-align:center; color:#64748B; background:#080C14; border-radius:12px; border:1px dashed #1E293B;">
                <i class="fa-solid fa-cubes" style="font-size:32px; color:#334155; margin-bottom:10px;"></i>
                <div style="font-size:14px; font-weight:700; color:#E2E8FF;">Belum Ada Modul Didefinisikan</div>
                <div style="font-size:11.5px; margin:4px 0 16px;">Tambahkan modul fungsional pertama Anda.</div>
                <button type="button" class="btn btn-primary btn-sm" onclick="openModuleModal()">
                    <i class="fa-solid fa-plus"></i> Tambah Modul
                </button>
            </div>
        `;
        return;
    }

    projectPRD.modules.forEach(m => {
        const modCard = document.createElement('div');
        modCard.className = 'card-box';
        modCard.style.marginBottom = '0';
        modCard.style.padding = '16px 20px';

        const modFeatures = projectPRD.features.filter(f => f.moduleId === m.id);

        let featuresHtml = '';
        if (modFeatures.length === 0) {
            featuresHtml = `<div style="padding:12px; font-size:11.5px; color:#64748B; font-style:italic;">Belum ada fitur di dalam modul ini. Klik "Tambah Fitur".</div>`;
        } else {
            featuresHtml = `<div style="display:flex; flex-direction:column; gap:8px; margin-top:12px;">`;
            modFeatures.forEach(f => {
                let pBadge = 'badge-slate';
                if (f.priority === 'P0') pBadge = 'badge-rose';
                else if (f.priority === 'P1') pBadge = 'badge-amber';
                else if (f.priority === 'P2') pBadge = 'badge-indigo';

                featuresHtml += `
                    <div style="background:#07090E; border:1px solid #1E293B; border-radius:8px; padding:10px 14px; display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <div style="display:flex; align-items:center; gap:8px; margin-bottom:2px;">
                                <span class="badge ${pBadge}">${f.priority}</span>
                                <span style="font-size:12.5px; font-weight:700; color:#FFFFFF;">${f.name}</span>
                                <span style="font-size:10.5px; color:#94A3B8;">&bull; User: <strong style="color:#C7D2FE;">${f.primaryUser || 'Semua Role'}</strong></span>
                            </div>
                            <div style="font-size:11px; color:#94A3B8;">${f.description || '-'}</div>
                            ${f.expectedOutcome ? `<div style="font-size:10.5px; color:#10B981; margin-top:2px;"><i class="fa-solid fa-arrow-turn-up" style="margin-right:4px;"></i>Outcome: ${f.expectedOutcome}</div>` : ''}
                        </div>
                        <div style="display:flex; gap:6px; flex-shrink:0;">
                            <button type="button" class="btn btn-secondary btn-sm" onclick="editFeature('${f.id}')"><i class="fa-solid fa-pen-to-square"></i></button>
                            <button type="button" class="btn btn-rose btn-sm" onclick="deleteFeature('${f.id}')"><i class="fa-solid fa-trash-can"></i></button>
                        </div>
                    </div>
                `;
            });
            featuresHtml += `</div>`;
        }

        modCard.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:flex-start; border-bottom:1px solid var(--border-color); padding-bottom:10px;">
                <div>
                    <div style="display:flex; align-items:center; gap:8px;">
                        <i class="fa-solid fa-folder-closed" style="color:#818CF8; font-size:14px;"></i>
                        <span style="font-size:14px; font-weight:800; color:#FFFFFF;">${m.name}</span>
                        <span class="badge badge-slate">${modFeatures.length} Fitur</span>
                    </div>
                    <div style="font-size:11.5px; color:#94A3B8; margin-top:2px;">${m.description || ''}</div>
                    ${m.submodules ? `<div style="font-size:10.5px; color:#818CF8; margin-top:2px;"><i class="fa-solid fa-tags" style="margin-right:4px;"></i>Submodul: ${m.submodules}</div>` : ''}
                </div>
                <div style="display:flex; gap:6px;">
                    <button type="button" class="btn btn-primary btn-sm" onclick="openFeatureModal('${m.id}')" title="Tambah Fitur ke Modul Ini">
                        <i class="fa-solid fa-plus"></i> Fitur
                    </button>
                    <button type="button" class="btn btn-secondary btn-sm" onclick="editModule('${m.id}')"><i class="fa-solid fa-pen-to-square"></i></button>
                    <button type="button" class="btn btn-rose btn-sm" onclick="deleteModule('${m.id}')"><i class="fa-solid fa-trash-can"></i></button>
                </div>
            </div>
            ${featuresHtml}
        `;
        container.appendChild(modCard);
    });

    updateUiMetadata();
}

function openModuleModal(moduleId = null) {
    const titleEl = document.getElementById('modal-module-title');
    const idInput = document.getElementById('modal-module-id');
    const nameInput = document.getElementById('m-mod-name');
    const descInput = document.getElementById('m-mod-desc');
    const subInput = document.getElementById('m-mod-sub');

    if (moduleId) {
        const m = projectPRD.modules.find(x => x.id === moduleId);
        if (m) {
            titleEl.textContent = 'Edit Modul';
            idInput.value = m.id;
            nameInput.value = m.name;
            descInput.value = m.description || '';
            subInput.value = m.submodules || '';
        }
    } else {
        titleEl.textContent = 'Tambah Modul Baru';
        idInput.value = '';
        nameInput.value = '';
        descInput.value = '';
        subInput.value = '';
    }

    openModal('modal-module');
}

function editModule(id) { openModuleModal(id); }
function deleteModule(id) {
    projectPRD.modules = projectPRD.modules.filter(m => m.id !== id);
    projectPRD.features = projectPRD.features.filter(f => f.moduleId !== id);
    renderModulesAndFeatures();
}

function saveModuleModal() {
    const id = document.getElementById('modal-module-id').value;
    const name = document.getElementById('m-mod-name').value.trim();
    const desc = document.getElementById('m-mod-desc').value.trim();
    const subs = document.getElementById('m-mod-sub').value.trim();

    if (!name) {
        Swal.fire({ icon: 'warning', title: 'Nama Modul Wajib Diisi', background: '#0D111A', color: '#F8FAFC' });
        return;
    }

    if (id) {
        const m = projectPRD.modules.find(x => x.id === id);
        if (m) {
            m.name = name;
            m.description = desc;
            m.submodules = subs;
        }
    } else {
        projectPRD.modules.push({
            id: 'm_' + Date.now(),
            name: name,
            description: desc,
            submodules: subs
        });
    }

    closeModal('modal-module');
    renderModulesAndFeatures();
}

// Feature Modal Handlers
function openFeatureModal(preselectedModuleId = null, featureId = null) {
    const titleEl = document.getElementById('modal-feat-title');
    const idInput = document.getElementById('modal-feat-id');
    const modSelect = document.getElementById('m-feat-mod');
    const userSelect = document.getElementById('m-feat-user');
    const nameInput = document.getElementById('m-feat-name');
    const prioritySelect = document.getElementById('m-feat-priority');
    const descInput = document.getElementById('m-feat-desc');
    const depInput = document.getElementById('m-feat-dep');
    const outcomeInput = document.getElementById('m-feat-outcome');

    // Populate module options
    modSelect.innerHTML = '';
    projectPRD.modules.forEach(m => {
        const opt = document.createElement('option');
        opt.value = m.id;
        opt.textContent = m.name;
        modSelect.appendChild(opt);
    });

    // Populate user role options
    userSelect.innerHTML = '<option value="">Semua Role / Publik</option>';
    projectPRD.roles.forEach(r => {
        const opt = document.createElement('option');
        opt.value = r.name;
        opt.textContent = r.name;
        userSelect.appendChild(opt);
    });

    if (featureId) {
        const f = projectPRD.features.find(x => x.id === featureId);
        if (f) {
            titleEl.textContent = 'Edit Fitur';
            idInput.value = f.id;
            modSelect.value = f.moduleId;
            nameInput.value = f.name;
            prioritySelect.value = f.priority || 'P1';
            userSelect.value = f.primaryUser || '';
            descInput.value = f.description || '';
            depInput.value = f.dependencies || '';
            outcomeInput.value = f.expectedOutcome || '';
        }
    } else {
        titleEl.textContent = 'Tambah Fitur Baru';
        idInput.value = '';
        if (preselectedModuleId) modSelect.value = preselectedModuleId;
        nameInput.value = '';
        prioritySelect.value = 'P1';
        descInput.value = '';
        depInput.value = '';
        outcomeInput.value = '';
    }

    openModal('modal-feature');
}

function editFeature(id) { openFeatureModal(null, id); }
function deleteFeature(id) {
    projectPRD.features = projectPRD.features.filter(f => f.id !== id);
    renderModulesAndFeatures();
}

function saveFeatureModal() {
    const id = document.getElementById('modal-feat-id').value;
    const moduleId = document.getElementById('m-feat-mod').value;
    const name = document.getElementById('m-feat-name').value.trim();
    const priority = document.getElementById('m-feat-priority').value;
    const primaryUser = document.getElementById('m-feat-user').value;
    const desc = document.getElementById('m-feat-desc').value.trim();
    const dep = document.getElementById('m-feat-dep').value.trim();
    const outcome = document.getElementById('m-feat-outcome').value.trim();

    if (!name || !moduleId) {
        Swal.fire({ icon: 'warning', title: 'Nama Fitur & Modul Wajib Diisi', background: '#0D111A', color: '#F8FAFC' });
        return;
    }

    if (id) {
        const f = projectPRD.features.find(x => x.id === id);
        if (f) {
            f.moduleId = moduleId;
            f.name = name;
            f.priority = priority;
            f.primaryUser = primaryUser;
            f.description = desc;
            f.dependencies = dep;
            f.expectedOutcome = outcome;
        }
    } else {
        projectPRD.features.push({
            id: 'f_' + Date.now(),
            moduleId: moduleId,
            name: name,
            priority: priority,
            primaryUser: primaryUser,
            description: desc,
            dependencies: dep,
            expectedOutcome: outcome
        });
    }

    closeModal('modal-feature');
    renderModulesAndFeatures();
}

// ============================================================================
// STEP 5: WORKFLOW ENGINE
// ============================================================================
function renderWorkflowNodes() {
    const container = document.getElementById('workflow-nodes-container');
    if (!container) return;
    container.innerHTML = '';

    if (projectPRD.workflows.length === 0) {
        container.innerHTML = `
            <div style="padding:40px 20px; text-align:center; color:#64748B; background:#080C14; border-radius:12px; border:1px dashed #1E293B;">
                <i class="fa-solid fa-arrows-split-up-and-left" style="font-size:32px; color:#334155; margin-bottom:10px;"></i>
                <div style="font-size:14px; font-weight:700; color:#E2E8FF;">Belum Ada Tahap Alur Kerja</div>
                <div style="font-size:11.5px; margin:4px 0 16px;">Rangkai alur proses operasional secara berurutan.</div>
                <button type="button" class="btn btn-primary btn-sm" onclick="openWorkflowModal()">
                    <i class="fa-solid fa-plus"></i> Tambah Tahap Pertama
                </button>
            </div>
        `;
        return;
    }

    projectPRD.workflows.forEach((w, idx) => {
        const card = document.createElement('div');
        card.className = 'wf-node-card';

        card.innerHTML = `
            <div class="wf-node-badge">${idx + 1}</div>
            <div style="flex:1; min-width:0;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:4px;">
                    <div>
                        <span style="font-size:14px; font-weight:800; color:#FFFFFF;">${w.name}</span>
                        <span class="badge badge-indigo" style="margin-left:8px;">${w.actor || 'Aktor Bebas'}</span>
                    </div>
                    <span class="badge badge-emerald">${w.status || 'ACTIVE'}</span>
                </div>
                <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:8px; margin-top:8px; font-size:11.5px; color:#94A3B8;">
                    ${w.trigger ? `<div><strong style="color:#CBD5E1;">Trigger:</strong> ${w.trigger}</div>` : ''}
                    ${w.input ? `<div><strong style="color:#CBD5E1;">Input:</strong> ${w.input}</div>` : ''}
                    ${w.action ? `<div><strong style="color:#CBD5E1;">Action:</strong> ${w.action}</div>` : ''}
                    ${w.decision ? `<div><strong style="color:#CBD5E1;">Decision:</strong> ${w.decision}</div>` : ''}
                    ${w.output ? `<div><strong style="color:#CBD5E1;">Output:</strong> ${w.output}</div>` : ''}
                </div>
            </div>
            <div style="display:flex; flex-direction:column; gap:4px; flex-shrink:0;">
                <div style="display:flex; gap:4px;">
                    <button type="button" class="btn btn-secondary btn-sm" onclick="moveWorkflowStep(${idx}, -1)" title="Pindah ke Atas" ${idx === 0 ? 'disabled style="opacity:0.4"' : ''}><i class="fa-solid fa-arrow-up"></i></button>
                    <button type="button" class="btn btn-secondary btn-sm" onclick="moveWorkflowStep(${idx}, 1)" title="Pindah ke Bawah" ${idx === projectPRD.workflows.length - 1 ? 'disabled style="opacity:0.4"' : ''}><i class="fa-solid fa-arrow-down"></i></button>
                </div>
                <div style="display:flex; gap:4px;">
                    <button type="button" class="btn btn-secondary btn-sm" onclick="editWorkflowStep('${w.id}')"><i class="fa-solid fa-pen-to-square"></i></button>
                    <button type="button" class="btn btn-rose btn-sm" onclick="deleteWorkflowStep('${w.id}')"><i class="fa-solid fa-trash-can"></i></button>
                </div>
            </div>
        `;
        container.appendChild(card);
    });

    updateUiMetadata();
}

function openWorkflowModal(wfId = null) {
    const titleEl = document.getElementById('modal-wf-title');
    const idInput = document.getElementById('modal-wf-id');
    const nameInput = document.getElementById('m-wf-name');
    const actorSelect = document.getElementById('m-wf-actor');
    const statusInput = document.getElementById('m-wf-status');
    const triggerInput = document.getElementById('m-wf-trigger');
    const inputInput = document.getElementById('m-wf-input');
    const actionInput = document.getElementById('m-wf-action');
    const decisionInput = document.getElementById('m-wf-decision');
    const outputInput = document.getElementById('m-wf-output');

    actorSelect.innerHTML = '<option value="">Pilih Aktor / Role</option>';
    projectPRD.roles.forEach(r => {
        const opt = document.createElement('option');
        opt.value = r.name;
        opt.textContent = r.name;
        actorSelect.appendChild(opt);
    });

    if (wfId) {
        const w = projectPRD.workflows.find(x => x.id === wfId);
        if (w) {
            titleEl.textContent = 'Edit Tahap Alur Kerja';
            idInput.value = w.id;
            nameInput.value = w.name;
            actorSelect.value = w.actor || '';
            statusInput.value = w.status || '';
            triggerInput.value = w.trigger || '';
            inputInput.value = w.input || '';
            actionInput.value = w.action || '';
            decisionInput.value = w.decision || '';
            outputInput.value = w.output || '';
        }
    } else {
        titleEl.textContent = 'Tambah Tahap Alur Kerja';
        idInput.value = '';
        nameInput.value = '';
        statusInput.value = '';
        triggerInput.value = '';
        inputInput.value = '';
        actionInput.value = '';
        decisionInput.value = '';
        outputInput.value = '';
    }

    openModal('modal-workflow');
}

function editWorkflowStep(id) { openWorkflowModal(id); }
function deleteWorkflowStep(id) {
    projectPRD.workflows = projectPRD.workflows.filter(w => w.id !== id);
    renderWorkflowNodes();
}
function moveWorkflowStep(idx, dir) {
    const targetIdx = idx + dir;
    if (targetIdx < 0 || targetIdx >= projectPRD.workflows.length) return;
    const temp = projectPRD.workflows[idx];
    projectPRD.workflows[idx] = projectPRD.workflows[targetIdx];
    projectPRD.workflows[targetIdx] = temp;
    renderWorkflowNodes();
}

function saveWorkflowModal() {
    const id = document.getElementById('modal-wf-id').value;
    const name = document.getElementById('m-wf-name').value.trim();
    const actor = document.getElementById('m-wf-actor').value;
    const status = document.getElementById('m-wf-status').value.trim();
    const trigger = document.getElementById('m-wf-trigger').value.trim();
    const inputVal = document.getElementById('m-wf-input').value.trim();
    const action = document.getElementById('m-wf-action').value.trim();
    const decision = document.getElementById('m-wf-decision').value.trim();
    const output = document.getElementById('m-wf-output').value.trim();

    if (!name) {
        Swal.fire({ icon: 'warning', title: 'Nama Tahap Wajib Diisi', background: '#0D111A', color: '#F8FAFC' });
        return;
    }

    if (id) {
        const w = projectPRD.workflows.find(x => x.id === id);
        if (w) {
            w.name = name;
            w.actor = actor;
            w.status = status;
            w.trigger = trigger;
            w.input = inputVal;
            w.action = action;
            w.decision = decision;
            w.output = output;
        }
    } else {
        projectPRD.workflows.push({
            id: 'wf_' + Date.now(),
            stepNo: projectPRD.workflows.length + 1,
            name: name,
            actor: actor,
            status: status,
            trigger: trigger,
            input: inputVal,
            action: action,
            decision: decision,
            output: output
        });
    }

    closeModal('modal-workflow');
    renderWorkflowNodes();
}

// ============================================================================
// STEP 6: BUSINESS RULES CONTROLLER
// ============================================================================
function renderBusinessRules() {
    const container = document.getElementById('rules-cards-container');
    if (!container) return;
    container.innerHTML = '';

    if (projectPRD.businessRules.length === 0) {
        container.innerHTML = `
            <div style="padding:40px 20px; text-align:center; color:#64748B; background:#080C14; border-radius:12px; border:1px dashed #1E293B;">
                <i class="fa-solid fa-gavel" style="font-size:32px; color:#334155; margin-bottom:10px;"></i>
                <div style="font-size:14px; font-weight:700; color:#E2E8FF;">Belum Ada Business Rules</div>
                <div style="font-size:11.5px; margin:4px 0 16px;">Tentukan aturan validasi logika bisnis untuk memastikan integritas data.</div>
                <button type="button" class="btn btn-primary btn-sm" onclick="openRuleModal()">
                    <i class="fa-solid fa-plus"></i> Tambah Rule
                </button>
            </div>
        `;
        return;
    }

    projectPRD.businessRules.forEach(r => {
        const card = document.createElement('div');
        card.className = 'card-box';
        card.style.marginBottom = '0';
        card.style.padding = '14px 18px';

        let sevBadge = 'badge-slate';
        if (r.severity === 'Blocking') sevBadge = 'badge-rose';
        else if (r.severity === 'Warning') sevBadge = 'badge-amber';
        else if (r.severity === 'Informational') sevBadge = 'badge-indigo';

        card.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px;">
                <div style="display:flex; align-items:center; gap:8px;">
                    <span class="badge ${sevBadge}">${r.severity || 'Blocking'}</span>
                    <span style="font-size:13.5px; font-weight:800; color:#FFFFFF;">${r.name}</span>
                </div>
                <div style="display:flex; gap:6px;">
                    <button type="button" class="btn btn-secondary btn-sm" onclick="editRule('${r.id}')"><i class="fa-solid fa-pen-to-square"></i></button>
                    <button type="button" class="btn btn-rose btn-sm" onclick="deleteRule('${r.id}')"><i class="fa-solid fa-trash-can"></i></button>
                </div>
            </div>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px; font-size:11.5px; margin-top:8px;">
                <div style="background:#07090E; border:1px solid #1E293B; border-radius:8px; padding:8px 12px;">
                    <div style="color:#F59E0B; font-weight:700; font-size:10.5px; text-transform:uppercase;">Kondisi (Condition):</div>
                    <div style="color:#CBD5E1; margin-top:2px;">${r.condition || '-'}</div>
                </div>
                <div style="background:#07090E; border:1px solid #1E293B; border-radius:8px; padding:8px 12px;">
                    <div style="color:#34D399; font-weight:700; font-size:10.5px; text-transform:uppercase;">Aksi Sistem (Action):</div>
                    <div style="color:#CBD5E1; margin-top:2px;">${r.action || '-'}</div>
                </div>
            </div>
            ${r.exception ? `<div style="font-size:11px; color:#94A3B8; margin-top:8px;"><strong style="color:#E2E8FF;">Pengecualian:</strong> ${r.exception}</div>` : ''}
        `;
        container.appendChild(card);
    });

    updateUiMetadata();
}

function openRuleModal(ruleId = null) {
    const titleEl = document.getElementById('modal-rule-title');
    const idInput = document.getElementById('modal-rule-id');
    const nameInput = document.getElementById('m-rule-name');
    const sevSelect = document.getElementById('m-rule-severity');
    const excInput = document.getElementById('m-rule-exception');
    const condInput = document.getElementById('m-rule-condition');
    const actInput = document.getElementById('m-rule-action');
    const descInput = document.getElementById('m-rule-desc');

    if (ruleId) {
        const r = projectPRD.businessRules.find(x => x.id === ruleId);
        if (r) {
            titleEl.textContent = 'Edit Business Rule';
            idInput.value = r.id;
            nameInput.value = r.name;
            sevSelect.value = r.severity || 'Blocking';
            excInput.value = r.exception || '';
            condInput.value = r.condition || '';
            actInput.value = r.action || '';
            descInput.value = r.description || '';
        }
    } else {
        titleEl.textContent = 'Tambah Business Rule';
        idInput.value = '';
        nameInput.value = '';
        sevSelect.value = 'Blocking';
        excInput.value = '';
        condInput.value = '';
        actInput.value = '';
        descInput.value = '';
    }

    openModal('modal-rule');
}

function editRule(id) { openRuleModal(id); }
function deleteRule(id) {
    projectPRD.businessRules = projectPRD.businessRules.filter(r => r.id !== id);
    renderBusinessRules();
}

function saveRuleModal() {
    const id = document.getElementById('modal-rule-id').value;
    const name = document.getElementById('m-rule-name').value.trim();
    const sev = document.getElementById('m-rule-severity').value;
    const exc = document.getElementById('m-rule-exception').value.trim();
    const cond = document.getElementById('m-rule-condition').value.trim();
    const act = document.getElementById('m-rule-action').value.trim();
    const desc = document.getElementById('m-rule-desc').value.trim();

    if (!name || !cond || !act) {
        Swal.fire({ icon: 'warning', title: 'Nama, Kondisi & Aksi Wajib Diisi', background: '#0D111A', color: '#F8FAFC' });
        return;
    }

    if (id) {
        const r = projectPRD.businessRules.find(x => x.id === id);
        if (r) {
            r.name = name;
            r.severity = sev;
            r.exception = exc;
            r.condition = cond;
            r.action = act;
            r.description = desc;
        }
    } else {
        projectPRD.businessRules.push({
            id: 'br_' + Date.now(),
            name: name,
            severity: sev,
            exception: exc,
            condition: cond,
            action: act,
            description: desc
        });
    }

    closeModal('modal-rule');
    renderBusinessRules();
}

// ============================================================================
// STEP 7: DATA MODEL (ENTITY BUILDER)
// ============================================================================
function renderEntities() {
    const container = document.getElementById('entities-cards-container');
    if (!container) return;
    container.innerHTML = '';

    if (projectPRD.entities.length === 0) {
        container.innerHTML = `
            <div style="padding:40px 20px; text-align:center; color:#64748B; background:#080C14; border-radius:12px; border:1px dashed #1E293B;">
                <i class="fa-solid fa-database" style="font-size:32px; color:#334155; margin-bottom:10px;"></i>
                <div style="font-size:14px; font-weight:700; color:#E2E8FF;">Belum Ada Entitas Data</div>
                <div style="font-size:11.5px; margin:4px 0 16px;">Bangun skema data model terstruktur untuk tabel dan relasi sistem.</div>
                <button type="button" class="btn btn-primary btn-sm" onclick="openEntityModal()">
                    <i class="fa-solid fa-plus"></i> Tambah Entitas Pertama
                </button>
            </div>
        `;
        return;
    }

    projectPRD.entities.forEach(ent => {
        const card = document.createElement('div');
        card.className = 'card-box';
        card.style.marginBottom = '0';
        card.style.padding = '16px 20px';

        let fieldsTableRows = '';
        (ent.fields || []).forEach(f => {
            fieldsTableRows += `
                <tr>
                    <td class="font-mono" style="color:#818CF8; font-weight:700;">${f.name}</td>
                    <td><span class="badge badge-indigo">${f.type}</span></td>
                    <td>${f.required === 'true' || f.required === true ? '<span style="color:#F43F5E; font-weight:700;">Wajib</span>' : '<span style="color:#94A3B8;">Opsional</span>'}</td>
                    <td class="font-mono" style="color:#94A3B8;">${f.defaultValue || '-'}</td>
                    <td>${f.validation || '-'}</td>
                    <td>${f.description || '-'}</td>
                    <td style="text-align:right;">
                        <button type="button" class="btn btn-rose btn-sm" onclick="deleteEntityField('${ent.id}', '${f.id}')" title="Hapus Field"><i class="fa-solid fa-xmark"></i></button>
                    </td>
                </tr>
            `;
        });

        let relationsHtml = '';
        if (ent.relationships && ent.relationships.length > 0) {
            relationsHtml = `
                <div style="margin-top:12px; padding-top:10px; border-top:1px solid #1E293B; display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
                    <span style="font-size:11px; font-weight:700; color:#94A3B8;">Relasi Entitas:</span>
                    ${ent.relationships.map(rel => `<span class="badge badge-emerald"><i class="fa-solid fa-link" style="margin-right:4px;"></i>${rel.relationType} &rarr; ${rel.targetEntity} (${rel.foreignKey || ''})</span>`).join('')}
                </div>
            `;
        }

        card.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px;">
                <div>
                    <div style="display:flex; align-items:center; gap:8px;">
                        <i class="fa-solid fa-table" style="color:#34D399; font-size:15px;"></i>
                        <span class="font-outfit" style="font-size:16px; font-weight:800; color:#FFFFFF;">${ent.name}</span>
                        <span class="badge badge-slate">${ent.type || 'Transactional'}</span>
                        <span class="font-mono" style="font-size:11px; color:#64748B;">storage: ${ent.storage || ent.name.toLowerCase()}</span>
                    </div>
                    <div style="font-size:11.5px; color:#94A3B8; margin-top:2px;">${ent.description || ''}</div>
                </div>
                <div style="display:flex; gap:6px;">
                    <button type="button" class="btn btn-primary btn-sm" onclick="openFieldModal('${ent.id}')">
                        <i class="fa-solid fa-plus"></i> Tambah Field
                    </button>
                    <button type="button" class="btn btn-secondary btn-sm" onclick="editEntity('${ent.id}')"><i class="fa-solid fa-pen-to-square"></i></button>
                    <button type="button" class="btn btn-rose btn-sm" onclick="deleteEntity('${ent.id}')"><i class="fa-solid fa-trash-can"></i></button>
                </div>
            </div>

            <div class="table-responsive">
                <table class="custom-table">
                    <thead>
                        <tr>
                            <th>Field Name</th>
                            <th>Data Type</th>
                            <th>Requirement</th>
                            <th>Default</th>
                            <th>Validation</th>
                            <th>Description</th>
                            <th style="width:40px;"></th>
                        </tr>
                    </thead>
                    <tbody>
                        ${fieldsTableRows || '<tr><td colspan="7" style="text-align:center; color:#64748B;">Belum ada field didefinisikan.</td></tr>'}
                    </tbody>
                </table>
            </div>
            ${relationsHtml}
        `;
        container.appendChild(card);
    });

    updateUiMetadata();
}

function openEntityModal(entId = null) {
    const titleEl = document.getElementById('modal-entity-title');
    const idInput = document.getElementById('modal-entity-id');
    const nameInput = document.getElementById('m-ent-name');
    const typeSelect = document.getElementById('m-ent-type');
    const storageInput = document.getElementById('m-ent-storage');
    const descInput = document.getElementById('m-ent-desc');

    if (entId) {
        const e = projectPRD.entities.find(x => x.id === entId);
        if (e) {
            titleEl.textContent = 'Edit Entitas Data';
            idInput.value = e.id;
            nameInput.value = e.name;
            typeSelect.value = e.type || 'Transactional';
            storageInput.value = e.storage || '';
            descInput.value = e.description || '';
        }
    } else {
        titleEl.textContent = 'Tambah Entitas Baru';
        idInput.value = '';
        nameInput.value = '';
        typeSelect.value = 'Transactional';
        storageInput.value = '';
        descInput.value = '';
    }

    openModal('modal-entity');
}

function editEntity(id) { openEntityModal(id); }
function deleteEntity(id) {
    projectPRD.entities = projectPRD.entities.filter(e => e.id !== id);
    renderEntities();
}

function saveEntityModal() {
    const id = document.getElementById('modal-entity-id').value;
    const name = document.getElementById('m-ent-name').value.trim();
    const type = document.getElementById('m-ent-type').value;
    const storage = document.getElementById('m-ent-storage').value.trim();
    const desc = document.getElementById('m-ent-desc').value.trim();

    if (!name) {
        Swal.fire({ icon: 'warning', title: 'Nama Entitas Wajib Diisi', background: '#0D111A', color: '#F8FAFC' });
        return;
    }

    if (id) {
        const e = projectPRD.entities.find(x => x.id === id);
        if (e) {
            e.name = name;
            e.type = type;
            e.storage = storage || name.toLowerCase();
            e.description = desc;
        }
    } else {
        projectPRD.entities.push({
            id: 'ent_' + Date.now(),
            name: name,
            type: type,
            storage: storage || name.toLowerCase(),
            description: desc,
            fields: [
                { id: 'f_' + Date.now(), name: 'id', type: 'String', required: 'true', defaultValue: 'UUID', validation: 'Primary Key', description: 'ID unik' }
            ],
            relationships: []
        });
    }

    closeModal('modal-entity');
    renderEntities();
}

// Field Modal Handlers
function openFieldModal(entityId) {
    document.getElementById('modal-field-entity-id').value = entityId;
    document.getElementById('m-fld-name').value = '';
    document.getElementById('m-fld-type').value = 'String';
    document.getElementById('m-fld-req').value = 'true';
    document.getElementById('m-fld-default').value = '';
    document.getElementById('m-fld-valid').value = '';
    document.getElementById('m-fld-desc').value = '';
    openModal('modal-field');
}

function deleteEntityField(entityId, fieldId) {
    const ent = projectPRD.entities.find(e => e.id === entityId);
    if (ent && ent.fields) {
        ent.fields = ent.fields.filter(f => f.id !== fieldId);
        renderEntities();
    }
}

function saveFieldModal() {
    const entityId = document.getElementById('modal-field-entity-id').value;
    const name = document.getElementById('m-fld-name').value.trim();
    const type = document.getElementById('m-fld-type').value;
    const req = document.getElementById('m-fld-req').value;
    const def = document.getElementById('m-fld-default').value.trim();
    const valid = document.getElementById('m-fld-valid').value.trim();
    const desc = document.getElementById('m-fld-desc').value.trim();

    if (!name) {
        Swal.fire({ icon: 'warning', title: 'Nama Field Wajib Diisi', background: '#0D111A', color: '#F8FAFC' });
        return;
    }

    const ent = projectPRD.entities.find(e => e.id === entityId);
    if (ent) {
        if (!ent.fields) ent.fields = [];
        ent.fields.push({
            id: 'fld_' + Date.now(),
            name: name,
            type: type,
            required: req,
            defaultValue: def,
            validation: valid,
            description: desc
        });
    }

    closeModal('modal-field');
    renderEntities();
}

// ============================================================================
// STEP 8: PERMISSIONS / RBAC MATRIX CONTROLLER
// ============================================================================
const RBAC_ACTIONS = ['view', 'create', 'edit', 'delete', 'approve', 'release', 'execute', 'verify', 'close', 'export'];

function initDefaultRbacMatrix() {
    projectPRD.permissions = {};
    const roles = projectPRD.roles.length > 0 ? projectPRD.roles : [{ id: 'r1', name: 'User' }];
    const modules = projectPRD.modules.length > 0 ? projectPRD.modules : [{ id: 'm1', name: 'Core System' }];

    roles.forEach(r => {
        modules.forEach(m => {
            const key = `${r.name}_${m.name}`;
            const isLeadOrManager = r.name.toLowerCase().includes('manager') || r.name.toLowerCase().includes('supervisor') || r.name.toLowerCase().includes('planner');
            projectPRD.permissions[key] = {
                view: true,
                create: isLeadOrManager,
                edit: isLeadOrManager,
                delete: r.name.toLowerCase().includes('manager'),
                approve: r.name.toLowerCase().includes('supervisor') || r.name.toLowerCase().includes('manager'),
                release: r.name.toLowerCase().includes('supervisor') || r.name.toLowerCase().includes('planner'),
                execute: r.name.toLowerCase().includes('mechanic') || r.name.toLowerCase().includes('buyer'),
                verify: r.name.toLowerCase().includes('supervisor') || r.name.toLowerCase().includes('surveyor'),
                close: r.name.toLowerCase().includes('manager') || r.name.toLowerCase().includes('planner'),
                export: true
            };
        });
    });
}

function renderRbacMatrix() {
    const table = document.getElementById('rbac-matrix-table');
    if (!table) return;

    const roles = projectPRD.roles.length > 0 ? projectPRD.roles : [{ id: 'r1', name: 'Standard User' }];
    const modules = projectPRD.modules.length > 0 ? projectPRD.modules : [{ id: 'm1', name: 'General Module' }];

    let thead = `
        <thead>
            <tr>
                <th style="min-width:180px;">Modul / Fitur</th>
                <th style="min-width:160px;">Role Pengguna</th>
                ${RBAC_ACTIONS.map(a => `<th style="text-align:center; text-transform:uppercase; font-size:10.5px;">${a}</th>`).join('')}
            </tr>
        </thead>
    `;

    let tbody = `<tbody>`;

    modules.forEach(m => {
        roles.forEach((r, rIdx) => {
            const permKey = `${r.name}_${m.name}`;
            if (projectPRD.roles.length > 0 && projectPRD.modules.length > 0) {
                if (!projectPRD.permissions[permKey]) {
                    projectPRD.permissions[permKey] = { view: true };
                }
            }
            const p = projectPRD.permissions[permKey] || { view: true };

            tbody += `
                <tr>
                    ${rIdx === 0 ? `<td rowspan="${roles.length}" style="font-weight:800; color:#FFFFFF; background:#0D111A; vertical-align:top; border-right:1px solid #1E293B;"><i class="fa-solid fa-folder" style="color:#818CF8; margin-right:6px;"></i>${m.name}</td>` : ''}
                    <td style="font-weight:700; color:#CBD5E1;">${r.name}</td>
                    ${RBAC_ACTIONS.map(act => {
                        const isChecked = p[act] ? 'checked' : '';
                        return `
                            <td style="text-align:center;">
                                <input type="checkbox" style="accent-color:#6366F1; cursor:pointer;" ${isChecked} onchange="toggleRbacPermission('${r.name}', '${m.name}', '${act}', this.checked)">
                            </td>
                        `;
                    }).join('')}
                </tr>
            `;
        });
    });

    tbody += `</tbody>`;
    table.innerHTML = thead + tbody;
}

function toggleRbacPermission(roleName, modName, action, value) {
    const key = `${roleName}_${modName}`;
    if (!projectPRD.permissions[key]) {
        projectPRD.permissions[key] = {};
    }
    projectPRD.permissions[key][action] = value;
}

function grantAllPermissions() {
    const roles = projectPRD.roles.length > 0 ? projectPRD.roles : [{ name: 'User' }];
    const modules = projectPRD.modules.length > 0 ? projectPRD.modules : [{ name: 'Core' }];
    roles.forEach(r => {
        modules.forEach(m => {
            const key = `${r.name}_${m.name}`;
            if (!projectPRD.permissions[key]) projectPRD.permissions[key] = {};
            RBAC_ACTIONS.forEach(act => projectPRD.permissions[key][act] = true);
        });
    });
    renderRbacMatrix();
}

function clearAllPermissions() {
    const roles = projectPRD.roles.length > 0 ? projectPRD.roles : [{ name: 'User' }];
    const modules = projectPRD.modules.length > 0 ? projectPRD.modules : [{ name: 'Core' }];
    roles.forEach(r => {
        modules.forEach(m => {
            const key = `${r.name}_${m.name}`;
            if (!projectPRD.permissions[key]) projectPRD.permissions[key] = {};
            RBAC_ACTIONS.forEach(act => projectPRD.permissions[key][act] = false);
        });
    });
    renderRbacMatrix();
}

// ============================================================================
// STEP 9: KPI & REPORTING CONTROLLER
// ============================================================================
function renderKpis() {
    const container = document.getElementById('kpis-cards-container');
    if (!container) return;
    container.innerHTML = '';

    if (projectPRD.kpis.length === 0) {
        container.innerHTML = `
            <div style="grid-column:1/-1; padding:40px 20px; text-align:center; color:#64748B; background:#080C14; border-radius:12px; border:1px dashed #1E293B;">
                <i class="fa-solid fa-chart-line" style="font-size:32px; color:#334155; margin-bottom:10px;"></i>
                <div style="font-size:14px; font-weight:700; color:#E2E8FF;">Belum Ada Metrik KPI</div>
                <div style="font-size:11.5px; margin:4px 0 16px;">Tentukan tolok ukur kesuksesan operasional produk Anda.</div>
                <button type="button" class="btn btn-primary btn-sm" onclick="openKpiModal()">
                    <i class="fa-solid fa-plus"></i> Tambah KPI
                </button>
            </div>
        `;
        return;
    }

    projectPRD.kpis.forEach(k => {
        const card = document.createElement('div');
        card.className = 'card-box';
        card.style.marginBottom = '0';
        card.style.padding = '14px 16px';
        card.style.display = 'flex';
        card.style.flexDirection = 'column';
        card.style.justifyContent = 'space-between';

        card.innerHTML = `
            <div>
                <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
                    <div style="font-size:13.5px; font-weight:800; color:#FFFFFF;">${k.name}</div>
                    <span class="badge badge-emerald">${k.target} ${k.unit || ''}</span>
                </div>
                <div style="font-size:11px; color:#94A3B8; line-height:1.4; margin-bottom:8px;">${k.description || ''}</div>
                <div style="background:#07090E; border:1px solid #1E293B; border-radius:8px; padding:8px 10px; font-size:11px; font-family:'JetBrains Mono',monospace; color:#818CF8; margin-bottom:8px;">
                    ${k.formula || 'Formula terstandar'}
                </div>
                <div style="display:flex; justify-content:space-between; font-size:10.5px; color:#64748B;">
                    <span>Freq: <strong style="color:#CBD5E1;">${k.frequency || 'Harian'}</strong></span>
                    <span>Vis: <strong style="color:#CBD5E1;">${k.visualization || 'Card'}</strong></span>
                </div>
            </div>
            <div style="display:flex; justify-content:flex-end; gap:6px; margin-top:12px; padding-top:8px; border-top:1px solid var(--border-color);">
                <button type="button" class="btn btn-secondary btn-sm" onclick="editKpi('${k.id}')"><i class="fa-solid fa-pen-to-square"></i></button>
                <button type="button" class="btn btn-rose btn-sm" onclick="deleteKpi('${k.id}')"><i class="fa-solid fa-trash-can"></i></button>
            </div>
        `;
        container.appendChild(card);
    });

    updateUiMetadata();
}

function openKpiModal(kpiId = null) {
    const titleEl = document.getElementById('modal-kpi-title');
    const idInput = document.getElementById('modal-kpi-id');
    const nameInput = document.getElementById('m-kpi-name');
    const targetInput = document.getElementById('m-kpi-target');
    const unitInput = document.getElementById('m-kpi-unit');
    const formInput = document.getElementById('m-kpi-formula');
    const sourceInput = document.getElementById('m-kpi-source');
    const freqSelect = document.getElementById('m-kpi-freq');
    const visSelect = document.getElementById('m-kpi-vis');
    const descInput = document.getElementById('m-kpi-desc');

    if (kpiId) {
        const k = projectPRD.kpis.find(x => x.id === kpiId);
        if (k) {
            titleEl.textContent = 'Edit Metrik KPI';
            idInput.value = k.id;
            nameInput.value = k.name;
            targetInput.value = k.target || '';
            unitInput.value = k.unit || '';
            formInput.value = k.formula || '';
            sourceInput.value = k.source || '';
            freqSelect.value = k.frequency || 'Harian';
            visSelect.value = k.visualization || 'Stat Card';
            descInput.value = k.description || '';
        }
    } else {
        titleEl.textContent = 'Tambah Metrik KPI';
        idInput.value = '';
        nameInput.value = '';
        targetInput.value = '';
        unitInput.value = '';
        formInput.value = '';
        sourceInput.value = '';
        freqSelect.value = 'Harian';
        visSelect.value = 'Stat Card';
        descInput.value = '';
    }

    openModal('modal-kpi');
}

function editKpi(id) { openKpiModal(id); }
function deleteKpi(id) {
    projectPRD.kpis = projectPRD.kpis.filter(k => k.id !== id);
    renderKpis();
}

function saveKpiModal() {
    const id = document.getElementById('modal-kpi-id').value;
    const name = document.getElementById('m-kpi-name').value.trim();
    const target = document.getElementById('m-kpi-target').value.trim();
    const unit = document.getElementById('m-kpi-unit').value.trim();
    const formula = document.getElementById('m-kpi-formula').value.trim();
    const source = document.getElementById('m-kpi-source').value.trim();
    const freq = document.getElementById('m-kpi-freq').value;
    const vis = document.getElementById('m-kpi-vis').value;
    const desc = document.getElementById('m-kpi-desc').value.trim();

    if (!name || !target) {
        Swal.fire({ icon: 'warning', title: 'Nama KPI & Target Wajib Diisi', background: '#0D111A', color: '#F8FAFC' });
        return;
    }

    if (id) {
        const k = projectPRD.kpis.find(x => x.id === id);
        if (k) {
            k.name = name;
            k.target = target;
            k.unit = unit;
            k.formula = formula;
            k.source = source;
            k.frequency = freq;
            k.visualization = vis;
            k.description = desc;
        }
    } else {
        projectPRD.kpis.push({
            id: 'kpi_' + Date.now(),
            name: name,
            target: target,
            unit: unit,
            formula: formula,
            source: source,
            frequency: freq,
            visualization: vis,
            description: desc
        });
    }

    closeModal('modal-kpi');
    renderKpis();
}

// ============================================================================
// STEP 10: NOTIFICATION CONTROLLER
// ============================================================================
function renderNotifications() {
    const container = document.getElementById('notifications-cards-container');
    if (!container) return;
    container.innerHTML = '';

    if (projectPRD.notifications.length === 0) {
        container.innerHTML = `
            <div style="grid-column:1/-1; padding:40px 20px; text-align:center; color:#64748B; background:#080C14; border-radius:12px; border:1px dashed #1E293B;">
                <i class="fa-solid fa-bell" style="font-size:32px; color:#334155; margin-bottom:10px;"></i>
                <div style="font-size:14px; font-weight:700; color:#E2E8FF;">Belum Ada Notifikasi</div>
                <div style="font-size:11.5px; margin:4px 0 16px;">Tentukan protokol peringatan dini dan eskalasi otomatis.</div>
                <button type="button" class="btn btn-primary btn-sm" onclick="openNotificationModal()">
                    <i class="fa-solid fa-plus"></i> Tambah Notifikasi
                </button>
            </div>
        `;
        return;
    }

    projectPRD.notifications.forEach(n => {
        const card = document.createElement('div');
        card.className = 'card-box';
        card.style.marginBottom = '0';
        card.style.padding = '14px 16px';

        let pBadge = 'badge-slate';
        if (n.priority && n.priority.includes('P1')) pBadge = 'badge-rose';
        else if (n.priority && n.priority.includes('P2')) pBadge = 'badge-amber';
        else pBadge = 'badge-indigo';

        card.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
                <div>
                    <div style="display:flex; align-items:center; gap:8px;">
                        <span class="badge ${pBadge}">${n.priority || 'P2'}</span>
                        <span style="font-size:13.5px; font-weight:800; color:#FFFFFF;">${n.name}</span>
                    </div>
                    <div style="font-size:11px; color:#34D399; margin-top:2px;">
                        <i class="fa-solid fa-user-tag" style="margin-right:4px;"></i>Penerima: <strong>${n.recipient || 'Semua Role'}</strong>
                    </div>
                </div>
                <span class="badge badge-cyan">${n.channel || 'In-App'}</span>
            </div>
            ${n.trigger ? `<div style="font-size:11.5px; color:#94A3B8; margin:6px 0;"><strong style="color:#CBD5E1;">Trigger:</strong> ${n.trigger}</div>` : ''}
            ${n.template ? `<div style="background:#07090E; border:1px solid #1E293B; border-radius:8px; padding:8px 12px; font-size:11px; color:#CBD5E1; font-family:'JetBrains Mono',monospace; margin-bottom:6px;">${n.template}</div>` : ''}
            ${n.escalation ? `<div style="font-size:10.5px; color:#F59E0B;"><i class="fa-solid fa-triangle-exclamation" style="margin-right:4px;"></i>Eskalasi: ${n.escalation}</div>` : ''}
            <div style="display:flex; justify-content:flex-end; gap:6px; margin-top:10px; padding-top:6px; border-top:1px solid var(--border-color);">
                <button type="button" class="btn btn-secondary btn-sm" onclick="editNotification('${n.id}')"><i class="fa-solid fa-pen-to-square"></i></button>
                <button type="button" class="btn btn-rose btn-sm" onclick="deleteNotification('${n.id}')"><i class="fa-solid fa-trash-can"></i></button>
            </div>
        `;
        container.appendChild(card);
    });

    updateUiMetadata();
}

function openNotificationModal(notifId = null) {
    const titleEl = document.getElementById('modal-notif-title');
    const idInput = document.getElementById('modal-notif-id');
    const nameInput = document.getElementById('m-notif-name');
    const recipSelect = document.getElementById('m-notif-recipient');
    const chanSelect = document.getElementById('m-notif-channel');
    const prioSelect = document.getElementById('m-notif-priority');
    const escInput = document.getElementById('m-notif-escala');
    const msgInput = document.getElementById('m-notif-msg');

    recipSelect.innerHTML = '<option value="">Semua Role / Petugas Terkait</option>';
    projectPRD.roles.forEach(r => {
        const opt = document.createElement('option');
        opt.value = r.name;
        opt.textContent = r.name;
        recipSelect.appendChild(opt);
    });

    if (notifId) {
        const n = projectPRD.notifications.find(x => x.id === notifId);
        if (n) {
            titleEl.textContent = 'Edit Notifikasi';
            idInput.value = n.id;
            nameInput.value = n.name;
            recipSelect.value = n.recipient || '';
            chanSelect.value = n.channel || 'In-App Toast';
            prioSelect.value = n.priority || 'P2 High';
            escInput.value = n.escalation || '';
            msgInput.value = n.template || '';
        }
    } else {
        titleEl.textContent = 'Tambah Notifikasi';
        idInput.value = '';
        nameInput.value = '';
        chanSelect.value = 'In-App Toast';
        prioSelect.value = 'P2 High';
        escInput.value = '';
        msgInput.value = '';
    }

    openModal('modal-notification');
}

function editNotification(id) { openNotificationModal(id); }
function deleteNotification(id) {
    projectPRD.notifications = projectPRD.notifications.filter(n => n.id !== id);
    renderNotifications();
}

function saveNotificationModal() {
    const id = document.getElementById('modal-notif-id').value;
    const name = document.getElementById('m-notif-name').value.trim();
    const recipient = document.getElementById('m-notif-recipient').value;
    const channel = document.getElementById('m-notif-channel').value;
    const priority = document.getElementById('m-notif-priority').value;
    const escalation = document.getElementById('m-notif-escala').value.trim();
    const template = document.getElementById('m-notif-msg').value.trim();

    if (!name) {
        Swal.fire({ icon: 'warning', title: 'Nama Event Pemicu Wajib Diisi', background: '#0D111A', color: '#F8FAFC' });
        return;
    }

    if (id) {
        const n = projectPRD.notifications.find(x => x.id === id);
        if (n) {
            n.name = name;
            n.recipient = recipient;
            n.channel = channel;
            n.priority = priority;
            n.escalation = escalation;
            n.template = template;
        }
    } else {
        projectPRD.notifications.push({
            id: 'notif_' + Date.now(),
            name: name,
            recipient: recipient,
            channel: channel,
            priority: priority,
            escalation: escalation,
            template: template
        });
    }

    closeModal('modal-notification');
    renderNotifications();
}

// ============================================================================
// STEP 11: INTEGRATION CONTROLLER
// ============================================================================
function renderIntegrations() {
    const container = document.getElementById('integrations-cards-container');
    if (!container) return;
    container.innerHTML = '';

    if (projectPRD.integrations.length === 0) {
        container.innerHTML = `
            <div style="grid-column:1/-1; padding:40px 20px; text-align:center; color:#64748B; background:#080C14; border-radius:12px; border:1px dashed #1E293B;">
                <i class="fa-solid fa-network-wired" style="font-size:32px; color:#334155; margin-bottom:10px;"></i>
                <div style="font-size:14px; font-weight:700; color:#E2E8FF;">Belum Ada Integrasi Eksternal</div>
                <div style="font-size:11.5px; margin:4px 0 16px;">Tentukan sistem eksternal yang terhubung ke arsitektur produk.</div>
                <button type="button" class="btn btn-primary btn-sm" onclick="openIntegrationModal()">
                    <i class="fa-solid fa-plus"></i> Tambah Integrasi
                </button>
            </div>
        `;
        return;
    }

    projectPRD.integrations.forEach(i => {
        const card = document.createElement('div');
        card.className = 'card-box';
        card.style.marginBottom = '0';
        card.style.padding = '14px 16px';

        card.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
                <div>
                    <div style="font-size:13.5px; font-weight:800; color:#FFFFFF;">${i.system}</div>
                    <div style="font-size:11px; color:#818CF8; margin-top:2px;">
                        <i class="fa-solid fa-arrows-turn-to-dots" style="margin-right:4px;"></i>${i.direction || 'Bi-directional'} &bull; ${i.frequency || 'Real-time'}
                    </div>
                </div>
                <span class="badge badge-emerald">${i.auth || 'REST API'}</span>
            </div>
            <div style="font-size:11.5px; color:#94A3B8; margin:6px 0;"><strong>Tujuan:</strong> ${i.purpose || '-'}</div>
            ${i.data ? `<div style="font-size:11px; color:#CBD5E1; font-family:'JetBrains Mono',monospace; background:#07090E; padding:6px 10px; border-radius:6px; margin-bottom:6px;">Payload: ${i.data}</div>` : ''}
            ${i.mockNotes ? `<div style="font-size:10.5px; color:#F59E0B;"><i class="fa-solid fa-code" style="margin-right:4px;"></i>Simulasi MVP: ${i.mockNotes}</div>` : ''}
            <div style="display:flex; justify-content:flex-end; gap:6px; margin-top:10px; padding-top:6px; border-top:1px solid var(--border-color);">
                <button type="button" class="btn btn-secondary btn-sm" onclick="editIntegration('${i.id}')"><i class="fa-solid fa-pen-to-square"></i></button>
                <button type="button" class="btn btn-rose btn-sm" onclick="deleteIntegration('${i.id}')"><i class="fa-solid fa-trash-can"></i></button>
            </div>
        `;
        container.appendChild(card);
    });

    updateUiMetadata();
}

function openIntegrationModal(integId = null) {
    const titleEl = document.getElementById('modal-integ-title');
    const idInput = document.getElementById('modal-integ-id');
    const sysInput = document.getElementById('m-integ-system');
    const dirSelect = document.getElementById('m-integ-dir');
    const freqSelect = document.getElementById('m-integ-freq');
    const purpInput = document.getElementById('m-integ-purpose');
    const dataInput = document.getElementById('m-integ-data');
    const authInput = document.getElementById('m-integ-auth');
    const mockInput = document.getElementById('m-integ-mock');

    if (integId) {
        const i = projectPRD.integrations.find(x => x.id === integId);
        if (i) {
            titleEl.textContent = 'Edit Integrasi Sistem';
            idInput.value = i.id;
            sysInput.value = i.system;
            dirSelect.value = i.direction || 'Inbound';
            freqSelect.value = i.frequency || 'Real-time Webhook';
            purpInput.value = i.purpose || '';
            dataInput.value = i.data || '';
            authInput.value = i.auth || '';
            mockInput.value = i.mockNotes || '';
        }
    } else {
        titleEl.textContent = 'Tambah Integrasi Sistem';
        idInput.value = '';
        sysInput.value = '';
        dirSelect.value = 'Inbound';
        freqSelect.value = 'Real-time Webhook';
        purpInput.value = '';
        dataInput.value = '';
        authInput.value = '';
        mockInput.value = '';
    }

    openModal('modal-integration');
}

function editIntegration(id) { openIntegrationModal(id); }
function deleteIntegration(id) {
    projectPRD.integrations = projectPRD.integrations.filter(i => i.id !== id);
    renderIntegrations();
}

function saveIntegrationModal() {
    const id = document.getElementById('modal-integ-id').value;
    const system = document.getElementById('m-integ-system').value.trim();
    const dir = document.getElementById('m-integ-dir').value;
    const freq = document.getElementById('m-integ-freq').value;
    const purpose = document.getElementById('m-integ-purpose').value.trim();
    const data = document.getElementById('m-integ-data').value.trim();
    const auth = document.getElementById('m-integ-auth').value.trim();
    const mock = document.getElementById('m-integ-mock').value.trim();

    if (!system) {
        Swal.fire({ icon: 'warning', title: 'Nama Sistem Wajib Diisi', background: '#0D111A', color: '#F8FAFC' });
        return;
    }

    if (id) {
        const i = projectPRD.integrations.find(x => x.id === id);
        if (i) {
            i.system = system;
            i.direction = dir;
            i.frequency = freq;
            i.purpose = purpose;
            i.data = data;
            i.auth = auth;
            i.mockNotes = mock;
        }
    } else {
        projectPRD.integrations.push({
            id: 'integ_' + Date.now(),
            system: system,
            direction: dir,
            frequency: freq,
            purpose: purpose,
            data: data,
            auth: auth,
            mockNotes: mock
        });
    }

    closeModal('modal-integration');
    renderIntegrations();
}

// ============================================================================
// STEP 12: UI/UX ARCHITECTURE & 60 THEMES
// ============================================================================
function initThemeCatalogUI() {
    renderThemeCategoryFilters();
    renderThemeGrid();
}

function renderThemeCategoryFilters() {
    const container = document.getElementById('theme-category-filters');
    if (!container || typeof MOCK_DB === 'undefined') return;
    container.innerHTML = '';

    MOCK_DB.categories.forEach(cat => {
        const btn = document.createElement('button');
        btn.type = 'button';
        const isActive = cat.type === activeThemeCat;
        btn.className = 'btn btn-secondary btn-sm' + (isActive ? ' btn-primary' : '');
        btn.textContent = `${cat.name} (${cat.count})`;
        btn.onclick = () => {
            activeThemeCat = cat.type;
            renderThemeCategoryFilters();
            renderThemeGrid();
        };
        container.appendChild(btn);
    });
}

function filterThemeCards(query) {
    currentThemeQuery = (query || '').toLowerCase().trim();
    renderThemeGrid();
}

function renderThemeGrid() {
    const container = document.getElementById('themes-grid-container');
    if (!container || typeof MOCK_DB === 'undefined') return;
    container.innerHTML = '';

    let list = MOCK_DB.styles || [];
    if (activeThemeCat !== 'all') {
        list = list.filter(s => String(s.type).toLowerCase() === activeThemeCat.toLowerCase());
    }
    if (currentThemeQuery) {
        list = list.filter(s => s.name.toLowerCase().includes(currentThemeQuery) || s.desc.toLowerCase().includes(currentThemeQuery));
    }

    list.forEach(st => {
        const isSelected = st.id === projectPRD.uiux.themeId;
        const card = document.createElement('div');
        card.className = 'theme-card' + (isSelected ? ' selected' : '');
        card.onclick = () => selectTheme(st.id);

        let svgSrc = '';
        if (typeof generateArtisanSvg === 'function') {
            svgSrc = generateArtisanSvg(st);
        }

        const cols = (st.color || '6366f1,a855f7').split(',');
        const c1 = '#' + (cols[0] || '6366f1');
        const c2 = '#' + (cols[1] || 'a855f7');

        card.innerHTML = `
            <div style="height:90px; border-radius:8px; overflow:hidden; margin-bottom:8px; background:#07090E; border:1px solid rgba(255,255,255,0.06);">
                <img src="${svgSrc}" alt="${st.name}" style="width:100%; height:100%; object-fit:cover; display:block;" loading="lazy">
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <div style="font-size:12px; font-weight:800; color:#FFFFFF;">${st.name}</div>
                <div style="display:flex; gap:3px;">
                    <span style="width:8px; height:8px; border-radius:50%; background:${c1}; display:inline-block;"></span>
                    <span style="width:8px; height:8px; border-radius:50%; background:${c2}; display:inline-block;"></span>
                </div>
            </div>
            <div style="font-size:10.5px; color:#94A3B8; line-height:1.3; height:28px; overflow:hidden; text-overflow:ellipsis; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical;">${st.desc}</div>
        `;
        container.appendChild(card);
    });
}

function selectTheme(themeId) {
    projectPRD.uiux.themeId = themeId;
    const styleObj = (typeof MOCK_DB !== 'undefined') ? MOCK_DB.styles.find(s => s.id === themeId) : null;
    if (styleObj) {
        projectPRD.uiux.themeName = styleObj.name;
        const nameEl = document.getElementById('active-theme-name');
        const swatchEl = document.getElementById('active-theme-swatch');
        if (nameEl) nameEl.textContent = `${styleObj.name} (${styleObj.type.toUpperCase()})`;
        if (swatchEl) {
            const cols = styleObj.color.split(',');
            swatchEl.style.background = `linear-gradient(135deg, #${cols[0] || '6366f1'}, #${cols[1] || '3b82f6'})`;
        }
    }
    renderThemeGrid();
    updateUiMetadata();
}

function updateUiLayout(val) { projectPRD.uiux.layout = val; }
function updateUiNav(val) { projectPRD.uiux.navigation = val; }
function updateUiA11y(val) { projectPRD.uiux.accessibility = val; }

// Screens Mapping Handlers
function renderScreens() {
    const container = document.getElementById('screens-cards-container');
    if (!container) return;
    container.innerHTML = '';

    if (projectPRD.uiux.screens.length === 0) {
        container.innerHTML = `<div style="grid-column:1/-1; font-size:11.5px; color:#64748B; font-style:italic;">Belum ada screen dipetakan. Klik "Tambah Screen".</div>`;
        return;
    }

    projectPRD.uiux.screens.forEach(sc => {
        const card = document.createElement('div');
        card.className = 'card-box';
        card.style.marginBottom = '0';
        card.style.padding = '12px 14px';

        card.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:4px;">
                <div style="font-size:12.5px; font-weight:800; color:#FFFFFF;"><i class="fa-solid fa-window-maximize" style="color:#818CF8; margin-right:6px;"></i>${sc.name}</div>
                <button type="button" class="btn btn-rose btn-sm" style="padding:2px 6px;" onclick="deleteScreen('${sc.id}')"><i class="fa-solid fa-xmark"></i></button>
            </div>
            ${sc.features ? `<div style="font-size:11px; color:#34D399; margin-bottom:4px;">Fitur: ${sc.features}</div>` : ''}
            ${sc.components ? `<div style="font-size:10.5px; color:#94A3B8;">Komponen: ${sc.components}</div>` : ''}
        `;
        container.appendChild(card);
    });

    updateUiMetadata();
}

function openScreenModal() {
    document.getElementById('modal-screen-id').value = '';
    document.getElementById('m-screen-name').value = '';
    document.getElementById('m-screen-features').value = '';
    document.getElementById('m-screen-components').value = '';
    openModal('modal-screen');
}

function deleteScreen(id) {
    projectPRD.uiux.screens = projectPRD.uiux.screens.filter(s => s.id !== id);
    renderScreens();
}

function saveScreenModal() {
    const name = document.getElementById('m-screen-name').value.trim();
    const feats = document.getElementById('m-screen-features').value.trim();
    const comps = document.getElementById('m-screen-components').value.trim();

    if (!name) {
        Swal.fire({ icon: 'warning', title: 'Nama Screen Wajib Diisi', background: '#0D111A', color: '#F8FAFC' });
        return;
    }

    projectPRD.uiux.screens.push({
        id: 'scr_' + Date.now(),
        name: name,
        features: feats,
        components: comps
    });

    closeModal('modal-screen');
    renderScreens();
}

// ============================================================================
// STEP 14: PRD COMPLETENESS CHECKER
// ============================================================================
function checkCompleteness() {
    const p = projectPRD;
    const checks = [
        { step: 1, name: 'Project Definition', pass: Boolean(p.project.name && p.project.problem && p.project.objective), weight: 10, detail: p.project.name ? p.project.name : 'Nama / problem belum diisi' },
        { step: 2, name: '5 Pilar Arsitektur', pass: Boolean(p.taxonomy.pillar), weight: 10, detail: p.taxonomy.pillar ? getPillarName(p.taxonomy.pillar) : 'Pilih 1 Pilar Arsitektur' },
        { step: 3, name: 'Users & Roles', pass: p.roles.length >= 2, weight: 10, detail: `${p.roles.length} Role didefinisikan (Min. 2)` },
        { step: 4, name: 'Modules & Features', pass: p.modules.length >= 1 && p.features.length >= 2, weight: 10, detail: `${p.modules.length} Modul, ${p.features.length} Fitur (Min. 2 fitur)` },
        { step: 5, name: 'Process & Workflow', pass: p.workflows.length >= 3, weight: 10, detail: `${p.workflows.length} Tahap alur kerja (Min. 3)` },
        { step: 6, name: 'Business Rules', pass: p.businessRules.length >= 1, weight: 10, detail: `${p.businessRules.length} Aturan bisnis terdaftar` },
        { step: 7, name: 'Data Model (Entities)', pass: p.entities.length >= 1, weight: 10, detail: `${p.entities.length} Entitas data terstruktur` },
        { step: 8, name: 'Permissions / RBAC', pass: Object.keys(p.permissions).length > 0, weight: 5, detail: 'Matriks hak akses terkonfigurasi' },
        { step: 9, name: 'KPI & Reporting', pass: p.kpis.length >= 1, weight: 5, detail: `${p.kpis.length} Metrik KPI terukur` },
        { step: 10, name: 'Notification Protocols', pass: p.notifications.length >= 1, weight: 5, detail: `${p.notifications.length} Protokol alert` },
        { step: 11, name: 'Integration Requirements', pass: p.integrations.length >= 1, weight: 5, detail: `${p.integrations.length} Sistem eksternal terhubung` },
        { step: 12, name: 'UI/UX Architecture', pass: Boolean(p.uiux.themeId && p.uiux.screens.length >= 1), weight: 5, detail: `Style #${p.uiux.themeId}, ${p.uiux.screens.length} Screens` },
        { step: 13, name: 'Technical MVP Spec', pass: Boolean(p.technicalMVP.deployment && p.project.name), weight: 5, detail: 'Single-file index.html target' }
    ];

    let totalScore = 0;
    let warnings = [];

    const grid = document.getElementById('completeness-checklist-grid');
    if (grid) grid.innerHTML = '';

    checks.forEach(c => {
        if (c.pass) totalScore += c.weight;
        else warnings.push(`Seksi ${c.step} (${c.name}): ${c.detail}`);

        // Update sidebar icon badge
        const b = document.getElementById(`badge-step-${c.step}`);
        if (b) {
            b.classList.remove('done', 'warn');
            if (c.pass) {
                b.classList.add('done');
                b.innerHTML = '<i class="fa-solid fa-check" style="font-size:10px;"></i>';
            } else {
                b.classList.add('warn');
                b.textContent = c.step;
            }
        }

        if (grid) {
            const item = document.createElement('div');
            item.className = 'card-box';
            item.style.marginBottom = '0';
            item.style.padding = '12px 14px';
            item.style.display = 'flex';
            item.style.alignItems = 'center';
            item.style.justifyContent = 'space-between';

            const statusIcon = c.pass
                ? '<i class="fa-solid fa-circle-check" style="color:#10B981; font-size:18px;"></i>'
                : '<i class="fa-solid fa-triangle-exclamation" style="color:#F59E0B; font-size:18px;"></i>';

            item.innerHTML = `
                <div style="display:flex; align-items:center; gap:12px;">
                    ${statusIcon}
                    <div>
                        <div style="font-size:12.5px; font-weight:800; color:#FFFFFF;">${c.step}. ${c.name}</div>
                        <div style="font-size:11px; color:#94A3B8;">${c.detail}</div>
                    </div>
                </div>
                <button type="button" class="btn btn-secondary btn-sm" onclick="goToStep(${c.step})">Buka</button>
            `;
            grid.appendChild(item);
        }
    });

    const scoreDisplay = document.getElementById('checker-score-display');
    const topScore = document.getElementById('top-completeness-score');
    const topBar = document.getElementById('top-completeness-bar');

    if (scoreDisplay) scoreDisplay.textContent = `${totalScore}%`;
    if (topScore) topScore.textContent = `${totalScore}%`;
    if (topBar) topBar.style.width = `${totalScore}%`;

    const warnBox = document.getElementById('checker-warnings-box');
    if (warnBox) {
        if (warnings.length === 0) {
            warnBox.innerHTML = `
                <div style="background:rgba(16,185,129,0.12); border:1px solid rgba(16,185,129,0.3); border-radius:12px; padding:14px 18px; display:flex; align-items:center; gap:12px; color:#34D399;">
                    <i class="fa-solid fa-circle-check" style="font-size:22px;"></i>
                    <div style="font-size:12.5px;">
                        <strong>Spesifikasi Sempurna!</strong> Seluruh 13 seksi requirement telah lengkap dan siap diekspor menjadi Quality PRD &amp; MVP Prompt.
                    </div>
                </div>
            `;
        } else {
            warnBox.innerHTML = `
                <div style="background:rgba(245,158,11,0.12); border:1px solid rgba(245,158,11,0.3); border-radius:12px; padding:14px 18px; color:#FCD34D;">
                    <div style="font-size:12.5px; font-weight:800; display:flex; align-items:center; gap:8px; margin-bottom:6px;">
                        <i class="fa-solid fa-triangle-exclamation"></i>
                        <span>Terdapat ${warnings.length} Catatan Kelengkapan:</span>
                    </div>
                    <ul style="font-size:11.5px; margin-left:22px; line-height:1.6;">
                        ${warnings.map(w => `<li>${w}</li>`).join('')}
                    </ul>
                    <div style="font-size:11px; margin-top:8px; opacity:0.85;">
                        * Anda tetap dapat melanjutkan membuat PRD, namun melengkapi seksi di atas akan mencegah AI menebak requirement.
                    </div>
                </div>
            `;
        }
    }
}

// ============================================================================
// STEP 15: QUALITY PRD GENERATOR (24 SECTIONS MARKDOWN)
// ============================================================================
function generateDesignContract(p) {
    const theme = MOCK_DB.styles.find(s => String(s.id) === String(p.uiux.themeId));
    const directions = {
        dashboard: 'Operational clarity: compact sidebar, actionable work queue first, restrained KPI summary, aligned numeric columns and persistent filters. No oversized marketing hero.',
        landing_page: 'Conversion editorial: clear value proposition and one primary CTA, asymmetric hero, product evidence, benefits then FAQ. No admin sidebar or invented testimonials.',
        company_profile: 'Corporate editorial: strong typographic masthead, project case studies, factual credentials and clear contact path. Avoid generic KPI tiles and fabricated client logos.',
        e_commerce: 'Product-led commerce: search and category navigation, consistent product imagery ratios, visible price and stock, clear cart totals and recoverable checkout steps.',
        blog_content: 'Reading-first editorial: distinctive masthead, featured story, category index and 60–75 character reading measure. Do not turn articles into dashboard stat cards.'
    };
    const palette = theme && theme.color ? theme.color.split(',').filter(c => /^[0-9a-f]{6}$/i.test(c)).map(c => '#' + c) : [];
    return `### 19.1 Art Direction & Product Fit
- **Direction:** ${directions[p.taxonomy.pillar] || 'Pillar belum dipilih; arah visual perlu dikonfirmasi sebelum implementasi.'}
- **Theme reference:** ${theme ? theme.name : 'Belum dipilih; jangan mengklaim tema telah disepakati.'}
- **Catalog accent candidates:** ${palette.join(', ') || 'Belum ditentukan'}. These are accents, NOT a verified accessible surface/text palette.
- Preserve selected theme character. No automatic purple gradient, glass panels, glowing borders, or identical bento cards unless explicitly required by the chosen theme.

### 19.2 Design Tokens & Component Contract
- Define semantic CSS variables for canvas, surface, raised surface, primary text, muted text, border, accent, on-accent, success, warning and danger. Specify actual values before coding; measure text contrast >=4.5:1 and meaningful controls >=3:1.
- Type scale: body 16px/1.5, metadata 12–14px/1.4, section title 24–32px/1.2; editorial hero 36–64px with responsive clamp. Maximum two font families with local/system fallbacks. Numeric data uses tabular figures.
- Spacing scale: 4, 8, 12, 16, 24, 32, 48, 64px. Content gutters 16px mobile, 24px tablet, 32px desktop. Use 8px control radius, 12px surface radius as baseline; adapt deliberately to selected theme.
- One primary action per task region; secondary actions lower emphasis. Consistent button/input height 44px. No hover-only controls. Icons use one SVG family and consistent stroke.

### 19.3 Screen-Specific Interaction Plan
${p.uiux.screens.map((s, i) => `- **${i + 1}. ${s.name}:** features: ${s.features || 'Belum dipetakan'}; components: ${s.components || 'Belum ditentukan'}. Define primary task, initial viewport hierarchy, primary CTA, action outcome and return path. Missing details are proposed decisions, not approved requirements.`).join('\n') || '- No screens mapped. Screen hierarchy and core task require confirmation.'}
- Each data-backed screen defines loading, empty-first-use, no-results, error with retry, populated and permission-denied states. Never show fabricated success after an error.
- Forms retain entered values on failure, show linked inline errors, prevent duplicate submit and focus first invalid field. Destructive actions name the affected record and require confirmation or undo.

### 19.4 Responsive, Accessibility & Visual Acceptance
- Test 375, 768 and 1440px widths, landscape and 200% zoom. No page-level horizontal overflow. Tables may scroll inside labeled containers; do not remove critical columns without a detail alternative.
- Keyboard-visible focus; labeled icon buttons; semantic headings and landmarks. Dialogs trap focus, close on Escape and return focus to opener. Status never relies on color alone.
- Motion uses opacity/transform 120–200ms without layout shifts; honor prefers-reduced-motion. No autoplay or decorative perpetual animation.
- Review actual screens, not adjectives: clear first task, readable type hierarchy, consistent spacing, coherent states and realistic domain copy. Mark sample data as demo. No fake ratings, customer counts, revenue or compliance claims.
- Deliver screenshots at tested widths and report unresolved visual/accessibility issues. These criteria are acceptance targets, not claims that testing has already passed.
`;
}

function generateQualityPrdMarkdown() {
    const p = projectPRD;
    const now = new Date();
    const dateStr = now.toLocaleDateString('id-ID', { day: 'numeric', month: 'long', year: 'numeric' });

    let md = `# PRODUCT REQUIREMENTS DOCUMENT (PRD)
**Product Title:** ${p.project.name || 'Enterprise Solution'}  
**Document Version:** 1.0.0 (MVP Draft — requires stakeholder validation)
**Generation Date:** ${dateStr}  
**Architecture Paradigm:** Single-File MVP Architecture (\`index.html\`)  
**Validation Status:** Generated specification, not certification. Unspecified requirements need confirmation.

---

## 1. Executive Summary
${p.project.description || 'Sistem solusi enterprise yang dirancang untuk mengotomasi alur operasional dan pengolahan data terpadu.'}

## 2. Product Overview
- **Industry & Domain:** ${p.project.industry || 'Enterprise'}
- **Department:** ${p.project.department || 'Operations'}
- **Target Organization:** ${p.project.targetOrg || 'Corporate Stakeholders'}
- **Core Architecture Pillar:** ${p.taxonomy.pillar ? getPillarName(p.taxonomy.pillar) : 'Belum ditentukan'}
- **Architectural Archetype:** ${p.taxonomy.pillar && getPillarObj(p.taxonomy.pillar) ? getPillarObj(p.taxonomy.pillar).archetype : 'Enterprise Web Application'}
- **Architecture Characteristic:** ${p.taxonomy.pillar && getPillarObj(p.taxonomy.pillar) ? getPillarObj(p.taxonomy.pillar).description : 'Modular single-file architecture'}

## 3. Problem Statement
${p.project.problem || 'Permasalahan operasional yang dihadapi organisasi.'}

## 4. Business Objectives & Success Criteria
### 4.1 Business Objectives
${p.project.objective || 'Meningkatkan efisiensi dan keandalan sistem.'}

### 4.2 Measurable Success Criteria
${p.project.successCriteria || 'Keberhasilan diukur dari utilisasi penuh dan ketiadaan error fatal.'}

## 5. Scope of Work
### 5.1 In-Scope (Mandatory Deliverables)
${p.project.scope || 'Seluruh fitur fungsional inti yang terdaftar.'}

### 5.2 Out-of-Scope (Excluded from MVP)
${p.project.outOfScope || 'Integrasi backend monolitik eksternal dan akuntansi buku besar manual.'}

### 5.3 Additional Client Notes & Constraints
${p.project.additionalNotes || 'Tidak ada catatan tambahan khusus.'}

## 6. Target Users & Stakeholder Hierarchy
Sistem ini dirancang khusus untuk memenuhi kebutuhan hierarki peran sebagai berikut:
| No | Role Name | Department | User Type | Responsibility |
|:---|:---|:---|:---|:---|
${p.roles.map((r, i) => `| ${i + 1} | **${r.name}** | ${r.department || '-'} | ${r.type ? r.type.toUpperCase() : 'PRIMARY'} | ${r.responsibility || '-'} |`).join('\n') || '| 1 | Operator | Operasional | PRIMARY | Menjalankan sistem |'}

## 7. Personas & Operational Ergonomics
${p.roles.map(r => `### 7.${r.id} Persona: ${r.name}
- **Department:** ${r.department || 'Operasional'}
- **Operational Need:** ${r.responsibility || '-'}
- **Pain Points & Context:** ${r.persona || 'Memerlukan antarmuka responsif tanpa hambatan reload.'}
`).join('\n') || 'Persona terstandar mengikuti SOP perusahaan.'}

## 8. Product Architecture & System Boundaries
- **Deployment Format:** Single Standalone File \`index.html\` (HTML5 + CSS3 + Vanilla JS).
- **Backend Dependency:** None (100% offline executable).
- **Database Dependency:** None (In-memory reactive arrays + \`localStorage\` persistence).
- **Execution Environment:** Compatible with all modern evergreen browsers (Chrome, Edge, Safari, Firefox).

## 9. Module Architecture & Decomposition
Sistem didekomposisi ke dalam modul dan submodul fungsional berikut:
${p.modules.map((m, i) => `### 9.${i + 1} Modul: ${m.name}
- **Deskripsi:** ${m.description || '-'}
- **Submodul Terkait:** ${m.submodules || 'Core Engine'}
`).join('\n') || 'Modul terintegrasi penuh.'}

## 10. Functional Requirements Matrix (P0 - P3)
| Req ID | Module | Feature Name | Priority | Primary Actor | Expected Outcome |
|:---|:---|:---|:---|:---|:---|
${p.features.map(f => {
    const mod = p.modules.find(m => m.id === f.moduleId);
    return `| **${f.id}** | ${mod ? mod.name : 'Core'} | ${f.name} | **${f.priority || 'P1'}** | ${f.primaryUser || 'Semua Role'} | ${f.expectedOutcome || '-'} |`;
}).join('\n') || '| F1 | Core | Tampilan Data | P0 | User | Data tersaji |'}

## 11. Business Processes & Operational Workflows
Alur operasional terstruktur langkah demi langkah:
| Step | Process Name | Trigger | Actor | Input | Action | Decision Gate | Output | Status |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
${p.workflows.map(w => `| ${w.stepNo} | **${w.name}** | ${w.trigger || '-'} | ${w.actor || 'User'} | ${w.input || '-'} | ${w.action || '-'} | ${w.decision || '-'} | ${w.output || '-'} | \`${w.status || 'ACTIVE'}\` |`).join('\n') || '| 1 | Inisialisasi | Buka aplikasi | User | URL | Render UI | - | Dashboard aktif | READY |'}

## 12. Visual Workflow Sequence & Lifecycle States
\`\`\`text
${p.workflows.map(w => `[Step ${w.stepNo}: ${w.name}] (${w.status})`).join(' \n       ↓ \n')}
\`\`\`

## 13. Enterprise Business Rules & Constraints
Aturan integritas logika bisnis yang wajib diterapkan secara ketat:
| Rule ID | Rule Name | Condition | Enforcement Action | Severity | Exception |
|:---|:---|:---|:---|:---|:---|
${p.businessRules.map(r => `| **${r.id}** | ${r.name} | \`${r.condition || '-'}\` | ${r.action || '-'} | **${r.severity || 'Blocking'}** | ${r.exception || '-'} |`).join('\n') || '| BR1 | Validasi Data | Field kosong | Tampilkan error | Blocking | - |'}

## 14. Data Model (Entities, Fields, Relationships & Schemas)
${p.entities.map(e => `### 14.${e.id} Entity: ${e.name} (\`${e.storage || e.name.toLowerCase()}\`)
- **Tipe:** ${e.type || 'Transactional'}
- **Deskripsi:** ${e.description || '-'}

**Field Specification:**
| Field Name | Type | Requirement | Default | Validation | Description |
|:---|:---|:---|:---|:---|:---|
${(e.fields || []).map(f => `| \`${f.name}\` | ${f.type} | ${f.required === 'true' || f.required === true ? '**Required**' : 'Optional'} | \`${f.defaultValue || '-'}\` | ${f.validation || '-'} | ${f.description || '-'} |`).join('\n')}

${e.relationships && e.relationships.length > 0 ? `**Relationships:**\n${e.relationships.map(rel => `- ${rel.relationType} to \`${rel.targetEntity}\` via foreign key \`${rel.foreignKey}\``).join('\n')}` : ''}
`).join('\n') || 'Skema entitas data dimodelkan melalui mock array.'}

## 15. Role-Based Access Control (RBAC) Matrix
Matriks wewenang pengguna terhadap setiap modul sistem:
| Modul | Role | View | Create | Edit | Delete | Approve | Release | Execute | Verify | Close | Export |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
${(() => {
    let rbacRows = [];
    const roles = p.roles.length > 0 ? p.roles : [{ name: 'User' }];
    const modules = p.modules.length > 0 ? p.modules : [{ name: 'Core' }];
    modules.forEach(m => {
        roles.forEach(r => {
            const key = `${r.name}_${m.name}`;
            const perm = p.permissions[key] || { view: true };
            const chk = act => perm[act] ? '✓' : '-';
            rbacRows.push(`| ${m.name} | **${r.name}** | ${chk('view')} | ${chk('create')} | ${chk('edit')} | ${chk('delete')} | ${chk('approve')} | ${chk('release')} | ${chk('execute')} | ${chk('verify')} | ${chk('close')} | ${chk('export')} |`);
        });
    });
    return rbacRows.join('\n');
})()}

## 16. Key Performance Indicators (KPIs) & Analytics
| KPI Name | Formula | Target | Unit | Frequency | Visualization | Source |
|:---|:---|:---|:---|:---|:---|:---|
${p.kpis.map(k => `| **${k.name}** | \`${k.formula || '-'}\` | **${k.target || '-'}** | ${k.unit || ''} | ${k.frequency || 'Harian'} | ${k.visualization || 'Card'} | \`${k.source || '-'}\` |`).join('\n') || '| Utilisasi | Selesai / Total | >=90% | % | Harian | Card | System |'}

## 17. Notification & Escalation Protocols
| Event | Trigger Condition | Recipient Role | Channel | Priority | Escalation Protocol |
|:---|:---|:---|:---|:---|:---|
${p.notifications.map(n => `| **${n.name}** | ${n.trigger || '-'} | ${n.recipient || 'Petugas'} | ${n.channel || 'In-App'} | **${n.priority || 'P2'}** | ${n.escalation || '-'} |`).join('\n') || '| Alert Sistem | Error terdeteksi | Admin | In-App | P2 | Hubungi IT |'}

## 18. Integration Requirements & External Systems
| System Name | Purpose | Direction | Data Payload | Frequency | Protocol / Auth | MVP Mock Plan |
|:---|:---|:---|:---|:---|:---|:---|
${p.integrations.map(i => `| **${i.system}** | ${i.purpose || '-'} | ${i.direction || 'Inbound'} | \`${i.data || '-'}\` | ${i.frequency || 'Real-time'} | ${i.auth || 'REST API'} | ${i.mockNotes || 'Disimulasikan via tombol sync'} |`).join('\n') || '| External API | Sinkronisasi data | Inbound | JSON | Harian | REST | Simulasi dummy |'}

## 19. UI/UX Specification & Theme System
- **Selected Visual Theme:** #${p.uiux.themeId} &bull; **${p.uiux.themeName}**
- **Layout Architecture:** \`${p.uiux.layout}\`
- **Navigation Scheme:** \`${p.uiux.navigation}\`
- **Accessibility Compliance:** \`${p.uiux.accessibility}\` (Minimum 4.5:1 text contrast, WCAG AA touch targets).

${generateDesignContract(p)}
## 20. Screen & Information Architecture Mapping
| Screen Name | Mapped Features | Key Interactive Components |
|:---|:---|:---|
${p.uiux.screens.map(s => `| **${s.name}** | ${s.features || '-'} | ${s.components || '-'} |`).join('\n') || '| Main Dashboard | Seluruh fitur | Grid, Table, Modal |'}

## 21. Technical MVP Specification (Single-File Architecture)
Untuk menjamin kecepatan validasi tanpa kompleksitas server, MVP dibangun dengan spesifikasi teknis:
- **Deliverable:** Tepat 1 file tunggal \`index.html\`.
- **Frontend Stack:** HTML5 murni, Embedded CSS semantic tokens, Vanilla JavaScript ES6+ tanpa dependency CDN runtime.
- **Data Persistence:** \`localStorage\` browser + Reactive In-Memory State.
- **Backend / Database:** Tidak diperlukan server backend (Zero Node.js/Python server, Zero SQL/NoSQL DB setup).
- **Authentication:** Mock User Switcher pada header untuk beralih antar-role secara instan.

## 22. Non-Functional Requirements (NFR)
1. **Performance:** Initial render waktu muat halaman < 400ms; filter dan sorting tabel berjalan instan di memori < 50ms.
2. **Offline Resilience:** Aplikasi dapat dibuka langsung secara offline melalui \`file:///path/index.html\` tanpa koneksi internet aktif.
3. **Security:** Seluruh input pengguna disanitasi terhadap XSS (Cross-Site Scripting); tidak ada data sensitif yang diekspos keluar browser.
4. **Data Integrity:** Status mutasi data konsisten disimpan kembali ke \`localStorage\` sehingga tidak hilang saat browser direfresh.

## 23. Acceptance Criteria & Edge Cases
### 23.1 Acceptance Criteria
- [ ] Seluruh alur kerja dari tahap 1 hingga akhir dapat disimulasikan secara fungsional di browser.
- [ ] Formulir penambahan data memiliki validasi input wajib (tidak menerima data kosong).
- [ ] Fitur filter dan pencarian tabel berfungsi nyata menyaring baris data.
- [ ] Transisi status mengubah tampilan visual badge secara reaktif.
- [ ] Mock User Switcher berhasil mengubah pembatasan aksi sesuai Matriks RBAC.

### 23.2 Edge Cases Handled
- Data \`localStorage\` kosong pada pembukaan perdana di-seed otomatis dengan 10-15 baris data realistis.
- Validasi mencegah submit ganda dengan status tombol loading / disabled.
- Tampilan responsif pada resolusi desktop (1920x1080, 1366x768) dan tablet (1024x768).

## 24. Future Production Considerations & Scaling
Saat beralih dari MVP Single-File \`index.html\` ke sistem produksi perusahaan penuh:
1. Migrasi \`localStorage\` ke database relasional (PostgreSQL / MySQL) dengan transaksi ACID.
2. Memisahkan logika frontend ke framework modern (React / Laravel Blade) dan REST/GraphQL API.
3. Implementasi protokol autentikasi enterprise (OAuth2, SAML 2.0 / Active Directory SSO).
4. Menghubungkan konektor real-time ke SCADA/IoT dan ERP SAP melalui Message Broker (Kafka/RabbitMQ).

---
*Generated autonomously by Enterprise PRD Studio &bull; Single Source of Truth for AI Implementation.*
`;

    return md;
}

function renderPrdDocument() {
    const md = generateQualityPrdMarkdown();
    const rawBox = document.getElementById('prd-raw-textarea');
    const prevBox = document.getElementById('prd-preview-container');
    const linesCount = document.getElementById('prd-lines-count');

    if (rawBox) rawBox.value = md;
    if (linesCount) linesCount.textContent = `${md.split('\n').length} Baris Spesifikasi`;

    if (prevBox) {
        // Simple client-side markdown formatter for preview
        prevBox.innerHTML = convertMarkdownToHtml(md);
    }
}

function switchPrdTab(tab) {
    const rawBox = document.getElementById('prd-raw-textarea');
    const prevBox = document.getElementById('prd-preview-container');
    const btnRaw = document.getElementById('btn-tab-prd-raw');
    const btnPrev = document.getElementById('btn-tab-prd-preview');

    if (tab === 'raw') {
        if (rawBox) rawBox.style.display = 'block';
        if (prevBox) prevBox.style.display = 'none';
        if (btnRaw) { btnRaw.classList.add('btn-primary'); btnRaw.classList.remove('btn-secondary'); }
        if (btnPrev) { btnPrev.classList.remove('btn-primary'); btnPrev.classList.add('btn-secondary'); }
    } else {
        if (rawBox) rawBox.style.display = 'none';
        if (prevBox) prevBox.style.display = 'block';
        if (btnPrev) { btnPrev.classList.add('btn-primary'); btnPrev.classList.remove('btn-secondary'); }
        if (btnRaw) { btnRaw.classList.remove('btn-primary'); btnRaw.classList.add('btn-secondary'); }
    }
}

function copyPrdMarkdown() {
    const md = generateQualityPrdMarkdown();
    navigator.clipboard.writeText(md).then(() => {
        Swal.fire({
            icon: 'success',
            title: 'Dokumen PRD Tersalin!',
            text: 'Dokumen markdown 24-seksi telah disalin ke clipboard.',
            background: '#0D111A',
            color: '#F8FAFC',
            timer: 2200
        });
    });
}

function downloadPrdMarkdown() {
    const md = generateQualityPrdMarkdown();
    const cleanName = (projectPRD.project.name || 'ENTERPRISE_PRD').replace(/[^a-zA-Z0-9_-]/g, '_').toUpperCase();
    const filename = `PRD_${cleanName}.md`;

    const blob = new Blob([md], { type: 'text/markdown;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

function printPrdDocument() {
    const md = generateQualityPrdMarkdown();
    const printWindow = window.open('', '_blank');
    if (!printWindow) {
        Swal.fire({ icon: 'error', title: 'Jendela cetak diblokir', text: 'Izinkan popup untuk mencetak PRD.' });
        return;
    }
    printWindow.document.write(`
        <html>
        <head>
            <title>PRD - ${escapeHtml(projectPRD.project.name || 'Enterprise Solution')}</title>
            <style>
                body { font-family: -apple-system, sans-serif; line-height: 1.6; color: #111; padding: 40px; }
                h1 { font-size: 24px; border-bottom: 2px solid #333; padding-bottom: 8px; }
                h2 { font-size: 18px; margin-top: 24px; color: #1E3A8A; border-bottom: 1px solid #ddd; }
                table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 12px; }
                th, td { border: 1px solid #ccc; padding: 6px 10px; text-align: left; }
                th { background: #f3f4f6; }
                code { font-family: monospace; background: #f3f4f6; padding: 2px 4px; }
            </style>
        </head>
        <body>${convertMarkdownToHtml(md)}</body>
        </html>
    `);
    printWindow.document.close();
    printWindow.focus();
    setTimeout(() => { printWindow.print(); }, 500);
}

function convertMarkdownToHtml(md) {
    return escapeHtml(md)
        .replace(/^# (.*$)/gim, '<h1>$1</h1>')
        .replace(/^## (.*$)/gim, '<h2>$1</h2>')
        .replace(/^### (.*$)/gim, '<h3>$1</h3>')
        .replace(/^> (.*$)/gim, '<blockquote>$1</blockquote>')
        .replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/gim, '<em>$1</em>')
        .replace(/`([^`]+)`/gim, '<code>$1</code>')
        .replace(/\n\n/gim, '<br><br>')
        .replace(/\|(.+)\|/gim, (match) => {
            if (match.includes('---')) return '';
            const cells = match.split('|').filter(c => c.trim() !== '');
            const isHeader = false;
            return `<tr>${cells.map(c => `<td>${c.trim()}</td>`).join('')}</tr>`;
        })
        .replace(/(?:<tr>[^\n]*<\/tr>\s*)+/g, '<div class="table-responsive"><table class="custom-table">$&</table></div>');
}

// ============================================================================
// STEP 16: MVP IMPLEMENTATION PROMPT GENERATOR
// ============================================================================
function generateMvpImplementationPrompt() {
    const p = projectPRD;
    const prdMarkdown = generateQualityPrdMarkdown();

    const prompt = `Act as a Principal Full-Stack Engineer and Lead UI/UX Architect.

Your task is to build the application described in the attached Product Requirements Document (PRD) as a fully functional Single-File MVP.

# DELIVERABLE SPECIFICATION
Output exactly ONE file:
\`index.html\`

The file must contain:
1. All HTML5 semantic markup
2. All CSS styling embedded with semantic CSS variables matching the PRD theme; no runtime CDN dependencies
3. All JavaScript application logic (Vanilla JS ES6+)
4. All initial mock data (10-15 realistic, comprehensive records pre-seeded into state)

# CRITICAL ZERO-TOLERANCE RULES
- DO NOT create a backend server (no Node.js, Express, Python, PHP, or Go backend).
- DO NOT create a database server (no MySQL, PostgreSQL, MongoDB, or Firebase).
- DO NOT create separate .css or .js files; everything MUST be contained in the single \`index.html\`.
- DO NOT invent business rules or workflows that contradict the PRD.
- DO NOT output placeholder text ("TODO", "Implement here", "Logic goes here"). Every interactive element MUST work.
- The file MUST run directly in any browser by double-clicking it offline (\`file:///...\`).

# FUNCTIONAL MVP REQUIREMENTS (NO VISUAL DUMMIES)
The output must NOT be a static mockup. Implement only interactions supported by the PRD. The following patterns apply ONLY when mapped to its features; do not add ERP tables, approval flows, or KPI dashboards to editorial, marketing, or commerce pages without a stated requirement:
1. **Interactive Data Tables & Filters:**
   - Multi-criteria filtering by status, priority, category, and real-time text search.
   - Sorting and pagination.
2. **Working Modal Forms (Create / Edit):**
   - Modal forms MUST perform full validation and upon submit, append new records to local state with toast confirmation (SweetAlert2 or custom toast).
3. **Reactive Status Transitions:**
   - Changing status (e.g. from "Planned" -> "Released" -> "In-Progress" -> "Closed") must update the state, timeline, and visual status badges instantly.
4. **Approval & Role Simulation:**
   - Include a "Mock User Switcher" in the top bar allowing the tester to switch between roles (${p.roles.map(r => r.name).join(', ') || 'Planner, Supervisor, Mechanic'}).
   - The UI must enforce permissions based on the RBAC Matrix in the PRD (e.g. hide or disable Approve/Release buttons for unauthorized roles).
5. **State Persistence:**
   - Persist modified records to \`localStorage\` so data survives page reloads.
   - Include a "Reset to Default Demo Data" button in the status bar or header.
6. **KPI & Analytics Cards:**
   - Display executive KPI cards with calculations dynamically reflecting the current state records.

# UI/UX & STYLING GUIDELINES
- Visual Aesthetic: Match the selected theme: #${p.uiux.themeId} (${p.uiux.themeName}).
- Color Palette: Follow section 19. Respect selected theme; do not force dark mode. Verify contrast, not merely claim WCAG compliance.
- Icons: Inline SVG from one consistent icon family; no CDN or emoji navigation.
- Feedback: Accessible local dialogs and inline validation; no external alert dependency.
- Layout: ${p.uiux.layout.replace(/_/g, ' ').toUpperCase()} with clean optical alignments and responsive mobile/desktop handling.

---

# SOURCE OF TRUTH: STRUCTURED PRODUCT REQUIREMENTS DOCUMENT (PRD)
Below is the complete, authoritative PRD. Treat every requirement, rule, and workflow in this document as the absolute source of truth:

\`\`\`markdown
${prdMarkdown}
\`\`\`

# INSTRUCTION TO AI CODING AGENT
Generate the complete, testable prototype \`index.html\` file now. Begin directly with \`<!DOCTYPE html>\` and end with \`</html>\`. Do not skip any JavaScript functions or mock data records. Mock roles are not production authentication; do not store real sensitive data in this prototype.`;

    return prompt;
}

function renderMvpPromptOutput() {
    const promptText = generateMvpImplementationPrompt();
    const promptBox = document.getElementById('mvp-prompt-box');
    const linesCount = document.getElementById('prompt-lines-count');

    if (promptBox) promptBox.value = promptText;
    if (linesCount) linesCount.textContent = `${promptText.split('\n').length} Baris Instruksi Coding Agent`;
}

function copyMvpPrompt() {
    const promptText = generateMvpImplementationPrompt();
    navigator.clipboard.writeText(promptText).then(() => {
        Swal.fire({
            icon: 'success',
            title: 'MVP Prompt Berhasil Disalin!',
            text: 'Tempelkan langsung ke Claude 3.7 Sonnet, GPT-4o, Cursor, v0, atau Antigravity untuk membangun single-file index.html.',
            background: '#0D111A',
            color: '#F8FAFC',
            confirmButtonColor: '#6366F1',
            timer: 3500
        });
    });
}

function downloadMvpPromptTxt() {
    const promptText = generateMvpImplementationPrompt();
    const cleanName = (projectPRD.project.name || 'MVP_PROMPT').replace(/[^a-zA-Z0-9_-]/g, '_').toUpperCase();
    const filename = `MVP_IMPLEMENTATION_PROMPT_${cleanName}.txt`;

    const blob = new Blob([promptText], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// ============================================================================
// TEMPORARY DRAFTS STORAGE & PERSISTENCE ENGINE
// ============================================================================
function calculateCompletenessScore() {
    const p = projectPRD;
    const checks = [
        { pass: Boolean(p.project.name && p.project.problem && p.project.objective), weight: 10 },
        { pass: Boolean(p.taxonomy.pillar), weight: 10 },
        { pass: p.roles.length >= 2, weight: 10 },
        { pass: p.modules.length >= 1 && p.features.length >= 2, weight: 10 },
        { pass: p.workflows.length >= 3, weight: 10 },
        { pass: p.businessRules.length >= 1, weight: 10 },
        { pass: p.entities.length >= 1, weight: 10 },
        { pass: Object.keys(p.permissions).length > 0, weight: 5 },
        { pass: p.kpis.length >= 1, weight: 5 },
        { pass: p.notifications.length >= 1, weight: 5 },
        { pass: p.integrations.length >= 1, weight: 5 },
        { pass: Boolean(p.uiux.themeId && p.uiux.screens.length >= 1), weight: 5 },
        { pass: Boolean(p.technicalMVP.deployment && p.project.name), weight: 5 }
    ];
    return checks.reduce((sum, c) => sum + (c.pass ? c.weight : 0), 0);
}

function saveProject(showToast = false) {
    if (currentStep === 1) saveStep1Inputs();
    try {
        localStorage.setItem('enterprise_prd_studio_project', JSON.stringify(projectPRD));
        if (showToast) {
            Swal.fire({
                toast: true,
                position: 'top-end',
                icon: 'success',
                title: 'Proyek Tersimpan di Browser',
                showConfirmButton: false,
                timer: 2000,
                background: '#0D111A',
                color: '#F8FAFC'
            });
        }
    } catch (e) {
        console.error('Error saving to localStorage:', e);
    }
}

function loadProject() {
    try {
        const saved = localStorage.getItem('enterprise_prd_studio_project');
        if (saved) {
            const parsed = JSON.parse(saved);
            if (parsed && parsed.project) {
                projectPRD = parsed;
                return;
            }
        }
    } catch (e) {
        console.error('Error loading from localStorage:', e);
    }
    // Default: workspace completely empty by default!
    projectPRD = getEmptyProject();
}

// DRAFTS STORAGE (TEMPAT SIMPAN SEMENTARA)
function getDrafts() {
    try {
        const saved = localStorage.getItem('enterprise_prd_drafts');
        return saved ? JSON.parse(saved) : [];
    } catch (e) {
        console.error('Error reading drafts from localStorage:', e);
        return [];
    }
}

function saveDraftsToStorage(drafts) {
    try {
        localStorage.setItem('enterprise_prd_drafts', JSON.stringify(drafts));
        updateDraftsCountBadge();
    } catch (e) {
        console.error('Error writing drafts to localStorage:', e);
    }
}

function updateDraftsCountBadge() {
    const countEl = document.getElementById('top-drafts-count');
    const drafts = getDrafts();
    if (countEl) {
        countEl.textContent = drafts.length;
    }
}

function saveQuickDraft() {
    if (currentStep === 1) saveStep1Inputs();
    saveProject(false);

    const drafts = getDrafts();
    const now = new Date();
    const timeStr = now.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    const dateStr = now.toLocaleDateString('id-ID', { day: 'numeric', month: 'short', year: 'numeric' });
    const draftName = projectPRD.project.name ? `Draft: ${projectPRD.project.name}` : `Draft Proyek (${dateStr} ${timeStr})`;

    const newDraft = {
        id: 'draft_' + Date.now(),
        name: draftName,
        savedAt: now.toISOString(),
        score: calculateCompletenessScore(),
        stats: {
            projectName: projectPRD.project.name || 'Proyek Tanpa Judul',
            pillar: projectPRD.taxonomy.pillar || '-',
            rolesCount: projectPRD.roles.length,
            modulesCount: projectPRD.modules.length,
            featuresCount: projectPRD.features.length,
            entitiesCount: projectPRD.entities.length,
            screensCount: projectPRD.uiux.screens.length
        },
        data: JSON.parse(JSON.stringify(projectPRD))
    };

    drafts.unshift(newDraft);
    if (drafts.length > 30) drafts.pop(); // keep last 30 drafts
    saveDraftsToStorage(drafts);

    const autoChip = document.getElementById('auto-draft-chip');
    if (autoChip) {
        autoChip.innerHTML = `<i class="fa-solid fa-circle-check" style="margin-right:4px;"></i>Draft Tersimpan (${timeStr})`;
    }

    Swal.fire({
        toast: true,
        position: 'top-end',
        icon: 'success',
        title: 'Draft Berhasil Disimpan Sementara',
        text: `Tersimpan: "${draftName}" (${drafts.length} draft di browser)`,
        showConfirmButton: false,
        timer: 2500,
        background: '#0D111A',
        color: '#F8FAFC'
    });
}

function saveNamedDraft() {
    if (currentStep === 1) saveStep1Inputs();
    saveProject(false);

    const input = document.getElementById('draft-name-input');
    const nameVal = input ? input.value.trim() : '';
    const now = new Date();
    const timeStr = now.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    const dateStr = now.toLocaleDateString('id-ID', { day: 'numeric', month: 'short', year: 'numeric' });

    const finalName = nameVal || (projectPRD.project.name ? `Draft: ${projectPRD.project.name}` : `Draft PRD - ${dateStr} ${timeStr}`);

    const drafts = getDrafts();
    const newDraft = {
        id: 'draft_' + Date.now(),
        name: finalName,
        savedAt: now.toISOString(),
        score: calculateCompletenessScore(),
        stats: {
            projectName: projectPRD.project.name || 'Proyek Tanpa Judul',
            pillar: projectPRD.taxonomy.pillar || '-',
            rolesCount: projectPRD.roles.length,
            modulesCount: projectPRD.modules.length,
            featuresCount: projectPRD.features.length,
            entitiesCount: projectPRD.entities.length,
            screensCount: projectPRD.uiux.screens.length
        },
        data: JSON.parse(JSON.stringify(projectPRD))
    };

    drafts.unshift(newDraft);
    if (drafts.length > 30) drafts.pop();
    saveDraftsToStorage(drafts);

    if (input) input.value = '';
    renderDraftsList();

    Swal.fire({
        toast: true,
        position: 'top-end',
        icon: 'success',
        title: 'Draft Baru Tersimpan',
        text: `"${finalName}" berhasil disimpan ke slot simpanan sementara.`,
        showConfirmButton: false,
        timer: 2500,
        background: '#0D111A',
        color: '#F8FAFC'
    });
}

function openDraftManagerModal() {
    const input = document.getElementById('draft-name-input');
    if (input) {
        const now = new Date();
        const timeStr = now.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit' });
        input.value = projectPRD.project.name ? `Draft: ${projectPRD.project.name} (${timeStr})` : `Draft Proyek - ${timeStr}`;
    }
    renderDraftsList();
    openModal('modal-drafts');
}

function renderDraftsList() {
    const container = document.getElementById('drafts-list-container');
    if (!container) return;
    container.innerHTML = '';

    const drafts = getDrafts();
    if (drafts.length === 0) {
        container.innerHTML = `
            <div style="text-align:center; padding:32px 16px; background:#0A0E17; border:1px dashed #1E293B; border-radius:12px; color:#64748B;">
                <i class="fa-solid fa-box-open" style="font-size:32px; color:#334155; margin-bottom:10px;"></i>
                <div style="font-size:13px; font-weight:700; color:#E2E8FF; margin-bottom:4px;">Belum Ada Draft Tersimpan Sementara</div>
                <div style="font-size:11.5px; max-width:400px; margin:0 auto;">Ketik nama draft di atas lalu klik "Simpan Draft" atau tekan tombol "Simpan Draft" di header kapan saja untuk membuat simpanan cadangan.</div>
            </div>
        `;
        return;
    }

    drafts.forEach(d => {
        const dateObj = new Date(d.savedAt);
        const formattedDate = dateObj.toLocaleDateString('id-ID', { day: 'numeric', month: 'short', year: 'numeric' }) + ', ' + dateObj.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit' });
        const pillarName = getPillarName(d.stats?.pillar) || (d.stats?.pillar && d.stats?.pillar !== '-' ? d.stats?.pillar : 'Belum pilih pilar');

        const card = document.createElement('div');
        card.className = 'draft-card';
        card.innerHTML = `
            <div style="flex:1; min-width:0; padding-right:12px;">
                <div style="display:flex; align-items:center; gap:8px; margin-bottom:4px;">
                    <span style="font-weight:800; font-size:13.5px; color:#F8FAFC; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${escapeHtml(d.name)}</span>
                    <span class="badge ${d.score >= 80 ? 'badge-emerald' : d.score >= 40 ? 'badge-amber' : 'badge-slate'}" style="font-size:10px;">PRD ${d.score || 0}%</span>
                </div>
                <div style="display:flex; flex-wrap:wrap; align-items:center; gap:10px; font-size:11px; color:#94A3B8;">
                    <span><i class="fa-regular fa-clock" style="margin-right:4px;"></i>${formattedDate}</span>
                    <span>&bull;</span>
                    <span style="color:#818CF8;"><i class="fa-solid fa-layer-group" style="margin-right:4px;"></i>${escapeHtml(pillarName)}</span>
                    <span>&bull;</span>
                    <span>${d.stats?.modulesCount || 0} Modul, ${d.stats?.featuresCount || 0} Fitur</span>
                    <span>&bull;</span>
                    <span>${d.stats?.entitiesCount || 0} Entitas</span>
                </div>
            </div>
            <div style="display:flex; align-items:center; gap:6px; flex-shrink:0;">
                <button type="button" class="btn btn-primary btn-sm" onclick="loadDraft('${d.id}')" title="Muat draft ini ke workspace aktif">
                    <i class="fa-solid fa-arrow-right-to-bracket"></i>
                    <span>Muat</span>
                </button>
                <button type="button" class="btn btn-secondary btn-sm" onclick="exportSingleDraftJson('${d.id}')" title="Unduh draft ini sebagai file JSON">
                    <i class="fa-solid fa-download"></i>
                </button>
                <button type="button" class="btn btn-rose btn-sm" onclick="deleteDraft('${d.id}')" title="Hapus draft ini dari simpanan sementara">
                    <i class="fa-solid fa-trash-can"></i>
                </button>
            </div>
        `;
        container.appendChild(card);
    });
}

function loadDraft(draftId) {
    const drafts = getDrafts();
    const d = drafts.find(item => item.id === draftId);
    if (!d) return;

    Swal.fire({
        title: 'Muat Draft Ini?',
        text: `Memuat "${d.name}". Seluruh lembar kerja aktif saat ini akan digantikan dengan data draft ini.`,
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#6366F1',
        cancelButtonColor: '#334155',
        confirmButtonText: 'Ya, Muat Draft',
        cancelButtonText: 'Batal',
        background: '#0D111A',
        color: '#F8FAFC'
    }).then((res) => {
        if (res.isConfirmed) {
            projectPRD = JSON.parse(JSON.stringify(d.data));
            syncStep1Form();
            saveProject(false);
            initTaxonomyUI();
            renderRoles();
            renderModulesAndFeatures();
            renderWorkflowNodes();
            renderBusinessRules();
            renderEntities();
            renderRbacMatrix();
            renderKpis();
            renderNotifications();
            renderIntegrations();
            renderScreens();
            updateUiMetadata();
            checkCompleteness();
            closeModal('modal-drafts');
            goToStep(1);

            Swal.fire({
                icon: 'success',
                title: 'Draft Berhasil Dimuat!',
                text: `"${d.name}" sekarang aktif di lembar kerja Anda.`,
                background: '#0D111A',
                color: '#F8FAFC',
                confirmButtonColor: '#6366F1',
                timer: 2500
            });
        }
    });
}

function deleteDraft(draftId) {
    Swal.fire({
        title: 'Hapus Draft Ini?',
        text: 'Draft ini akan dihapus permanen dari simpanan sementara browser Anda.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#F43F5E',
        cancelButtonColor: '#334155',
        confirmButtonText: 'Ya, Hapus',
        cancelButtonText: 'Batal',
        background: '#0D111A',
        color: '#F8FAFC'
    }).then((res) => {
        if (res.isConfirmed) {
            let drafts = getDrafts();
            drafts = drafts.filter(d => d.id !== draftId);
            saveDraftsToStorage(drafts);
            renderDraftsList();
            Swal.fire({
                toast: true,
                position: 'top-end',
                icon: 'success',
                title: 'Draft Dihapus',
                showConfirmButton: false,
                timer: 1800,
                background: '#0D111A',
                color: '#F8FAFC'
            });
        }
    });
}

function clearAllDrafts() {
    const drafts = getDrafts();
    if (drafts.length === 0) {
        Swal.fire({
            icon: 'info',
            title: 'Tidak Ada Draft',
            text: 'Daftar draft simpanan sementara sudah kosong.',
            background: '#0D111A',
            color: '#F8FAFC'
        });
        return;
    }

    Swal.fire({
        title: 'Hapus SEMUA Draft?',
        text: `Anda akan menghapus ${drafts.length} draft simpanan sementara di browser. Tindakan ini tidak dapat dibatalkan.`,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#F43F5E',
        cancelButtonColor: '#334155',
        confirmButtonText: 'Ya, Hapus Semua',
        cancelButtonText: 'Batal',
        background: '#0D111A',
        color: '#F8FAFC'
    }).then((res) => {
        if (res.isConfirmed) {
            saveDraftsToStorage([]);
            renderDraftsList();
            Swal.fire({
                toast: true,
                position: 'top-end',
                icon: 'success',
                title: 'Semua Draft Berhasil Dihapus',
                showConfirmButton: false,
                timer: 2000,
                background: '#0D111A',
                color: '#F8FAFC'
            });
        }
    });
}

function exportSingleDraftJson(draftId) {
    const drafts = getDrafts();
    const d = drafts.find(item => item.id === draftId);
    if (!d) return;

    const cleanName = (d.name || 'draft').replace(/[^a-zA-Z0-9_-]/g, '_').toLowerCase();
    const filename = `${cleanName}.json`;
    const dataStr = JSON.stringify(d.data, null, 2);

    const blob = new Blob([dataStr], { type: 'application/json;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

function resetProjectConfirm() {
    Swal.fire({
        title: 'Kosongkan Seluruh Isian?',
        text: 'Semua isian formulir aktif akan dikosongkan. Jika ada data penting, simpan sebagai Draft terlebih dahulu.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#F43F5E',
        cancelButtonColor: '#334155',
        confirmButtonText: 'Ya, Kosongkan',
        cancelButtonText: 'Batal',
        background: '#0D111A',
        color: '#F8FAFC'
    }).then((result) => {
        if (result.isConfirmed) {
            projectPRD = getEmptyProject();
            syncStep1Form();
            saveProject(false);
            initTaxonomyUI();
            renderRoles();
            renderModulesAndFeatures();
            renderWorkflowNodes();
            renderBusinessRules();
            renderEntities();
            renderRbacMatrix();
            renderKpis();
            renderNotifications();
            renderIntegrations();
            renderScreens();
            updateUiMetadata();
            checkCompleteness();
            goToStep(1);

            Swal.fire({
                toast: true,
                position: 'top-end',
                icon: 'success',
                title: 'Lembar Kerja Berhasil Dikosongkan',
                showConfirmButton: false,
                timer: 2000,
                background: '#0D111A',
                color: '#F8FAFC'
            });
        }
    });
}

function exportProjectJson() {
    if (currentStep === 1) saveStep1Inputs();
    const cleanName = (projectPRD.project.name || 'PROJECT_PRD').replace(/[^a-zA-Z0-9_-]/g, '_').toLowerCase();
    const filename = `${cleanName}-prd.json`;
    const dataStr = JSON.stringify(projectPRD, null, 2);

    const blob = new Blob([dataStr], { type: 'application/json;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);

    Swal.fire({
        toast: true,
        position: 'top-end',
        icon: 'success',
        title: 'File JSON PRD Berhasil Diunduh',
        showConfirmButton: false,
        timer: 2000,
        background: '#0D111A',
        color: '#F8FAFC'
    });
}

function importProjectJson(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            const data = JSON.parse(e.target.result);
            if (data && data.project) {
                projectPRD = data;
                syncStep1Form();
                saveProject();
                initTaxonomyUI();
                renderRoles();
                renderModulesAndFeatures();
                renderWorkflowNodes();
                renderBusinessRules();
                renderEntities();
                renderRbacMatrix();
                renderKpis();
                renderNotifications();
                renderIntegrations();
                renderScreens();
                updateUiMetadata();
                checkCompleteness();
                goToStep(1);

                Swal.fire({
                    icon: 'success',
                    title: 'Proyek Berhasil Diimpor!',
                    text: `Proyek "${projectPRD.project.name || 'Tanpa Judul'}" berhasil dimuat.`,
                    background: '#0D111A',
                    color: '#F8FAFC'
                });
            } else {
                Swal.fire({ icon: 'error', title: 'Format JSON Tidak Valid', text: 'Struktur project PRD tidak dikenali.', background: '#0D111A', color: '#F8FAFC' });
            }
        } catch (err) {
            Swal.fire({ icon: 'error', title: 'Gagal Membaca File', text: err.message, background: '#0D111A', color: '#F8FAFC' });
        }
    };
    reader.readAsText(file);
    event.target.value = '';
}

// ============================================================================
// AI PROMPT FORMAT & INSTANT JSON IMPORT ENGINE
// ============================================================================
function getAiPromptTemplate(userTitle = '', userDesc = '') {
    const titleText = userTitle.trim() ? userTitle.trim() : '[TULISKAN NAMA ATAU JUDUL APLIKASI DI SINI, CONTOH: "Sistem Manajemen Gudang & Logistik Spareparts Alat Berat Tambang"]';
    const descText = userDesc.trim() ? `\n\nDESKRIPSI DETAIL & KEBUTUHAN:\n"${userDesc.trim()}"` : '';
    
    return `Anda adalah seorang Principal Enterprise Software Architect dan Requirements Engineer berskala korporat.
Tugas Anda adalah merancang spesifikasi sistem aplikasi perangkat lunak yang sangat komprehensif, terstruktur, dan siap implementasi berdasarkan konsep produk berikut:

JUDUL PRODUK / SISTEM:
"${titleText}"${descText}

Tolong buatkan seluruh spesifikasi requirement dalam satu format JSON yang valid, terstruktur, dan lengkap mengikuti skema di bawah ini.

PENTING - ATURAN OUTPUT:
1. Hanya keluarkan kode JSON yang VALID di dalam blok \`\`\`json ... \`\`\` tanpa penjelasan pembuka/penutup di luar blok.
2. JANGAN menggunakan placeholder ("TODO", "dsb", "dll"). Tuliskan data realistis, istilah industri yang tepat, dan aturan bisnis yang mendalam.
3. Nilai "taxonomy.pillar" WAJIB memilih salah satu dari 5 pilar berikut:
   - "dashboard" (Untuk Dashboard ERP, Control Center, Operasional, Work Order, CRUD berdensitas tinggi)
   - "landing_page" (Untuk Landing Page Pemasaran, Lead Generation, Showcase Produk/Jasa)
   - "company_profile" (Untuk Company Profile Korporat, Portofolio Holding, ESG, Hubungan Investor)
   - "e_commerce" (Untuk E-Commerce, Marketplace, B2B Commodity Trading, Pemesanan & Checkout)
   - "blog_content" (Untuk Portal Berita, Artikel Riset, Blog Industri, Publikasi Editorial)
4. Buatlah spesifikasi terstruktur dengan cakupan seimbang:
   - 3 Roles pengguna (dengan tanggung jawab & persona jelas)
   - 3 Modul utama dengan masing-masing 2 Fitur
   - 4-5 Tahapan Workflow berurutan (dengan actor, trigger, action, output)
   - 3 Business Rules (aturan validasi / hard constraint)
   - 2 Entities data (tabel master/transaksional lengkap dengan fields dan tipe data)
   - 3 KPI metrik terukur
   - 2 Notifikasi operasional / eskalasi
   - 2 Integrasi sistem (API/Webhook)
   - 2-3 Screens UI/UX utama yang dipetakan ke fitur
5. EFISIENSI & KEPADATAN TEKS:
   Tuliskan deskripsi secara tajam, padat, profesional, dan to-the-point (hindari repetisi kalimat atau narasi panjang yang bertele-tele) agar seluruh 16 tahapan dapat dikomputasi dengan cepat dan tuntas tanpa risiko terputus atau timeout.

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
      "name": "Nama Role 1 (Contoh: Operations Supervisor)",
      "department": "Departemen",
      "type": "primary",
      "responsibility": "Tanggung jawab utama operasional role ini.",
      "persona": "Karakteristik & fokus utama persona ini saat memakai aplikasi."
    },
    {
      "id": "r2",
      "name": "Nama Role 2 (Contoh: Field Operator)",
      "department": "Departemen",
      "type": "primary",
      "responsibility": "Tanggung jawab utama operasional role ini.",
      "persona": "Karakteristik & fokus utama persona ini saat memakai aplikasi."
    }
  ],
  "modules": [
    {
      "id": "m1",
      "name": "Nama Modul 1",
      "code": "MOD-01",
      "desc": "Deskripsi modul fungsional.",
      "features": [
        {
          "id": "f101",
          "name": "Nama Fitur 1.1",
          "code": "FEAT-101",
          "priority": "P1 High",
          "desc": "Deskripsi fungsional fitur.",
          "acceptance": "Kriteria penerimaan pengujian fitur."
        },
        {
          "id": "f102",
          "name": "Nama Fitur 1.2",
          "code": "FEAT-102",
          "priority": "P2 Medium",
          "desc": "Deskripsi fungsional fitur.",
          "acceptance": "Kriteria penerimaan pengujian fitur."
        }
      ]
    }
  ],
  "workflows": [
    {
      "id": "wf1",
      "stepNo": 1,
      "name": "Nama Tahapan 1",
      "actor": "Role Pelaksana",
      "status": "DRAFT",
      "trigger": "Pemicu alur kerja",
      "input": "Dokumen / data masukan",
      "action": "Tindakan yang dieksekusi",
      "decision": "Pengecekan validasi",
      "output": "Hasil keluaran / status baru"
    },
    {
      "id": "wf2",
      "stepNo": 2,
      "name": "Nama Tahapan 2",
      "actor": "Role Pelaksana",
      "status": "APPROVED",
      "trigger": "Tahap 1 selesai",
      "input": "Dokumen dari tahap 1",
      "action": "Review & approval",
      "decision": "Setujui atau tolak",
      "output": "Status disetujui"
    },
    {
      "id": "wf3",
      "stepNo": 3,
      "name": "Nama Tahapan 3",
      "actor": "Role Pelaksana",
      "status": "COMPLETED",
      "trigger": "Persetujuan final",
      "input": "Data tervalidasi",
      "action": "Eksekusi penyelesaian",
      "decision": "Konfirmasi selesai",
      "output": "Transaksi selesai & arsip audit"
    }
  ],
  "businessRules": [
    {
      "id": "br1",
      "code": "BR-01",
      "name": "Nama Aturan Bisnis Kunci 1",
      "category": "Integritas Data",
      "level": "Hard Constraint",
      "ruleStatement": "Pernyataan aturan bisnis yang wajib ditaati sistem.",
      "failAction": "Tindakan sistem jika aturan dilanggar (misal: Tolak submit & beri peringatan)."
    }
  ],
  "entities": [
    {
      "id": "e1",
      "name": "NamaEntitasData",
      "code": "tbl_records",
      "desc": "Tabel utama penyimpan data transaksi.",
      "fields": [
        { "name": "id", "type": "VARCHAR(36)", "required": true, "desc": "Primary Key unik" },
        { "name": "code", "type": "VARCHAR(40)", "required": true, "desc": "Kode identifikasi unik" },
        { "name": "status", "type": "VARCHAR(20)", "required": true, "desc": "Status alur data" },
        { "name": "created_at", "type": "TIMESTAMP", "required": true, "desc": "Waktu pembuatan record" }
      ]
    }
  ],
  "permissions": {
    "Role 1_Modul 1": { "view": true, "create": true, "edit": true, "delete": true, "approve": true, "export": true },
    "Role 2_Modul 1": { "view": true, "create": true, "edit": false, "delete": false, "approve": false, "export": true }
  },
  "kpis": [
    {
      "id": "k1",
      "name": "Nama Metrik KPI 1",
      "code": "KPI-01",
      "target": ">= 95%",
      "formula": "Rumus kalkulasi metrik",
      "source": "Tabel sumber data",
      "frequency": "Daily / Realtime"
    }
  ],
  "notifications": [
    {
      "id": "n1",
      "event": "Event Pemicu Alert",
      "channel": "In-App Banner & Toast",
      "recipient": "Role Penerima Notifikasi",
      "priority": "P1 Critical",
      "escalation": "Aturan eskalasi jika dalam X jam tidak direspon",
      "messageTemplate": "[ALERT] Pesan notifikasi sistem..."
    }
  ],
  "integrations": [
    {
      "id": "i1",
      "systemName": "Nama Sistem Eksternal",
      "direction": "Inbound / Outbound / Bi-directional",
      "frequency": "Real-time Webhook / REST API",
      "purpose": "Tujuan pertukaran data",
      "dataPayload": "Struktur payload data",
      "protocolAuth": "REST API Bearer Token OAuth 2.0",
      "offlineSimulation": "Simulasi mock array di browser localStorage untuk single-file MVP"
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
        "name": "Dashboard Utama",
        "features": "Stat Cards Ringkasan, Alert Kritis, Quick Action",
        "components": "4 Stat Cards, Bento Grid Layout, Quick Action Buttons"
      },
      {
        "id": "s2",
        "name": "Katalog Manajemen Data",
        "features": "Tabel Data Berdensitas Tinggi, Multi-Filter, Search, Modal Form Tambah Data",
        "components": "Filter Bar Multi-Kriteria, Reactive Data Table, Pagination, Status Badges"
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
}`;
}

function getPerStepAiPromptTemplate(scope = 'all', userTitle = '', userDesc = '') {
    const titleText = userTitle.trim() ? userTitle.trim() : (projectPRD.project.name || '[JUDUL APLIKASI]');
    const descText = userDesc.trim() ? `\nDeskripsi Kebutuhan: "${userDesc.trim()}"` : (projectPRD.project.description ? `\nDeskripsi Kebutuhan: "${projectPRD.project.description}"` : '');

    const header = `Anda adalah seorang Principal Enterprise Software Architect.
Berdasarkan ide produk berikut:
JUDUL SISTEM: "${titleText}"${descText}

ATURAN OUTPUT:
1. Hanya keluarkan kode JSON valid di dalam blok \`\`\`json ... \`\`\` tanpa penjelasan di luar blok.
2. Tuliskan konten realistis, mendalam, dan relevan dengan industri tanpa placeholder TODO/dll.`;

    if (scope === 'step1') {
        return `${header}

Tolong rumuskan DEFINISI PROYEK (Step 1) dalam format JSON berikut:
\`\`\`json
{
  "project": {
    "name": "${titleText}",
    "industry": "Sektor Industri (misal: Logistics & Supply Chain, Healthcare, Mining)",
    "department": "Departemen Pengguna Utama",
    "targetOrg": "Target Organisasi / End-User",
    "description": "Deskripsi komprehensif sistem...",
    "problem": "Masalah nyata dan inefisiensi yang dihadapi pengguna saat ini...",
    "objective": "Target kuantitatif & kualitatif bisnis...",
    "scope": "Ruang lingkup yang WAJIB ada (In-Scope)...",
    "outOfScope": "Hal-hal yang TIDAK dikerjakan pada rilis ini (Out-of-Scope)...",
    "successCriteria": "Metrik penentu keberhasilan...",
    "additionalNotes": "Standar kepatuhan / SOP khusus..."
  }
}
\`\`\``;
    }

    if (scope === 'step2') {
        return `${header}

Tolong rekomendasikan PILAR ARSITEKTUR & ARCHETYPE (Step 2) yang paling relevan untuk sistem "${titleText}".
Pilih salah satu nilai "pillar" yang tepat dari 5 pilihan ini:
- "dashboard" (ERP, Control Center, Gudang, Operasional Internal, Work Order, High Data Density)
- "landing_page" (Pemasaran produk/jasa, konversi lead, showcase penawaran)
- "company_profile" (Profil holding korporasi, hubungan investor, ESG)
- "e_commerce" (Toko online, katalog barang, keranjang, checkout & pesanan)
- "blog_content" (Portal berita, artikel riset, publikasi editorial)

Keluarkan dalam format JSON:
\`\`\`json
{
  "taxonomy": {
    "pillar": "dashboard",
    "archetype": "Enterprise Control Center / Operational ERP",
    "rationale": "Alasan arsitektur ini dipilih..."
  }
}
\`\`\``;
    }

    if (scope === 'step3') {
        return `${header}

Tolong buatkan daftar ROLES & PERSONA PENGGUNA (Step 3) minimal 3-5 peran dalam format JSON berikut:
\`\`\`json
{
  "roles": [
    {
      "id": "r1",
      "name": "Nama Jabatan / Peran",
      "department": "Departemen",
      "type": "primary",
      "responsibility": "Tanggung jawab utama dalam operasional sistem...",
      "persona": "Karakteristik pengguna, prioritas kerja, dan ekspektasi antarmuka..."
    },
    {
      "id": "r2",
      "name": "Nama Jabatan 2",
      "department": "Departemen",
      "type": "secondary",
      "responsibility": "Tanggung jawab...",
      "persona": "Persona..."
    }
  ]
}
\`\`\``;
    }

    if (scope === 'step4') {
        return `${header}

Tolong buatkan MODUL & FITUR FUNGSIONAL (Step 4) minimal 3 modul dengan 2-3 fitur per modul dalam format JSON:
\`\`\`json
{
  "modules": [
    {
      "id": "m1",
      "name": "Nama Modul 1",
      "desc": "Tujuan dan fungsi utama modul ini...",
      "features": [
        {
          "id": "f101",
          "name": "Nama Fitur 1.1",
          "priority": "P1 High",
          "desc": "Deskripsi cara kerja fitur...",
          "acceptance": "Kriteria penerimaan pengujian (Acceptance Criteria)..."
        }
      ]
    }
  ]
}
\`\`\``;
    }

    if (scope === 'step5') {
        return `${header}

Tolong buatkan TAHAPAN WORKFLOW & PROSES BISNIS (Step 5) minimal 4-6 tahapan berurutan dalam format JSON:
\`\`\`json
{
  "workflows": [
    {
      "id": "w1",
      "stepNo": 1,
      "name": "Nama Tahapan 1 (misal: Pengajuan Tiket / Permintaan)",
      "actor": "Role Pelaksana",
      "status": "SUBMITTED",
      "trigger": "Pemicu dimulainya tahapan ini...",
      "input": "Data / dokumen yang diperlukan...",
      "action": "Aktivitas yang dieksekusi...",
      "decision": "Aturan validasi / gerbang persetujuan...",
      "output": "Hasil keluaran dan status baru..."
    }
  ]
}
\`\`\``;
    }

    if (scope === 'step6') {
        return `${header}

Tolong buatkan ATURAN BISNIS & CONSTRAINT (Step 6) minimal 3-5 aturan ketat dalam format JSON:
\`\`\`json
{
  "businessRules": [
    {
      "id": "br1",
      "name": "Nama Aturan Bisnis",
      "severity": "Blocking",
      "condition": "Kondisi atau pemicu aturan (misal: Nilai transaksi > 50 juta)...",
      "action": "Tindakan wajib sistem (misal: Wajib approval level 2 & blokir rilis)...",
      "exception": "Pengecualian aturan jika ada...",
      "description": "Penjelasan aturan bisnis..."
    }
  ]
}
\`\`\``;
    }

    if (scope === 'step7') {
        return `${header}

Tolong buatkan SKEMA ENTITAS DATA (Step 7) minimal 2-4 tabel utama lengkap dengan atribut dan tipe data dalam format JSON:
\`\`\`json
{
  "entities": [
    {
      "id": "e1",
      "name": "NamaEntitas (misal: Transaksi, User, Item)",
      "type": "Master / Transactional",
      "storage": "tbl_nama_entitas",
      "desc": "Penjelasan kegunaan entitas data ini...",
      "fields": [
        { "name": "id", "type": "String", "required": "true", "defaultValue": "UUID", "validation": "Unique PK", "desc": "Primary Key" },
        { "name": "kode_ref", "type": "String", "required": "true", "defaultValue": "-", "validation": "Unique", "desc": "Nomor referensi unik" },
        { "name": "status", "type": "String", "required": "true", "defaultValue": "DRAFT", "validation": "-", "desc": "Status rekaman" }
      ]
    }
  ]
}
\`\`\``;
    }

    if (scope === 'step8') {
        return `${header}

Tolong buatkan MATRIKS HAK AKSES / RBAC (Step 8) dalam format JSON pemetaan Role ke Modul:
\`\`\`json
{
  "permissions": {
    "Role 1_Modul 1": { "view": true, "create": true, "edit": true, "delete": false, "approve": true, "export": true },
    "Role 2_Modul 1": { "view": true, "create": true, "edit": true, "delete": true, "approve": false, "export": true }
  }
}
\`\`\``;
    }

    if (scope === 'step9') {
        return `${header}

Tolong buatkan METRIK KPI & REPORTING (Step 9) minimal 3-5 KPI terukur dalam format JSON:
\`\`\`json
{
  "kpis": [
    {
      "id": "k1",
      "name": "Nama Metrik KPI",
      "target": ">= 95%",
      "unit": "% / Jam / Rupiah",
      "formula": "Rumus atau kalkulasi metrik...",
      "source": "Tabel atau modul sumber data...",
      "frequency": "Harian / Mingguan / Real-time",
      "visualization": "Stat Card / Line Trend / Bar Chart",
      "description": "Rasional dan kegunaan metrik bagi manajemen..."
    }
  ]
}
\`\`\``;
    }

    if (scope === 'step10') {
        return `${header}

Tolong buatkan NOTIFIKASI & ALERT OPERASIONAL (Step 10) minimal 3 skenario notifikasi dalam format JSON:
\`\`\`json
{
  "notifications": [
    {
      "id": "n1",
      "name": "Event Pemicu Alert",
      "recipient": "Role Penerima",
      "channel": "In-App Toast / Email / Push Notification",
      "priority": "P1 Critical / P2 High / P3 Normal",
      "escalation": "Aturan eskalasi jika tidak direspon dalam X jam...",
      "template": "[PERINGATAN] Template pesan notifikasi..."
    }
  ]
}
\`\`\``;
    }

    if (scope === 'step11') {
        return `${header}

Tolong buatkan INTEGRASI SISTEM (Step 11) minimal 2 integrasi eksternal (API/Webhook) dalam format JSON:
\`\`\`json
{
  "integrations": [
    {
      "id": "i1",
      "system": "Nama Sistem Eksternal (misal: SAP ERP, Payment Gateway, AD SSO)",
      "direction": "Inbound / Outbound / Bi-directional",
      "frequency": "Real-time Webhook / Batch Harian",
      "purpose": "Tujuan pertukaran data...",
      "data": "Objek data / payload...",
      "auth": "REST API Bearer Token OAuth 2.0",
      "mockNotes": "Simulasi mock array di browser localStorage..."
    }
  ]
}
\`\`\``;
    }

    if (scope === 'step12') {
        return `${header}

Tolong buatkan ARSITEKTUR LAYAR UI/UX & SCREEN MAPPING (Step 12) minimal 3-4 screen halaman utama dalam format JSON:
\`\`\`json
{
  "uiux": {
    "screens": [
      {
        "id": "s1",
        "name": "Dashboard Utama",
        "features": "Stat Cards Ringkasan, Alert Kritis, Quick Action",
        "components": "4 Stat Cards, Data Chart, Filter Bar, Action Buttons"
      },
      {
        "id": "s2",
        "name": "Halaman Manajemen Data",
        "features": "Tabel Berdensitas Tinggi, Multi-Filter, Search, Form Modal",
        "components": "Reactive Data Table, Filter Bar, Pagination, Status Badges"
      }
    ]
  }
}
\`\`\``;
    }

    if (scope === 'step13') {
        return `${header}

Tolong buatkan SPESIFIKASI TEKNIS MVP SINGLE-FILE (Step 13) yang mendefinisikan strategi state lokal dan arsitektur browser dalam format JSON:
\`\`\`json
{
  "techMvp": {
    "notes": "Strategi persistensi localStorage browser, simulasi mock data realistis 10-15 baris, dan penanganan interaktivitas tanpa server eksternal.",
    "stateManagement": "localStorage reactive dispatch",
    "offlineStrategy": "Zero external dependencies, standalone single-file index.html"
  }
}
\`\`\``;
    }

    // Default: Semua 16 langkah
    return getAiPromptTemplate(userTitle, userDesc);
}

function handleAiScopeChange() {
    const scopeSelect = document.getElementById('ai-step-scope-select');
    const scope = scopeSelect ? scopeSelect.value : 'all';
    const conceptInput = document.getElementById('ai-concept-input');
    const step1DescInput = document.getElementById('p-desc');
    const display = document.getElementById('ai-prompt-display');
    const titleVal = conceptInput ? conceptInput.value : '';
    const descVal = (step1DescInput && step1DescInput.value.trim()) ? step1DescInput.value.trim() : (projectPRD.project.description || '');

    const badge = document.getElementById('ai-prompt-title-badge');
    const importBadge = document.getElementById('ai-import-scope-indicator');
    const btnLabel = document.getElementById('btn-process-import-label');

    if (display) {
        display.value = getPerStepAiPromptTemplate(scope, titleVal, descVal);
    }

    if (scope === 'all') {
        if (badge) badge.textContent = 'Isi Prompt Semua 16 Langkah:';
        if (importBadge) {
            importBadge.className = 'badge badge-indigo';
            importBadge.textContent = 'Target: Semua 16 Langkah';
        }
        if (btnLabel) btnLabel.textContent = 'Proses & Isi Otomatis Seluruh 16 Langkah PRD';
    } else {
        const text = scopeSelect ? scopeSelect.options[scopeSelect.selectedIndex].text : scope;
        if (badge) badge.textContent = `Isi Prompt Khusus: ${text}`;
        if (importBadge) {
            importBadge.className = 'badge badge-emerald';
            importBadge.textContent = `Target Khusus: ${text}`;
        }
        if (btnLabel) btnLabel.textContent = `Terapkan Data ke ${text}`;
    }
}

function openAiPromptFormatModal(preselectedScope = null) {
    if (currentStep === 1) saveStep1Inputs();
    const displayBox = document.getElementById('ai-prompt-display');
    const conceptInput = document.getElementById('ai-concept-input');
    const pasteBox = document.getElementById('ai-paste-json-box');
    const scopeSelect = document.getElementById('ai-step-scope-select');

    const step1NameInput = document.getElementById('p-name');
    const step1DescInput = document.getElementById('p-desc');
    const currentName = (step1NameInput && step1NameInput.value.trim()) ? step1NameInput.value.trim() : (projectPRD.project.name || '');
    const currentDesc = (step1DescInput && step1DescInput.value.trim()) ? step1DescInput.value.trim() : (projectPRD.project.description || '');

    if (conceptInput) {
        conceptInput.value = currentName;
    }

    // Set scope selector
    if (preselectedScope && scopeSelect) {
        scopeSelect.value = preselectedScope;
    } else if (scopeSelect && (!preselectedScope && currentStep > 1)) {
        // Otomatis arahkan ke step saat ini jika user sedang di step tertentu
        const stepMapping = {
            1: 'step1', 3: 'step3', 4: 'step4', 5: 'step5', 6: 'step6',
            7: 'step7', 8: 'step8', 9: 'step9', 10: 'step10', 11: 'step11', 13: 'step13'
        };
        if (stepMapping[currentStep]) {
            scopeSelect.value = stepMapping[currentStep];
        } else {
            scopeSelect.value = 'all';
        }
    }

    const activeScope = scopeSelect ? scopeSelect.value : 'all';

    if (displayBox) {
        displayBox.value = getPerStepAiPromptTemplate(activeScope, currentName, currentDesc);
    }
    if (pasteBox) {
        pasteBox.value = '';
    }

    handleAiScopeChange();
    switchAiModalTab('prompt');
    openModal('modal-ai-json');
}

function switchAiModalTab(tab) {
    const promptBtn = document.getElementById('tab-ai-prompt-btn');
    const importBtn = document.getElementById('tab-ai-import-btn');
    const promptPanel = document.getElementById('ai-tab-prompt-panel');
    const importPanel = document.getElementById('ai-tab-import-panel');

    if (tab === 'prompt') {
        if (promptBtn) {
            promptBtn.style.borderBottomColor = '#6366F1';
            promptBtn.style.color = '#FFFFFF';
            promptBtn.style.fontWeight = '700';
        }
        if (importBtn) {
            importBtn.style.borderBottomColor = 'transparent';
            importBtn.style.color = '#94A3B8';
            importBtn.style.fontWeight = '400';
        }
        if (promptPanel) promptPanel.style.display = 'block';
        if (importPanel) importPanel.style.display = 'none';
    } else {
        if (promptBtn) {
            promptBtn.style.borderBottomColor = 'transparent';
            promptBtn.style.color = '#94A3B8';
            promptBtn.style.fontWeight = '400';
        }
        if (importBtn) {
            importBtn.style.borderBottomColor = '#10B981';
            importBtn.style.color = '#FFFFFF';
            importBtn.style.fontWeight = '700';
        }
        if (promptPanel) promptPanel.style.display = 'none';
        if (importPanel) importPanel.style.display = 'block';
    }
}

function updateAiPromptWithConcept() {
    const input = document.getElementById('ai-concept-input');
    const step1DescInput = document.getElementById('p-desc');
    const display = document.getElementById('ai-prompt-display');
    const scopeSelect = document.getElementById('ai-step-scope-select');
    const scope = scopeSelect ? scopeSelect.value : 'all';
    const descVal = (step1DescInput && step1DescInput.value.trim()) ? step1DescInput.value.trim() : (projectPRD.project.description || '');
    if (display) {
        display.value = getPerStepAiPromptTemplate(scope, input ? input.value : '', descVal);
    }
}

function copyAiGeneratorPrompt() {
    const display = document.getElementById('ai-prompt-display');
    if (!display || !display.value) return;

    navigator.clipboard.writeText(display.value).then(() => {
        Swal.fire({
            toast: true,
            position: 'top-end',
            icon: 'success',
            title: 'Format Prompt AI Berhasil Disalin!',
            text: 'Tempelkan langsung ke ChatGPT, Gemini, atau Claude.',
            showConfirmButton: false,
            timer: 2500,
            background: '#0D111A',
            color: '#F8FAFC'
        });
    }).catch(err => {
        // Fallback
        display.select();
        document.execCommand('copy');
        Swal.fire({
            toast: true,
            position: 'top-end',
            icon: 'success',
            title: 'Format Prompt AI Berhasil Disalin!',
            showConfirmButton: false,
            timer: 2000,
            background: '#0D111A',
            color: '#F8FAFC'
        });
    });
}

function downloadEmptyJsonTemplate() {
    const cleanTemplate = getEmptyProject();
    // Add sample placeholder references
    cleanTemplate.project.name = 'Contoh Aplikasi Enterprise';
    cleanTemplate.taxonomy.pillar = 'dashboard';
    cleanTemplate.taxonomy.archetype = 'Enterprise ERP / Control Center';

    const dataStr = JSON.stringify(cleanTemplate, null, 2);
    const blob = new Blob([dataStr], { type: 'application/json;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'template_enterprise_prd.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

function handleAiJsonFileSelected(event) {
    const file = event.target.files[0];
    if (!file) return;

    const label = document.getElementById('ai-file-label');
    if (label) label.textContent = `File dipilih: ${file.name}`;

    const reader = new FileReader();
    reader.onload = function(e) {
        const pasteBox = document.getElementById('ai-paste-json-box');
        if (pasteBox) {
            pasteBox.value = e.target.result;
        }
    };
    reader.readAsText(file);
}

function cleanAndParseJson(rawText) {
    if (!rawText) throw new Error('Kode JSON tidak boleh kosong.');
    let text = rawText.trim();

    // Strip markdown code fences if AI returned ```json ... ``` or ``` ... ```
    if (text.startsWith('```')) {
        const firstNewLine = text.indexOf('\n');
        if (firstNewLine !== -1) {
            text = text.substring(firstNewLine + 1);
        }
    }
    if (text.endsWith('```')) {
        text = text.substring(0, text.length - 3);
    }
    text = text.trim();

    // Try finding outer curly braces if extra commentary surrounded the JSON
    const firstBrace = text.indexOf('{');
    const lastBrace = text.lastIndexOf('}');
    if (firstBrace !== -1 && lastBrace !== -1 && lastBrace > firstBrace) {
        text = text.substring(firstBrace, lastBrace + 1);
    }

    try {
        return JSON.parse(text);
    } catch (e1) {
        // Fallback: strip trailing commas before closing braces/brackets (common LLM JSON flaw)
        try {
            const cleaned = text
                .replace(/,\s*([\]}])/g, '$1');
            return JSON.parse(cleaned);
        } catch (e2) {
            throw new Error(`Format JSON tidak valid: ${e1.message}`);
        }
    }
}

function getAiSettings() {
    try {
        const saved = localStorage.getItem('enterprise_prd_ai_settings');
        if (saved) {
            const parsed = JSON.parse(saved);
            return {
                baseUrl: parsed.baseUrl || 'https://siaptuan.my.id/v1',
                model: parsed.model || 'gpt-5.6-luna.st',
                apiKey: parsed.apiKey || ''
            };
        }
    } catch (e) {
        console.warn('Error reading AI settings:', e);
    }
    return {
        baseUrl: 'https://siaptuan.my.id/v1',
        model: 'gpt-5.6-luna.st',
        apiKey: ''
    };
}

const AI_PRESETS = {
    'siaptuan': {
        name: 'SiapTuan Luna',
        baseUrl: 'https://siaptuan.my.id/v1',
        model: 'gpt-5.6-luna.st'
    },
    'openai': {
        name: 'OpenAI (GPT-4o Mini)',
        baseUrl: 'https://api.openai.com/v1',
        model: 'gpt-4o-mini'
    },
    'groq': {
        name: 'Groq (Llama 3.3)',
        baseUrl: 'https://api.groq.com/openai/v1',
        model: 'llama-3.3-70b-versatile'
    },
    'openrouter': {
        name: 'OpenRouter (Llama 3.3)',
        baseUrl: 'https://openrouter.ai/api/v1',
        model: 'meta-llama/llama-3.3-70b-instruct'
    },
    'ollama': {
        name: 'Ollama Localhost',
        baseUrl: 'http://localhost:11434/v1',
        model: 'qwen2.5-coder:latest'
    }
};

function setAiPreset(key) {
    const preset = AI_PRESETS[key];
    if (!preset) return;

    const baseUrlInput = document.getElementById('ai-settings-base-url');
    const modelInput = document.getElementById('ai-settings-model');

    if (baseUrlInput) baseUrlInput.value = preset.baseUrl;
    if (modelInput) modelInput.value = preset.model;

    document.querySelectorAll('.ai-preset-btn').forEach(btn => {
        if (btn.getAttribute('data-preset') === key) {
            btn.style.borderColor = '#38BDF8';
            btn.style.background = 'rgba(56,189,248,0.2)';
            btn.style.color = '#FFFFFF';
        } else {
            btn.style.borderColor = '#334155';
            btn.style.background = '#0F172A';
            btn.style.color = '#E2E8F0';
        }
    });

    Swal.fire({
        toast: true,
        position: 'top-end',
        icon: 'info',
        title: `Preset: ${preset.name}`,
        text: preset.baseUrl,
        showConfirmButton: false,
        timer: 1800,
        background: '#0D111A',
        color: '#F8FAFC'
    });
}

function getNormalizedAiEndpoint(rawUrl) {
    let url = (rawUrl || '').trim();
    if (!url) url = 'https://siaptuan.my.id/v1';
    url = url.replace(/\/+$/, '');
    if (url.endsWith('/chat/completions')) {
        return url;
    }
    return `${url}/chat/completions`;
}

function resolveAiProxyEndpoints() {
    const isFile = window.location.protocol === 'file:';
    const hostname = window.location.hostname || '';
    const isVercel = hostname.endsWith('vercel.app') || hostname.includes('vercel');
    const isLocalhost = hostname === 'localhost' || hostname === '127.0.0.1';

    let candidates = [];

    if (isVercel) {
        // Lingkungan Vercel Cloud (ui-ux-design-template.vercel.app)
        candidates.push({ url: '/api/proxy', name: 'Vercel Serverless (/api/proxy)', type: 'vercel' });
    } else if (isLocalhost) {
        // Lingkungan Localhost (XAMPP Apache / PHP)
        candidates.push({ url: 'ai_proxy.php', name: 'Local XAMPP (ai_proxy.php)', type: 'php' });
        candidates.push({ url: '/api/proxy', name: 'Local Vercel Dev (/api/proxy)', type: 'vercel' });
        candidates.push({ url: 'https://ui-ux-design-template.vercel.app/api/proxy', name: 'Vercel Cloud Fallback', type: 'vercel_cloud' });
    } else if (isFile) {
        // Lingkungan File Protocol (file:///...)
        candidates.push({ url: 'http://localhost/UI%20UX%20Design/ai_proxy.php', name: 'Local Apache Port 80', type: 'php' });
        candidates.push({ url: 'https://ui-ux-design-template.vercel.app/api/proxy', name: 'Vercel Cloud Gateway', type: 'vercel_cloud' });
    } else {
        // Custom domain lain
        candidates.push({ url: '/api/proxy', name: 'Serverless Proxy (/api/proxy)', type: 'vercel' });
        candidates.push({ url: 'ai_proxy.php', name: 'PHP Proxy (ai_proxy.php)', type: 'php' });
        candidates.push({ url: 'https://ui-ux-design-template.vercel.app/api/proxy', name: 'Vercel Cloud Fallback', type: 'vercel_cloud' });
    }

    return candidates;
}

async function checkAiProxyHealth() {
    const statusBanner = document.getElementById('ai-proxy-status-banner');
    if (!statusBanner) return;

    statusBanner.innerHTML = `
        <div style="display:flex; align-items:center; gap:8px;">
            <i class="fa-solid fa-circle-notch fa-spin" style="color:#38BDF8;"></i>
            <span>Memeriksa status AI Proxy (Vercel Serverless / Local XAMPP)...</span>
        </div>
    `;

    const candidates = resolveAiProxyEndpoints();

    for (const candidate of candidates) {
        try {
            const ctrl = new AbortController();
            const timeoutId = setTimeout(() => ctrl.abort(), 3500);
            const res = await fetch(candidate.url, { method: 'GET', signal: ctrl.signal });
            clearTimeout(timeoutId);

            if (res.ok) {
                const data = await res.json();
                statusBanner.style.background = 'rgba(16,185,129,0.08)';
                statusBanner.style.border = '1px solid rgba(16,185,129,0.3)';
                statusBanner.style.color = '#6EE7B7';

                let platformLabel = candidate.type === 'vercel' 
                    ? 'Vercel Serverless (/api/proxy)' 
                    : (candidate.type === 'vercel_cloud' ? 'Vercel Cloud Gateway' : 'Apache XAMPP Port 80');

                statusBanner.innerHTML = `
                    <div style="display:flex; justify-content:space-between; align-items:center; width:100%;">
                        <div style="display:flex; align-items:center; gap:8px;">
                            <i class="fa-solid fa-circle-check" style="color:#10B981; font-size:14px;"></i>
                            <div>
                                <div style="font-weight:700; color:#FFFFFF; font-size:12px;">Proxy Aktif (${escapeHtml(platformLabel)})</div>
                                <div style="font-size:10.5px; color:#A7F3D0;">Bypass CORS berjalan lancar via ${escapeHtml(candidate.name)}.</div>
                            </div>
                        </div>
                        <span class="badge badge-emerald" style="font-size:10px; padding:2px 8px;">Online</span>
                    </div>
                `;
                return true;
            }
        } catch (_) {
            // Lanjut ke kandidat berikutnya
        }
    }

    statusBanner.style.background = 'rgba(245,158,11,0.08)';
    statusBanner.style.border = '1px solid rgba(245,158,11,0.3)';
    statusBanner.style.color = '#FDE68A';

    const isVercel = (window.location.hostname || '').includes('vercel');
    let advice = isVercel
        ? 'Pastikan file <code>api/proxy.js</code> sudah ter-deploy di Vercel.'
        : 'Pastikan Apache XAMPP aktif, atau gunakan deployment Vercel dengan file <code>api/proxy.js</code>.';

    statusBanner.innerHTML = `
        <div style="display:flex; align-items:flex-start; gap:8px; width:100%;">
            <i class="fa-solid fa-triangle-exclamation" style="color:#F59E0B; margin-top:2px; font-size:14px; flex-shrink:0;"></i>
            <div style="font-size:11.5px; line-height:1.5;">
                <strong style="color:#FFFFFF;">Proxy Offline:</strong> ${advice}
            </div>
        </div>
    `;
    return false;
}

function saveAiSettings() {
    const baseUrlInput = document.getElementById('ai-settings-base-url');
    const modelInput = document.getElementById('ai-settings-model');
    const keyInput = document.getElementById('ai-settings-key');

    let baseUrl = baseUrlInput ? baseUrlInput.value.trim() : '';
    let model = modelInput ? modelInput.value.trim() : '';
    let apiKey = keyInput ? keyInput.value.trim() : '';

    if (!baseUrl) baseUrl = 'https://siaptuan.my.id/v1';
    if (!model) model = 'gpt-5.6-luna.st';

    const settings = { baseUrl, model, apiKey };
    localStorage.setItem('enterprise_prd_ai_settings', JSON.stringify(settings));

    closeModal('modal-ai-settings');

    Swal.fire({
        toast: true,
        position: 'top-end',
        icon: 'success',
        title: 'Pengaturan AI Berhasil Disimpan!',
        text: `Model: ${model}`,
        showConfirmButton: false,
        timer: 2500,
        background: '#0D111A',
        color: '#F8FAFC'
    });
}

function openAiSettingsModal() {
    const settings = getAiSettings();
    const baseUrlInput = document.getElementById('ai-settings-base-url');
    const modelInput = document.getElementById('ai-settings-model');
    const keyInput = document.getElementById('ai-settings-key');
    const keyStatus = document.getElementById('ai-key-status');

    if (baseUrlInput) baseUrlInput.value = settings.baseUrl;
    if (modelInput) modelInput.value = settings.model;
    if (keyInput) keyInput.value = settings.apiKey;

    if (keyStatus) {
        if (settings.apiKey) {
            keyStatus.className = 'badge badge-emerald';
            keyStatus.textContent = 'API Key Tersedia';
        } else {
            keyStatus.className = 'badge badge-slate';
            keyStatus.textContent = 'Belum Ada Key';
        }
    }

    openModal('modal-ai-settings');
    checkAiProxyHealth();
}

function toggleAiApiKeyVisibility() {
    const keyInput = document.getElementById('ai-settings-key');
    const icon = document.getElementById('ai-key-toggle-icon');
    if (!keyInput || !icon) return;

    if (keyInput.type === 'password') {
        keyInput.type = 'text';
        icon.className = 'fa-solid fa-eye-slash';
    } else {
        keyInput.type = 'password';
        icon.className = 'fa-solid fa-eye';
    }
}

async function callAiChatCompletions(endpoint, apiKey, payload) {
    let lastDirectError = null;

    // 1. Coba direct fetch terlebih dahulu (Bekerja sempurna jika endpoint mendukung CORS, misal OpenAI, Groq, OpenRouter)
    try {
        const directRes = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`
            },
            body: JSON.stringify(payload)
        });

        if (directRes.ok) {
            return await directRes.json();
        }

        let errDetail = `HTTP ${directRes.status}`;
        try {
            const errJson = await directRes.json();
            if (errJson && errJson.error && errJson.error.message) {
                errDetail = errJson.error.message;
            } else if (errJson && typeof errJson === 'object') {
                errDetail = JSON.stringify(errJson);
            }
        } catch (_) {
            const txt = await directRes.text();
            if (txt) errDetail = txt.substring(0, 200);
        }

        if (directRes.status === 401 || directRes.status === 403 || directRes.status === 429) {
            throw new Error(`[API Error ${directRes.status}] ${errDetail}`);
        }
        lastDirectError = new Error(`Direct fetch HTTP ${directRes.status}: ${errDetail}`);
    } catch (err) {
        if (err.message && err.message.startsWith('[API Error')) {
            throw err;
        }
        lastDirectError = err;
        console.warn('Direct fetch tidak dapat menjangkau server (kemungkinan CORS / Origin di browser). Mengalihkan ke Proxy...', err);
    }

    // 2. Fallback melalui Proxy (Mendukung Vercel Serverless & Local XAMPP PHP)
    const candidates = resolveAiProxyEndpoints();
    let proxyErrors = [];

    for (const candidate of candidates) {
        try {
            const proxyRes = await fetch(candidate.url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    endpoint: endpoint,
                    apiKey: apiKey,
                    body: payload
                })
            });

            let proxyData;
            try {
                proxyData = await proxyRes.json();
            } catch (_) {
                const raw = await proxyRes.text();
                throw new Error(`Output proxy ${candidate.name} tidak valid (${proxyRes.status}): ${raw.substring(0, 200)}`);
            }

            if (proxyRes.ok) {
                return proxyData;
            }

            let detailMsg = `HTTP ${proxyRes.status}`;
            if (proxyData && proxyData.error && proxyData.error.message) {
                detailMsg = proxyData.error.message;
            } else if (proxyData && typeof proxyData === 'object') {
                detailMsg = JSON.stringify(proxyData);
            }

            throw new Error(`[AI Provider Error] ${detailMsg}`);

        } catch (candidateErr) {
            if (candidateErr.message && candidateErr.message.startsWith('[AI Provider Error]')) {
                throw candidateErr;
            }
            proxyErrors.push(`${candidate.name}: ${candidateErr.message}`);
        }
    }

    // 3. Jika semua proxy gagal
    let errorMsg = `Gagal Menghubungkan ke Endpoint AI maupun Proxy.\n\n`;
    errorMsg += `Target Endpoint: ${endpoint}\n`;
    errorMsg += `Error Direct: ${lastDirectError ? lastDirectError.message : 'Network / CORS limitation'}\n`;
    errorMsg += `Log Proxy:\n - ${proxyErrors.join('\n - ')}\n\n`;

    const isVercel = (window.location.hostname || '').includes('vercel');
    if (isVercel) {
        errorMsg += `PANDUAN SOLUSI (Vercel Cloud):\n`;
        errorMsg += `1. Pastikan file api/proxy.js sudah ter-deploy di Vercel.\n`;
        errorMsg += `2. Jika terjadi timeout 55 detik, gunakan fitur "Isi Per Step" yang jauh lebih ringan.\n`;
    } else {
        errorMsg += `PANDUAN SOLUSI:\n`;
        errorMsg += `1. Pastikan Apache di XAMPP Control Panel aktif, ATAU gunakan deployment Vercel.\n`;
        errorMsg += `2. Anda juga dapat memilih preset provider super-cepat (Groq / OpenAI) di Pengaturan AI.\n`;
    }

    throw new Error(errorMsg);
}

async function testAiConnection() {
    const baseUrlInput = document.getElementById('ai-settings-base-url');
    const modelInput = document.getElementById('ai-settings-model');
    const keyInput = document.getElementById('ai-settings-key');

    let baseUrl = baseUrlInput ? baseUrlInput.value.trim() : '';
    let model = modelInput ? modelInput.value.trim() : '';
    const apiKey = keyInput ? keyInput.value.trim() : '';

    if (!baseUrl) baseUrl = 'https://siaptuan.my.id/v1';
    if (!model) model = 'gpt-5.6-luna.st';

    if (!apiKey) {
        Swal.fire({
            icon: 'warning',
            title: 'API Key Belum Diisi',
            text: 'Masukkan API Key Anda terlebih dahulu untuk menguji koneksi.',
            background: '#0D111A',
            color: '#F8FAFC'
        });
        return;
    }

    const endpoint = getNormalizedAiEndpoint(baseUrl);
    const startTime = performance.now();

    Swal.fire({
        title: 'Menguji Koneksi AI...',
        html: `<div style="font-size:12px; color:#94A3B8; margin-top:8px;">Menghubungkan ke <code>${escapeHtml(endpoint)}</code><br>Model: <code>${escapeHtml(model)}</code></div>`,
        allowOutsideClick: false,
        background: '#0D111A',
        color: '#F8FAFC',
        didOpen: () => {
            Swal.showLoading();
        }
    });

    try {
        const data = await callAiChatCompletions(endpoint, apiKey, {
            model: model,
            messages: [
                { role: 'user', content: 'Ping! Respond with the single word "OK" only.' }
            ],
            max_tokens: 30
        });

        const latencyMs = Math.round(performance.now() - startTime);
        const reply = data.choices && data.choices[0] && data.choices[0].message ? data.choices[0].message.content : 'OK';

        Swal.fire({
            icon: 'success',
            title: 'Koneksi Berhasil!',
            html: `
                <div style="font-size:13px; color:#E2E8F0; margin-bottom:10px;">
                    Endpoint &amp; API Key valid. Respon diterima dalam <strong>${latencyMs} ms</strong>.
                </div>
                <div style="background:#07090E; border:1px solid #1E293B; border-radius:8px; padding:10px; font-size:11.5px; text-align:left; color:#94A3B8;">
                    <div><strong>Model:</strong> <code>${escapeHtml(model)}</code></div>
                    <div><strong>Respon:</strong> <code style="color:#34D399;">${escapeHtml(reply.trim())}</code></div>
                </div>
            `,
            background: '#0D111A',
            color: '#F8FAFC',
            confirmButtonColor: '#10B981'
        });
    } catch (err) {
        Swal.fire({
            icon: 'error',
            title: 'Koneksi Gagal',
            html: `<div style="font-size:12px; color:#F43F5E; text-align:left; background:#080C14; padding:12px; border-radius:6px; border:1px solid #334155; word-break:break-word; white-space:pre-line; max-height:280px; overflow-y:auto;">${escapeHtml(err.message)}</div>`,
            background: '#0D111A',
            color: '#F8FAFC',
            confirmButtonColor: '#F43F5E'
        });
    }
}

function applyPrdData(data, sourceLabel = 'AI') {
    if (!data || typeof data !== 'object') {
        throw new Error('Format data tidak valid atau bukan objek.');
    }
    if (!data.project) {
        throw new Error('Objek data wajib memiliki properti "project".');
    }

    // Robust Mapping & Normalization for AI Output
    if (!data.taxonomy) data.taxonomy = { pillar: 'dashboard', archetype: 'Enterprise ERP / Control Center' };
    if (!data.taxonomy.pillar || !['dashboard', 'landing_page', 'company_profile', 'e_commerce', 'blog_content'].includes(data.taxonomy.pillar)) {
        data.taxonomy.pillar = 'dashboard';
    }
    if (!data.taxonomy.archetype) {
        const pObj = getPillarObj(data.taxonomy.pillar);
        data.taxonomy.archetype = pObj ? pObj.archetype : 'Enterprise Architecture';
    }

    // Project fields normalization
    if (!data.project.additionalNotes && data.project.additionalRequirements) {
        data.project.additionalNotes = data.project.additionalRequirements;
    }

    if (!data.roles) data.roles = [];
    data.roles = data.roles.map((r, idx) => ({
        id: r.id || 'r_' + (idx + 1),
        name: r.name || 'Role ' + (idx + 1),
        department: r.department || r.dept || 'Operasional',
        type: (r.type && String(r.type).toLowerCase() === 'secondary') ? 'secondary' : 'primary',
        responsibility: r.responsibility || r.resp || r.description || '',
        persona: r.persona || ''
    }));

    if (!data.modules) data.modules = [];
    data.modules = data.modules.map((m, idx) => ({
        id: m.id || 'm_' + (idx + 1),
        name: m.name || 'Modul ' + (idx + 1),
        description: m.description || m.desc || '',
        submodules: m.submodules || (Array.isArray(m.features) ? m.features.map(f => f.name).join(', ') : ''),
        features: Array.isArray(m.features) ? m.features : []
    }));

    if (!data.features) data.features = [];
    // Extract features from modules if projectPRD.features is empty but modules have features
    let flattenedFeats = [];
    data.modules.forEach(m => {
        if (m.features && Array.isArray(m.features)) {
            m.features.forEach((f, fIdx) => {
                flattenedFeats.push({
                    id: f.id || 'f_' + m.id + '_' + (fIdx + 1),
                    moduleId: m.id,
                    name: f.name || 'Fitur ' + (fIdx + 1),
                    priority: f.priority || 'P1',
                    primaryUser: f.primaryUser || (data.roles[0] ? data.roles[0].name : ''),
                    description: f.description || f.desc || '',
                    dependencies: f.dependencies || m.name,
                    expectedOutcome: f.expectedOutcome || f.acceptance || ''
                });
            });
        }
    });
    if (flattenedFeats.length > 0 && data.features.length === 0) {
        data.features = flattenedFeats;
    } else {
        data.features = data.features.map((f, idx) => ({
            id: f.id || 'f_' + (idx + 1),
            moduleId: f.moduleId || (data.modules[0] ? data.modules[0].id : ''),
            name: f.name || 'Fitur ' + (idx + 1),
            priority: f.priority || 'P1',
            primaryUser: f.primaryUser || (data.roles[0] ? data.roles[0].name : ''),
            description: f.description || f.desc || '',
            dependencies: f.dependencies || '',
            expectedOutcome: f.expectedOutcome || f.acceptance || ''
        }));
    }

    if (!data.workflows) data.workflows = [];
    data.workflows = data.workflows.map((w, idx) => ({
        id: w.id || 'w_' + (idx + 1),
        stepNo: w.stepNo || (idx + 1),
        name: w.name || 'Tahap ' + (idx + 1),
        actor: w.actor || (data.roles[0] ? data.roles[0].name : 'User'),
        trigger: w.trigger || '',
        input: w.input || '',
        action: w.action || '',
        decision: w.decision || '',
        output: w.output || '',
        status: w.status || 'ACTIVE'
    }));

    if (!data.businessRules) data.businessRules = [];
    data.businessRules = data.businessRules.map((br, idx) => ({
        id: br.id || 'br_' + (idx + 1),
        name: br.name || 'Aturan Bisnis ' + (idx + 1),
        severity: br.severity || br.level || 'Blocking',
        condition: br.condition || br.ruleStatement || 'Validasi Input',
        action: br.action || br.failAction || 'Tolak & Beri Notifikasi',
        exception: br.exception || 'Tidak ada pengecualian.',
        description: br.description || br.desc || br.ruleStatement || ''
    }));

    if (!data.entities) data.entities = [];
    data.entities = data.entities.map((e, idx) => ({
        id: e.id || 'e_' + (idx + 1),
        name: e.name || 'Entitas_' + (idx + 1),
        description: e.description || e.desc || '',
        type: e.type || (idx === 0 ? 'Master' : 'Transactional'),
        storage: e.storage || e.code || ('tbl_' + (e.name || 'entity').toLowerCase()),
        fields: (e.fields || []).map((f, fIdx) => ({
            id: f.id || 'fld_' + (fIdx + 1),
            name: f.name || 'field_' + (fIdx + 1),
            type: f.type || 'String',
            required: f.required !== undefined ? String(f.required) : 'true',
            defaultValue: f.defaultValue || '-',
            validation: f.validation || '-',
            description: f.description || f.desc || '-'
        })),
        relationships: e.relationships || []
    }));

    if (!data.kpis) data.kpis = [];
    data.kpis = data.kpis.map((k, idx) => ({
        id: k.id || 'kpi_' + (idx + 1),
        name: k.name || 'KPI ' + (idx + 1),
        target: k.target || '>= 95%',
        unit: k.unit || '%',
        formula: k.formula || 'Kalkulasi Otomatis',
        source: k.source || (data.entities[0] ? data.entities[0].name : 'Sistem'),
        frequency: k.frequency || 'Harian',
        visualization: k.visualization || 'Stat Card',
        description: k.description || k.desc || ''
    }));

    if (!data.notifications) data.notifications = [];
    data.notifications = data.notifications.map((n, idx) => ({
        id: n.id || 'n_' + (idx + 1),
        name: n.name || n.event || 'Notifikasi ' + (idx + 1),
        trigger: n.trigger || n.triggerCondition || '',
        recipient: n.recipient || (data.roles[0] ? data.roles[0].name : 'Semua Role'),
        channel: n.channel || 'In-App Toast',
        priority: n.priority || 'P2 High',
        escalation: n.escalation || 'Teruskan ke atasan',
        template: n.template || n.messageTemplate || ('[INFO] Notifikasi ' + (n.name || 'sistem'))
    }));

    if (!data.integrations) data.integrations = [];
    data.integrations = data.integrations.map((i, idx) => ({
        id: i.id || 'i_' + (idx + 1),
        system: i.system || i.systemName || 'Sistem Eksternal',
        direction: i.direction || 'Inbound',
        frequency: i.frequency || 'Real-time Webhook',
        purpose: i.purpose || 'Pertukaran data operasional',
        data: i.data || i.dataPayload || 'JSON Payload',
        auth: i.auth || i.protocolAuth || 'REST API Bearer Token',
        mockNotes: i.mockNotes || i.offlineSimulation || 'Disimulasikan dengan mock array di browser'
    }));

    if (!data.uiux) data.uiux = { themeId: 2, themeName: 'Bento UI', layout: 'sidebar_topbar', navigation: 'sidebar', accessibility: 'wcag_aa', screens: [] };
    if (!data.uiux.screens) data.uiux.screens = [];
    data.uiux.screens = data.uiux.screens.map((s, idx) => ({
        id: s.id || 's_' + (idx + 1),
        name: s.name || 'Screen ' + (idx + 1),
        features: s.features || (data.features[idx] ? data.features[idx].name : 'Ringkasan & Aksi'),
        components: s.components || 'Stat Cards, Data Table, Filter Bar'
    }));

    if (!data.permissions || Object.keys(data.permissions).length === 0) {
        data.permissions = {};
    }

    if (!data.technicalMVP) {
        data.technicalMVP = {
            frontend: 'HTML5',
            styling: 'Vanilla CSS / Tailwind CDN Tokens',
            logic: 'Vanilla JavaScript ES6+',
            storage: 'localStorage & Reactive Mock Arrays',
            backend: 'None (Pure Client-Side State)',
            database: 'None (In-Memory JSON Collection)',
            auth: 'Mock Role Switcher (Client-side Session)',
            deployment: 'Standalone Single-File index.html'
        };
    }

    // Assign to centralized State
    projectPRD = data;

    // Inisialisasi default permissions jika kosong
    if (Object.keys(projectPRD.permissions).length === 0) {
        initDefaultRbacMatrix();
    }

    // Synchronize form to DOM FIRST before saving!
    syncStep1Form();

    // Persist & Save automatic draft
    saveProject(false);
    saveQuickDraft();

    // Synchronize and re-render all 16 steps
    initTaxonomyUI();
    if (projectPRD.taxonomy.pillar) {
        document.querySelectorAll('.pillar-card-hero').forEach(card => card.classList.remove('selected'));
        const targetPillar = document.getElementById(`pillar-card-${projectPRD.taxonomy.pillar}`);
        if (targetPillar) targetPillar.classList.add('selected');
        updatePillarSummary();
    }

    renderRoles();
    renderModulesAndFeatures();
    renderWorkflowNodes();
    renderBusinessRules();
    renderEntities();
    renderRbacMatrix();
    renderKpis();
    renderNotifications();
    renderIntegrations();

    if (projectPRD.uiux.themeId && typeof selectTheme === 'function') {
        selectTheme(projectPRD.uiux.themeId);
    } else {
        renderThemeGrid();
    }
    renderScreens();
    updateUiMetadata();
    checkCompleteness();

    goToStep(1);

    const score = calculateCompletenessScore();

    Swal.fire({
        icon: 'success',
        title: `${sourceLabel} Berhasil Mengisi PRD!`,
        html: `Proyek <strong>"${escapeHtml(projectPRD.project.name || 'Proyek Baru')}"</strong> telah terisi otomatis di seluruh 16 tahapan.<br><br>
               <span class="badge badge-emerald" style="font-size:12px; padding:4px 12px;">Kelengkapan PRD: ${score}%</span>
               <div style="font-size:11.5px; color:#94A3B8; margin-top:10px;">Silakan tinjau dan edit poin-poin yang diperlukan pada tiap langkah.</div>`,
        background: '#0D111A',
        color: '#F8FAFC',
        confirmButtonColor: '#6366F1'
    });
}

async function generatePrdWithDirectAi() {
    const alertResult = await Swal.fire({
        title: 'Rekomendasi: Generate Per-Step',
        icon: 'info',
        html: `
            <div style="font-size:12.5px; color:#94A3B8; text-align:left; line-height:1.6; background:#080C14; padding:14px; border-radius:10px; border:1px solid #1E293B;">
                <p style="margin-bottom:10px; color:#FCA5A5;">
                    <i class="fa-solid fa-triangle-exclamation" style="color:#F43F5E; margin-right:4px;"></i>
                    Mengisi seluruh 16 tahapan sekaligus memerlukan waktu sangat lama (&gt; 60 detik) sehingga rawan <strong>timeout / error</strong> pada koneksi serverless.
                </p>
                <p style="color:#38BDF8; font-weight:700; margin-bottom:0;">
                    <i class="fa-solid fa-wand-magic-sparkles" style="color:#FDE047; margin-right:4px;"></i>
                    Gunakan <strong>"Isi Step Ini by AI"</strong> di setiap langkah (hanya butuh 5–15 detik, super cepat &amp; 100% bebas error).
                </p>
            </div>
        `,
        showCancelButton: true,
        confirmButtonText: `<i class="fa-solid fa-wand-magic-sparkles"></i> Isi Step ${currentStep} by AI (Cepat)`,
        cancelButtonText: 'Tetap Coba Isi Semua',
        confirmButtonColor: '#6366F1',
        cancelButtonColor: '#334155',
        background: '#0D111A',
        color: '#F8FAFC'
    });

    if (alertResult.isConfirmed) {
        generateCurrentStepByAi();
        return;
    }

    if (alertResult.dismiss !== Swal.DismissReason.cancel) {
        return;
    }

    if (currentStep === 1) saveStep1Inputs();

    const nameInput = document.getElementById('p-name');
    const descInput = document.getElementById('p-desc');
    const problemInput = document.getElementById('p-problem');
    const notesInput = document.getElementById('p-additional');

    const title = nameInput ? nameInput.value.trim() : (projectPRD.project.name || '');
    let detailedDesc = descInput ? descInput.value.trim() : (projectPRD.project.description || '');

    if (problemInput && problemInput.value.trim()) {
        detailedDesc += `\nMasalah: ${problemInput.value.trim()}`;
    }
    if (notesInput && notesInput.value.trim()) {
        detailedDesc += `\nCatatan Khusus: ${notesInput.value.trim()}`;
    }

    if (!title) {
        Swal.fire({
            icon: 'warning',
            title: 'Judul Proyek Masih Kosong',
            html: 'Silakan isi <strong>Judul / Nama Proyek</strong> dan <strong>Deskripsi Detail</strong> pada Step 1 terlebih dahulu.<br><br>Cukup isi 2 hal tersebut, AI akan langsung melengkapi semua poin spesifikasi lainnya!',
            background: '#0D111A',
            color: '#F8FAFC',
            confirmButtonColor: '#6366F1',
            confirmButtonText: 'Isi Sekarang'
        }).then(() => {
            goToStep(1);
            if (nameInput) nameInput.focus();
        });
        return;
    }

    const settings = getAiSettings();
    if (!settings.apiKey) {
        Swal.fire({
            icon: 'info',
            title: 'Konfigurasi API AI Diperlukan',
            html: 'API Key belum dikonfigurasi.<br>Silakan masukkan API Key Anda pada dialog Pengaturan AI berikut untuk mengaktifkan direct generate.',
            background: '#0D111A',
            color: '#F8FAFC',
            confirmButtonColor: '#38BDF8',
            confirmButtonText: 'Buka Pengaturan AI'
        }).then(() => {
            openAiSettingsModal();
        });
        return;
    }

    const promptText = getAiPromptTemplate(title, detailedDesc);

    const endpoint = getNormalizedAiEndpoint(settings.baseUrl);
    const model = settings.model || 'gpt-5.6-luna.st';

    let secondsCount = 0;
    let timerInterval = null;

    Swal.fire({
        title: 'Sedang Merancang Spesifikasi PRD...',
        html: `
            <div style="font-size:12.5px; color:#94A3B8; margin-top:8px; line-height:1.6;">
                AI sedang menganalisis <strong>"${escapeHtml(title)}"</strong> dan menyusun seluruh arsitektur (16 langkah PRD)...
            </div>
            <div style="margin-top:10px; font-size:12px; color:#38BDF8; font-weight:600;">
                <i class="fa-solid fa-stopwatch" style="margin-right:4px;"></i> Waktu berjalan: <span id="ai-prd-timer-val" style="font-family:'JetBrains Mono',monospace;">0 detik</span>
            </div>
            <div style="margin-top:10px; display:inline-block; font-family:'JetBrains Mono', monospace; font-size:11px; background:#07090E; padding:4px 10px; border-radius:6px; color:#34D399; border:1px solid #1E293B;">
                Model: ${escapeHtml(model)} &bull; 16 Tahapan Lengkap
            </div>
            <div style="font-size:10.5px; color:#64748B; margin-top:8px;">
                Jika model AI mengalami antrean, proses ini memerlukan waktu 30–120 detik.
            </div>
        `,
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        background: '#0D111A',
        color: '#F8FAFC',
        didOpen: () => {
            Swal.showLoading();
            timerInterval = setInterval(() => {
                secondsCount++;
                const el = document.getElementById('ai-prd-timer-val');
                if (el) el.textContent = `${secondsCount} detik`;
            }, 1000);
        },
        willClose: () => {
            if (timerInterval) clearInterval(timerInterval);
        }
    });

    try {
        const resData = await callAiChatCompletions(endpoint, settings.apiKey, {
            model: model,
            messages: [
                {
                    role: 'system',
                    content: 'Anda adalah enterprise software architect terkemuka. Jawaban Anda WAJIB HANYA berupa JSON valid sesuai spesifikasi yang diminta tanpa teks pembuka/penutup.'
                },
                {
                    role: 'user',
                    content: promptText
                }
            ],
            temperature: 0.6,
            max_tokens: 4096
        });

        const rawContent = resData.choices && resData.choices[0] && resData.choices[0].message ? resData.choices[0].message.content : '';

        if (!rawContent || !rawContent.trim()) {
            throw new Error('AI memberikan respon kosong. Silakan periksa limit kuota model Anda.');
        }

        const parsedData = cleanAndParseJson(rawContent);

        // Pertahankan judul & deskripsi user jika diinput manual
        if (title && parsedData.project) {
            parsedData.project.name = title;
        }
        if (detailedDesc && parsedData.project && (!parsedData.project.description || parsedData.project.description.length < 20)) {
            parsedData.project.description = detailedDesc;
        }

        applyPrdData(parsedData, 'AI Assistant');

    } catch (err) {
        const isTimeout = err.message && (err.message.toLowerCase().includes('timed out') || err.message.toLowerCase().includes('timeout'));

        if (isTimeout) {
            Swal.fire({
                icon: 'warning',
                title: 'Waktu Tunggu Generasi Terlampaui (Timeout)',
                html: `
                    <div style="font-size:12.5px; color:#FDE68A; background:rgba(245,158,11,0.08); border:1px solid rgba(245,158,11,0.3); border-radius:8px; padding:12px; text-align:left; margin-bottom:12px; line-height:1.6;">
                        <i class="fa-solid fa-clock-rotate-left" style="color:#F59E0B; margin-right:6px;"></i>
                        Server model <strong>${escapeHtml(model)}</strong> memerlukan waktu lebih lama dari batas timeout cURL proxy untuk merancang seluruh 16 tahapan sekaligus.
                    </div>
                    <div style="font-size:12px; color:#CBD5E1; text-align:left; line-height:1.6;">
                        <strong>Solusi Tercepat &amp; Direkomendasikan:</strong><br>
                        <span style="color:#38BDF8;">&bull;</span> <strong>Gunakan Fitur "Isi Per Step"</strong>: Menghasilkan spesifikasi per langkah secara instan (5–15 detik) tanpa risiko timeout.<br>
                        <span style="color:#34D399;">&bull;</span> <strong>Ganti Provider Cepat</strong>: Pilih <em>Groq (Llama 3.3)</em> atau <em>OpenAI (gpt-4o-mini)</em> di Pengaturan AI untuk kecepatan tinggi (~500 tokens/detik).<br>
                        <span style="color:#F59E0B;">&bull;</span> <strong>Format Prompt Manual</strong>: Buka dialog "Format Prompt AI" lalu salin ke ChatGPT/Gemini secara langsung.
                    </div>
                `,
                background: '#0D111A',
                color: '#F8FAFC',
                showCancelButton: true,
                confirmButtonText: 'Buka Mode Isi Per Step',
                confirmButtonColor: '#10B981',
                cancelButtonText: 'Buka Pengaturan AI',
                cancelButtonColor: '#0284C7'
            }).then((res) => {
                if (res.isConfirmed) {
                    openAiPromptFormatModal();
                } else if (res.dismiss === Swal.DismissReason.cancel) {
                    openAiSettingsModal();
                }
            });
            return;
        }

        Swal.fire({
            icon: 'error',
            title: 'Gagal Menghasilkan PRD dari AI',
            html: `
                <div style="font-size:12px; color:#F43F5E; text-align:left; background:#080C14; padding:12px; border-radius:6px; border:1px solid #334155; word-break:break-all; margin-bottom:12px;">
                    ${escapeHtml(err.message)}
                </div>
                <div style="font-size:11.5px; color:#94A3B8;">
                    Tips: Pastikan Base URL, Model Name, dan API Key di Pengaturan AI sudah benar. Anda juga dapat menggunakan tombol Format Prompt untuk menyalin prompt secara manual.
                </div>
            `,
            background: '#0D111A',
            color: '#F8FAFC',
            confirmButtonColor: '#6366F1',
            showCancelButton: true,
            confirmButtonText: 'Buka Pengaturan AI',
            cancelButtonText: 'Tutup'
        }).then((res) => {
            if (res.isConfirmed) {
                openAiSettingsModal();
            }
        });
    }
}

async function generateStepWithDirectAi(stepScope, stepName) {
    if (currentStep === 1) saveStep1Inputs();

    const nameInput = document.getElementById('p-name');
    const descInput = document.getElementById('p-desc');
    const problemInput = document.getElementById('p-problem');

    let title = nameInput && nameInput.value.trim() ? nameInput.value.trim() : (projectPRD.project.name || '');
    let detailedDesc = descInput && descInput.value.trim() ? descInput.value.trim() : (projectPRD.project.description || '');

    if (problemInput && problemInput.value.trim()) {
        detailedDesc += `\nMasalah: ${problemInput.value.trim()}`;
    }

    if (!title) {
        const promptRes = await Swal.fire({
            title: 'Masukkan Nama / Ide Sistem',
            input: 'text',
            inputLabel: 'Tuliskan ide aplikasi Anda sebagai panduan AI:',
            inputPlaceholder: 'Contoh: Sistem Manajemen Gudang & Logistik Spareparts',
            showCancelButton: true,
            confirmButtonText: 'Lanjut Generate',
            cancelButtonText: 'Batal',
            confirmButtonColor: '#6366F1',
            cancelButtonColor: '#334155',
            background: '#0D111A',
            color: '#F8FAFC',
            inputValidator: (val) => {
                if (!val || !val.trim()) return 'Nama / ide sistem tidak boleh kosong!';
            }
        });

        if (!promptRes.value) return;

        title = promptRes.value.trim();
        projectPRD.project.name = title;
        if (nameInput) nameInput.value = title;
        updateUiMetadata();
    }

    const settings = getAiSettings();
    if (!settings.apiKey) {
        Swal.fire({
            icon: 'info',
            title: 'Konfigurasi API AI Diperlukan',
            html: 'API Key belum dikonfigurasi.<br>Silakan masukkan API Key Anda pada dialog Pengaturan AI berikut.',
            background: '#0D111A',
            color: '#F8FAFC',
            confirmButtonColor: '#38BDF8',
            confirmButtonText: 'Buka Pengaturan AI'
        }).then(() => {
            openAiSettingsModal();
        });
        return;
    }

    const promptText = getPerStepAiPromptTemplate(stepScope, title, detailedDesc);
    const endpoint = getNormalizedAiEndpoint(settings.baseUrl);
    const model = settings.model || 'gpt-5.6-luna.st';

    let stepSeconds = 0;
    let stepTimerInterval = null;

    Swal.fire({
        title: `Merancang ${escapeHtml(stepName || 'Step')}...`,
        html: `
            <div style="font-size:12.5px; color:#94A3B8; margin-top:8px; line-height:1.6;">
                AI sedang menyusun spesifikasi khusus <strong>${escapeHtml(stepName)}</strong> untuk <strong>"${escapeHtml(title)}"</strong>...
            </div>
            <div style="margin-top:10px; font-size:12px; color:#38BDF8; font-weight:600;">
                <i class="fa-solid fa-stopwatch" style="margin-right:4px;"></i> Waktu berjalan: <span id="ai-step-timer-val" style="font-family:'JetBrains Mono',monospace;">0 detik</span>
            </div>
            <div style="margin-top:10px; display:inline-block; font-family:'JetBrains Mono', monospace; font-size:11px; background:#07090E; padding:4px 10px; border-radius:6px; color:#38BDF8; border:1px solid #1E293B;">
                Model: ${escapeHtml(model)} &bull; Output Ringan Per Step (5–15 detik)
            </div>
        `,
        allowOutsideClick: false,
        allowEscapeKey: false,
        showConfirmButton: false,
        background: '#0D111A',
        color: '#F8FAFC',
        didOpen: () => {
            Swal.showLoading();
            stepTimerInterval = setInterval(() => {
                stepSeconds++;
                const el = document.getElementById('ai-step-timer-val');
                if (el) el.textContent = `${stepSeconds} detik`;
            }, 1000);
        },
        willClose: () => {
            if (stepTimerInterval) clearInterval(stepTimerInterval);
        }
    });

    try {
        const resData = await callAiChatCompletions(endpoint, settings.apiKey, {
            model: model,
            messages: [
                {
                    role: 'system',
                    content: 'Anda adalah enterprise software architect terkemuka. Jawaban Anda WAJIB HANYA berupa JSON valid sesuai spesifikasi yang diminta tanpa teks pembuka/penutup.'
                },
                {
                    role: 'user',
                    content: promptText
                }
            ],
            temperature: 0.6,
            max_tokens: 2048
        });

        const rawContent = resData.choices && resData.choices[0] && resData.choices[0].message ? resData.choices[0].message.content : '';

        if (!rawContent || !rawContent.trim()) {
            throw new Error('AI memberikan respon kosong.');
        }

        const parsedData = cleanAndParseJson(rawContent);

        // Langsung lakukan partial import via logic yang sudah ada
        const pasteBox = document.getElementById('ai-paste-json-box');
        if (pasteBox) pasteBox.value = JSON.stringify(parsedData, null, 2);

        const scopeSelect = document.getElementById('ai-step-scope-select');
        if (scopeSelect) scopeSelect.value = stepScope;

        processAiJsonImport();

    } catch (err) {
        Swal.fire({
            icon: 'error',
            title: `Gagal Mengisi ${escapeHtml(stepName || 'Step')}`,
            html: `
                <div style="font-size:12px; color:#F43F5E; text-align:left; background:#080C14; padding:12px; border-radius:6px; border:1px solid #334155; word-break:break-all; margin-bottom:12px;">
                    ${escapeHtml(err.message)}
                </div>
            `,
            background: '#0D111A',
            color: '#F8FAFC',
            confirmButtonColor: '#6366F1'
        });
    }
}


function processAiJsonImport() {
    const pasteBox = document.getElementById('ai-paste-json-box');
    const rawVal = pasteBox ? pasteBox.value : '';

    if (!rawVal || !rawVal.trim()) {
        Swal.fire({
            icon: 'warning',
            title: 'JSON Masih Kosong',
            text: 'Silakan tempel kode JSON dari ChatGPT / Gemini atau pilih file .json terlebih dahulu.',
            background: '#0D111A',
            color: '#F8FAFC'
        });
        return;
    }

    try {
        const data = cleanAndParseJson(rawVal);
        if (!data || typeof data !== 'object') {
            throw new Error('Format JSON tidak valid atau bukan objek.');
        }

        const scopeSelect = document.getElementById('ai-step-scope-select');
        const selectedScope = scopeSelect ? scopeSelect.value : 'all';

        // Deteksi apakah ini format Full PRD atau Partial Step
        const isFullPrd = data.project && (data.roles || data.modules || data.taxonomy || data.workflows);

        if (isFullPrd && selectedScope === 'all') {
            // Full PRD Import
            applyPrdData(data, 'Impor JSON AI');
            closeModal('modal-ai-json');
            return;
        }

        // ==========================================
        // PARTIAL STEP-BY-STEP MERGING LOGIC
        // ==========================================
        let updatedStepName = '';
        let targetGoToStep = null;

        // 1. Project Definition (Step 1)
        if (data.project) {
            projectPRD.project = {
                ...projectPRD.project,
                ...data.project
            };
            syncStep1Form();
            updatedStepName = '1. Project Definition';
            targetGoToStep = 1;
        }

        // 1.5 Taxonomy & 5 Pilar Arsitektur (Step 2)
        if (data.taxonomy) {
            if (data.taxonomy.pillar) {
                selectPillar(data.taxonomy.pillar);
            }
            if (data.taxonomy.archetype) {
                projectPRD.taxonomy.archetype = data.taxonomy.archetype;
            }
            updatedStepName = '2. 5 Pilar Arsitektur';
            targetGoToStep = 2;
        }

        // 2. Roles (Step 3)
        if (data.roles && Array.isArray(data.roles)) {
            const mappedRoles = data.roles.map((r, idx) => ({
                id: r.id || 'r_' + (Date.now() + idx),
                name: r.name || 'Role ' + (idx + 1),
                department: r.department || r.dept || 'Operasional',
                type: (r.type && String(r.type).toLowerCase() === 'secondary') ? 'secondary' : 'primary',
                responsibility: r.responsibility || r.resp || r.description || '',
                persona: r.persona || ''
            }));
            projectPRD.roles = mappedRoles;
            renderRoles();
            updatedStepName = '3. Roles & Stakeholder Personas';
            targetGoToStep = 3;
        }

        // 3. Modules & Features (Step 4)
        if (data.modules && Array.isArray(data.modules)) {
            projectPRD.modules = data.modules.map((m, idx) => ({
                id: m.id || 'm_' + (Date.now() + idx),
                name: m.name || 'Modul ' + (idx + 1),
                description: m.description || m.desc || '',
                submodules: m.submodules || (m.features ? m.features.map(f => f.name).join(', ') : '')
            }));

            let flattenedFeats = [];
            data.modules.forEach(m => {
                if (m.features && Array.isArray(m.features)) {
                    m.features.forEach((f, fIdx) => {
                        flattenedFeats.push({
                            id: f.id || 'f_' + m.id + '_' + (fIdx + 1),
                            moduleId: m.id,
                            name: f.name || 'Fitur ' + (fIdx + 1),
                            priority: f.priority || 'P1',
                            primaryUser: f.primaryUser || (projectPRD.roles[0] ? projectPRD.roles[0].name : ''),
                            description: f.description || f.desc || '',
                            dependencies: f.dependencies || m.name,
                            expectedOutcome: f.expectedOutcome || f.acceptance || ''
                        });
                    });
                }
            });
            if (flattenedFeats.length > 0) {
                projectPRD.features = flattenedFeats;
            } else if (data.features && Array.isArray(data.features)) {
                projectPRD.features = data.features;
            }
            renderModulesAndFeatures();
            updatedStepName = '4. Modules & Features';
            targetGoToStep = 4;
        }

        // 4. Workflows (Step 5)
        if (data.workflows && Array.isArray(data.workflows)) {
            projectPRD.workflows = data.workflows.map((w, idx) => ({
                id: w.id || 'w_' + (Date.now() + idx),
                stepNo: w.stepNo || (idx + 1),
                name: w.name || 'Tahap ' + (idx + 1),
                actor: w.actor || (projectPRD.roles[0] ? projectPRD.roles[0].name : 'User'),
                trigger: w.trigger || '',
                input: w.input || '',
                action: w.action || '',
                decision: w.decision || '',
                output: w.output || '',
                status: w.status || 'ACTIVE'
            }));
            renderWorkflowNodes();
            updatedStepName = '5. Workflow & Business Process';
            targetGoToStep = 5;
        }

        // 5. Business Rules (Step 6)
        if (data.businessRules && Array.isArray(data.businessRules)) {
            projectPRD.businessRules = data.businessRules.map((br, idx) => ({
                id: br.id || 'br_' + (Date.now() + idx),
                name: br.name || 'Aturan Bisnis ' + (idx + 1),
                severity: br.severity || br.level || 'Blocking',
                condition: br.condition || br.ruleStatement || 'Validasi Input',
                action: br.action || br.failAction || 'Tolak & Beri Notifikasi',
                exception: br.exception || 'Tidak ada pengecualian.',
                description: br.description || br.desc || br.ruleStatement || ''
            }));
            renderBusinessRules();
            updatedStepName = '6. Business Rules';
            targetGoToStep = 6;
        }

        // 6. Entities (Step 7)
        if (data.entities && Array.isArray(data.entities)) {
            projectPRD.entities = data.entities.map((e, idx) => ({
                id: e.id || 'e_' + (Date.now() + idx),
                name: e.name || 'Entitas_' + (idx + 1),
                description: e.description || e.desc || '',
                type: e.type || (idx === 0 ? 'Master' : 'Transactional'),
                storage: e.storage || e.code || ('tbl_' + (e.name || 'entity').toLowerCase()),
                fields: (e.fields || []).map((f, fIdx) => ({
                    id: f.id || 'fld_' + (fIdx + 1),
                    name: f.name || 'field_' + (fIdx + 1),
                    type: f.type || 'String',
                    required: f.required !== undefined ? String(f.required) : 'true',
                    defaultValue: f.defaultValue || '-',
                    validation: f.validation || '-',
                    description: f.description || f.desc || '-'
                })),
                relationships: e.relationships || []
            }));
            renderEntities();
            updatedStepName = '7. Data Entities (Schema)';
            targetGoToStep = 7;
        }

        // 7. Permissions / RBAC (Step 8)
        if (data.permissions && typeof data.permissions === 'object') {
            projectPRD.permissions = {
                ...projectPRD.permissions,
                ...data.permissions
            };
            renderRbacMatrix();
            updatedStepName = '8. Matriks Hak Akses (RBAC)';
            targetGoToStep = 8;
        }

        // 8. KPIs (Step 9)
        if (data.kpis && Array.isArray(data.kpis)) {
            projectPRD.kpis = data.kpis.map((k, idx) => ({
                id: k.id || 'kpi_' + (Date.now() + idx),
                name: k.name || 'KPI ' + (idx + 1),
                target: k.target || '>= 95%',
                unit: k.unit || '%',
                formula: k.formula || 'Kalkulasi Otomatis',
                source: k.source || (projectPRD.entities[0] ? projectPRD.entities[0].name : 'Sistem'),
                frequency: k.frequency || 'Harian',
                visualization: k.visualization || 'Stat Card',
                description: k.description || k.desc || ''
            }));
            renderKpis();
            updatedStepName = '9. Key Performance Indicators (KPI)';
            targetGoToStep = 9;
        }

        // 9. Notifications (Step 10)
        if (data.notifications && Array.isArray(data.notifications)) {
            projectPRD.notifications = data.notifications.map((n, idx) => ({
                id: n.id || 'n_' + (Date.now() + idx),
                name: n.name || n.event || 'Notifikasi ' + (idx + 1),
                recipient: n.recipient || (projectPRD.roles[0] ? projectPRD.roles[0].name : 'Semua Role'),
                channel: n.channel || 'In-App Toast',
                priority: n.priority || 'P2 High',
                escalation: n.escalation || 'Teruskan ke atasan',
                template: n.template || n.messageTemplate || ('[INFO] Notifikasi ' + (n.name || 'sistem'))
            }));
            renderNotifications();
            updatedStepName = '10. Notifikasi & Alert Operasional';
            targetGoToStep = 10;
        }

        // 10. Integrations (Step 11)
        if (data.integrations && Array.isArray(data.integrations)) {
            projectPRD.integrations = data.integrations.map((i, idx) => ({
                id: i.id || 'i_' + (Date.now() + idx),
                system: i.system || i.systemName || 'Sistem Eksternal',
                direction: i.direction || 'Inbound',
                frequency: i.frequency || 'Real-time Webhook',
                purpose: i.purpose || 'Pertukaran data operasional',
                data: i.data || i.dataPayload || 'JSON Payload',
                auth: i.auth || i.protocolAuth || 'REST API Bearer Token',
                mockNotes: i.mockNotes || i.offlineSimulation || 'Disimulasikan dengan mock array di browser'
            }));
            renderIntegrations();
            updatedStepName = '11. Integrasi Sistem';
            targetGoToStep = 11;
        }

        // 11. UIUX Screens Architecture (Step 12)
        if (data.uiux && data.uiux.screens && Array.isArray(data.uiux.screens)) {
            projectPRD.uiux.screens = data.uiux.screens.map((s, idx) => ({
                id: s.id || 's_' + (Date.now() + idx),
                name: s.name || 'Screen ' + (idx + 1),
                features: s.features || (projectPRD.features[idx] ? projectPRD.features[idx].name : 'Ringkasan & Aksi'),
                components: s.components || 'Stat Cards, Data Table, Filter Bar'
            }));
            renderScreens();
            updatedStepName = '12. UI/UX Screens Architecture';
            targetGoToStep = 12;
        }

        // 12. Technical MVP Specification (Step 13)
        if (data.techMvp) {
            if (data.techMvp.notes) {
                projectPRD.project.additionalNotes = (projectPRD.project.additionalNotes ? projectPRD.project.additionalNotes + '\n' : '') + data.techMvp.notes;
                syncStep1Form();
            }
            updatedStepName = '13. Technical MVP Specification';
            targetGoToStep = 13;
        }

        if (!updatedStepName) {
            // Fallback to general applyPrdData if no recognized step matched
            applyPrdData(data, 'Impor JSON AI');
            closeModal('modal-ai-json');
            return;
        }

        // Persist & Save automatic draft
        saveProject(false);
        saveQuickDraft();
        updateUiMetadata();
        checkCompleteness();

        closeModal('modal-ai-json');
        if (targetGoToStep) goToStep(targetGoToStep);

        Swal.fire({
            icon: 'success',
            title: 'Bagian Berhasil Diperbarui!',
            html: `Berhasil mengisi <strong>${escapeHtml(updatedStepName)}</strong> secara instan.<br><span style="font-size:12px; color:#94A3B8;">Bagian lain dari proyek tetap aman terjaga.</span>`,
            background: '#0D111A',
            color: '#F8FAFC',
            confirmButtonColor: '#10B981'
        });

    } catch (err) {
        Swal.fire({
            icon: 'error',
            title: 'Gagal Memproses JSON AI',
            text: 'Terjadi kesalahan saat membaca JSON: ' + err.message,
            background: '#0D111A',
            color: '#F8FAFC',
            confirmButtonColor: '#F43F5E'
        });
    }
}

// Helper for executing AI generation on currently active step
function generateCurrentStepByAi() {
    const stepScopeMap = {
        1: { scope: 'step1', name: 'Step 1: Project Definition & Scope' },
        2: { scope: 'step2', name: 'Step 2: 5 Pilar Arsitektur' },
        3: { scope: 'step3', name: 'Step 3: Users & Roles' },
        4: { scope: 'step4', name: 'Step 4: Modules & Features' },
        5: { scope: 'step5', name: 'Step 5: Workflows' },
        6: { scope: 'step6', name: 'Step 6: Business Rules' },
        7: { scope: 'step7', name: 'Step 7: Data Entities' },
        8: { scope: 'step8', name: 'Step 8: RBAC Permissions' },
        9: { scope: 'step9', name: 'Step 9: KPIs & Reporting' },
        10: { scope: 'step10', name: 'Step 10: Notifications' },
        11: { scope: 'step11', name: 'Step 11: System Integrations' },
        12: { scope: 'step12', name: 'Step 12: UI Screens Architecture' },
        13: { scope: 'step13', name: 'Step 13: Technical MVP Spec' },
        14: { scope: 'step14', name: 'Step 14: PRD Completeness Audit' },
        15: { scope: 'step15', name: 'Step 15: Quality PRD' },
        16: { scope: 'step16', name: 'Step 16: MVP Implementation Prompt' }
    };

    if (currentStep === 14) {
        runAiPrdReviewAudit();
    } else if (currentStep === 15) {
        renderPrdDocument();
        Swal.fire({
            icon: 'success',
            title: 'Dokumen PRD Diperbarui!',
            text: 'Dokumen PRD 24-seksi berhasil disusun dari data seluruh langkah.',
            background: '#0D111A',
            color: '#F8FAFC',
            timer: 2000,
            showConfirmButton: false
        });
    } else if (currentStep === 16) {
        enhanceMvpPromptWithAi();
    } else {
        const info = stepScopeMap[currentStep] || { scope: 'step' + currentStep, name: 'Step ' + currentStep };
        generateStepWithDirectAi(info.scope, info.name);
    }
}

async function runAiPrdReviewAudit() {
    const settings = getAiSettings();
    if (!settings.apiKey) {
        Swal.fire({
            icon: 'info',
            title: 'Konfigurasi API AI Diperlukan',
            text: 'Masukkan API Key Anda di Pengaturan AI terlebih dahulu.',
            background: '#0D111A',
            color: '#F8FAFC',
            confirmButtonColor: '#38BDF8',
            confirmButtonText: 'Buka Pengaturan AI'
        }).then(() => openAiSettingsModal());
        return;
    }

    const title = projectPRD.project.name || 'Sistem Tanpa Judul';
    const endpoint = getNormalizedAiEndpoint(settings.baseUrl);
    const model = settings.model || 'gpt-5.6-luna.st';

    Swal.fire({
        title: 'Mengaudit PRD via AI...',
        html: `
            <div style="font-size:12px; color:#94A3B8; margin-top:8px;">
                AI sedang mengevaluasi koherensi arsitektur, kelengkapan entitas, dan aturan bisnis...
            </div>
            <div style="margin-top:10px; font-family:'JetBrains Mono',monospace; font-size:11px; color:#38BDF8;">
                Model: ${escapeHtml(model)} &bull; Audit Cepat (5-10 detik)
            </div>
        `,
        allowOutsideClick: false,
        didOpen: () => Swal.showLoading(),
        background: '#0D111A',
        color: '#F8FAFC'
    });

    try {
        const auditPrompt = `Anda adalah Lead Software Auditor dan Requirements Reviewer.
Audit spesifikasi PRD berikut:
- Produk: "${title}"
- Deskripsi: "${projectPRD.project.description || '-'}"
- Jumlah Role: ${projectPRD.roles.length}
- Jumlah Modul: ${projectPRD.modules.length}
- Jumlah Fitur: ${projectPRD.features.length}
- Jumlah Workflow: ${projectPRD.workflows.length}
- Jumlah Aturan Bisnis: ${projectPRD.businessRules.length}
- Jumlah Entitas Data: ${projectPRD.entities.length}
- Jumlah KPI: ${projectPRD.kpis.length}

Berikan review singkat dalam format JSON:
\`\`\`json
{
  "score": 92,
  "strengths": ["Poin kelebihan 1", "Poin kelebihan 2"],
  "recommendations": ["Rekomendasi perbaikan 1", "Rekomendasi perbaikan 2"],
  "verdict": "PRD Ready for MVP Coding / Need minor refinement"
}
\`\`\``;

        const resData = await callAiChatCompletions(endpoint, settings.apiKey, {
            model: model,
            messages: [
                { role: 'system', content: 'Jawaban WAJIB HANYA berupa JSON valid tanpa teks di luar blok json.' },
                { role: 'user', content: auditPrompt }
            ],
            temperature: 0.5,
            max_tokens: 1024
        });

        const raw = resData.choices && resData.choices[0] && resData.choices[0].message ? resData.choices[0].message.content : '';
        const parsed = cleanAndParseJson(raw);

        const warningsBox = document.getElementById('checker-warnings-box');
        if (warningsBox && parsed) {
            warningsBox.innerHTML = `
                <div style="background:rgba(99,102,241,0.08); border:1px solid rgba(99,102,241,0.3); border-radius:12px; padding:16px; margin-bottom:16px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <div style="font-weight:800; color:#A5B4FC; font-size:14px;">
                            <i class="fa-solid fa-clipboard-check" style="margin-right:6px;"></i> Hasil Audit Kualitas AI (Skor: ${parsed.score || 90}/100)
                        </div>
                        <span class="badge badge-emerald">${escapeHtml(parsed.verdict || 'Ready for MVP')}</span>
                    </div>
                    <div style="font-size:12px; color:#E2E8FF; margin-bottom:8px;">
                        <strong>Kelebihan:</strong> ${(parsed.strengths || []).join(' &bull; ')}
                    </div>
                    <div style="font-size:12px; color:#FDE68A;">
                        <strong>Rekomendasi AI:</strong> ${(parsed.recommendations || []).join(' &bull; ')}
                    </div>
                </div>
            ` + warningsBox.innerHTML;
        }

        Swal.fire({
            icon: 'success',
            title: `Audit Selesai (Skor: ${parsed.score || 90}/100)`,
            html: `
                <div style="font-size:12.5px; text-align:left; color:#CBD5E1; line-height:1.6;">
                    <strong style="color:#6EE7B7;">Status:</strong> ${escapeHtml(parsed.verdict || 'PRD Siap Diimplementasikan')}<br><br>
                    <strong style="color:#A5B4FC;">Rekomendasi AI:</strong>
                    <ul style="margin:6px 0 0 16px; padding:0;">
                        ${(parsed.recommendations || []).map(r => `<li>${escapeHtml(r)}</li>`).join('')}
                    </ul>
                </div>
            `,
            background: '#0D111A',
            color: '#F8FAFC',
            confirmButtonColor: '#6366F1'
        });

    } catch (err) {
        Swal.fire({
            icon: 'error',
            title: 'Audit AI Gagal',
            text: err.message,
            background: '#0D111A',
            color: '#F8FAFC'
        });
    }
}

async function enhanceMvpPromptWithAi() {
    const settings = getAiSettings();
    if (!settings.apiKey) {
        Swal.fire({
            icon: 'info',
            title: 'Konfigurasi API AI Diperlukan',
            text: 'Masukkan API Key Anda di Pengaturan AI terlebih dahulu.',
            background: '#0D111A',
            color: '#F8FAFC',
            confirmButtonColor: '#38BDF8',
            confirmButtonText: 'Buka Pengaturan AI'
        }).then(() => openAiSettingsModal());
        return;
    }

    const title = projectPRD.project.name || 'Aplikasi';
    const endpoint = getNormalizedAiEndpoint(settings.baseUrl);
    const model = settings.model || 'gpt-5.6-luna.st';

    Swal.fire({
        title: 'Mengoptimasi Prompt MVP via AI...',
        html: `
            <div style="font-size:12px; color:#94A3B8; margin-top:8px;">
                AI sedang menyempurnakan aturan coding, state mocking, dan guardrail implementasi...
            </div>
            <div style="margin-top:10px; font-family:'JetBrains Mono',monospace; font-size:11px; color:#38BDF8;">
                Model: ${escapeHtml(model)} &bull; Cepat (5-10 detik)
            </div>
        `,
        allowOutsideClick: false,
        didOpen: () => Swal.showLoading(),
        background: '#0D111A',
        color: '#F8FAFC'
    });

    try {
        const promptOptimizeQuery = `Anda adalah Principal AI Prompt Engineer.
Berdasarkan sistem "${title}" dengan ${projectPRD.roles.length} roles, ${projectPRD.modules.length} modul, dan ${projectPRD.entities.length} data entitas,
Tuliskan 3 instruksi pembatas teknis tingkat tinggi (technical constraints & anti-slop rules) dalam format JSON:
\`\`\`json
{
  "constraints": [
    "Wajib menggunakan interaktivitas DOM murni tanpa reload halaman",
    "Gunakan schema validasi strict di setiap input modal sebelum commit ke localStorage",
    "Sediakan mock user switcher untuk verifikasi role RBAC secara visual"
  ]
}
\`\`\``;

        const resData = await callAiChatCompletions(endpoint, settings.apiKey, {
            model: model,
            messages: [
                { role: 'system', content: 'Jawaban WAJIB HANYA berupa JSON valid tanpa teks lain.' },
                { role: 'user', content: promptOptimizeQuery }
            ],
            temperature: 0.5,
            max_tokens: 1024
        });

        const raw = resData.choices && resData.choices[0] && resData.choices[0].message ? resData.choices[0].message.content : '';
        const parsed = cleanAndParseJson(raw);

        if (parsed && parsed.constraints && Array.isArray(parsed.constraints)) {
            const extraRules = '\n\n/* AI ENHANCED TECHNICAL CONSTRAINTS */\n' + parsed.constraints.map((c, i) => `// ${i+1}. ${c}`).join('\n');
            const promptBox = document.getElementById('mvp-prompt-raw-textarea');
            if (promptBox) {
                promptBox.value += extraRules;
            }
        }

        Swal.fire({
            icon: 'success',
            title: 'Prompt MVP Dioptimasi!',
            text: 'AI telah menambahkan guardrails teknis dan edge-case constraints ke dalam Prompt MVP.',
            background: '#0D111A',
            color: '#F8FAFC',
            confirmButtonColor: '#6366F1'
        });

    } catch (err) {
        Swal.fire({
            icon: 'error',
            title: 'Gagal Mengoptimasi Prompt',
            text: err.message,
            background: '#0D111A',
            color: '#F8FAFC'
        });
    }
}

// Modal generic open/close
function openModal(modalId) {
    const el = document.getElementById(modalId);
    if (el) el.classList.add('active');
}

function closeModal(modalId) {
    const el = document.getElementById(modalId);
    if (el) el.classList.remove('active');
}

function togglePresetDropdown() {
    const menu = document.getElementById('preset-dropdown-menu');
    if (menu) {
        menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
    }
}

// Close preset dropdown on outside click
window.addEventListener('click', function(e) {
    const menu = document.getElementById('preset-dropdown-menu');
    const btn = document.getElementById('btn-preset-menu');
    if (menu && btn && !btn.contains(e.target) && !menu.contains(e.target)) {
        menu.style.display = 'none';
    }
});

// Auto-run on load
window.addEventListener('DOMContentLoaded', () => {
    initEnterprisePrdStudio();
});



"""
