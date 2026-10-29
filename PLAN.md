# Last Draw — plan

Każdy krok = jedna rzecz, którą Karol sprawdzi w kilka minut. Po „działa” — commit.
Najpierw cała gra na szarych prostokątach, grafika i dźwięk na końcu (etap 5).

## Etap 0 — przygotowanie

- [x] Prywatne repo na GitHubie (`karolszwedo/last-draw`), Git LFS na grafikę i dźwięk.
- [x] Projekt Godota w `godot\`, renderer **Kompatybilny** (żeby działało w przeglądarce).
- [ ] Wybór paczki pixel art (postacie + tło westernu) i dźwięków → wpis do `ASSETY.md`.

## Etap 1 — rdzeń pojedynku (szare prostokąty)

- [x] Dwa prostokąty naprzeciw siebie i napis „Ready…”.
- [x] Po losowej pauzie napis zmienia się na „FIRE!”.
- [ ] Spacja po „FIRE!” → wyświetla czas reakcji.
- [ ] Spacja przed „FIRE!” → „Too early!” (falstart).
- [ ] Przeciwnik strzela po swoim czasie → „You win” / „You lose”.
- [ ] Klawisz restartu → nowa runda.

## Etap 2 — tryb 1 gracza

- [ ] 5 przeciwników po kolei, każdy szybszy, linijka tekstu przed pojedynkiem.
- [ ] Ekran wygranej (pokonany szef) i przegranej.
- [ ] Rekord czasu reakcji zapisany na dysku i widoczny po ponownym uruchomieniu.

## Etap 3 — tryb 2 graczy

- [ ] A (lewy) i L (prawy), kto pierwszy po sygnale, wygrywa rundę.
- [ ] Falstart = runda dla przeciwnika; remis = powtórka.
- [ ] Mecz do 3 wygranych, ekran zwycięzcy.

## Etap 4 — menu

- [ ] Ekran startowy: 1 gracz / 2 graczy, powrót do menu po meczu.

## Etap 5 — grafika i dźwięk

- [ ] Tło ulicy i postacie z paczki pixel art (stoi / strzela / pada).
- [ ] Dzwon, strzał, wiatr; muzyka cichnie przed sygnałem.
- [ ] Toczący się krzak w czasie czekania.

## Etap 6 — wydanie

- [ ] Eksport do przeglądarki (Web) i test.
- [ ] Strona na itch.io (widoczność decyduje Karol), README w repo.
