# Last Draw — assety

Każdy gotowy asset (grafika, dźwięk, czcionka) wpisujemy tu w chwili dodania do projektu.
Bez licencji nie wolno wydać gry na itch.io.

| Co | Plik(i) w projekcie | Autor | Licencja | Link |
|---|---|---|---|---|
| Kowboj (64×64, stoi / strzela / pada; z boku, patrzy w lewo) | `godot/assets/linkninja/` (3 PNG + 3 pliki Aseprite, oryginał) | LinkNinja | „Feel free to use this in any project, no credit needed” (strona, 31.10.2026) | https://linkninja.itch.io/pixelart-cowboy |
| YEEHAW! — kafelki i tło Dzikiego Zachodu (8 px, styl NES) | `godot/assets/yeehaw/` (19 plików PNG, oryginał) | CURSED OFFERINGS | Wolno zmieniać i używać w projektach komercyjnych i niekomercyjnych (strona, 31.10.2026) | https://cursed-offerings.itch.io/yeehaw |

| Krój Rye (napis „LAST DRAW”) | `narzedzia/kroje/Rye-Regular.ttf` + `OFL-Rye.txt` (tylko do przepisu, w grze jest obrazek) | Nicole Fally, Sorkin Type Co | SIL Open Font License 1.1 — wolno używać w grach, także płatnych (31.10.2026) | https://fonts.google.com/specimen/Rye |
| Krój Silkscreen (małe napisy pikselowe) | `narzedzia/kroje/Silkscreen-Regular.ttf` + `OFL-Silkscreen.txt` (tylko do przepisu) | Jason Kottke | SIL Open Font License 1.1 (31.10.2026) | https://fonts.google.com/specimen/Silkscreen |
| Muzyka „Lasso Lady (seamless loop)” — western 8-bit (NES, FamiTracker), 140 bpm, pętla bez szwu | `godot/assets/muzyka/lassolady.ogg` | congusbongus | CC0 (domena publiczna, podpis niewymagany) (strona, 31.10.2026) | https://opengameart.org/content/lasso-lady-seamless-loop |

## Pliki przerobione (z tych powyżej)

Robi je przepis `narzedzia/sklej_grafike.py` (uruchomienie opisane w pliku).

| Plik | Z czego | Co zmienione |
|---|---|---|
| `godot/assets/tlo_ulica.png` (384×216, w grze ×3) | YEEHAW: niebo i skały, kaktusy, saloon i pas ziemi z przykładowej ulicy | złożone w jeden kadr, saloon pośrodku, pas piasku na dole na napisy |
| `godot/assets/kowboj.png` (16 klatek 64×64) | LinkNinja: strzał (5 klatek) + pierwsze 4 klatki padania | czarny obrys; klatka 0 służy jako „stoi” (oryginalna animacja „stoi” jest przodem, nie pasuje); leżący bez kapki i opuszczony o 2 px; okrągłą kałużę zastąpiła własna płaska (7 klatek) |

## Dźwięki własne

Wygenerowane przepisem `narzedzia/zrob_dzwieki.py` (styl 8-bit, fale jak w NES). Nasze, bez cudzej licencji.
Wybór Karola, 31.10.2026.

| Plik | Co | Wersja z przepisu |
|---|---|---|
| `godot/assets/dzwieki/dzwon.wav` | sygnał „FIRE!” — wysoki, krótki „dzyń” | `dzwon_1_ding` |
| `godot/assets/dzwieki/strzal.wav` | strzał z echem jak w kanionie | `strzal_2_z_echem` |
| `godot/assets/dzwieki/wiatr.wav` | wiatr z cichym gwizdem, pętla 6 s | `wiatr_2_szum_z_gwizdem` |

## Grafika własna

| Plik | Co |
|---|---|
| `godot/assets/krzak.png` (8 klatek 16×16, w grze ×3) | toczący się krzak, narysowany przepisem `narzedzia/sklej_grafike.py` (31.10.2026) |
| `godot/assets/tytul/daleko.png`, `srodek.png`, `blisko.png` | warstwy ruchomego tła ekranu tytułowego, złożone z YEEHAW (skały, kaktusy, sklep, saloon, bank) |
| `godot/assets/tytul/napis.png`, `opcje.png` | „LAST DRAW” krojem Rye i opcje krojem Silkscreen, przerobione na piksele (obrys, cień, kolory z YEEHAW) |

Podpis w grze (mile widziany, niewymagany): przy wydaniu dodać „Art: LinkNinja, CURSED OFFERINGS” w README i na itch.io.
