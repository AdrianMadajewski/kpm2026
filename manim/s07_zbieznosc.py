from manim_slides import Slide
from common import *
from s06_topologia_czesciowa import _kula_na_osi


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
        defn = MathTex(r"x_n\to x \iff \forall\, U\in\tau_p,\ x\in U\ \ \exists\, N\ \forall\, n\ge N\colon\ x_n\in U",
                       font_size=32, color=KOLOR_DRUGORZEDNY)
        defn.next_to(pytanie, DOWN, buff=0.35)
        self.play(FadeIn(defn, shift=0.2 * DOWN))
        self.next_slide()

        stw = Tex(r"\textbf{Stwierdzenie.} $x_n\to x$ w $\tau_p$ wtedy i tylko wtedy, gdy "
                  r"$\displaystyle\lim_{n\to\infty} p(x,x_n)=p(x,x)$.", font_size=34)
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
        Q4 = MathTex(r"(\Leftarrow)\ \text{Niech } U\in\tau_p,\ x\in U.\ \text{Z lematu }",
                     r"B_p(x,\varepsilon)\subseteq U", r"\text{ dla pewnego } \varepsilon>0.", font_size=FS)
        Q5 = MathTex(r"\text{Z założenia istnieje } N \text{ takie, że dla każdego } n\ge N \text{ mamy }",
                     r"p(x,x_n)<p(x,x)+\varepsilon", r"\text{,}", font_size=FS)
        Q6 = MathTex(r"\text{czyli }", r"x_n\in B_p(x,\varepsilon)\subseteq U", r"\text{ dla } n\ge N.\ \blacksquare",
                     font_size=FS)
        dowod = VGroup(Q1, Q2, Q2b, Q3, Q4, Q5, Q6).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        dowod.next_to(stw, DOWN, buff=0.4).to_edge(LEFT, buff=0.7)

        def pokaz(linia, *idx):
            """Linia z podświetlonymi fragmentami, które potem wracają do czerni; na końcu pauza."""
            for k in idx:
                linia[k].set_color(O)
            self.play(FadeIn(linia, shift=0.2 * RIGHT))
            self.wait(0.4)
            if idx:
                self.play(*[linia[k].animate.set_color(KOLOR_TEKST) for k in idx], run_time=0.6)
            self.next_slide()

        def pokaz_przyp(przyp):
            self.play(FadeIn(przyp, shift=0.2 * UP))
            self.next_slide()

        def schowaj_przyp(przyp):
            # Podpowiedź znika dopiero na kliknięcie.
            self.play(FadeOut(przyp, shift=0.2 * DOWN), run_time=0.6)
            self.next_slide()

        baza = przypomnienie(r"\text{(Lemat)}\quad \text{kule } B_p \text{ tworzą bazę topologii } \tau_p")
        kula = przypomnienie(r"B_p(x,\varepsilon)\coloneqq\{u\in X : p(x,u)<p(x,x)+\varepsilon\}")
        p2 = przypomnienie(r"\text{(P2)}\quad p(x,x)\le p(x,y)")
        lemat = przypomnienie(r"\text{(Lemat)}\quad x\in U\in\tau_p \implies \exists\,\varepsilon>0\colon\ "
                              r"B_p(x,\varepsilon)\subseteq U")

        # (=>)
        self.play(FadeIn(Q1[0], shift=0.2 * RIGHT))
        self.next_slide()
        pokaz_przyp(baza)
        Q1[2].set_color(O)
        self.play(FadeIn(Q1[1:], shift=0.2 * RIGHT))
        self.wait(0.4)
        self.play(Q1[2].animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()
        schowaj_przyp(baza)
        pokaz(Q2, 1)
        pokaz_przyp(kula)
        pokaz(Q2b, 1)
        schowaj_przyp(kula)
        pokaz_przyp(p2)
        pokaz(Q3, 1)
        schowaj_przyp(p2)
        self.play(Q3[3].animate.set_color(O), run_time=0.5)
        self.wait(0.3)
        self.play(Q3[3].animate.set_color(KOLOR_TEKST), run_time=0.6)
        self.next_slide()

        # (<=)
        pokaz_przyp(lemat)
        pokaz(Q4, 1)
        schowaj_przyp(lemat)
        pokaz(Q5, 1)
        pokaz_przyp(kula)
        pokaz(Q6, 1)
        schowaj_przyp(kula)

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
        R = MathTex(r"p(x,x_n)", r"=\max\{x,0\}", r"=x", r"=p(x,x)", font_size=36)
        R.next_to(prz, DOWN, buff=0.5)
        self.play(FadeIn(R[0], shift=0.2 * RIGHT))
        self.next_slide()
        for k in (1, 2, 3):
            R[k].set_color(O)
            self.play(FadeIn(R[k], shift=0.2 * RIGHT))
            self.wait(0.3)
            self.play(R[k].animate.set_color(KOLOR_TEKST), run_time=0.5)
            self.next_slide()

        wn = Tex(r"więc $x_n\to x$ dla \emph{każdego} $x\in[0,\infty)$!", font_size=36)
        wn.next_to(R, DOWN, buff=0.4)
        self.play(FadeIn(wn, shift=0.2 * RIGHT))
        self.next_slide()

        # ---- Rysunek na osi ----
        os = NumberLine(x_range=[0, 5, 1], length=8, include_numbers=True,
                        font_size=24, include_tip=False).move_to(np.array([0, -2.4, 0]))
        xt = ValueTracker(1.0)
        et = ValueTracker(1.0)
        ciag = Dot(os.n2p(0), radius=0.09, color=KOLOR_Y).set_z_index(11)
        e_ciag = MathTex(r"x_n", font_size=28, color=KOLOR_Y).next_to(ciag, DOWN, buff=0.4)
        kx = always_redraw(lambda: Dot(os.n2p(xt.get_value()), radius=0.08, color=O).set_z_index(10))
        ex = always_redraw(lambda: MathTex("x", font_size=28).next_to(kx, DOWN, buff=0.4))
        kula = always_redraw(lambda: _kula_na_osi(os, xt.get_value() + et.get_value(), O, 0.35))
        e_kula = always_redraw(lambda: MathTex(r"B_p(x,\varepsilon)", font_size=28, color=O)
                               .next_to(kula[0], UP, buff=0.15).align_to(kula[0], RIGHT))
        eps_lab = MathTex(r"\varepsilon=", font_size=30)
        eps_num = DecimalNumber(1.0, num_decimal_places=2, font_size=30)
        eps_grp = VGroup(eps_lab, eps_num).arrange(RIGHT, buff=0.12).move_to(np.array([5.4, -1.5, 0]))
        eps_num.add_updater(lambda m: m.set_value(et.get_value()).next_to(eps_lab, RIGHT, buff=0.12))

        self.play(Create(os))
        self.play(FadeIn(ciag), FadeIn(e_ciag))
        self.next_slide()
        self.play(FadeIn(kx), FadeIn(ex))
        self.next_slide()
        self.play(FadeIn(kula), FadeIn(e_kula), FadeIn(eps_grp))
        self.wait(0.2)
        self.next_slide()

        # epsilon maleje: kula wciąż zawiera x_n = 0.
        self.play(et.animate.set_value(0.2), run_time=1.5)
        self.next_slide()
        self.play(Indicate(ciag, color=KOLOR_Y, scale_factor=1.6))
        self.next_slide()

        # x wędruje po osi: dla każdego x kula zawiera 0.
        self.play(xt.animate.set_value(3.0), run_time=1.5)
        self.next_slide()
        self.play(xt.animate.set_value(4.5), run_time=1.2)
        self.next_slide()
        self.play(xt.animate.set_value(2.0), run_time=1.2)
        self.next_slide()

        konc = Tex(r"Granica ciągu \textbf{nie jest jednoznaczna}.", font_size=36, color=O)
        konc.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(konc, shift=0.2 * UP))
        self.wait(0.2)
        self.next_slide()
