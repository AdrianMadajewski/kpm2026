from manim_slides import Slide
from common import *


class Podsumowanie(Slide):
    """Cztery najważniejsze wnioski + pętla z tytułu: p(x,x) >= 0, metryka d(x,x) = 0, p(x*,x*) = 0."""

    def construct(self):
        O = KOLOR_CZESCIOWA
        B = KOLOR_METRYKA
        FS = 31

        naglowek = Tex(r"Podsumowanie", font_size=48)
        self.play(FadeIn(naglowek))
        self.next_slide()
        self.play(naglowek.animate.scale(44 / 48).to_edge(UP, buff=0.4), run_time=1.0)

        # ---- Cztery wnioski ----
        def punkt_listy(tekst):
            t = Tex(tekst, font_size=FS, tex_environment="flushleft")
            kropka = Dot(radius=0.045).move_to(t.get_corner(UL) + 0.25 * LEFT + 0.14 * DOWN)
            return VGroup(kropka, t)

        wnioski = VGroup(
            punkt_listy(r"Metryka częściowa dopuszcza $p(x,x)\ge 0$,\\"
                        r"czyli mierzy, jak słabo określony jest punkt."),
            punkt_listy(r"Metryki to dokładnie te metryki częściowe,\\w których $p(x,x)=0$."),
            punkt_listy(r"Topologia $\tau_p$ jest $T_0$, ale nie musi być $T_1$,\\"
                        r"a granice ciągów nie muszą być jednoznaczne."),
            punkt_listy(r"Zupełność wybiera granicę z $p(x,x)=\lim p(x_n,x_m)$,\\"
                        r"a punkt stały kontrakcji jest w pełni określony."),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        wnioski.next_to(naglowek, DOWN, buff=0.6).to_edge(LEFT, buff=0.6)

        # ---- Pętla z tytułu, po prawej ----
        srodek = np.array([4.6, 0.6, 0])
        punkt = Dot(srodek, radius=0.09)
        etykieta_x = MathTex("x", font_size=36).next_to(punkt, DOWN, buff=0.15)
        petla = Arc(radius=0.35, start_angle=-PI / 2 + 0.45, angle=2 * PI - 0.9,
                    arc_center=srodek + 0.42 * UP, color=O).add_tip(tip_length=0.15)
        wzor_p = MathTex(r"p(x,x)\ge 0", font_size=38, color=O).next_to(petla, UP, buff=0.3)

        # 1. Pierwszy wniosek, potem rysunek z pętlą: p(x,x) >= 0.
        self.play(FadeIn(wnioski[0], shift=0.2 * RIGHT))
        self.next_slide()
        self.play(FadeIn(punkt, scale=0.5), FadeIn(etykieta_x), Create(petla), FadeIn(wzor_p))
        self.next_slide()

        # 2. Metryki: pętla na niebiesko i d(x,x) = 0.
        self.play(FadeIn(wnioski[1], shift=0.2 * RIGHT))
        wzor_0 = MathTex(r"d(x,x)=0", font_size=38, color=B).move_to(wzor_p)
        self.play(petla.animate.set_color(B), FadeTransform(wzor_p, wzor_0), run_time=0.8)
        self.next_slide()

        # 3. Topologia: wracamy do ogólnej metryki częściowej.
        wzor_p2 = MathTex(r"p(x,x)\ge 0", font_size=38, color=O).move_to(wzor_0)
        self.play(FadeIn(wnioski[2], shift=0.2 * RIGHT),
                  petla.animate.set_color(O), FadeTransform(wzor_0, wzor_p2), run_time=0.8)
        self.next_slide()

        # 4. Punkt stały: pętla niebieska, p(x*,x*) = 0.
        self.play(FadeIn(wnioski[3], shift=0.2 * RIGHT))
        self.next_slide()
        etykieta_xs = MathTex(r"x^*", font_size=36).move_to(etykieta_x)
        wzor_k = MathTex(r"p(x^*,x^*)=0", font_size=38, color=B).move_to(wzor_p2)
        self.play(petla.animate.set_color(B), FadeTransform(wzor_p2, wzor_k),
                  FadeTransform(etykieta_x, etykieta_xs), run_time=1.0)
        self.play(Flash(punkt, color=B, line_length=0.25, flash_radius=0.3))
        self.next_slide()


class Literatura(Slide):
    """Literatura."""

    def construct(self):
        naglowek = Tex(r"Literatura", font_size=44).to_edge(UP, buff=0.4)
        pozycje = [
            r"S.\,G.~Matthews, \emph{Metric domains for completeness},\\"
            r"praca doktorska, University of Warwick, 1985.",
            r"S.\,G.~Matthews, \emph{Partial metric topology},\\"
            r"Annals of the New York Academy of Sciences 728 (1994), 183--197.",
            r"M.~Bukatin, R.~Kopperman, S.\,G.~Matthews, H.~Pajoohesh, \emph{Partial metric spaces},\\"
            r"The American Mathematical Monthly 116 (2009), no.~8, 708--718.",
            r"G.~Kahn, \emph{The semantics of a simple language for parallel programming},\\"
            r"Information Processing 74 (Proc.\ IFIP Congress), North-Holland, 1974, 471--475.",
            r"S.\,G.~Matthews, \texttt{partialmetric.org} (\texttt{dcs.warwick.ac.uk/pmetric}).",
        ]
        wiersze = VGroup()
        for i, t in enumerate(pozycje, start=1):
            nr = Tex(rf"[{i}]", font_size=28, color=KOLOR_DRUGORZEDNY)
            tekst = VGroup(*[MathTex(r"\text{" + linia + "}", font_size=28) for linia in t.split(r"\\")])
            tekst.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            wiersz = VGroup(nr, tekst).arrange(RIGHT, buff=0.25, aligned_edge=UP)
            wiersze.add(wiersz)
        wiersze.arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        wiersze.next_to(naglowek, DOWN, buff=0.5)
        if wiersze.width > 13:
            wiersze.scale_to_fit_width(13)
        wiersze.set_x(0)

        self.play(FadeIn(naglowek))
        self.play(LaggedStart(*[FadeIn(w, shift=0.2 * RIGHT) for w in wiersze], lag_ratio=0.2), run_time=2.0)
        self.next_slide()


class Podziekowania(Slide):
    """Podziękowania za uwagę i kod QR do repozytorium z prezentacją."""

    def construct(self):
        from pathlib import Path

        dzieki = Tex(r"Dziękuję za uwagę!", font_size=60)
        qr = SVGMobject(str(Path(__file__).parent / "grafika" / "qr_github.svg"))
        qr.set_fill(KOLOR_TEKST, 1).set_stroke(width=0).set_height(3.4)
        adres = Tex(r"\texttt{github.com/AdrianMadajewski/kpm2026}", font_size=30, color=KOLOR_DRUGORZEDNY)
        VGroup(dzieki, qr, adres).arrange(DOWN, buff=0.5)

        self.play(FadeIn(dzieki, shift=0.2 * DOWN))
        self.next_slide()
        self.play(FadeIn(qr, scale=0.9), FadeIn(adres, shift=0.2 * UP))
        self.next_slide()
