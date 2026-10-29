# Last Draw — GDD

Nazwa robocza. Pierwsza mini-gra na rozgrzewkę. Spisane 29.10.2026 z ankiety z Karolem.

## O co chodzi

Główna ulica miasteczka na Dzikim Zachodzie, południe. Dwóch rewolwerowców stoi naprzeciw siebie (widok
z boku). Napis „Ready…”, muzyka cichnie, zostaje wiatr, przez ulicę toczy się krzak. Po losowej pauzie bije
dzwon i wyskakuje „FIRE!”. Kto pierwszy strzeli, wygrywa. Kto strzeli przed dzwonem — przegrywa.

Cel nauki: przejść cały cykl gry od GDD do wydania na itch.io; nauczyć się odliczania czasu, stanów gry
(czekanie → sygnał → wynik), menu, dźwięku, animacji i zapisu rekordu.

## Ustalenia (ankieta 29.10.2026)

| Co | Decyzja |
|---|---|
| Grafika | 2D, pixel art z gotowej darmowej paczki |
| Sygnał | dzwon + napis „FIRE!” (gra działa też bez dźwięku) |
| Napięcie przed sygnałem | muzyka cichnie, zostaje wiatr; toczący się krzak |
| Tryby | 1 gracz vs komputer **i** 2 graczy na jednej klawiaturze |
| Klawisze | 1 gracz: spacja; 2 graczy: **A** (lewy) i **L** (prawy) |
| Przeciwnicy (1 gracz) | 5, z imionami i charakterem, coraz szybsi (imiona do ustalenia) |
| Falstart w 2 graczy | przegrana runda |
| Język gry | angielski |

## Zasady

**Pojedynek (wspólne dla obu trybów)**
- Po „Ready…” losowa pauza 2–6 s, potem dzwon + „FIRE!”.
- Strzał przed sygnałem = falstart = przegrana runda.
- Strzał po sygnale: wygrywa szybszy. Gra pokazuje czas reakcji, np. „0.312 s”.

**1 gracz**
- 5 przeciwników po kolei, każdy szybszy. Przed pojedynkiem jedna linijka tekstu o przeciwniku.
- Przeciwnik „strzela” po swoim czasie reakcji (z lekkim losowym rozrzutem). Propozycja na start:
  0,60 → 0,48 → 0,38 → 0,30 → 0,24 s (szef). Do dostrojenia w graniu.
- 2 życia: pierwsza przegrana (także falstart) → ten sam przeciwnik jeszcze raz; druga → koniec gry,
  powrót do pierwszego przeciwnika (decyzja Karola, 29.10.2026).
- Pokonanie szefa = wygrana gra. Rekord = najlepszy czas reakcji, zapisany na dysku.

**2 graczy**
- Gracz lewy: A, gracz prawy: L. Mecz do 3 wygranych rund.
- Falstart = runda dla przeciwnika. Strzał w tej samej klatce = remis, runda od nowa.

## W pierwszej wersji

- ekran startowy z wyborem: 1 gracz / 2 graczy,
- pojedynek z losową pauzą, falstartem i czasem reakcji,
- tryb 1 gracza: 5 przeciwników, ekran wygranej i przegranej, rekord,
- tryb 2 graczy: do 3 wygranych,
- pixel art: dwie postacie (stoi / strzela / pada), tło ulicy, krzak,
- dźwięki: dzwon, strzał, wiatr, muzyka w tle, która cichnie przed sygnałem,
- wersja do grania w przeglądarce na itch.io.

## NIE w pierwszej wersji

- celowanie, różne bronie, sklep, ulepszenia,
- fabuła dłuższa niż linijka tekstu o przeciwniku,
- gra przez internet,
- pad / telefon (tylko klawiatura),
- polska wersja językowa.

## Później (pomysły na potem)

- fałszywe sygnały (kracze wrona, trzaska okiennica — kto strzeli, ma falstart),
- przeciwnicy, którzy blefują (drgnięcie ręki przed dzwonem),
- powolne zbliżenie kamery na postacie,
- wersja w low poly 3D.

## Otwarte pytania

- Imiona i charaktery 5 przeciwników.
