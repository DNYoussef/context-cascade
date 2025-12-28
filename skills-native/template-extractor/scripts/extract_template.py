#!/usr/bin/env python3
"""
Template Extraction Helper Script

Automates the extraction of design specifications from Office documents.
Handles DOCX, PPTX, and XLSX files by unpacking and parsing their XML contents.

Usage:
    python extract_template.py <document_path> <output_dir>

Example:
    python extract_template.py company_sop.docx ./extracted_template
"""

import sys
import os
import zipfile
import json
import re
import shutil
from xml.etree import ElementTree as ET
from pathlib import Path

# XML namespaces used in Office documents
NAMESPACES = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'x': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main',
}

def half_points_to_points(half_points):
    """Convert OOXML half-points to standard points."""
    return int(half_points) / 2

def twips_to_points(twips):
    """Convert OOXML twips (1/20 of a point) to points."""
    return int(twips) / 20

def emu_to_inches(emu):
    """Convert EMUs (English Metric Units) to inches."""
    return int(emu) / 914400

def extract_theme_colors(theme_xml_path):
    """Extract color scheme from theme XML file."""
    colors = {}
    try:
        tree = ET.parse(theme_xml_path)
        root = tree.getroot()
        
        # Find color scheme element
        for clr_scheme in root.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}clrScheme'):
            color_names = ['dk1', 'lt1', 'dk2', 'lt2', 'accent1', 'accent2', 
                          'accent3', 'accent4', 'accent5', 'accent6', 'hlink', 'folHlink']
            
            for color_name in color_names:
                elem = clr_scheme.find(f'a:{color_name}', NAMESPACES)
                if elem is not None:
                    # Check for srgbClr (direct hex color)
                    srgb = elem.find('.//a:srgbClr', NAMESPACES)
                    if srgb is not None:
                        colors[color_name] = f"#{srgb.get('val')}"
                    # Check for sysClr (system color)
                    sys_clr = elem.find('.//a:sysClr', NAMESPACES)
                    if sys_clr is not None:
                        last_clr = sys_clr.get('lastClr')
                        if last_clr:
                            colors[color_name] = f"#{last_clr}"
    except Exception as e:
        print(f"Warning: Could not parse theme colors: {e}")
    
    return colors

def extract_theme_fonts(theme_xml_path):
    """Extract font scheme from theme XML file."""
    fonts = {'major': None, 'minor': None}
    try:
        tree = ET.parse(theme_xml_path)
        root = tree.getroot()
        
        # Find font scheme
        for font_scheme in root.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}fontScheme'):
            major = font_scheme.find('.//a:majorFont/a:latin', NAMESPACES)
            minor = font_scheme.find('.//a:minorFont/a:latin', NAMESPACES)
            
            if major is not None:
                fonts['major'] = major.get('typeface')
            if minor is not None:
                fonts['minor'] = minor.get('typeface')
    except Exception as e:
        print(f"Warning: Could not parse theme fonts: {e}")
    
    return fonts

def extract_styles(styles_xml_path):
    """Extract style definitions from styles.xml (DOCX)."""
    styles = {}
    try:
        tree = ET.parse(styles_xml_path)
        root = tree.getroot()
        
        for style in root.findall('.//w:style', NAMESPACES):
            style_id = style.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}styleId')
            style_type = style.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}type')
            
            style_info = {
                'type': style_type,
                'id': style_id,
            }
            
            # Get style name
            name_elem = style.find('w:name', NAMESPACES)
            if name_elem is not None:
                style_info['name'] = name_elem.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val')
            
            # Get font properties
            rPr = style.find('.//w:rPr', NAMESPACES)
            if rPr is not None:
                # Font size (in half-points)
                sz = rPr.find('w:sz', NAMESPACES)
                if sz is not None:
                    val = sz.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val')
                    style_info['font_size_pt'] = half_points_to_points(val)
                
                # Font family
                rFonts = rPr.find('w:rFonts', NAMESPACES)
                if rFonts is not None:
                    style_info['font_family'] = rFonts.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ascii')
                
                # Bold
                bold = rPr.find('w:b', NAMESPACES)
                style_info['bold'] = bold is not None
                
                # Color
                color = rPr.find('w:color', NAMESPACES)
                if color is not None:
                    val = color.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val')
                    if val and val != 'auto':
                        style_info['color'] = f"#{val}"
            
            # Get paragraph properties
            pPr = style.find('.//w:pPr', NAMESPACES)
            if pPr is not None:
                # Spacing
                spacing = pPr.find('w:spacing', NAMESPACES)
                if spacing is not None:
                    before = spacing.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}before')
                    after = spacing.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}after')
                    line = spacing.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}line')
                    
                    if before:
                        style_info['space_before_pt'] = twips_to_points(before)
                    if after:
                        style_info['space_after_pt'] = twips_to_points(after)
                    if line:
                        style_info['line_spacing_twips'] = int(line)
            
            styles[style_id] = style_info
    except Exception as e:
        print(f"Warning: Could not parse styles: {e}")
    
    return styles

def extract_page_settings(document_xml_path):
    """Extract page settings from document.xml (DOCX)."""
    settings = {}
    try:
        tree = ET.parse(document_xml_path)
        root = tree.getroot()
        
        # Find sectPr (section properties) - usually at the end of body
        for sectPr in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sectPr'):
            # Page size
            pgSz = sectPr.find('w:pgSz', NAMESPACES)
            if pgSz is not None:
                w = pgSz.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}w')
                h = pgSz.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}h')
                orient = pgSz.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}orient')
                
                if w:
                    settings['page_width_inches'] = twips_to_points(w) / 72
                if h:
                    settings['page_height_inches'] = twips_to_points(h) / 72
                settings['orientation'] = orient or 'portrait'
            
            # Margins
            pgMar = sectPr.find('w:pgMar', NAMESPACES)
            if pgMar is not None:
                for margin in ['top', 'right', 'bottom', 'left', 'header', 'footer']:
                    val = pgMar.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}' + margin)
                    if val:
                        settings[f'margin_{margin}_inches'] = twips_to_points(val) / 72
    except Exception as e:
        print(f"Warning: Could not parse page settings: {e}")
    
    return settings

def unpack_document(doc_path, output_dir):
    """Unpack an Office document (ZIP file) to a directory."""
    with zipfile.ZipFile(doc_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    print(f"Unpacked document to: {output_dir}")

def copy_media_assets(unpacked_dir, output_assets_dir):
    """Copy media files (logos, images) to assets directory."""
    media_paths = [
        os.path.join(unpacked_dir, 'word', 'media'),
        os.path.join(unpacked_dir, 'ppt', 'media'),
        os.path.join(unpacked_dir, 'xl', 'media'),
    ]
    
    os.makedirs(output_assets_dir, exist_ok=True)
    copied = []
    
    for media_path in media_paths:
        if os.path.exists(media_path):
            for filename in os.listdir(media_path):
                src = os.path.join(media_path, filename)
                dst = os.path.join(output_assets_dir, filename)
                shutil.copy2(src, dst)
                copied.append(filename)
                print(f"Copied asset: {filename}")
    
    return copied

def detect_document_type(doc_path):
    """Detect document type from file extension."""
    ext = Path(doc_path).suffix.lower()
    type_map = {
        '.docx': 'docx',
        '.pptx': 'pptx',
        '.xlsx': 'xlsx',
    }
    return type_map.get(ext, 'unknown')

def extract_template(doc_path, output_dir):
    """Main extraction function."""
    
    # Create output directory structure
    os.makedirs(output_dir, exist_ok=True)
    unpacked_dir = os.path.join(output_dir, 'unpacked')
    assets_dir = os.path.join(output_dir, 'assets')
    
    # Detect document type
    doc_type = detect_document_type(doc_path)
    print(f"Document type: {doc_type}")
    
    # Unpack the document
    unpack_document(doc_path, unpacked_dir)
    
    # Initialize extraction results
    extraction = {
        'document_type': doc_type,
        'source_file': os.path.basename(doc_path),
        'colors': {},
        'fonts': {},
        'styles': {},
        'page_settings': {},
        'assets': [],
    }
    
    # Extract based on document type
    if doc_type == 'docx':
        # Theme (colors and fonts)
        theme_path = os.path.join(unpacked_dir, 'word', 'theme', 'theme1.xml')
        if os.path.exists(theme_path):
            extraction['colors'] = extract_theme_colors(theme_path)
            extraction['fonts'] = extract_theme_fonts(theme_path)
        
        # Styles
        styles_path = os.path.join(unpacked_dir, 'word', 'styles.xml')
        if os.path.exists(styles_path):
            extraction['styles'] = extract_styles(styles_path)
        
        # Page settings
        doc_path_xml = os.path.join(unpacked_dir, 'word', 'document.xml')
        if os.path.exists(doc_path_xml):
            extraction['page_settings'] = extract_page_settings(doc_path_xml)
    
    elif doc_type == 'pptx':
        theme_path = os.path.join(unpacked_dir, 'ppt', 'theme', 'theme1.xml')
        if os.path.exists(theme_path):
            extraction['colors'] = extract_theme_colors(theme_path)
            extraction['fonts'] = extract_theme_fonts(theme_path)
    
    elif doc_type == 'xlsx':
        theme_path = os.path.join(unpacked_dir, 'xl', 'theme', 'theme1.xml')
        if os.path.exists(theme_path):
            extraction['colors'] = extract_theme_colors(theme_path)
            extraction['fonts'] = extract_theme_fonts(theme_path)
    
    # Copy media assets
    extraction['assets'] = copy_media_assets(unpacked_dir, assets_dir)
    
    # Save extraction results as JSON
    results_path = os.path.join(output_dir, 'extraction_results.json')
    with open(results_path, 'w') as f:
        json.dump(extraction, f, indent=2)
    print(f"\nExtraction results saved to: {results_path}")
    
    # Print summary
    print("\n" + "="*50)
    print("EXTRACTION SUMMARY")
    print("="*50)
    
    print(f"\nTheme Colors Found: {len(extraction['colors'])}")
    for name, color in extraction['colors'].items():
        print(f"  {name}: {color}")
    
    print(f"\nTheme Fonts:")
    print(f"  Major (headings): {extraction['fonts'].get('major', 'Not found')}")
    print(f"  Minor (body): {extraction['fonts'].get('minor', 'Not found')}")
    
    print(f"\nStyles Found: {len(extraction['styles'])}")
    # Show key styles
    key_styles = ['Heading1', 'Heading2', 'Heading3', 'Normal', 'Title']
    for style_id in key_styles:
        if style_id in extraction['styles']:
            s = extraction['styles'][style_id]
            size = s.get('font_size_pt', '?')
            font = s.get('font_family', '?')
            print(f"  {style_id}: {font} {size}pt")
    
    if extraction['page_settings']:
        ps = extraction['page_settings']
        print(f"\nPage Settings:")
        print(f"  Size: {ps.get('page_width_inches', '?')}\" x {ps.get('page_height_inches', '?')}\"")
        print(f"  Orientation: {ps.get('orientation', '?')}")
        print(f"  Margins (T/R/B/L): {ps.get('margin_top_inches', '?')}\" / " +
              f"{ps.get('margin_right_inches', '?')}\" / " +
              f"{ps.get('margin_bottom_inches', '?')}\" / " +
              f"{ps.get('margin_left_inches', '?')}\"")
    
    print(f"\nAssets Extracted: {len(extraction['assets'])}")
    for asset in extraction['assets']:
        print(f"  {asset}")
    
    print("\n" + "="*50)
    print("Next steps:")
    print("1. Review extraction_results.json for raw data")
    print("2. Inspect unpacked/ directory for detailed XML")
    print("3. Check assets/ for logos and images")
    print("4. Use this data to complete TEMPLATE_SPEC.md and AI_PROMPT.md")
    print("="*50)
    
    return extraction

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python extract_template.py <document_path> <output_dir>")
        print("Example: python extract_template.py company_sop.docx ./extracted_template")
        sys.exit(1)
    
    doc_path = sys.argv[1]
    output_dir = sys.argv[2]
    
    if not os.path.exists(doc_path):
        print(f"Error: File not found: {doc_path}")
        sys.exit(1)
    
    extract_template(doc_path, output_dir)
