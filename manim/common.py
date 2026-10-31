"""Wspólne ustawienia animacji: szablon LaTeX i kolory."""
from manim import *

# Polskie znaki bez babel (T1 + utf8 wystarczą do składu).
SZABLON = TexTemplate()
SZABLON.add_to_preamble(
    r"\usepackage[T1]{fontenc}"
    r"\usepackage[utf8]{inputenc}"
    r"\usepackage{lmodern}"
    r"\usepackage{amsmath,amssymb,mathtools}"
)
config.tex_template = SZABLON

# Jasne tło, ciemny tekst.
config.background_color = WHITE
KOLOR_TEKST = BLACK
KOLOR_DRUGORZEDNY = GRAY_D   # podtytuły, opisy
for klasa in (Tex, MathTex, Text, Dot, Line, Arrow, Arc, NumberLine, Axes):
    klasa.set_default(color=KOLOR_TEKST)

# Stałe kolory w całej prezentacji (ciemniejsze odcienie, czytelne na białym).
KOLOR_METRYKA = BLUE_D       # zwykła metryka d
KOLOR_CZESCIOWA = ManimColor("#E06C00")  # metryka częściowa p
KOLOR_SAMO = RED_D           # odległość punktu od siebie p(x,x)
