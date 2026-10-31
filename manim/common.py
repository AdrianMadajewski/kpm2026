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


# Ramki dla definicji, twierdzeń itd. (jak bloki w Beamerze).
STYL_BLOKU = {
    "Definicja":    (ManimColor("#EAF2FA"), KOLOR_METRYKA),
    "Twierdzenie":  (ManimColor("#FDEFE2"), KOLOR_CZESCIOWA),
    "Stwierdzenie": (ManimColor("#F1F1F1"), GRAY_D),
    "Lemat":        (ManimColor("#F1F1F1"), GRAY_D),
    "Wniosek":      (ManimColor("#F1F1F1"), GRAY_D),
}


def blok(tresc, rodzaj="Definicja", szerokosc=None):
    """Treść w ramce z nagłówkiem. Zwraca VGroup(tlo, naglowek, tresc).

    Ramka jest liczona od razu dla całej treści, więc można ją pokazać
    wcześniej, a fragmenty treści dopisywać później.
    """
    tlo_kolor, kolor = STYL_BLOKU[rodzaj]
    naglowek = Tex(rodzaj, font_size=28, color=kolor)
    naglowek.next_to(tresc, UP, buff=0.2).align_to(tresc, LEFT)
    calosc = VGroup(naglowek, tresc)
    tlo = SurroundingRectangle(calosc, buff=0.25, corner_radius=0.12,
                               color=kolor, stroke_width=2.5)
    if szerokosc is not None and tlo.width < szerokosc:
        tlo.stretch_to_fit_width(szerokosc).align_to(calosc, LEFT).shift(0.25 * LEFT)
    tlo.set_fill(tlo_kolor, 1)
    return VGroup(tlo, naglowek, tresc)


# Bez generowania odwróconych animacji (bardzo wydłuża budowanie).
from manim_slides import Slide as _Slide
_Slide.skip_reversing = True
