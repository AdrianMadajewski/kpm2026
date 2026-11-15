from manim_slides import Slide
from common import *


class Zbieznosc(Slide):
    """Zbieżność w tau_p: pytanie, stwierdzenie p(x,x_n) -> p(x,x) z dowodem, przykład x_n = 0 w max."""

    def construct(self):
        FS = 30
        O = KOLOR_CZESCIOWA
        KOLOR_Y = ManimColor("#7B3FA0")

        def przypomnienie(tex):
            return MathTex(tex, font_size=30, color=O).to_edge(DOWN, buff=0.35)

        # ---- Pytanie na środku, potem do góry ----
        pytanie = Tex(r"Kiedy ciąg $(x_n)_{n\in\mathbb{N}}\subset X$ jest zbieżny do $x\in X$ w $\tau_p$?",
                      font_size=40)
        self.play(FadeIn(pytanie))
        self.next_slide()
        self.play(pytanie.animate.scale(0.85).to_edge(UP, buff=0.4), run_time=1.0)
        self.next_slide()

        # Przypomnienie definicji topologicznej.
        defn = MathTex(r"x_n\to x \iff", r"\forall\, U\in\tau_p,\ x\in U",
                       r"\ \ \exists\, N\ \forall\, n\ge N\colon\ x_n\in U",
                       font_size=32, color=KOLOR_DRUGORZEDNY)
        defn.next_to(pytanie, DOWN, buff=0.35)
        self.play(FadeIn(defn, shift=0.2 * DOWN))
        self.next_slide()

        stw = Tex(r"\textbf{Stwierdzenie.} $x_n\to x$ w $\tau_p$ wtedy i tylko wtedy, gdy ",
                  r"$\displaystyle\lim_{n\to\infty} p(x,x_n)=p(x,x)$", r".", font_size=34)
        stw.next_to(defn, DOWN, buff=0.35)
        self.play(FadeIn(stw, shift=0.2 * DOWN))
        self.wait(0.2)
        self.next_slide()

        Q1 = MathTex(r"\textit{Dowód.}\ (\Rightarrow)", r"\ \text{Ustalmy }\varepsilon>0.\ \text{Kula }",
                     r"B_p(x,\varepsilon)", r"\text{ jest otwarta i zawiera } x\text{,}", font_size=FS)
        Q2 = MathTex(r"\text{więc istnieje } N \text{ takie, że dla każdego } n\ge N \text{ mamy }",
                     r"x_n\in B_p(x,\varepsilon)", r"\text{,}", font_size=FS)
        Q2b = MathTex(r"\text{czyli }", r"p(x,x_n)<p(x,x)+\varepsilon", r".", font_size=FS)
        Q3 = MathTex(r"\text{Z (P2) mamy }", r"p(x,x)\le p(x,x_n)", r"\text{, zatem }",
                     r"0\le p(x,x_n)-p(x,x)<\varepsilon", r"\text{ dla } n\ge N.", font_size=FS)
        Q3b = MathTex(r"\text{Zatem }", r"\lim_{n\to\infty} p(x,x_n)=p(x,x)", r".", font_size=FS)
        Q4 = MathTex(r"(\Leftarrow)\ ", r"\text{Niech } U\in\tau_p,\ x\in U.", r"\ \text{Z lematu }",
                     r"B_p(x,\varepsilon)\subseteq U", r"\text{ dla pewnego } \varepsilon>0.", font_size=FS)
        Q5 = MathTex(r"\text{Z założenia }", r"\text{istnieje } N \text{ takie, że dla każdego } n\ge N",
                     r"\text{ mamy }", r"p(x,x_n)-p(x,x)<\varepsilon", r"\text{,}", font_size=FS)
        Q6 = MathTex(r"\text{zatem }", r"p(x,x_n)<p(x,x)+\varepsilon", r"\text{, czyli }",
                     r"x_n\in B_p(x,\varepsilon)\subseteq U", r"\text{ dla } n\ge N", r".", font_size=FS)
        dowod = VGroup(Q1, Q2, Q2b, Q3, Q3b, Q4, Q5, Q6).arrange(DOWN, aligned_edge=LEFT, buff=0.17)
        dowod.next_to(stw, DOWN, buff=0.35).to_edge(LEFT, buff=0.7)

        def pokaz(*czesci, pomaranczowe=()):
            """Pokaż fragmenty linii; wskazane od razu na pomarańczowo. Potem pauza."""
            for c in pomaranczowe:
                c.set_color(O)
            self.play(*[FadeIn(c, shift=0.2 * RIGHT) for c in czesci])
            self.next_slide()

        def wyszarz(*czesci, przyp=None, extra=()):
            """Na kliknięcie: pomarańczowe wracają do czerni, podpowiedź z dołu znika."""
            anims = [c.animate.set_color(KOLOR_TEKST) for c in czesci] + list(extra)
            if przyp is not None:
                anims.append(FadeOut(przyp, shift=0.2 * DOWN))
            self.play(*anims, run_time=0.6)
            self.next_slide()

        def pokaz_przyp(przyp):
            self.play(FadeIn(przyp, shift=0.2 * UP))
            self.next_slide()

        baza = przypomnienie(r"\text{(Lemat)}\quad \text{kule } B_p \text{ tworzą bazę topologii } \tau_p")
        kula = przypomnienie(r"B_p(x,\varepsilon)\coloneqq\{u\in X : p(x,u)<p(x,x)+\varepsilon\}")
        p2 = przypomnienie(r"\text{(P2)}\quad p(x,x)\le p(x,y)")
        lemat = przypomnienie(r"\text{(Lemat)}\quad x\in U\in\tau_p \implies \exists\,\varepsilon>0\colon\ "
                              r"B_p(x,\varepsilon)\subseteq U")

        # (=>)
        pokaz(Q1[0])
        pokaz_przyp(baza)
        pokaz(Q1[1:], pomaranczowe=[Q1[2]])
        wyszarz(Q1[2], przyp=baza)

        # Skąd Q2: definicja zbieżności (u góry) dla U := B_p(x, eps).
        podkr = Underline(defn[1], color=O, stroke_width=3, buff=0.08)
        Q2[1].set_color(O)
        self.play(defn[1].animate.set_color(O), Create(podkr), FadeIn(Q2, shift=0.2 * RIGHT))
        self.next_slide()
        self.play(defn[1].animate.set_color(KOLOR_DRUGORZEDNY), FadeOut(podkr), Q2[1].animate.set_color(KOLOR_TEKST),
                  run_time=0.6)
        self.next_slide()

        pokaz_przyp(kula)
        pokaz(Q2b, pomaranczowe=[Q2b[1]])
        wyszarz(Q2b[1], przyp=kula)

        pokaz_przyp(p2)
        pokaz(Q3[:2], pomaranczowe=[Q3[1]])
        wyszarz(Q3[1], przyp=p2)
        pokaz(Q3[2:], pomaranczowe=[Q3[3]])
        wyszarz(Q3[3])
        pokaz(Q3b, pomaranczowe=[Q3b[1]])
        wyszarz(Q3b[1])

        # (<=)
        pokaz(Q4[:2])
        pokaz_przyp(lemat)
        pokaz(Q4[2:], pomaranczowe=[Q4[3]])
        wyszarz(Q4[3], przyp=lemat)
        # Korzystamy z założenia (prawa strona stwierdzenia): podkreślenie.
        podkr_z = Underline(stw[1], color=O, stroke_width=3, buff=0.05)
        Q5[3].set_color(O)
        self.play(stw[1].animate.set_color(O), Create(podkr_z), FadeIn(Q5, shift=0.2 * RIGHT))
        self.next_slide()
        wyszarz(Q5[3], stw[1], extra=[FadeOut(podkr_z)])
        pokaz(Q6[:2], pomaranczowe=[Q6[1]])
        wyszarz(Q6[1])
        pokaz_przyp(kula)
        pokaz(Q6[2:], pomaranczowe=[Q6[3]])
        wyszarz(Q6[3], przyp=kula)

        # To, co chcieliśmy pokazać: definicja zbieżności u góry i odpowiadające jej fragmenty dowodu.
        cel = [Q4[1], Q5[1], Q6[3], Q6[4]]
        self.play(*[c.animate.set_color(O) for c in cel], defn[1].animate.set_color(O),
                  defn[2].animate.set_color(O), run_time=0.7)
        self.next_slide()
        self.play(*[c.animate.set_color(KOLOR_TEKST) for c in cel], defn[1].animate.set_color(KOLOR_DRUGORZEDNY),
                  defn[2].animate.set_color(KOLOR_DRUGORZEDNY), run_time=0.6)
        kwadrat = MathTex(r"\blacksquare", font_size=FS).next_to(Q6, RIGHT, buff=0.15)
        self.play(FadeIn(kwadrat))
        self.next_slide()

        # ================= Przykład: x_n = 0 w max =================
        self.play(*[FadeOut(m, shift=0.3 * LEFT) for m in self.mobjects], run_time=0.8)
        self.next_slide()

        prz = MathTex(r"\textbf{Przykład.}\ \ X=[0,\infty),\quad p(x,y)=\max\{x,y\},\quad",
                      r"x_n\coloneqq 0", r"\ \text{ dla } n\in\mathbb{N}.", font_size=34)
        prz.to_edge(UP, buff=0.5)
        prz[1].set_color(KOLOR_Y)
        self.play(FadeIn(prz, shift=0.2 * DOWN))
        self.next_slide()

        # Rachunek: p(x, x_n) = max{x, 0} = x = p(x, x).
        R = MathTex(r"p(x,x_n)", r"=\max\{x,0\}", r"=x", r"=\max\{x,x\}", r"=p(x,x)", font_size=36)
        R.next_to(prz, DOWN, buff=0.5)
        self.play(FadeIn(R[0], shift=0.2 * RIGHT))
        self.next_slide()
        for k in (1, 2, 3, 4):
            R[k].set_color(O)
            self.play(FadeIn(R[k], shift=0.2 * RIGHT))
            self.wait(0.3)
            self.play(R[k].animate.set_color(KOLOR_TEKST), run_time=0.5)
            self.next_slide()

        lim = MathTex(r"\text{Zatem }", r"\lim_{n\to\infty} p(x,x_n)=x", r"=p(x,x)", r",", font_size=36)
        lim.next_to(R, DOWN, buff=0.4)
        self.play(FadeIn(lim, shift=0.2 * RIGHT))
        self.next_slide()

        wn = Tex(r"więc $x_n\to x$ dla \emph{każdego} $x\in[0,\infty)$!", font_size=36)
        wn.next_to(lim, DOWN, buff=0.4)
        self.play(FadeIn(wn, shift=0.2 * RIGHT))
        self.next_slide()

        konc = Tex(r"\textbf{Granica ciągu nie jest jednoznaczna.}", font_size=36, color=O)
        konc.next_to(wn, DOWN, buff=0.6)
        self.play(FadeIn(konc, shift=0.2 * UP))
        self.wait(0.2)
        self.next_slide()
