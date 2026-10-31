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

# Stałe kolory w całej prezentacji.
KOLOR_METRYKA = BLUE        # zwykła metryka d
KOLOR_CZESCIOWA = ORANGE    # metryka częściowa p
KOLOR_SAMO = RED            # odległość punktu od siebie p(x,x)
