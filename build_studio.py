# -*- coding: utf-8 -*-
"""
Main compiler for Enterprise PRD Studio.
Extracts preserved 60-theme assets from index.html.bak and stitches together
gen_css, gen_html, and gen_js_engines into a standalone, single-file index.html.
"""

import os
from gen_css import get_css
from gen_html import get_html
from gen_js_engines import get_js_engines
from gen_assets import get_preserved_assets

OUT_FILE = "index.html"

def build():
    print("Loading preserved 60 themes catalog & SVG generator...")
    mock_code, svg_code = get_preserved_assets()

    print("Generating CSS design system...")
    css = get_css()

    print("Generating HTML layout & 16-step workspace shell...")
    html = get_html()

    print("Generating JS reactive engines, 5 Pillars & Drafts Storage...")
    js_engines = get_js_engines()

    final_document = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enterprise PRD Studio - Requirements Engine &amp; Single-File MVP Prompt</title>
    <meta name="description" content="Enterprise Taxonomy Offline, Structured Requirements, Quality PRD Builder, and AI MVP Implementation Prompt Generator for Single-File HTML MVPs.">
    
    <!-- Google Fonts: Inter, Outfit, JetBrains Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Outfit:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    
    <!-- FontAwesome 6 CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    
    <!-- SweetAlert2 CDN -->
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>

    <style>
{css}
    </style>
</head>
<body>
{html}

    <script>
    // ============================================================================
    // 1. PRESERVED 60 DESIGN THEMES CATALOG
    // ============================================================================
    {mock_code}

    // ============================================================================
    // 2. PRESERVED ARTISAN SVG GENERATOR
    // ============================================================================
    {svg_code}

    // ============================================================================
    // 3. ENTERPRISE PRD ENGINES, 5 ARCHITECTURE PILLARS & DRAFTS STORAGE
    // ============================================================================
{js_engines}
    </script>
</body>
</html>
"""

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_document)

    size = os.path.getsize(OUT_FILE)
    print(f"Successfully compiled {OUT_FILE}! Total size: {size:,} bytes.")

if __name__ == "__main__":
    build()
