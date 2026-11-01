from manim_slides import Slide
from common import *


TYTUL_SEKCJI = r"Topologia w przestrzeni częściowo metrycznej"


class PytaniaCzesciowa(Slide):
    """Te same trzy pytania co w sekcji 1 — teraz dla metryki częściowej."""

    def construct(self):
        naglowek = Tex(TYTUL_SEKCJI, font_size=44).to_edge(UP, buff=0.4)
        self.play(FadeIn(naglowek))
        self.next_slide()

        pytania = VGroup(
            Tex(r"1. Jak wyglądają zbiory otwarte?", font_size=38),
            Tex(r"2. Co możemy powiedzieć o zbieżności?", font_size=38),
            Tex(r"3. Jakie aksjomaty oddzielania spełnia nasza przestrzeń?", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(0.2 * DOWN)
        for pyt in pytania:
            self.play(FadeIn(pyt, shift=0.2 * RIGHT))
            self.next_slide()


class KulaCzesciowa(Slide):
    """Kula w metryce częściowej: od B_d do B_p, potem rachunek dla p = max."""

    def construct(self):
        naglowek = Tex(TYTUL_SEKCJI, font_size=44).to_edge(UP, buff=0.4)
        self.add(naglowek)

        FS = 40
        kula_d = MathTex(
            r"B_d(x,\varepsilon)", r"\coloneqq", r"\{y\in X :", r"d(x,y)", r"<", r"\varepsilon\}",
            font_size=FS,
        ).move_to(1.6 * UP)
        kula_p = MathTex(
            r"B_p(x,\varepsilon)", r"\coloneqq", r"\{y\in X :", r"p(x,y)", r"<", r"p(x,x)+", r"\varepsilon\}",
            font_size=FS,
        ).move_to(1.6 * UP)
        podpis_d = Tex(r"kula w przestrzeni metrycznej", font_size=30, color=KOLOR_DRUGORZEDNY)
        podpis_d.next_to(kula_d, DOWN, buff=0.3)
        podpis_p = Tex(r"kula w przestrzeni częściowo metrycznej", font_size=30, color=KOLOR_DRUGORZEDNY)
        podpis_p.next_to(kula_p, DOWN, buff=0.3)

        # Krok 1: przypomnienie kuli metrycznej.
        self.play(FadeIn(kula_d, shift=0.2 * DOWN), FadeIn(podpis_d))
        self.next_slide()

        # Krok 2: podświetl -> zamień tylko różniące się znaki -> zgaś.
        self.play(kula_d[0].animate.set_color(KOLOR_CZESCIOWA),
                  kula_d[3].animate.set_color(KOLOR_CZESCIOWA), run_time=0.7)
        self.wait(0.3)
        for i in (0, 3, 5):
            kula_p[i].set_color(KOLOR_CZESCIOWA)
        self.play(TransformMatchingShapes(kula_d, kula_p), run_time=1.3)
        self.play(FadeOut(podpis_d, shift=0.4 * LEFT), run_time=0.5)
        self.play(FadeIn(podpis_p, shift=0.4 * RIGHT), run_time=0.6)
        self.wait(0.5)
        self.play(*[kula_p[i].animate.set_color(KOLOR_TEKST) for i in (0, 3, 5)], run_time=0.7)
        self.next_slide()

        # Krok 3: rachunek dla p = max.
        wstep = Tex(r"Dla $X\coloneqq[0,\infty)$ i $p(x,y)\coloneqq\max\{x,y\}$ mamy", font_size=34)
        r1 = MathTex(r"B_p(x,\varepsilon)", r"=\{y\ge 0 : \max\{x,y\}<x+\varepsilon\}", font_size=36)
        r2 = MathTex(r"=\{y\ge 0 : y<x+\varepsilon\}", font_size=36)
        r3 = MathTex(r"=[0,\,x+\varepsilon).", font_size=36, color=KOLOR_CZESCIOWA)
        bo = Tex(r"bo zawsze $x<x+\varepsilon$", font_size=28, color=KOLOR_DRUGORZEDNY)

        wstep.next_to(podpis_p, DOWN, buff=0.7).to_edge(LEFT, buff=1.2)
        r1.next_to(wstep, DOWN, buff=0.35).align_to(wstep, LEFT).shift(0.5 * RIGHT)
        r2.next_to(r1, DOWN, buff=0.25).align_to(r1[1], LEFT)
        r3.next_to(r2, DOWN, buff=0.25).align_to(r1[1], LEFT)
        bo.next_to(r2, RIGHT, buff=0.6)

        self.play(FadeIn(wstep))
        self.next_slide()
        self.play(FadeIn(r1, shift=0.2 * RIGHT))
        self.next_slide()
        self.play(FadeIn(r2, shift=0.2 * RIGHT), FadeIn(bo))
        self.next_slide()
        self.play(FadeIn(r3, shift=0.2 * RIGHT))
        self.wait(0.2)
        self.next_slide()


def _koniec_otwarty(punkt, kolor):
    return Circle(radius=0.08, color=kolor, stroke_width=4).set_fill(WHITE, 1).move_to(punkt).set_z_index(5)


def _koniec_domkniety(punkt, kolor):
    return Dot(punkt, radius=0.08, color=kolor).set_z_index(5)


def _kula_na_osi(os, prawy, kolor, wys):
    """Kula [0, prawy) w przykładzie max, narysowana nad osią na wysokości `wys`."""
    a, b = os.n2p(0) + wys * UP, os.n2p(prawy) + wys * UP
    return VGroup(
        Line(a, b, color=kolor, stroke_width=7).set_cap_style(CapStyleType.ROUND),
        _koniec_domkniety(a, kolor),
        _koniec_otwarty(b, kolor),
    )


class LematBaza(Slide):
    """Lemat: kule tworzą bazę topologii — treść, rysunek dla max i krótki dowód."""

    def construct(self):
        KOLOR_Y = ManimColor("#7B3FA0")

        lemat = VGroup(
            Tex(r"\textbf{Lemat.} Jeżeli $y\in B_p(x,\varepsilon)$, to istnieje $\delta>0$ takie, że", font_size=32),
            MathTex(r"B_p(y,\delta)\subset B_p(x,\varepsilon).", font_size=34),
        ).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.45)
        self.play(FadeIn(lemat, shift=0.2 * DOWN))
        self.next_slide()

        # Rysunek w przykładzie max: x = 2, eps = 1.5, y = 1, delta = 1.5.
        os = NumberLine(x_range=[0, 5, 1], length=10, include_numbers=True,
                        font_size=26, include_tip=False).move_to(0.75 * UP)
        x0, eps, y0 = 2.0, 1.5, 1.0
        delta = x0 + eps - max(x0, y0)
        kx = Dot(os.n2p(x0), radius=0.09, color=KOLOR_CZESCIOWA).set_z_index(10)
        ky = Dot(os.n2p(y0), radius=0.09, color=KOLOR_Y).set_z_index(10)
        ex = MathTex("x", font_size=30).next_to(kx, DOWN, buff=0.45)
        ey = MathTex("y", font_size=30).next_to(ky, DOWN, buff=0.45)
        kula_x = _kula_na_osi(os, x0 + eps, KOLOR_CZESCIOWA, 0.35)
        kula_y = _kula_na_osi(os, y0 + delta, KOLOR_Y, 0.7)
        e_kx = MathTex(r"B_p(x,\varepsilon)", font_size=30, color=KOLOR_CZESCIOWA).next_to(kula_x[0], RIGHT, buff=0.3)
        e_ky = MathTex(r"B_p(y,\delta)", font_size=30, color=KOLOR_Y).next_to(kula_y[0], RIGHT, buff=0.3)

        self.play(Create(os))
        self.play(FadeIn(kx), FadeIn(ex))
        self.play(FadeIn(kula_x), FadeIn(e_kx))
        self.next_slide()
        self.play(FadeIn(ky), FadeIn(ey))
        self.next_slide()
        self.play(FadeIn(kula_y), FadeIn(e_ky))
        self.next_slide()

        # Dowód.
        FS = 32
        d1 = Tex(r"\textit{Dowód.} Niech $\delta\coloneqq p(x,x)+\varepsilon-p(x,y)>0$ i $z\in B_p(y,\delta)$.", font_size=FS)
        d2 = MathTex(r"p(x,z)", r"\le", r"p(x,y)+p(y,z)", r"-p(y,y)", font_size=FS + 2)
        d3 = MathTex(r"<", r"p(x,y)+\delta", r"=", r"p(x,x)+\varepsilon,", font_size=FS + 2)
        d4 = Tex(r"czyli $z\in B_p(x,\varepsilon)$. \hfill $\blacksquare$", font_size=FS)
        dowod = VGroup(d1, d2, d3, d4).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        dowod.next_to(os, DOWN, buff=0.95).to_edge(LEFT, buff=0.8)
        d2.shift(0.6 * RIGHT)
        d3.next_to(d2, DOWN, buff=0.22).align_to(d2[1], LEFT)
        d4.next_to(d3, DOWN, buff=0.22).align_to(d1, LEFT)
        uwaga = Tex(r"(P4)", font_size=28, color=KOLOR_CZESCIOWA).next_to(d2, RIGHT, buff=0.5)

        self.play(FadeIn(d1))
        self.next_slide()
        self.play(FadeIn(d2))
        self.play(d2[3].animate.set_color(KOLOR_CZESCIOWA), FadeIn(uwaga))
        self.next_slide()
        self.play(FadeIn(d3))
        self.next_slide()
        self.play(FadeIn(d4))
        self.next_slide()

        # Wniosek.
        self.play(FadeOut(VGroup(dowod, uwaga)))
        wniosek = VGroup(
            Tex(r"Zatem kule tworzą bazę topologii $\tau_p$.", font_size=34),
            Tex(r"W przykładzie zbiory otwarte to $\emptyset$, $[0,\infty)$ oraz $[0,a)$ dla $a>0$.",
                font_size=34, color=KOLOR_CZESCIOWA),
        ).arrange(DOWN, buff=0.3).next_to(os, DOWN, buff=1.3)
        self.play(FadeIn(wniosek[0], shift=0.2 * UP))
        self.next_slide()
        self.play(FadeIn(wniosek[1], shift=0.2 * UP))
        self.wait(0.2)
        self.next_slide()
