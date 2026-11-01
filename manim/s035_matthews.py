from manim_slides import Slide
from common import *
import os
import numpy as np

ZDJECIE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zdjecia", "matthews.jpg")


class Matthews(Slide):
    """Krótko o Steve'ie Matthewsie przed definicją metryki częściowej."""

    def construct(self):
        naglowek = Tex(r"Steve G.\ Matthews", font_size=48).to_edge(UP, buff=0.5)
        self.play(FadeIn(naglowek))
        self.next_slide()

        # Zamiast zdjęcia: buźka w okularach.
        twarz = Circle(radius=1.15, color=KOLOR_TEKST, stroke_width=4).set_fill(ManimColor("#FFE7A8"), 1)
        oko_l = Dot(twarz.get_center() + np.array([-0.4, 0.3, 0]), radius=0.09)
        oko_p = Dot(twarz.get_center() + np.array([0.4, 0.3, 0]), radius=0.09)
        szkla = VGroup(*[Circle(radius=0.26, color=KOLOR_TEKST, stroke_width=3).move_to(o) for o in (oko_l, oko_p)])
        mostek = Line(szkla[0].get_right(), szkla[1].get_left(), color=KOLOR_TEKST, stroke_width=3)
        usmiech = Arc(radius=0.6, start_angle=-PI + 0.6, angle=PI - 1.2, color=KOLOR_TEKST, stroke_width=4)
        usmiech.move_to(twarz.get_center() + 0.42 * DOWN)
        ramka = RoundedRectangle(width=2.9, height=3.6, corner_radius=0.15, color=GRAY_C, stroke_width=2)
        foto = VGroup(ramka, VGroup(twarz, oko_l, oko_p, szkla, mostek, usmiech).move_to(ramka))
        foto.to_edge(LEFT, buff=1.0).shift(0.4 * DOWN)

        punkty = VGroup(*[
            Tex(t, font_size=32, tex_environment="flushleft") for t in [
                r"$\bullet$ informatyk, University of Warwick\\\phantom{$\bullet$ }(Department of Computer Science),",
                r"$\bullet$ doktorat (1985) o sieciach przepływu danych\\"
                r"\phantom{$\bullet$ }(model Kahna, test Wadge'a, język Lucid).",
            ]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        punkty.next_to(foto, RIGHT, buff=0.8)

        self.play(FadeIn(foto))
        self.play(Wiggle(foto[1], scale_value=1.08))
        for p in punkty:
            self.play(FadeIn(p, shift=0.2 * RIGHT))
            self.next_slide()
