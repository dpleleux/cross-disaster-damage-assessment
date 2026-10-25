# Cross-Disaster Building Damage Assessment

Can a model trained on other disasters (earthquakes, wildfires, tornadoes) assess
building damage in Houston after a flood, using few or no local labels?

Poster and presentation for the
[UH HPE Data Science Institute Data Science Showcase](https://hpedsi.uh.edu/partnerships/sponsored-events/data-science-showcase),
by Muhammad Murtaza and Darrin Leleux (Engineering Data Science, University of Houston).
Data: [xBD / xView2](https://xview2.org/dataset).

## Layout

| Path | Contents |
|---|---|
| `poster/` | Quarto project: 48 x 36 in UH research poster (HTML/CSS). See `poster/TEMPLATE-NOTES.md` for template details and layout tips. |
| `slides/` | Quarto project: Reveal.js presentation with UH styling (`uh-slides.css`). |
| `shared/` | UH logo and `figures/` used by both documents. |
| `scripts/build.py` | Renders both documents to HTML and PDF in `docs/`. |
| `docs/` | Published output, served by GitHub Pages: `index.html` landing page, `poster/`, `slides/`. |
| `data/` | Local xBD data (git-ignored; never commit it). |

## Editing

- Poster text: `poster/poster.qmd`. Section positions and sizes: `poster/poster.css`.
  Boxes are fixed size; the browser console warns when content overflows.
- Slides: `slides/slides.qmd`.
- Figures: save to `shared/figures/` and reference them as
  `![Caption](../shared/figures/name.png)` from either document.
- Live preview: `quarto preview poster/poster.qmd` or `quarto preview slides/slides.qmd`.

## Building

Requirements: [Quarto](https://quarto.org), [uv](https://docs.astral.sh/uv/),
Node.js (for DeckTape), and Chrome or Edge. WeasyPrint on Windows also needs Pango:
see the [WeasyPrint install guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html).

```bash
uv sync
uv run scripts/build.py              # both documents, HTML + PDF
uv run scripts/build.py --only poster
uv run scripts/build.py --html-only
```

Outputs:

- `docs/poster/index.html`, `docs/poster/poster.pdf` (48 x 36 in, one page)
- `docs/slides/index.html`, `docs/slides/slides.pdf` (1280 x 720, one slide per page)

Commit `docs/` after building so the web version matches the submitted PDFs.
