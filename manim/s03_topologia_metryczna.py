from manim_slides import Slide
from common import *
import numpy as np


def kula(srodek_ekran, promien, kolor=KOLOR_METRYKA, wypelnienie=0.15):
    """Kula otwarta w R^2: wypełnione koło z przerywanym brzegiem."""
    wnetrze = Circle(radius=promien, stroke_width=0).set_fill(kolor, wypelnienie)
    brzeg = DashedVMobject(Circle(radius=promien, color=kolor, stroke_width=3), num_dashes=40)
    return VGroup(wnetrze, brzeg).move_to(srodek_ekran)


class TopologiaMetryczna(Slide):
    def construct(self):
        naglowek = Tex(r"Topologia w przestrzeni metrycznej", font_size=44).to_edge(UP, buff=0.4)

        ax = Axes(
            x_range=[0, 4, 1], y_range=[0, 3, 1],
            x_length=5.2, y_length=3.9,
            tips=False,
            axis_config={"include_numbers": True, "font_size": 24},
        ).to_edge(RIGHT, buff=0.7).shift(0.2 * DOWN)
        J = ax.x_axis.unit_size  # długość jednostki na ekranie (taka sama na obu osiach)

        def P(u):
            return ax.c2p(u[0], u[1])

        def kolumna(*wiersze):
            g = VGroup(*wiersze).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            return g.to_edge(LEFT, buff=0.6).shift(0.2 * DOWN)

        # ---------------- Krok 1: kula ----------------
        tekst1 = kolumna(
            Tex(r"Kula o środku $x$ i promieniu $\varepsilon>0$", font_size=32),
            MathTex(r"B_d(x,\varepsilon)\coloneqq\{y\in X : d(x,y)<\varepsilon\}", font_size=34),
        )
        x1 = np.array([1.6, 1.5])
        eps = ValueTracker(0.8)
        k1 = always_redraw(lambda: kula(P(x1), eps.get_value() * J))
        promien = always_redraw(lambda: Line(P(x1), P(x1 + np.array([eps.get_value(), 0])),
                                             color=KOLOR_METRYKA, stroke_width=3))
        etyk_eps = always_redraw(lambda: MathTex(r"\varepsilon", font_size=30, color=KOLOR_METRYKA)
                                 .next_to(promien, UP, buff=0.08))
        d1 = Dot(P(x1), radius=0.07)
        e1 = MathTex("x", font_size=30).next_to(d1, DL, buff=0.08)

        self.play(Write(naglowek))
        self.play(Create(ax))
        self.play(FadeIn(tekst1, shift=0.2 * RIGHT))
        self.play(FadeIn(k1), FadeIn(d1), Write(e1), Create(promien), Write(etyk_eps))
        self.play(eps.animate.set_value(1.2), run_time=1.2)
        self.play(eps.animate.set_value(0.4), run_time=1.2)
        self.play(eps.animate.set_value(0.8), run_time=1.0)
        self.next_slide()

        # ---------------- Krok 2: zbiór otwarty ----------------
        tekst2 = kolumna(
            Tex(r"Zbiór $U\subset X$ jest \emph{otwarty}, gdy", font_size=32),
            Tex(r"dla każdego $x\in U$ istnieje $\varepsilon>0$", font_size=32),
            Tex(r"takie, że $B_d(x,\varepsilon)\subset U$.", font_size=32),
        )
        srodek_U = np.array([2.1, 1.5])
        pa, pb = 1.5, 1.0  # półosie elipsy w jednostkach osi
        U = DashedVMobject(Ellipse(width=2 * pa * J, height=2 * pb * J, color=KOLOR_TEKST,
                                   stroke_width=3), num_dashes=50).move_to(P(srodek_U))
        U_tlo = Ellipse(width=2 * pa * J, height=2 * pb * J, stroke_width=0).set_fill(GRAY, 0.12).move_to(P(srodek_U))
        etyk_U = MathTex("U", font_size=34).move_to(P(srodek_U + np.array([pa * 0.85, pb * 0.95])))

        kat = np.linspace(0, 2 * PI, 400)
        brzeg = np.stack([srodek_U[0] + pa * np.cos(kat), srodek_U[1] + pb * np.sin(kat)], axis=1)

        def odl_do_brzegu(u):
            return np.min(np.linalg.norm(brzeg - u, axis=1))

        punkty_stale = [np.array([1.5, 1.7]), np.array([2.6, 1.1])]
        male_kule = VGroup(*[
            VGroup(kula(P(u), 0.8 * odl_do_brzegu(u) * J), Dot(P(u), radius=0.06))
            for u in punkty_stale
        ])

        t = ValueTracker(0.0)
        kierunek = np.array([1.0, 0.45]) / np.linalg.norm([1.0, 0.45])

        def ruchomy():
            return srodek_U + t.get_value() * kierunek

        ruch = always_redraw(lambda: VGroup(
            kula(P(ruchomy()), 0.8 * odl_do_brzegu(ruchomy()) * J),
            Dot(P(ruchomy()), radius=0.06),
        ))

        self.play(FadeOut(VGroup(tekst1, d1, e1, promien, etyk_eps, k1)))
        self.play(FadeIn(tekst2, shift=0.2 * RIGHT), FadeIn(U_tlo), Create(U), Write(etyk_U))
        self.play(LaggedStart(*[FadeIn(m) for m in male_kule], lag_ratio=0.4))
        self.play(FadeIn(ruch))
        self.play(t.animate.set_value(1.30), run_time=3, rate_func=smooth)
        self.next_slide()

        # ---------------- Krok 3: zbieżność ----------------
        tekst3 = kolumna(
            Tex(r"Ciąg $(x_n)_{n\in\mathbb{N}}\subset X$ jest zbieżny do $a$, gdy", font_size=32),
            MathTex(r"\lim_{n\to\infty} d(a,x_n)=0.", font_size=34),
            Tex(r"Każda kula wokół $a$ zawiera", font_size=32),
            Tex(r"prawie wszystkie wyrazy ciągu.", font_size=32),
        )
        a = np.array([2.4, 1.5])
        wyrazy = []
        for n in range(1, 16):
            r = 1.25 * 0.8 ** n
            th = 0.9 * n
            wyrazy.append(a + r * np.array([np.cos(th), np.sin(th)]))
        kropki = VGroup(*[Dot(P(u), radius=0.05, color=KOLOR_TEKST) for u in wyrazy])
        da = Dot(P(a), radius=0.07, color=KOLOR_TEKST)
        ea = MathTex("a", font_size=32).next_to(da, DL, buff=0.3)
        ea.add_background_rectangle(color=WHITE, opacity=0.85, buff=0.04)

        self.play(FadeOut(VGroup(tekst2, U, U_tlo, etyk_U, male_kule, ruch)))
        self.play(FadeIn(tekst3, shift=0.2 * RIGHT), FadeIn(da), Write(ea))
        self.play(LaggedStart(*[FadeIn(k, scale=0.5) for k in kropki], lag_ratio=0.25), run_time=2.5)

        kula_a = kula(P(a), 0.9 * J)
        self.play(FadeIn(kula_a))
        for e in [0.9, 0.45, 0.2]:
            nowa = kula(P(a), e * J)
            self.play(Transform(kula_a, nowa), run_time=0.8)
            self.play(*[
                k.animate.set_color(KOLOR_METRYKA if np.linalg.norm(u - a) < e else GRAY_B)
                for k, u in zip(kropki, wyrazy)
            ], run_time=0.6)
            self.wait(0.3)
        self.next_slide()

        # ---------------- Krok 4: Hausdorff ----------------
        tekst4 = kolumna(
            Tex(r"Dla $x\neq y$ kule o promieniu $\tfrac{1}{2}d(x,y)$", font_size=32),
            Tex(r"wokół $x$ i wokół $y$ są rozłączne.", font_size=32),
            Tex(r"Zatem granica ciągu jest jedyna.", font_size=32, color=KOLOR_METRYKA),
        )
        hx, hy = np.array([1.1, 1.3]), np.array([2.9, 1.9])
        r = np.linalg.norm(hy - hx) / 2
        kx, ky = kula(P(hx), r * J), kula(P(hy), r * J)
        dx, dy = Dot(P(hx), radius=0.07), Dot(P(hy), radius=0.07)
        ex = MathTex("x", font_size=30).next_to(dx, DOWN, buff=0.12)
        ey = MathTex("y", font_size=30).next_to(dy, DOWN, buff=0.12)
        odc = DashedLine(P(hx), P(hy), color=KOLOR_DRUGORZEDNY, stroke_width=2)

        self.play(FadeOut(VGroup(tekst3, kropki, da, ea, kula_a)))
        self.play(FadeIn(tekst4[:2], shift=0.2 * RIGHT), FadeIn(dx), FadeIn(dy), Write(ex), Write(ey))
        self.play(Create(odc))
        self.play(GrowFromCenter(kx), GrowFromCenter(ky))
        self.play(Write(tekst4[2]))
        self.next_slide()

        # ---------------- Krok 5: ciąg stały ----------------
        tekst5 = kolumna(
            MathTex(r"x_n = a \quad\text{dla } n\in\mathbb{N}", font_size=34),
            Tex(r"Ciąg stały jest zbieżny", font_size=32),
            Tex(r"\emph{tylko} do $a$.", font_size=32),
        )
        a5 = np.array([1.6, 1.5])
        b5 = np.array([3.0, 2.0])
        d5a = Dot(P(a5), radius=0.08, color=KOLOR_TEKST)
        e5a = MathTex(r"a = x_1 = x_2 = \dots", font_size=28).next_to(d5a, DOWN, buff=0.15)
        d5b = Dot(P(b5), radius=0.07)
        e5b = MathTex("b", font_size=30).next_to(d5b, UR, buff=0.08)
        kb = kula(P(b5), 0.6 * J)

        self.play(FadeOut(VGroup(tekst4, kx, ky, dx, dy, ex, ey, odc)))
        self.play(FadeIn(tekst5[0], shift=0.2 * RIGHT), FadeIn(d5a), Write(e5a))
        self.play(FadeIn(d5b), Write(e5b))
        self.play(FadeIn(kb))
        self.play(Transform(kb, kula(P(b5), 0.3 * J)))
        self.play(FadeIn(tekst5[1:], shift=0.2 * RIGHT))
        ramka = SurroundingRectangle(tekst5[1:], color=KOLOR_METRYKA, buff=0.15, corner_radius=0.08)
        self.play(Create(ramka))
        self.next_slide()
