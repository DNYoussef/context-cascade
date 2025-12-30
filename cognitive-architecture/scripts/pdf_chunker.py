#!/usr/bin/env python3
"""
PDF Chunker for Large Document Processing

Safely extracts chunks from large PDFs to avoid context window overflow.
Designed for extracting specific chapters/sections for axiom analysis.

Usage:
    python pdf_chunker.py <pdf_path> --toc         # Show table of contents
    python pdf_chunker.py <pdf_path> --pages 1-50  # Extract page range
    python pdf_chunker.py <pdf_path> --search "self-reference"  # Find keyword
    python pdf_chunker.py <pdf_path> --chunk-all   # Chunk entire book

Output:
    chunks/ directory with individual text files per chapter/section
"""

import os
import sys
import argparse
import json
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional


def check_dependencies():
    """Check and report on available PDF libraries."""
    available = {}

    try:
        import fitz  # PyMuPDF
        available['pymupdf'] = True
        print("[OK] PyMuPDF (fitz) available")
    except ImportError:
        available['pymupdf'] = False
        print("[WARN] PyMuPDF not installed: pip install PyMuPDF")

    try:
        import pdfplumber
        available['pdfplumber'] = True
        print("[OK] pdfplumber available")
    except ImportError:
        available['pdfplumber'] = False
        print("[WARN] pdfplumber not installed: pip install pdfplumber")

    try:
        from pypdf import PdfReader
        available['pypdf'] = True
        print("[OK] pypdf available")
    except ImportError:
        try:
            from PyPDF2 import PdfReader
            available['pypdf2'] = True
            print("[OK] PyPDF2 available")
        except ImportError:
            available['pypdf'] = False
            print("[WARN] pypdf not installed: pip install pypdf")

    return available


class PDFChunker:
    """
    Chunks large PDFs into manageable sections.

    Designed to prevent context window overflow when processing
    books like Metamagical Themas (800+ pages).
    """

    def __init__(self, pdf_path: str, output_dir: str = None):
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir) if output_dir else self.pdf_path.parent / "chunks"
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Try to initialize with available library
        self.reader = None
        self.library = None
        self._init_reader()

    def _init_reader(self):
        """Initialize PDF reader with best available library."""
        try:
            import fitz
            self.doc = fitz.open(str(self.pdf_path))
            self.library = 'pymupdf'
            print(f"[PDF] Opened with PyMuPDF: {len(self.doc)} pages")
            return
        except ImportError:
            pass

        try:
            import pdfplumber
            self.doc = pdfplumber.open(str(self.pdf_path))
            self.library = 'pdfplumber'
            print(f"[PDF] Opened with pdfplumber: {len(self.doc.pages)} pages")
            return
        except ImportError:
            pass

        try:
            from pypdf import PdfReader
            self.doc = PdfReader(str(self.pdf_path))
            self.library = 'pypdf'
            print(f"[PDF] Opened with pypdf: {len(self.doc.pages)} pages")
            return
        except ImportError:
            pass

        raise ImportError(
            "No PDF library available. Install one of:\n"
            "  pip install PyMuPDF\n"
            "  pip install pdfplumber\n"
            "  pip install pypdf"
        )

    @property
    def page_count(self) -> int:
        """Get total page count."""
        if self.library == 'pymupdf':
            return len(self.doc)
        elif self.library == 'pdfplumber':
            return len(self.doc.pages)
        elif self.library == 'pypdf':
            return len(self.doc.pages)
        return 0

    def get_page_text(self, page_num: int) -> str:
        """Extract text from a single page (0-indexed)."""
        if self.library == 'pymupdf':
            return self.doc[page_num].get_text()
        elif self.library == 'pdfplumber':
            page = self.doc.pages[page_num]
            return page.extract_text() or ""
        elif self.library == 'pypdf':
            return self.doc.pages[page_num].extract_text() or ""
        return ""

    def extract_pages(self, start: int, end: int) -> str:
        """
        Extract text from page range (1-indexed, inclusive).

        Args:
            start: First page (1-indexed)
            end: Last page (1-indexed, inclusive)

        Returns:
            Combined text from all pages in range
        """
        # Convert to 0-indexed
        start_idx = max(0, start - 1)
        end_idx = min(self.page_count, end)

        texts = []
        for i in range(start_idx, end_idx):
            page_text = self.get_page_text(i)
            texts.append(f"\n{'='*60}\n[PAGE {i+1}]\n{'='*60}\n")
            texts.append(page_text)

        return "\n".join(texts)

    def search_keyword(self, keyword: str, context_pages: int = 1) -> List[Dict]:
        """
        Find pages containing keyword.

        Args:
            keyword: Text to search for
            context_pages: Pages before/after to include

        Returns:
            List of matches with page numbers and snippets
        """
        matches = []
        keyword_lower = keyword.lower()

        for i in range(self.page_count):
            text = self.get_page_text(i)
            if keyword_lower in text.lower():
                # Find snippet around keyword
                idx = text.lower().find(keyword_lower)
                start = max(0, idx - 100)
                end = min(len(text), idx + len(keyword) + 100)
                snippet = text[start:end].replace('\n', ' ')

                matches.append({
                    "page": i + 1,  # 1-indexed
                    "snippet": f"...{snippet}...",
                    "context_range": (
                        max(1, i + 1 - context_pages),
                        min(self.page_count, i + 1 + context_pages)
                    )
                })

        return matches

    def get_toc(self) -> List[Dict]:
        """
        Extract table of contents if available.

        Returns:
            List of TOC entries with title and page
        """
        toc = []

        if self.library == 'pymupdf':
            raw_toc = self.doc.get_toc()
            for level, title, page in raw_toc:
                toc.append({
                    "level": level,
                    "title": title,
                    "page": page,
                })
        else:
            # Search first 20 pages for "Contents" or "Table of Contents"
            for i in range(min(20, self.page_count)):
                text = self.get_page_text(i)
                if "contents" in text.lower():
                    toc.append({
                        "level": 0,
                        "title": f"[Possible TOC on page {i+1}]",
                        "page": i + 1,
                    })

        return toc

    def chunk_by_pages(self, chunk_size: int = 30) -> List[Path]:
        """
        Split entire PDF into chunks of N pages each.

        Args:
            chunk_size: Pages per chunk

        Returns:
            List of output file paths
        """
        output_files = []

        for start in range(0, self.page_count, chunk_size):
            end = min(start + chunk_size, self.page_count)
            chunk_num = (start // chunk_size) + 1

            text = self.extract_pages(start + 1, end)

            output_file = self.output_dir / f"chunk_{chunk_num:03d}_pages_{start+1}-{end}.txt"
            output_file.write_text(text, encoding='utf-8')
            output_files.append(output_file)

            print(f"[CHUNK] {output_file.name}: pages {start+1}-{end}")

        return output_files

    def save_page_range(self, start: int, end: int, name: str = None) -> Path:
        """
        Save specific page range to file.

        Args:
            start: First page (1-indexed)
            end: Last page (1-indexed)
            name: Optional output filename

        Returns:
            Path to output file
        """
        text = self.extract_pages(start, end)

        if not name:
            name = f"pages_{start}-{end}.txt"

        output_file = self.output_dir / name
        output_file.write_text(text, encoding='utf-8')

        print(f"[SAVED] {output_file}: {end - start + 1} pages, {len(text):,} chars")
        return output_file

    def close(self):
        """Close the PDF document."""
        if self.library == 'pymupdf':
            self.doc.close()
        elif self.library == 'pdfplumber':
            self.doc.close()


# =============================================================================
# METAMAGICAL THEMAS SPECIFIC TARGETING
# =============================================================================

# Based on research, these are the key sections for VERILINGUA/VERIX
METAMAGICAL_TARGETS = {
    "self_reference": {
        "description": "Self-Referential Sentences and Viral Structures",
        "keywords": ["self-referential", "self-reference", "autological", "heterological"],
        "estimated_pages": (1, 100),  # Section I: Snags and Snarls
    },
    "nomic": {
        "description": "Nomic: Self-Modifying Game",
        "keywords": ["nomic", "reflexivity", "self-amendment"],
        "estimated_pages": (80, 130),
    },
    "lisp_recursion": {
        "description": "Lisp and Recursive Structures",
        "keywords": ["lisp", "recursion", "lambda", "atoms and lists"],
        "estimated_pages": (400, 500),  # Section IV
    },
    "strange_loops": {
        "description": "Strange Loops and Tangled Hierarchies",
        "keywords": ["strange loop", "tangled hierarchy", "level-crossing"],
        "estimated_pages": (600, 700),
    },
    "turing_test": {
        "description": "Turing Test and Machine Intelligence",
        "keywords": ["turing test", "imitation game", "machine intelligence"],
        "estimated_pages": (500, 600),  # Section V
    },
}


def analyze_metamagical_themas(pdf_path: str, output_dir: str = None):
    """
    Specialized analysis for Metamagical Themas.

    Extracts targeted sections relevant to VERILINGUA/VERIX development.
    """
    chunker = PDFChunker(pdf_path, output_dir)

    print(f"\n{'='*60}")
    print("METAMAGICAL THEMAS TARGETED EXTRACTION")
    print(f"{'='*60}")
    print(f"Total pages: {chunker.page_count}")

    # Show TOC if available
    toc = chunker.get_toc()
    if toc:
        print(f"\nTable of Contents ({len(toc)} entries):")
        for entry in toc[:20]:  # First 20 entries
            indent = "  " * entry["level"]
            print(f"{indent}{entry['title']} (p.{entry['page']})")

    # Search for target sections
    print(f"\n{'='*60}")
    print("SEARCHING FOR KEY SECTIONS")
    print(f"{'='*60}")

    found_sections = {}

    for section_name, section_info in METAMAGICAL_TARGETS.items():
        print(f"\n[SECTION] {section_name}: {section_info['description']}")

        all_matches = []
        for keyword in section_info["keywords"]:
            matches = chunker.search_keyword(keyword)
            all_matches.extend(matches)
            if matches:
                print(f"  '{keyword}': found on pages {[m['page'] for m in matches[:5]]}")

        if all_matches:
            # Deduplicate and sort by page
            pages = sorted(set(m["page"] for m in all_matches))
            found_sections[section_name] = {
                "pages": pages,
                "count": len(pages),
                "info": section_info,
            }

    # Generate extraction plan
    print(f"\n{'='*60}")
    print("EXTRACTION PLAN")
    print(f"{'='*60}")

    plan = []
    for section_name, data in found_sections.items():
        pages = data["pages"]
        if len(pages) >= 3:
            # Find contiguous ranges
            start = min(pages)
            end = max(pages)
            plan.append({
                "name": section_name,
                "start": max(1, start - 5),  # 5 pages context before
                "end": min(chunker.page_count, end + 5),  # 5 pages context after
            })
            print(f"  {section_name}: pages {start}-{end} ({len(pages)} hits)")

    # Save plan
    plan_file = chunker.output_dir / "extraction_plan.json"
    with open(plan_file, 'w') as f:
        json.dump({
            "total_pages": chunker.page_count,
            "toc_entries": len(toc),
            "found_sections": {k: {"pages": v["pages"][:10], "count": v["count"]}
                             for k, v in found_sections.items()},
            "extraction_plan": plan,
        }, f, indent=2)

    print(f"\n[PLAN] Saved to: {plan_file}")

    chunker.close()
    return plan


def main():
    parser = argparse.ArgumentParser(
        description="PDF Chunker for Large Document Processing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python pdf_chunker.py metamagical.pdf --toc
    python pdf_chunker.py metamagical.pdf --pages 1-50
    python pdf_chunker.py metamagical.pdf --search "self-reference"
    python pdf_chunker.py metamagical.pdf --metamagical
    python pdf_chunker.py metamagical.pdf --chunk-all --chunk-size 25
        """
    )

    parser.add_argument("pdf_path", help="Path to PDF file")
    parser.add_argument("--output", "-o", help="Output directory for chunks")
    parser.add_argument("--toc", action="store_true", help="Show table of contents")
    parser.add_argument("--pages", help="Extract page range (e.g., '1-50')")
    parser.add_argument("--search", help="Search for keyword")
    parser.add_argument("--chunk-all", action="store_true", help="Chunk entire document")
    parser.add_argument("--chunk-size", type=int, default=30, help="Pages per chunk")
    parser.add_argument("--metamagical", action="store_true",
                       help="Specialized analysis for Metamagical Themas")
    parser.add_argument("--check-deps", action="store_true", help="Check PDF library dependencies")

    args = parser.parse_args()

    if args.check_deps:
        check_dependencies()
        return

    if not Path(args.pdf_path).exists():
        print(f"[ERROR] File not found: {args.pdf_path}")
        sys.exit(1)

    if args.metamagical:
        analyze_metamagical_themas(args.pdf_path, args.output)
        return

    chunker = PDFChunker(args.pdf_path, args.output)

    if args.toc:
        toc = chunker.get_toc()
        print(f"\nTable of Contents ({len(toc)} entries):")
        for entry in toc:
            indent = "  " * entry["level"]
            print(f"{indent}{entry['title']} (p.{entry['page']})")

    elif args.pages:
        match = re.match(r'(\d+)-(\d+)', args.pages)
        if match:
            start, end = int(match.group(1)), int(match.group(2))
            chunker.save_page_range(start, end)
        else:
            print(f"[ERROR] Invalid page range: {args.pages}")

    elif args.search:
        matches = chunker.search_keyword(args.search)
        print(f"\nFound '{args.search}' on {len(matches)} pages:")
        for m in matches[:20]:
            print(f"  Page {m['page']}: {m['snippet'][:100]}...")

    elif args.chunk_all:
        files = chunker.chunk_by_pages(args.chunk_size)
        print(f"\nCreated {len(files)} chunks in: {chunker.output_dir}")

    else:
        print(f"PDF: {args.pdf_path}")
        print(f"Pages: {chunker.page_count}")
        print("\nUse --help for options")

    chunker.close()


if __name__ == "__main__":
    main()
