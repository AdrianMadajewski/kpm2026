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


class PlanPodsumowanie(Slide):
    """Plan po sekcji 4: przesuwa się do góry, a na dole dochodzi punkt „Podsumowanie”."""

    def construct(self):
        naglowek = Tex(r"Plan", font_size=48).to_edge(UP, buff=0.5)
        plan = plan_referatu(aktywny=3).move_to(0.4 * DOWN)
        wiersze, strzalki = plan
        self.play(FadeIn(naglowek), FadeIn(plan))
        self.next_slide()

        # Plan do góry, punkt 4 przygasa.
        cel_y = naglowek.get_bottom()[1] - 0.35 - plan.height / 2
        self.play(plan.animate.shift((cel_y - plan.get_center()[1]) * UP), run_time=1.0)
        self.play(wiersze[3][0].animate.set_stroke(GRAY_C, width=2, opacity=0.35),
                  wiersze[3][1].animate.set_opacity(0.35), run_time=0.5)

        # Nowy punkt na dole.
        numer = Tex(r"5.", font_size=38)
        opis = Tex(r"Podsumowanie", font_size=38)
        wiersz = VGroup(numer, opis).arrange(RIGHT, buff=0.3)
        ramka = SurroundingRectangle(wiersz, buff=0.2, corner_radius=0.1, color=GRAY_C, stroke_width=2)
        ramka.stretch_to_fit_width(wiersze[3][0].width).align_to(wiersz, LEFT).shift(0.2 * LEFT)
        nowy = VGroup(ramka, wiersz)
        nowy.next_to(wiersze[3], DOWN, buff=0.45).align_to(wiersze[3], LEFT)
        strzalka = Arrow(wiersze[3][0].get_bottom(), ramka.get_top(), buff=0.05, stroke_width=3,
                         max_tip_length_to_length_ratio=0.35, color=GRAY_C)
        self.play(GrowArrow(strzalka), FadeIn(nowy, shift=0.2 * UP))
        self.play(ramka.animate.set_stroke(KOLOR_CZESCIOWA, width=4, opacity=1), run_time=0.6)
        self.next_slide()
