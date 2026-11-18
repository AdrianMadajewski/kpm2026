from manim_slides import Slide
from common import *
import numpy as np


class PrzestrzenMetryczna(Slide):
    def construct(self):
        naglowek = Tex(r"Przestrzeń metryczna", font_size=44).to_edge(UP, buff=0.4)

        # --- Lewa kolumna: definicja ---------------------------------------
        wstep = VGroup(
            Tex(r"Metryka na zbiorze $X$ to funkcja", font_size=32),
            MathTex(r"d\colon X\times X\to[0,\infty)", font_size=34),
            Tex(r"taka, że dla $x,y,z\in X$", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)

        def aksjomat(nazwa, wzor):
            return VGroup(
                Tex(nazwa, font_size=30, color=KOLOR_DRUGORZEDNY),
                MathTex(wzor, font_size=34),
            ).arrange(RIGHT, buff=0.3)

        m1 = aksjomat(r"(M1)", r"d(x,y)=0 \iff x=y")
        m2 = aksjomat(r"(M2)", r"d(x,y)=d(y,x)")
        m3 = aksjomat(r"(M3)", r"d(x,z)\le d(x,y)+d(y,z)")
        aksjomaty = VGroup(m1, m2, m3).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        nazwa = VGroup(
            Tex(r"Parę $(X,d)$ nazywamy", font_size=32),
            Tex(r"\emph{przestrzenią metryczną}.", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        lewa = VGroup(wstep, aksjomaty, nazwa).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        definicja = blok(lewa, "Definicja")
        definicja.to_edge(LEFT, buff=0.4).shift(0.2 * DOWN)

        # --- Prawa kolumna: ilustracja w R^2 --------------------------------
        ax = Axes(
            x_range=[0, 4, 1], y_range=[0, 3, 1],
            x_length=5.2, y_length=3.9,
            tips=False,
            axis_config={"include_numbers": True, "font_size": 24},
        ).to_edge(RIGHT, buff=0.7).shift(0.35 * UP)

        px = np.array([1.0, 1.0])
        py = ValueTracker(3.0), ValueTracker(1.5)

        def P(u):  # współrzędne -> punkt na ekranie
            return ax.c2p(u[0], u[1])

        def wsp_y():
            return np.array([py[0].get_value(), py[1].get_value()])

        kropka_x = Dot(P(px), radius=0.07).set_z_index(10)
        etyk_x = MathTex("x", font_size=32).next_to(kropka_x, DL, buff=0.08)
        kropka_y = always_redraw(lambda: Dot(P(wsp_y()), radius=0.07).set_z_index(10))
        etyk_y = always_redraw(lambda: MathTex("y", font_size=32).next_to(P(wsp_y()), UR, buff=0.08))
        odc_xy = always_redraw(lambda: Line(P(px), P(wsp_y()), color=KOLOR_METRYKA, stroke_width=5))

        wartosc = VGroup(
            MathTex(r"d(x,y) =", font_size=34, color=KOLOR_METRYKA),
            DecimalNumber(0, num_decimal_places=2, font_size=34, color=KOLOR_METRYKA),
        ).arrange(RIGHT, buff=0.15).next_to(ax, DOWN, buff=0.35)
        wartosc[1].add_updater(lambda m: m.set_value(np.linalg.norm(wsp_y() - px)))

        # Krok 1: definicja i przestrzeń.
        self.play(FadeIn(naglowek))
        self.next_slide()
        definicja[0].become(tlo_dla(definicja, wstep))
        self.add(definicja[0], definicja[1])
        # Definicja razem z rysunkiem; d: X x X -> [0, inf) na niebiesko.
        wstep[1].set_color(KOLOR_METRYKA)
        self.play(FadeIn(wstep, shift=0.2 * RIGHT), Create(ax))
        self.play(FadeIn(kropka_x), FadeIn(etyk_x), FadeIn(kropka_y), FadeIn(etyk_y))
        self.play(Create(odc_xy), FadeIn(wartosc))
        self.next_slide()

        # Krok 2: (M1) — y dojeżdża do x, odległość spada do zera.
        self.play(dopasuj_ramke(definicja, wstep, m1))
        m1[1].set_color(KOLOR_METRYKA)
        self.play(FadeIn(m1, shift=0.2 * RIGHT), wstep[1].animate.set_color(KOLOR_TEKST))
        self.play(py[0].animate.set_value(px[0]), py[1].animate.set_value(px[1]), run_time=2.5)
        self.wait(0.5)
        self.play(py[0].animate.set_value(3.0), py[1].animate.set_value(1.5), run_time=1.5)
        self.next_slide()

        # Krok 3: (M2) — strzałki w obie strony mają tę samą długość.
        self.play(dopasuj_ramke(definicja, wstep, m1, m2))
        m2[1].set_color(KOLOR_METRYKA)
        self.play(FadeIn(m2, shift=0.2 * RIGHT), m1[1].animate.set_color(KOLOR_TEKST))
        yv = wsp_y()
        kier = (yv - px) / np.linalg.norm(yv - px)
        normal = np.array([-kier[1], kier[0]]) * 0.18
        tam = Arrow(P(px + normal), P(yv + normal), buff=0.1, color=KOLOR_METRYKA, stroke_width=4)
        z_pow = Arrow(P(yv - normal), P(px - normal), buff=0.1, color=KOLOR_METRYKA, stroke_width=4)
        e_tam = MathTex(r"d(x,y)", font_size=28, color=KOLOR_METRYKA).next_to(tam.get_center(), UL, buff=0.15)
        e_zpow = MathTex(r"d(y,x)", font_size=28, color=KOLOR_METRYKA).next_to(z_pow.get_center(), DR, buff=0.15)
        self.play(FadeOut(odc_xy), GrowArrow(tam), FadeIn(e_tam))
        self.play(GrowArrow(z_pow), FadeIn(e_zpow))
        self.next_slide()

        # Krok 4: (M3) — trójkąt i „rozprostowanie” dwóch boków.
        self.play(FadeOut(VGroup(tam, z_pow, e_tam, e_zpow)), FadeOut(wartosc))
        self.play(dopasuj_ramke(definicja, wstep, m1, m2, m3))
        m3[1].set_color(KOLOR_METRYKA)
        self.play(FadeIn(m3, shift=0.2 * RIGHT), m2[1].animate.set_color(KOLOR_TEKST))
        pz = np.array([2.0, 2.8])
        kropka_z = Dot(P(pz), radius=0.07).set_z_index(10)
        etyk_z = MathTex("z", font_size=32).next_to(kropka_z, UP, buff=0.1)
        bok_xy = Line(P(px), P(yv), color=KOLOR_METRYKA, stroke_width=5)
        bok_yz = Line(P(yv), P(pz), color=KOLOR_METRYKA, stroke_width=5)
        bok_xz = Line(P(px), P(pz), color=KOLOR_TEKST, stroke_width=5)
        self.play(FadeIn(kropka_z), FadeIn(etyk_z))
        self.play(Create(bok_xz))
        self.play(Create(bok_xy), Create(bok_yz))

        # Porównanie długości: boki „zjeżdżają” pod wykres i układają się poziomo.
        jedn = ax.x_axis.unit_size
        l_xz = np.linalg.norm(pz - px)
        l1 = np.linalg.norm(yv - px)
        l2 = np.linalg.norm(pz - yv)
        start = ax.c2p(0, 0) + 0.9 * DOWN + 0.3 * RIGHT
        pasek0 = Line(start, start + l_xz * jedn * RIGHT, color=KOLOR_TEKST, stroke_width=6)
        start1 = start + 0.55 * DOWN
        pasek1 = Line(start1, start1 + l1 * jedn * RIGHT, color=KOLOR_METRYKA, stroke_width=6)
        pasek2 = Line(start1 + l1 * jedn * RIGHT, start1 + (l1 + l2) * jedn * RIGHT,
                      color=KOLOR_METRYKA, stroke_width=6)
        e0 = MathTex(r"d(x,z)", font_size=28).next_to(pasek0, LEFT, buff=0.2)
        e1 = MathTex(r"d(x,y)+d(y,z)", font_size=28, color=KOLOR_METRYKA).next_to(pasek1, LEFT, buff=0.2)
        k0, k1, k2 = bok_xz.copy(), bok_xy.copy(), bok_yz.copy()
        self.play(Transform(k0, pasek0), FadeIn(e0), run_time=1.5)
        self.play(Transform(k1, pasek1), run_time=1.2)
        self.play(Transform(k2, pasek2), FadeIn(e1), run_time=1.2)
        # Pionowa kreska na końcu krótszego paska pokazuje nadwyżkę.
        znacznik = DashedLine(pasek0.get_end() + 0.15 * UP, pasek0.get_end() + 0.7 * DOWN,
                              color=KOLOR_DRUGORZEDNY, stroke_width=2)
        self.play(Create(znacznik))
        self.play(Indicate(m3[1], color=KOLOR_METRYKA, scale_factor=1.1))
        self.next_slide()

        # Krok 6: nazwa przestrzeni.
        self.play(m3[1].animate.set_color(KOLOR_TEKST), dopasuj_ramke(definicja, wstep, m1, m2, m3, nazwa))
        self.play(FadeIn(nazwa, shift=0.2 * RIGHT))
        self.next_slide()
