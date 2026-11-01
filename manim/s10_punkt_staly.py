from manim_slides import Slide
from common import *


class Kontrakcja(Slide):
    """Kontrakcja: wersja metryczna (niebieska) -> częściowo metryczna, potem przykład f(x) = x/2 w max."""

    def construct(self):
        FS = 34
        O = KOLOR_CZESCIOWA

        naglowek = Tex(r"Kontrakcje", font_size=48)
        self.play(FadeIn(naglowek))
        self.next_slide()
        self.play(naglowek.animate.scale(44 / 48).to_edge(UP, buff=0.4), run_time=1.0)
        self.next_slide()

        # ---- Definicja w przestrzeni metrycznej ----
        A = Tex(r"\textbf{Definicja.} Odwzorowanie $f\colon X\to X$ nazywamy \emph{kontrakcją} w ", font_size=FS)
        B = MathTex(r"(X,d)", font_size=FS)
        C = Tex(r", gdy", font_size=FS)
        wiersz1 = VGroup(A, B, C).arrange(RIGHT, buff=0.12)
        C.next_to(B, RIGHT, buff=0.04).align_to(A, DOWN)
        D = MathTex(r"\exists\,c\in[0,1)\ \ \forall\,x,y\in X\colon\ \ d(f(x),f(y))\le c\cdot d(x,y).",
                    font_size=FS + 2)
        definicja = VGroup(wiersz1, D).arrange(DOWN, buff=0.35).next_to(naglowek, DOWN, buff=0.5)
        self.play(FadeIn(wiersz1, shift=0.2 * DOWN))
        self.next_slide()
        self.play(FadeIn(D, shift=0.2 * DOWN))
        self.next_slide()

        self.play(B.animate.set_color(KOLOR_METRYKA), D.animate.set_color(KOLOR_METRYKA), run_time=0.6)
        self.next_slide()

        B2 = MathTex(r"(X,p)", font_size=FS, color=O).move_to(B)
        D2 = MathTex(r"\exists\,c\in[0,1)\ \ \forall\,x,y\in X\colon\ \ p(f(x),f(y))\le c\cdot p(x,y).",
                     font_size=FS + 2, color=O).move_to(D)
        self.play(TransformMatchingShapes(B, B2), TransformMatchingShapes(D, D2), run_time=1.2)
        self.next_slide()
        self.play(B2.animate.set_color(KOLOR_TEKST), D2.animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()

        # ---- Przykład: f(x) = x/2 w max ----
        prz = MathTex(r"\textbf{Przykład.}\ \ X=[0,\infty),\quad p(x,y)=\max\{x,y\},\quad",
                      r"f(x)\coloneqq \tfrac{x}{2}", r".", font_size=32)
        prz.next_to(definicja, DOWN, buff=0.7)
        self.play(FadeIn(prz, shift=0.2 * RIGHT))
        self.next_slide()

        R = MathTex(r"p(f(x),f(y))", r"=\max\Bigl\{\tfrac{x}{2},\tfrac{y}{2}\Bigr\}",
                    r"=\tfrac{1}{2}\max\{x,y\}", r"=\tfrac{1}{2}\,p(x,y)", font_size=36)
        R.next_to(prz, DOWN, buff=0.4)
        self.play(FadeIn(R[0], shift=0.2 * RIGHT))
        self.next_slide()
        for k in (1, 2, 3):
            R[k].set_color(O)
            self.play(FadeIn(R[k], shift=0.2 * RIGHT))
            self.next_slide()
            self.play(R[k].animate.set_color(KOLOR_TEKST), run_time=0.5)

        wn = Tex(r"więc $f$ jest kontrakcją ze stałą $c=\tfrac{1}{2}$.", font_size=34)
        wn.next_to(R, DOWN, buff=0.4)
        self.play(FadeIn(wn, shift=0.2 * RIGHT))
        self.wait(0.2)
        self.next_slide()


class TwierdzenieMatthewsa(Slide):
    """Twierdzenie Matthewsa o punkcie stałym i dowód, że p(x*, x*) = 0."""

    def construct(self):
        FS = 32
        O = KOLOR_CZESCIOWA

        naglowek = Tex(r"Twierdzenie o punkcie stałym", font_size=48)
        self.play(FadeIn(naglowek))
        self.next_slide()
        self.play(naglowek.animate.scale(44 / 48).to_edge(UP, buff=0.4), run_time=1.0)
        self.next_slide()

        tw = VGroup(
            MathTex(r"\textbf{Twierdzenie}\ \text{(Matthews, 1994)}\textbf{.}\ \text{Niech } (X,p)"
                    r"\text{ będzie zupełną przestrzenią}", font_size=34),
            MathTex(r"\text{częściowo metryczną, a } f\colon X\to X \text{ kontrakcją.}", font_size=34),
            MathTex(r"\text{Wtedy } f \text{ ma dokładnie jeden punkt stały } x^*\in X", r"\text{ oraz }",
                    r"p(x^*,x^*)=0", r".", font_size=34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        tw.next_to(naglowek, DOWN, buff=0.5)
        self.play(FadeIn(tw[0], shift=0.2 * DOWN))
        self.play(FadeIn(tw[1], shift=0.2 * DOWN))
        self.next_slide()
        self.play(FadeIn(tw[2][0], shift=0.2 * RIGHT))
        self.next_slide()
        tw[2][2].set_color(O)
        self.play(FadeIn(tw[2][1:], shift=0.2 * RIGHT))
        self.next_slide()
        self.play(tw[2][2].animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()

        FS = 29

        def przypomnienie(tex):
            return MathTex(tex, font_size=30, color=O).to_edge(DOWN, buff=0.35)

        def pokaz(*czesci, pomaranczowe=()):
            for c in pomaranczowe:
                c.set_color(O)
            self.play(*[FadeIn(c, shift=0.2 * RIGHT) for c in czesci])
            self.next_slide()

        def wyszarz(*czesci, przyp=None):
            anims = [c.animate.set_color(KOLOR_TEKST) for c in czesci]
            if przyp is not None:
                anims.append(FadeOut(przyp, shift=0.2 * DOWN))
            self.play(*anims, run_time=0.6)
            self.next_slide()

        def pokaz_przyp(przyp):
            self.play(FadeIn(przyp, shift=0.2 * UP))
            self.next_slide()

        kontr = przypomnienie(r"\text{(kontrakcja)}\quad p(f(x),f(y))\le c\cdot p(x,y),\quad c\in[0,1)")
        p1 = przypomnienie(r"\text{(P1)}\quad x=y \iff p(x,x)=p(x,y)=p(y,y)")
        p2 = przypomnienie(r"\text{(P2)}\quad p(x,x)\le p(x,y)")
        p4 = przypomnienie(r"\text{(P4)}\quad p(x,z)\le p(x,y)+p(y,z)-p(y,y)")
        zup = przypomnienie(r"\text{(zupełność)}\quad x_n\to x^*,\quad "
                            r"p(x^*,x^*)=\lim_{n\to\infty}p(x^*,x_n)=\lim_{n,m\to\infty}p(x_n,x_m)")

        # =============== Strona 1: oszacowanie p(x_n, x_m) ===============
        A1 = MathTex(r"\textit{Dowód.}\ \textit{Istnienie.}\ \text{Ustalmy } x_0\in X", r"\text{ i niech }",
                     r"x_{n+1}\coloneqq f(x_n)", r"\text{ dla } n=0,1,2,\dots", font_size=FS)
        A2 = MathTex(r"p(x_{n+1},x_n)", r"=p(f(x_n),f(x_{n-1}))", r"\le c\cdot p(x_n,x_{n-1})",
                     r"\le\dots\le c^n\cdot p(x_1,x_0)", r".", font_size=FS)
        A3 = MathTex(r"\text{Niech } m>n.\ \text{Dla } x=x_n,\ y=x_{n+1},\ z=x_m\text{ mamy}", font_size=FS)
        R1 = MathTex(r"p(x_n,x_m)", r"\le p(x_n,x_{n+1})+", r"p(x_{n+1},x_m)", r"-p(x_{n+1},x_{n+1})",
                     font_size=FS)
        R2 = MathTex(r"\le p(x_n,x_{n+1})+", r"p(x_{n+1},x_m)", font_size=FS)
        R3 = MathTex(r"\le p(x_n,x_{n+1})+", r"p(x_{n+1},x_{n+2})+p(x_{n+2},x_m)", font_size=FS)
        R4 = MathTex(r"\le\dots\le", r"\sum_{k=n}^{m-1}p(x_k,x_{k+1})", r"\le\sum_{k=n}^{m-1}c^k\, p(x_1,x_0)",
                     r"\le\frac{c^n}{1-c}\,p(x_1,x_0)", r".", font_size=FS)
        strona1 = VGroup(A1, A2, A3, R1, R2, R3, R4).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        strona1.next_to(tw, DOWN, buff=0.25).to_edge(LEFT, buff=0.6)
        A2.shift(0.6 * RIGHT)
        R1.shift(0.6 * RIGHT)
        for r in (R2, R3, R4):
            r.align_to(R1[1], LEFT)

        pokaz(A1[0])
        pokaz(A1[1:], pomaranczowe=[A1[2]])
        wyszarz(A1[2])

        pokaz(A2[0])
        pokaz(A2[1], pomaranczowe=[A2[1]])
        wyszarz(A2[1])
        pokaz_przyp(kontr)
        pokaz(A2[2], pomaranczowe=[A2[2]])
        wyszarz(A2[2])
        pokaz(A2[3:], pomaranczowe=[A2[3]])
        wyszarz(A2[3], przyp=kontr)

        # (P4) dla trzech punktów x_n, x_{n+1}, x_m.
        pokaz(A3)
        pokaz(R1[0])
        pokaz_przyp(p4)
        pokaz(R1[1:], pomaranczowe=[R1[1], R1[2], R1[3]])
        wyszarz(R1[1], R1[2], R1[3], przyp=p4)

        # Odejmowany wyraz jest nieujemny: pomijamy go.
        nieuj = przypomnienie(r"p(x_{n+1},x_{n+1})\ge 0")
        self.play(R1[3].animate.set_color(O), FadeIn(nieuj, shift=0.2 * UP), run_time=0.6)
        self.next_slide()
        pokaz(R2)
        wyszarz(R1[3], przyp=nieuj)

        # To samo dla p(x_{n+1}, x_m): (P4) z y = x_{n+2}.
        self.play(R2[1].animate.set_color(O), run_time=0.5)
        self.next_slide()
        notka = MathTex(r"(x=x_{n+1},\ y=x_{n+2},\ z=x_m)", font_size=26, color=O)
        notka.next_to(R3, RIGHT, buff=0.5)
        self.play(FadeIn(p4, shift=0.2 * UP), FadeIn(notka, shift=0.2 * LEFT))
        self.next_slide()
        pokaz(R3, pomaranczowe=[R3[1]])
        self.play(R2[1].animate.set_color(KOLOR_TEKST), R3[1].animate.set_color(KOLOR_TEKST),
                  notka.animate.set_color(KOLOR_DRUGORZEDNY), FadeOut(p4, shift=0.2 * DOWN), run_time=0.6)
        self.next_slide()

        # Suma i szereg geometryczny.
        pokaz(R4[:2], pomaranczowe=[R4[1]])
        wyszarz(R4[1])
        self.play(A2[3].animate.set_color(O), run_time=0.5)
        self.next_slide()
        pokaz(R4[2], pomaranczowe=[R4[2]])
        wyszarz(R4[2], A2[3])
        geom = MathTex(r"\sum_{k=n}^{m-1}c^k\le\sum_{k=n}^{\infty}c^k=\frac{c^n}{1-c}", font_size=26, color=O)
        geom.to_corner(DR, buff=0.3)
        pokaz_przyp(geom)
        pokaz(R4[3:], pomaranczowe=[R4[3]])
        wyszarz(R4[3], przyp=geom)

        self.play(FadeOut(strona1, shift=0.3 * LEFT), run_time=0.7)
        self.next_slide()

        # =============== Strona 2: ciąg Cauchy'ego, granica, punkt stały ===============
        A5 = MathTex(r"\text{Z (P2) także }", r"p(x_n,x_n)\le p(x_n,x_{n+1})\le c^n\, p(x_1,x_0)", r".",
                     font_size=FS)
        A6 = MathTex(r"\text{Zatem }", r"\lim_{n,m\to\infty}p(x_n,x_m)=0", r"\text{, czyli }",
                     r"(x_n)_{n\ge 0}\text{ jest ciągiem Cauchy'ego}", r".", font_size=FS)

        B1 = MathTex(r"\text{Z zupełności istnieje } x^*\in X\text{ taki, że }", r"x_n\to x^*", r"\text{ oraz }",
                     r"p(x^*,x^*)=\lim_{n,m\to\infty}p(x_n,x_m)=0", r".", font_size=FS)
        B2 = MathTex(r"\textit{Punkt stały.}\ \text{Z (P4) i kontrakcji, skoro } x_{n+1}=f(x_n)\text{:}", font_size=FS)
        B3 = MathTex(r"p(x^*,f(x^*))", r"\le p(x^*,x_{n+1})+p(f(x_n),f(x^*))", r"\le p(x^*,x_{n+1})+c\cdot p(x_n,x^*)",
                     r"\xrightarrow[n\to\infty]{}0", r".", font_size=FS)
        B4 = MathTex(r"\text{Zatem }", r"p(x^*,f(x^*))=0", r"\text{, a z (P2) }",
                     r"p(x^*,x^*)=p(f(x^*),f(x^*))=0", r"\text{, więc z (P1) }", r"f(x^*)=x^*", r".", font_size=FS)
        B5 = MathTex(r"\textit{Jednoznaczność.}\ \text{Jeśli } f(y)=y\text{, to }",
                     r"p(x^*,y)=p(f(x^*),f(y))\le c\cdot p(x^*,y)", r"\text{, więc }", r"p(x^*,y)=0", r".",
                     font_size=FS)
        B6 = MathTex(r"\text{Z (P2) }", r"p(x^*,x^*)=p(x^*,y)=p(y,y)=0", r"\text{, więc z (P1) }", r"y=x^*",
                     r".", font_size=FS)
        strona2 = VGroup(A5, A6, B1, B2, B3, B4).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        strona2.next_to(tw, DOWN, buff=0.35).to_edge(LEFT, buff=0.6)
        B3.shift(0.6 * RIGHT)
        strona3 = VGroup(B5, B6).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        strona3.next_to(tw, DOWN, buff=0.4).to_edge(LEFT, buff=0.6)

        pokaz_przyp(p2)
        pokaz(A5, pomaranczowe=[A5[1]])
        wyszarz(A5[1], przyp=p2)
        pokaz(A6[:2], pomaranczowe=[A6[1]])
        wyszarz(A6[1])
        pokaz(A6[2:])

        # Zupełność: granica x* i od razu p(x*, x*) = 0.
        pokaz_przyp(zup)
        pokaz(B1[:2], pomaranczowe=[B1[1]])
        pokaz(B1[2:], pomaranczowe=[B1[3]])
        wyszarz(B1[1], B1[3], przyp=zup)
        # To już jest druga część tezy.
        self.play(B1[3].animate.set_color(O), tw[2][2].animate.set_color(O), run_time=0.6)
        self.next_slide()
        wyszarz(B1[3], tw[2][2])

        # f(x*) = x*.
        pokaz(B2)
        pokaz_przyp(p4)
        pokaz(B3[:2], pomaranczowe=[B3[1]])
        wyszarz(B3[1], przyp=p4)
        pokaz_przyp(kontr)
        pokaz(B3[2], pomaranczowe=[B3[2]])
        wyszarz(B3[2], przyp=kontr)
        pokaz(B3[3:], pomaranczowe=[B3[3]])
        wyszarz(B3[3])
        pokaz(B4[:2], pomaranczowe=[B4[1]])
        wyszarz(B4[1])
        pokaz_przyp(p2)
        pokaz(B4[2:4], pomaranczowe=[B4[3]])
        wyszarz(B4[3], przyp=p2)
        pokaz_przyp(p1)
        pokaz(B4[4:], pomaranczowe=[B4[5]])
        wyszarz(B4[5], przyp=p1)

        self.play(FadeOut(strona2, shift=0.3 * LEFT), run_time=0.7)
        self.next_slide()

        # Jednoznaczność.
        pokaz(B5[0])
        pokaz_przyp(kontr)
        pokaz(B5[1], pomaranczowe=[B5[1]])
        wyszarz(B5[1], przyp=kontr)
        pokaz(B5[2:], pomaranczowe=[B5[3]])
        wyszarz(B5[3])
        pokaz_przyp(p2)
        pokaz(B6[:2], pomaranczowe=[B6[1]])
        wyszarz(B6[1], przyp=p2)
        pokaz_przyp(p1)
        pokaz(B6[2:], pomaranczowe=[B6[3]])
        wyszarz(B6[3], przyp=p1)
        kwadrat = MathTex(r"\blacksquare", font_size=FS).next_to(B6, RIGHT, buff=0.15)
        self.play(FadeIn(kwadrat))
        self.next_slide()
