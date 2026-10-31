# Last Draw — plan

Każdy krok = jedna rzecz, którą Karol sprawdzi w kilka minut. Po „działa” — commit.
Najpierw cała gra na szarych prostokątach, grafika i dźwięk na końcu (etap 5).

## Etap 0 — przygotowanie

- [x] Prywatne repo na GitHubie (`karolszwedo/last-draw`), Git LFS na grafikę i dźwięk.
- [x] Projekt Godota w `godot\`, renderer **Kompatybilny** (żeby działało w przeglądarce).
- [x] Wybór paczki pixel art (postacie + tło westernu) → wpis do `ASSETY.md` (31.10.2026).
- [x] Dźwięki dzwonu, strzału i wiatru — własne 8-bit z `narzedzia/zrob_dzwieki.py` (31.10.2026).
- [ ] Wybór muzyki 8-bit w klimacie westernu → wpis do `ASSETY.md`.

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
- [ ] Muzyka w tle, cichnie przed sygnałem.
- [ ] Toczący się krzak w czasie czekania.

## Etap 6 — wydanie

- [ ] Eksport do przeglądarki (Web) i test.
- [ ] Strona na itch.io (widoczność decyduje Karol), README w repo.
