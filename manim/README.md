# Animated slides (Manim + manim-slides)

The slides are written in Polish; this folder holds the scene code and the build script.

## Installation (Windows)

1. **Python 3.10–3.12** from python.org (tick *Add python.exe to PATH* in the installer).
2. **LaTeX**: MiKTeX (https://miktex.org) — during setup choose *Install missing packages on-the-fly: Yes*.
   TeX Live works too. The scenes need `amsmath`, `amssymb`, `mathtools`, `lmodern` and Polish fonts (`T1` encoding).
3. In a terminal opened in this `manim` folder:

   ```
   py -3.12 -m venv .venv
   .venv\Scripts\activate
   python -m pip install --upgrade pip
   pip install manim==0.19.1 manim-slides==5.7.0
   ```

   The versions are pinned on purpose: manim 0.22 does not work with manim-slides 5.7.

4. Check the setup: `python build.py --scene Tytul` should finish without errors.

## Building

Double-click `build_hd.bat`, or run in the activated environment:

```
python build.py --quality h      # 1080p60, the conference version
python build.py                  # quick 360p preview
python build.py --scene Kule     # re-render one scene only
python build.py --html-only      # re-bundle without rendering
python build.py --scene PrzykladMax --quality h --html   # one scene alone -> PrzykladMax.html
python build.py --scene PrzykladMax --html-only          # bundle an already rendered scene alone
```

The result is `prezentacja.html`: one file with the videos and reveal.js embedded,
which works offline. The first `--html-only`/full build downloads reveal.js once,
so it needs internet that time. A full 1080p build takes a while (tens of minutes).

Controls in the browser: arrow keys / space to advance, `F` for full screen.

## Files

- `build.py` — build script; the `SCENES` list sets the slide order.
- `common.py` — shared colours, LaTeX template and helpers.
- `sNN_*.py` — scenes, numbered in presentation order.
