from manim_slides import Slide
from common import *


class Tytul(Slide):
    def construct(self):
        tytul = Tex(
            r"Czy odległość punktu od samego siebie\\musi być zerowa?",
            font_size=60,
        ).to_edge(UP, buff=0.8)
        podtytul = Tex(
            r"Przestrzenie częściowo metryczne",
            font_size=36,
            color=KOLOR_DRUGORZEDNY,
        ).next_to(tytul, DOWN, buff=0.4)
        autor = VGroup(
            Tex(r"Adrian Madajewski", font_size=32),
            Tex(r"Wydział Matematyki i Informatyki UAM", font_size=26, color=KOLOR_DRUGORZEDNY),
            Tex(r"KPM 2026, Warszawa", font_size=26, color=KOLOR_DRUGORZEDNY),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN, buff=0.6)

        # Autor i tytuł widoczne od razu.
        self.add(autor, tytul)
        self.wait(0.5)
        self.next_slide()

        # Podtytuł.
        self.play(FadeIn(podtytul, shift=0.2 * UP))
        self.next_slide()

        # Punkt z pętlą: odległość od samego siebie.
        srodek = 0.4 * DOWN
        punkt = Dot(srodek, radius=0.09)
        etykieta_x = MathTex("x", font_size=36).next_to(punkt, DOWN, buff=0.15)
        petla = Arc(
            radius=0.35,
            start_angle=-PI / 2 + 0.45,
            angle=2 * PI - 0.9,
            arc_center=srodek + 0.42 * UP,
            color=KOLOR_METRYKA,
        ).add_tip(tip_length=0.15)
        wzor_d = MathTex(r"d(x,x) = 0", font_size=40, color=KOLOR_METRYKA)
        wzor_d.next_to(petla, RIGHT, buff=0.4)

        self.play(FadeIn(punkt, scale=0.5), FadeIn(etykieta_x))
        self.play(Create(petla), FadeIn(wzor_d))
        self.next_slide()

        # A gdyby nie?
        wzor_p = MathTex(r"p(x,x) \ge 0", font_size=40, color=KOLOR_CZESCIOWA)
        wzor_p.move_to(wzor_d, aligned_edge=LEFT)
        self.play(FadeOut(wzor_d, shift=0.4 * LEFT), run_time=0.7)
        self.play(
            petla.animate.set_color(KOLOR_CZESCIOWA),
            FadeIn(wzor_p, shift=0.4 * RIGHT),
            run_time=0.8,
        )
        self.play(Wiggle(punkt, scale_value=1.6))
        self.next_slide()
