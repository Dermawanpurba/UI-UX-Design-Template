# -*- coding: utf-8 -*-
"""HTML layout generator."""

def get_html():
    return r"""
<div class="app-shell">
    <!-- TOP NAVIGATION HEADER -->
    <header class="top-header">
        <div class="brand-box">
            <div class="brand-logo">
                <i class="fa-solid fa-cube"></i>
            </div>
            <div>
                <div style="display:flex; align-items:center; gap:8px;">
                    <span class="font-outfit" style="font-size:16px; font-weight:900; color:#FFFFFF; letter-spacing:0.5px;">ENTERPRISE PRD STUDIO</span>
                    <span class="badge badge-indigo">5 Pilar Arsitektur</span>
                </div>
                <div style="font-size:11px; color:var(--text-muted);">
                    Requirements Engineering Engine &bull; Quality PRD &bull; Single-File HTML MVP
                </div>
            </div>
        </div>

        <!-- Middle: Project Name & Completeness Meter -->
        <div style="display:flex; align-items:center; gap:20px;">
            <div style="display:flex; flex-direction:column; align-items:flex-end;">
                <div style="display:flex; align-items:center; gap:8px;">
                    <span style="font-size:11px; color:var(--text-muted); text-transform:uppercase; font-weight:700;">Proyek Aktif:</span>
                    <span id="top-project-name" class="font-outfit" style="font-size:13px; font-weight:800; color:#F8FAFC; max-width:260px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">Proyek Baru (Kosong)</span>
                </div>
                <div style="display:flex; align-items:center; gap:8px; margin-top:2px;">
                    <span style="font-size:10.5px; color:#94A3B8;">Kelengkapan PRD:</span>
                    <div style="width:100px; height:6px; background:#1E293B; border-radius:10px; overflow:hidden;">
                        <div id="top-completeness-bar" style="width:0%; height:100%; background:linear-gradient(90deg, #6366F1, #10B981); border-radius:10px; transition:width 0.3s ease;"></div>
                    </div>
                    <span id="top-completeness-score" style="font-size:11px; font-weight:800; color:#94A3B8;">0%</span>
                </div>
            </div>
        </div>

        <!-- Right: Draft Manager & Action Buttons -->
        <div style="display:flex; align-items:center; gap:8px;">
            <!-- TEMPAT SAVE SEMENTARA (DRAFT STORAGE) -->
            <button type="button" class="btn btn-emerald btn-sm" onclick="saveQuickDraft()" title="Simpan draft aktif secara instan ke browser">
                <i class="fa-solid fa-floppy-disk"></i>
                <span>Simpan Draft</span>
            </button>
            <button type="button" class="btn btn-secondary btn-sm" onclick="openDraftManagerModal()" title="Kelola slot simpanan sementara (Drafts)">
                <i class="fa-solid fa-box-archive" style="color:#818CF8;"></i>
                <span>Tempat Simpan Sementara</span>
                <span class="badge badge-indigo" id="top-drafts-count" style="margin-left:2px;">0</span>
            </button>

            <!-- PENGATURAN AI (CHATGPT COMPATIBLE) -->
            <button type="button" class="btn btn-secondary btn-sm" onclick="openAiSettingsModal()" title="Konfigurasi API AI (Base URL, Model, API Key) untuk generate otomatis langsung tanpa copy-paste manual">
                <i class="fa-solid fa-gear" style="color:#38BDF8;"></i>
                <span>Pengaturan AI</span>
            </button>

            <!-- FORMAT PROMPT AI & IMPOR JSON (FAST TRACK) -->
            <button type="button" class="btn btn-primary btn-sm" onclick="generatePrdWithDirectAi()" title="Ketik judul & deskripsi produk, lalu klik untuk mengisi seluruh 16 langkah PRD otomatis langsung via AI!" style="background:linear-gradient(135deg, #6366F1 0%, #8B5CF6 100%); border-color:#7C3AED; box-shadow:0 0 14px rgba(99,102,241,0.35); font-weight:700;">
                <i class="fa-solid fa-wand-magic-sparkles" style="color:#FDE047;"></i>
                <span id="top-btn-ai-text">Isi Semua Otomatis by AI</span>
            </button>

            <!-- Template Preset Dropdown (Opsional) -->
            <div class="dropdown" style="position:relative;">
                <button type="button" class="btn btn-secondary btn-sm" onclick="togglePresetDropdown()" id="btn-preset-menu">
                    <i class="fa-solid fa-wand-magic-sparkles" style="color:#F59E0B;"></i>
                    <span>Preset</span>
                    <i class="fa-solid fa-chevron-down" style="font-size:9px; margin-left:2px;"></i>
                </button>
                <div id="preset-dropdown-menu" style="display:none; position:absolute; right:0; top:110%; width:260px; background:#0D111A; border:1px solid #1E293B; border-radius:10px; box-shadow:0 10px 25px rgba(0,0,0,0.5); z-index:50; padding:6px;">
                    <button type="button" onclick="loadMiningCmmsPreset(); togglePresetDropdown();" style="width:100%; text-align:left; padding:8px 12px; border-radius:6px; background:transparent; border:none; color:#E2E8FF; font-size:12px; cursor:pointer; display:flex; align-items:center; gap:8px;" onmouseover="this.style.background='rgba(99,102,241,0.15)'" onmouseout="this.style.background='transparent'">
                        <i class="fa-solid fa-screwdriver-wrench" style="color:#818CF8; width:16px;"></i>
                        <div>
                            <div style="font-weight:700;">Mining CMMS &amp; Fleet</div>
                            <div style="font-size:10px; color:#94A3B8;">Work Order, PM, Spares, MTTR/MTBF</div>
                        </div>
                    </button>
                    <button type="button" onclick="loadB2BTradingPreset(); togglePresetDropdown();" style="width:100%; text-align:left; padding:8px 12px; border-radius:6px; background:transparent; border:none; color:#E2E8FF; font-size:12px; cursor:pointer; display:flex; align-items:center; gap:8px; margin-top:4px;" onmouseover="this.style.background='rgba(16,185,129,0.15)'" onmouseout="this.style.background='transparent'">
                        <i class="fa-solid fa-cart-shopping" style="color:#34D399; width:16px;"></i>
                        <div>
                            <div style="font-weight:700;">B2B Coal &amp; Ore Trading</div>
                            <div style="font-size:10px; color:#94A3B8;">Auction, GCV Blending, Surveyor CoA</div>
                        </div>
                    </button>
                </div>
            </div>

            <!-- JSON Export & Import -->
            <button type="button" class="btn btn-secondary btn-sm" onclick="exportProjectJson()" title="Ekspor PRD sebagai file JSON">
                <i class="fa-solid fa-file-export"></i>
                <span>JSON</span>
            </button>
            <label class="btn btn-secondary btn-sm" style="margin-bottom:0; cursor:pointer;" title="Buka file PRD JSON sebelumnya">
                <i class="fa-solid fa-file-import"></i>
                <span>Impor</span>
                <input type="file" id="input-import-json" accept=".json" style="display:none;" onchange="importProjectJson(event)">
            </label>
            <button type="button" class="btn btn-rose btn-sm" onclick="resetProjectConfirm()" title="Kosongkan seluruh isian proyek">
                <i class="fa-solid fa-rotate-left"></i>
            </button>
        </div>
    </header>

    <!-- WORKSPACE SHELL -->
    <div class="workspace-shell">
        <!-- SIDEBAR STEPPER (16 STEPS) -->
        <aside class="sidebar-stepper" id="sidebar-stepper">
            <div class="step-nav-header">
                <span style="font-size:11.5px; font-weight:800; color:#A5B4FC; text-transform:uppercase; letter-spacing:0.5px;">16-Step Blueprint Wizard</span>
                <span class="badge badge-slate" id="sidebar-step-count">Step 1 / 16</span>
            </div>

            <div style="padding:8px 0; overflow-y:auto; flex:1;">
                <!-- Step 1 -->
                <div class="step-nav-item active" id="nav-step-1" onclick="goToStep(1)">
                    <div class="step-num-badge" id="badge-step-1">1</div>
                    <div style="flex:1; min-width:0;">
                        <div style="font-size:12.5px; font-weight:700; color:#FFFFFF;">1. Project Definition</div>
                        <div style="font-size:10.5px; color:var(--text-muted);">Nama, objektif, ruang lingkup</div>
                    </div>
                </div>

                <!-- Step 2 -->
                <div class="step-nav-item" id="nav-step-2" onclick="goToStep(2)">
                    <div class="step-num-badge" id="badge-step-2">2</div>
                    <div style="flex:1; min-width:0;">
                        <div style="font-size:12.5px; font-weight:700; color:#FFFFFF;">2. 5 Pilar Arsitektur</div>
                        <div style="font-size:10.5px; color:var(--text-muted);" id="sub-step-2">Pilih 1 Pilar Inti</div>
                    </div>
                </div>

                <!-- Step 3 -->
                <div class="step-nav-item" id="nav-step-3" onclick="goToStep(3)">
                    <div class="step-num-badge" id="badge-step-3">3</div>
                    <div style="flex:1; min-width:0;">
                        <div style="font-size:12.5px; font-weight:700; color:#FFFFFF;">3. Users &amp; Roles</div>
                        <div style="font-size:10.5px; color:var(--text-muted);" id="sub-step-3">0 Role terdaftar</div>
                    </div>
                </div>

                <!-- Step 4 -->
                <div class="step-nav-item" id="nav-step-4" onclick="goToStep(4)">
                    <div class="step-num-badge" id="badge-step-4">4</div>
                    <div style="flex:1; min-width:0;">
                        <div style="font-size:12.5px; font-weight:700; color:#FFFFFF;">4. Modules &amp; Features</div>
                        <div style="font-size:10.5px; color:var(--text-muted);" id="sub-step-4">0 Modul / 0 Fitur</div>
                    </div>
                </div>

                <!-- Step 5 -->
                <div class="step-nav-item" id="nav-step-5" onclick="goToStep(5)">
                    <div class="step-num-badge" id="badge-step-5">5</div>
                    <div style="flex:1; min-width:0;">
                        <div style="font-size:12.5px; font-weight:700; color:#FFFFFF;">5. Business Process &amp; Workflow</div>
                        <div style="font-size:10.5px; color:var(--text-muted);" id="sub-step-5">0 Tahapan alur kerja</div>
                    </div>
                </div>

                <!-- Step 6 -->
                <div class="step-nav-item" id="nav-step-6" onclick="goToStep(6)">
                    <div class="step-num-badge" id="badge-step-6">6</div>
                    <div style="flex:1; min-width:0;">
                        <div style="font-size:12.5px; font-weight:700; color:#FFFFFF;">6. Business Rules</div>
                        <div style="font-size:10.5px; color:var(--text-muted);" id="sub-step-6">0 Aturan validasi</div>
                    </div>
                </div>

                <!-- Step 7 -->
                <div class="step-nav-item" id="nav-step-7" onclick="goToStep(7)">
                    <div class="step-num-badge" id="badge-step-7">7</div>
                    <div style="flex:1; min-width:0;">
                        <div style="font-size:12.5px; font-weight:700; color:#FFFFFF;">7. Data Model (Entity Builder)</div>
                        <div style="font-size:10.5px; color:var(--text-muted);" id="sub-step-7">0 Entitas data</div>
                    </div>
                </div>

                <!-- Step 8 -->
                <div class="step-nav-item" id="nav-step-8" onclick="goToStep(8)">
                    <div class="step-num-badge" id="badge-step-8">8</div>
                    <div style="flex:1; min-width:0;">
                        <div style="font-size:12.5px; font-weight:700; color:#FFFFFF;">8. Permissions / RBAC</div>
                        <div style="font-size:10.5px; color:var(--text-muted);" id="sub-step-8">Matriks hak akses</div>
                    </div>
                </div>

                <!-- Step 9 -->
                <div class="step-nav-item" id="nav-step-9" onclick="goToStep(9)">
                    <div class="step-num-badge" id="badge-step-9">9</div>
                    <div style="flex:1; min-width:0;">
                        <div style="font-size:12.5px; font-weight:700; color:#FFFFFF;">9. KPI &amp; Reporting</div>
                        <div style="font-size:10.5px; color:var(--text-muted);" id="sub-step-9">0 Metrik KPI</div>
                    </div>
                </div>

                <!-- Step 10 -->
                <div class="step-nav-item" id="nav-step-10" onclick="goToStep(10)">
                    <div class="step-num-badge" id="badge-step-10">10</div>
                    <div style="flex:1; min-width:0;">
                        <div style="font-size:12.5px; font-weight:700; color:#FFFFFF;">10. Notification</div>
                        <div style="font-size:10.5px; color:var(--text-muted);" id="sub-step-10">0 Notifikasi &amp; Alert</div>
                    </div>
                </div>

                <!-- Step 11 -->
                <div class="step-nav-item" id="nav-step-11" onclick="goToStep(11)">
                    <div class="step-num-badge" id="badge-step-11">11</div>
                    <div style="flex:1; min-width:0;">
                        <div style="font-size:12.5px; font-weight:700; color:#FFFFFF;">11. Integration Requirements</div>
                        <div style="font-size:10.5px; color:var(--text-muted);" id="sub-step-11">0 Sistem integrasi</div>
                    </div>
                </div>

                <!-- Step 12 -->
                <div class="step-nav-item" id="nav-step-12" onclick="goToStep(12)">
                    <div class="step-num-badge" id="badge-step-12">12</div>
                    <div style="flex:1; min-width:0;">
                        <div style="font-size:12.5px; font-weight:700; color:#FFFFFF;">12. UI/UX Architecture</div>
                        <div style="font-size:10.5px; color:var(--text-muted);" id="sub-step-12">60 Styles &bull; Screen map</div>
                    </div>
                </div>

                <!-- Step 13 -->
                <div class="step-nav-item" id="nav-step-13" onclick="goToStep(13)">
                    <div class="step-num-badge" id="badge-step-13">13</div>
                    <div style="flex:1; min-width:0;">
                        <div style="font-size:12.5px; font-weight:700; color:#FFFFFF;">13. Technical MVP Spec</div>
                        <div style="font-size:10.5px; color:var(--text-muted);">Single-file index.html</div>
                    </div>
                </div>

                <!-- Step 14 -->
                <div class="step-nav-item" id="nav-step-14" onclick="goToStep(14)">
                    <div class="step-num-badge" id="badge-step-14">14</div>
                    <div style="flex:1; min-width:0;">
                        <div style="font-size:12.5px; font-weight:700; color:#FFFFFF;">14. PRD Review &amp; Checker</div>
                        <div style="font-size:10.5px; color:var(--text-muted);">Uji kelengkapan dokumen</div>
                    </div>
                </div>

                <!-- Step 15 -->
                <div class="step-nav-item" id="nav-step-15" onclick="goToStep(15)">
                    <div class="step-num-badge" id="badge-step-15" style="background:#10B981; color:#FFFFFF; border-color:#10B981;"><i class="fa-solid fa-file-lines"></i></div>
                    <div style="flex:1; min-width:0;">
                        <div style="font-size:12.5px; font-weight:800; color:#34D399;">15. Generate Quality PRD</div>
                        <div style="font-size:10.5px; color:#A7F3D0;">Dokumen PRD 24 Seksi</div>
                    </div>
                </div>

                <!-- Step 16 -->
                <div class="step-nav-item" id="nav-step-16" onclick="goToStep(16)">
                    <div class="step-num-badge" id="badge-step-16" style="background:#6366F1; color:#FFFFFF; border-color:#6366F1;"><i class="fa-solid fa-robot"></i></div>
                    <div style="flex:1; min-width:0;">
                        <div style="font-size:12.5px; font-weight:800; color:#C7D2FE;">16. Generate MVP Prompt</div>
                        <div style="font-size:10.5px; color:#A5B4FC;">Single index.html prompt</div>
                    </div>
                </div>
            </div>
        </aside>

        <!-- MAIN VIEWPORT CONTAINER -->
        <main class="main-viewport">
            <!-- STEP 1: PROJECT DEFINITION -->
            <div class="step-panel active" id="panel-step-1">
                <div class="card-box highlight">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
                        <div>
                            <span class="badge badge-indigo">Langkah 1 Dari 16</span>
                            <h2 class="font-outfit" style="font-size:20px; font-weight:800; color:#FFFFFF; margin:6px 0 2px;">Project Definition &amp; Scope</h2>
                            <p style="font-size:12px; color:var(--text-secondary);">Mulai dari lembar kerja bersih. Definisikan nama produk, masalah bisnis, target objektif, batasan ruang lingkup, dan kriteria sukses.</p>
                        </div>
                        <span class="badge badge-emerald" id="auto-draft-chip"><i class="fa-solid fa-clock-rotate-left" style="margin-right:4px;"></i>Draft Siap Simpan</span>
                    </div>

                    <!-- Fast-Track Callout Banner -->
                    <div style="background:linear-gradient(135deg, rgba(99,102,241,0.16) 0%, rgba(139,92,246,0.16) 100%); border:1px solid rgba(99,102,241,0.45); border-radius:12px; padding:14px 18px; margin-bottom:18px; display:flex; align-items:center; justify-content:space-between; gap:16px; box-shadow:0 4px 20px rgba(99,102,241,0.15);">
                        <div style="display:flex; align-items:center; gap:14px;">
                            <div style="width:42px; height:42px; border-radius:10px; background:linear-gradient(135deg, #6366F1, #8B5CF6); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-size:19px; flex-shrink:0; box-shadow:0 0 18px rgba(99,102,241,0.45);">
                                <i class="fa-solid fa-wand-magic-sparkles"></i>
                            </div>
                            <div>
                                <div style="font-size:14px; font-weight:800; color:#FFFFFF; display:flex; align-items:center; gap:8px;">
                                    <span>Isi Semua Otomatis by AI (Direct API &bull; Tanpa Ribet JSON)</span>
                                    <span class="badge badge-emerald">ChatGPT Compatible</span>
                                </div>
                                <div style="font-size:11.5px; color:#C7D2FE; margin-top:2px;">Cukup isi <strong>Nama Produk &amp; Deskripsi Detail</strong> di bawah, lalu klik <strong>"Isi Semua by AI"</strong>. Sistem akan langsung memanggil AI dan mengisi 16 langkah PRD secara instan!</div>
                            </div>
                        </div>
                        <div style="display:flex; align-items:center; gap:8px; flex-shrink:0;">
                            <button type="button" class="btn btn-secondary btn-sm" onclick="openAiSettingsModal()" title="Konfigurasi API AI (Base URL, Model, API Key)">
                                <i class="fa-solid fa-gear" style="color:#38BDF8;"></i>
                                <span>Pengaturan AI</span>
                            </button>
                            <button type="button" class="btn btn-secondary btn-sm" onclick="openAiPromptFormatModal()" title="Buka mode generator per-step ringan untuk ChatGPT/Gemini">
                                <i class="fa-solid fa-layer-group" style="color:#818CF8;"></i>
                                <span>Isi Per Step</span>
                            </button>
                            <button type="button" class="btn btn-primary btn-sm" onclick="generatePrdWithDirectAi()" style="background:linear-gradient(135deg, #10B981 0%, #059669 100%); border-color:#059669; font-weight:800; box-shadow:0 0 16px rgba(16,185,129,0.35);">
                                <i class="fa-solid fa-bolt" style="color:#FDE047; margin-right:6px;"></i><span id="banner-btn-ai-text">Isi Semua by AI</span>
                            </button>
                        </div>
                    </div>

                    <div class="grid-2">
                        <div class="form-group">
                            <label class="form-label">Nama Produk / Aplikasi <span style="color:#F43F5E;">*</span></label>
                            <input type="text" id="p-name" class="form-control" placeholder="Tuliskan nama produk atau aplikasi...">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Industri &bull; Sektor <span style="color:#F43F5E;">*</span></label>
                            <input type="text" id="p-industry" class="form-control" placeholder="Contoh: Heavy Industry, Mining, Logistics, Healthcare...">
                        </div>
                    </div>

                    <div class="grid-2">
                        <div class="form-group">
                            <label class="form-label">Departemen Pengguna Utama</label>
                            <input type="text" id="p-dept" class="form-control" placeholder="Contoh: Operations, Maintenance, Engineering...">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Target Organisasi / Pengguna Akhir</label>
                            <input type="text" id="p-target-org" class="form-control" placeholder="Contoh: Kontraktor Tambang, Holding Korporasi, Manufaktur...">
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Deskripsi Singkat Produk <span style="color:#F43F5E;">*</span></label>
                        <textarea id="p-desc" class="form-control" rows="2" placeholder="Jelaskan ringkasan sistem, tujuan fungsional, dan nilai tambah bagi operasional..."></textarea>
                    </div>

                    <div class="grid-2">
                        <div class="form-group">
                            <label class="form-label">Problem Statement (Masalah Nyata di Lapangan) <span style="color:#F43F5E;">*</span></label>
                            <textarea id="p-problem" class="form-control" rows="3" placeholder="Masalah utama yang ingin diselesaikan oleh aplikasi ini..."></textarea>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Business Objectives (Tujuan Bisnis Utama) <span style="color:#F43F5E;">*</span></label>
                            <textarea id="p-objective" class="form-control" rows="3" placeholder="Target kuantitatif atau kualitatif yang ingin dicapai..."></textarea>
                        </div>
                    </div>

                    <div class="grid-2">
                        <div class="form-group">
                            <label class="form-label">In-Scope (Ruang Lingkup Termasuk)</label>
                            <textarea id="p-scope" class="form-control" rows="3" placeholder="Fitur dan batasan yang WAJIB ada pada rilis ini..."></textarea>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Out-of-Scope (Bukan Ruang Lingkup Rilis Ini)</label>
                            <textarea id="p-out-scope" class="form-control" rows="3" placeholder="Hal-hal yang TIDAK dikerjakan pada tahap ini..."></textarea>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Success Criteria (Indikator Keberhasilan Produk)</label>
                        <textarea id="p-success" class="form-control" rows="2" placeholder="Kriteria atau metrik penentu suksesnya produk..."></textarea>
                    </div>

                    <div class="form-group">
                        <label class="form-label">
                            <span>Additional Requirements (Catatan Tambahan / Kebutuhan Khusus)</span>
                            <span style="font-size:11px; color:var(--text-muted);">Sangat disarankan &bull; Bantu AI memahami aturan unik Anda</span>
                        </label>
                        <textarea id="p-additional" class="form-control" rows="3" placeholder="Tuliskan aturan operasional khusus, SOP perusahaan, atau instruksi kritis yang harus dipatuhi sistem..."></textarea>
                    </div>

                    <div class="step-footer-nav">
                        <div></div>
                        <button type="button" class="btn btn-primary" onclick="goToStep(2)">
                            <span>Lanjut: 5 Pilar Arsitektur</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- STEP 2: 5 PILAR ARSITEKTUR (SUBTIPE DIHAPUS SEMUA) -->
            <div class="step-panel" id="panel-step-2">
                <div class="card-box highlight">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:18px;">
                        <div>
                            <span class="badge badge-indigo">Langkah 2 Dari 16</span>
                            <h2 class="font-outfit" style="font-size:20px; font-weight:800; color:#FFFFFF; margin:6px 0 2px;">5 Pilar Arsitektur</h2>
                            <p style="font-size:12px; color:var(--text-secondary);">Pilih salah satu dari 5 Pilar Arsitektur utama sebagai fondasi sistem Anda.</p>
                        </div>
                        <span class="badge badge-emerald"><i class="fa-solid fa-layer-group" style="margin-right:4px;"></i>5 Pilar Utama</span>
                    </div>

                    <!-- 5 Architecture Pillars Large Cards -->
                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px; margin-bottom:24px;" id="pillars-large-container">
                        <!-- Rendered by JS: 5 Pillars Only -->
                    </div>

                    <!-- Active Pillar Summary Pill -->
                    <div style="background:#07090E; border:1px solid #1E293B; border-radius:12px; padding:16px 20px; display:flex; align-items:center; justify-content:space-between; margin-bottom:16px;">
                        <div style="display:flex; align-items:center; gap:14px;">
                            <div id="active-pillar-icon-box" style="width:40px; height:40px; border-radius:10px; background:rgba(99,102,241,0.18); border:1px solid rgba(99,102,241,0.3); display:flex; align-items:center; justify-content:center; color:#818CF8; font-size:18px;">
                                <i class="fa-solid fa-cube"></i>
                            </div>
                            <div>
                                <div style="font-size:11px; color:var(--text-muted); text-transform:uppercase; font-weight:700;">Pilar Arsitektur Terpilih:</div>
                                <div style="font-size:14px; font-weight:800; color:#FFFFFF;" id="active-pillar-title">Belum Dipilih (Klik salah satu pilar di atas)</div>
                            </div>
                        </div>
                        <span class="badge badge-indigo" id="active-pillar-badge">PILIH PILAR</span>
                    </div>

                    <div class="step-footer-nav">
                        <button type="button" class="btn btn-secondary" onclick="goToStep(1)">
                            <i class="fa-solid fa-arrow-left"></i>
                            <span>Kembali: Project Definition</span>
                        </button>
                        <button type="button" class="btn btn-primary" onclick="goToStep(3)">
                            <span>Lanjut: Users &amp; Roles</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- STEP 3: USERS & ROLES BUILDER -->
            <div class="step-panel" id="panel-step-3">
                <div class="card-box highlight">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
                        <div>
                            <span class="badge badge-indigo">Langkah 3 Dari 16</span>
                            <h2 class="font-outfit" style="font-size:20px; font-weight:800; color:#FFFFFF; margin:6px 0 2px;">Users, Personas &amp; Roles</h2>
                            <p style="font-size:12px; color:var(--text-secondary);">Definisikan seluruh aktor sistem. Tentukan nama role, departemen, tanggung jawab, dan persona operasional mereka.</p>
                        </div>
                        <div style="display:flex; gap:8px;">
                            <button type="button" class="btn btn-secondary btn-sm" onclick="generateStepWithDirectAi('step3', 'Step 3: Users & Roles')" title="Generate hanya Role & Persona langsung via AI" style="border-color:#6366F1; color:#A5B4FC;">
                                <i class="fa-solid fa-wand-magic-sparkles" style="color:#FDE047;"></i>
                                <span>Isi Step Ini by AI</span>
                            </button>
                            <button type="button" class="btn btn-primary btn-sm" onclick="openRoleModal()">
                                <i class="fa-solid fa-user-plus"></i>
                                <span>Tambah Role Baru</span>
                            </button>
                        </div>
                    </div>

                    <div class="grid-3" id="roles-cards-container" style="margin-bottom:20px;">
                        <!-- Rendered by JS -->
                    </div>

                    <div class="step-footer-nav">
                        <button type="button" class="btn btn-secondary" onclick="goToStep(2)">
                            <i class="fa-solid fa-arrow-left"></i>
                            <span>Kembali: 5 Pilar Arsitektur</span>
                        </button>
                        <button type="button" class="btn btn-primary" onclick="goToStep(4)">
                            <span>Lanjut: Modules &amp; Features</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- STEP 4: MODULES & FEATURES BUILDER -->
            <div class="step-panel" id="panel-step-4">
                <div class="card-box highlight">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
                        <div>
                            <span class="badge badge-indigo">Langkah 4 Dari 16</span>
                            <h2 class="font-outfit" style="font-size:20px; font-weight:800; color:#FFFFFF; margin:6px 0 2px;">Modules &amp; Functional Features</h2>
                            <p style="font-size:12px; color:var(--text-secondary);">Hierarki arsitektur: Module &rarr; Submodule &rarr; Feature. Setiap fitur memiliki prioritas (P0-P3), user utama, dan expected outcome.</p>
                        </div>
                        <div style="display:flex; gap:8px;">
                            <button type="button" class="btn btn-secondary btn-sm" onclick="generateStepWithDirectAi('step4', 'Step 4: Modules & Features')" title="Generate modul & fitur langsung via AI" style="border-color:#6366F1; color:#A5B4FC;">
                                <i class="fa-solid fa-wand-magic-sparkles" style="color:#FDE047;"></i>
                                <span>Isi Step Ini by AI</span>
                            </button>
                            <button type="button" class="btn btn-secondary btn-sm" onclick="openModuleModal()">
                                <i class="fa-solid fa-folder-plus"></i>
                                <span>Tambah Modul</span>
                            </button>
                            <button type="button" class="btn btn-primary btn-sm" onclick="openFeatureModal()">
                                <i class="fa-solid fa-plus"></i>
                                <span>Tambah Fitur</span>
                            </button>
                        </div>
                    </div>

                    <div id="modules-list-container" style="display:flex; flex-direction:column; gap:16px; margin-bottom:20px;">
                        <!-- Rendered by JS -->
                    </div>

                    <div class="step-footer-nav">
                        <button type="button" class="btn btn-secondary" onclick="goToStep(3)">
                            <i class="fa-solid fa-arrow-left"></i>
                            <span>Kembali: Roles</span>
                        </button>
                        <button type="button" class="btn btn-primary" onclick="goToStep(5)">
                            <span>Lanjut: Business Process &amp; Workflow</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- STEP 5: BUSINESS PROCESS & WORKFLOW BUILDER -->
            <div class="step-panel" id="panel-step-5">
                <div class="card-box highlight">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
                        <div>
                            <span class="badge badge-indigo">Langkah 5 Dari 16</span>
                            <h2 class="font-outfit" style="font-size:20px; font-weight:800; color:#FFFFFF; margin:6px 0 2px;">Business Process &amp; Visual Workflow</h2>
                            <p style="font-size:12px; color:var(--text-secondary);">Rangkai alur operasional bertahap dari awal hingga selesai. Lengkapi dengan trigger, aktor, input, action, dan approval gate.</p>
                        </div>
                        <div style="display:flex; gap:8px;">
                            <button type="button" class="btn btn-secondary btn-sm" onclick="generateStepWithDirectAi('step5', 'Step 5: Workflows')" title="Generate alur proses operasional langsung via AI" style="border-color:#6366F1; color:#A5B4FC;">
                                <i class="fa-solid fa-wand-magic-sparkles" style="color:#FDE047;"></i>
                                <span>Isi Step Ini by AI</span>
                            </button>
                            <button type="button" class="btn btn-primary btn-sm" onclick="openWorkflowModal()">
                                <i class="fa-solid fa-plus"></i>
                                <span>Tambah Tahap Alur</span>
                            </button>
                        </div>
                    </div>

                    <div class="wf-node-track" id="workflow-nodes-container" style="margin-bottom:20px;">
                        <!-- Rendered by JS -->
                    </div>

                    <div class="step-footer-nav">
                        <button type="button" class="btn btn-secondary" onclick="goToStep(4)">
                            <i class="fa-solid fa-arrow-left"></i>
                            <span>Kembali: Modules</span>
                        </button>
                        <button type="button" class="btn btn-primary" onclick="goToStep(6)">
                            <span>Lanjut: Business Rules</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- STEP 6: BUSINESS RULES BUILDER -->
            <div class="step-panel" id="panel-step-6">
                <div class="card-box highlight">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
                        <div>
                            <span class="badge badge-indigo">Langkah 6 Dari 16</span>
                            <h2 class="font-outfit" style="font-size:20px; font-weight:800; color:#FFFFFF; margin:6px 0 2px;">Enterprise Business Rules</h2>
                            <p style="font-size:12px; color:var(--text-secondary);">Aturan logika bisnis dan validasi ketat (Condition, Action, Exception, Severity). Pisahkan dari deskripsi visual UI.</p>
                        </div>
                        <div style="display:flex; gap:8px;">
                            <button type="button" class="btn btn-secondary btn-sm" onclick="generateStepWithDirectAi('step6', 'Step 6: Business Rules')" title="Generate aturan bisnis & validasi langsung via AI" style="border-color:#6366F1; color:#A5B4FC;">
                                <i class="fa-solid fa-wand-magic-sparkles" style="color:#FDE047;"></i>
                                <span>Isi Step Ini by AI</span>
                            </button>
                            <button type="button" class="btn btn-primary btn-sm" onclick="openRuleModal()">
                                <i class="fa-solid fa-plus"></i>
                                <span>Tambah Business Rule</span>
                            </button>
                        </div>
                    </div>

                    <div id="rules-cards-container" style="display:flex; flex-direction:column; gap:12px; margin-bottom:20px;">
                        <!-- Rendered by JS -->
                    </div>

                    <div class="step-footer-nav">
                        <button type="button" class="btn btn-secondary" onclick="goToStep(5)">
                            <i class="fa-solid fa-arrow-left"></i>
                            <span>Kembali: Workflow</span>
                        </button>
                        <button type="button" class="btn btn-primary" onclick="goToStep(7)">
                            <span>Lanjut: Data Model (Entity Builder)</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- STEP 7: DATA MODEL (ENTITY BUILDER) -->
            <div class="step-panel" id="panel-step-7">
                <div class="card-box highlight">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
                        <div>
                            <span class="badge badge-indigo">Langkah 7 Dari 16</span>
                            <h2 class="font-outfit" style="font-size:20px; font-weight:800; color:#FFFFFF; margin:6px 0 2px;">Data Model &amp; Entity Architecture</h2>
                            <p style="font-size:12px; color:var(--text-secondary);">Entity Builder terstruktur: Field types, validasi, dan relasi One-to-One / One-to-Many / Many-to-Many.</p>
                        </div>
                        <div style="display:flex; gap:8px;">
                            <button type="button" class="btn btn-secondary btn-sm" onclick="generateStepWithDirectAi('step7', 'Step 7: Data Entities')" title="Generate skema entitas database langsung via AI" style="border-color:#6366F1; color:#A5B4FC;">
                                <i class="fa-solid fa-wand-magic-sparkles" style="color:#FDE047;"></i>
                                <span>Isi Step Ini by AI</span>
                            </button>
                            <button type="button" class="btn btn-primary btn-sm" onclick="openEntityModal()">
                                <i class="fa-solid fa-database"></i>
                                <span>Tambah Entity Baru</span>
                            </button>
                        </div>
                    </div>

                    <div id="entities-cards-container" style="display:flex; flex-direction:column; gap:18px; margin-bottom:20px;">
                        <!-- Rendered by JS -->
                    </div>

                    <div class="step-footer-nav">
                        <button type="button" class="btn btn-secondary" onclick="goToStep(6)">
                            <i class="fa-solid fa-arrow-left"></i>
                            <span>Kembali: Business Rules</span>
                        </button>
                        <button type="button" class="btn btn-primary" onclick="goToStep(8)">
                            <span>Lanjut: Permissions / RBAC</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- STEP 8: PERMISSIONS / RBAC MATRIX -->
            <div class="step-panel" id="panel-step-8">
                <div class="card-box highlight">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
                        <div>
                            <span class="badge badge-indigo">Langkah 8 Dari 16</span>
                            <h2 class="font-outfit" style="font-size:20px; font-weight:800; color:#FFFFFF; margin:6px 0 2px;">Role-Based Access Control (RBAC) Matrix</h2>
                            <p style="font-size:12px; color:var(--text-secondary);">Matriks hak akses dinamis yang dihasilkan dari Role (Step 3) dan Modul (Step 4).</p>
                        </div>
                        <div style="display:flex; gap:6px;">
                            <button type="button" class="btn btn-secondary btn-sm" onclick="generateStepWithDirectAi('step8', 'Step 8: RBAC Permissions')" title="Generate matriks hak akses RBAC via AI" style="border-color:#6366F1; color:#A5B4FC;">
                                <i class="fa-solid fa-wand-magic-sparkles" style="color:#FDE047;"></i>
                                <span>Isi Step Ini by AI</span>
                            </button>
                            <button type="button" class="btn btn-secondary btn-sm" onclick="grantAllPermissions()">
                                <i class="fa-solid fa-check-double"></i> Centang Semua
                            </button>
                            <button type="button" class="btn btn-secondary btn-sm" onclick="clearAllPermissions()">
                                <i class="fa-solid fa-ban"></i> Reset Matrix
                            </button>
                        </div>
                    </div>

                    <div class="table-responsive" style="margin-bottom:20px;">
                        <table class="custom-table" id="rbac-matrix-table">
                            <!-- Rendered by JS -->
                        </table>
                    </div>

                    <div class="step-footer-nav">
                        <button type="button" class="btn btn-secondary" onclick="goToStep(7)">
                            <i class="fa-solid fa-arrow-left"></i>
                            <span>Kembali: Data Model</span>
                        </button>
                        <button type="button" class="btn btn-primary" onclick="goToStep(9)">
                            <span>Lanjut: KPI &amp; Reporting</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- STEP 9: KPI & REPORTING BUILDER -->
            <div class="step-panel" id="panel-step-9">
                <div class="card-box highlight">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
                        <div>
                            <span class="badge badge-indigo">Langkah 9 Dari 16</span>
                            <h2 class="font-outfit" style="font-size:20px; font-weight:800; color:#FFFFFF; margin:6px 0 2px;">Key Performance Indicators (KPI) &amp; Reporting</h2>
                            <p style="font-size:12px; color:var(--text-secondary);">Definisikan metrik kinerja utama beserta formula perhitungan, target, dan tipe visualisasinya.</p>
                        </div>
                        <div style="display:flex; gap:8px;">
                            <button type="button" class="btn btn-secondary btn-sm" onclick="generateStepWithDirectAi('step9', 'Step 9: KPIs & Reporting')" title="Generate metrik KPI via AI" style="border-color:#6366F1; color:#A5B4FC;">
                                <i class="fa-solid fa-wand-magic-sparkles" style="color:#FDE047;"></i>
                                <span>Isi Step Ini by AI</span>
                            </button>
                            <button type="button" class="btn btn-primary btn-sm" onclick="openKpiModal()">
                                <i class="fa-solid fa-chart-line"></i>
                                <span>Tambah Metrik KPI</span>
                            </button>
                        </div>
                    </div>

                    <div class="grid-3" id="kpis-cards-container" style="margin-bottom:20px;">
                        <!-- Rendered by JS -->
                    </div>

                    <div class="step-footer-nav">
                        <button type="button" class="btn btn-secondary" onclick="goToStep(8)">
                            <i class="fa-solid fa-arrow-left"></i>
                            <span>Kembali: RBAC</span>
                        </button>
                        <button type="button" class="btn btn-primary" onclick="goToStep(10)">
                            <span>Lanjut: Notification Protocols</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- STEP 10: NOTIFICATION BUILDER -->
            <div class="step-panel" id="panel-step-10">
                <div class="card-box highlight">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
                        <div>
                            <span class="badge badge-indigo">Langkah 10 Dari 16</span>
                            <h2 class="font-outfit" style="font-size:20px; font-weight:800; color:#FFFFFF; margin:6px 0 2px;">Notification &amp; Escalation Protocols</h2>
                            <p style="font-size:12px; color:var(--text-secondary);">Aturan pengiriman alert otomatis: event pemicu, recipient role, channel, dan aturan eskalasi.</p>
                        </div>
                        <div style="display:flex; gap:8px;">
                            <button type="button" class="btn btn-secondary btn-sm" onclick="generateStepWithDirectAi('step10', 'Step 10: Notifications')" title="Generate notifikasi & alert via AI" style="border-color:#6366F1; color:#A5B4FC;">
                                <i class="fa-solid fa-wand-magic-sparkles" style="color:#FDE047;"></i>
                                <span>Isi Step Ini by AI</span>
                            </button>
                            <button type="button" class="btn btn-primary btn-sm" onclick="openNotificationModal()">
                                <i class="fa-solid fa-bell"></i>
                                <span>Tambah Notifikasi</span>
                            </button>
                        </div>
                    </div>

                    <div class="grid-2" id="notifications-cards-container" style="margin-bottom:20px;">
                        <!-- Rendered by JS -->
                    </div>

                    <div class="step-footer-nav">
                        <button type="button" class="btn btn-secondary" onclick="goToStep(9)">
                            <i class="fa-solid fa-arrow-left"></i>
                            <span>Kembali: KPI</span>
                        </button>
                        <button type="button" class="btn btn-primary" onclick="goToStep(11)">
                            <span>Lanjut: Integration Requirements</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- STEP 11: INTEGRATION REQUIREMENTS -->
            <div class="step-panel" id="panel-step-11">
                <div class="card-box highlight">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
                        <div>
                            <span class="badge badge-indigo">Langkah 11 Dari 16</span>
                            <h2 class="font-outfit" style="font-size:20px; font-weight:800; color:#FFFFFF; margin:6px 0 2px;">External System Integration Requirements</h2>
                            <p style="font-size:12px; color:var(--text-secondary);">Daftar sistem eksternal yang dihubungkan (ERP, IoT, API). Untuk MVP, integrasi disimulasikan via mock state.</p>
                        </div>
                        <div style="display:flex; gap:8px;">
                            <button type="button" class="btn btn-secondary btn-sm" onclick="generateStepWithDirectAi('step11', 'Step 11: System Integrations')" title="Generate spesifikasi integrasi via AI" style="border-color:#6366F1; color:#A5B4FC;">
                                <i class="fa-solid fa-wand-magic-sparkles" style="color:#FDE047;"></i>
                                <span>Isi Step Ini by AI</span>
                            </button>
                            <button type="button" class="btn btn-primary btn-sm" onclick="openIntegrationModal()">
                                <i class="fa-solid fa-network-wired"></i>
                                <span>Tambah Integrasi</span>
                            </button>
                        </div>
                    </div>

                    <div class="grid-2" id="integrations-cards-container" style="margin-bottom:20px;">
                        <!-- Rendered by JS -->
                    </div>

                    <div class="step-footer-nav">
                        <button type="button" class="btn btn-secondary" onclick="goToStep(10)">
                            <i class="fa-solid fa-arrow-left"></i>
                            <span>Kembali: Notification</span>
                        </button>
                        <button type="button" class="btn btn-primary" onclick="goToStep(12)">
                            <span>Lanjut: UI/UX Architecture</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- STEP 12: UI/UX ARCHITECTURE & 60 THEMES -->
            <div class="step-panel" id="panel-step-12">
                <div class="card-box highlight">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
                        <div>
                            <span class="badge badge-indigo">Langkah 12 Dari 16</span>
                            <h2 class="font-outfit" style="font-size:20px; font-weight:800; color:#FFFFFF; margin:6px 0 2px;">UI/UX Architecture &amp; 60 Themes Catalog</h2>
                            <p style="font-size:12px; color:var(--text-secondary);">Pilih estetika visual dari 60 gaya desain modern dan petakan struktur halaman/screen yang mewadahi fitur-fitur PRD.</p>
                        </div>
                        <div style="display:flex; gap:8px;">
                            <button type="button" class="btn btn-secondary btn-sm" onclick="generateStepWithDirectAi('step13', 'Step 12: UI Screens Architecture')" title="Generate pemetaan screen & UI via AI" style="border-color:#6366F1; color:#A5B4FC;">
                                <i class="fa-solid fa-wand-magic-sparkles" style="color:#FDE047;"></i>
                                <span>Isi Step Ini by AI</span>
                            </button>
                            <button type="button" class="btn btn-primary btn-sm" onclick="openScreenModal()">
                                <i class="fa-solid fa-desktop"></i>
                                <span>Tambah Screen</span>
                            </button>
                        </div>
                    </div>

                    <!-- Selected Theme Pill -->
                    <div id="selected-theme-summary-card" style="background:#07090E; border:1px solid #1E293B; border-radius:12px; padding:14px 18px; display:flex; align-items:center; justify-content:space-between; margin-bottom:18px;">
                        <div style="display:flex; align-items:center; gap:12px;">
                            <div id="active-theme-swatch" style="width:32px; height:32px; border-radius:8px; background:linear-gradient(135deg, #6366F1, #3B82F6); border:1px solid rgba(255,255,255,0.2);"></div>
                            <div>
                                <div style="font-size:11px; color:var(--text-muted); text-transform:uppercase; font-weight:700;">Gaya Visual Terpilih:</div>
                                <div style="font-size:13.5px; font-weight:800; color:#FFFFFF;" id="active-theme-name">Bento UI (MODERN)</div>
                            </div>
                        </div>
                        <span class="badge badge-emerald">✓ Terhubung ke PRD Tokens</span>
                    </div>

                    <!-- Layout Archetype Selector -->
                    <div class="grid-3" style="margin-bottom:18px;">
                        <div class="form-group">
                            <label class="form-label">Tata Letak Shell (Layout Shell)</label>
                            <select id="ui-layout-select" class="form-control" onchange="updateUiLayout(this.value)">
                                <option value="sidebar_topbar">Sidebar Shell + Top Header (Standard Enterprise)</option>
                                <option value="dual_sidebar">Dual Sidebar + Control Center (Complex Operations)</option>
                                <option value="bento_multipanel">Bento Asymmetrical Multi-Panel (Analytics)</option>
                                <option value="floating_dock">Floating Clean Dock (Modern Minimal)</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Tipe Navigasi (Navigation Type)</label>
                            <select id="ui-nav-select" class="form-control" onchange="updateUiNav(this.value)">
                                <option value="sidebar">Left Sidebar Fixed + Collapsible Drawer</option>
                                <option value="topbar">Top Fixed Navigation Bar</option>
                                <option value="hybrid">Hybrid (Top Module Tabs + Left Submodule Menu)</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Standar Aksesibilitas (Accessibility)</label>
                            <select id="ui-a11y-select" class="form-control" onchange="updateUiA11y(this.value)">
                                <option value="wcag_aa">WCAG 2.1 AA Compliant (Kontras Minimal 4.5:1)</option>
                                <option value="wcag_aaa">WCAG 2.1 AAA High Contrast (Kontras 7:1)</option>
                                <option value="touch_optimized">Touch-Friendly Tablet / Mobile Site (Min 44px tap targets)</option>
                            </select>
                        </div>
                    </div>

                    <!-- Screen Mapping List -->
                    <div style="font-size:12.5px; font-weight:700; color:#FFFFFF; margin-bottom:8px;">
                        Screen &amp; Information Architecture Mapping:
                    </div>
                    <div class="grid-3" id="screens-cards-container" style="margin-bottom:20px;">
                        <!-- Rendered by JS -->
                    </div>

                    <!-- 60 Themes Catalog Grid Filter Header -->
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:10px;">
                        <div style="font-size:12.5px; font-weight:700; color:#FFFFFF;">
                            Katalog 60 Gaya Desain UI/UX:
                        </div>
                        <input type="text" id="search-theme-input" class="form-control" placeholder="Cari gaya (Bento, Glass, Neumorphism, Cyberpunk)..." style="width:260px;" oninput="filterThemeCards(this.value)">
                    </div>

                    <!-- Category Filter Buttons -->
                    <div id="theme-category-filters" style="display:flex; gap:6px; overflow-x:auto; padding-bottom:8px; margin-bottom:14px;">
                        <!-- Rendered by JS -->
                    </div>

                    <!-- 60 Themes Visual Cards Grid -->
                    <div class="grid-4" id="themes-grid-container" style="max-height:440px; overflow-y:auto; padding-right:6px; margin-bottom:18px;">
                        <!-- Rendered by JS -->
                    </div>

                    <div class="step-footer-nav">
                        <button type="button" class="btn btn-secondary" onclick="goToStep(11)">
                            <i class="fa-solid fa-arrow-left"></i>
                            <span>Kembali: Integrations</span>
                        </button>
                        <button type="button" class="btn btn-primary" onclick="goToStep(13)">
                            <span>Lanjut: Technical MVP Spec</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- STEP 13: TECHNICAL MVP SPECIFICATION -->
            <div class="step-panel" id="panel-step-13">
                <div class="card-box highlight">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
                        <div>
                            <span class="badge badge-indigo">Langkah 13 Dari 16</span>
                            <h2 class="font-outfit" style="font-size:20px; font-weight:800; color:#FFFFFF; margin:6px 0 2px;">Technical MVP Specification (Single-File Architecture)</h2>
                            <p style="font-size:12px; color:var(--text-secondary);">Target implementasi MVP: satu file <code>index.html</code> mandiri tanpa database dan backend sungguhan.</p>
                        </div>
                        <span class="badge badge-emerald"><i class="fa-solid fa-file-code" style="margin-right:4px;"></i>Strict 1-File MVP</span>
                    </div>

                    <div class="grid-2" style="margin-bottom:16px;">
                        <div style="background:#07090E; border:1px solid #1E293B; border-radius:12px; padding:16px;">
                            <div style="font-size:13px; font-weight:700; color:#38BDF8; margin-bottom:10px;">
                                <i class="fa-solid fa-layer-group" style="margin-right:6px;"></i> Standar Single-File MVP Target
                            </div>
                            <ul style="font-size:12px; color:#94A3B8; line-height:1.8; margin-left:18px;">
                                <li><strong>Target Deliverable:</strong> Tepat satu file <code>index.html</code> mandiri.</li>
                                <li><strong>Struktur Internal:</strong> HTML5 + Embedded CSS + Vanilla JS + Mock Data.</li>
                                <li><strong>Dependencies:</strong> Zero npm / zero bundlers. Hanya CDN (FontAwesome, Tailwind, SweetAlert2).</li>
                                <li><strong>Offline Capability:</strong> Dapat dijalankan langsung dengan klik dua kali di browser.</li>
                            </ul>
                        </div>

                        <div style="background:#07090E; border:1px solid #1E293B; border-radius:12px; padding:16px;">
                            <div style="font-size:13px; font-weight:700; color:#10B981; margin-bottom:10px;">
                                <i class="fa-solid fa-database" style="margin-right:6px;"></i> Standar State &amp; Data Mocking
                            </div>
                            <ul style="font-size:12px; color:#94A3B8; line-height:1.8; margin-left:18px;">
                                <li><strong>Persistent State:</strong> <code>localStorage</code> browser untuk menyimpan transaksi dummy.</li>
                                <li><strong>Seed Data:</strong> In-memory mock arrays (10-15 baris data realistis).</li>
                                <li><strong>Interaktivitas Fungsional:</strong> Formulir Create/Edit bekerja, filter bekerja, status state berubah nyata.</li>
                                <li><strong>Autentikasi:</strong> Mock User Switcher di header untuk mensimulasikan role tanpa backend.</li>
                            </ul>
                        </div>
                    </div>

                    <div class="card-box" style="background:#080C14; margin-bottom:20px;">
                        <div style="font-size:13px; font-weight:700; color:#E2E8FF; margin-bottom:8px;">
                            <i class="fa-solid fa-shield-halved" style="color:#F59E0B; margin-right:6px;"></i> Catatan Pembatasan untuk AI Implementation Agent:
                        </div>
                        <p style="font-size:12px; color:#94A3B8; line-height:1.6;">
                            Prompt implementasi MVP akan secara ketat melarang AI membuat backend server eksternal, server database SQL/NoSQL terpisah, atau file CSS/JS terpisah. Semua requirement PRD diwujudkan dalam interaction layer yang fungsional di browser.
                        </p>
                    </div>

                    <div class="step-footer-nav">
                        <button type="button" class="btn btn-secondary" onclick="goToStep(12)">
                            <i class="fa-solid fa-arrow-left"></i>
                            <span>Kembali: UI/UX Architecture</span>
                        </button>
                        <button type="button" class="btn btn-primary" onclick="goToStep(14)">
                            <span>Lanjut: PRD Review &amp; Completeness</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- STEP 14: PRD REVIEW & COMPLETENESS CHECKER -->
            <div class="step-panel" id="panel-step-14">
                <div class="card-box highlight">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
                        <div>
                            <span class="badge badge-indigo">Langkah 14 Dari 16</span>
                            <h2 class="font-outfit" style="font-size:20px; font-weight:800; color:#FFFFFF; margin:6px 0 2px;">PRD Completeness Checker &amp; Review</h2>
                            <p style="font-size:12px; color:var(--text-secondary);">Verifikasi otomatis kelengkapan seluruh 13 seksi spesifikasi sebelum menghasilkan dokumen PRD final.</p>
                        </div>
                        <div style="text-align:right;">
                            <div style="font-size:11px; color:var(--text-muted); font-weight:700;">TOTAL SKOR KELENGKAPAN:</div>
                            <div class="font-outfit" style="font-size:24px; font-weight:900; color:#34D399;" id="checker-score-display">0%</div>
                        </div>
                    </div>

                    <!-- Completeness Checklist Grid -->
                    <div class="grid-2" id="completeness-checklist-grid" style="margin-bottom:20px;">
                        <!-- Rendered by JS -->
                    </div>

                    <!-- Warning Alerts Container -->
                    <div id="checker-warnings-box" style="margin-bottom:20px;"></div>

                    <div class="step-footer-nav">
                        <button type="button" class="btn btn-secondary" onclick="goToStep(13)">
                            <i class="fa-solid fa-arrow-left"></i>
                            <span>Kembali: Technical MVP Spec</span>
                        </button>
                        <div style="display:flex; gap:10px;">
                            <button type="button" class="btn btn-emerald" onclick="goToStep(15)">
                                <i class="fa-solid fa-file-lines"></i>
                                <span>Lanjut: Generate Quality PRD</span>
                            </button>
                            <button type="button" class="btn btn-primary" onclick="goToStep(16)">
                                <i class="fa-solid fa-robot"></i>
                                <span>Lanjut: Generate MVP Prompt</span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- STEP 15: GENERATE QUALITY PRD (HUMAN READABLE MARKDOWN) -->
            <div class="step-panel" id="panel-step-15">
                <div class="card-box highlight">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px; flex-wrap:wrap; gap:12px;">
                        <div>
                            <span class="badge badge-emerald">Dokumen PRD Final</span>
                            <h2 class="font-outfit" style="font-size:20px; font-weight:800; color:#FFFFFF; margin:6px 0 2px;">Quality Product Requirements Document (PRD)</h2>
                            <p style="font-size:12px; color:var(--text-secondary);">Dokumen spesifikasi produk 24-seksi komprehensif, terstruktur, berbasis tabel, dan bebas AI slop.</p>
                        </div>
                        <div style="display:flex; align-items:center; gap:8px;">
                            <button type="button" class="btn btn-primary btn-sm" onclick="copyPrdMarkdown()">
                                <i class="fa-regular fa-copy"></i> Salin PRD Markdown
                            </button>
                            <button type="button" class="btn btn-secondary btn-sm" onclick="downloadPrdMarkdown()">
                                <i class="fa-solid fa-download"></i> Unduh .MD
                            </button>
                            <button type="button" class="btn btn-secondary btn-sm" onclick="printPrdDocument()">
                                <i class="fa-solid fa-print"></i> Cetak
                            </button>
                        </div>
                    </div>

                    <!-- View Switcher Tabs -->
                    <div style="display:flex; gap:8px; margin-bottom:12px; border-bottom:1px solid #1E293B; padding-bottom:8px;">
                        <button type="button" class="btn btn-secondary btn-sm" id="btn-tab-prd-preview" onclick="switchPrdTab('preview')">
                            <i class="fa-solid fa-eye"></i> Pratinjau Terformat (Rich Preview)
                        </button>
                        <button type="button" class="btn btn-secondary btn-sm" id="btn-tab-prd-raw" onclick="switchPrdTab('raw')">
                            <i class="fa-solid fa-code"></i> Raw Markdown Source
                        </button>
                        <span style="font-size:11.5px; color:#94A3B8; margin-left:auto; align-self:center;" id="prd-lines-count">0 Baris</span>
                    </div>

                    <!-- Formatted Preview -->
                    <div id="prd-preview-container" class="markdown-render" style="display:block;">
                        <!-- Rendered by JS -->
                    </div>

                    <!-- Raw Markdown Textarea -->
                    <textarea id="prd-raw-textarea" class="form-control font-mono" style="display:none; height:600px; font-size:12px; background:#05070B; color:#CBD5E1; line-height:1.6; border:1px solid #1E293B;" readonly></textarea>

                    <div class="step-footer-nav">
                        <button type="button" class="btn btn-secondary" onclick="goToStep(14)">
                            <i class="fa-solid fa-arrow-left"></i>
                            <span>Kembali: Review &amp; Completeness</span>
                        </button>
                        <button type="button" class="btn btn-primary" onclick="goToStep(16)">
                            <span>Lanjut: Generate MVP Implementation Prompt</span>
                            <i class="fa-solid fa-robot"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- STEP 16: GENERATE MVP IMPLEMENTATION PROMPT -->
            <div class="step-panel" id="panel-step-16">
                <div class="card-box highlight">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px; flex-wrap:wrap; gap:12px;">
                        <div>
                            <span class="badge badge-indigo">AI Coding Agent Prompt</span>
                            <h2 class="font-outfit" style="font-size:20px; font-weight:800; color:#FFFFFF; margin:6px 0 2px;">AI MVP Implementation Prompt</h2>
                            <p style="font-size:12px; color:var(--text-secondary);">Prompt khusus yang menginstruksikan AI coding agent untuk membangun PRD menjadi single-file <code>index.html</code> fungsional.</p>
                        </div>
                        <div style="display:flex; align-items:center; gap:8px;">
                            <button type="button" class="btn btn-primary" onclick="copyMvpPrompt()">
                                <i class="fa-regular fa-copy"></i> Salin Prompt MVP
                            </button>
                            <button type="button" class="btn btn-secondary" onclick="downloadMvpPromptTxt()">
                                <i class="fa-solid fa-download"></i> Unduh .TXT
                            </button>
                        </div>
                    </div>

                    <!-- Visual Summary Banner -->
                    <div style="background:linear-gradient(135deg, #0F172A 0%, #1E1B4B 50%, #0F172A 100%); border:1px solid #312E81; border-radius:14px; padding:16px 20px; margin-bottom:16px;">
                        <div style="font-size:11px; font-weight:800; color:#818CF8; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:4px;">Target Implementasi Coding Agent:</div>
                        <div style="font-size:13px; color:#E2E8FF; line-height:1.6;">
                            Single-file <code>index.html</code> &bull; Pure HTML5, CSS3 &amp; Vanilla JavaScript &bull; Mock State &amp; LocalStorage &bull; Zero Backend Server &bull; Zero Database Setup &bull; Langsung Berjalan Secara Offline.
                        </div>
                    </div>

                    <!-- Output Prompt Box -->
                    <div class="form-group" style="margin-bottom:20px;">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                            <label class="form-label font-mono" style="font-size:11.5px; color:#94A3B8;">mvp-implementation-prompt.txt (Single Source of Truth Injected)</label>
                            <span style="font-size:11px; color:#A5B4FC; font-weight:700;" id="prompt-lines-count">0 Baris</span>
                        </div>
                        <textarea id="mvp-prompt-box" class="form-control font-mono" style="height:480px; font-size:11.5px; background:#05070B; color:#CBD5E1; line-height:1.6; border:1px solid #1E293B;" readonly></textarea>
                    </div>

                    <div class="step-footer-nav">
                        <button type="button" class="btn btn-secondary" onclick="goToStep(15)">
                            <i class="fa-solid fa-arrow-left"></i>
                            <span>Kembali: Dokumen PRD</span>
                        </button>
                        <button type="button" class="btn btn-emerald" onclick="copyMvpPrompt()">
                            <i class="fa-regular fa-copy"></i>
                            <span>Salin ke Clipboard &bull; Siap Pakai di Claude / Cursor / Antigravity</span>
                        </button>
                    </div>
                </div>
            </div>
        </main>
    </div>
</div>

<!-- ==================== MODALS ==================== -->

<!-- TEMPAT SIMPAN SEMENTARA (DRAFT MANAGER MODAL) -->
<div class="modal-backdrop" id="modal-drafts">
    <div class="modal-box" style="max-width:720px;">
        <div class="modal-header">
            <div style="display:flex; align-items:center; gap:10px;">
                <div style="width:34px; height:34px; border-radius:8px; background:rgba(16,185,129,0.18); border:1px solid rgba(16,185,129,0.3); display:flex; align-items:center; justify-content:center; color:#34D399;">
                    <i class="fa-solid fa-box-archive"></i>
                </div>
                <div>
                    <h3 class="font-outfit" style="font-size:16px; font-weight:800; color:#FFFFFF; margin:0;">Tempat Simpan Sementara (Draft Manager)</h3>
                    <div style="font-size:11px; color:#94A3B8;">Simpan progres pengerjaan di browser tanpa perlu database eksternal</div>
                </div>
            </div>
            <button type="button" onclick="closeModal('modal-drafts')" style="background:transparent; border:none; color:#94A3B8; font-size:20px; cursor:pointer;">&times;</button>
        </div>
        <div class="modal-body">
            <!-- Form Simpan Draft Baru -->
            <div style="background:#07090E; border:1px solid #1E293B; border-radius:12px; padding:14px 16px; margin-bottom:18px;">
                <label class="form-label" style="margin-bottom:8px;">
                    <span>Simpan Status Pengerjaan Saat Ini Sebagai Draft Baru:</span>
                </label>
                <div style="display:flex; gap:8px;">
                    <input type="text" id="draft-name-input" class="form-control" placeholder="Contoh: Draft Aplikasi HR v1, Draft E-Commerce Revisi..." style="flex:1;">
                    <button type="button" class="btn btn-emerald" onclick="saveNamedDraft()">
                        <i class="fa-solid fa-floppy-disk"></i>
                        <span>Simpan Draft</span>
                    </button>
                </div>
            </div>

            <!-- Daftar Draft Tersimpan -->
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                <span style="font-size:12.5px; font-weight:700; color:#E2E8FF;">Daftar Draft Tersimpan di Browser:</span>
                <button type="button" class="btn btn-rose btn-sm" onclick="clearAllDrafts()" style="padding:3px 8px;">
                    <i class="fa-solid fa-trash-can"></i> Hapus Semua Draft
                </button>
            </div>

            <div id="drafts-list-container" style="display:flex; flex-direction:column; gap:8px; max-height:320px; overflow-y:auto; padding-right:4px;">
                <!-- Rendered by JS -->
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" onclick="closeModal('modal-drafts')">Tutup</button>
        </div>
    </div>
</div>

<!-- MODAL FORMAT PROMPT AI & IMPOR JSON -->
<div class="modal-backdrop" id="modal-ai-json">
    <div class="modal-box" style="max-width:840px; max-height:92vh; display:flex; flex-direction:column;">
        <div class="modal-header">
            <div style="display:flex; align-items:center; gap:10px;">
                <div style="width:36px; height:36px; border-radius:10px; background:linear-gradient(135deg, #6366F1, #8B5CF6); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-size:17px;">
                    <i class="fa-solid fa-wand-magic-sparkles"></i>
                </div>
                <div>
                    <h3 class="font-outfit" style="font-size:16px; font-weight:800; color:#FFFFFF; margin:0;">Format Prompt AI &amp; Impor JSON Otomatis</h3>
                    <div style="font-size:11px; color:#94A3B8;">Isi otomatis seluruh 16 langkah PRD menggunakan ChatGPT, Claude, atau Gemini</div>
                </div>
            </div>
            <button type="button" onclick="closeModal('modal-ai-json')" style="background:transparent; border:none; color:#94A3B8; font-size:20px; cursor:pointer;">&times;</button>
        </div>
        <div class="modal-body" style="overflow-y:auto; flex:1; padding:16px 20px;">
            <!-- Step Scope Selector -->
            <div style="background:rgba(99,102,241,0.08); border:1px solid rgba(99,102,241,0.3); border-radius:10px; padding:10px 14px; margin-bottom:14px; display:flex; align-items:center; justify-content:space-between; gap:12px;">
                <div style="display:flex; align-items:center; gap:8px;">
                    <i class="fa-solid fa-sliders" style="color:#818CF8; font-size:14px;"></i>
                    <span style="font-size:12px; font-weight:700; color:#FFFFFF;">Pilih Target Pengisian:</span>
                </div>
                <div style="display:flex; align-items:center; gap:8px;">
                    <select id="ai-step-scope-select" class="form-control font-outfit" style="font-size:12px; padding:6px 12px; border-radius:6px; background:#080C14; border-color:#334155; color:#F8FAFC; width:auto; font-weight:600;" onchange="handleAiScopeChange()">
                        <option value="all">🌟 Semua 16 Langkah Sekaligus (Komprehensif)</option>
                        <option value="step1">1. Project Definition (Nama, Problem, Scope)</option>
                        <option value="step3">3. Roles &amp; Stakeholder Personas</option>
                        <option value="step4">4. Modules &amp; Functional Features</option>
                        <option value="step5">5. Business Process &amp; Workflow Steps</option>
                        <option value="step6">6. Business Rules &amp; Constraints</option>
                        <option value="step7">7. Data Entities (Entity Schema &amp; Fields)</option>
                        <option value="step8">8. Permissions / RBAC Matrix</option>
                        <option value="step9">9. KPI &amp; Operational Metrics</option>
                        <option value="step10">10. Notifications &amp; Alert Templates</option>
                        <option value="step11">11. Integrations (API &amp; Webhooks)</option>
                        <option value="step13">13. Screen Architecture &amp; UI Layout</option>
                    </select>
                </div>
            </div>

            <!-- Tabs Navigation -->
            <div style="display:flex; border-bottom:1px solid #1E293B; margin-bottom:16px; gap:8px;">
                <button type="button" class="btn btn-secondary btn-sm" id="tab-ai-prompt-btn" onclick="switchAiModalTab('prompt')" style="border-bottom-left-radius:0; border-bottom-right-radius:0; border-bottom:2px solid #6366F1; color:#FFFFFF; font-weight:700;">
                    <i class="fa-solid fa-copy" style="margin-right:6px; color:#818CF8;"></i>1. Salin Format Prompt ke AI
                </button>
                <button type="button" class="btn btn-secondary btn-sm" id="tab-ai-import-btn" onclick="switchAiModalTab('import')" style="border-bottom-left-radius:0; border-bottom-right-radius:0; border-bottom:2px solid transparent;">
                    <i class="fa-solid fa-file-import" style="margin-right:6px; color:#34D399;"></i>2. Tempel / Upload JSON dari AI
                </button>
            </div>

            <!-- Tab 1: Format Prompt untuk AI -->
            <div id="ai-tab-prompt-panel">
                <div style="background:#07090E; border:1px solid #1E293B; border-radius:10px; padding:12px 16px; margin-bottom:14px;">
                    <label class="form-label" style="font-size:11.5px; margin-bottom:6px;">
                        <span>Topik / Judul Aplikasi Anda:</span>
                    </label>
                    <div style="display:flex; gap:8px;">
                        <input type="text" id="ai-concept-input" class="form-control" placeholder="Contoh: Sistem Manajemen Gudang Spareparts &amp; Logistik Alat Berat" oninput="updateAiPromptWithConcept()">
                        <button type="button" class="btn btn-emerald" onclick="copyAiGeneratorPrompt()">
                            <i class="fa-solid fa-copy"></i>
                            <span>Salin Prompt</span>
                        </button>
                    </div>
                </div>

                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                    <span style="font-size:11px; font-weight:700; color:#94A3B8; text-transform:uppercase;" id="ai-prompt-title-badge">Isi Prompt Siap Kirim ke ChatGPT / Gemini / Claude:</span>
                    <button type="button" class="btn btn-secondary btn-sm" onclick="downloadEmptyJsonTemplate()" style="padding:2px 8px; font-size:11px;">
                        <i class="fa-solid fa-download"></i> Unduh File Template JSON
                    </button>
                </div>

                <textarea id="ai-prompt-display" class="form-control font-mono" rows="11" readonly style="font-size:11px; background:#05070B; line-height:1.5; color:#A5B4FC;"></textarea>

                <div style="margin-top:14px; background:rgba(99,102,241,0.06); border:1px solid rgba(99,102,241,0.2); border-radius:10px; padding:12px 14px; font-size:11.5px; color:#CBD5E1; line-height:1.6;">
                    <strong style="color:#FFFFFF;"><i class="fa-solid fa-circle-info" style="color:#818CF8; margin-right:6px;"></i>Langkah Penggunaan Ringan &amp; Cepat:</strong>
                    <ol style="margin-left:18px; margin-top:4px;">
                        <li>Pilih <strong>Target Pengisian</strong> di atas (Bisa per step seperti Role, Fitur, Workflow, atau Semua Sekaligus).</li>
                        <li>Klik <strong>"Salin Prompt"</strong> lalu tempel di <a href="https://chatgpt.com" target="_blank" style="color:#60A5FA; text-decoration:underline;">ChatGPT</a>, Gemini, atau Claude. AI akan merespon dengan cepat karena formatnya sangat ringkas.</li>
                        <li>Salin JSON yang dihasilkan AI, lalu klik tab <strong>"2. Tempel / Upload JSON dari AI"</strong> untuk langsung memperbarui step terkait tanpa menghapus data lainnya!</li>
                    </ol>
                </div>
            </div>

            <!-- Tab 2: Impor / Tempel JSON -->
            <div id="ai-tab-import-panel" style="display:none;">
                <div class="form-group">
                    <label class="form-label" style="display:flex; justify-content:space-between;">
                        <span>Tempel Kode JSON dari AI:</span>
                        <span id="ai-import-scope-indicator" class="badge badge-indigo" style="font-size:10px;">Target: Otomatis Terdeteksi</span>
                    </label>
                    <textarea id="ai-paste-json-box" class="form-control font-mono" rows="10" placeholder="Tempel kode JSON hasil generate AI di sini..."></textarea>
                </div>

                <div style="display:flex; align-items:center; gap:12px; margin-bottom:14px;">
                    <div style="flex:1; height:1px; background:#1E293B;"></div>
                    <span style="font-size:11px; color:#64748B; font-weight:700;">ATAU UNGGAH FILE</span>
                    <div style="flex:1; height:1px; background:#1E293B;"></div>
                </div>

                <div class="form-group">
                    <label class="btn btn-secondary" style="width:100%; justify-content:center; cursor:pointer; padding:10px;">
                        <i class="fa-solid fa-cloud-arrow-up" style="font-size:16px; color:#818CF8; margin-right:8px;"></i>
                        <span id="ai-file-label">Pilih File .json Dari Komputer</span>
                        <input type="file" id="ai-json-file-input" accept=".json" style="display:none;" onchange="handleAiJsonFileSelected(event)">
                    </label>
                </div>

                <div style="display:flex; justify-content:flex-end; margin-top:16px;">
                    <button type="button" class="btn btn-emerald" onclick="processAiJsonImport()" style="padding:10px 20px; font-weight:800; font-size:13px; box-shadow:0 0 16px rgba(16,185,129,0.35);">
                        <i class="fa-solid fa-wand-magic-sparkles"></i>
                        <span id="btn-process-import-label">Proses &amp; Terapkan Data JSON</span>
                    </button>
                </div>
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" onclick="closeModal('modal-ai-json')">Tutup</button>
        </div>
    </div>
</div>

<!-- MODAL PENGATURAN AI (CHATGPT COMPATIBLE) -->
<div class="modal-backdrop" id="modal-ai-settings">
    <div class="modal-box" style="max-width:580px;">
        <div class="modal-header">
            <div style="display:flex; align-items:center; gap:10px;">
                <div style="width:38px; height:38px; border-radius:10px; background:linear-gradient(135deg, #0284C7, #38BDF8); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-size:17px; box-shadow:0 0 12px rgba(56,189,248,0.35);">
                    <i class="fa-solid fa-robot"></i>
                </div>
                <div>
                    <h3 class="font-outfit" style="font-size:16px; font-weight:800; color:#FFFFFF; margin:0;">Pengaturan AI Engine</h3>
                    <div style="font-size:11px; color:#94A3B8;">OpenAI / ChatGPT Compatible Endpoint &bull; Direct AI Builder</div>
                </div>
            </div>
            <button type="button" onclick="closeModal('modal-ai-settings')" style="background:transparent; border:none; color:#94A3B8; font-size:20px; cursor:pointer;" title="Tutup Dialog">&times;</button>
        </div>
        <div class="modal-body" style="padding:18px 20px;">
            <!-- Live Proxy & Environment Status Banner -->
            <div id="ai-proxy-status-banner" style="background:rgba(56,189,248,0.06); border:1px solid rgba(56,189,248,0.2); border-radius:10px; padding:10px 14px; margin-bottom:14px; font-size:11.5px; color:#BAE6FD; line-height:1.5;">
                <div style="display:flex; align-items:center; gap:8px;">
                    <i class="fa-solid fa-circle-notch fa-spin" style="color:#38BDF8;"></i>
                    <span>Memeriksa status Local AI Proxy (Apache XAMPP)...</span>
                </div>
            </div>

            <!-- Quick Provider Presets -->
            <div style="margin-bottom:14px;">
                <label style="font-size:11px; font-weight:700; color:#94A3B8; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:6px; display:block;">
                    Pilih Cepat Template Provider:
                </label>
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(100px, 1fr)); gap:6px;">
                    <button type="button" class="ai-preset-btn" data-preset="siaptuan" onclick="setAiPreset('siaptuan')" style="background:#0F172A; border:1px solid #334155; border-radius:8px; padding:6px 8px; font-size:11px; color:#E2E8F0; cursor:pointer; font-weight:600; text-align:center; transition:all 0.15s ease;">
                        <i class="fa-solid fa-bolt" style="color:#38BDF8; margin-right:4px;"></i>SiapTuan
                    </button>
                    <button type="button" class="ai-preset-btn" data-preset="openai" onclick="setAiPreset('openai')" style="background:#0F172A; border:1px solid #334155; border-radius:8px; padding:6px 8px; font-size:11px; color:#E2E8F0; cursor:pointer; font-weight:600; text-align:center; transition:all 0.15s ease;">
                        <i class="fa-solid fa-brain" style="color:#10B981; margin-right:4px;"></i>OpenAI
                    </button>
                    <button type="button" class="ai-preset-btn" data-preset="groq" onclick="setAiPreset('groq')" style="background:#0F172A; border:1px solid #334155; border-radius:8px; padding:6px 8px; font-size:11px; color:#E2E8F0; cursor:pointer; font-weight:600; text-align:center; transition:all 0.15s ease;">
                        <i class="fa-solid fa-gauge-high" style="color:#F59E0B; margin-right:4px;"></i>Groq
                    </button>
                    <button type="button" class="ai-preset-btn" data-preset="openrouter" onclick="setAiPreset('openrouter')" style="background:#0F172A; border:1px solid #334155; border-radius:8px; padding:6px 8px; font-size:11px; color:#E2E8F0; cursor:pointer; font-weight:600; text-align:center; transition:all 0.15s ease;">
                        <i class="fa-solid fa-network-wired" style="color:#818CF8; margin-right:4px;"></i>OpenRouter
                    </button>
                    <button type="button" class="ai-preset-btn" data-preset="ollama" onclick="setAiPreset('ollama')" style="background:#0F172A; border:1px solid #334155; border-radius:8px; padding:6px 8px; font-size:11px; color:#E2E8F0; cursor:pointer; font-weight:600; text-align:center; transition:all 0.15s ease;">
                        <i class="fa-solid fa-laptop-code" style="color:#EC4899; margin-right:4px;"></i>Ollama
                    </button>
                </div>
            </div>

            <div class="form-group" style="margin-bottom:14px;">
                <label class="form-label" style="font-size:12px; font-weight:700; color:#F8FAFC; margin-bottom:6px; display:flex; justify-content:space-between;">
                    <span>Base URL</span>
                    <span style="font-size:10.5px; color:#64748B;">Otomatis dinormalisasi ke /chat/completions</span>
                </label>
                <input type="text" id="ai-settings-base-url" class="form-control font-mono" placeholder="https://siaptuan.my.id/v1" style="background:#07090E; border-color:#1E293B; color:#38BDF8; font-size:12.5px; padding:10px 14px; border-radius:8px;">
                <div style="font-size:10.5px; color:#64748B; margin-top:4px;">Contoh: <code>https://siaptuan.my.id/v1</code> atau <code>https://api.openai.com/v1</code></div>
            </div>

            <div class="form-group" style="margin-bottom:14px;">
                <label class="form-label" style="font-size:12px; font-weight:700; color:#F8FAFC; margin-bottom:6px;">
                    <span>Model Name</span>
                </label>
                <input type="text" id="ai-settings-model" class="form-control font-mono" placeholder="gpt-5.6-luna.st" style="background:#07090E; border-color:#1E293B; color:#34D399; font-size:12.5px; padding:10px 14px; border-radius:8px;">
                <div style="font-size:10.5px; color:#64748B; margin-top:4px;">Model ID: <code>gpt-5.6-luna.st</code>, <code>gpt-4o-mini</code>, <code>llama-3.3-70b-versatile</code>, dsb.</div>
            </div>

            <div class="form-group" style="margin-bottom:14px;">
                <label class="form-label" style="font-size:12px; font-weight:700; color:#F8FAFC; margin-bottom:6px; display:flex; justify-content:space-between; align-items:center;">
                    <span>API Key / Bearer Token</span>
                    <span id="ai-key-status" class="badge badge-slate" style="font-size:10px;">Lokal Browser</span>
                </label>
                <div style="position:relative; display:flex; align-items:center;">
                    <input type="password" id="ai-settings-key" class="form-control font-mono" placeholder="sk-..." style="background:#07090E; border-color:#1E293B; color:#F8FAFC; font-size:12.5px; padding:10px 42px 10px 14px; border-radius:8px;">
                    <button type="button" onclick="toggleAiApiKeyVisibility()" style="position:absolute; right:12px; background:transparent; border:none; color:#94A3B8; cursor:pointer; font-size:14px;" title="Lihat/Sembunyikan API Key">
                        <i class="fa-solid fa-eye" id="ai-key-toggle-icon"></i>
                    </button>
                </div>
                <div style="font-size:10.5px; color:#64748B; margin-top:4px;">Disimpan aman secara terenkripsi di localStorage browser lokal perangkat Anda.</div>
            </div>
        </div>
        <div class="modal-footer" style="display:flex; justify-content:space-between; align-items:center;">
            <button type="button" class="btn btn-secondary btn-sm" onclick="testAiConnection()" id="btn-test-ai-conn">
                <i class="fa-solid fa-plug-circle-check" style="color:#38BDF8;"></i>
                <span>Uji Koneksi AI</span>
            </button>
            <div style="display:flex; gap:8px;">
                <button type="button" class="btn btn-secondary" onclick="closeModal('modal-ai-settings')">Batal</button>
                <button type="button" class="btn btn-primary" onclick="saveAiSettings()" style="background:linear-gradient(135deg, #0284C7, #2563EB); border-color:#1D4ED8; font-weight:700;">
                    <i class="fa-solid fa-floppy-disk"></i>
                    <span>Simpan Pengaturan</span>
                </button>
            </div>
        </div>
    </div>
</div>

<!-- Role Modal -->
<div class="modal-backdrop" id="modal-role">
    <div class="modal-box">
        <div class="modal-header">
            <h3 class="font-outfit" style="font-size:16px; font-weight:800; color:#FFFFFF;" id="modal-role-title">Tambah Role Baru</h3>
            <button type="button" onclick="closeModal('modal-role')" style="background:transparent; border:none; color:#94A3B8; font-size:18px; cursor:pointer;">&times;</button>
        </div>
        <div class="modal-body">
            <input type="hidden" id="modal-role-id">
            <div class="form-group">
                <label class="form-label">Nama Role / Jabatan <span style="color:#F43F5E;">*</span></label>
                <input type="text" id="m-role-name" class="form-control" placeholder="Contoh: Maintenance Planner, Supervisor, Mekanik">
            </div>
            <div class="grid-2">
                <div class="form-group">
                    <label class="form-label">Departemen</label>
                    <input type="text" id="m-role-dept" class="form-control" placeholder="Contoh: Plant Maintenance">
                </div>
                <div class="form-group">
                    <label class="form-label">Tipe Pengguna</label>
                    <select id="m-role-type" class="form-control">
                        <option value="primary">Primary User (Pengguna Kunci)</option>
                        <option value="secondary">Secondary User (Pengguna Pendukung / Approver)</option>
                    </select>
                </div>
            </div>
            <div class="form-group">
                <label class="form-label">Tanggung Jawab Utama (Responsibility)</label>
                <textarea id="m-role-resp" class="form-control" rows="2" placeholder="Tugas utama dalam sistem..."></textarea>
            </div>
            <div class="form-group">
                <label class="form-label">Persona &bull; Kebutuhan Operasional</label>
                <textarea id="m-role-persona" class="form-control" rows="2" placeholder="Pain points dan kebutuhan khusus role ini..."></textarea>
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" onclick="closeModal('modal-role')">Batal</button>
            <button type="button" class="btn btn-primary" onclick="saveRoleModal()">Simpan Role</button>
        </div>
    </div>
</div>

<!-- Module Modal -->
<div class="modal-backdrop" id="modal-module">
    <div class="modal-box">
        <div class="modal-header">
            <h3 class="font-outfit" style="font-size:16px; font-weight:800; color:#FFFFFF;" id="modal-module-title">Tambah Modul Baru</h3>
            <button type="button" onclick="closeModal('modal-module')" style="background:transparent; border:none; color:#94A3B8; font-size:18px; cursor:pointer;">&times;</button>
        </div>
        <div class="modal-body">
            <input type="hidden" id="modal-module-id">
            <div class="form-group">
                <label class="form-label">Nama Modul <span style="color:#F43F5E;">*</span></label>
                <input type="text" id="m-mod-name" class="form-control" placeholder="Contoh: Work Order Management, Preventive Maintenance">
            </div>
            <div class="form-group">
                <label class="form-label">Deskripsi Modul</label>
                <textarea id="m-mod-desc" class="form-control" rows="2" placeholder="Tujuan modul dan fungsi bisnis utamanya..."></textarea>
            </div>
            <div class="form-group">
                <label class="form-label">Submodul (Pisahkan dengan koma jika lebih dari satu)</label>
                <input type="text" id="m-mod-sub" class="form-control" placeholder="Contoh: WO Creation, Planning Board, Execution &amp; Close">
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" onclick="closeModal('modal-module')">Batal</button>
            <button type="button" class="btn btn-primary" onclick="saveModuleModal()">Simpan Modul</button>
        </div>
    </div>
</div>

<!-- Feature Modal -->
<div class="modal-backdrop" id="modal-feature">
    <div class="modal-box">
        <div class="modal-header">
            <h3 class="font-outfit" style="font-size:16px; font-weight:800; color:#FFFFFF;" id="modal-feat-title">Tambah Fitur Baru</h3>
            <button type="button" onclick="closeModal('modal-feature')" style="background:transparent; border:none; color:#94A3B8; font-size:18px; cursor:pointer;">&times;</button>
        </div>
        <div class="modal-body">
            <input type="hidden" id="modal-feat-id">
            <div class="form-group">
                <label class="form-label">Modul Induk <span style="color:#F43F5E;">*</span></label>
                <select id="m-feat-mod" class="form-control"></select>
            </div>
            <div class="form-group">
                <label class="form-label">Nama Fitur <span style="color:#F43F5E;">*</span></label>
                <input type="text" id="m-feat-name" class="form-control" placeholder="Contoh: Filter &amp; Search Work Order by Status">
            </div>
            <div class="grid-2">
                <div class="form-group">
                    <label class="form-label">Prioritas Fitur</label>
                    <select id="m-feat-priority" class="form-control">
                        <option value="P0">P0 &bull; Critical (Wajib MVP)</option>
                        <option value="P1">P1 &bull; High Priority</option>
                        <option value="P2">P2 &bull; Medium Priority</option>
                        <option value="P3">P3 &bull; Nice to Have</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="form-label">Pengguna Utama (Primary Role)</label>
                    <select id="m-feat-user" class="form-control"></select>
                </div>
            </div>
            <div class="form-group">
                <label class="form-label">Deskripsi Fitur &amp; Perilaku</label>
                <textarea id="m-feat-desc" class="form-control" rows="2" placeholder="Bagaimana fitur ini bekerja dan interaksi apa yang terjadi..."></textarea>
            </div>
            <div class="grid-2">
                <div class="form-group">
                    <label class="form-label">Dependencies (Ketergantungan)</label>
                    <input type="text" id="m-feat-dep" class="form-control" placeholder="Contoh: Equipment Master, Spare Part Stock">
                </div>
                <div class="form-group">
                    <label class="form-label">Expected Outcome</label>
                    <input type="text" id="m-feat-outcome" class="form-control" placeholder="Contoh: Tabel terfilter instan <100ms">
                </div>
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" onclick="closeModal('modal-feature')">Batal</button>
            <button type="button" class="btn btn-primary" onclick="saveFeatureModal()">Simpan Fitur</button>
        </div>
    </div>
</div>

<!-- Workflow Step Modal -->
<div class="modal-backdrop" id="modal-workflow">
    <div class="modal-box">
        <div class="modal-header">
            <h3 class="font-outfit" style="font-size:16px; font-weight:800; color:#FFFFFF;" id="modal-wf-title">Tambah Tahap Alur Kerja</h3>
            <button type="button" onclick="closeModal('modal-workflow')" style="background:transparent; border:none; color:#94A3B8; font-size:18px; cursor:pointer;">&times;</button>
        </div>
        <div class="modal-body">
            <input type="hidden" id="modal-wf-id">
            <div class="form-group">
                <label class="form-label">Nama Tahap / Langkah <span style="color:#F43F5E;">*</span></label>
                <input type="text" id="m-wf-name" class="form-control" placeholder="Contoh: Work Request, Planning, Approval, Execution">
            </div>
            <div class="grid-2">
                <div class="form-group">
                    <label class="form-label">Aktor (Pelaksana Tahap)</label>
                    <select id="m-wf-actor" class="form-control"></select>
                </div>
                <div class="form-group">
                    <label class="form-label">Status State Hasil</label>
                    <input type="text" id="m-wf-status" class="form-control" placeholder="Contoh: SUBMITTED, PLANNED, APPROVED, CLOSED">
                </div>
            </div>
            <div class="grid-2">
                <div class="form-group">
                    <label class="form-label">Pemicu (Trigger)</label>
                    <input type="text" id="m-wf-trigger" class="form-control" placeholder="Contoh: Kerusakan unit dilaporkan operator">
                </div>
                <div class="form-group">
                    <label class="form-label">Input Diperlukan</label>
                    <input type="text" id="m-wf-input" class="form-control" placeholder="Contoh: No Unit, Gejala, Foto Kerusakan">
                </div>
            </div>
            <div class="form-group">
                <label class="form-label">Tindakan / Aktivitas (Action)</label>
                <textarea id="m-wf-action" class="form-control" rows="2" placeholder="Apa yang dilakukan user pada tahap ini..."></textarea>
            </div>
            <div class="grid-2">
                <div class="form-group">
                    <label class="form-label">Decision / Approval Gate</label>
                    <input type="text" id="m-wf-decision" class="form-control" placeholder="Contoh: Disetujui Supervisor atau Direvisi">
                </div>
                <div class="form-group">
                    <label class="form-label">Output Tahap</label>
                    <input type="text" id="m-wf-output" class="form-control" placeholder="Contoh: Nomor WO resmi terbit">
                </div>
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" onclick="closeModal('modal-workflow')">Batal</button>
            <button type="button" class="btn btn-primary" onclick="saveWorkflowModal()">Simpan Tahap</button>
        </div>
    </div>
</div>

<!-- Business Rule Modal -->
<div class="modal-backdrop" id="modal-rule">
    <div class="modal-box">
        <div class="modal-header">
            <h3 class="font-outfit" style="font-size:16px; font-weight:800; color:#FFFFFF;" id="modal-rule-title">Tambah Business Rule</h3>
            <button type="button" onclick="closeModal('modal-rule')" style="background:transparent; border:none; color:#94A3B8; font-size:18px; cursor:pointer;">&times;</button>
        </div>
        <div class="modal-body">
            <input type="hidden" id="modal-rule-id">
            <div class="form-group">
                <label class="form-label">Nama Aturan (Rule Name) <span style="color:#F43F5E;">*</span></label>
                <input type="text" id="m-rule-name" class="form-control" placeholder="Contoh: WO cannot be released without assigned manpower">
            </div>
            <div class="grid-2">
                <div class="form-group">
                    <label class="form-label">Tingkat Keparahan (Severity)</label>
                    <select id="m-rule-severity" class="form-control">
                        <option value="Blocking">Blocking (Mencegah Aksi / Error)</option>
                        <option value="Warning">Warning (Peringatan / Konfirmasi)</option>
                        <option value="Informational">Informational (Pemberitahuan)</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="form-label">Pengecualian (Exception)</label>
                    <input type="text" id="m-rule-exception" class="form-control" placeholder="Contoh: Override darurat oleh Plant Manager">
                </div>
            </div>
            <div class="form-group">
                <label class="form-label">Kondisi (Condition) <span style="color:#F43F5E;">*</span></label>
                <textarea id="m-rule-condition" class="form-control" rows="2" placeholder="Contoh: Assigned Manpower == 0 OR Assigned Mechanics is Empty"></textarea>
            </div>
            <div class="form-group">
                <label class="form-label">Aksi yang Dijalankan (Action) <span style="color:#F43F5E;">*</span></label>
                <textarea id="m-rule-action" class="form-control" rows="2" placeholder="Contoh: Kunci tombol Rilis, tampilkan pesan validasi merah"></textarea>
            </div>
            <div class="form-group">
                <label class="form-label">Deskripsi &amp; Rasional</label>
                <textarea id="m-rule-desc" class="form-control" rows="2" placeholder="Mengapa aturan ini penting bagi operasional..."></textarea>
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" onclick="closeModal('modal-rule')">Batal</button>
            <button type="button" class="btn btn-primary" onclick="saveRuleModal()">Simpan Rule</button>
        </div>
    </div>
</div>

<!-- Entity Modal -->
<div class="modal-backdrop" id="modal-entity">
    <div class="modal-box">
        <div class="modal-header">
            <h3 class="font-outfit" style="font-size:16px; font-weight:800; color:#FFFFFF;" id="modal-entity-title">Tambah Entitas Data</h3>
            <button type="button" onclick="closeModal('modal-entity')" style="background:transparent; border:none; color:#94A3B8; font-size:18px; cursor:pointer;">&times;</button>
        </div>
        <div class="modal-body">
            <input type="hidden" id="modal-entity-id">
            <div class="form-group">
                <label class="form-label">Nama Entitas <span style="color:#F43F5E;">*</span></label>
                <input type="text" id="m-ent-name" class="form-control" placeholder="Contoh: WorkOrder, Equipment, SparePart">
            </div>
            <div class="grid-2">
                <div class="form-group">
                    <label class="form-label">Tipe Entitas</label>
                    <select id="m-ent-type" class="form-control">
                        <option value="Transactional">Transactional (Data Dinamis Berulang)</option>
                        <option value="Master">Master Data (Data Induk Referensi)</option>
                        <option value="Config / Lookup">Config / Lookup (Tabel Kamus)</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="form-label">Tabel / Penyimpanan MVP</label>
                    <input type="text" id="m-ent-storage" class="form-control" placeholder="Contoh: tbl_work_orders (localStorage)">
                </div>
            </div>
            <div class="form-group">
                <label class="form-label">Deskripsi Entitas</label>
                <textarea id="m-ent-desc" class="form-control" rows="2" placeholder="Deskripsi entitas data ini..."></textarea>
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" onclick="closeModal('modal-entity')">Batal</button>
            <button type="button" class="btn btn-primary" onclick="saveEntityModal()">Simpan Entitas</button>
        </div>
    </div>
</div>

<!-- Field Modal -->
<div class="modal-backdrop" id="modal-field">
    <div class="modal-box">
        <div class="modal-header">
            <h3 class="font-outfit" style="font-size:16px; font-weight:800; color:#FFFFFF;">Tambah Field ke Entitas</h3>
            <button type="button" onclick="closeModal('modal-field')" style="background:transparent; border:none; color:#94A3B8; font-size:18px; cursor:pointer;">&times;</button>
        </div>
        <div class="modal-body">
            <input type="hidden" id="modal-field-entity-id">
            <div class="form-group">
                <label class="form-label">Nama Field <span style="color:#F43F5E;">*</span></label>
                <input type="text" id="m-fld-name" class="form-control" placeholder="Contoh: wo_number, equipment_id, status">
            </div>
            <div class="grid-2">
                <div class="form-group">
                    <label class="form-label">Tipe Data</label>
                    <select id="m-fld-type" class="form-control">
                        <option value="String">String (Teks Pendek)</option>
                        <option value="Text">Text (Teks Panjang)</option>
                        <option value="Integer">Integer (Bilangan Bulat)</option>
                        <option value="Decimal">Decimal (Angka Desimal)</option>
                        <option value="Boolean">Boolean (True / False)</option>
                        <option value="Date">Date (Tanggal)</option>
                        <option value="DateTime">DateTime (Tanggal &amp; Waktu)</option>
                        <option value="Enum">Enum (Pilihan Terbatas)</option>
                        <option value="JSON">JSON / Array</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="form-label">Sifat Field</label>
                    <select id="m-fld-req" class="form-control">
                        <option value="true">Wajib Diisi (Required)</option>
                        <option value="false">Opsional (Nullable)</option>
                    </select>
                </div>
            </div>
            <div class="grid-2">
                <div class="form-group">
                    <label class="form-label">Nilai Default</label>
                    <input type="text" id="m-fld-default" class="form-control" placeholder="Contoh: 'OPEN', 0, CURRENT_TIMESTAMP">
                </div>
                <div class="form-group">
                    <label class="form-label">Aturan Validasi</label>
                    <input type="text" id="m-fld-valid" class="form-control" placeholder="Contoh: Unique, Min:3, Regex:^WO-[0-9]{5}$">
                </div>
            </div>
            <div class="form-group">
                <label class="form-label">Deskripsi Field</label>
                <input type="text" id="m-fld-desc" class="form-control" placeholder="Deskripsi field ini...">
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" onclick="closeModal('modal-field')">Batal</button>
            <button type="button" class="btn btn-primary" onclick="saveFieldModal()">Tambahkan Field</button>
        </div>
    </div>
</div>

<!-- KPI Modal -->
<div class="modal-backdrop" id="modal-kpi">
    <div class="modal-box">
        <div class="modal-header">
            <h3 class="font-outfit" style="font-size:16px; font-weight:800; color:#FFFFFF;" id="modal-kpi-title">Tambah Metrik KPI</h3>
            <button type="button" onclick="closeModal('modal-kpi')" style="background:transparent; border:none; color:#94A3B8; font-size:18px; cursor:pointer;">&times;</button>
        </div>
        <div class="modal-body">
            <input type="hidden" id="modal-kpi-id">
            <div class="form-group">
                <label class="form-label">Nama KPI <span style="color:#F43F5E;">*</span></label>
                <input type="text" id="m-kpi-name" class="form-control" placeholder="Contoh: Mean Time To Repair (MTTR), PM Compliance %">
            </div>
            <div class="grid-2">
                <div class="form-group">
                    <label class="form-label">Target Nilai</label>
                    <input type="text" id="m-kpi-target" class="form-control" placeholder="Contoh: &lt; 2.5, &gt;= 90%">
                </div>
                <div class="form-group">
                    <label class="form-label">Satuan (Unit)</label>
                    <input type="text" id="m-kpi-unit" class="form-control" placeholder="Contoh: Jam, %, Hari, BCM">
                </div>
            </div>
            <div class="form-group">
                <label class="form-label">Formula Perhitungan</label>
                <input type="text" id="m-kpi-formula" class="form-control" placeholder="Contoh: (Total Downtime Jam / Jumlah Breakdown Kerusakan)">
            </div>
            <div class="grid-3">
                <div class="form-group">
                    <label class="form-label">Sumber Data</label>
                    <input type="text" id="m-kpi-source" class="form-control" placeholder="Contoh: WorkOrder Table">
                </div>
                <div class="form-group">
                    <label class="form-label">Frekuensi Evaluasi</label>
                    <select id="m-kpi-freq" class="form-control">
                        <option value="Shift">Per Shift</option>
                        <option value="Harian">Harian (Daily)</option>
                        <option value="Mingguan">Mingguan (Weekly)</option>
                        <option value="Bulanan">Bulanan (Monthly)</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="form-label">Tipe Visualisasi</label>
                    <select id="m-kpi-vis" class="form-control">
                        <option value="Stat Card">Stat Card / Ringkasan</option>
                        <option value="Bar Chart">Bar Chart (Batang)</option>
                        <option value="Line Trend">Line Chart (Tren)</option>
                        <option value="Donut Chart">Donut Chart</option>
                        <option value="Gauge Meter">Gauge Meter</option>
                    </select>
                </div>
            </div>
            <div class="form-group">
                <label class="form-label">Deskripsi &amp; Rasional</label>
                <textarea id="m-kpi-desc" class="form-control" rows="2" placeholder="Mengukur efisiensi sistem..."></textarea>
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" onclick="closeModal('modal-kpi')">Batal</button>
            <button type="button" class="btn btn-primary" onclick="saveKpiModal()">Simpan KPI</button>
        </div>
    </div>
</div>

<!-- Notification Modal -->
<div class="modal-backdrop" id="modal-notification">
    <div class="modal-box">
        <div class="modal-header">
            <h3 class="font-outfit" style="font-size:16px; font-weight:800; color:#FFFFFF;" id="modal-notif-title">Tambah Notifikasi &amp; Alert</h3>
            <button type="button" onclick="closeModal('modal-notification')" style="background:transparent; border:none; color:#94A3B8; font-size:18px; cursor:pointer;">&times;</button>
        </div>
        <div class="modal-body">
            <input type="hidden" id="modal-notif-id">
            <div class="form-group">
                <label class="form-label">Nama Event Pemicu <span style="color:#F43F5E;">*</span></label>
                <input type="text" id="m-notif-name" class="form-control" placeholder="Contoh: Critical Breakdown P0 Logged, PM Overdue > 48 Jam">
            </div>
            <div class="grid-2">
                <div class="form-group">
                    <label class="form-label">Penerima (Recipient Role)</label>
                    <select id="m-notif-recipient" class="form-control"></select>
                </div>
                <div class="form-group">
                    <label class="form-label">Channel Pengiriman</label>
                    <select id="m-notif-channel" class="form-control">
                        <option value="In-App Toast">In-App Banner / Toast</option>
                        <option value="Email">Email Notification</option>
                        <option value="SMS / WhatsApp">WhatsApp / SMS Gateway</option>
                        <option value="Push Notification">Browser Push Notification</option>
                    </select>
                </div>
            </div>
            <div class="grid-2">
                <div class="form-group">
                    <label class="form-label">Tingkat Prioritas</label>
                    <select id="m-notif-priority" class="form-control">
                        <option value="P1 Critical">P1 Critical (Segera)</option>
                        <option value="P2 High">P2 High Priority</option>
                        <option value="P3 Normal">P3 Normal</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="form-label">Aturan Eskalasi</label>
                    <input type="text" id="m-notif-escala" class="form-control" placeholder="Contoh: Jika tak direspon 30 menit, teruskan ke Manager">
                </div>
            </div>
            <div class="form-group">
                <label class="form-label">Template Pesan</label>
                <textarea id="m-notif-msg" class="form-control" rows="2" placeholder="Contoh: [PERINGATAN] Terjadi event kritis pada sistem..."></textarea>
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" onclick="closeModal('modal-notification')">Batal</button>
            <button type="button" class="btn btn-primary" onclick="saveNotificationModal()">Simpan Notifikasi</button>
        </div>
    </div>
</div>

<!-- Integration Modal -->
<div class="modal-backdrop" id="modal-integration">
    <div class="modal-box">
        <div class="modal-header">
            <h3 class="font-outfit" style="font-size:16px; font-weight:800; color:#FFFFFF;" id="modal-integ-title">Tambah Kebutuhan Integrasi</h3>
            <button type="button" onclick="closeModal('modal-integration')" style="background:transparent; border:none; color:#94A3B8; font-size:18px; cursor:pointer;">&times;</button>
        </div>
        <div class="modal-body">
            <input type="hidden" id="modal-integ-id">
            <div class="form-group">
                <label class="form-label">Nama Sistem Eksternal <span style="color:#F43F5E;">*</span></label>
                <input type="text" id="m-integ-system" class="form-control" placeholder="Contoh: SAP S/4HANA ERP, Active Directory SSO, REST API Gateway">
            </div>
            <div class="grid-2">
                <div class="form-group">
                    <label class="form-label">Arah Aliran Data (Direction)</label>
                    <select id="m-integ-dir" class="form-control">
                        <option value="Inbound">Inbound (Masuk ke Sistem Ini)</option>
                        <option value="Outbound">Outbound (Kirim ke Sistem Luar)</option>
                        <option value="Bi-directional">Bi-directional (Dua Arah / Sinkronisasi)</option>
                    </select>
                </div>
                <div class="form-group">
                    <label class="form-label">Frekuensi Pertukaran</label>
                    <select id="m-integ-freq" class="form-control">
                        <option value="Real-time Webhook">Real-time Webhook / REST</option>
                        <option value="Per Shift">Per Pergantian Shift</option>
                        <option value="Batch Harian">Batch Harian (Daily 00:00)</option>
                        <option value="Manual On-Demand">Manual On-Demand</option>
                    </select>
                </div>
            </div>
            <div class="form-group">
                <label class="form-label">Tujuan Integrasi (Purpose)</label>
                <input type="text" id="m-integ-purpose" class="form-control" placeholder="Tujuan menghubungkan sistem ini..."></textarea>
            </div>
            <div class="grid-2">
                <div class="form-group">
                    <label class="form-label">Objek Data / Payload</label>
                    <input type="text" id="m-integ-data" class="form-control" placeholder="Contoh: UserProfile, MaterialIssue, TransactionLog">
                </div>
                <div class="form-group">
                    <label class="form-label">Protokol / Autentikasi</label>
                    <input type="text" id="m-integ-auth" class="form-control" placeholder="Contoh: REST API Bearer OAuth 2.0 / API Key">
                </div>
            </div>
            <div class="form-group">
                <label class="form-label">Catatan Simulasi MVP (Offline Mock Behavior)</label>
                <textarea id="m-integ-mock" class="form-control" rows="2" placeholder="Bagaimana integrasi disimulasikan di MVP tanpa backend..."></textarea>
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" onclick="closeModal('modal-integration')">Batal</button>
            <button type="button" class="btn btn-primary" onclick="saveIntegrationModal()">Simpan Integrasi</button>
        </div>
    </div>
</div>

<!-- Screen Modal -->
<div class="modal-backdrop" id="modal-screen">
    <div class="modal-box">
        <div class="modal-header">
            <h3 class="font-outfit" style="font-size:16px; font-weight:800; color:#FFFFFF;" id="modal-screen-title">Tambah Screen / Halaman</h3>
            <button type="button" onclick="closeModal('modal-screen')" style="background:transparent; border:none; color:#94A3B8; font-size:18px; cursor:pointer;">&times;</button>
        </div>
        <div class="modal-body">
            <input type="hidden" id="modal-screen-id">
            <div class="form-group">
                <label class="form-label">Nama Screen / Tampilan <span style="color:#F43F5E;">*</span></label>
                <input type="text" id="m-screen-name" class="form-control" placeholder="Contoh: Dashboard Overview, Management Table, Detail Modal">
            </div>
            <div class="form-group">
                <label class="form-label">Fitur Terkait (Dipetakan dari Step 4)</label>
                <input type="text" id="m-screen-features" class="form-control" placeholder="Contoh: Filter Data, Create New Record, Status Transition">
            </div>
            <div class="form-group">
                <label class="form-label">Komponen Kunci pada Screen Ini</label>
                <textarea id="m-screen-components" class="form-control" rows="2" placeholder="Contoh: Stat Cards, Data Table dengan pagination, Modal Form..."></textarea>
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" onclick="closeModal('modal-screen')">Batal</button>
            <button type="button" class="btn btn-primary" onclick="saveScreenModal()">Simpan Screen</button>
        </div>
    </div>
</div>



"""
