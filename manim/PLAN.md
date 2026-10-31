# Plan animacji (Manim + manim-slides)

Referat „Czy punkt musi być w odległości zero od siebie?”, OMatKo!!! 2026, limit 25 min.
Jasne tło. Kolory: metryka — niebieski, metryka częściowa — pomarańczowy, p(x,x) — czerwony.

## Motywy powracające
- **Plan referatu**: te same cztery punkty co w wersji Beamer, w ramkach połączonych strzałkami (`plan_referatu` w `common.py`); na początku każdej sekcji podświetla się bieżący punkt.
- **Rozmyty punkt**: pod punktem x czerwony odcinek długości p(x,x); kropka bez odcinka = punkt w pełni określony.
- **Pętla z tytułu**: wraca na końcu jako klamra.

## Sceny
| # | Scena | Animacja | Czas |
|---|---|---|---|
| 0 | Tytuł | tytuł, punkt z pętlą d(x,x)=0 → p(x,x)=? | 1 min |
| 1 | Plan | cztery punkty planu pojawiają się po kolei, potem wyróżnienie punktu 1 | 0,5 min |
| 2 | Przestrzeń metryczna | M1–M3 z ilustracjami (zlewające się punkty, symetryczne strzałki, trójkąt) | 2 min |
| 3 | Topologia metryczna | kula (x−ε,x+ε) kurczy się do punktu; zbieżny ciąg; rozłączne kule (Hausdorff) | 2 min |
| 4 | Metryka częściowa | M1–M3 → P1–P4, −p(y,y) na czerwono, powrót pętli | 2 min |
| 5 | Przykład max + intuicja | p = max to przedziały [0,x]; odcinek [0,x] = niepewność, kurczy się do 0; p(x,y) jako otoczka; (P2) | 2,5 min |
| 6 | p(x,x)=0 ⇒ metryka | czerwony wyraz w P4 znika, zostaje M3; P1 → M1 | 1,5 min |
| 7 | — | (scena z przedziałami włączona do sceny 5) | — |
| 8 ★ | Kule | dwie osie: (x−ε,x+ε) znika w punkcie, [0,x+ε) zatrzymuje się na [0,x] | 2,5 min |
| 9 | Baza | mniejsza kula wokół y mieści się w kuli wokół x | 1 min |
| 10 | T₀, nie T₁ | asymetria: kula wokół x traci y, kula wokół y zawsze zawiera x | 1,5 min |
| 11 ★ | Ciąg x_n = 0 | punkt x jeździ po osi, kula [0,x+ε) zawsze zawiera 0 | 2 min |
| 12 | Zupełność | x_n = 1/n → 0, czerwone odcinki maleją; kandydat, zbieżność, przynależność | 2 min |
| 13 ★ | Banach | iteracja f(x)=x/2 łukami po osi, odcinki maleją do zera | 2,5 min |
| 14 | Klamra | plan w całości, pętla: p(x,x)=? → p(x*,x*)=0, „Dziękuję za uwagę” | 1 min |

Kolejność pracy: sceny po kolei (8 zrobiona wcześniej). Bez pełnych dowodów.
