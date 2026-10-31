# Last Draw — assety

Każdy gotowy asset (grafika, dźwięk, czcionka) wpisujemy tu w chwili dodania do projektu.
Bez licencji nie wolno wydać gry na itch.io.

| Co | Plik(i) w projekcie | Autor | Licencja | Link |
|---|---|---|---|---|
| Kowboj (64×64, stoi / strzela / pada; z boku, patrzy w lewo) | `godot/assets/linkninja/` (3 PNG + 3 pliki Aseprite, oryginał) | LinkNinja | „Feel free to use this in any project, no credit needed” (strona, 31.10.2026) | https://linkninja.itch.io/pixelart-cowboy |
| YEEHAW! — kafelki i tło Dzikiego Zachodu (8 px, styl NES) | `godot/assets/yeehaw/` (19 plików PNG, oryginał) | CURSED OFFERINGS | Wolno zmieniać i używać w projektach komercyjnych i niekomercyjnych (strona, 31.10.2026) | https://cursed-offerings.itch.io/yeehaw |

## Pliki przerobione (z tych powyżej)

Robi je przepis `narzedzia/sklej_grafike.py` (uruchomienie opisane w pliku).

| Plik | Z czego | Co zmienione |
|---|---|---|
| `godot/assets/tlo_ulica.png` (384×216, w grze ×3) | YEEHAW: niebo i skały, kaktusy, saloon i pas ziemi z przykładowej ulicy | złożone w jeden kadr, saloon pośrodku, pas piasku na dole na napisy |
| `godot/assets/kowboj.png` (12 klatek 64×64) | LinkNinja: strzał (5 klatek) + pada (7 klatek) | czarny obrys; klatka 0 służy jako „stoi” (oryginalna animacja „stoi” jest przodem, nie pasuje) |

Podpis w grze (mile widziany, niewymagany): przy wydaniu dodać „Art: LinkNinja, CURSED OFFERINGS” w README i na itch.io.
