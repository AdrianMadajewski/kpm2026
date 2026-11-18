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
        B = MathTex(r"(X,", r"d", r")", font_size=FS)
        C = Tex(r", gdy", font_size=FS)
        wiersz1 = VGroup(A, B, C).arrange(RIGHT, buff=0.12)
        C.next_to(B, RIGHT, buff=0.04).align_to(A, DOWN)
        D = MathTex(r"\forall\,\varepsilon>0\ \ \exists\,N\in\mathbb{N}\ \ \forall\,n,m\ge N\colon\ \ ",
                    r"d", r"(x_n,x_m)", r"<\varepsilon.", font_size=FS + 2)
        wiersz2 = VGroup(D)
        definicja = VGroup(wiersz1, wiersz2).arrange(DOWN, buff=0.35).next_to(naglowek, DOWN, buff=0.35)
        self.play(FadeIn(wiersz1, shift=0.2 * DOWN))
        self.play(FadeIn(wiersz2, shift=0.2 * DOWN))
        self.next_slide()

        # Podświetlenie na niebiesko: przestrzeń metryczna i warunek Cauchy'ego.
        self.play(B.animate.set_color(KOLOR_METRYKA), D.animate.set_color(KOLOR_METRYKA), run_time=0.6)
        self.next_slide()

        # Przejście do metryki częściowej: d -> p, warunek z "granicą" a.
        # Wspólne fragmenty przesuwają się na miejsce, d zmienia się w p, nowe części się pojawiają.
        B2 = MathTex(r"(X,", r"p", r")", font_size=FS, color=O).move_to(B)
        D2 = MathTex(r"\exists\,a\in\mathbb{R}\ \ ",
                     r"\forall\,\varepsilon>0\ \ \exists\,N\in\mathbb{N}\ \ \forall\,n,m\ge N\colon\ \ ",
                     r"|", r"p", r"(x_n,x_m)", r"-a|", r"<\varepsilon.", font_size=FS + 2, color=O)
        D2.move_to(D)
        self.play(
            ReplacementTransform(B[0], B2[0]), FadeTransform(B[1], B2[1]), ReplacementTransform(B[2], B2[2]),
            ReplacementTransform(D[0], D2[1]), FadeTransform(D[1], D2[3]),
            ReplacementTransform(D[2], D2[4]), ReplacementTransform(D[3], D2[6]),
            run_time=1.0,
        )
        self.play(FadeIn(D2[0], shift=0.2 * RIGHT), FadeIn(D2[2]), FadeIn(D2[5], shift=0.2 * LEFT), run_time=0.7)
        self.next_slide()
        self.play(B2.animate.set_color(KOLOR_TEKST), D2.animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()

        piszemy = MathTex(r"\text{Piszemy wtedy }", r"\lim_{n,m\to\infty} p(x_n,x_m)=a", r".", font_size=FS)
        piszemy.next_to(definicja, DOWN, buff=0.22)
        piszemy[1].set_color(O)
        self.play(FadeIn(piszemy, shift=0.2 * RIGHT))
        self.next_slide()
        self.play(piszemy[1].animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()

        # ---- Przykład w max ----
        prz = MathTex(r"\textbf{Przykład.}\ \ X=[0,\infty),\quad p(x,y)=\max\{x,y\},\quad",
                      r"x_n\coloneqq 1+\tfrac{1}{n}", r"\ \text{ dla } n\in\mathbb{N}.", font_size=32)
        prz[1].set_color(KOLOR_Y)
        prz.next_to(piszemy, DOWN, buff=0.35)
        self.play(FadeIn(prz, shift=0.2 * RIGHT))
        self.next_slide()

        R = MathTex(r"p(x_n,x_m)", r"=\max\Bigl\{1+\tfrac{1}{n},\,1+\tfrac{1}{m}\Bigr\}",
                    r"=1+\frac{1}{\min\{n,m\}}", r"\xrightarrow[n,m\to\infty]{}1", font_size=34)
        R.next_to(prz, DOWN, buff=0.22)
        self.play(FadeIn(R[0], shift=0.2 * RIGHT))
        self.next_slide()
        for k in (1, 2, 3):
            R[k].set_color(O)
            self.play(FadeIn(R[k], shift=0.2 * RIGHT))
            self.next_slide()
            self.play(R[k].animate.set_color(KOLOR_TEKST), run_time=0.5)
        wn = Tex(r"więc $(x_n)_{n\in\mathbb{N}}$ jest ciągiem Cauchy'ego i $\lim_{n,m\to\infty} p(x_n,x_m)=1$",
                 r"$\,\neq 0$", r".", font_size=32)
        wn.next_to(R, DOWN, buff=0.22)
        self.play(FadeIn(wn[0], shift=0.2 * RIGHT))
        self.next_slide()
        wn[1].set_color(KOLOR_METRYKA)
        self.play(FadeIn(wn[1:], shift=0.2 * RIGHT))
        self.next_slide()
        self.play(wn[1].animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()

        # ---- Zupełność całej przestrzeni ----
        zup = VGroup(
            MathTex(r"\textbf{Definicja.}\ \text{Przestrzeń } (X,p) \text{ jest \emph{zupełna}, gdy każdy ciąg "
                    r"Cauchy'ego } (x_n)_{n\in\mathbb{N}}\subset X", font_size=31),
            MathTex(r"\text{jest zbieżny w } \tau_p \text{ do pewnego } x\in X \text{ takiego, że}", font_size=31),
            MathTex(r"p(x,x)=\lim_{n\to\infty} p(x,x_n)=\lim_{n,m\to\infty} p(x_n,x_m).", font_size=31),
        ).arrange(DOWN, buff=0.12)
        zup.next_to(wn, DOWN, buff=0.3)
        zup[2].set_color(O)
        self.play(FadeIn(zup[:2], shift=0.2 * RIGHT))
        self.next_slide()
        self.play(FadeIn(zup[2], shift=0.2 * RIGHT))
        self.next_slide()
        self.play(zup[2].animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()


class MetrykaIndukowana(Slide):
    """Dwa twierdzenia (bez dowodów): d_p jest metryką oraz zupełność (X,p) <=> zupełność (X,d_p)."""

    def construct(self):
        FS = 34
        B = KOLOR_METRYKA

        naglowek = Tex(TYTUL_ZUP, font_size=44).to_edge(UP, buff=0.4)
        self.add(naglowek)

        tw1 = VGroup(
            MathTex(r"\textbf{Twierdzenie.}\ \text{Niech } (X,p) \text{ będzie przestrzenią częściowo metryczną.}",
                    font_size=FS),
            MathTex(r"\text{Wtedy wzór}", font_size=FS),
            MathTex(r"d_p(x,y)\coloneqq 2p(x,y)-p(x,x)-p(y,y)", font_size=FS + 4),
            MathTex(r"\text{definiuje metrykę na } X.", font_size=FS),
        ).arrange(DOWN, buff=0.22)
        tw1[0].align_to(tw1, LEFT)
        tw1[1].align_to(tw1, LEFT)
        tw1[3].align_to(tw1, LEFT)

        tw2 = VGroup(
            MathTex(r"\textbf{Twierdzenie.}\ \text{Przestrzeń } (X,p) \text{ jest zupełna wtedy i tylko wtedy,}",
                    font_size=FS),
            MathTex(r"\text{gdy przestrzeń metryczna } (X,d_p) \text{ jest zupełna.}", font_size=FS),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)

        VGroup(tw1, tw2).arrange(DOWN, aligned_edge=LEFT, buff=0.8).next_to(naglowek, DOWN, buff=0.6)
        tw1[2].set_x(0)

        # Twierdzenie 1: wzór na d_p na chwilę na niebiesko (to jest metryka).
        self.play(FadeIn(tw1[:2], shift=0.2 * DOWN))
        self.next_slide()
        tw1[2].set_color(B)
        self.play(FadeIn(tw1[2], shift=0.2 * DOWN))
        self.next_slide()
        self.play(FadeIn(tw1[3], shift=0.2 * DOWN), tw1[2].animate.set_color(KOLOR_TEKST))
        self.next_slide()

        # Twierdzenie 2.
        self.play(FadeIn(tw2, shift=0.2 * DOWN))
        self.next_slide()
