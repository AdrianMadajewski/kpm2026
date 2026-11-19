"""Render all scenes in order and bundle them into a single HTML file (manim-slides).

Usage:
    python build.py                  # quick preview (360p, 10 fps)
    python build.py --quality h      # conference version (1080p, 60 fps)
    python build.py --scene Tytul    # render a single scene only (no HTML)
    python build.py --scene PrzykladMax --html   # render one scene and bundle it alone into PrzykladMax.html
    python build.py --html-only      # skip rendering, just bundle the HTML
    python build.py --scene PrzykladMax --html-only  # bundle one already rendered scene into PrzykladMax.html
"""
import argparse
from pathlib import Path
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
    ("s09_zupelnosc.py", "MetrykaIndukowana"),
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


# Mały zegar w prawym dolnym rogu: rusza przy pierwszej zmianie slajdu, klawisz T go chowa/pokazuje.
ZEGAR = """
<div id="zegar-prezentacji" style="position:fixed;right:1.2vw;bottom:1.6vh;z-index:9999;
  font-family:ui-monospace,Consolas,monospace;font-size:clamp(11px,1.1vw,22px);
  color:#888780;opacity:0.75;letter-spacing:0.05em;pointer-events:none;user-select:none;">00:00</div>
<script>
(function () {
  var el = document.getElementById("zegar-prezentacji");
  var start = null;
  function fmt(ms) {
    var s = Math.floor(ms / 1000);
    return String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0");
  }
  function startuj() { if (start === null) start = Date.now(); }
  setInterval(function () { if (start !== null) el.textContent = fmt(Date.now() - start); }, 250);
  document.addEventListener("keydown", function (e) {
    if (e.key === "t" || e.key === "T") {
      el.style.visibility = el.style.visibility === "hidden" ? "visible" : "hidden";
    } else {
      startuj();
    }
  });
  document.addEventListener("click", startuj);
  function podepnij() {
    if (window.Reveal && Reveal.on) { Reveal.on("slidechanged", startuj); Reveal.on("fragmentshown", startuj); }
    else setTimeout(podepnij, 200);
  }
  podepnij();
})();
</script>
"""


def dodaj_zegar(path):
    html = Path(path).read_text(encoding="utf-8")
    if "zegar-prezentacji" in html:
        return
    i = html.rfind("</body>")
    Path(path).write_text(html[:i] + ZEGAR + html[i:], encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--quality", default="p", choices=QUALITY,
                        help="p=preview 360p/10fps, l=480p, m=720p, h=1080p, k=4K (default: p)")
    parser.add_argument("--scene", help="render only this scene class (skips the HTML step)")
    parser.add_argument("--html-only", action="store_true", help="only bundle already rendered scenes")
    parser.add_argument("--html", action="store_true",
                        help="with --scene: also bundle that scene alone into <Scene>.html")
    args = parser.parse_args()

    if args.scene and args.scene not in {cls for _, cls in SCENES}:
        parser.error(f"unknown scene: {args.scene}")

    if not args.html_only:
        todo = [(f, c) for f, c in SCENES if not args.scene or c == args.scene]
        for i, (file, cls) in enumerate(todo, start=1):
            print(f"[{i}/{len(todo)}] {cls}", flush=True)
            run([sys.executable, "-m", "manim", "render", *QUALITY[args.quality],
                 "--disable_caching", file, cls])

    if args.scene and not (args.html or args.html_only):
        return

    scenes = [args.scene] if args.scene else [cls for _, cls in SCENES]
    output = f"{args.scene}.html" if args.scene else OUTPUT
    run([
        sys.executable, "-m", "manim_slides", "convert",
        *scenes, output,
        "--to", "html", "--one-file", "--offline",
        f"-ctitle={TITLE}",
        "-cbackground_color=white",
        "-creveal_theme=white",
        "-cslide_number=false",
        "-cprogress=false",
    ])
    dodaj_zegar(output)
    print(f"Done: {output}")


if __name__ == "__main__":
    main()
