# -*- coding: utf-8 -*-
"""
CSS generator for Enterprise PRD Studio.
Provides premium enterprise dark mode styles, custom forms, tables, modals, badges,
draft storage UI, and large 5-pillar architecture cards.
"""

def get_css():
    return """
        :root {
            --bg-base: #07090E;
            --surface-panel: #0D111A;
            --surface-card: #121826;
            --surface-card-hover: #182235;
            --surface-subtle: #0B0E17;
            --border-color: #1E293B;
            --border-glow: rgba(99, 102, 241, 0.4);
            --border-active: #6366F1;
            
            --text-primary: #F8FAFC;
            --text-secondary: #94A3B8;
            --text-muted: #64748B;
            
            --primary: #6366F1;
            --primary-hover: #4F46E5;
            --primary-glow: rgba(99, 102, 241, 0.25);
            
            --emerald: #10B981;
            --emerald-bg: rgba(16, 185, 129, 0.12);
            --emerald-border: rgba(16, 185, 129, 0.3);
            
            --amber: #F59E0B;
            --amber-bg: rgba(245, 158, 11, 0.12);
            --amber-border: rgba(245, 158, 11, 0.3);
            
            --rose: #F43F5E;
            --rose-bg: rgba(244, 63, 94, 0.12);
            --rose-border: rgba(244, 63, 94, 0.3);
            
            --cyan: #06B6D4;
            --cyan-bg: rgba(6, 182, 212, 0.12);
            --cyan-border: rgba(6, 182, 212, 0.3);
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }

        html, body {
            width: 100%;
            height: 100vh;
            background-color: var(--bg-base);
            color: var(--text-primary);
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            overflow: hidden;
            -webkit-font-smoothing: antialiased;
        }

        .font-outfit { font-family: 'Outfit', sans-serif; }
        .font-mono { font-family: 'JetBrains Mono', monospace; }

        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #1E293B; border-radius: 6px; }
        ::-webkit-scrollbar-thumb:hover { background: #334155; }

        /* App Shell Layout */
        .app-shell {
            display: flex;
            flex-direction: column;
            height: 100vh;
            width: 100vw;
            overflow: hidden;
        }

        /* Top Header */
        .top-header {
            height: 62px;
            background: var(--surface-panel);
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 20px;
            flex-shrink: 0;
            z-index: 30;
        }

        .brand-box {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .brand-logo {
            width: 38px;
            height: 38px;
            border-radius: 10px;
            background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #FFFFFF;
            font-size: 18px;
            box-shadow: 0 0 16px rgba(99, 102, 241, 0.45);
        }

        /* Workspace Grid */
        .workspace-shell {
            display: flex;
            flex: 1;
            height: calc(100vh - 62px);
            overflow: hidden;
        }

        /* Sidebar Navigation */
        .sidebar-stepper {
            width: 310px;
            background: var(--surface-panel);
            border-right: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            flex-shrink: 0;
            overflow-y: auto;
            overflow-x: hidden;
        }

        .step-nav-header {
            padding: 14px 18px;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(255,255,255,0.01);
        }

        .step-nav-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 11px 16px;
            margin: 2px 8px;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.2s ease;
            border: 1px solid transparent;
            position: relative;
        }
        .step-nav-item:hover {
            background: rgba(99, 102, 241, 0.08);
            border-color: rgba(99, 102, 241, 0.15);
        }
        .step-nav-item.active {
            background: rgba(99, 102, 241, 0.16);
            border-color: rgba(99, 102, 241, 0.4);
            box-shadow: 0 0 16px rgba(99, 102, 241, 0.18);
        }

        .step-num-badge {
            width: 26px;
            height: 26px;
            border-radius: 8px;
            background: #182235;
            border: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 11.5px;
            font-weight: 700;
            color: var(--text-secondary);
            flex-shrink: 0;
            transition: all 0.2s ease;
        }
        .step-nav-item.active .step-num-badge {
            background: var(--primary);
            color: #FFFFFF;
            border-color: var(--primary);
            box-shadow: 0 0 10px rgba(99, 102, 241, 0.5);
        }
        .step-num-badge.done {
            background: rgba(16, 185, 129, 0.2);
            color: #34D399;
            border-color: rgba(16, 185, 129, 0.4);
        }
        .step-num-badge.warn {
            background: rgba(245, 158, 11, 0.2);
            color: #FBBF24;
            border-color: rgba(245, 158, 11, 0.4);
        }

        /* Main Content View Container */
        .main-viewport {
            flex: 1;
            height: 100%;
            overflow-y: auto;
            padding: 24px 32px 60px;
            background: var(--bg-base);
        }

        .step-panel {
            display: none;
            max-width: 1200px;
            margin: 0 auto;
        }
        .step-panel.active {
            display: block;
            animation: fadeIn 0.25s ease-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Card Panels & Containers */
        .card-box {
            background: var(--surface-card);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 20px 24px;
            margin-bottom: 20px;
        }
        .card-box.highlight {
            border-color: rgba(99, 102, 241, 0.35);
            background: linear-gradient(180deg, rgba(18, 24, 38, 0.9) 0%, rgba(13, 17, 26, 0.95) 100%);
        }

        /* Form Controls */
        .form-group {
            display: flex;
            flex-direction: column;
            gap: 6px;
            margin-bottom: 16px;
        }
        .form-label {
            font-size: 12px;
            font-weight: 700;
            color: #E2E8F0;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .form-control {
            width: 100%;
            padding: 10px 14px;
            border-radius: 10px;
            background: var(--surface-subtle);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            font-size: 12.5px;
            font-family: inherit;
            outline: none;
            transition: border-color 0.2s, box-shadow 0.2s;
        }
        .form-control:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
        }
        textarea.form-control {
            resize: vertical;
            line-height: 1.6;
        }

        /* Buttons */
        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 8px 16px;
            border-radius: 10px;
            font-size: 12.5px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
            border: 1px solid transparent;
            white-space: nowrap;
            text-decoration: none;
        }
        .btn-primary {
            background: var(--primary);
            color: #FFFFFF;
            box-shadow: 0 2px 10px rgba(99, 102, 241, 0.35);
        }
        .btn-primary:hover {
            background: var(--primary-hover);
            box-shadow: 0 4px 14px rgba(99, 102, 241, 0.45);
        }
        .btn-secondary {
            background: #182235;
            color: var(--text-primary);
            border-color: var(--border-color);
        }
        .btn-secondary:hover {
            background: #202D45;
            border-color: #334155;
        }
        .btn-emerald {
            background: rgba(16, 185, 129, 0.18);
            color: #34D399;
            border-color: rgba(16, 185, 129, 0.4);
        }
        .btn-emerald:hover {
            background: rgba(16, 185, 129, 0.28);
        }
        .btn-amber {
            background: rgba(245, 158, 11, 0.18);
            color: #FBBF24;
            border-color: rgba(245, 158, 11, 0.4);
        }
        .btn-amber:hover {
            background: rgba(245, 158, 11, 0.28);
        }
        .btn-rose {
            background: rgba(244, 63, 94, 0.18);
            color: #FB7185;
            border-color: rgba(244, 63, 94, 0.4);
        }
        .btn-rose:hover {
            background: rgba(244, 63, 94, 0.28);
        }
        .btn-sm {
            padding: 5px 10px;
            font-size: 11px;
            border-radius: 7px;
        }

        /* Badges */
        .badge {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 3px 8px;
            border-radius: 6px;
            font-size: 10.5px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .badge-indigo { background: rgba(99,102,241,0.18); color: #A5B4FC; border: 1px solid rgba(99,102,241,0.3); }
        .badge-emerald { background: rgba(16,185,129,0.18); color: #6EE7B7; border: 1px solid rgba(16,185,129,0.3); }
        .badge-amber { background: rgba(245,158,11,0.18); color: #FCD34D; border: 1px solid rgba(245,158,11,0.3); }
        .badge-rose { background: rgba(244,63,94,0.18); color: #FDA4AF; border: 1px solid rgba(244,63,94,0.3); }
        .badge-cyan { background: rgba(6,182,212,0.18); color: #67E8F9; border: 1px solid rgba(6,182,212,0.3); }
        .badge-slate { background: #1E293B; color: #CBD5E1; border: 1px solid #334155; }

        /* Tables */
        .table-responsive {
            width: 100%;
            overflow-x: auto;
            border-radius: 10px;
            border: 1px solid var(--border-color);
        }
        .custom-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 12px;
            text-align: left;
        }
        .custom-table th {
            background: #0B0F19;
            color: #94A3B8;
            font-weight: 700;
            padding: 10px 14px;
            border-bottom: 1px solid var(--border-color);
            white-space: nowrap;
        }
        .custom-table td {
            padding: 11px 14px;
            border-bottom: 1px solid rgba(255,255,255,0.04);
            color: #E2E8F0;
            vertical-align: middle;
        }
        .custom-table tr:hover td {
            background: rgba(255,255,255,0.02);
        }

        /* Grids & Cards */
        .grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; }
        .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
        .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }

        @media (max-width: 1024px) {
            .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
        }

        /* Step Footer Navigation Bar */
        .step-footer-nav {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-top: 24px;
            margin-top: 24px;
            border-top: 1px solid var(--border-color);
        }

        /* Modal Dialogs */
        .modal-backdrop {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(4px);
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 100;
            padding: 20px;
        }
        .modal-backdrop.active {
            display: flex;
        }
        .modal-box {
            background: var(--surface-panel);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            width: 100%;
            max-width: 640px;
            max-height: 90vh;
            overflow-y: auto;
            box-shadow: 0 20px 40px rgba(0,0,0,0.6);
            display: flex;
            flex-direction: column;
        }
        .modal-header {
            padding: 16px 22px;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .modal-body {
            padding: 20px 22px;
            overflow-y: auto;
        }
        .modal-footer {
            padding: 14px 22px;
            border-top: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: flex-end;
            gap: 10px;
        }

        /* Visual Sequence Nodes for Workflow */
        .wf-node-track {
            display: flex;
            flex-direction: column;
            gap: 12px;
            position: relative;
        }
        .wf-node-card {
            background: var(--surface-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 14px 18px;
            display: flex;
            align-items: flex-start;
            gap: 14px;
            position: relative;
            transition: all 0.2s ease;
        }
        .wf-node-card:hover {
            border-color: rgba(99,102,241,0.4);
            transform: translateX(3px);
        }
        .wf-node-badge {
            width: 32px;
            height: 32px;
            border-radius: 8px;
            background: rgba(99,102,241,0.18);
            border: 1px solid rgba(99,102,241,0.3);
            color: #818CF8;
            font-size: 13px;
            font-weight: 800;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }

        /* 5 Architecture Pillar Cards (Clean, Prominent & Non-Slop) */
        .pillar-card-hero {
            background: var(--surface-card);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 22px 24px;
            cursor: pointer;
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .pillar-card-hero:hover {
            border-color: rgba(99, 102, 241, 0.45);
            background: var(--surface-card-hover);
            transform: translateY(-3px);
            box-shadow: 0 10px 24px rgba(0,0,0,0.4);
        }
        .pillar-card-hero.selected {
            border-color: var(--primary);
            background: linear-gradient(180deg, rgba(99, 102, 241, 0.16) 0%, rgba(18, 24, 38, 0.95) 100%);
            box-shadow: 0 0 24px rgba(99, 102, 241, 0.28);
        }
        .pillar-icon-box {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            margin-bottom: 14px;
            transition: transform 0.2s ease;
        }
        .pillar-card-hero:hover .pillar-icon-box {
            transform: scale(1.08);
        }

        /* 60 Themes Card Grid */
        .theme-card {
            background: var(--surface-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 10px;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .theme-card:hover {
            border-color: rgba(99,102,241,0.4);
            transform: translateY(-2px);
        }
        .theme-card.selected {
            border-color: var(--primary);
            background: rgba(99,102,241,0.14);
            box-shadow: 0 0 16px rgba(99,102,241,0.3);
        }

        /* Draft Slot Card */
        .draft-card {
            background: var(--surface-subtle);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 14px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: all 0.2s ease;
        }
        .draft-card:hover {
            border-color: rgba(99, 102, 241, 0.4);
            background: rgba(255,255,255,0.02);
        }

        /* Markdown PRD Output Viewer */
        .markdown-render {
            background: #05070B;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 28px;
            color: #CBD5E1;
            font-size: 13px;
            line-height: 1.7;
            max-height: 650px;
            overflow-y: auto;
        }
        .markdown-render h1 { font-size: 22px; color: #FFFFFF; margin: 20px 0 10px; font-weight: 800; border-bottom: 1px solid var(--border-color); padding-bottom: 8px; }
        .markdown-render h2 { font-size: 17px; color: #A5B4FC; margin: 18px 0 8px; font-weight: 700; }
        .markdown-render h3 { font-size: 14px; color: #E2E8F0; margin: 14px 0 6px; font-weight: 700; }
        .markdown-render p { margin-bottom: 12px; }
        .markdown-render ul, .markdown-render ol { margin-left: 20px; margin-bottom: 12px; }
        .markdown-render li { margin-bottom: 4px; }
        .markdown-render table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 12px; }
        .markdown-render th, .markdown-render td { border: 1px solid #1E293B; padding: 8px 12px; text-align: left; }
        .markdown-render th { background: #0F172A; color: #94A3B8; font-weight: 700; }
        .markdown-render blockquote { border-left: 4px solid var(--primary); padding-left: 14px; color: #94A3B8; margin: 12px 0; background: rgba(99,102,241,0.06); padding: 8px 14px; border-radius: 0 8px 8px 0; }
        .markdown-render code { font-family: 'JetBrains Mono', monospace; background: #0D111A; padding: 2px 6px; border-radius: 4px; font-size: 11.5px; color: #38BDF8; }
        .markdown-render pre { background: #080C14; padding: 14px; border-radius: 8px; overflow-x: auto; border: 1px solid #1E293B; margin: 14px 0; }
        .markdown-render pre code { background: transparent; padding: 0; color: #E2E8F0; }
    """

if __name__ == "__main__":
    print("CSS module compiled. Length:", len(get_css()))
