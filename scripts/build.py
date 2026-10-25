"""Render the poster and slides to HTML and PDF in docs/. Run: uv run scripts/build.py

Requires Quarto on PATH. Poster PDF uses WeasyPrint (native Pango libraries
needed on Windows: https://doc.courtbouillon.org/weasyprint/stable/first_steps.html).
Slides PDF uses DeckTape via npx (Node.js) and a locally installed Chrome or Edge.

Options:
  --only poster|slides   build one document
  --html-only            skip PDF export
"""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
DECKTAPE = "decktape@3.14.0"
BROWSERS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
]


def require(tool):
    path = shutil.which(tool)
    if not path:
        sys.exit(f"{tool} was not found on PATH.")
    return path


def render(project):
    subprocess.run([require("quarto"), "render", str(ROOT / project)], check=True)


def poster_pdf():
    try:
        from weasyprint import HTML
    except (ImportError, OSError) as exc:
        sys.exit(f"WeasyPrint or its native dependencies are missing: {exc}")
    document = HTML(filename=str(DOCS / "poster" / "index.html")).render()
    if len(document.pages) != 1:
        sys.exit(f"Expected one poster page, got {len(document.pages)}. Check poster/poster.css.")
    out = DOCS / "poster" / "poster.pdf"
    document.write_pdf(out)
    print(f"Created {out.relative_to(ROOT)} (48 x 36 inches)")


def slides_pdf():
    browser = next((b for b in BROWSERS if Path(b).exists()), None)
    if not browser:
        sys.exit("No Chrome or Edge found for DeckTape. Add its path to BROWSERS in scripts/build.py.")
    out = DOCS / "slides" / "slides.pdf"
    # Use the local browser instead of letting Puppeteer download its own.
    env = {**os.environ, "PUPPETEER_SKIP_DOWNLOAD": "1"}
    subprocess.run(
        [require("npx"), "--yes", DECKTAPE, "reveal", "--size", "1280x720",
         "--chrome-path", browser,
         (DOCS / "slides" / "index.html").as_uri(), str(out)],
        check=True, env=env,
    )
    print(f"Created {out.relative_to(ROOT)}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--only", choices=["poster", "slides"])
    parser.add_argument("--html-only", action="store_true")
    args = parser.parse_args()

    if args.only in (None, "poster"):
        render("poster")
        if not args.html_only:
            poster_pdf()
    if args.only in (None, "slides"):
        render("slides")
        if not args.html_only:
            slides_pdf()


if __name__ == "__main__":
    main()
