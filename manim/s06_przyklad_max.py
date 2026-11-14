from manim_slides import Slide
from common import *


class PrzykladMax(Slide):
    """Przykład X = [0,∞), p = max, z intuicją p(x,x) jako miary nieokreśloności."""

    def construct(self):
        naglowek = Tex(r"Przykład", font_size=44).to_edge(UP, buff=0.4)
        KOLOR_Y = ManimColor("#7B3FA0")  # fiolet — punkt y i [0,y]

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
            MathTex(r"x=\max\{x,x\}\le\max\{x,y\}", font_size=FS),
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
            return MathTex(r"\checkmark", font_size=40, color=KOLOR_CZESCIOWA).next_to(m, RIGHT, buff=0.3)

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

        bso = Tex(r"Bez straty ogólności ", r"$\max\{x,z\}=x$", r".", font_size=FS)
        mamy = Tex(r"Mamy ", r"$\max\{x,y\}\ge x$", r" oraz ", r"$\max\{y,z\}\ge y$", r".", font_size=FS)
        rach = MathTex(
            r"\text{Stąd}\quad",
            r"\max\{x,y\}+\max\{y,z\}-y",
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
        O = KOLOR_CZESCIOWA
        czarny = KOLOR_TEKST
        # "Stąd max{x,y} + max{y,z} - y"
        self.play(FadeIn(rach[:2], shift=0.2 * RIGHT), run_time=0.6)
        self.next_slide()
        # "≥ x + y - y": korzystamy z obu nierówności z linijki "Mamy ...".
        self.play(mamy[1].animate.set_color(O), mamy[3].animate.set_color(O), run_time=0.5)
        self.next_slide()
        rach[2].set_color(O)
        self.play(FadeIn(rach[2], shift=0.2 * RIGHT), run_time=0.6)
        self.next_slide()
        self.play(mamy[1].animate.set_color(czarny), mamy[3].animate.set_color(czarny),
                  rach[2].animate.set_color(czarny), run_time=0.5)
        self.next_slide()
        # "= x"
        rach[3].set_color(O)
        self.play(FadeIn(rach[3], shift=0.2 * RIGHT), run_time=0.6)
        self.next_slide()
        self.play(rach[3].animate.set_color(czarny), run_time=0.5)
        self.next_slide()
        # "= max{x,z}": korzystamy z założenia bso.
        self.play(bso[1].animate.set_color(O), run_time=0.5)
        self.next_slide()
        rach[4].set_color(O)
        self.play(FadeIn(rach[4], shift=0.2 * RIGHT), run_time=0.6)
        self.next_slide()
        self.play(bso[1].animate.set_color(czarny), rach[4].animate.set_color(czarny), run_time=0.5)
        self.next_slide()
        # Udowodniona nierówność (P4) dla max: podświetlenie, pauza, ptaszek.
        # Tylko końce łańcucha: max{x,y}+max{y,z}-y  ...  = max{x,z}.
        self.play(rach[1].animate.set_color(O), rach[4].animate.set_color(O), run_time=0.5)
        self.next_slide()
        ptaszek = ptaszek_przy(prawe[3])
        self.play(FadeIn(ptaszek, scale=1.5), rach[1].animate.set_color(czarny), rach[4].animate.set_color(czarny))
        self.next_slide()
        self.play(FadeOut(VGroup(*etykiety, *lewe, *prawe, *strzalki, dowod, ptaszek, ptaszki)))

        # Krok 2: układ współrzędnych. Na OX punkty x, y; na OY wartość max{x,y}.
        ax = Axes(
            x_range=[0, 5, 1], y_range=[0, 4, 1],
            x_length=4.5, y_length=3.6,
            tips=False,
            axis_config={"include_numbers": True, "font_size": 24},
        )
        ax.shift(np.array([-2.0, -2.6, 0]) - ax.c2p(0, 0))
        etyk_p = MathTex(r"p", font_size=34).next_to(ax.y_axis, UP, buff=0.15)
        self.play(Create(ax), FadeIn(etyk_p))
        self.next_slide()

        xx = ValueTracker(3.0)
        yy = ValueTracker(1.5)
        kropka_x = always_redraw(lambda: Dot(ax.c2p(xx.get_value(), 0), radius=0.09,
                                             color=KOLOR_CZESCIOWA).set_z_index(10))
        etyk_x = always_redraw(lambda: MathTex("x", font_size=34).next_to(kropka_x, DOWN, buff=0.62))
        kropka_y1 = always_redraw(lambda: Dot(ax.c2p(yy.get_value(), 0), radius=0.09,
                                              color=KOLOR_Y).set_z_index(10))
        etyk_y1 = always_redraw(lambda: MathTex("y", font_size=34).next_to(kropka_y1, DOWN, buff=0.62))
        self.play(FadeIn(kropka_x), FadeIn(etyk_x))
        self.play(FadeIn(kropka_y1), FadeIn(etyk_y1))
        self.next_slide()

        # Kwadrat [0, max{x,y}]^2: jego wysokość na OY to p(x,y).
        def m():
            return max(xx.get_value(), yy.get_value())

        def kolor_m():
            # Pomarańczowy, gdy maksimum to x; fioletowy, gdy y.
            return KOLOR_CZESCIOWA if xx.get_value() >= yy.get_value() else KOLOR_Y

        kwadrat = always_redraw(lambda: Polygon(
            ax.c2p(0, 0), ax.c2p(m(), 0), ax.c2p(m(), m()), ax.c2p(0, m()),
            color=kolor_m(), stroke_width=4).set_fill(kolor_m(), 0.12))
        etyk_pxy = always_redraw(lambda: VGroup(
            MathTex(r"p(x,y)=\max\{x,y\}=", font_size=30, color=kolor_m()),
            DecimalNumber(m(), num_decimal_places=2, font_size=30, color=kolor_m()),
        ).arrange(RIGHT, buff=0.1).next_to(ax.c2p(0, m()), LEFT, buff=0.55))
        self.play(Create(kwadrat), FadeIn(etyk_pxy))
        self.next_slide()

        # Ruszamy punktami: kwadrat zawsze sięga do większego z nich.
        self.play(yy.animate.set_value(4.0), run_time=1.6)
        self.next_slide()
        self.play(xx.animate.set_value(2.0), run_time=1.2)
        self.next_slide()
        self.play(yy.animate.set_value(1.0), run_time=1.6)
        self.next_slide()
        self.play(xx.animate.set_value(3.5), run_time=1.2)
        self.next_slide()
        self.play(xx.animate.set_value(3.0), yy.animate.set_value(1.5), run_time=1.0)
        self.next_slide()

        # Sprzątamy kwadrat i y; zostaje x w punkcie 3 (statyczna kopia).
        kropka_s = Dot(ax.c2p(3, 0), radius=0.09, color=KOLOR_CZESCIOWA).set_z_index(10)
        etyk_s = MathTex("x", font_size=34).next_to(kropka_s, DOWN, buff=0.62)
        self.remove(kropka_x, etyk_x)
        self.add(kropka_s, etyk_s)
        self.play(FadeOut(VGroup(kwadrat, etyk_pxy, kropka_y1, etyk_y1)))
        self.next_slide()

        # 2) Pomarańczowa kreska z x do góry, do wysokości p(x,x).
        slupek_x = Line(ax.c2p(3, 0), ax.c2p(3, 3), color=KOLOR_CZESCIOWA,
                        stroke_width=7).set_cap_style(CapStyleType.ROUND)
        linia_x = DashedLine(ax.c2p(3, 3), ax.c2p(0, 3), color=KOLOR_CZESCIOWA, stroke_width=2)
        podpis_x = MathTex(r"p(x,x)=\max\{x,x\}=3.00", font_size=30, color=KOLOR_CZESCIOWA)
        podpis_x.next_to(ax.c2p(0, 3), LEFT, buff=0.55)
        self.play(Create(slupek_x))
        self.bring_to_front(kropka_s)
        self.play(Create(linia_x), FadeIn(podpis_x))
        self.next_slide()

        # 3) Punkt y na prawo od x i fioletowa kreska do p(y,y).
        y = ValueTracker(4.0)
        kropka_y = always_redraw(lambda: Dot(ax.c2p(y.get_value(), 0), radius=0.09,
                                             color=KOLOR_Y).set_z_index(10))
        etyk_y = always_redraw(lambda: MathTex("y", font_size=34).next_to(kropka_y, DOWN, buff=0.62))
        slupek_y = always_redraw(lambda: Line(
            ax.c2p(y.get_value(), 0), ax.c2p(y.get_value(), max(y.get_value(), 1e-3)),
            color=KOLOR_Y, stroke_width=7,
            stroke_opacity=1 if y.get_value() > 0.02 else 0).set_cap_style(CapStyleType.ROUND))
        linia_y = always_redraw(lambda: DashedLine(
            ax.c2p(y.get_value(), y.get_value()), ax.c2p(0, y.get_value()),
            color=KOLOR_Y, stroke_width=2) if y.get_value() > 0.1 else VMobject())
        podpis_y = always_redraw(lambda: VGroup(
            MathTex(r"p(y,y)=\max\{y,y\}=", font_size=30, color=KOLOR_Y),
            DecimalNumber(y.get_value(), num_decimal_places=2, font_size=30, color=KOLOR_Y),
        ).arrange(RIGHT, buff=0.1).next_to(ax.c2p(0, y.get_value()), LEFT, buff=0.55))
        self.play(FadeIn(kropka_y), FadeIn(etyk_y))
        self.next_slide()
        self.play(Create(slupek_y))
        self.play(Create(linia_y), FadeIn(podpis_y))
        self.next_slide()

        # 4) y jedzie do (0,0) razem z oznaczeniami.
        self.play(y.animate.set_value(0.0), run_time=3.0)
        self.next_slide()

        # 5) Pytanie.
        pytanie = VGroup(
            Tex(r"O którym z punktów", font_size=36),
            Tex(r"wiemy więcej?", font_size=36),
        ).arrange(DOWN, buff=0.15)
        pytanie.move_to([4.0, 0.3, 0])
        self.play(FadeIn(pytanie, shift=0.2 * UP))
        self.next_slide()


class Interpretacja(Slide):
    """Jak rozumieć odległość w metryce częściowej — punkty na kolejne kliknięcia."""

    def construct(self):
        naglowek = Tex(r"Interpretacja", font_size=44).to_edge(UP, buff=0.4)
        self.play(FadeIn(naglowek))
        self.next_slide()

        def punkt(*linie):
            tekst = VGroup(*[Tex(l, font_size=32) for l in linie]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            # Kropka na wysokości środka pierwszej linii.
            y = tekst[0].get_center()[1]
            kropka = Dot(radius=0.045).move_to([tekst.get_left()[0] - 0.3, y, 0])
            return VGroup(kropka, tekst)

        punkty = VGroup(
            punkt(r"Element $x$ to \emph{przybliżenie} --- znamy o nim tylko część informacji."),
            punkt(r"$p(x,x)$ mierzy niedookreśloność $x$ --- im większe, tym mniej o nim wiemy."),
            punkt(r"$p(x,x)=0$ --- element $x$ jest \emph{w pełni określony}."),
            punkt(r"$p(x,y)$ to łączna niepewność $x$ i $y$."),
            punkt(r"$p(x,y)\ge p(x,x)$ --- odległość nie jest mniejsza niż niepewność",
                  r"żadnego z punktów (P2)."),
            punkt(r"$x=y \iff p(x,x)=p(x,y)=p(y,y)$ --- porównanie z $y$ nie wnosi",
                  r"żadnej nowej niepewności (P1)."),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        punkty.next_to(naglowek, DOWN, buff=0.5).to_edge(LEFT, buff=0.6)

        for p in punkty:
            self.play(FadeIn(p, shift=0.2 * RIGHT), run_time=0.6)
            self.next_slide()

        pytanie = Tex(r"A co, jeśli \emph{każdy} punkt jest w pełni określony?",
                      font_size=36).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(pytanie, shift=0.2 * UP))
        self.next_slide()
