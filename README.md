# Czy odległość punktu od samego siebie musi być zerowa?

Talk on Matthews' partial metric spaces, KPM 2026 (Warsaw) — Adrian Madajewski.

**Presentation:** https://adrianmadajewski.github.io/kpm2026/
(use the arrow keys or click to advance; T hides the timer)

**Download (offline HTML):** https://github.com/AdrianMadajewski/kpm2026/releases/download/html/prezentacja.html
— one self-contained file, open it in any browser

**PDF (Beamer):** https://github.com/AdrianMadajewski/kpm2026/releases/download/pdf/prezentacja.pdf
— also attached as the `prezentacja-pdf` artifact to every
[PDF workflow run](https://github.com/AdrianMadajewski/kpm2026/actions/workflows/pdf.yml)

- `abstrakt.md` — abstract (in Polish)
- `beamer/` — LaTeX Beamer version
- `manim/` — animated version (Manim + manim-slides); see [`manim/README.md`](manim/README.md) for local builds

Two GitHub Actions workflows rebuild everything automatically:

- `.github/workflows/presentation.yml` renders the animated slides in 1080p, publishes them on GitHub Pages
  and attaches the HTML file to the `html` release (on every push that touches `manim/`),
- `.github/workflows/pdf.yml` compiles the Beamer PDF and attaches it to the `pdf` release
  (on every push that touches `beamer/`).
