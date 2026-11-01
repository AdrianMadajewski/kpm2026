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
        self.next_slide()

        # Krok 1a: sprawdzenie aksjomatów (P1)–(P4).
        # Po lewej ogólny warunek, po prawej ten sam warunek dla p = max, potem ptaszek.
        FS = 30

        def etyk(t):
            return Tex(t, font_size=28, color=KOLOR_DRUGORZEDNY)

        lewe = [
            MathTex(r"x=y \iff p(x,x)=p(x,y)=p(y,y)", font_size=FS),
            MathTex(r"p(x,x)\le p(x,y)", font_size=FS),
            MathTex(r"p(x,y)=p(y,x)", font_size=FS),
            MathTex(r"p(x,z)\le p(x,y)+p(y,z)-p(y,y)", font_size=FS),
        ]
        prawe = [
            MathTex(r"x=y \iff x=\max\{x,y\}=y", font_size=FS),
            MathTex(r"x\le\max\{x,y\}", font_size=FS),
            MathTex(r"\max\{x,y\}=\max\{y,x\}", font_size=FS),
            MathTex(r"\max\{x,z\}\le\max\{x,y\}+\max\{y,z\}-y", font_size=FS),
        ]
        etykiety = [etyk(rf"(P{i})") for i in range(1, 5)]

        # Siatka: etykieta | warunek ogólny | warunek dla max | ptaszek.
        y0 = wzor.get_bottom()[1] - 0.75
        dy = 0.62
        x_etyk, x_lewe, x_prawe = -6.4, -5.5, 0.9
        for i in range(4):
            y = y0 - i * dy
            etykiety[i].move_to([x_etyk, y, 0], aligned_edge=LEFT)
            lewe[i].move_to([x_lewe, y, 0], aligned_edge=LEFT)
            prawe[i].move_to([x_prawe, y, 0], aligned_edge=LEFT)
        strzalki = [MathTex(r"\rightsquigarrow", font_size=FS, color=KOLOR_DRUGORZEDNY)
                    .move_to([x_prawe - 0.45, y0 - i * dy, 0]) for i in range(4)]

        def ptaszek_przy(m):
            return MathTex(r"\checkmark", font_size=40, color=KOLOR_METRYKA).next_to(m, RIGHT, buff=0.3)

        ptaszki = VGroup()
        for i in range(3):
            self.play(FadeIn(VGroup(etykiety[i], lewe[i]), shift=0.2 * RIGHT), run_time=0.6)
            self.next_slide()
            self.play(FadeIn(strzalki[i]), FadeIn(prawe[i], shift=0.2 * RIGHT), run_time=0.6)
            self.next_slide()
            pt = ptaszek_przy(prawe[i])
            ptaszki.add(pt)
            self.play(FadeIn(pt, scale=1.5), run_time=0.5)
            self.next_slide()

        # (P4): warunek, jego postać dla max, uzasadnienie, ptaszek.
        self.play(FadeIn(VGroup(etykiety[3], lewe[3]), shift=0.2 * RIGHT), run_time=0.6)
        self.next_slide()
        self.play(FadeIn(strzalki[3]), FadeIn(prawe[3], shift=0.2 * RIGHT), run_time=0.6)
        self.next_slide()

        bso = Tex(r"Bez straty ogólności $\max\{x,z\}=x$.", font_size=FS)
        mamy = Tex(r"Mamy $\max\{x,y\}\ge x$ oraz $\max\{y,z\}\ge y$.", font_size=FS)
        rach = MathTex(
            r"\text{Stąd}\quad \max\{x,y\}+\max\{y,z\}-y",
            r"\ge x+y-y",
            r"=x",
            r"=\max\{x,z\}.",
            font_size=FS,
        )
        dowod = VGroup(bso, mamy, rach).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        dowod.next_to(lewe[3], DOWN, buff=0.5).align_to(lewe[3], LEFT)
        self.play(FadeIn(bso))
        self.next_slide()
        self.play(FadeIn(mamy))
        self.next_slide()
        for czesc in rach:
            self.play(FadeIn(czesc, shift=0.2 * RIGHT), run_time=0.6)
            self.next_slide()
        ptaszek = ptaszek_przy(prawe[3])
        self.play(FadeIn(ptaszek, scale=1.5))
        self.next_slide()
        self.play(FadeOut(VGroup(*etykiety, *lewe, *prawe, *strzalki, dowod, ptaszek, ptaszki)))

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
