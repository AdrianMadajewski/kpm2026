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
        B = KOLOR_METRYKA

        # Tytuł.
        self.play(FadeIn(naglowek))
        self.next_slide()

        # Podstawowe pytania o topologię — każde na osobne kliknięcie.
        pytania = VGroup(
            Tex(r"1. Jak wyglądają zbiory otwarte?", font_size=38),
            Tex(r"2. Jakie aksjomaty oddzielania spełnia nasza przestrzeń?", font_size=38),
            Tex(r"3. Co możemy powiedzieć o zbieżności?", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(0.2 * DOWN)
        for pyt in pytania:
            self.play(FadeIn(pyt, shift=0.2 * RIGHT))
            self.next_slide()
        self.play(FadeOut(pytania))

        # ---- Pomocnicze: zbiory na rysunku ----
        def plama(srodek, R, faza):
            """Punkty brzegu "nieregularnego" zbioru wokół srodek (współrzędne osi)."""
            th = np.linspace(0, 2 * PI, 240)
            r = R * (1 + 0.16 * np.sin(3 * th + faza) + 0.08 * np.cos(2 * th - faza))
            return np.stack([srodek[0] + r * np.cos(th), srodek[1] + 0.8 * r * np.sin(th)], axis=1)

        def zbior(pkt, kolor=KOLOR_TEKST, wyp=GRAY):
            ksztalt = VMobject().set_points_smoothly([P(u) for u in pkt[:-1]] + [P(pkt[0])])
            return VGroup(ksztalt.copy().set_stroke(width=0).set_fill(wyp, 0.14),
                          DashedVMobject(ksztalt.copy().set_stroke(kolor, 3), num_dashes=50))

        def odl(u, brzeg):
            return np.min(np.linalg.norm(brzeg - u, axis=1))

        # ================= Krok 1: zbiory otwarte w topologii =================
        tekst1 = kolumna(
            Tex(r"Zbiór $U\subset X$ jest \emph{otwarty}, gdy $U\in\tau$.", font_size=32),
            Tex(r"Równoważnie, dla każdego $x\in U$ istnieje", font_size=32),
            Tex(r"zbiór otwarty $V$ taki, że $x\in V\subset U$.", font_size=32),
        )
        c_U = np.array([2.0, 1.5])
        brzeg_U = plama(c_U, 1.25, 0.4)
        U = zbior(brzeg_U)
        etyk_U = MathTex("U", font_size=34).move_to(P(c_U + np.array([1.25, 0.95])))

        def otoczenie(u, faza):
            R = 0.7 * odl(u, brzeg_U) / 1.24
            return zbior(plama(u, R, faza), kolor=KOLOR_DRUGORZEDNY, wyp=GRAY_D)

        stale = [(np.array([1.35, 1.75]), 1.3), (np.array([2.55, 1.05]), 2.6)]
        male_V = VGroup(*[VGroup(otoczenie(u, f), Dot(P(u), radius=0.06)) for u, f in stale])

        t = ValueTracker(0.0)
        kier = np.array([1.0, 0.5]) / np.linalg.norm([1.0, 0.5])
        ruchomy_V = always_redraw(lambda: VGroup(
            otoczenie(c_U + t.get_value() * kier, 2.0 + 2.0 * t.get_value()),
            Dot(P(c_U + t.get_value() * kier), radius=0.06),
        ))
        etyk_x = always_redraw(lambda: MathTex("x", font_size=28)
                               .next_to(P(c_U + t.get_value() * kier), DL, buff=0.06))

        self.play(FadeIn(tekst1[2][0], shift=0.2 * RIGHT), Create(ax))
        self.next_slide()
        self.play(FadeIn(tekst1[2][1:], shift=0.2 * RIGHT))
        self.play(FadeIn(U[0]), Create(U[1]), FadeIn(etyk_U))
        self.play(LaggedStart(*[FadeIn(m) for m in male_V], lag_ratio=0.4))
        self.play(FadeIn(ruchomy_V), FadeIn(etyk_x))
        self.play(t.animate.set_value(0.95), run_time=3, rate_func=smooth)
        self.next_slide()

        self.play(FadeOut(VGroup(tekst1, U, etyk_U, male_V, ruchomy_V, etyk_x)))

        # ================= Krok 2: kule tworzą bazę =================
        tekst2 = kolumna(
            MathTex(r"B_d(x,\varepsilon)\coloneqq\{y\in X : d(x,y)<\varepsilon\}", font_size=34, color=B),
            Tex(r"Kule tworzą \emph{bazę} topologii $\tau_d$, czyli", font_size=32),
            Tex(r"$U$ jest otwarty $\iff$ dla każdego $x\in U$", font_size=32),
            Tex(r"istnieje $\varepsilon>0$ takie, że $B_d(x,\varepsilon)\subset U$.", font_size=32),
        )
        tresc2 = tekst2[2]
        self.play(FadeIn(tresc2[0], shift=0.2 * RIGHT))
        self.next_slide()

        # Zbiór otwarty U jako kula, a w nim mniejsze kule wokół punktów.
        c_K, r_K = np.array([2.0, 1.5]), 1.15
        UK = VGroup(Circle(radius=r_K * J, stroke_width=0).set_fill(GRAY, 0.14),
                    DashedVMobject(Circle(radius=r_K * J, color=KOLOR_TEKST, stroke_width=3), num_dashes=50)
                    ).move_to(P(c_K))
        etyk_UK = MathTex("U", font_size=34).move_to(P(c_K + np.array([0.95, 0.95])))

        def kulka(u):
            return kula(P(u), 0.75 * (r_K - np.linalg.norm(u - c_K)) * J)

        stale2 = [np.array([1.45, 1.8]), np.array([2.5, 1.1])]
        male_B = VGroup(*[VGroup(kulka(u), Dot(P(u), radius=0.06)) for u in stale2])
        s = ValueTracker(0.0)
        kier2 = np.array([-0.4, -1.0]) / np.linalg.norm([-0.4, -1.0])
        ruchoma_B = always_redraw(lambda: VGroup(
            kulka(c_K + s.get_value() * kier2), Dot(P(c_K + s.get_value() * kier2), radius=0.06)))
        etyk_x2 = always_redraw(lambda: MathTex("x", font_size=28)
                                .next_to(P(c_K + s.get_value() * kier2), DL, buff=0.06))

        self.play(FadeIn(tresc2[1:], shift=0.2 * RIGHT))
        self.play(FadeIn(UK[0]), Create(UK[1]), FadeIn(etyk_UK))
        self.play(LaggedStart(*[FadeIn(m) for m in male_B], lag_ratio=0.4))
        self.play(FadeIn(ruchoma_B), FadeIn(etyk_x2))
        self.play(s.animate.set_value(0.95), run_time=3, rate_func=smooth)
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
        wniosek4 = Tex(r"Przestrzeń metryczna jest Hausdorffa ($T_2$).", font_size=32, color=KOLOR_METRYKA)
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
        self.next_slide()
        self.play(FadeIn(wniosek4))
        self.wait(0.4)
        self.play(wniosek4.animate.set_color(KOLOR_TEKST), run_time=0.8)
        self.next_slide()


class ZbieznoscMetryczna(Slide):
    """Zbieżność w przestrzeni metrycznej: wersja z d i wersja topologiczna (otoczenia)."""
    def construct(self):
        naglowek, ax, J, P, kolumna = przygotuj()
        self.add(naglowek)
        B = KOLOR_METRYKA

        # ---- Lewa kolumna: najpierw definicja topologiczna, potem równoważność z d ----
        tekst_top = VGroup(
            Tex(r"Ciąg $(x_n)_{n\in\mathbb{N}}\subset X$ jest zbieżny do $a\in X$, gdy", font_size=30),
            MathTex(r"\forall\,U\in\tau_d,\ a\in U\ \ \exists\,N\ \forall\,n\ge N\colon\ x_n\in U", r".",
                    font_size=30),
            Tex(r"(każde otoczenie $a$ zawiera prawie wszystkie wyrazy ciągu)", font_size=26,
                color=KOLOR_DRUGORZEDNY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        tekst_d = VGroup(
            Tex(r"W przestrzeni metrycznej:", font_size=30, color=KOLOR_DRUGORZEDNY),
            MathTex(r"x_n\to a", r"\iff", r"\forall\,\varepsilon>0\ \exists\,N\ \forall\,n\ge N\colon\ "
                    r"x_n\in B_d(a,\varepsilon)", font_size=30),
            MathTex(r"\iff", r"\lim_{n\to\infty} d(a,x_n)=0", r".", font_size=30),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        tekst_d[2].shift((tekst_d[1][1].get_left()[0] - tekst_d[2][0].get_left()[0]) * RIGHT)
        lewa = VGroup(tekst_top, tekst_d).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        lewa.to_edge(LEFT, buff=0.4).shift(0.2 * DOWN)
        if lewa.get_right()[0] > ax.get_left()[0] - 0.2:
            lewa.scale_to_fit_width(ax.get_left()[0] - 0.2 - lewa.get_left()[0]).to_edge(LEFT, buff=0.4)

        # ---- Rysunek: ciąg spiralą zbiega do a ----
        a = np.array([2.1, 1.45])
        LICZBA = 7
        wyrazy = [a + 1.45 * 0.76 ** n * np.array([np.cos(1.15 * n), np.sin(1.15 * n)])
                  for n in range(1, LICZBA + 1)]
        # Im dalej w ciągu, tym mniejsza kropka i podpis.
        kropki = VGroup(*[
            Dot(P(u), radius=0.07 - 0.005 * (n - 1), color=KOLOR_TEKST).set_z_index(5)
            for n, u in enumerate(wyrazy, start=1)
        ])
        etykiety = VGroup()
        for n, (u, k) in enumerate(zip(wyrazy, kropki), start=1):
            kier = (u - a) / np.linalg.norm(u - a)
            e = MathTex(rf"x_{{{n}}}", font_size=26 - 1.8 * (n - 1))
            e.move_to(k.get_center() + (0.2 - 0.012 * n) * np.array([kier[0], kier[1], 0])
                      + 0.08 * np.array([kier[0], kier[1], 0]) * e.width / 0.3)
            etykiety.add(e)
        da = Dot(P(a), radius=0.07, color=B).set_z_index(6)
        ea = MathTex("a", font_size=30, color=B).move_to(da.get_center() + np.array([-0.6, -0.5, 0])).set_z_index(6)
        strz_a = Line(ea.get_corner(UR), da.get_center(), buff=0.08, color=B, stroke_width=2).set_z_index(6)
        ea = VGroup(ea, strz_a)

        def koloruj(czy_w_srodku):
            return [k.animate.set_color(B if czy_w_srodku(u) else GRAY_B) for k, u in zip(kropki, wyrazy)]

        self.play(Create(ax))
        self.play(FadeIn(tekst_top[:2], shift=0.2 * RIGHT), FadeIn(da), FadeIn(ea))
        self.play(LaggedStart(*[FadeIn(k, scale=0.5) for k in kropki], lag_ratio=0.15), FadeIn(etykiety),
                  run_time=2.0)
        self.next_slide()

        # ---- Wersja topologiczna: dowolny zbiór otwarty U wokół a ----
        self.play(FadeIn(tekst_top[2], shift=0.2 * RIGHT))
        self.next_slide()

        def zbior_U(srodek, szer, wys, kat):
            ksztalt = Ellipse(width=szer * J, height=wys * J).rotate(kat).move_to(P(srodek))
            return VGroup(ksztalt.copy().set_stroke(width=0).set_fill(GRAY, 0.15),
                          DashedVMobject(ksztalt.copy().set_stroke(KOLOR_TEKST, 3), num_dashes=40))

        def w_elipsie(u, srodek, szer, wys, kat):
            v = u - srodek
            c, s_ = np.cos(-kat), np.sin(-kat)
            x, y = c * v[0] - s_ * v[1], s_ * v[0] + c * v[1]
            return (x / (szer / 2)) ** 2 + (y / (wys / 2)) ** 2 < 1

        zbiory = [
            (a + np.array([0.4, 0.2]), 2.4, 1.3, 0.5),
            (a + np.array([-0.18, 0.08]), 1.0, 0.55, -0.4),
        ]
        U = zbior_U(*zbiory[0])
        eU = MathTex("U", font_size=30).next_to(U, UR, buff=0.0)
        self.play(FadeIn(U), FadeIn(eU), *koloruj(lambda u: w_elipsie(u, *zbiory[0])))
        self.next_slide()
        U2 = zbior_U(*zbiory[1])
        self.play(Transform(U, U2), eU.animate.next_to(U2, UR, buff=0.0),
                  *koloruj(lambda u: w_elipsie(u, *zbiory[1])), run_time=1.0)
        self.next_slide()

        # ---- W przestrzeni metrycznej wystarczą kule: eps maleje, N rośnie ----
        self.play(FadeOut(U), FadeOut(eU), *[k.animate.set_color(KOLOR_TEKST) for k in kropki])
        self.play(FadeIn(tekst_d[:2], shift=0.2 * RIGHT))

        def N_dla(e):
            return next(n for n in range(1, LICZBA + 1) if all(np.linalg.norm(u - a) < e for u in wyrazy[n - 1:]))

        def opis(e):
            return MathTex(rf"\varepsilon={e:.2f},\quad N={N_dla(e)}", font_size=30, color=B) \
                .next_to(ax, DOWN, buff=0.35)

        eps_lista = [1.0, 0.6, 0.3]
        kula_a = kula(P(a), eps_lista[0] * J)
        napis = opis(eps_lista[0])
        self.play(FadeIn(kula_a), FadeIn(napis), *koloruj(lambda u: np.linalg.norm(u - a) < eps_lista[0]))
        self.next_slide()
        for e in eps_lista[1:]:
            nowy = opis(e)
            self.play(Transform(kula_a, kula(P(a), e * J)), FadeOut(napis), FadeIn(nowy),
                      *koloruj(lambda u, e=e: np.linalg.norm(u - a) < e), run_time=1.0)
            napis = nowy
            self.next_slide()

        # ---- Równoważność z granicą odległości ----
        self.play(FadeIn(tekst_d[2], shift=0.2 * RIGHT))
        self.next_slide()
