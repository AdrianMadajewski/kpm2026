from manim_slides import Slide
from common import *


TYTUL_ZUP = r"Zupełność"


class CiagCauchyego(Slide):
    """Ciąg Cauchy'ego: od wersji metrycznej do częściowo metrycznej, potem przykład w max."""

    def construct(self):
        FS = 34
        O = KOLOR_CZESCIOWA
        KOLOR_Y = ManimColor("#7B3FA0")

        naglowek = Tex(TYTUL_ZUP, font_size=48)
        self.play(FadeIn(naglowek))
        self.next_slide()
        self.play(naglowek.animate.scale(44 / 48).to_edge(UP, buff=0.4), run_time=1.0)
        self.next_slide()

        # ---- Definicja w przestrzeni metrycznej ----
        A = Tex(r"\textbf{Definicja.} Ciąg $(x_n)_{n\in\mathbb{N}}\subset X$ jest \emph{ciągiem Cauchy'ego} w ",
                font_size=FS)
        B = MathTex(r"(X,d)", font_size=FS)
        C = Tex(r", gdy", font_size=FS)
        wiersz1 = VGroup(A, B, C).arrange(RIGHT, buff=0.12)
        C.next_to(B, RIGHT, buff=0.04).align_to(A, DOWN)
        D = MathTex(r"\forall\,\varepsilon>0\ \ \exists\,N\in\mathbb{N}\ \ \forall\,n,m\ge N\colon\ \ "
                    r"d(x_n,x_m)<\varepsilon.", font_size=FS + 2)
        wiersz2 = VGroup(D)
        definicja = VGroup(wiersz1, wiersz2).arrange(DOWN, buff=0.35).next_to(naglowek, DOWN, buff=0.6)
        self.play(FadeIn(wiersz1, shift=0.2 * DOWN))
        self.play(FadeIn(wiersz2, shift=0.2 * DOWN))
        self.next_slide()

        # Podświetlenie na niebiesko: przestrzeń metryczna i warunek Cauchy'ego.
        self.play(B.animate.set_color(KOLOR_METRYKA), D.animate.set_color(KOLOR_METRYKA), run_time=0.6)
        self.next_slide()

        # Przejście do metryki częściowej: d -> p, warunek z "granicą" a.
        B2 = MathTex(r"(X,p)", font_size=FS, color=O).move_to(B)
        D2 = MathTex(r"\exists\,a\in\mathbb{R}\ \ \forall\,\varepsilon>0\ \ \exists\,N\in\mathbb{N}\ \ "
                     r"\forall\,n,m\ge N\colon\ \ |p(x_n,x_m)-a|<\varepsilon.", font_size=FS + 2, color=O)
        D2.move_to(D)
        self.play(TransformMatchingShapes(B, B2), TransformMatchingShapes(D, D2), run_time=1.2)
        self.next_slide()
        self.play(B2.animate.set_color(KOLOR_TEKST), D2.animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()

        # ---- Przykład w max ----
        prz = MathTex(r"\textbf{Przykład.}\ \ X=[0,\infty),\quad p(x,y)=\max\{x,y\},\quad",
                      r"x_n\coloneqq 1+\tfrac{1}{n}", r"\ \text{ dla } n\in\mathbb{N}.", font_size=32)
        prz[1].set_color(KOLOR_Y)
        prz.next_to(definicja, DOWN, buff=0.7)
        self.play(FadeIn(prz, shift=0.2 * RIGHT))
        self.next_slide()

        R = MathTex(r"p(x_n,x_m)", r"=\max\Bigl\{1+\tfrac{1}{n},\,1+\tfrac{1}{m}\Bigr\}",
                    r"=1+\frac{1}{\min\{n,m\}}", r"\xrightarrow[n,m\to\infty]{}1", font_size=34)
        R.next_to(prz, DOWN, buff=0.45)
        self.play(FadeIn(R[0], shift=0.2 * RIGHT))
        self.next_slide()
        for k in (1, 2, 3):
            R[k].set_color(O)
            self.play(FadeIn(R[k], shift=0.2 * RIGHT))
            self.next_slide()
            self.play(R[k].animate.set_color(KOLOR_TEKST), run_time=0.5)
        wn = Tex(r"więc $(x_n)_{n\in\mathbb{N}}$ jest ciągiem Cauchy'ego z $a=1\neq 0$.",
                 font_size=32)
        wn.next_to(R, DOWN, buff=0.4)
        self.play(FadeIn(wn, shift=0.2 * RIGHT))
        self.wait(0.2)
        self.next_slide()
