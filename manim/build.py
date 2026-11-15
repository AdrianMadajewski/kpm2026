"""Render all scenes in order and bundle them into a single HTML file (manim-slides).

Usage:
    python build.py                  # quick preview (360p, 10 fps)
    python build.py --quality h      # conference version (1080p, 60 fps)
    python build.py --scene Tytul    # render a single scene only (no HTML)
    python build.py --scene PrzykladMax --html   # render one scene and bundle it alone into PrzykladMax.html
    python build.py --html-only      # skip rendering, just bundle the HTML
    python build.py --scene PrzykladMax --html-only  # bundle one already rendered scene into PrzykladMax.html
    python build.py --quality m --web site          # website build: site/index.html + separate video files
"""
import argparse
import os
import subprocess
import sys

# Scene order in the presentation: (file, scene class).
SCENES = [
    ("s00_tytul.py", "Tytul"),
    ("s01_plan.py", "Plan"),
    # 1. Metric spaces and their topology
    ("s02_metryka.py", "PrzestrzenMetryczna"),
    ("s03_topologia_metryczna.py", "TopologiaMetryczna"),
    ("s03_topologia_metryczna.py", "Oddzielanie"),
    ("s03_topologia_metryczna.py", "ZbieznoscMetryczna"),
    # 2. Partial metric spaces
    ("s01_plan.py", "PlanSekcja2"),
    ("s04_matthews.py", "Matthews"),
    ("s04_matthews.py", "Strumienie"),
    ("s05_czesciowa.py", "MetrykaCzesciowa"),
    ("s06_przyklad_max.py", "PrzykladMax"),
    ("s06_przyklad_max.py", "Interpretacja"),
    ("s05_czesciowa.py", "MetrykaJakoSzczegolny"),
    ("s05_czesciowa.py", "WniosekOkreslonosc"),
    # 3. Topology of partial metric spaces
    ("s01_plan.py", "PlanSekcja3"),
    ("s07_topologia_czesciowa.py", "PytaniaCzesciowa"),
    ("s07_topologia_czesciowa.py", "KulaCzesciowa"),
    ("s07_topologia_czesciowa.py", "Kule"),
    ("s07_topologia_czesciowa.py", "LematBaza"),
    ("s07_topologia_czesciowa.py", "WlasnosciTopologii"),
    ("s08_zbieznosc.py", "Zbieznosc"),
    # 4. Completeness and the fixed point theorem
    ("s01_plan.py", "PlanSekcja4"),
    ("s09_zupelnosc.py", "CiagCauchyego"),
    ("s09_zupelnosc.py", "ZupelnoscMax"),
    ("s10_punkt_staly.py", "Kontrakcja"),
    ("s10_punkt_staly.py", "TwierdzenieMatthewsa"),
    # Summary
    ("s01_plan.py", "PlanPodsumowanie"),
    ("s11_podsumowanie.py", "Podsumowanie"),
    ("s11_podsumowanie.py", "Literatura"),
    ("s11_podsumowanie.py", "Podziekowania"),
]

OUTPUT = "prezentacja.html"
TITLE = "Czy odległość punktu od samego siebie musi być zerowa?"

QUALITY = {
    "p": ["-r", "640,360", "--fps", "10"],  # preview
    "l": ["-ql"],  # 480p15
    "m": ["-qm"],  # 720p30
    "h": ["-qh"],  # 1080p60
    "k": ["-qk"],  # 2160p60
}


def run(cmd):
    print("$", " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--quality", default="p", choices=QUALITY,
                        help="p=preview 360p/10fps, l=480p, m=720p, h=1080p, k=4K (default: p)")
    parser.add_argument("--scene", help="render only this scene class (skips the HTML step)")
    parser.add_argument("--html-only", action="store_true", help="only bundle already rendered scenes")
    parser.add_argument("--html", action="store_true",
                        help="with --scene: also bundle that scene alone into <Scene>.html")
    parser.add_argument("--web", metavar="DIR",
                        help="bundle into DIR/index.html with videos as separate files (for GitHub Pages)")
    args = parser.parse_args()

    if args.scene and args.scene not in {cls for _, cls in SCENES}:
        parser.error(f"unknown scene: {args.scene}")

    if not args.html_only:
        todo = [(f, c) for f, c in SCENES if not args.scene or c == args.scene]
        for i, (file, cls) in enumerate(todo, start=1):
            print(f"[{i}/{len(todo)}] {cls}", flush=True)
            run([sys.executable, "-m", "manim", "render", *QUALITY[args.quality],
                 "--disable_caching", file, cls])

    if args.scene and not (args.html or args.html_only or args.web):
        return

    scenes = [args.scene] if args.scene else [cls for _, cls in SCENES]
    if args.web:
        os.makedirs(args.web, exist_ok=True)
        output = os.path.join(args.web, "index.html")
        bundle = []  # videos are copied next to index.html, keeping the page small
    else:
        output = f"{args.scene}.html" if args.scene else OUTPUT
        bundle = ["--one-file"]
    run([
        sys.executable, "-m", "manim_slides", "convert",
        *scenes, output,
        "--to", "html", *bundle, "--offline",
        f"-ctitle={TITLE}",
        "-cbackground_color=white",
        "-creveal_theme=white",
        "-cslide_number=true",
        "-cprogress=true",
    ])
    print(f"Done: {output}")


if __name__ == "__main__":
    main()
