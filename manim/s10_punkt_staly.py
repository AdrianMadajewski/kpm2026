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

        uwaga = MathTex(r"\text{Dla } p=d \text{ to twierdzenie Banacha; istnienie dowodzi się tak samo, "
                        r"przez iteracje } x_{n+1}\coloneqq f(x_n).", font_size=28, color=KOLOR_DRUGORZEDNY)
        uwaga.next_to(tw, DOWN, buff=0.35)
        self.play(FadeIn(uwaga, shift=0.2 * RIGHT))
        self.next_slide()

        # ---- Dowód, że p(x*, x*) = 0 ----
        L1 = MathTex(r"\textit{Dowód, że } p(x^*,x^*)=0.\ \text{Skoro }", r"f(x^*)=x^*", r"\text{, to}",
                     font_size=FS)
        L2 = MathTex(r"p(x^*,x^*)", r"=p(f(x^*),f(x^*))", r"\le c\cdot p(x^*,x^*)", r".", font_size=FS + 2)
        L3 = MathTex(r"\text{Zatem }", r"(1-c)\cdot p(x^*,x^*)\le 0", r".", font_size=FS)
        L4 = MathTex(r"\text{Ponieważ }", r"1-c>0", r"\text{ i }", r"p(x^*,x^*)\ge 0", r"\text{, to }",
                     r"p(x^*,x^*)=0", r".", font_size=FS)
        dowod = VGroup(L1, L2, L3, L4).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        dowod.next_to(uwaga, DOWN, buff=0.4).to_edge(LEFT, buff=0.8)
        L2.shift(0.8 * RIGHT)

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

        pokaz(L1, pomaranczowe=[L1[1]])
        wyszarz(L1[1])

        pokaz(L2[0])
        pokaz(L2[1], pomaranczowe=[L2[1]])
        wyszarz(L2[1])
        pokaz_przyp(kontr)
        pokaz(L2[2:], pomaranczowe=[L2[2]])
        wyszarz(L2[2], przyp=kontr)

        pokaz(L3, pomaranczowe=[L3[1]])
        wyszarz(L3[1])

        pokaz(L4[:4], pomaranczowe=[L4[1], L4[3]])
        wyszarz(L4[1], L4[3])
        pokaz(L4[4:], pomaranczowe=[L4[5]])
        wyszarz(L4[5])
        kwadrat = MathTex(r"\blacksquare", font_size=FS).next_to(L4, RIGHT, buff=0.15)
        self.play(FadeIn(kwadrat))
        self.next_slide()
