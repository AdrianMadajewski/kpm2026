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


class ZupelnoscMax(Slide):
    """([0, inf), max) jest zupełna: kandydat na granicę, zbieżność, przynależność."""

    def construct(self):
        FS = 30
        O = KOLOR_CZESCIOWA

        naglowek = Tex(TYTUL_ZUP, font_size=44).to_edge(UP, buff=0.4)
        self.add(naglowek)

        stw = Tex(r"\textbf{Stwierdzenie.} Przestrzeń $([0,\infty),\max)$ jest zupełna.", font_size=36)
        stw.next_to(naglowek, DOWN, buff=0.45)
        self.play(FadeIn(stw, shift=0.2 * DOWN))
        self.wait(0.2)
        self.next_slide()

        L1 = MathTex(r"\textit{Dowód.}\ \text{Niech } (x_n)_{n\in\mathbb{N}}\subset[0,\infty) \text{ będzie ciągiem "
                     r"Cauchy'ego}", r"\text{ i }", r"a\coloneqq\lim_{n,m\to\infty}\max\{x_n,x_m\}", r".", font_size=FS)
        K = MathTex(r"\textit{Kandydat.}\ \text{Dla } m=n\text{: }", r"x_n=\max\{x_n,x_n\}\xrightarrow[n\to\infty]{}a",
                    r"\text{, czyli }", r"\lim_{n\to\infty}x_n=a", r".", font_size=FS)
        Z1 = MathTex(r"\textit{Zbieżność.}\ ", r"p(a,x_n)=\max\{a,x_n\}\xrightarrow[n\to\infty]{}\max\{a,a\}=a=p(a,a)",
                     r"\text{, więc }", r"x_n\to a \text{ w } \tau_p", r".", font_size=FS)
        Z2 = MathTex(r"\text{Ponadto }", r"p(a,a)=a=\lim_{n,m\to\infty}p(x_n,x_m)", r".", font_size=FS)
        P = MathTex(r"\textit{Przynależność.}\ ", r"x_n\ge 0", r"\text{ dla } n\in\mathbb{N}\text{, więc }",
                    r"a=\lim_{n\to\infty}x_n\ge 0", r"\text{, czyli } a\in[0,\infty).", font_size=FS)
        dowod = VGroup(L1, K, Z1, Z2, P).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        dowod.next_to(stw, DOWN, buff=0.45).to_edge(LEFT, buff=0.6)

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

        stw_zb = przypomnienie(r"x_n\to x \text{ w } \tau_p \iff \lim_{n\to\infty}p(x,x_n)=p(x,x)")
        war_zup = przypomnienie(r"p(x,x)=\lim_{n\to\infty}p(x,x_n)=\lim_{n,m\to\infty}p(x_n,x_m)")

        # Założenie i oznaczenie granicy.
        pokaz(L1[0])
        pokaz(L1[1:], pomaranczowe=[L1[2]])
        wyszarz(L1[2])

        # 1. Kandydat na granicę.
        pokaz(K[:2], pomaranczowe=[K[1]])
        wyszarz(K[1])
        pokaz(K[2:], pomaranczowe=[K[3]])
        wyszarz(K[3])

        # 2. Zbieżność w tau_p.
        pokaz(Z1[:2], pomaranczowe=[Z1[1]])
        wyszarz(Z1[1])
        pokaz_przyp(stw_zb)
        pokaz(Z1[2:], pomaranczowe=[Z1[3]])
        wyszarz(Z1[3], przyp=stw_zb)
        pokaz_przyp(war_zup)
        pokaz(Z2, pomaranczowe=[Z2[1]])
        wyszarz(Z2[1], przyp=war_zup)

        # 3. Przynależność granicy do X.
        pokaz(P[:3], pomaranczowe=[P[1]])
        wyszarz(P[1])
        pokaz(P[3:], pomaranczowe=[P[3]])
        wyszarz(P[3])
        kwadrat = MathTex(r"\blacksquare", font_size=FS).next_to(P, RIGHT, buff=0.15)
        self.play(FadeIn(kwadrat))
        self.next_slide()
