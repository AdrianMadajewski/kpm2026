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
            Tex(r"2. Jakie aksjomaty oddzielania spełnia nasza przestrzeń?", font_size=38),
            Tex(r"3. Co możemy powiedzieć o zbieżności?", font_size=38),
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
        # Litery d/p wydzielone, żeby zmieniały się tylko one.
        kula_d = MathTex(
            r"B_", r"d", r"(x,\varepsilon)", r"\coloneqq", r"\{y\in X :", r"d", r"(x,y)", r"<", r"\varepsilon\}",
            font_size=FS,
        ).move_to(1.6 * UP)
        kula_p = MathTex(
            r"B_", r"p", r"(x,\varepsilon)", r"\coloneqq", r"\{y\in X :", r"p", r"(x,y)", r"<", r"p(x,x)+",
            r"\varepsilon\}", font_size=FS,
        ).move_to(1.6 * UP)
        podpis_d = Tex(r"kula w przestrzeni metrycznej", font_size=30, color=KOLOR_DRUGORZEDNY)
        podpis_d.next_to(kula_d, DOWN, buff=0.3)
        podpis_p = Tex(r"kula w przestrzeni częściowo metrycznej", font_size=30, color=KOLOR_DRUGORZEDNY)
        podpis_p.next_to(kula_p, DOWN, buff=0.3)

        # Krok 1: przypomnienie kuli metrycznej.
        self.play(FadeIn(kula_d, shift=0.2 * DOWN), FadeIn(podpis_d))
        self.next_slide()

        # Krok 2: d odpływa w górę, reszta robi miejsce, p i p(x,x)+ wpływają od dołu.
        stare = [kula_d[1], kula_d[5]]
        nowe = [kula_p[1], kula_p[5], kula_p[8]]
        self.play(*[FadeOut(m, shift=0.25 * UP) for m in stare], FadeOut(podpis_d, shift=0.25 * UP),
                  run_time=0.5, rate_func=smooth)
        self.play(
            *[ReplacementTransform(kula_d[i], kula_p[j]) for i, j in ((0, 0), (2, 2), (3, 3), (4, 4), (6, 6),
                                                                      (7, 7), (8, 9))],
            run_time=0.9, rate_func=smooth,
        )
        for m in nowe:
            m.set_color(KOLOR_CZESCIOWA)
        self.play(*[FadeIn(m, shift=0.25 * UP) for m in nowe], FadeIn(podpis_p, shift=0.25 * UP),
                  run_time=0.6, rate_func=smooth)
        self.wait(0.5)
        self.play(*[m.animate.set_color(KOLOR_TEKST) for m in nowe], run_time=0.7)
        self.next_slide()

        # Krok 3: rachunek dla p = max.
        wstep = Tex(r"Dla $X\coloneqq[0,\infty)$ i $p(x,y)\coloneqq\max\{x,y\}$ mamy", font_size=34)
        r1 = MathTex(r"B_p(x,\varepsilon)", r"=\{y\ge 0 : \max\{x,y\}<x+\varepsilon\}", font_size=36)
        r2 = MathTex(r"=\{y\ge 0 : y<x+\varepsilon\}", font_size=36)
        r3 = MathTex(r"=[0,\,x+\varepsilon).", font_size=36)
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
        opis_d = MathTex(r"d(x,y) \coloneqq |x-y|", font_size=34, color=KOLOR_METRYKA)
        opis_d.next_to(os_d, UP, buff=0.55).to_edge(LEFT, buff=0.8)
        opis_p = MathTex(r"p(x,y) \coloneqq \max\{x,y\}", font_size=34, color=KOLOR_CZESCIOWA)
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

        # eps machamy w dół i w górę: kula B_p zawsze zawiera [0, x], niezależnie od eps.
        for e in (1.9, 0.5, 1.7, 0.2):
            self.play(eps.animate.set_value(e), run_time=1.1, rate_func=smooth)
        self.next_slide()


def _klodka(kolor=ManimColor("#7B3FA0")):
    """Mała kłódka: korpus z dziurką od klucza i pałąk (pałąk osobno, żeby dało się go "zatrzasnąć")."""
    korpus = RoundedRectangle(width=0.5, height=0.4, corner_radius=0.07, color=kolor,
                              stroke_width=2).set_fill(kolor, 1)
    dziurka = VGroup(Dot(radius=0.045, color=WHITE).shift(0.03 * UP),
                     Rectangle(width=0.035, height=0.1, stroke_width=0).set_fill(WHITE, 1).shift(0.04 * DOWN))
    dziurka.move_to(korpus)
    r = 0.15
    luk = Arc(radius=r, start_angle=0, angle=PI, color=kolor, stroke_width=6)
    lewa = Line([-r, 0, 0], [-r, -0.12, 0], color=kolor, stroke_width=6)
    prawa = Line([r, 0, 0], [r, -0.12, 0], color=kolor, stroke_width=6)
    palak = VGroup(luk, lewa, prawa)
    palak.next_to(korpus, UP, buff=-0.1)
    return VGroup(korpus, dziurka, palak)


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
    """Lemat: kule tworzą bazę topologii — treść i krótki dowód."""

    def construct(self):

        # Motywacja: po co nam lemat.
        cel = Tex(r"Chcemy, żeby kule $B_p$ wyznaczały topologię", font_size=38)
        cel2 = Tex(r"--- tak jak w przestrzeni metrycznej.", font_size=38)
        pytanie = Tex(r"Jaki warunek musi być spełniony?", font_size=38, color=KOLOR_CZESCIOWA)
        odp = VGroup(
            Tex(r"Wokół każdego punktu kuli musi zmieścić się", font_size=36),
            Tex(r"mniejsza kula, cała zawarta w tej pierwszej.", font_size=36),
        ).arrange(DOWN, buff=0.12)
        motywacja = VGroup(VGroup(cel, cel2).arrange(DOWN, buff=0.12), pytanie, odp).arrange(DOWN, buff=0.6)
        self.play(FadeIn(motywacja[0], shift=0.2 * DOWN))
        self.next_slide()
        self.play(FadeIn(pytanie, shift=0.2 * UP))
        self.next_slide()
        self.play(FadeIn(odp, shift=0.2 * UP))
        self.next_slide()
        self.play(FadeOut(motywacja, shift=0.2 * UP))

        lemat = VGroup(
            Tex(r"\textbf{Lemat.} Jeżeli $y\in B_p(x,\varepsilon)$, to istnieje $\delta>0$ takie, że", font_size=32),
            MathTex(r"B_p(y,\delta)\subset B_p(x,\varepsilon).", font_size=34),
        ).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.45)
        self.play(FadeIn(lemat, shift=0.2 * DOWN))
        self.next_slide()

        # Dowód — każde przejście na kliknięcie, z podświetleniem tego, z czego korzystamy.
        FS = 32
        O = KOLOR_CZESCIOWA

        L1 = MathTex(r"\text{\textit{Dowód.} Ustalmy }", r"y\in B_p(x,\varepsilon)",
                     r"\coloneqq\{u\in X :", r"p(x,u)<p(x,x)+\varepsilon", r"\}.", font_size=FS)
        L2 = MathTex(r"\text{Niech }", r"\delta\coloneqq p(x,x)+\varepsilon-p(x,y)", r">0", r".", font_size=FS)
        L3 = MathTex(r"\text{Niech }", r"z\in B_p(y,\delta)", r"\coloneqq\{u\in X :",
                     r"p(y,u)<p(y,y)+\delta", r"\}.\ \text{Wtedy}", font_size=FS)
        L4 = MathTex(r"p(x,z)", r"\le", r"p(x,y)+", r"p(y,z)-p(y,y)", r"<", r"p(x,y)+\delta",
                     r"=", r"p(x,x)+\varepsilon", r",", font_size=FS + 2)
        L5 = Tex(r"czyli $z\in B_p(x,\varepsilon)$. \hfill $\blacksquare$", font_size=FS)
        dowod = VGroup(L1, L2, L3, L4, L5).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        dowod.next_to(lemat, DOWN, buff=0.7).to_edge(LEFT, buff=0.8)
        L4.shift(0.6 * RIGHT + 0.2 * DOWN)
        L5.shift(0.2 * DOWN)
        tag = Tex(r"(P4)", font_size=24, color=KOLOR_DRUGORZEDNY).next_to(L4[1], UP, buff=0.1)
        tresc_p4 = MathTex(r"\text{(P4)}\quad p(x,z)\le p(x,y)+p(y,z)-p(y,y)",
                           font_size=30, color=KOLOR_CZESCIOWA).to_edge(DOWN, buff=0.3)

        def zaswiec(*m):
            return [x.animate.set_color(O) for x in m]

        def zgas(*m):
            return [x.animate.set_color(KOLOR_TEKST) for x in m]

        # Ustalmy y.
        self.play(FadeIn(L1))
        self.next_slide()

        # Niech delta := ...  (pauza)  > 0 — bo y jest w kuli, czyli p(x,y) < p(x,x)+eps.
        # Kropka najpierw stoi tuż za definicją delta, potem przesuwa się za "> 0".
        kropka_cel = L2[3].get_center()
        dol_kropki = L2[3].get_bottom()[1]
        L2[3].next_to(L2[1], RIGHT, buff=0.05)
        L2[3].shift((dol_kropki - L2[3].get_bottom()[1]) * UP)
        self.play(FadeIn(L2[:2]), FadeIn(L2[3]))
        self.next_slide()
        # Z czego korzystamy: y jest w kuli wokół x. Podświetlenie zostaje do kliknięcia.
        self.play(*zaswiec(L1[1], L1[3]), run_time=0.6)
        self.next_slide()
        L2[2].set_color(O)
        self.play(L2[3].animate.move_to(kropka_cel), FadeIn(L2[2], shift=0.2 * RIGHT), run_time=0.7)
        self.next_slide()
        self.play(*zgas(L1[1], L1[3], L2[2]), run_time=0.6)
        self.next_slide()

        # Niech z w kuli wokół y.
        self.play(FadeIn(L3))
        self.next_slide()

        # Krok 1: (P4).
        self.play(FadeIn(L4[0]))
        self.next_slide()
        self.play(FadeIn(tresc_p4, shift=0.2 * UP))
        self.next_slide()
        # Cała prawa strona (P4) naraz, razem ze znakiem i podpisem.
        tag.set_color(O)
        L4[1:4].set_color(O)
        self.play(FadeIn(L4[1]), FadeIn(tag), FadeIn(L4[2:4], shift=0.2 * RIGHT))
        self.next_slide()
        self.play(FadeOut(tresc_p4, shift=0.2 * DOWN), tag.animate.set_color(KOLOR_DRUGORZEDNY),
                  L4[1:4].animate.set_color(KOLOR_TEKST), run_time=0.7)
        self.next_slide()

        # Krok 2: z w B_p(y, delta), czyli p(y,z) - p(y,y) < delta.
        self.play(*zaswiec(L3[1], L3[3], L4[3]), run_time=0.6)
        self.next_slide()
        # Jedno kliknięcie: stare podświetlenie gaśnie, "< p(x,y) + delta" wchodzi na pomarańczowo
        # i po chwili samo robi się czarne.
        L4[5].set_color(O)
        self.play(*zgas(L3[1], L3[3], L4[3]), FadeIn(L4[4:6], shift=0.2 * RIGHT), run_time=0.7)
        self.wait(0.5)
        self.play(*zgas(L4[5]), run_time=0.6)
        self.next_slide()

        # Krok 3: definicja delta.
        self.play(*zaswiec(L2[1], L4[5]), run_time=0.6)
        self.next_slide()
        L4[7].set_color(O)
        self.play(FadeIn(L4[6:], shift=0.2 * RIGHT))
        self.wait(0.4)
        self.play(*zgas(L2[1], L4[5], L4[7]), run_time=0.6)
        self.next_slide()

        # Przed wnioskiem: definicja B_p(x, eps) oraz p(x,z) < p(x,x) + eps.
        def_kuli = [L1[1][2:], L1[2], L1[3], L1[4]]
        nier = [L4[0], L4[4], L4[7]]
        self.play(*zaswiec(*def_kuli, *nier), run_time=0.6)
        self.next_slide()
        self.play(*zgas(*def_kuli, *nier), run_time=0.6)
        self.play(FadeIn(L5))
        self.next_slide()
        uwaga = tag

        # Wniosek.
        self.play(FadeOut(VGroup(dowod, uwaga)))
        wniosek = VGroup(
            Tex(r"Zatem kule tworzą bazę topologii $\tau_p$.", font_size=34),
            Tex(r"W przykładzie zbiory otwarte to $\emptyset$, $[0,\infty)$ oraz $[0,a)$ dla $a>0$.",
                font_size=34, color=KOLOR_CZESCIOWA),
        ).arrange(DOWN, buff=0.3).move_to(0.3 * DOWN)
        self.play(FadeIn(wniosek[0], shift=0.2 * UP))
        self.next_slide()
        self.play(FadeIn(wniosek[1], shift=0.2 * UP))
        self.wait(0.2)
        self.next_slide()


class WlasnosciTopologii(Slide):
    """Własności topologii tau_p: tytuł na środku, potem do góry, potem stwierdzenie T_0."""

    def construct(self):
        tytul = Tex(r"Własności topologii $\tau_p$", font_size=48)
        self.play(FadeIn(tytul))
        self.next_slide()

        self.play(tytul.animate.scale(44 / 48).to_edge(UP, buff=0.4), run_time=1.0)
        self.next_slide()

        stw = Tex(r"\textbf{Stwierdzenie.} Topologia $\tau_p$ spełnia aksjomat $T_0$.", font_size=36)
        stw.next_to(tytul, DOWN, buff=0.5)
        self.play(FadeIn(stw, shift=0.2 * DOWN))
        self.wait(0.2)
        self.next_slide()

        # ---- Przypomnienie T_0 (sam rysunek, po prawej) ----
        ramka = RoundedRectangle(width=3.4, height=1.9, corner_radius=0.15, color=GRAY_C, stroke_width=2)
        ramka.move_to(np.array([4.6, 0.55, 0]))
        px_ = Dot(ramka.get_center() + 0.7 * LEFT, radius=0.07)
        py_ = Dot(ramka.get_center() + 0.7 * RIGHT, radius=0.07)
        lx = MathTex("x", font_size=28).next_to(px_, DOWN, buff=0.1)
        ly = MathTex("y", font_size=28).next_to(py_, DOWN, buff=0.1)
        owal = Ellipse(width=1.2, height=1.2).move_to(px_)
        otoczenie = VGroup(
            owal.copy().set_stroke(width=0).set_fill(KOLOR_METRYKA, 0.15),
            DashedVMobject(owal.copy().set_stroke(KOLOR_METRYKA, 2.5), num_dashes=30),
        )
        naz = MathTex(r"T_0", font_size=34).next_to(ramka, UP, buff=0.12)
        def_t0 = VGroup(MathTex(r"\forall\, x\neq y\ \ \exists\, U\in\tau\colon", font_size=26),
            MathTex(r"x\in U\not\ni y\ \ \text{lub}\ \ y\in U\not\ni x", font_size=26)).arrange(DOWN, buff=0.12)
        def_t0.next_to(ramka, DOWN, buff=0.2)
        panel_t0 = VGroup(ramka, px_, py_, lx, ly, otoczenie, naz, def_t0)
        self.play(FadeIn(VGroup(ramka, px_, py_, lx, ly, naz)))
        self.play(FadeIn(otoczenie))
        self.play(FadeIn(def_t0, shift=0.2 * DOWN))
        self.next_slide()

        # ---- Dowód ----
        FS = 32
        O = KOLOR_CZESCIOWA
        KOLOR_Y = ManimColor("#7B3FA0")

        L1 = Tex(r"\textit{Dowód.} Ustalmy $x\neq y$.", font_size=FS)
        L2 = MathTex(r"\text{Z (P1) mamy }", r"p(x,x)\neq p(x,y)", r"\text{ lub }", r"p(y,y)\neq p(x,y)", r".",
                     font_size=FS)
        L3 = MathTex(r"\text{Z (P2) wynika, że }", r"p(x,x)<p(x,y)", r"\text{ lub }", r"p(y,y)<p(x,y)", r".",
                     font_size=FS)
        L4 = MathTex(r"\text{Niech np. }", r"p(x,x)<p(x,y)", r"\text{ i }",
                     r"\varepsilon\coloneqq p(x,y)-p(x,x)", r">0", r".", font_size=FS)
        L5 = MathTex(r"\text{Wtedy }", r"p(x,y)=p(x,x)+\varepsilon", r"\text{, czyli }",
                     r"y\notin B_p(x,\varepsilon)", r".\ \blacksquare", font_size=FS)
        dowod = VGroup(L1, L2, L3, L4, L5).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        dowod.next_to(stw, DOWN, buff=0.45).to_edge(LEFT, buff=0.8)

        def przypomnienie(tex):
            return MathTex(tex, font_size=30, color=O).to_edge(DOWN, buff=0.35)

        p1 = przypomnienie(r"\text{(P1)}\quad x=y \iff p(x,x)=p(x,y)=p(y,y)")
        p2 = przypomnienie(r"\text{(P2)}\quad p(x,x)\le p(x,y)")

        self.play(FadeIn(L1))
        self.next_slide()

        # (P1)
        self.play(FadeIn(p1, shift=0.2 * UP))
        self.next_slide()
        L2[1].set_color(O); L2[3].set_color(O)
        self.play(FadeIn(L2, shift=0.2 * RIGHT))
        self.next_slide()
        self.play(FadeOut(p1, shift=0.2 * DOWN), L2[1].animate.set_color(KOLOR_TEKST),
                  L2[3].animate.set_color(KOLOR_TEKST), run_time=0.7)
        self.next_slide()

        # (P2)
        self.play(FadeIn(p2, shift=0.2 * UP))
        self.next_slide()
        L3[1].set_color(O); L3[3].set_color(O)
        self.play(FadeIn(L3, shift=0.2 * RIGHT))
        self.next_slide()
        self.play(FadeOut(p2, shift=0.2 * DOWN), L3[1].animate.set_color(KOLOR_TEKST),
                  L3[3].animate.set_color(KOLOR_TEKST), run_time=0.7)
        self.next_slide()

        # Wybór epsilon: najpierw sama definicja, potem podświetlenie i dopisanie > 0.
        kropka_tmp = L4[5].copy().next_to(L4[3], RIGHT, buff=0.04).align_to(L4[5], DOWN)
        self.play(FadeIn(L4[:4], shift=0.2 * RIGHT), FadeIn(kropka_tmp, shift=0.2 * RIGHT))
        self.next_slide()
        L4[4].set_color(O)
        self.play(L4[3].animate.set_color(O), FadeIn(L4[4], shift=0.2 * RIGHT),
                  ReplacementTransform(kropka_tmp, L4[5]), run_time=0.7)
        self.next_slide()
        self.play(L4[3].animate.set_color(KOLOR_TEKST), L4[4].animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()

        # Wniosek: y poza kulą.
        self.play(L4[3].animate.set_color(O), run_time=0.6)
        self.next_slide()
        L5[1].set_color(O); L5[3].set_color(O)
        self.play(FadeIn(L5, shift=0.2 * RIGHT))
        self.wait(0.4)
        self.play(L4[3].animate.set_color(KOLOR_TEKST), L5[1].animate.set_color(KOLOR_TEKST),
                  L5[3].animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()

        # ================= Uwaga: T_1 nie musi zachodzić =================
        self.play(*[FadeOut(m, shift=0.3 * LEFT) for m in self.mobjects if m is not tytul], run_time=0.8)
        self.next_slide()

        uwaga = Tex(r"\textbf{Uwaga.} Topologia $\tau_p$ \emph{nie musi} spełniać aksjomatu $T_1$.", font_size=36)
        uwaga.next_to(tytul, DOWN, buff=0.5)
        self.play(FadeIn(uwaga, shift=0.2 * DOWN))
        self.wait(0.2)
        self.next_slide()

        # ---- Przypomnienie T_1 (rysunek po prawej) ----
        ramka1 = RoundedRectangle(width=3.4, height=1.9, corner_radius=0.15, color=GRAY_C, stroke_width=2)
        ramka1.move_to(np.array([4.6, 0.55, 0]))
        qx = Dot(ramka1.get_center() + 0.7 * LEFT, radius=0.07)
        qy = Dot(ramka1.get_center() + 0.7 * RIGHT, radius=0.07)
        mx = MathTex("x", font_size=28).next_to(qx, DOWN, buff=0.1)
        my = MathTex("y", font_size=28).next_to(qy, DOWN, buff=0.1)

        def otocz(srodek, kolor):
            # Owale nachodzą na siebie, ale każdy zawiera tylko swój punkt (jak w scenie Oddzielanie).
            o = Ellipse(width=1.5, height=1.3).move_to(srodek)
            return VGroup(o.copy().set_stroke(width=0).set_fill(kolor, 0.15),
                          DashedVMobject(o.copy().set_stroke(kolor, 2.5), num_dashes=30))

        ox_ = otocz(ramka1.get_center() + 0.4 * LEFT, KOLOR_METRYKA)
        oy_ = otocz(ramka1.get_center() + 0.4 * RIGHT, KOLOR_CZESCIOWA)
        naz1 = MathTex(r"T_1", font_size=34).next_to(ramka1, UP, buff=0.12)
        self.play(FadeIn(VGroup(ramka1, qx, qy, mx, my, naz1)))
        self.play(FadeIn(ox_))
        self.play(FadeIn(oy_))
        def_t1 = VGroup(MathTex(r"\forall\, x\neq y\ \ \exists\, U,V\in\tau\colon", font_size=26),
            MathTex(r"x\in U\not\ni y\ \ \text{i}\ \ y\in V\not\ni x", font_size=26)).arrange(DOWN, buff=0.12)
        def_t1.next_to(ramka1, DOWN, buff=0.2)
        self.play(FadeIn(def_t1, shift=0.2 * DOWN))
        self.next_slide()

        # ---- Przykład bez dowodu: max, y = 0 i x > 0 ----
        M1 = MathTex(r"\text{Niech }", r"X\coloneqq[0,\infty)", r",\ ", r"p(x,y)\coloneqq\max\{x,y\}",
                     r"\text{ oraz }", r"y\coloneqq 0,\ x>0", r".", font_size=FS)
        M1.next_to(uwaga, DOWN, buff=0.6).to_edge(LEFT, buff=0.8)
        self.play(FadeIn(M1, shift=0.2 * RIGHT))
        self.next_slide()

        # ---- Rysunek: y = 0, x = 3, kula wokół x kurczy się, a y wciąż w niej jest ----
        os1 = NumberLine(x_range=[0, 5, 1], length=6.2, include_numbers=True,
                         font_size=24, include_tip=False)
        os1.next_to(M1, DOWN, buff=1.5).align_to(M1, LEFT)
        y1, x1 = 0.0, 3.0
        sy = Dot(os1.n2p(y1), radius=0.08, color=KOLOR_Y).set_z_index(10)
        sx = Dot(os1.n2p(x1), radius=0.08, color=O).set_z_index(10)
        fy = MathTex("y", font_size=28).next_to(sy, DOWN, buff=0.4)
        fx = MathTex("x", font_size=28).next_to(sx, DOWN, buff=0.4)
        self.play(Create(os1))
        self.play(FadeIn(sy), FadeIn(fy), FadeIn(sx), FadeIn(fx))
        self.next_slide()

        eps_t = ValueTracker(1.5)
        kula_x = always_redraw(lambda: _kula_na_osi(os1, x1 + eps_t.get_value(), O, 0.35))
        e_kx = always_redraw(lambda: MathTex(r"B_p(x,\varepsilon)", font_size=28, color=O)
                             .next_to(kula_x[0], UP, buff=0.15).align_to(kula_x[0], RIGHT))
        eps_lab = MathTex(r"\varepsilon=", font_size=30)
        eps_num = DecimalNumber(1.5, num_decimal_places=2, font_size=30)
        eps_grp = VGroup(eps_lab, eps_num).arrange(RIGHT, buff=0.12)
        eps_grp.next_to(os1, DOWN, buff=0.75).align_to(os1, RIGHT)
        eps_num.add_updater(lambda m: m.set_value(eps_t.get_value()).next_to(eps_lab, RIGHT, buff=0.12))
        self.play(FadeIn(kula_x), FadeIn(e_kx), FadeIn(eps_grp))
        self.wait(0.2)
        self.next_slide()

        self.play(eps_t.animate.set_value(0.6), run_time=1.5)
        self.next_slide()
        self.play(eps_t.animate.set_value(0.15), run_time=1.5)
        self.next_slide()

        # Nad y = 0 pojawia się kłódka i się zatrzaskuje: kula wokół x jest "przypięta" do 0,
        # więc y nie da się wyrzucić z żadnej kuli wokół x.
        klodka = _klodka().scale(0.8).next_to(sy, UP, buff=0.12).set_z_index(11)
        palak = klodka[2]
        palak.shift(0.12 * UP)
        self.play(FadeIn(klodka, shift=0.2 * DOWN), run_time=0.6)
        self.play(palak.animate.shift(0.12 * DOWN), run_time=0.25, rate_func=rush_into)
        self.next_slide()
