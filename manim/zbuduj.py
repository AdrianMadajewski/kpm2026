"""Renderuje sceny po kolei i składa je w jeden plik HTML (manim-slides).

Użycie:
    python zbuduj.py            # szybki podgląd (480p)
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
    ("s08_kule.py", "Kule"),
]

WYJSCIE = "prezentacja.html"


def uruchom(polecenie):
    print("$", " ".join(polecenie), flush=True)
    subprocess.run(polecenie, check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--jakosc", default="l", choices=["l", "m", "h", "k"],
                        help="jakość renderu: l=480p, m=720p, h=1080p, k=4K")
    parser.add_argument("--tylko-html", action="store_true")
    args = parser.parse_args()

    if not args.tylko_html:
        for plik, klasa in SCENY:
            uruchom([sys.executable, "-m", "manim", "render", f"-q{args.jakosc}",
                     "--disable_caching", plik, klasa])

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
