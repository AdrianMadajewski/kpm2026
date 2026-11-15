from manim_slides import Slide
from common import *


class Kontrakcja(Slide):
    """Punkt stały i kontrakcja: wersja metryczna (niebieska) -> częściowo metryczna, przykład f(x) = x/2 w max."""

    def construct(self):
        FS = 34
        O = KOLOR_CZESCIOWA

        naglowek = Tex(r"Kontrakcje i punkty stałe", font_size=48)
        self.play(FadeIn(naglowek))
        self.next_slide()
        self.play(naglowek.animate.scale(44 / 48).to_edge(UP, buff=0.4), run_time=1.0)
        self.next_slide()

        # ---- Definicja punktu stałego ----
        PS1 = MathTex(r"\textbf{Definicja.}\ \text{Punkt } x^*\in X \text{ nazywamy \emph{punktem stałym} "
                      r"odwzorowania } f\colon X\to X\text{, gdy}", font_size=FS)
        PS2 = MathTex(r"f(x^*)=x^*", r".", font_size=FS + 2)
        PS = VGroup(PS1, PS2).arrange(DOWN, buff=0.25).next_to(naglowek, DOWN, buff=0.4)
        self.play(FadeIn(PS1, shift=0.2 * DOWN))
        self.next_slide()
        PS2[0].set_color(O)
        self.play(FadeIn(PS2, shift=0.2 * DOWN))
        self.next_slide()
        self.play(PS2[0].animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()

        # ---- Definicja kontrakcji w przestrzeni metrycznej ----
        A = Tex(r"\textbf{Definicja.} Odwzorowanie $f\colon X\to X$ nazywamy \emph{kontrakcją} w ", font_size=FS)
        B = MathTex(r"(X,", r"d", r")", font_size=FS)
        C = Tex(r", gdy", font_size=FS)
        wiersz1 = VGroup(A, B, C).arrange(RIGHT, buff=0.12)
        C.next_to(B, RIGHT, buff=0.04).align_to(A, DOWN)
        D = MathTex(r"\exists\,c\in[0,1)\ \ \forall\,x,y\in X\colon\ \ ", r"d", r"(f(x),f(y))\le c\cdot ",
                    r"d", r"(x,y).", font_size=FS + 2)
        definicja = VGroup(wiersz1, D).arrange(DOWN, buff=0.25).next_to(PS, DOWN, buff=0.35)
        self.play(FadeIn(wiersz1, shift=0.2 * DOWN))
        self.next_slide()
        self.play(FadeIn(D, shift=0.2 * DOWN))
        self.next_slide()

        self.play(B.animate.set_color(KOLOR_METRYKA), D.animate.set_color(KOLOR_METRYKA), run_time=0.6)
        self.next_slide()

        # Wspólne fragmenty zostają na miejscu, d przenika w p.
        B2 = MathTex(r"(X,", r"p", r")", font_size=FS, color=O).move_to(B)
        D2 = MathTex(r"\exists\,c\in[0,1)\ \ \forall\,x,y\in X\colon\ \ ", r"p", r"(f(x),f(y))\le c\cdot ",
                     r"p", r"(x,y).", font_size=FS + 2, color=O).move_to(D)
        self.play(*[(FadeTransform if k == 1 else ReplacementTransform)(B[k], B2[k]) for k in range(3)],
                  *[(FadeTransform if k in (1, 3) else ReplacementTransform)(D[k], D2[k]) for k in range(5)],
                  run_time=1.0)
        self.next_slide()
        self.play(B2.animate.set_color(KOLOR_TEKST), D2.animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()

        # ---- Przykład: f(x) = x/2 w max ----
        prz = MathTex(r"\textbf{Przykład.}\ \ X=[0,\infty),\quad p(x,y)=\max\{x,y\},\quad",
                      r"f(x)\coloneqq \tfrac{x}{2}", r".", font_size=32)
        prz.next_to(definicja, DOWN, buff=0.4)
        self.play(FadeIn(prz, shift=0.2 * RIGHT))
        self.next_slide()

        R = MathTex(r"p(f(x),f(y))", r"=\max\Bigl\{\tfrac{x}{2},\tfrac{y}{2}\Bigr\}",
                    r"=\tfrac{1}{2}\max\{x,y\}", r"=\tfrac{1}{2}\,p(x,y)", font_size=36)
        R.next_to(prz, DOWN, buff=0.25)
        self.play(FadeIn(R[0], shift=0.2 * RIGHT))
        self.next_slide()
        for k in (1, 2, 3):
            R[k].set_color(O)
            self.play(FadeIn(R[k], shift=0.2 * RIGHT))
            self.next_slide()
            self.play(R[k].animate.set_color(KOLOR_TEKST), run_time=0.5)

        wn = Tex(r"więc $f$ jest kontrakcją ze stałą $c=\tfrac{1}{2}$.", font_size=34)
        wn.next_to(R, DOWN, buff=0.25)
        self.play(FadeIn(wn, shift=0.2 * RIGHT))
        self.next_slide()

        # Punkt stały w przykładzie.
        ps = MathTex(r"\text{Jedynym punktem stałym } f \text{ jest }", r"x^*=0", r"\text{, przy czym }",
                     r"p(0,0)=0", r".", font_size=34)
        ps.next_to(wn, DOWN, buff=0.25)
        ps[1].set_color(O)
        self.play(FadeIn(ps[:2], shift=0.2 * RIGHT))
        self.next_slide()
        self.play(ps[1].animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()
        ps[3].set_color(O)
        self.play(FadeIn(ps[2:], shift=0.2 * RIGHT))
        self.next_slide()
        self.play(ps[3].animate.set_color(KOLOR_TEKST), run_time=0.6)
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

        # Nagłówek znika, a twierdzenie idzie do góry, żeby zrobić miejsce na dowód.
        self.play(FadeOut(naglowek, shift=0.3 * UP), tw.animate.to_edge(UP, buff=0.35), run_time=0.7)

        # =============== Strona 0: jednoznaczność (prostsza, więc najpierw) ===============
        J1 = MathTex(r"\textit{Dowód.}\ \textit{Jednoznaczność.}\ \text{Niech }", r"f(x)=x", r"\text{ oraz }",
                     r"f(y)=y", r".", font_size=FS)
        J2 = MathTex(r"\text{Wtedy }", r"p(x,y)=p(f(x),f(y))", r"\le c\cdot p(x,y)", r",", font_size=FS)
        J3 = MathTex(r"\text{więc }", r"(1-c)\,p(x,y)\le 0", r"\text{. Ponieważ } c<1 \text{ i } p\ge 0\text{, to }",
                     r"p(x,y)=0", r".", font_size=FS)
        J4 = MathTex(r"\text{Z (P2) i (P3) }", r"p(x,x)\le p(x,y)=0", r"\text{ oraz }",
                     r"p(y,y)\le p(y,x)=p(x,y)=0", r".", font_size=FS)
        J5 = MathTex(r"\text{Zatem }", r"p(x,x)=p(x,y)=p(y,y)", r"\text{, więc z (P1) }", r"x=y", r".",
                     font_size=FS)
        strona0 = VGroup(J1, J2, J3, J4, J5).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        strona0.next_to(tw, DOWN, buff=0.45).to_edge(LEFT, buff=0.6)
        p2p3 = przypomnienie(r"\text{(P2)}\quad p(x,x)\le p(x,y),\qquad \text{(P3)}\quad p(x,y)=p(y,x)")

        pokaz(J1[0])
        pokaz(J1[1:], pomaranczowe=[J1[1], J1[3]])
        wyszarz(J1[1], J1[3])
        pokaz(J2[:2], pomaranczowe=[J2[1]])
        wyszarz(J2[1])
        pokaz_przyp(kontr)
        pokaz(J2[2:], pomaranczowe=[J2[2]])
        wyszarz(J2[2], przyp=kontr)
        pokaz(J3[:2], pomaranczowe=[J3[1]])
        wyszarz(J3[1])
        pokaz(J3[2:], pomaranczowe=[J3[3]])
        wyszarz(J3[3])
        pokaz_przyp(p2p3)
        pokaz(J4[:2], pomaranczowe=[J4[1]])
        wyszarz(J4[1])
        pokaz(J4[2:], pomaranczowe=[J4[3]])
        wyszarz(J4[3], przyp=p2p3)
        pokaz_przyp(p1)
        pokaz(J5[:2], pomaranczowe=[J5[1]])
        wyszarz(J5[1])
        pokaz(J5[2:], pomaranczowe=[J5[3]])
        wyszarz(J5[3], przyp=p1)

        self.play(FadeOut(strona0, shift=0.3 * LEFT), run_time=0.7)
        self.next_slide()

        # =============== Strona 1: oszacowanie p(x_n, x_m) ===============
        A1 = MathTex(r"\textit{Istnienie.}\ \text{Ustalmy } x_0\in X", r"\text{ i niech }",
                     r"x_{n+1}\coloneqq f(x_n)", r"\text{ dla } n=0,1,2,\dots", font_size=FS)
        A2 = MathTex(r"p(x_{n+1},x_n)", r"=p(f(x_n),f(x_{n-1}))", r"\le c\cdot p(x_n,x_{n-1})",
                     r"\le\dots\le c^n\cdot p(x_1,x_0)", r".", font_size=FS)
        A3 = MathTex(r"\text{Niech } m>n.\ \text{Wtedy}", font_size=FS)
        R1 = MathTex(r"p(x_n,x_m)", r"\le p(x_n,x_{n+1})+", r"p(x_{n+1},x_m)", r"-p(x_{n+1},x_{n+1})",
                     font_size=FS)
        R2 = MathTex(r"\le p(x_n,x_{n+1})+", r"p(x_{n+1},x_m)", font_size=FS)
        R3 = MathTex(r"\le p(x_n,x_{n+1})+", r"p(x_{n+1},x_{n+2})+", r"p(x_{n+2},x_m)", r"-p(x_{n+2},x_{n+2})",
                     font_size=FS)
        R3b = MathTex(r"\le p(x_n,x_{n+1})+p(x_{n+1},x_{n+2})+", r"p(x_{n+2},x_{n+3})+p(x_{n+3},x_m)",
                      r"-p(x_{n+3},x_{n+3})", font_size=FS)
        R4 = MathTex(r"\le\dots\le", r"\sum_{k=n}^{m-1}p(x_k,x_{k+1})", r"\le\sum_{k=n}^{m-1}c^k\, p(x_1,x_0)",
                     font_size=FS)
        R5 = MathTex(r"=p(x_1,x_0)\sum_{k=n}^{m-1}c^k", r"\le\frac{c^n}{1-c}\,p(x_1,x_0)", r".", font_size=FS)
        strona1 = VGroup(A1, A2, A3, R1, R2, R3, R3b, R4, R5).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        strona1.next_to(tw, DOWN, buff=0.22).to_edge(LEFT, buff=0.6)
        A2.shift(0.6 * RIGHT)
        R1.shift(0.6 * RIGHT)
        for r in (R2, R3, R3b, R4, R5):
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
        gw1 = MathTex(r"(*)", font_size=FS).next_to(A2, RIGHT, buff=0.4)
        self.play(FadeIn(gw1))
        self.next_slide()

        # (P4) dla trzech punktów x_n, x_{n+1}, x_m.
        p4_a = przypomnienie(r"\text{(P4)}\quad p(x_n,x_m)\le p(x_n,x_{n+1})+p(x_{n+1},x_m)-p(x_{n+1},x_{n+1})")
        pokaz(A3)
        pokaz(R1[0])
        pokaz_przyp(p4_a)
        pokaz(R1[1:], pomaranczowe=[R1[1], R1[2], R1[3]])
        wyszarz(R1[1], R1[2], R1[3], przyp=p4_a)

        # Odejmowany wyraz jest nieujemny: pomijamy go.
        nieuj = przypomnienie(r"p(x_{n+1},x_{n+1})\ge 0")
        self.play(R1[3].animate.set_color(O), FadeIn(nieuj, shift=0.2 * UP), run_time=0.6)
        self.next_slide()
        pokaz(R2)
        wyszarz(R1[3], przyp=nieuj)

        # To samo dla p(x_{n+1}, x_m): (P4) z y = x_{n+2}.
        self.play(R2[1].animate.set_color(O), run_time=0.5)
        self.next_slide()
        p4_b = przypomnienie(r"\text{(P4)}\quad p(x_{n+1},x_m)\le p(x_{n+1},x_{n+2})+p(x_{n+2},x_m)"
                             r"-p(x_{n+2},x_{n+2})")
        pokaz_przyp(p4_b)
        pokaz(R3, pomaranczowe=[R3[1], R3[2], R3[3]])
        wyszarz(R2[1], R3[1], R3[2], R3[3], przyp=p4_b)
        # Odejmowany wyraz jest nieujemny: zapominamy o nim.
        nieuj_b = przypomnienie(r"p(x_{n+2},x_{n+2})\ge 0")
        self.play(R3[3].animate.set_color(O), FadeIn(nieuj_b, shift=0.2 * UP), run_time=0.6)
        self.next_slide()
        czlon_b = R3[3]
        self.play(FadeOut(czlon_b, shift=0.2 * DOWN), FadeOut(nieuj_b, shift=0.2 * DOWN), run_time=0.6)
        R3.remove(czlon_b)  # inaczej wraca przy FadeOut całej strony
        self.next_slide()

        # Jeszcze raz (P4) dla p(x_{n+2}, x_m).
        self.play(R3[2].animate.set_color(O), run_time=0.5)
        self.next_slide()
        p4_d = przypomnienie(r"\text{(P4)}\quad p(x_{n+2},x_m)\le p(x_{n+2},x_{n+3})+p(x_{n+3},x_m)"
                             r"-p(x_{n+3},x_{n+3})")
        pokaz_przyp(p4_d)
        pokaz(R3b, pomaranczowe=[R3b[1], R3b[2]])
        wyszarz(R3[2], R3b[1], R3b[2], przyp=p4_d)
        nieuj_d = przypomnienie(r"p(x_{n+3},x_{n+3})\ge 0")
        self.play(R3b[2].animate.set_color(O), FadeIn(nieuj_d, shift=0.2 * UP), run_time=0.6)
        self.next_slide()
        czlon_d = R3b[2]
        self.play(FadeOut(czlon_d, shift=0.2 * DOWN), FadeOut(nieuj_d, shift=0.2 * DOWN), run_time=0.6)
        R3b.remove(czlon_d)
        self.next_slide()

        # Suma i szereg geometryczny.
        pokaz(R4[:2], pomaranczowe=[R4[1]])
        wyszarz(R4[1])
        self.play(A2[3].animate.set_color(O), run_time=0.5)
        self.next_slide()
        pokaz(R4[2], pomaranczowe=[R4[2]])
        wyszarz(R4[2], A2[3])
        # Wyłączenie stałej przed sumę (bez kolorów).
        pokaz(R5[0])
        geom = MathTex(r"\sum_{k=n}^{m-1}c^k\le\sum_{k=n}^{\infty}c^k=\frac{c^n}{1-c}", font_size=26, color=O)
        geom.to_edge(DOWN, buff=0.2)
        pokaz_przyp(geom)
        pokaz(R5[1:], pomaranczowe=[R5[1]])
        wyszarz(R5[1], przyp=geom)

        self.play(FadeOut(strona1, shift=0.3 * LEFT), FadeOut(gw1, shift=0.3 * LEFT), run_time=0.7)
        self.next_slide()

        # =============== Strona 2: ciąg iteracji jest ciągiem Cauchy'ego ===============
        A0r = MathTex(r"(*)\quad", r"p(x_{n+1},x_n)\le c^n\cdot p(x_1,x_0)", r"\text{ dla } n\ge 0.", font_size=FS)
        A4r = MathTex(r"\text{Dla } m>n \text{ mamy }", r"p(x_n,x_m)\le\frac{c^n}{1-c}\,p(x_1,x_0)", r".",
                      font_size=FS)
        A5 = MathTex(r"\text{Dla } m=n \text{ mamy }", r"p(x_n,x_n)", r"\le p(x_n,x_{n+1})",
                     r"\le c^n\, p(x_1,x_0)", r".", font_size=FS)
        A5b = MathTex(r"\text{Zatem }", r"\lim_{n\to\infty}p(x_n,x_n)=0", r".", font_size=FS)
        C1 = MathTex(r"\text{Ustalmy } N\in\mathbb{N}\text{ i niech } n,m\ge N.", r"\ \text{Z (P3) możemy założyć, że }",
                     r"m\ge n", r".", font_size=FS)
        C2 = MathTex(r"\text{Wtedy }", r"p(x_n,x_m)\le\frac{c^n}{1-c}\,p(x_1,x_0)", r"\le\frac{c^N}{1-c}\,p(x_1,x_0)",
                     r".", font_size=FS)
        C3 = MathTex(r"\text{Ponieważ }", r"\frac{c^N}{1-c}\,p(x_1,x_0)\xrightarrow[N\to\infty]{}0",
                     r"\text{, to }", r"\lim_{n,m\to\infty}p(x_n,x_m)=0", r",", font_size=FS)
        C4 = MathTex(r"\text{czyli }", r"(x_n)_{n\in\mathbb{N}}\text{ jest ciągiem Cauchy'ego}", r".", font_size=FS)
        strona2 = VGroup(A0r, A4r, A5, A5b, C1, C2, C3, C4).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        strona2.next_to(tw, DOWN, buff=0.3).to_edge(LEFT, buff=0.6)

        cn0 = przypomnienie(r"c\in[0,1)\implies c^n\xrightarrow[n\to\infty]{}0")
        p3 = przypomnienie(r"\text{(P3)}\quad p(x,y)=p(y,x)")
        m_eq_n = przypomnienie(r"\text{dla } m=n\text{:}\quad c^n\le\frac{c^n}{1-c}")
        cN = przypomnienie(r"n\ge N \implies c^n\le c^N")

        # Przypomnienie wyników z poprzedniej strony.
        pokaz(A0r)
        pokaz(A4r)
        # Przypadek m = n.
        pokaz(A5[:2])
        pokaz_przyp(p2)
        pokaz(A5[2], pomaranczowe=[A5[2]])
        wyszarz(A5[2], przyp=p2)
        self.play(A0r[1].animate.set_color(O), run_time=0.6)
        self.next_slide()
        pokaz(A5[3:], pomaranczowe=[A5[3]])
        self.play(A5[3].animate.set_color(KOLOR_TEKST), A0r[1].animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()
        pokaz_przyp(cn0)
        pokaz(A5b, pomaranczowe=[A5b[1]])
        wyszarz(A5b[1], przyp=cn0)

        # Wspólne oszacowanie dla n, m >= N.
        pokaz(C1[0])
        pokaz_przyp(p3)
        pokaz(C1[1:], pomaranczowe=[C1[2]])
        wyszarz(C1[2], przyp=p3)
        # Pierwsza nierówność: z linijek "m > n" i "m = n".
        self.play(A4r[1].animate.set_color(O), A5[3].animate.set_color(O), run_time=0.6)
        self.next_slide()
        pokaz_przyp(m_eq_n)
        pokaz(C2[:2], pomaranczowe=[C2[1]])
        self.play(A4r[1].animate.set_color(KOLOR_TEKST), A5[3].animate.set_color(KOLOR_TEKST),
                  C2[1].animate.set_color(KOLOR_TEKST), FadeOut(m_eq_n, shift=0.2 * DOWN), run_time=0.6)
        self.next_slide()
        pokaz_przyp(cN)
        pokaz(C2[2:], pomaranczowe=[C2[2]])
        wyszarz(C2[2], przyp=cN)
        # Granica.
        cN0 = przypomnienie(r"c\in[0,1)\implies c^N\xrightarrow[N\to\infty]{}0")
        pokaz_przyp(cN0)
        pokaz(C3[:2], pomaranczowe=[C3[1]])
        wyszarz(C3[1], przyp=cN0)
        pokaz(C3[2:], pomaranczowe=[C3[3]])
        wyszarz(C3[3])
        pokaz(C4)

        self.play(FadeOut(strona2, shift=0.3 * LEFT), run_time=0.7)
        self.next_slide()

        # =============== Strona 3: granica jest punktem stałym ===============
        B1 = MathTex(r"\text{Z zupełności istnieje } x^*\in X\text{ taki, że }", r"x_n\to x^*", r"\text{ oraz }",
                     r"p(x^*,x^*)=\lim_{n,m\to\infty}p(x_n,x_m)=0", r".", font_size=FS)
        B2 = MathTex(r"\textit{Punkt stały.}\ \text{Dla } n\in\mathbb{N}\text{ mamy}", font_size=FS)
        B3 = MathTex(r"p(x^*,f(x^*))", r"\le p(x^*,x_{n+1})+p(x_{n+1},f(x^*))", r"-p(x_{n+1},x_{n+1})",
                     font_size=FS)
        B3b = MathTex(r"\le p(x^*,x_{n+1})+p(x_{n+1},f(x^*))", font_size=FS)
        B3c = MathTex(r"=p(x^*,x_{n+1})+", r"p(f(x_n),f(x^*))", font_size=FS)
        B3d = MathTex(r"\le p(x^*,x_{n+1})+", r"c\cdot p(x_n,x^*)", r"\xrightarrow[n\to\infty]{}0", r".",
                      font_size=FS)
        B4 = MathTex(r"\text{Zatem }", r"p(x^*,f(x^*))=0", r"\text{, a z (P2) }",
                     r"p(x^*,x^*)=p(f(x^*),f(x^*))=0", r"\text{, więc z (P1) }", r"f(x^*)=x^*", r".", font_size=FS)
        strona3 = VGroup(B1, B2, B3, B3b, B3c, B3d, B4).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        strona3.next_to(tw, DOWN, buff=0.35).to_edge(LEFT, buff=0.6)
        B3.shift(0.6 * RIGHT)
        for r in (B3b, B3c, B3d):
            r.align_to(B3[1], LEFT)

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
        p4_c = przypomnienie(r"\text{(P4)}\quad p(x^*,f(x^*))\le p(x^*,x_{n+1})+p(x_{n+1},f(x^*))"
                             r"-p(x_{n+1},x_{n+1})")
        pokaz(B2)
        pokaz(B3[0])
        pokaz_przyp(p4_c)
        pokaz(B3[1:], pomaranczowe=[B3[1], B3[2]])
        wyszarz(B3[1], B3[2], przyp=p4_c)
        # Odejmowany wyraz jest nieujemny: pomijamy go.
        nieuj_c = przypomnienie(r"p(x_{n+1},x_{n+1})\ge 0")
        self.play(B3[2].animate.set_color(O), FadeIn(nieuj_c, shift=0.2 * UP), run_time=0.6)
        self.next_slide()
        pokaz(B3b)
        wyszarz(B3[2], przyp=nieuj_c)
        # x_{n+1} = f(x_n).
        iter_c = przypomnienie(r"x_{n+1}=f(x_n)")
        pokaz_przyp(iter_c)
        pokaz(B3c, pomaranczowe=[B3c[1]])
        wyszarz(B3c[1], przyp=iter_c)
        # Kontrakcja.
        pokaz_przyp(kontr)
        pokaz(B3d[:2], pomaranczowe=[B3d[1]])
        wyszarz(B3d[1], przyp=kontr)
        # Zbieżność do x*.
        zb_c = przypomnienie(r"x_n\to x^*\implies p(x^*,x_n)\xrightarrow[n\to\infty]{}p(x^*,x^*)=0")
        pokaz_przyp(zb_c)
        pokaz(B3d[2:], pomaranczowe=[B3d[2]])
        wyszarz(B3d[2], przyp=zb_c)
        pokaz(B4[:2], pomaranczowe=[B4[1]])
        wyszarz(B4[1])
        pokaz_przyp(p2)
        pokaz(B4[2:4], pomaranczowe=[B4[3]])
        wyszarz(B4[3], przyp=p2)
        pokaz_przyp(p1)
        pokaz(B4[4:], pomaranczowe=[B4[5]])
        wyszarz(B4[5], przyp=p1)

        kwadrat = MathTex(r"\blacksquare", font_size=FS).next_to(B4, RIGHT, buff=0.15)
        self.play(FadeIn(kwadrat))
        self.next_slide()
