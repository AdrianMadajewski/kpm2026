from manim_slides import Slide
from common import *


class Plan(Slide):
    def construct(self):
        naglowek = Tex(r"Plan", font_size=48).to_edge(UP, buff=0.5)
        plan = plan_referatu().move_to(0.4 * DOWN)
        wiersze, strzalki = plan

        self.play(FadeIn(naglowek))
        self.next_slide()

        # Każdy punkt planu na osobne kliknięcie.
        self.play(FadeIn(wiersze[0], shift=0.2 * RIGHT))
        self.next_slide()
        for i in range(1, len(wiersze)):
            self.play(GrowArrow(strzalki[i - 1]), run_time=0.4)
            self.play(FadeIn(wiersze[i], shift=0.2 * RIGHT), run_time=0.7)
            self.next_slide()

        # Przejście do pierwszej sekcji: wyróżnienie punktu 1.
        cel = plan_referatu(aktywny=0).move_to(plan)
        self.play(Transform(plan, cel))
        self.next_slide()


def _przerywnik(numer):
    """Slajd przejścia do sekcji `numer` (1..4): plan z podświetlonym punktem."""

    class PlanSekcji(Slide):
        def construct(self):
            naglowek = Tex(r"Plan", font_size=48).to_edge(UP, buff=0.5)
            poprzedni = plan_referatu(aktywny=numer - 2).move_to(0.4 * DOWN)
            biezacy = plan_referatu(aktywny=numer - 1).move_to(0.4 * DOWN)
            self.play(FadeIn(naglowek), FadeIn(poprzedni))
            self.play(Transform(poprzedni, biezacy))
            self.next_slide()

    PlanSekcji.__name__ = f"PlanSekcja{numer}"
    PlanSekcji.__qualname__ = PlanSekcji.__name__
    return PlanSekcji


PlanSekcja2 = _przerywnik(2)
PlanSekcja3 = _przerywnik(3)
PlanSekcja4 = _przerywnik(4)
