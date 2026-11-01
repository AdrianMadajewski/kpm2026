from manim_slides import Slide
from common import *


def otwarty(punkt, kolor):
    """Pusty kółko oznaczające koniec otwarty."""
    return Circle(radius=0.08, color=kolor, stroke_width=4).set_fill(WHITE, 1).move_to(punkt)


def zamkniety(punkt, kolor):
    """Pełna kropka oznaczająca koniec domknięty."""
    return Dot(punkt, radius=0.08, color=kolor)


class Kule(Slide):
    def construct(self):
        naglowek = Tex(r"Topologia w przestrzeni częściowo metrycznej", font_size=44).to_edge(UP, buff=0.4)

        def os():
            return NumberLine(
                x_range=[0, 5, 1],
                length=10,
                include_numbers=True,
                font_size=28,
                include_tip=False,
            )

        os_d = os().shift(1.0 * UP)
        os_p = os().shift(1.9 * DOWN)
        opis_d = MathTex(r"d(x,y) = |x-y|", font_size=34, color=KOLOR_METRYKA)
        opis_d.next_to(os_d, UP, buff=0.55).to_edge(LEFT, buff=0.8)
        opis_p = MathTex(r"p(x,y) = \max\{x,y\}", font_size=34, color=KOLOR_CZESCIOWA)
        opis_p.next_to(os_p, UP, buff=0.55).to_edge(LEFT, buff=0.8)

        x0 = 2
        punkt_d = Dot(os_d.n2p(x0), radius=0.09, color=KOLOR_METRYKA).set_z_index(10)
        punkt_p = Dot(os_p.n2p(x0), radius=0.09, color=KOLOR_CZESCIOWA).set_z_index(10)
        etyk_d = MathTex("x", font_size=32).next_to(punkt_d, UP, buff=0.15)
        etyk_p = MathTex("x", font_size=32).next_to(punkt_p, UP, buff=0.15)

        self.add(naglowek)
        self.play(Create(os_d), Create(os_p), FadeIn(opis_d), FadeIn(opis_p))
        self.play(FadeIn(punkt_d), FadeIn(punkt_p), FadeIn(etyk_d), FadeIn(etyk_p))
        self.next_slide()

        # Kule o promieniu eps.
        eps = ValueTracker(1.5)

        def kula_d():
            e = eps.get_value()
            a, b = os_d.n2p(x0 - e), os_d.n2p(x0 + e)
            return VGroup(
                Line(a, b, color=KOLOR_METRYKA, stroke_width=7).set_cap_style(CapStyleType.ROUND),
                otwarty(a, KOLOR_METRYKA),
                otwarty(b, KOLOR_METRYKA),
            )

        def kula_p():
            e = eps.get_value()
            a, b = os_p.n2p(0), os_p.n2p(x0 + e)
            return VGroup(
                Line(a, b, color=KOLOR_CZESCIOWA, stroke_width=7).set_cap_style(CapStyleType.ROUND),
                zamkniety(a, KOLOR_CZESCIOWA),
                otwarty(b, KOLOR_CZESCIOWA),
            )

        k_d = always_redraw(kula_d)
        k_p = always_redraw(kula_p)
        wzor_kd = MathTex(r"B_d(x,\varepsilon) = (x-\varepsilon,\, x+\varepsilon)",
                          font_size=34, color=KOLOR_METRYKA)
        wzor_kd.next_to(opis_d, RIGHT, buff=1.2)
        wzor_kp = MathTex(r"B_p(x,\varepsilon) = [0,\, x+\varepsilon)",
                          font_size=34, color=KOLOR_CZESCIOWA)
        wzor_kp.next_to(opis_p, RIGHT, buff=1.2)

        licznik = VGroup(
            MathTex(r"\varepsilon =", font_size=36),
            DecimalNumber(eps.get_value(), num_decimal_places=2, font_size=36),
        ).arrange(RIGHT, buff=0.15).to_corner(DR, buff=0.5)
        licznik[1].add_updater(lambda m: m.set_value(eps.get_value()))

        self.add(k_d, k_p)
        self.bring_to_front(punkt_d, punkt_p)
        self.play(FadeIn(k_d), FadeIn(k_p), FadeIn(wzor_kd), FadeIn(wzor_kp), FadeIn(licznik))
        self.next_slide()

        # eps -> 0
        self.play(eps.animate.set_value(0.03), run_time=4, rate_func=smooth)
        self.next_slide()

        # Co zostaje: [0, x] = p(x,x).
        odcinek = Line(os_p.n2p(0), os_p.n2p(x0), color=KOLOR_CZESCIOWA,
                       stroke_width=7).set_cap_style(CapStyleType.ROUND)
        odcinek.shift(0.75 * DOWN)
        klamra = Brace(odcinek, DOWN, color=KOLOR_CZESCIOWA)
        podpis = MathTex(r"p(x,x) = x", font_size=34, color=KOLOR_CZESCIOWA).next_to(klamra, DOWN, buff=0.1)
        self.play(Create(odcinek))
        self.play(GrowFromCenter(klamra), FadeIn(podpis))
        self.next_slide()
        komentarz = Tex(r"każda kula wokół $x$ zawiera $[0,x]$", font_size=32)
        komentarz.move_to([2.4, -3.4, 0])
        self.play(FadeIn(komentarz, shift=0.2 * LEFT))
        self.wait(0.2)
        self.next_slide()
