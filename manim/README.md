# Animacje (Manim + manim-slides)

## Instalacja (Windows)

1. Python 3.10–3.12 oraz LaTeX (MiKTeX lub TeX Live) w `PATH`.
2. W folderze `manim`:

   ```
   py -m venv .venv
   .venv\Scripts\activate
   pip install manim==0.19.1 manim-slides==5.7.0
   ```

   Wersje są przypięte: manim 0.22 nie współpracuje z manim-slides 5.7.

## Budowanie

```
python zbuduj.py              # podgląd 480p
python zbuduj.py --jakosc h   # wersja na konferencję, 1080p
python zbuduj.py --tylko-html # tylko składanie HTML z już wyrenderowanych scen
```

Wynik: `prezentacja.html` — jeden plik z osadzonymi filmami i reveal.js,
działa bez internetu. Przy pierwszym budowaniu manim-slides pobiera reveal.js
z CDN (potrzebny internet tylko wtedy).

Kolejność scen ustala lista `SCENY` w `zbuduj.py`.
