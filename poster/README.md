# University of Houston poster in Quarto

An editable Quarto adaptation of UH's 48 x 36-inch research poster:
https://www.uh.edu/research/_downloads/templates/poster-template-uh.pptx

## Open and edit in Positron

1. Extract this entire folder. Keep the files together.
2. Open `poster.qmd` in Positron.
3. Replace the title, authors, department, and text inside each `.panel-body`.
4. Use Quarto Preview, or run `quarto preview poster.qmd` in Positron's terminal.

The preview fits the window. Its print dimensions remain **48 inches wide by
36 inches high**. The supplied HTML is self-contained and can be opened offline.
The supplied PDF is a full-size blank template preview; regenerate it after editing.

## PDF from Positron

### Browser route (no LaTeX or Python PDF package)

Run `quarto render poster.qmd --to html`, open `poster.html` in Chrome or Edge,
and print to PDF. Enable background graphics, disable browser headers/footers,
and use zero margins. The CSS requests a 48 x 36-inch page. Check the saved PDF
properties before sending it to a printer, because browser/driver paper settings
can override the requested size. Choose a matching custom paper size if needed.

### Exact-size PDF with Python

Install WeasyPrint in your Python environment:

```bash
python -m pip install weasyprint
```

WeasyPrint needs native libraries. On Windows, install Pango as described in its
official setup guide (installing the Python package alone may not be sufficient):
https://doc.courtbouillon.org/weasyprint/stable/first_steps.html

Then, from this folder in Positron's terminal:

```bash
python export_pdf.py
```

This renders the QMD and produces `poster.pdf`. No LaTeX is required. The export
script checks that the result is one page. Inspect all text before printing:
fixed-size poster boxes do not grow when you add content. The browser console
also warns if a section's content exceeds its boundaries.

## Figures, computation, and layout

Put figures in `assets/`, then replace the figure placeholder with:

```markdown
![Your figure caption.](assets/your-figure.png){width=95%}
```

Normal Markdown lists and tables work inside `.panel-body`. Python or R code cells
can generate plots there too, with the corresponding Quarto computation engine
installed. For Python plotting, a typical cell uses `#| fig-width: 12` and
`#| fig-height: 7`; put it inside the desired panel and check the rendered size.

`poster.css` sets every section's position and height in inches. Change those
values to rebalance space. Font sizes are near the top of the stylesheet.
Optional `{.small}` divs use 26pt text. Maintain readable poster type rather than
shrinking large amounts of text to fit.

## Fidelity and provenance

The adaptation preserves the source's overall geometry, section ordering,
UH red (#C8102E), pale gray gradient, thin red outlines, logo placement, and
unheaded lower-center figure area. The UH logo was extracted unchanged from
the supplied PPTX. Retain UH's applicable brand rules when using it.

The source has some misaligned borders, overflowing placeholder boxes, and a
duplicate overlapping Results heading. This adaptation aligns the boxes and uses
one Results heading. Header heights are standardized to 0.825 inches. It uses a
60pt author line for fit (the source specifies 82pt) and 32pt body text. Fonts
fall back to available system fonts, so this is a close editable reconstruction,
not a pixel-identical PowerPoint rendering or a new officially approved UH template.

The template is a single research poster, not a Reveal.js slide deck. HTML/CSS
preserves this layout for print; changing the format to `beamer` or `pdf` will
not preserve it. Render HTML and use one of the PDF routes above.

Quarto option documentation: https://quarto.org/docs/reference/formats/html.html
