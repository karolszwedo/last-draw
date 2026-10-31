# Przepis na efekty dźwiękowe Last Draw w stylu 8-bit (jak konsola NES).
# Uruchomienie (z folderu 01-last-draw):
#   python -P narzedzia/zrob_dzwieki.py              -> wybrane dźwięki do godot/assets/dzwieki/
#   python -P narzedzia/zrob_dzwieki.py <folder>     -> wszystkie wersje do odsłuchu
#
# Skąd brzmienie „8-bit”: NES miał tylko proste fale — prostokątną (pulse), trójkątną i szum —
# a głośność w 16 stopniach. Tu robimy to samo w Pythonie.
import math
import random
import struct
import sys
import wave

SR = 22050                     # próbek na sekundę
random.seed(7)                 # ten sam „los” przy każdym uruchomieniu = te same dźwięki


def pulse(f, t, duty=0.5):
    return 1.0 if (t * f) % 1.0 < duty else -1.0


def triangle(f, t):
    x = (t * f) % 1.0
    v = 4 * x - 1 if x < 0.5 else 3 - 4 * x
    return round(v * 7.5) / 7.5              # schodki jak w NES (16 poziomów)


def vol(v):
    return int(max(0.0, min(1.0, v)) * 15) / 15     # głośność w 16 stopniach (0..15), cichnie do zera


class Szum:
    """Szum 1-bitowy: losowe +1/-1 trzymane przez chwilę; im rzadsza zmiana, tym niższy szum."""
    def __init__(self):
        self.faza, self.v = 0.0, 1.0

    def next(self, f):
        self.faza += f / SR
        if self.faza >= 1.0:
            self.faza %= 1.0
            self.v = random.choice((-1.0, 1.0))
        return self.v


def zapisz(sciezka, probki, szczyt=0.8, petla=False):
    probki = list(probki)
    if not petla:                                   # 10 ms wyciszenia na końcu: bez „pyknięcia”
        k = int(0.01 * SR)
        for i in range(k):
            probki[-k + i] *= 1 - i / k
    m = max(abs(x) for x in probki) or 1.0
    dane = b''.join(struct.pack('<h', int(x / m * szczyt * 32767)) for x in probki)
    with wave.open(sciezka, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(dane)


def miks(*sciezki):
    n = max(len(s) for s in sciezki)
    return [sum(s[i] for s in sciezki if i < len(s)) for i in range(n)]


def opoznij(s, sek, glosnosc):
    return [0.0] * int(sek * SR) + [x * glosnosc for x in s]


# ---------- strzał ----------
def strzal(dlugosc=0.4):
    sz, out = Szum(), []
    for i in range(int(dlugosc * SR)):
        t = i / SR
        f = 1500 + 8500 * math.exp(-t / 0.06)                # szum opada z wysokiego na niski
        huk = sz.next(f) * vol(math.exp(-t / 0.09))
        uderzenie = pulse(40 + 140 * math.exp(-t / 0.02), t) * vol(math.exp(-t / 0.04)) * 0.6
        out.append(huk + uderzenie)
    return out


def strzal_echo():
    s = strzal()
    return miks(s, opoznij(s, 0.18, 0.35), opoznij(s, 0.36, 0.12))   # echo jak w kanionie


# ---------- dzwon ----------
def ding(dlugosc=1.6, zanik=0.5):
    out = []
    for i in range(int(dlugosc * SR)):
        t = i / SR
        e = vol(math.exp(-t / zanik))
        out.append((pulse(1046.5, t, 0.25) + 0.4 * pulse(1568.0, t, 0.125)) * e)
    return out


def bong(dlugosc=3.0):
    # dzwon kościelny: kilka tonów naraz (jak prawdziwy dzwon), niski i długi
    out = []
    for i in range(int(dlugosc * SR)):
        t = i / SR
        e = vol(math.exp(-t / 1.0)); e2 = vol(math.exp(-t / 0.35))
        out.append(triangle(220, t) * e + 0.3 * pulse(264, t, 0.5) * e
                   + 0.25 * pulse(330, t, 0.25) * e + 0.4 * pulse(440, t, 0.125) * e2)
    return out


def ding_ding():
    return miks(ding(1.4, 0.3), opoznij(ding(1.4, 0.45), 0.32, 1.0))


# ---------- wiatr (zapętlony: koniec przechodzi płynnie w początek) ----------
def wiatr(dlugosc=6.0, gwizd=False):
    sz, out, lp = Szum(), [], 0.0
    n, zakladka = int(dlugosc * SR), int(0.5 * SR)
    for i in range(n + zakladka):
        t = i / SR
        # podmuchy: wolne fale, pełne cykle w 6 s, żeby pętla się zgadzała
        p = 0.5 + 0.3 * math.sin(2 * math.pi * t / 6) + 0.2 * math.sin(2 * math.pi * 3 * t / 6 + 1.3)
        lp += 0.15 * (sz.next(1200 + 2800 * p) - lp)          # łagodzimy ostry szum
        v = lp * vol(0.25 + 0.6 * p)
        if gwizd:
            v += 0.12 * triangle(700 + 150 * math.sin(2 * math.pi * 2 * t / 6), t) * vol(max(0, p - 0.55) * 2)
        out.append(v)
    for i in range(zakladka):                                 # zakładka: płynne sklejenie końca z początkiem
        a = i / zakladka
        out[i] = out[i] * a + out[n + i] * (1 - a)
    return out[:n]


if __name__ == '__main__':
    # Wszystkie wersje liczymy zawsze w tej samej kolejności, bo każda zużywa część „losu” (szumu);
    # dzięki temu wybrane pliki są dokładnie takie, jakich Karol słuchał.
    wersje = {
        'strzal_1_krotki.wav': (strzal(), 0.8, False),
        'strzal_2_z_echem.wav': (strzal_echo(), 0.8, False),
        'dzwon_1_ding.wav': (ding(), 0.8, False),
        'dzwon_2_bong.wav': (bong(), 0.8, False),
        'dzwon_3_ding_ding.wav': (ding_ding(), 0.8, False),
        'wiatr_1_szum.wav': (wiatr(), 0.5, True),
        'wiatr_2_szum_z_gwizdem.wav': (wiatr(gwizd=True), 0.5, True),
    }
    if len(sys.argv) > 1:                                     # wszystkie wersje do odsłuchu
        cel = sys.argv[1].rstrip('/\\') + '/'
        pliki = {n: n for n in wersje}
    else:                                                     # wybór Karola (31.10.2026) do gry
        cel = 'godot/assets/dzwieki/'
        pliki = {'dzwon_1_ding.wav': 'dzwon.wav',
                 'strzal_2_z_echem.wav': 'strzal.wav',
                 'wiatr_2_szum_z_gwizdem.wav': 'wiatr.wav'}
    for nazwa, plik in pliki.items():
        probki, szczyt, petla = wersje[nazwa]
        zapisz(cel + plik, probki, szczyt, petla)
    print('gotowe:', cel, sorted(pliki.values()))
