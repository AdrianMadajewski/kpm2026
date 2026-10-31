# Plan animacji (Manim + manim-slides)

Referat „Czy punkt musi być w odległości zero od siebie?”, OMatKo!!! 2026, limit 25 min.
Jasne tło. Kolory: metryka — niebieski, metryka częściowa — pomarańczowy, p(x,x) — czerwony.

## Motywy powracające
- **Mapa referatu**: metryka → metryka częściowa → topologia → zupełność → Banach; na początku każdej sekcji podświetla się bieżąca.
- **Rozmyty punkt**: pod punktem x czerwony odcinek długości p(x,x); kropka bez odcinka = punkt w pełni określony.
- **Pętla z tytułu**: wraca na końcu jako klamra.

## Sceny
| # | Scena | Animacja | Czas |
|---|---|---|---|
| 0 | Tytuł | tytuł, punkt z pętlą d(x,x)=0 → p(x,x)=? | 1 min |
| 1 | Mapa | pięć prostokątów połączonych strzałkami | 0,5 min |
| 2 | Przestrzeń metryczna | M1–M3 z ilustracjami (zlewające się punkty, symetryczne strzałki, trójkąt) | 2 min |
| 3 | Topologia metryczna | kula (x−ε,x+ε) kurczy się do punktu; zbieżny ciąg; rozłączne kule (Hausdorff) | 2 min |
| 4 | Metryka częściowa | M1–M3 → P1–P4, −p(y,y) na czerwono, powrót pętli | 2 min |
| 5 | p(x,x)=0 ⇒ metryka | czerwony wyraz w P4 znika, zostaje M3; P1 → M1 | 1,5 min |
| 6 | Przykład max | oś [0,5]; większy punkt = p(x,y); czerwony odcinek [0,x] (rozmyty punkt), suwak | 2,5 min |
| 7 | Przedziały | dwa przedziały i obejmujący je przedział; zwężanie | 1 min |
| 8 ★ | Kule | dwie osie: (x−ε,x+ε) znika w punkcie, [0,x+ε) zatrzymuje się na [0,x] | 2,5 min |
| 9 | Baza | mniejsza kula wokół y mieści się w kuli wokół x | 1 min |
| 10 | T₀, nie T₁ | asymetria: kula wokół x traci y, kula wokół y zawsze zawiera x | 1,5 min |
| 11 ★ | Ciąg x_n = 0 | punkt x jeździ po osi, kula [0,x+ε) zawsze zawiera 0 | 2 min |
| 12 | Zupełność | x_n = 1/n → 0, czerwone odcinki maleją; kandydat, zbieżność, przynależność | 2 min |
| 13 ★ | Banach | iteracja f(x)=x/2 łukami po osi, odcinki maleją do zera | 2,5 min |
| 14 | Klamra | mapa w całości, pętla: p(x,x)=? → p(x*,x*)=0, „Dziękuję za uwagę” | 1 min |

Kolejność pracy: 8 → 6 → pozostałe od 1. Bez pełnych dowodów.
