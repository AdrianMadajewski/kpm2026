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
        self.play(*[kula_p[i].animate.set_color(KOLOR_TEKST) for i in (0, 3)], run_time=0.7)
        self.play(Indicate(kula_p[5], color=KOLOR_CZESCIOWA, scale_factor=1.15))
        self.wait(0.4)
        self.play(kula_p[5].animate.set_color(KOLOR_TEKST), run_time=0.7)
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
