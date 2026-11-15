from manim_slides import Slide
from common import *


class Podsumowanie(Slide):
    """Cztery najważniejsze wnioski + powrót pętli z tytułu: p(x,x) = ? -> p(x*,x*) = 0."""

    def construct(self):
        O = KOLOR_CZESCIOWA
        FS = 31

        naglowek = Tex(r"Podsumowanie", font_size=48)
        self.play(FadeIn(naglowek))
        self.next_slide()
        self.play(naglowek.animate.scale(44 / 48).to_edge(UP, buff=0.4), run_time=1.0)

        # ---- Pętla z tytułu, po prawej ----
        srodek = np.array([4.6, 0.6, 0])
        punkt = Dot(srodek, radius=0.09)
        etykieta_x = MathTex("x", font_size=36).next_to(punkt, DOWN, buff=0.15)
        petla = Arc(radius=0.35, start_angle=-PI / 2 + 0.45, angle=2 * PI - 0.9,
                    arc_center=srodek + 0.42 * UP, color=O).add_tip(tip_length=0.15)
        wzor_p = MathTex(r"p(x,x)=\,?", font_size=38, color=O).next_to(petla, UP, buff=0.3)
        self.play(FadeIn(punkt, scale=0.5), FadeIn(etykieta_x), Create(petla), FadeIn(wzor_p))
        self.next_slide()

        # ---- Cztery wnioski ----
        def punkt_listy(tekst):
            t = Tex(tekst, font_size=FS, tex_environment="flushleft")
            kropka = Dot(radius=0.045).move_to(t.get_corner(UL) + 0.25 * LEFT + 0.14 * DOWN)
            return VGroup(kropka, t)

        wnioski = VGroup(
            punkt_listy(r"Metryka częściowa dopuszcza $p(x,x)>0$,\\"
                        r"czyli mierzy, jak słabo określony jest punkt."),
            punkt_listy(r"Metryki to dokładnie te metryki częściowe,\\w których $p(x,x)=0$."),
            punkt_listy(r"Topologia $\tau_p$ jest $T_0$, ale nie musi być $T_1$,\\"
                        r"a granice ciągów nie muszą być jednoznaczne."),
            punkt_listy(r"Zupełność wybiera granicę z $p(x,x)=\lim p(x_n,x_m)$,\\"
                        r"a punkt stały kontrakcji jest w pełni określony."),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        wnioski.next_to(naglowek, DOWN, buff=0.6).to_edge(LEFT, buff=0.6)

        # 1. p(x,x) > 0: pętla "pulsuje".
        self.play(FadeIn(wnioski[0], shift=0.2 * RIGHT))
        self.play(Indicate(wzor_p, color=O, scale_factor=1.15))
        self.next_slide()

        # 2. Metryki: na chwilę pętla niebieska z d(x,x) = 0, potem wraca.
        self.play(FadeIn(wnioski[1], shift=0.2 * RIGHT))
        wzor_d = MathTex(r"d(x,x)=0", font_size=38, color=KOLOR_METRYKA).move_to(wzor_p)
        self.play(petla.animate.set_color(KOLOR_METRYKA), FadeTransform(wzor_p, wzor_d), run_time=0.8)
        self.wait(0.4)
        wzor_p2 = MathTex(r"p(x,x)=\,?", font_size=38, color=O).move_to(wzor_d)
        self.play(petla.animate.set_color(O), FadeTransform(wzor_d, wzor_p2), run_time=0.8)
        wzor_p = wzor_p2
        self.next_slide()

        # 3. Topologia.
        self.play(FadeIn(wnioski[2], shift=0.2 * RIGHT))
        self.wait(0.2)
        self.next_slide()

        # 4. Punkt stały: pętla kurczy się i robi się niebieska, p(x*,x*) = 0.
        self.play(FadeIn(wnioski[3], shift=0.2 * RIGHT))
        self.next_slide()
        etykieta_xs = MathTex(r"x^*", font_size=36).move_to(etykieta_x)
        wzor_k = MathTex(r"p(x^*,x^*)=0", font_size=38, color=KOLOR_METRYKA).move_to(wzor_p)
        self.play(petla.animate.set_color(KOLOR_METRYKA), FadeTransform(wzor_p, wzor_k),
                  FadeTransform(etykieta_x, etykieta_xs), run_time=1.0)
        self.play(Flash(punkt, color=KOLOR_METRYKA, line_length=0.25, flash_radius=0.3))
        self.next_slide()


class Podziekowania(Slide):
    """Podziękowania za uwagę i kod QR do repozytorium z prezentacją."""

    def construct(self):
        from pathlib import Path

        dzieki = Tex(r"Dziękuję za uwagę!", font_size=60)
        qr = SVGMobject(str(Path(__file__).parent / "grafika" / "qr_github.svg"))
        qr.set_fill(KOLOR_TEKST, 1).set_stroke(width=0).set_height(3.4)
        adres = Tex(r"\texttt{github.com/AdrianMadajewski/kpm2026}", font_size=30, color=KOLOR_DRUGORZEDNY)
        VGroup(dzieki, qr, adres).arrange(DOWN, buff=0.5)

        self.play(FadeIn(dzieki, shift=0.2 * DOWN))
        self.next_slide()
        self.play(FadeIn(qr, scale=0.9), FadeIn(adres, shift=0.2 * UP))
        self.next_slide()
