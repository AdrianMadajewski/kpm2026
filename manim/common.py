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
for klasa in (Tex, MathTex, Text, Dot, Line, Arrow, Arc, NumberLine, Axes,
              DecimalNumber, Integer):
    klasa.set_default(color=KOLOR_TEKST)

# Stałe kolory w całej prezentacji (ciemniejsze odcienie, czytelne na białym).
KOLOR_METRYKA = BLUE_D       # zwykła metryka d
KOLOR_CZESCIOWA = ManimColor("#E06C00")  # metryka częściowa p
KOLOR_SAMO = RED_D           # odległość punktu od siebie p(x,x)


# Plan referatu (te same punkty co w wersji Beamer).
PUNKTY_PLANU = [
    r"Przestrzenie metryczne i ich topologia",
    r"Przestrzenie częściowo metryczne",
    r"Topologia w przestrzeniach częściowo metrycznych",
    r"Zupełność i twierdzenie o punkcie stałym",
]


def plan_referatu(aktywny=None):
    """Lista punktów planu w ramkach połączonych strzałkami.

    aktywny -- numer punktu (od 0) do wyróżnienia albo None.
    """
    wiersze = VGroup()
    for i, tekst in enumerate(PUNKTY_PLANU):
        numer = Tex(rf"{i + 1}.", font_size=38)
        opis = Tex(tekst, font_size=38)
        wiersz = VGroup(numer, opis).arrange(RIGHT, buff=0.3)
        ramka = SurroundingRectangle(
            wiersz, buff=0.2, corner_radius=0.1, color=GRAY_C, stroke_width=2
        )
        wiersze.add(VGroup(ramka, wiersz))
    # Ramki o jednakowej szerokości, wyrównane do lewej.
    szer = max(w[0].width for w in wiersze)
    for w in wiersze:
        w[0].stretch_to_fit_width(szer).align_to(w[1], LEFT).shift(0.2 * LEFT)
    wiersze.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
    strzalki = VGroup(*[
        Arrow(wiersze[i][0].get_bottom(), wiersze[i + 1][0].get_top(),
              buff=0.05, stroke_width=3, max_tip_length_to_length_ratio=0.35,
              color=GRAY_C)
        for i in range(len(wiersze) - 1)
    ])
    if aktywny is not None:
        for i, w in enumerate(wiersze):
            if i == aktywny:
                w[0].set_stroke(KOLOR_CZESCIOWA, width=4)
            else:
                w[0].set_stroke(opacity=0.35)
                w[1].set_opacity(0.35)
    return VGroup(wiersze, strzalki)


# Bloki definicji, twierdzeń itd. — bez widocznej ramki i nagłówka.
# Zachowujemy strukturę VGroup(tlo, naglowek, tresc), żeby sceny mogły
# korzystać z pozycji bloku (np. komentarze obok), ale tło i nagłówek są
# niewidoczne.


def _niewidoczne_tlo(*obiekty):
    return SurroundingRectangle(VGroup(*obiekty), buff=0.25).set_stroke(opacity=0).set_fill(opacity=0)


def blok(tresc, rodzaj="Definicja", szerokosc=None):
    """Treść bloku. Zwraca VGroup(tlo, naglowek, tresc) z niewidocznym tłem i nagłówkiem."""
    naglowek = VectorizedPoint(tresc.get_corner(UL))
    wynik = VGroup(_niewidoczne_tlo(tresc), naglowek, tresc)
    wynik.rodzaj = rodzaj
    return wynik


def tlo_dla(b, *widoczne):
    """Niewidoczne tło dopasowane do widocznych fragmentów (zgodność ze scenami)."""
    return _niewidoczne_tlo(*widoczne)


def dopasuj_ramke(b, *widoczne):
    """Dawniej wydłużała ramkę; teraz praktycznie natychmiastowa i niewidoczna."""
    return Transform(b[0], tlo_dla(b, *widoczne), run_time=0.05)


# Bez generowania odwróconych animacji (bardzo wydłuża budowanie).
from manim_slides import Slide as _Slide
_Slide.skip_reversing = True
