from manim_slides import Slide
from common import *


class PrzykladMax(Slide):
    """Przykład X = [0,∞), p = max, z intuicją p(x,x) jako miary nieokreśloności."""

    def construct(self):
        naglowek = Tex(r"Przykład", font_size=44).to_edge(UP, buff=0.4)

        # Krok 1: przykład.
        wzor = MathTex(r"X\coloneqq[0,\infty),\qquad p(x,y)\coloneqq\max\{x,y\}", font_size=40)
        wzor.next_to(naglowek, DOWN, buff=0.45)
        szczegol = MathTex(r"\text{w szczególności } p(x,x) = x", font_size=34, color=KOLOR_DRUGORZEDNY)
        szczegol.next_to(wzor, DOWN, buff=0.25)
        self.play(FadeIn(naglowek))
        self.play(FadeIn(wzor, shift=0.2 * DOWN))
        self.play(FadeIn(szczegol))
        self.next_slide()

        # Krok 1a: sprawdzenie aksjomatów (P1)–(P4).
        def wiersz(nazwa, *tex):
            return VGroup(
                Tex(nazwa, font_size=30, color=KOLOR_DRUGORZEDNY),
                MathTex(*tex, font_size=34),
            ).arrange(RIGHT, buff=0.3)

        a1 = wiersz(r"(P1)", r"x=\max\{x,y\}=y \iff x=y")
        a2 = wiersz(r"(P2)", r"x\le\max\{x,y\}")
        a3 = wiersz(r"(P3)", r"\max\{x,y\}=\max\{y,x\}")
        a4 = wiersz(r"(P4)", r"\max\{x,z\}\le\max\{x,y\}+\max\{y,z\}-y")
        aks = VGroup(a1, a2, a3, a4).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        aks.next_to(szczegol, DOWN, buff=0.5).to_edge(LEFT, buff=1.2)

        for a in (a1, a2, a3):
            self.play(FadeIn(a, shift=0.2 * RIGHT), run_time=0.6)
        self.next_slide()

        self.play(FadeIn(a4, shift=0.2 * RIGHT))
        self.next_slide()

        bso = Tex(r"Bez straty ogólności $\max\{x,z\}=x$. Wtedy", font_size=32)
        rach = MathTex(
            r"\max\{x,y\}+\max\{y,z\}-y", r"\ge", r"x+y-y", r"=", r"x", r"=", r"\max\{x,z\}",
            font_size=34,
        )
        bo = MathTex(r"\text{bo } \max\{x,y\}\ge x \text{ oraz } \max\{y,z\}\ge y.",
                     font_size=30, color=KOLOR_DRUGORZEDNY)
        dowod = VGroup(bso, rach, bo).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        dowod.next_to(aks, DOWN, buff=0.45).align_to(aks, LEFT).shift(0.6 * RIGHT)
        self.play(FadeIn(bso))
        self.play(FadeIn(rach[:3]))
        self.play(FadeIn(bo))
        self.play(FadeIn(rach[3:]))
        ptaszek = MathTex(r"\checkmark", font_size=44, color=KOLOR_METRYKA).next_to(a4, RIGHT, buff=0.4)
        self.play(FadeIn(ptaszek, scale=1.5))
        self.next_slide()
        self.play(FadeOut(VGroup(aks, dowod, ptaszek)))

        # Krok 2: punkt x jako przedział [0, x].
        os = NumberLine(x_range=[0, 5, 1], length=10, include_numbers=True,
                        font_size=28, include_tip=False).shift(0.2 * DOWN)
        POD = 0.75 * DOWN  # odsunięcie odcinków pod oś (poniżej liczb)

        x = ValueTracker(3.0)
        kropka = always_redraw(lambda: Dot(os.n2p(x.get_value()), radius=0.08))
        etyk_x = always_redraw(lambda: MathTex("x", font_size=34).next_to(kropka, UP, buff=0.15))
        odcinek = always_redraw(lambda: Line(
            os.n2p(0) + POD, os.n2p(max(x.get_value(), 1e-3)) + POD,
            color=KOLOR_SAMO, stroke_width=9))
        wartosc = always_redraw(lambda: VGroup(
            MathTex(r"p(x,x) =", font_size=34, color=KOLOR_SAMO),
            DecimalNumber(x.get_value(), num_decimal_places=2, font_size=34, color=KOLOR_SAMO),
        ).arrange(RIGHT, buff=0.15).next_to(os.n2p(0) + POD, DOWN, buff=0.35, aligned_edge=LEFT))
        opis = Tex(r"wiemy tylko, że wartość leży w $[0,x]$",
                   font_size=32).next_to(os, DOWN, buff=1.8)
        dopisek = Tex(r"(to tak naprawdę przedziały $[0,x]$)", font_size=28,
                      color=KOLOR_DRUGORZEDNY).next_to(opis, DOWN, buff=0.15)

        self.play(Create(os))
        self.play(FadeIn(kropka), FadeIn(etyk_x))
        self.play(Create(odcinek), FadeIn(wartosc))
        self.play(FadeIn(opis), FadeIn(dopisek))
        self.next_slide()

        # Odcinek się kurczy: coraz lepiej określony punkt.
        self.play(x.animate.set_value(0.8), run_time=2)
        self.play(x.animate.set_value(0.0), run_time=1.2)
        okreslony = Tex(r"w pełni określony", font_size=32, color=KOLOR_METRYKA)
        okreslony.next_to(os.n2p(0), UP, buff=0.65).shift(0.6 * RIGHT)
        self.play(FadeOut(odcinek), FadeIn(okreslony, shift=0.2 * DOWN))
        self.next_slide()

        # Krok 3: odległość dwóch punktów.
        self.play(FadeOut(VGroup(kropka, etyk_x, wartosc, opis, dopisek, okreslony)))
        xa, ya = 1.5, 3.5
        dx = Dot(os.n2p(xa), radius=0.08)
        dy = Dot(os.n2p(ya), radius=0.08)
        ex = MathTex("x", font_size=34).next_to(dx, UP, buff=0.15)
        ey = MathTex("y", font_size=34).next_to(dy, UP, buff=0.15)
        odc_x = Line(os.n2p(0) + POD, os.n2p(xa) + POD, color=KOLOR_SAMO, stroke_width=9)
        odc_y = Line(os.n2p(0) + 1.6 * POD, os.n2p(ya) + 1.6 * POD, color=KOLOR_SAMO, stroke_width=9)
        ex_odc = MathTex(r"[0,x]", font_size=30, color=KOLOR_SAMO).next_to(odc_x, RIGHT, buff=0.2)
        ey_odc = MathTex(r"[0,y]", font_size=30, color=KOLOR_SAMO).next_to(odc_y, RIGHT, buff=0.2)
        self.play(FadeIn(dx), FadeIn(dy), FadeIn(ex), FadeIn(ey))
        self.play(Create(odc_x), FadeIn(ex_odc), Create(odc_y), FadeIn(ey_odc))
        self.next_slide()

        NAD = 0.7 * UP
        otoczka = Line(os.n2p(0) + NAD, os.n2p(ya) + NAD, color=KOLOR_CZESCIOWA, stroke_width=9)
        klamra = Brace(otoczka, UP, color=KOLOR_CZESCIOWA, buff=0.1)
        podpis = MathTex(r"p(x,y) = \max\{x,y\}", font_size=34,
                         color=KOLOR_CZESCIOWA).next_to(klamra, UP, buff=0.1)
        opis3 = Tex(r"najmniejszy przedział zawierający $[0,x]$ i $[0,y]$",
                    font_size=32).move_to(szczegol)
        self.play(FadeOut(szczegol))
        self.play(Create(otoczka), GrowFromCenter(klamra), FadeIn(podpis))
        self.play(FadeIn(opis3))
        self.next_slide()

        p2 = Tex(r"$[0,x]\subseteq[0,y]$, więc $p(x,y)\ge p(x,x)$ \quad (P2)",
                 font_size=32).next_to(odc_y, DOWN, buff=0.5).set_x(0)
        self.play(FadeIn(p2, shift=0.2 * UP))
        self.next_slide()

        # Krok 4: morał.
        self.play(FadeOut(p2))
        moral = VGroup(
            Tex(r"$p(x,x)>0$ \quad --- element niedookreślony", font_size=34),
            Tex(r"$p(x,x)=0$ \quad --- element w pełni określony", font_size=34, color=KOLOR_METRYKA),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(moral[0], shift=0.2 * UP))
        self.play(FadeIn(moral[1], shift=0.2 * UP))
        self.next_slide()
