from manim_slides import Slide
from common import *
import os

ZDJECIE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zdjecia", "matthews.jpg")


class Matthews(Slide):
    """Krótko o Steve'ie Matthewsie przed definicją metryki częściowej."""

    def construct(self):
        naglowek = Tex(r"Steve G.\ Matthews", font_size=48).to_edge(UP, buff=0.5)
        self.play(FadeIn(naglowek))
        self.next_slide()

        # Zdjęcie, jeśli jest w manim/zdjecia/matthews.jpg; inaczej szara ramka.
        if os.path.exists(ZDJECIE):
            foto = ImageMobject(ZDJECIE)
            foto.height = 3.6
        else:
            foto = VGroup(
                RoundedRectangle(width=2.9, height=3.6, corner_radius=0.15, color=GRAY_C, stroke_width=2),
                Tex(r"zdjęcie", font_size=28, color=GRAY_C),
            )
        foto.to_edge(LEFT, buff=1.0).shift(0.4 * DOWN)

        punkty = VGroup(*[
            Tex(t, font_size=32, tex_environment="flushleft") for t in [
                r"$\bullet$ informatyk, University of Warwick\\\phantom{$\bullet$ }(Department of Computer Science),",
                r"$\bullet$ doktorat (1985) o sieciach przepływu danych\\"
                r"\phantom{$\bullet$ }(model Kahna, test Wadge'a, język Lucid),",
                r"$\bullet$ 1994: praca \emph{Partial metric topology},\\"
                r"\phantom{$\bullet$ }w której wprowadza metryki częściowe,",
                r"$\bullet$ obiekty ,,częściowo policzone'' mają u niego\\"
                r"\phantom{$\bullet$ }niezerową odległość od samych siebie.",
            ]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        punkty.next_to(foto, RIGHT, buff=0.8).align_to(foto, UP)

        self.play(FadeIn(foto))
        for p in punkty:
            self.play(FadeIn(p, shift=0.2 * RIGHT))
            self.next_slide()
