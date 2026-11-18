from manim_slides import Slide
from common import *
import numpy as np


class Matthews(Slide):
    """Krótko o Steve'ie Matthewsie przed definicją metryki częściowej."""

    def construct(self):
        naglowek = Tex(r"Steve G.\ Matthews", font_size=48).to_edge(UP, buff=0.5)

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
                r"$\bullet$ doktorat (1985) o sieciach przepływu danych.",
            ]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        punkty.next_to(foto, RIGHT, buff=0.8)

        self.play(FadeIn(naglowek), FadeIn(foto))
        self.play(Wiggle(foto[1], scale_value=1.08))
        self.next_slide()
        for p in punkty:
            self.play(FadeIn(p, shift=0.2 * RIGHT))
            self.next_slide()


class Strumienie(Slide):
    """Intuicja Matthewsa: strumień danych liczony po kawałku, przerwanie przepływu,
    porównanie dwóch strumieni po wspólnym początku (bez wzorów)."""

    def construct(self):
        O = KOLOR_CZESCIOWA
        B = KOLOR_METRYKA
        KOLOR_Y = ManimColor("#7B3FA0")
        BOK = 0.62
        N = 8

        naglowek = Tex(r"Sieci przepływu danych", font_size=44).to_edge(UP, buff=0.4)
        self.add(naglowek)

        def wiersz(y):
            kratki = VGroup(*[Square(BOK, color=GRAY_C, stroke_width=2) for _ in range(N)])
            return kratki.arrange(RIGHT, buff=0.08).move_to([0, y, 0])

        def bit(b, kratka, kolor):
            return MathTex(str(b), font_size=36, color=kolor).move_to(kratka)

        def podpis(tekst, pod, kolor=KOLOR_DRUGORZEDNY):
            return Tex(tekst, font_size=30, color=kolor).next_to(pod, DOWN, buff=0.35)

        # ================= 1. Strumień liczony bit po bicie =================
        kx = wiersz(1.5)
        ex = MathTex("x", "=", font_size=38, color=KOLOR_TEKST).next_to(kx, LEFT, buff=0.3)
        self.play(FadeIn(ex), Create(kx))
        self.next_slide()

        bity_x = [0, 1, 1, 0, 1, 0, 0, 1]
        cyfry_x = VGroup()
        p1 = podpis(r"program dopisuje kolejne elementy --- wiemy coraz więcej", kx)
        for i, b in enumerate(bity_x[:4]):
            c = bit(b, kx[i], KOLOR_TEKST)
            cyfry_x.add(c)
            anims = [FadeIn(c, shift=0.3 * DOWN)]
            if i == 0:
                anims.append(FadeIn(p1))
            self.play(*anims, run_time=0.5)
            self.next_slide()

        reszta = VGroup(*[bit(b, kx[i], KOLOR_TEKST) for i, b in enumerate(bity_x[4:], start=4)])
        kropki = MathTex(r"\dots", font_size=38, color=KOLOR_TEKST).next_to(kx, RIGHT, buff=0.15)
        self.play(LaggedStart(*[FadeIn(c, shift=0.3 * DOWN) for c in reszta], lag_ratio=0.3),
                  FadeIn(kropki), run_time=1.0)
        cyfry_x.add(*reszta)
        p1b = podpis(r"strumień nieskończony --- wynik w pełni określony", kx, B)
        self.play(cyfry_x.animate.set_color(B), kropki.animate.set_color(B), ex.animate.set_color(B),
                  FadeOut(p1), FadeIn(p1b), run_time=0.8)
        self.next_slide()

        # ================= 2. Przerwanie przepływu =================
        kz = wiersz(-1.0)
        ez = MathTex("z", "=", font_size=38, color=KOLOR_TEKST).next_to(kz, LEFT, buff=0.3)
        bity_z = [1, 0, 1]
        cyfry_z = VGroup(*[bit(b, kz[i], KOLOR_TEKST) for i, b in enumerate(bity_z)])
        self.play(FadeIn(ez), Create(kz))
        self.play(LaggedStart(*[FadeIn(c, shift=0.3 * DOWN) for c in cyfry_z], lag_ratio=0.4), run_time=1.2)
        self.next_slide()

        # Błyskawica uderza w kolejną kratkę.
        k = len(bity_z)
        p2 = podpis(r"przerwanie przepływu --- wynik już nigdy się nie uzupełni", kz, RED_D)
        cel = kz[k].get_top()
        piorun = Polygon(
            cel + np.array([0.08, 0.95, 0]), cel + np.array([-0.18, 0.42, 0]), cel + np.array([0.02, 0.46, 0]),
            cel + np.array([-0.12, 0.02, 0]), cel + np.array([0.22, 0.56, 0]), cel + np.array([0.04, 0.52, 0]),
            cel + np.array([0.26, 0.95, 0]),
            color=ManimColor("#E0A800"), stroke_width=2,
        ).set_fill(ManimColor("#FFD23F"), 1).set_z_index(5)
        self.play(FadeIn(piorun, shift=0.3 * DOWN), run_time=0.25)
        self.play(Flash(kz[k].get_center(), color=RED_D, line_length=0.25, flash_radius=0.5), run_time=0.5)
        rozbite = VGroup(*kz[k:])
        self.play(LaggedStart(*[FadeOut(kr, shift=1.2 * DOWN, scale=0.7) for kr in rozbite], lag_ratio=0.12),
                  FadeOut(piorun), run_time=1.4)
        self.play(FadeIn(p2, shift=0.2 * UP), ez.animate.set_color(RED_D), cyfry_z.animate.set_color(RED_D),
                  kz[:k].animate.set_stroke(RED_D))
        self.next_slide()

        # ================= 3. Porównanie dwóch strumieni =================
        self.play(FadeOut(VGroup(ez, kz[:k], cyfry_z, p2, p1b)), run_time=0.6)
        self.play(cyfry_x.animate.set_color(KOLOR_TEKST), kropki.animate.set_color(KOLOR_TEKST),
                  ex.animate.set_color(KOLOR_TEKST), run_time=0.5)
        ky = wiersz(-0.1)
        ey = MathTex("y", "=", font_size=38, color=KOLOR_Y).next_to(ky, LEFT, buff=0.3)
        bity_y = [0, 1, 1, 1, 0, 1, 1, 0]
        cyfry_y = VGroup(*[bit(b, ky[i], KOLOR_Y) for i, b in enumerate(bity_y)])
        kropki_y = MathTex(r"\dots", font_size=38, color=KOLOR_Y).next_to(ky, RIGHT, buff=0.15)
        self.play(FadeIn(ey), Create(ky))
        self.play(LaggedStart(*[FadeIn(c, shift=0.3 * DOWN) for c in cyfry_y], lag_ratio=0.15),
                  FadeIn(kropki_y), run_time=1.2)
        self.next_slide()

        wspolne = 3
        tlo = VGroup(*[
            Rectangle(width=BOK, height=kx[i].get_top()[1] - ky[i].get_bottom()[1] + 0.12, stroke_width=0)
            .set_fill(O, 0.18).move_to([kx[i].get_center()[0], (kx[i].get_top()[1] + ky[i].get_bottom()[1]) / 2, 0])
            for i in range(wspolne)
        ]).set_z_index(-1)
        xs = (kx[wspolne - 1].get_right()[0] + kx[wspolne].get_left()[0]) / 2
        roznica = DashedLine([xs, kx[0].get_top()[1] + 0.15, 0], [xs, ky[0].get_bottom()[1] - 0.15, 0],
                             color=RED_D, stroke_width=3)
        opis_wsp = Tex(r"wspólny początek", font_size=30, color=O).next_to(tlo, DOWN, buff=0.25)
        self.play(FadeIn(tlo), Create(roznica), FadeIn(opis_wsp))
        self.next_slide()

        moral = Tex(r"im dłużej strumienie się zgadzają, tym są sobie bliższe", font_size=32)
        moral.move_to([0, -2.6, 0])
        self.play(FadeIn(moral, shift=0.2 * UP))
        self.wait(0.2)
        self.next_slide()
