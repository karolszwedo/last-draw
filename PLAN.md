# Last Draw — plan

Każdy krok = jedna rzecz, którą Karol sprawdzi w kilka minut. Po „działa” — commit.
Najpierw cała gra na szarych prostokątach, grafika i dźwięk na końcu (etap 5).

## Etap 0 — przygotowanie

- [x] Prywatne repo na GitHubie (`karolszwedo/last-draw`), Git LFS na grafikę i dźwięk.
- [x] Projekt Godota w `godot\`, renderer **Kompatybilny** (żeby działało w przeglądarce).
- [x] Wybór paczki pixel art (postacie + tło westernu) → wpis do `ASSETY.md` (31.10.2026).
- [x] Dźwięki dzwonu, strzału i wiatru — własne 8-bit z `narzedzia/zrob_dzwieki.py` (31.10.2026).
- [x] Muzyka 8-bit w klimacie westernu: „Lasso Lady” (CC0) → `ASSETY.md` (31.10.2026).

## Etap 1 — rdzeń pojedynku (szare prostokąty)

- [x] Dwa prostokąty naprzeciw siebie i napis „Ready…”.
- [x] Po losowej pauzie napis zmienia się na „FIRE!”.
- [x] Spacja po „FIRE!” → wyświetla czas reakcji.
- [x] Spacja przed „FIRE!” → „Too early!” (falstart).
- [x] Przeciwnik strzela po swoim czasie → „You win” / „You lose”.
- [x] Klawisz restartu (R) → nowa runda.

## Etap 2 — tryb 1 gracza

- [x] 5 przeciwników po kolei, każdy szybszy; 2 życia.
- [x] Linijka tekstu o przeciwniku przed pojedynkiem.
- [x] Ekran wygranej (pokonany szef) i przegranej.
- [x] Rekord czasu reakcji zapisany na dysku i widoczny po ponownym uruchomieniu.

## Etap 3 — tryb 2 graczy

- [x] A (lewy) i L (prawy), kto pierwszy po sygnale, wygrywa rundę.
- [x] Falstart = runda dla przeciwnika; remis = powtórka.
- [x] Mecz do 3 wygranych, ekran zwycięzcy.

## Etap 4 — menu

- [x] Ekran startowy: 1 gracz / 2 graczy, powrót do menu po meczu (Esc).

## Etap 5 — grafika i dźwięk

- [x] Tło ulicy i stojące postacie w trybie 1 gracza (w miejsce prostokątów).
- [x] Animacja strzału i padania zamiast znikania (1 gracz), płaska kałuża.
- [x] To samo w trybie 2 graczy.
- [x] Dzwon, strzał, wiatr w obu trybach.
- [x] Muzyka w tle (autoload `Music`), cichnie przed sygnałem; po strzale wraca, a wiatr cichnie.
- [x] Toczący się krzak w czasie czekania (własny rysunek, `krzak.gd`).

## Etap 5b — ekran tytułowy (dopisany 31.10.2026)

- [x] Podgląd: ruchome tło + napis w 3 krojach; wybrany Rye.
- [x] Ruchome tło ulicy w menu (paralaksa, `tlo_tytulowe.gd`), słońce, krzak wraca co jakiś czas.
- [x] Napis „LAST DRAW” i migające opcje.

## Etap 6 — wydanie

- [x] Eksport do przeglądarki (Web) i test w Chrome (31.10.2026): działa, dźwięk OK, proporcje keep.
      Paczka na itch.io: `export/last-draw-web.zip` (index.html w środku, poza gitem).
- [ ] Strona na itch.io (widoczność decyduje Karol), README w repo.
