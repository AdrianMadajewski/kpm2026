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
