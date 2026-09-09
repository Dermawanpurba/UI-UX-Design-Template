# Enterprise PRD Studio & Single-File MVP Prompt Engine

Platform perancangan kebutuhan perangkat lunak perusahaan (Product Requirements Document), taksonomi offline, dan generator prompt implementasi MVP berbasis Web.

## 🚀 Fitur Utama

- **16-Step Comprehensive Requirements Architecture**: Dari pendefinisian ruang lingkup, stakeholder persona, modul, data model ERD, matriks RBAC, hingga metrik KPI.
- **Direct AI Integration & Intelligent Proxy**: 
  - Terintegrasi dengan endpoint AI ChatGPT-compatible (SiapTuan, Groq, OpenAI).
  - Mendukung backend Serverless gratis di Vercel (`/api/proxy`).
  - Auto-fallback & proxy health check otomatis.
- **Standalone & Single-File Ready**: Frontend dibangun menggunakan Vanilla HTML/CSS/JS tanpa overhead framework frontend, cepat, dan responsif.
- **Auto Drafts & Local Persistence**: Fitur simpan draft lokal, ekspor/impor skema JSON PRD lengkap.

## 🛠️ Struktur Proyek

```text
├── index.html            # Web application frontend utama
├── api/
│   └── proxy.js          # Vercel Serverless Function (Node.js) untuk bypass CORS AI
├── vercel.json           # Konfigurasi routing rewrite Vercel
├── package.json          # Metadata project Vercel
├── ai_proxy.php          # Alternatif proxy untuk Apache XAMPP / PHP
├── PROMPT_AI_GENERATOR.md# Panduan prompt master AI
├── template_project_ai.json # Contoh format skema JSON PRD
├── build_studio.py       # Compiler modular untuk index.html
├── gen_assets.py         # Database 60 tema & SVG generator
├── gen_css.py            # CSS Design System
├── gen_html.py           # Shell HTML & 16-step workspace
└── gen_js_engines.py     # Reactive JS engines & AI caller
```

## 🌐 Deployment Vercel

Aplikasi ini siap di-deploy langsung ke [Vercel](https://vercel.com):
1. Sambungkan repository ini ke proyek Vercel Anda.
2. Vercel akan otomatis menyajikan `index.html` dan mengeksekusi `/api/proxy` secara serverless tanpa konfigurasi tambahan.

---
Dikembangkan dengan standar arsitektur enterprise modern.
