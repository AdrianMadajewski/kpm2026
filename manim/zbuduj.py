"""Renderuje sceny po kolei i składa je w jeden plik HTML (manim-slides).

Użycie:
    python zbuduj.py            # szybki podgląd (360p, 10 kl./s)
    python zbuduj.py --jakosc l # 480p
    python zbuduj.py --jakosc h # wersja na konferencję (1080p)
    python zbuduj.py --tylko-html   # bez renderowania, tylko składanie HTML
"""
import argparse
import subprocess
import sys

# Kolejność scen w prezentacji: (plik, klasa).
SCENY = [
    ("s00_tytul.py", "Tytul"),
    ("s01_plan.py", "Plan"),
    ("s02_metryka.py", "PrzestrzenMetryczna"),
    ("s03_topologia_metryczna.py", "TopologiaMetryczna"),
    ("s03_topologia_metryczna.py", "Oddzielanie"),
    ("s03_topologia_metryczna.py", "ZbieznoscMetryczna"),
    ("s01_plan.py", "PlanSekcja2"),
    ("s04_czesciowa.py", "MetrykaCzesciowa"),
    ("s05_przyklad_max.py", "PrzykladMax"),
    ("s05_przyklad_max.py", "Interpretacja"),
    ("s04_czesciowa.py", "MetrykaJakoSzczegolny"),
    ("s04_czesciowa.py", "WniosekOkreslonosc"),
    ("s01_plan.py", "PlanSekcja3"),
    ("s06_topologia_czesciowa.py", "PytaniaCzesciowa"),
    ("s06_topologia_czesciowa.py", "KulaCzesciowa"),
    ("s08_kule.py", "Kule"),
    ("s06_topologia_czesciowa.py", "LematBaza"),
    ("s06_topologia_czesciowa.py", "WlasnosciTopologii"),
    ("s07_zbieznosc.py", "Zbieznosc"),
    ("s01_plan.py", "PlanSekcja4"),
    ("s09_zupelnosc.py", "CiagCauchyego"),
    ("s09_zupelnosc.py", "ZupelnoscMax"),
    ("s10_punkt_staly.py", "Kontrakcja"),
    ("s10_punkt_staly.py", "TwierdzenieMatthewsa"),
    ("s01_plan.py", "PlanPodsumowanie"),
    ("s11_podsumowanie.py", "Podsumowanie"),
]

WYJSCIE = "prezentacja.html"


def uruchom(polecenie):
    print("$", " ".join(polecenie), flush=True)
    subprocess.run(polecenie, check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--jakosc", default="p", choices=["p", "l", "m", "h", "k"],
                        help="jakość: p=podgląd 360p/10fps, l=480p, m=720p, h=1080p, k=4K")
    parser.add_argument("--scena", help="renderuj tylko tę klasę sceny")
    parser.add_argument("--tylko-html", action="store_true")
    args = parser.parse_args()

    if not args.tylko_html:
        for plik, klasa in SCENY:
            if args.scena and klasa != args.scena:
                continue
            if args.jakosc == "p":
                opcje = ["-r", "640,360", "--fps", "10"]
            else:
                opcje = [f"-q{args.jakosc}"]
            uruchom([sys.executable, "-m", "manim", "render", *opcje,
                     "--disable_caching", plik, klasa])

    if args.scena:
        return  # pojedyncza scena: bez składania HTML

    uruchom([
        sys.executable, "-m", "manim_slides", "convert",
        *[klasa for _, klasa in SCENY], WYJSCIE,
        "--to", "html", "--one-file", "--offline",
        "-ctitle=Czy odległość punktu od samego siebie musi być zerowa?",
        "-cbackground_color=white",
        "-creveal_theme=white",
        "-cslide_number=true",
        "-cprogress=true",
    ])
    print(f"Gotowe: {WYJSCIE}")


if __name__ == "__main__":
    main()
