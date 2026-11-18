from manim_slides import Slide
from common import *


class Podsumowanie(Slide):
    """Sześć wniosków; po prawej rysunek do każdego: pętla p(x,x), T_0, zbieżność, zupełność, punkt stały."""

    def construct(self):
        O = KOLOR_CZESCIOWA
        B = KOLOR_METRYKA
        KOLOR_Y = ManimColor("#7B3FA0")
        FS = 28

        naglowek = Tex(r"Podsumowanie", font_size=48)
        self.play(FadeIn(naglowek))
        self.next_slide()
        self.play(naglowek.animate.scale(44 / 48).to_edge(UP, buff=0.4), run_time=1.0)

        # ---- Wnioski ----
        def punkt_listy(tekst):
            t = Tex(tekst, font_size=FS, tex_environment="flushleft")
            kropka = Dot(radius=0.04).move_to(t.get_corner(UL) + 0.22 * LEFT + 0.13 * DOWN)
            return VGroup(kropka, t)

        wnioski = VGroup(
            punkt_listy(r"Metryka częściowa dopuszcza $p(x,x)\ge 0$,\\"
                        r"czyli mierzy, jak słabo określony jest punkt."),
            punkt_listy(r"Metryki to dokładnie te metryki częściowe,\\w których $p(x,x)=0$."),
            punkt_listy(r"Topologia $\tau_p$ jest $T_0$, ale nie musi być $T_1$,\\"
                        r"a granice ciągów nie muszą być jednoznaczne."),
            punkt_listy(r"W $\tau_p$ mamy $x_n\to x$ wtedy i tylko wtedy, gdy\\"
                        r"$\lim p(x,x_n)=p(x,x)$."),
            punkt_listy(r"$(X,p)$ jest zupełna, gdy każdy ciąg Cauchy'ego zbiega do $x$,\\"
                        r"dla którego $p(x,x)=\lim p(x,x_n)=\lim p(x_n,x_m)$."),
            punkt_listy(r"Twierdzenie Banacha przenosi się na zupełne przestrzenie\\"
                        r"częściowo metryczne, a punkt stały jest w pełni określony."),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        wnioski.next_to(naglowek, DOWN, buff=0.45).to_edge(LEFT, buff=0.5)

        # ---- Pętla z tytułu, po prawej ----
        srodek = np.array([4.9, 0.6, 0])
        punkt = Dot(srodek, radius=0.09)
        etykieta_x = MathTex("x", font_size=36).next_to(punkt, DOWN, buff=0.15)
        petla = Arc(radius=0.35, start_angle=-PI / 2 + 0.45, angle=2 * PI - 0.9,
                    arc_center=srodek + 0.42 * UP, color=O).add_tip(tip_length=0.15)
        wzor_p = MathTex(r"p", r"(x,x)", r"\ge", r"0", font_size=38, color=O).next_to(petla, UP, buff=0.3)

        # Każdy wniosek pojawia się razem ze swoją animacją po prawej.
        # 1. p(x,x) >= 0: rysunek z pętlą.
        self.play(FadeIn(wnioski[0], shift=0.2 * RIGHT),
                  FadeIn(punkt, scale=0.5), FadeIn(etykieta_x), Create(petla), FadeIn(wzor_p), run_time=1.0)
        self.next_slide()

        # 2. Metryki: pętla na niebiesko i d(x,x) = 0.
        wzor_0 = MathTex(r"d", r"(x,x)", r"=", r"0", font_size=38, color=B).move_to(wzor_p)
        self.play(FadeIn(wnioski[1], shift=0.2 * RIGHT),
                  petla.animate.set_color(B),
                  # p i >= odpływają w górę, d i = wpływają od dołu, (x,x) i 0 zostają (zmieniają kolor).
                  FadeOut(wzor_p[0], shift=0.25 * UP), FadeOut(wzor_p[2], shift=0.25 * UP),
                  FadeIn(wzor_0[0], shift=0.25 * UP), FadeIn(wzor_0[2], shift=0.25 * UP),
                  ReplacementTransform(wzor_p[1], wzor_0[1]), ReplacementTransform(wzor_p[3], wzor_0[3]),
                  run_time=1.0)
        self.next_slide()

        # 3. Topologia: pętla znika, a w tym miejscu rysunek T_0.
        ramka = RoundedRectangle(width=3.4, height=1.9, corner_radius=0.15, color=GRAY_C, stroke_width=2)
        ramka.move_to(srodek + 0.1 * UP)
        px_ = Dot(ramka.get_center() + 0.7 * LEFT, radius=0.07)
        py_ = Dot(ramka.get_center() + 0.7 * RIGHT, radius=0.07)
        lx = MathTex("x", font_size=28).next_to(px_, DOWN, buff=0.1)
        ly = MathTex("y", font_size=28).next_to(py_, DOWN, buff=0.1)
        owal = Ellipse(width=1.2, height=1.2).move_to(px_)
        otoczenie = VGroup(
            owal.copy().set_stroke(width=0).set_fill(B, 0.15),
            DashedVMobject(owal.copy().set_stroke(B, 2.5), num_dashes=30),
        )
        naz = MathTex(r"T_0", font_size=34).next_to(ramka, UP, buff=0.12)
        panel_t0 = VGroup(ramka, px_, py_, lx, ly, otoczenie, naz)
        self.play(FadeIn(wnioski[2], shift=0.2 * RIGHT),
                  # stary rysunek najpierw znika, nowy pojawia się zaraz po nim (bez nakładania)
                  Succession(FadeOut(VGroup(punkt, etykieta_x, petla, wzor_0), run_time=0.5),
                             FadeIn(VGroup(ramka, px_, py_, lx, ly, naz), run_time=0.6)), run_time=1.1)
        self.play(FadeIn(otoczenie))
        self.next_slide()

        # 4. Zbieżność: wartości p(x,x_n) dążą do poziomu p(x,x) (a nie do 0).
        ax = Axes(x_range=[0, 8, 2], y_range=[0, 3, 1], x_length=3.2, y_length=2.6, tips=False,
                  axis_config={"include_numbers": True, "font_size": 22}).move_to(np.array([4.2, 0.2, 0]))
        etyk_n = MathTex("n", font_size=26).next_to(ax.x_axis, RIGHT, buff=0.12)
        poziom = 1.0
        linia = DashedLine(ax.c2p(0, poziom), ax.c2p(8, poziom), color=O, stroke_width=2.5)
        etyk_linia = MathTex(r"p(x,x)", font_size=26, color=O).next_to(ax.c2p(8, poziom), DOWN, buff=0.12) \
            .align_to(ax.c2p(8, 0), RIGHT)
        kropki_x = VGroup(*[Dot(ax.c2p(n, poziom + 1.2 * 0.65 ** n), radius=0.05) for n in range(1, 9)])
        # Legenda nad wykresem zamiast podpisów przy kropkach.
        etyk_x = VGroup(Dot(radius=0.05), MathTex(r"p(x,x_n)", font_size=26)).arrange(RIGHT, buff=0.1)
        etyk_x.next_to(ax, UP, buff=0.2).align_to(ax, LEFT)
        self.play(FadeIn(wnioski[3], shift=0.2 * RIGHT),
                  Succession(FadeOut(panel_t0, run_time=0.5),
                             AnimationGroup(Create(ax), FadeIn(etyk_n), run_time=0.8)), run_time=1.3)
        self.play(Create(linia), FadeIn(etyk_linia))
        self.play(LaggedStart(*[FadeIn(k, scale=0.5) for k in kropki_x], lag_ratio=0.25),
                  FadeIn(etyk_x), run_time=2.0)
        self.next_slide()

        # 5. Zupełność: także p(x_n,x_m) dąży do tego samego poziomu p(x,x).
        kropki_c = VGroup(*[Dot(ax.c2p(n, poziom + 1.9 * 0.8 ** n), radius=0.05, color=KOLOR_Y)
                            for n in range(1, 9)])
        etyk_c = VGroup(Dot(radius=0.05, color=KOLOR_Y), MathTex(r"p(x_n,x_m)", font_size=26, color=KOLOR_Y)
                        ).arrange(RIGHT, buff=0.1)
        etyk_c.next_to(etyk_x, RIGHT, buff=0.4)
        self.play(FadeIn(wnioski[4], shift=0.2 * RIGHT),
                  LaggedStart(*[FadeIn(k, scale=0.5) for k in kropki_c], lag_ratio=0.25),
                  FadeIn(etyk_c), run_time=2.0)
        self.play(Indicate(VGroup(linia, etyk_linia), color=O, scale_factor=1.08))
        self.next_slide()

        # 6. Twierdzenie Banacha: wraca pętla, p(x*,x*) = 0 na pomarańczowo.
        wykres = VGroup(ax, etyk_n, linia, etyk_linia, kropki_x, etyk_x, kropki_c, etyk_c)
        petla.set_color(O)
        # Wzory podzielone na części, żeby podmieniać tylko to, co się zmienia.
        wzor_a = MathTex(r"p(", r"x", r",", r"x", r")", r"\ge", r"0", font_size=38, color=O).move_to(wzor_0)
        wzor_b = MathTex(r"p(", r"x", r"^*", r",", r"x", r"^*", r")", r"=", r"0", font_size=38, color=O)
        wzor_b.move_to(wzor_a)
        etyk_b = MathTex(r"x", r"^*", font_size=36).move_to(etykieta_x).align_to(etykieta_x, LEFT)
        self.play(FadeIn(wnioski[5], shift=0.2 * RIGHT),
                  Succession(FadeOut(wykres, run_time=0.5),
                             AnimationGroup(FadeIn(punkt), FadeIn(etykieta_x), FadeIn(petla), FadeIn(wzor_a),
                                            run_time=0.6)), run_time=1.1)
        self.next_slide()

        # x -> x*: gwiazdki wpadają z góry; >= odpływa w górę, = wpływa od dołu.
        anim = [
            *[ReplacementTransform(wzor_a[i], wzor_b[j]) for i, j in ((0, 0), (1, 1), (2, 3), (3, 4), (4, 6), (6, 8))],
            ReplacementTransform(etykieta_x, etyk_b[0]),
            FadeIn(wzor_b[2], shift=0.3 * DOWN), FadeIn(wzor_b[5], shift=0.3 * DOWN),
            FadeIn(etyk_b[1], shift=0.3 * DOWN),
            FadeOut(wzor_a[5], shift=0.25 * UP), FadeIn(wzor_b[7], shift=0.25 * UP),
        ]
        self.play(*anim, run_time=1.2, rate_func=smooth)
        self.play(Flash(punkt, color=O, line_length=0.25, flash_radius=0.3))
        self.next_slide()


class Literatura(Slide):
    """Literatura."""

    def construct(self):
        naglowek = Tex(r"Literatura", font_size=44).to_edge(UP, buff=0.4)
        pozycje = [
            r"S.\,G.~Matthews, \emph{Metric domains for completeness},\\"
            r"praca doktorska, University of Warwick, 1985.",
            r"S.\,G.~Matthews, \emph{Partial metric topology},\\"
            r"Annals of the New York Academy of Sciences 728 (1994), 183--197.",
            r"M.~Bukatin, R.~Kopperman, S.\,G.~Matthews, H.~Pajoohesh, \emph{Partial metric spaces},\\"
            r"The American Mathematical Monthly 116 (2009), no.~8, 708--718.",
            r"G.~Kahn, \emph{The semantics of a simple language for parallel programming},\\"
            r"Information Processing 74 (Proc.\ IFIP Congress), North-Holland, 1974, 471--475.",
            r"S.\,G.~Matthews, \texttt{partialmetric.org} (\texttt{dcs.warwick.ac.uk/pmetric}).",
        ]
        wiersze = VGroup()
        for i, t in enumerate(pozycje, start=1):
            nr = Tex(rf"[{i}]", font_size=28, color=KOLOR_DRUGORZEDNY)
            tekst = VGroup(*[MathTex(r"\text{" + linia + "}", font_size=28) for linia in t.split(r"\\")])
            tekst.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            wiersz = VGroup(nr, tekst).arrange(RIGHT, buff=0.25, aligned_edge=UP)
            wiersze.add(wiersz)
        wiersze.arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        wiersze.next_to(naglowek, DOWN, buff=0.5)
        if wiersze.width > 13:
            wiersze.scale_to_fit_width(13)
        wiersze.set_x(0)

        self.play(FadeIn(naglowek))
        self.play(LaggedStart(*[FadeIn(w, shift=0.2 * RIGHT) for w in wiersze], lag_ratio=0.2), run_time=2.0)
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
