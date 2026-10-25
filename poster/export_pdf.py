"""Render the Quarto poster to a full-size PDF. Run: python export_pdf.py

Requires Quarto on PATH and WeasyPrint: python -m pip install weasyprint
See https://doc.courtbouillon.org/weasyprint/stable/first_steps.html for
platform-specific native dependencies, particularly Pango on Windows.
"""
from pathlib import Path
import shutil
import subprocess
import sys


def main():
    folder = Path(__file__).resolve().parent
    quarto = shutil.which("quarto")
    if not quarto:
        sys.exit("Quarto was not found on PATH. Run this in Positron's terminal with Quarto installed.")
    try:
        from weasyprint import HTML
    except (ImportError, OSError) as exc:
        sys.exit(f"WeasyPrint or its native dependencies are missing: {exc}\nSee README.md for setup.")
    subprocess.run([quarto, "render", "poster.qmd", "--to", "html"], cwd=folder, check=True)
    document = HTML(filename=str(folder / "poster.html")).render()
    if len(document.pages) != 1:
        sys.exit(f"Expected one poster page, got {len(document.pages)}. Check poster.css before printing.")
    document.write_pdf(folder / "poster.pdf")
    print(f"Created {folder / 'poster.pdf'} (48 x 36 inches)")


if __name__ == "__main__":
    main()
