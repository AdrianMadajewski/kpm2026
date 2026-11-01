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
        dowod.next_to(os, DOWN, buff=0.85).to_edge(LEFT, buff=0.8)
        L4.shift(0.6 * RIGHT + 0.2 * DOWN)
        L5.shift(0.2 * DOWN)
        tag = Tex(r"(P4)", font_size=24, color=KOLOR_DRUGORZEDNY).next_to(L4[1], UP, buff=0.1)
        tresc_p4 = MathTex(r"\text{(P4)}\quad p(a,c)\le p(a,b)+p(b,c)-p(b,b)",
                           font_size=30, color=KOLOR_CZESCIOWA).to_edge(DOWN, buff=0.3)

        def zaswiec(*m):
            return [x.animate.set_color(O) for x in m]

        def zgas(*m):
            return [x.animate.set_color(KOLOR_TEKST) for x in m]

        # Ustalmy y.
        self.play(FadeIn(L1))
        self.next_slide()

        # Niech delta := ...  (pauza)  > 0 — bo y jest w kuli, czyli p(x,y) < p(x,x)+eps.
        self.play(FadeIn(L2[:2]), FadeIn(L2[3]))
        self.next_slide()
        self.play(*zaswiec(L1[1], L1[3]), run_time=0.6)
        self.play(FadeIn(L2[2], shift=0.2 * RIGHT))
        self.wait(0.4)
        self.play(*zgas(L1[1], L1[3]), run_time=0.6)
        self.next_slide()

        # Niech z w kuli wokół y.
        self.play(FadeIn(L3))
        self.next_slide()

        # Krok 1: (P4).
        self.play(FadeIn(L4[0]))
        self.next_slide()
        self.play(FadeIn(tresc_p4, shift=0.2 * UP))
        self.next_slide()
        tag.set_color(O)
        self.play(FadeIn(L4[1]), FadeIn(tag))
        L4[2:4].set_color(O)
        self.play(FadeIn(L4[2:4], shift=0.2 * RIGHT))
        self.next_slide()
        self.play(FadeOut(tresc_p4, shift=0.2 * DOWN), tag.animate.set_color(KOLOR_DRUGORZEDNY),
                  L4[2:4].animate.set_color(KOLOR_TEKST), run_time=0.7)
        self.next_slide()

        # Krok 2: z w B_p(y, delta), czyli p(y,z) - p(y,y) < delta.
        self.play(*zaswiec(L3[1], L3[3], L4[3]), run_time=0.6)
        self.next_slide()
        self.play(FadeIn(L4[4:6], shift=0.2 * RIGHT))
        self.play(L4[5].animate.set_color(O), run_time=0.4)
        self.wait(0.4)
        self.play(*zgas(L3[1], L3[3], L4[3], L4[5]), run_time=0.6)
        self.next_slide()

        # Krok 3: definicja delta.
        self.play(*zaswiec(L2[1], L4[5]), run_time=0.6)
        self.next_slide()
        L4[7].set_color(O)
        self.play(FadeIn(L4[6:], shift=0.2 * RIGHT))
        self.wait(0.4)
        self.play(*zgas(L2[1], L4[5], L4[7]), run_time=0.6)
        self.next_slide()

        self.play(FadeIn(L5))
        self.next_slide()
        uwaga = tag

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
                     r"\varepsilon\coloneqq p(x,y)-p(x,x)>0", r".", font_size=FS)
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

        # Wybór epsilon.
        L4[3].set_color(O)
        self.play(FadeIn(L4, shift=0.2 * RIGHT))
        self.wait(0.4)
        self.play(L4[3].animate.set_color(KOLOR_TEKST), run_time=0.6)
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

        # ---- Rysunek w przykładzie max: x = 1.5, y = 3, eps = 1.5, kula [0, 3) ----
        os = NumberLine(x_range=[0, 5, 1], length=8, include_numbers=True,
                        font_size=24, include_tip=False).move_to(np.array([0, -2.75, 0]))
        x0, y0 = 1.5, 3.0
        eps = max(x0, y0) - x0
        kx = Dot(os.n2p(x0), radius=0.08, color=O).set_z_index(10)
        ky = Dot(os.n2p(y0), radius=0.08, color=KOLOR_Y).set_z_index(10)
        ex = MathTex("x", font_size=28).next_to(kx, DOWN, buff=0.4)
        ey = MathTex("y", font_size=28).next_to(ky, DOWN, buff=0.4)
        kula = _kula_na_osi(os, x0 + eps, O, 0.35)
        e_k = MathTex(r"B_p(x,\varepsilon)=[0,\,3)", font_size=28, color=O).next_to(kula[0], RIGHT, buff=0.35)
        self.play(Create(os))
        self.play(FadeIn(kx), FadeIn(ex), FadeIn(ky), FadeIn(ey))
        self.next_slide()
        self.play(FadeIn(kula), FadeIn(e_k))
        self.wait(0.2)
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

        # ---- Dowód (kontrprzykład max) ----
        M1 = MathTex(r"\textit{Dowód.}\ \text{Niech }", r"X=[0,\infty)", r",\ ", r"p(x,y)=\max\{x,y\}",
                     r"\text{ oraz }", r"0\le x<y", r".", font_size=FS)
        M2 = MathTex(r"\text{Każdy zbiór otwarty }", r"U\ni y", r"\text{ zawiera pewną kulę }",
                     r"B_p(y,\varepsilon)", r".", font_size=FS)
        M3 = MathTex(r"\text{Ale }", r"B_p(y,\varepsilon)=[0,\,y+\varepsilon)", r"\ni", r"x", r",",
                     font_size=FS)
        M4 = MathTex(r"\text{więc każde otoczenie } y \text{ zawiera } x", r"\text{, czyli brak } T_1.\ \blacksquare",
                     font_size=FS)
        dowod1 = VGroup(M1, M2, M3, M4).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        dowod1.next_to(uwaga, DOWN, buff=0.45).to_edge(LEFT, buff=0.8)

        baza = przypomnienie(r"\text{(Lemat)}\quad \text{kule } B_p \text{ tworzą bazę topologii } \tau_p")
        kula_max = przypomnienie(r"\text{(max)}\quad B_p(u,\varepsilon)=[0,\,u+\varepsilon)")

        self.play(FadeIn(M1, shift=0.2 * RIGHT))
        self.next_slide()

        # Lemat o bazie.
        self.play(FadeIn(baza, shift=0.2 * UP))
        self.next_slide()
        M2[3].set_color(O)
        self.play(FadeIn(M2, shift=0.2 * RIGHT))
        self.next_slide()
        self.play(FadeOut(baza, shift=0.2 * DOWN), M2[3].animate.set_color(KOLOR_TEKST), run_time=0.7)
        self.next_slide()

        # Kula w przykładzie max.
        self.play(FadeIn(kula_max, shift=0.2 * UP))
        self.next_slide()
        M3[1].set_color(O)
        self.play(FadeIn(M3[:2], shift=0.2 * RIGHT))
        self.next_slide()
        self.play(FadeOut(kula_max, shift=0.2 * DOWN), M3[1].animate.set_color(KOLOR_TEKST), run_time=0.7)
        self.next_slide()
        # x < y < y + eps, więc x należy do kuli.
        M3[3].set_color(O)
        self.play(FadeIn(M3[2:], shift=0.2 * RIGHT))
        self.wait(0.4)
        self.play(M3[3].animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()

        self.play(FadeIn(M4, shift=0.2 * RIGHT))
        self.wait(0.2)
        self.next_slide()

        # ---- Rysunek: x = 1.5, y = 3, kula wokół y kurczy się, a x wciąż w niej jest ----
        os1 = NumberLine(x_range=[0, 5, 1], length=8, include_numbers=True,
                         font_size=24, include_tip=False).move_to(np.array([0, -2.75, 0]))
        x1, y1 = 1.5, 3.0
        sx = Dot(os1.n2p(x1), radius=0.08, color=O).set_z_index(10)
        sy = Dot(os1.n2p(y1), radius=0.08, color=KOLOR_Y).set_z_index(10)
        fx = MathTex("x", font_size=28).next_to(sx, DOWN, buff=0.4)
        fy = MathTex("y", font_size=28).next_to(sy, DOWN, buff=0.4)
        self.play(Create(os1))
        self.play(FadeIn(sx), FadeIn(fx), FadeIn(sy), FadeIn(fy))
        self.next_slide()

        eps_t = ValueTracker(1.5)
        kula_y = always_redraw(lambda: _kula_na_osi(os1, y1 + eps_t.get_value(), KOLOR_Y, 0.35))
        e_ky = always_redraw(lambda: MathTex(r"B_p(y,\varepsilon)", font_size=28, color=KOLOR_Y)
                             .next_to(kula_y[0], UP, buff=0.15).align_to(kula_y[0], RIGHT))
        eps_lab = MathTex(r"\varepsilon=", font_size=30)
        eps_num = DecimalNumber(1.5, num_decimal_places=2, font_size=30)
        eps_grp = VGroup(eps_lab, eps_num).arrange(RIGHT, buff=0.12).move_to(np.array([5.2, -1.9, 0]))
        eps_num.add_updater(lambda m: m.set_value(eps_t.get_value()).next_to(eps_lab, RIGHT, buff=0.12))
        self.play(FadeIn(kula_y), FadeIn(e_ky), FadeIn(eps_grp))
        self.wait(0.2)
        self.next_slide()

        self.play(eps_t.animate.set_value(0.6), run_time=1.5)
        self.next_slide()
        self.play(eps_t.animate.set_value(0.15), run_time=1.5)
        self.next_slide()
        self.play(Indicate(sx, color=O, scale_factor=1.6))
        self.next_slide()

        # ================= Stwierdzenie: charakteryzacja T_1 =================
        eps_num.clear_updaters()
        zostaje = {tytul, ramka1, qx, qy, mx, my, ox_, oy_, naz1, def_t1}
        self.play(*[FadeOut(m, shift=0.3 * LEFT) for m in self.mobjects if m not in zostaje], run_time=0.8)
        self.next_slide()

        stw1 = VGroup(
            Tex(r"\textbf{Stwierdzenie.} Topologia $\tau_p$ spełnia aksjomat $T_1$ wtedy i tylko wtedy, gdy",
                font_size=34),
            MathTex(r"\forall\, x\neq y\colon\quad p(x,x)<p(x,y)\ \ \text{i}\ \ p(y,y)<p(x,y).", font_size=34),
        ).arrange(DOWN, buff=0.15)
        stw1.next_to(tytul, DOWN, buff=0.4)
        self.play(FadeIn(stw1, shift=0.2 * DOWN))
        self.wait(0.2)
        self.next_slide()

        # Ramka T_1 z definicją schodzi niżej, żeby zrobić miejsce na dowód.
        panel_t1 = VGroup(ramka1, qx, qy, mx, my, ox_, oy_, naz1, def_t1)
        self.play(panel_t1.animate.scale(0.85).to_edge(RIGHT, buff=0.35).shift(1.1 * DOWN), run_time=0.8)
        self.next_slide()

        N1 = MathTex(r"\textit{Dowód.}\ (\Leftarrow)\ \text{Ustalmy } x\neq y", r"\text{ i niech }",
                     r"\varepsilon\coloneqq p(x,y)-p(x,x)>0", r".", font_size=FS)
        N2 = MathTex(r"\text{Wtedy }", r"p(x,y)=p(x,x)+\varepsilon", r"\text{, więc }",
                     r"y\notin B_p(x,\varepsilon)\ni x", r".", font_size=FS)
        N3 = MathTex(r"\text{Analogicznie dla }", r"\delta\coloneqq p(x,y)-p(y,y)>0", r"\text{ mamy }",
                     r"x\notin B_p(y,\delta)\ni y", r".", font_size=FS)
        N4 = MathTex(r"(\Rightarrow)\ \text{Ustalmy } x\neq y", r"\text{. Z }T_1\text{ istnieje }",
                     r"U\in\tau_p", r"\text{, że }", r"y\in U\not\ni x", r".", font_size=FS)
        N5 = MathTex(r"\text{Z lematu }", r"B_p(y,\varepsilon)\subseteq U", r"\text{ dla pewnego }\varepsilon>0",
                     r"\text{, więc }", r"x\notin B_p(y,\varepsilon)", r".", font_size=FS)
        N6 = MathTex(r"\text{Zatem }", r"p(x,y)", r"=p(y,x)", r"\ge p(y,y)+\varepsilon", r">p(y,y)", r".",
                     font_size=FS)
        N7 = MathTex(r"\text{Analogicznie }", r"p(x,x)<p(x,y)", r".\ \blacksquare", font_size=FS)
        dowod2 = VGroup(N1, N2, N3, N4, N5, N6, N7).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        dowod2.next_to(stw1, DOWN, buff=0.4).to_edge(LEFT, buff=0.6)

        def pokaz(linia, *idx, pauza=True):
            for k in idx:
                linia[k].set_color(O)
            self.play(FadeIn(linia, shift=0.2 * RIGHT))
            self.wait(0.4)
            if idx:
                self.play(*[linia[k].animate.set_color(KOLOR_TEKST) for k in idx], run_time=0.6)
            if pauza:
                self.next_slide()

        def_kuli = przypomnienie(r"B_p(x,\varepsilon)\coloneqq\{u\in X : p(x,u)<p(x,x)+\varepsilon\}")
        lemat = przypomnienie(r"\text{(Lemat)}\quad y\in U\in\tau_p \implies \exists\,\varepsilon>0\colon\ B_p(y,\varepsilon)\subseteq U")
        p3 = przypomnienie(r"\text{(P3)}\quad p(x,y)=p(y,x)")

        # (<=)
        pokaz(N1, 2)
        self.play(FadeIn(def_kuli, shift=0.2 * UP))
        self.next_slide()
        pokaz(N2, 1, 3, pauza=False)
        self.play(FadeOut(def_kuli, shift=0.2 * DOWN), run_time=0.6)
        self.next_slide()
        pokaz(N3, 1, 3)
        uwaga_otw = przypomnienie(r"\text{kule są otwarte, więc } \tau_p \text{ spełnia } T_1")
        self.play(FadeIn(uwaga_otw, shift=0.2 * UP))
        self.next_slide()
        self.play(FadeOut(uwaga_otw, shift=0.2 * DOWN), run_time=0.6)
        self.next_slide()

        # (=>)
        pokaz(N4, 2, 4)
        self.play(FadeIn(lemat, shift=0.2 * UP))
        self.next_slide()
        pokaz(N5, 1, pauza=False)
        self.play(FadeOut(lemat, shift=0.2 * DOWN), run_time=0.6)
        self.next_slide()

        # Łańcuch: p(x,y) (P3) = p(y,x) >= p(y,y) + eps > p(y,y).
        self.play(FadeIn(N6[:2], shift=0.2 * RIGHT))
        self.next_slide()
        self.play(FadeIn(p3, shift=0.2 * UP))
        self.next_slide()
        N6[2].set_color(O)
        self.play(FadeIn(N6[2], shift=0.2 * RIGHT))
        self.wait(0.3)
        self.play(FadeOut(p3, shift=0.2 * DOWN), N6[2].animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()
        self.play(N5[4].animate.set_color(O), run_time=0.5)
        self.next_slide()
        N6[3].set_color(O)
        self.play(FadeIn(N6[3], shift=0.2 * RIGHT))
        self.wait(0.3)
        self.play(N5[4].animate.set_color(KOLOR_TEKST), N6[3].animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()
        N6[4].set_color(O)
        self.play(FadeIn(N6[4:], shift=0.2 * RIGHT))
        self.wait(0.3)
        self.play(N6[4].animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()
        pokaz(N7, 1)
