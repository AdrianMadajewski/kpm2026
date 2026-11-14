from manim_slides import Slide
from common import *
import numpy as np


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


class Strumienie(Slide):
    """Intuicja Matthewsa: ciąg binarny liczony po kawałku i odległość przez wspólny początek."""

    def construct(self):
        O = KOLOR_CZESCIOWA
        B = KOLOR_METRYKA
        KOLOR_Y = ManimColor("#7B3FA0")
        BOK = 0.62

        naglowek = Tex(r"Obliczenie po kawałku", font_size=44).to_edge(UP, buff=0.4)
        self.add(naglowek)

        def wiersz(y, n=8):
            kratki = VGroup(*[Square(BOK, color=GRAY_C, stroke_width=2) for _ in range(n)])
            kratki.arrange(RIGHT, buff=0.08).move_to([-0.6, y, 0])
            return kratki

        def bit(b, kratka, kolor):
            return MathTex(str(b), font_size=36, color=kolor).move_to(kratka)

        def ulamek(lewa, n):
            tekst = r"=0" if n is None else (r"=1" if n == 0 else rf"=\tfrac{{1}}{{{2 ** n}}}")
            return MathTex(lewa, tekst, font_size=38)

        # ---- Ciąg x liczony bit po bicie ----
        kx = wiersz(1.1)
        ex = MathTex("x", "=", font_size=38, color=O).next_to(kx, LEFT, buff=0.3)
        licznik = ulamek(r"p(x,x)", 0).next_to(kx, RIGHT, buff=0.6)
        self.play(FadeIn(ex), Create(kx), FadeIn(licznik))
        podpis = Tex(r"im więcej policzyliśmy, tym mniejsza niepewność", font_size=30,
                     color=KOLOR_DRUGORZEDNY).next_to(kx, DOWN, buff=0.45)
        self.next_slide()

        bity_x = [0, 1, 1, 0, 1, 0, 0, 1]
        cyfry_x = VGroup()
        for i, b in enumerate(bity_x[:5]):
            c = bit(b, kx[i], O)
            cyfry_x.add(c)
            nowy = ulamek(r"p(x,x)", i + 1).move_to(licznik, aligned_edge=LEFT)
            anims = [FadeIn(c, shift=0.3 * DOWN), FadeOut(licznik, shift=0.2 * UP), FadeIn(nowy, shift=0.2 * UP)]
            if i == 0:
                anims.append(FadeIn(podpis))
            self.play(*anims, run_time=0.6)
            licznik = nowy
            self.next_slide()

        # ---- Ciąg nieskończony: w pełni określony ----
        reszta = VGroup(*[bit(b, kx[i], O) for i, b in enumerate(bity_x[5:], start=5)])
        kropki = MathTex(r"\dots", font_size=38, color=O).next_to(kx, RIGHT, buff=0.15)
        nowy = ulamek(r"p(x,x)", None).next_to(kropki, RIGHT, buff=0.45)
        self.play(LaggedStart(*[FadeIn(c, shift=0.3 * DOWN) for c in reszta], lag_ratio=0.3),
                  FadeIn(kropki), FadeOut(licznik), FadeIn(nowy), run_time=1.0)
        licznik = nowy
        cyfry_x.add(*reszta)
        pelny = Tex(r"ciąg nieskończony --- w pełni określony", font_size=30, color=B).move_to(podpis)
        self.play(cyfry_x.animate.set_color(B), kropki.animate.set_color(B), ex.animate.set_color(B),
                  licznik.animate.set_color(B), FadeOut(podpis), FadeIn(pelny), run_time=0.8)
        self.next_slide()

        # ---- Drugi ciąg y i wspólny początek ----
        self.play(FadeOut(pelny), cyfry_x.animate.set_color(KOLOR_TEKST), kropki.animate.set_color(KOLOR_TEKST),
                  ex.animate.set_color(KOLOR_TEKST), licznik.animate.set_color(KOLOR_TEKST), run_time=0.6)
        ky = wiersz(-0.4)
        ey = MathTex("y", "=", font_size=38, color=KOLOR_Y).next_to(ky, LEFT, buff=0.3)
        bity_y = [0, 1, 1, 1, 0, 1, 1, 0]
        cyfry_y = VGroup(*[bit(b, ky[i], KOLOR_Y) for i, b in enumerate(bity_y)])
        kropki_y = MathTex(r"\dots", font_size=38, color=KOLOR_Y).next_to(ky, RIGHT, buff=0.15)
        self.play(FadeIn(ey), Create(ky))
        self.play(LaggedStart(*[FadeIn(c, shift=0.3 * DOWN) for c in cyfry_y], lag_ratio=0.15),
                  FadeIn(kropki_y), run_time=1.2)
        self.next_slide()

        # Wspólny początek: 0 1 1.
        wspolne = 3
        tlo = VGroup(*[
            Rectangle(width=BOK, height=kx[i].get_top()[1] - ky[i].get_bottom()[1] + 0.12, stroke_width=0)
            .set_fill(O, 0.18).move_to([kx[i].get_center()[0], (kx[i].get_top()[1] + ky[i].get_bottom()[1]) / 2, 0])
            for i in range(wspolne)
        ]).set_z_index(-1)
        roznica = DashedLine(
            [(kx[wspolne - 1].get_right()[0] + kx[wspolne].get_left()[0]) / 2, kx[0].get_top()[1] + 0.15, 0],
            [(kx[wspolne - 1].get_right()[0] + kx[wspolne].get_left()[0]) / 2, ky[0].get_bottom()[1] - 0.15, 0],
            color=RED_D, stroke_width=3)
        opis_wsp = Tex(r"wspólny początek", font_size=30, color=O).next_to(tlo, DOWN, buff=0.25)
        self.play(FadeIn(tlo), Create(roznica), FadeIn(opis_wsp))
        self.next_slide()

        wzor = MathTex(r"p(x,y)", r"=\tfrac{1}{2^{3}}", r"=\tfrac{1}{8}", font_size=40).move_to([0, -2.55, 0])
        self.play(FadeIn(wzor[0]))
        self.play(FadeIn(wzor[1], shift=0.2 * RIGHT))
        self.play(FadeIn(wzor[2], shift=0.2 * RIGHT))
        self.next_slide()
        moral = Tex(r"im dłużej ciągi się zgadzają, tym są bliżej", font_size=30,
                    color=KOLOR_DRUGORZEDNY).next_to(wzor, DOWN, buff=0.3)
        self.play(FadeIn(moral, shift=0.2 * UP))
        self.wait(0.2)
        self.next_slide()
