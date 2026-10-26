# CLAUDE.md

Context for Claude sessions in this repo. See `README.md` for layout and build details.

## Project

"Cross-Disaster Building Damage Assessment" by Muhammad Murtaza and Darrin Leleux
(Engineering Data Science, University of Houston). Research question: can a model
trained on other disasters (earthquakes, wildfires, tornadoes) assess building damage
in Houston after a flood, using few or no local labels?

- Dataset: xBD / xView2 (https://xview2.org/dataset), CC BY-NC-SA 4.0. Never commit
  imagery or labels; local data goes in the git-ignored `data/` folder.
- This repo holds only the two submission documents. Code and data are not required
  by the showcase.

## Showcase rules (UH HPE Data Science Institute Data Science Showcase)

Source: https://hpedsi.uh.edu/partnerships/sponsored-events/data-science-showcase
(checked 2026-10-25; re-check for updates).

- Registration closes 2026-11-01. Event / final presentation: 2026-12-07.
  Submission deadline for documents comes later by email to selected teams.
- Deliverables: a poster based on the UH poster template, and a presentation based
  on the poster. Files must be .pdf or .pptx; we submit PDF.
- The team number (from the registration acknowledgment email) must appear on the
  poster and on every slide. Not added yet.
- Judging: innovation, feasibility, impact, presentation.
- Open question: confirm with organizers that a Quarto reconstruction of the UH
  template is acceptable.

## Working conventions

- `poster/` and `slides/` are separate Quarto projects. Keep the slides consistent
  with the poster (same sections, same figures).
- Figures used by either document live in `shared/figures/`; reference them as
  `../shared/figures/<name>.png`.
- Poster boxes are fixed size (positions in inches in `poster/poster.css`); content
  does not grow the box. After edits, check for overflow in the rendered output.
- Build everything with `uv run scripts/build.py` (options: `--only poster|slides`,
  `--html-only`). Outputs go to `docs/`, which is committed and served by GitHub
  Pages, so the web version always matches the submitted PDFs. Rebuild and commit
  `docs/` together with source changes.
- After building, look at the PDFs (poster: one 48 x 36 in page; slides: 1280 x 720,
  one slide per page) before calling a change done.
- `slides/uh-slides.css` uses `!important` on the logo size because Quarto's
  footer.css loads later and would otherwise blow the logo up to full height.

## GitHub

- Target remote: https://github.com/dpleleux/cross-disaster-damage-assessment
  (not yet created/pushed as of 2026-10-25). GitHub Pages: branch `main`, folder `/docs`.
- `gh` CLI is not installed; git uses Git Credential Manager for auth.
- Commit only when asked.
