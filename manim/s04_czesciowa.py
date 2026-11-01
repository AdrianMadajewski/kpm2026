from manim_slides import Slide
from common import *


def aksjomat(nazwa, *czesci):
    return VGroup(
        Tex(nazwa, font_size=30, color=KOLOR_DRUGORZEDNY),
        MathTex(*czesci, font_size=34),
    ).arrange(RIGHT, buff=0.3)


class MetrykaCzesciowa(Slide):
    def construct(self):
        naglowek = Tex(r"Przestrzeń częściowo metryczna", font_size=44).to_edge(UP, buff=0.4)

        # --- Docelowy układ: definicja metryki częściowej ---------------------
        wstep_p = VGroup(
            Tex(r"Metryka", r" częściowa", r" na zbiorze $X$ to funkcja", font_size=32),
            MathTex(r"p", r"\colon X\times X\to[0,\infty)", font_size=34),
            Tex(r"taka, że dla $x,y,z\in X$", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        p1 = aksjomat(r"(P1)", r"x=y \iff p(x,x)=p(x,y)=p(y,y)")
        p2 = aksjomat(r"(P2)", r"p(x,x)\le p(x,y)")
        p3 = aksjomat(r"(P3)", r"p(x,y)=p(y,x)")
        p4 = aksjomat(r"(P4)", r"p(x,z)\le p(x,y)+p(y,z)", r"-p(y,y)")
        p4[1][1].set_color(KOLOR_CZESCIOWA)
        aks_p = VGroup(p1, p2, p3, p4).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        nazwa = VGroup(
            Tex(r"Parę $(X,p)$ nazywamy", font_size=32),
            Tex(r"\emph{przestrzenią częściowo metryczną}.", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        tresc = VGroup(wstep_p, aks_p, nazwa).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        definicja = blok(tresc, "Definicja").to_edge(LEFT, buff=0.4).shift(0.25 * DOWN)

        # --- Układ początkowy: przypomnienie metryki, w tych samych miejscach --
        wstep_d = VGroup(
            Tex(r"Metryka", r" na zbiorze $X$ to funkcja", font_size=32),
            MathTex(r"d", r"\colon X\times X\to[0,\infty)", font_size=34),
            Tex(r"taka, że dla $x,y,z\in X$", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        wstep_d.align_to(wstep_p, UL)
        m1 = aksjomat(r"(M1)", r"d(x,y)=0 \iff x=y").align_to(p1, UL)
        m2 = aksjomat(r"(M2)", r"d(x,y)=d(y,x)").align_to(p2, UL)
        m3 = aksjomat(r"(M3)", r"d(x,z)\le d(x,y)+d(y,z)").align_to(p3, UL)

        # Krok 1: przypomnienie definicji metryki.
        definicja[0].become(tlo_dla(definicja, wstep_d, m1, m2, m3))
        self.play(FadeIn(naglowek))
        self.play(FadeIn(definicja[0]), FadeIn(definicja[1]), FadeIn(wstep_d), FadeIn(m1), FadeIn(m2), FadeIn(m3))
        self.next_slide()

        # Krok 2: pytanie — pętla z tytułu.
        srodek = np.array([3.6, 1.4, 0])
        punkt = Dot(srodek, radius=0.09)
        etyk_x = MathTex("x", font_size=34).next_to(punkt, DOWN, buff=0.15)
        petla = Arc(radius=0.35, start_angle=-PI / 2 + 0.45, angle=2 * PI - 0.9,
                    arc_center=srodek + 0.42 * UP, color=KOLOR_CZESCIOWA).add_tip(tip_length=0.15)
        wzor = MathTex(r"p(x,x) = \,?", font_size=38, color=KOLOR_CZESCIOWA).next_to(petla, RIGHT, buff=0.35)
        pytanie = VGroup(
            Tex(r"A gdyby odległość punktu", font_size=32),
            Tex(r"od siebie mogła być dodatnia?", font_size=32),
        ).arrange(DOWN, buff=0.12).next_to(VGroup(punkt, petla, wzor), DOWN, buff=0.5)
        grafika = VGroup(punkt, etyk_x, petla, wzor, pytanie)
        self.play(FadeIn(punkt), FadeIn(etyk_x), Create(petla), FadeIn(wzor))
        self.play(FadeIn(pytanie, shift=0.2 * UP))
        self.next_slide()

        # Krok 3: przemiana aksjomatów — każde przejście na osobne kliknięcie.
        self.play(FadeOut(grafika))
        # Zmiany wyróżniamy na pomarańczowo, potem wracają do czerni.
        definicja[0].become(tlo_dla(definicja, wstep_p, aks_p))
        # 1) „częściowa” wjeżdża w lukę (reszta wiersza się rozsuwa), d znika, p wjeżdża.
        wstep_p[0][1].set_color(KOLOR_CZESCIOWA)
        wstep_p[1][0].set_color(KOLOR_CZESCIOWA)
        # najpierw d wyjeżdża, a reszta wiersza robi miejsce na „częściowa”,
        self.play(
            FadeOut(wstep_d[1][0], shift=0.4 * LEFT),
            wstep_d[0][1].animate.move_to(wstep_p[0][2]),
            wstep_d[1][1].animate.move_to(wstep_p[1][1]),
            run_time=0.8,
        )
        # potem wjeżdżają „częściowa” i p.
        self.play(
            FadeIn(wstep_p[0][1], shift=0.4 * RIGHT),
            FadeIn(wstep_p[1][0], shift=0.4 * RIGHT),
            run_time=0.8,
        )
        # Podmiana obiektów na docelowe (te same napisy w tych samych miejscach).
        self.remove(wstep_d[0][0], wstep_d[0][1], wstep_d[1][1], wstep_d[2])
        self.add(wstep_p[0][0], wstep_p[0][2], wstep_p[1][1], wstep_p[2])
        self.play(Indicate(wstep_p[0][1], color=KOLOR_CZESCIOWA, scale_factor=1.15),
                  Indicate(wstep_p[1][0], color=KOLOR_CZESCIOWA, scale_factor=1.3))
        # 2) powrót do czerni.
        self.wait(0.6)
        self.play(wstep_p[0][1].animate.set_color(KOLOR_TEKST),
                  wstep_p[1][0].animate.set_color(KOLOR_TEKST), run_time=0.8)
        self.next_slide()

        def zmien(stary, nowy, wzor_nowy, przesun=False, dopasuj=False):
            """Podświetl stary wzór -> (przesuń) -> zamień na nowy -> zgaś podświetlenie.

            dopasuj=True: wspólne znaki zostają na miejscu, zmieniają się tylko
            różniące się (np. d -> p, M3 -> P4). W przeciwnym razie stary wzór
            wyjeżdża w lewo, a nowy wjeżdża od lewej.
            """
            wzor_nowy.set_color(KOLOR_CZESCIOWA)
            self.play(stary[1].animate.set_color(KOLOR_CZESCIOWA), run_time=0.7)
            self.wait(0.3)
            if przesun:
                self.play(stary.animate.align_to(nowy, UL), run_time=1.0)
            if dopasuj:
                self.play(TransformMatchingShapes(stary, nowy), run_time=1.2)
            else:
                self.play(FadeOut(stary, shift=0.4 * LEFT), run_time=0.7)
                self.play(FadeIn(nowy, shift=0.4 * RIGHT), run_time=0.8)
            self.wait(0.6)
            self.play(wzor_nowy.animate.set_color(KOLOR_TEKST), run_time=0.8)

        # Najpierw nierówność trójkąta zjeżdża na dół...
        zmien(m3, VGroup(p4[0], p4[1][0]), p4[1][0], przesun=True, dopasuj=True)
        self.next_slide()
        # ...i dostaje dodatkowy człon -p(y,y).
        self.play(FadeIn(p4[1][1], shift=0.3 * LEFT), run_time=1.0)
        self.wait(0.4)
        self.play(Indicate(p4[1][1], color=KOLOR_CZESCIOWA, scale_factor=1.2), run_time=1.0)
        self.wait(0.6)
        self.play(p4[1][1].animate.set_color(KOLOR_TEKST), run_time=0.8)
        self.next_slide()

        # Pozostałe aksjomaty.
        zmien(m2, p3, p3[1], przesun=True, dopasuj=True)
        self.next_slide()
        zmien(m1, p1, p1[1])
        self.next_slide()
        p2[1].set_color(KOLOR_CZESCIOWA)
        self.play(FadeIn(p2, shift=0.2 * RIGHT), run_time=1.0)
        self.wait(0.6)
        self.play(p2[1].animate.set_color(KOLOR_TEKST), run_time=0.8)
        self.next_slide()

        # Krok 4: komentarze przy zmienionych aksjomatach.
        def komentarz(tekst, wiersz):
            k = Tex(r"$\leftarrow$ " + tekst, font_size=28, color=KOLOR_DRUGORZEDNY)
            return k.next_to(definicja[0], RIGHT, buff=0.3).match_y(wiersz)

        k1 = komentarz(r"rozróżnia punkty", p1)
        k2 = komentarz(r"nic nie jest bliżej $x$ niż samo $x$", p2)
        k4 = komentarz(r"silniejsza od zwykłej nierówności trójkąta", p4)
        for k in (k1, k2, k4):
            self.play(FadeIn(k, shift=0.2 * LEFT))
            self.next_slide()

        # Krok 5: nazwa przestrzeni.
        self.play(dopasuj_ramke(definicja, wstep_p, aks_p, nazwa))
        self.play(FadeIn(nazwa, shift=0.2 * RIGHT))
        self.next_slide()


class MetrykaJakoSzczegolny(Slide):
    """Stwierdzenie: p(x,x) = 0 dla każdego x  =>  p jest metryką."""

    def construct(self):
        naglowek = Tex(r"Przestrzeń częściowo metryczna", font_size=44).to_edge(UP, buff=0.4)
        self.add(naglowek)

        tw = blok(VGroup(
            Tex(r"Jeżeli $p$ jest metryką częściową na $X$ i $p(x,x)=0$", font_size=32),
            Tex(r"dla każdego $x\in X$, to $p$ jest metryką.", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15), "Stwierdzenie").next_to(naglowek, DOWN, buff=0.4)
        self.play(FadeIn(tw))
        self.next_slide()

        def etykieta(t):
            return Tex(t, font_size=30, color=KOLOR_DRUGORZEDNY)

        lewa_x = -5.0  # kolumna etykiet

        # (P4) -> (M3)
        y4 = 0.3
        e4 = etykieta(r"(P4)").move_to([lewa_x, y4, 0])
        w4 = MathTex(r"p(x,z)\le p(x,y)+p(y,z)", r"-", r"p(y,y)", font_size=38)
        w4[2].set_color(KOLOR_SAMO)
        w4.next_to(e4, RIGHT, buff=0.4)
        self.play(FadeIn(e4), FadeIn(w4))
        zero4 = MathTex("0", font_size=38, color=KOLOR_SAMO).move_to(w4[2])
        self.play(FadeOut(w4[2], shift=0.4 * LEFT), run_time=0.7)
        self.play(FadeIn(zero4, shift=0.4 * RIGHT), run_time=0.8)
        self.play(FadeOut(w4[1]), FadeOut(zero4))
        cel4 = etykieta(r"$=$ (M3)").next_to(w4[0], RIGHT, buff=0.5)
        self.play(FadeIn(cel4, shift=0.2 * LEFT))
        self.next_slide()

        # (P1) -> (M1)
        y1 = -0.7
        e1 = etykieta(r"(P1)").move_to([lewa_x, y1, 0])
        w1 = MathTex(r"x=y", r"\iff", r"p(x,x)", r"=", r"p(x,y)", r"=", r"p(y,y)", font_size=38)
        w1[2].set_color(KOLOR_SAMO)
        w1[6].set_color(KOLOR_SAMO)
        w1.next_to(e1, RIGHT, buff=0.4)
        self.play(FadeIn(e1), FadeIn(w1))
        z2 = MathTex("0", font_size=38, color=KOLOR_SAMO).move_to(w1[2])
        z6 = MathTex("0", font_size=38, color=KOLOR_SAMO).move_to(w1[6])
        self.play(FadeOut(w1[2], shift=0.4 * LEFT), FadeOut(w1[6], shift=0.4 * LEFT), run_time=0.7)
        self.play(FadeIn(z2, shift=0.4 * RIGHT), FadeIn(z6, shift=0.4 * RIGHT), run_time=0.8)
        wynik1 = MathTex(r"x=y", r"\iff", r"p(x,y)=0", font_size=38)
        wynik1.shift(w1[0].get_left() - wynik1[0].get_left())
        self.play(FadeOut(VGroup(z2, w1[3], w1[4], w1[5], z6)), FadeIn(wynik1[2]))
        self.remove(w1[0], w1[1])
        self.add(wynik1)
        cel1 = etykieta(r"$=$ (M1)").next_to(wynik1, RIGHT, buff=0.5)
        self.play(FadeIn(cel1, shift=0.2 * LEFT))
        self.next_slide()

        # (P3) = (M2)
        y3 = -1.7
        e3 = etykieta(r"(P3)").move_to([lewa_x, y3, 0])
        w3 = MathTex(r"p(x,y)=p(y,x)", font_size=38).next_to(e3, RIGHT, buff=0.4)
        cel3 = etykieta(r"$=$ (M2)").next_to(w3, RIGHT, buff=0.5)
        self.play(FadeIn(e3), FadeIn(w3))
        self.play(FadeIn(cel3, shift=0.2 * LEFT))
        self.next_slide()

        # Morał.
        moral = VGroup(
            Tex(r"Metryki to dokładnie te metryki częściowe,", font_size=32, color=KOLOR_METRYKA),
            Tex(r"w których każdy punkt jest \emph{w pełni określony}.", font_size=32, color=KOLOR_METRYKA),
        ).arrange(DOWN, buff=0.12).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(moral, shift=0.2 * UP))
        self.next_slide()
