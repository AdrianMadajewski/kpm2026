from manim_slides import Slide
from common import *


class Plan(Slide):
    def construct(self):
        naglowek = Tex(r"Plan", font_size=48).to_edge(UP, buff=0.5)
        plan = plan_referatu().move_to(0.4 * DOWN)
        wiersze, strzalki = plan

        self.play(Write(naglowek))
        self.play(FadeIn(wiersze[0], shift=0.2 * RIGHT))
        for i in range(1, len(wiersze)):
            self.play(GrowArrow(strzalki[i - 1]), run_time=0.4)
            self.play(FadeIn(wiersze[i], shift=0.2 * RIGHT), run_time=0.7)
        self.next_slide()

        # Przejście do pierwszej sekcji: wyróżnienie punktu 1.
        cel = plan_referatu(aktywny=0).move_to(plan)
        self.play(Transform(plan, cel))
        self.next_slide()
