from manim_slides import Slide
from common import *
import numpy as np


def kula(srodek_ekran, promien, kolor=KOLOR_METRYKA, wypelnienie=0.15):
    """Kula otwarta w R^2: wypełnione koło z przerywanym brzegiem."""
    wnetrze = Circle(radius=promien, stroke_width=0).set_fill(kolor, wypelnienie)
    brzeg = DashedVMobject(Circle(radius=promien, color=kolor, stroke_width=3), num_dashes=40)
    return VGroup(wnetrze, brzeg).move_to(srodek_ekran)


def przygotuj():
    """Nagłówek, osie i pomocnicze funkcje wspólne dla obu scen."""
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

    def kolumna(*wiersze, rodzaj="Definicja"):
        g = VGroup(*wiersze).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        return blok(g, rodzaj).to_edge(LEFT, buff=0.4).shift(0.2 * DOWN)
    return naglowek, ax, J, P, kolumna


class TopologiaMetryczna(Slide):
    def construct(self):
        naglowek, ax, J, P, kolumna = przygotuj()

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

        # Tytuł.
        self.play(FadeIn(naglowek))
        self.next_slide()

        # Podstawowe pytania o topologię — każde na osobne kliknięcie.
        pytania = VGroup(
            Tex(r"1. Jak wyglądają zbiory otwarte?", font_size=38),
            Tex(r"2. Co możemy powiedzieć o zbieżności?", font_size=38),
            Tex(r"3. Jakie aksjomaty oddzielania spełnia nasza przestrzeń?", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(0.2 * DOWN)
        for pyt in pytania:
            self.play(FadeIn(pyt, shift=0.2 * RIGHT))
            self.next_slide()
        self.play(FadeOut(pytania))

        # Definicja kuli na środku ekranu.
        cel_tekst1 = tekst1.copy()
        tekst1.move_to(ORIGIN)
        self.play(FadeIn(tekst1))
        self.next_slide()

        # Definicja na lewo, wykres z kulą po prawej.
        self.play(Transform(tekst1, cel_tekst1))
        self.play(Create(ax))
        self.play(FadeIn(k1), FadeIn(d1), FadeIn(e1), Create(promien), FadeIn(etyk_eps))
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
        self.play(FadeIn(tekst2, shift=0.2 * RIGHT), FadeIn(U_tlo), Create(U), FadeIn(etyk_U))
        self.play(LaggedStart(*[FadeIn(m) for m in male_kule], lag_ratio=0.4))
        self.play(FadeIn(ruch))
        self.play(t.animate.set_value(1.30), run_time=3, rate_func=smooth)
        self.next_slide()

        # ---------------- Krok 3: zbieżność ----------------
        tekst3 = kolumna(
            Tex(r"Ciąg $(x_n)_{n\in\mathbb{N}}\subset X$ jest zbieżny do $a$, gdy", font_size=32),
            MathTex(r"\lim_{n\to\infty} d(a,x_n)=0.", font_size=34),
        )
        komentarz3 = VGroup(
            Tex(r"Każda kula wokół $a$ zawiera", font_size=32),
            Tex(r"prawie wszystkie wyrazy ciągu.", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(tekst3, DOWN, buff=0.4).align_to(tekst3, LEFT)
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
        self.play(FadeIn(tekst3, shift=0.2 * RIGHT), FadeIn(da), FadeIn(ea))
        self.play(FadeIn(komentarz3))
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


class Oddzielanie(Slide):
    """Przypomnienie aksjomatów oddzielania i własność Hausdorffa."""
    def construct(self):
        naglowek, ax, J, P, kolumna = przygotuj()
        self.add(naglowek)

        # ---------------- Krok 4: Hausdorff ----------------
        tekst4 = kolumna(
            Tex(r"Dla $x\neq y$ kule o promieniu $\tfrac{1}{2}d(x,y)$", font_size=32),
            Tex(r"wokół $x$ i wokół $y$ są rozłączne.", font_size=32),
            rodzaj="Stwierdzenie",
        )
        wniosek4 = VGroup(
            Tex(r"Przestrzeń metryczna jest Hausdorffa ($T_2$),", font_size=32, color=KOLOR_METRYKA),
            Tex(r"więc granica ciągu jest jedyna.", font_size=32, color=KOLOR_METRYKA),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        wniosek4.next_to(tekst4, DOWN, buff=0.4).align_to(tekst4, LEFT)
        hx, hy = np.array([1.1, 1.3]), np.array([2.9, 1.9])
        r = np.linalg.norm(hy - hx) / 2
        kx, ky = kula(P(hx), r * J), kula(P(hy), r * J)
        dx, dy = Dot(P(hx), radius=0.07), Dot(P(hy), radius=0.07)
        ex = MathTex("x", font_size=30).next_to(dx, DOWN, buff=0.12)
        ey = MathTex("y", font_size=30).next_to(dy, DOWN, buff=0.12)
        odc = DashedLine(P(hx), P(hy), color=KOLOR_DRUGORZEDNY, stroke_width=2)


        # ---------------- Przypomnienie: aksjomaty oddzielania ----------------
        def panel(nazwa, opis):
            ramka = RoundedRectangle(width=3.7, height=2.1, corner_radius=0.15,
                                     color=GRAY_C, stroke_width=2)
            px_ = Dot(ramka.get_center() + 0.75 * LEFT, radius=0.07)
            py_ = Dot(ramka.get_center() + 0.75 * RIGHT, radius=0.07)
            lx = MathTex("x", font_size=28).next_to(px_, DOWN, buff=0.1)
            ly = MathTex("y", font_size=28).next_to(py_, DOWN, buff=0.1)
            tyt = MathTex(nazwa, font_size=36).next_to(ramka, UP, buff=0.15)
            tekst = Tex(opis, font_size=26).next_to(ramka, DOWN, buff=0.2)
            return VGroup(ramka, px_, py_, lx, ly, tyt, tekst)

        def owal(srodek, szer, kolor):
            o = Ellipse(width=szer, height=1.3)
            return VGroup(
                o.copy().set_stroke(width=0).set_fill(kolor, 0.15),
                DashedVMobject(o.copy().set_stroke(kolor, 2.5), num_dashes=30),
            ).move_to(srodek)

        p0 = panel(r"T_0", r"jeden z punktów ma otoczenie,\\które nie zawiera drugiego")
        p1 = panel(r"T_1", r"każdy z punktów ma otoczenie,\\które nie zawiera drugiego")
        p2 = panel(r"T_2", r"punkty mają\\rozłączne otoczenia")
        panele = VGroup(p0, p1, p2).arrange(RIGHT, buff=0.45)
        wstep_osd = Tex(r"Przestrzeń topologiczna $X$ spełnia aksjomat \dots, gdy dla dowolnych $x\neq y$",
                        font_size=28)
        zawartosc = VGroup(wstep_osd, panele).arrange(DOWN, buff=0.35)
        def_osd = blok(zawartosc, "Definicja").move_to(0.15 * UP)
        implikacje = MathTex(r"T_2 \;\Longrightarrow\; T_1 \;\Longrightarrow\; T_0", font_size=40)
        implikacje.next_to(def_osd, DOWN, buff=0.3)

        def srodek(p):
            return p[0].get_center()

        o0 = owal(srodek(p0) + 0.75 * LEFT, 1.2, KOLOR_METRYKA)
        o1a = owal(srodek(p1) + 0.5 * LEFT, 1.6, KOLOR_METRYKA)
        o1b = owal(srodek(p1) + 0.5 * RIGHT, 1.6, KOLOR_CZESCIOWA)
        o2a = owal(srodek(p2) + 0.5 * LEFT, 1.6, KOLOR_METRYKA)
        o2b = owal(srodek(p2) + 0.5 * RIGHT, 1.6, KOLOR_CZESCIOWA)

        def_osd[0].become(tlo_dla(def_osd, wstep_osd))
        self.play(FadeIn(def_osd[0]), FadeIn(def_osd[1]), FadeIn(wstep_osd))
        self.next_slide()
        self.play(dopasuj_ramke(def_osd, wstep_osd, p0))
        self.play(FadeIn(VGroup(*p0[:6])))
        self.play(FadeIn(o0), FadeIn(p0[6]))
        self.next_slide()
        self.play(dopasuj_ramke(def_osd, wstep_osd, p0, p1))
        self.play(FadeIn(VGroup(*p1[:6])))
        self.play(FadeIn(o1a), FadeIn(o1b), FadeIn(p1[6]))
        self.next_slide()
        self.play(dopasuj_ramke(def_osd, wstep_osd, p0, p1, p2))
        self.play(FadeIn(VGroup(*p2[:6])))
        self.play(FadeIn(o2a), FadeIn(o2b))
        # Owale odsuwają się i zwężają, aż przestaną się przecinać.
        self.play(
            o2a.animate.stretch_to_fit_width(1.3).move_to(srodek(p2) + 0.75 * LEFT),
            o2b.animate.stretch_to_fit_width(1.3).move_to(srodek(p2) + 0.75 * RIGHT),
            run_time=1.2,
        )
        self.play(FadeIn(p2[6]))
        self.next_slide()
        self.play(FadeIn(implikacje, shift=0.2 * UP))
        self.next_slide()
        self.play(FadeOut(VGroup(def_osd, panele, o0, o1a, o1b, o2a, o2b, implikacje)))
        self.play(FadeIn(ax))
        self.play(FadeIn(tekst4, shift=0.2 * RIGHT), FadeIn(dx), FadeIn(dy), FadeIn(ex), FadeIn(ey))
        self.play(Create(odc))
        self.play(GrowFromCenter(kx), GrowFromCenter(ky))
        self.play(FadeIn(wniosek4))
        ptaszki = MathTex(r"T_0\ \checkmark \qquad T_1\ \checkmark \qquad T_2\ \checkmark",
                          font_size=36, color=KOLOR_METRYKA)
        ptaszki.next_to(wniosek4, DOWN, buff=0.4).align_to(wniosek4, LEFT)
        self.play(FadeIn(ptaszki, shift=0.2 * UP))
        self.next_slide()

