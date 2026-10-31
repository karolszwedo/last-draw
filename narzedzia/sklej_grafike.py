# Przepis na grafikę Last Draw: skleja tło ulicy i arkusz kowboja z pobranych paczek.
# Uruchomienie (z folderu 01-last-draw):  python -P narzedzia/sklej_grafike.py
# Wynik: godot/assets/tlo_ulica.png (384x216), godot/assets/kowboj.png (16 klatek 64x64)
#        i godot/assets/krzak.png (8 klatek 16x16, własny rysunek).
from PIL import Image

ASSETS = 'godot/assets/'
Y = ASSETS + 'yeehaw/'
W, H = 384, 216      # tło: 384x216, w grze powiększone 3x = okno 1152x648
G = 176              # linia ziemi (y), pod nią pas piasku na napisy

def wczytaj(sciezka):
    return Image.open(sciezka).convert('RGBA')

# --- tło ulicy z elementów YEEHAW ---
ulica = wczytaj(Y + '_exampleA_standard.png')     # przykładowa ulica: stąd saloon i pas ziemi
skaly = wczytaj(Y + 'yeehaw_parallax_layerC_standard.png')
kaktusy = wczytaj(Y + 'yeehaw_parallax_layerB_standard.png')

def wytnij_saloon():
    s = ulica.crop((186, 56, 286, 153))
    # niebo wokół saloonu robimy przezroczyste (zalewanie od brzegów, środka nie ruszamy)
    w, h = s.size
    tlo = {s.getpixel((x, 0))[:3] for x in range(w)} | {s.getpixel((x, y))[:3] for y in range(h) for x in (0, w - 1)}
    stos, byly = [(x, 0) for x in range(w)] + [(x, y) for y in range(h) for x in (0, w - 1)], set()
    while stos:
        x, y = stos.pop()
        if (x, y) in byly or not (0 <= x < w and 0 <= y < h):
            continue
        byly.add((x, y))
        if s.getpixel((x, y))[:3] in tlo:
            s.putpixel((x, y), (0, 0, 0, 0))
            stos += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return s

tlo = Image.new('RGBA', (W, H), skaly.getpixel((0, 0)))
for x in range(0, W, skaly.width):
    tlo.paste(skaly, (x, G - skaly.height), skaly)
for x in range(0, W, kaktusy.width):
    tlo.paste(kaktusy, (x, G - kaktusy.height + 2), kaktusy)
saloon = wytnij_saloon()
tlo.paste(saloon, ((W - saloon.width) // 2, G - saloon.height + 1), saloon)
pas = ulica.crop((152, 152, 296, 160))           # pas ziemi, 18 kafelków po 8 px
for x in range(0, W, pas.width):
    tlo.paste(pas, (x, G), pas)
for y in range(G + pas.height, H):
    for x in range(W):
        tlo.putpixel((x, y), (245, 132, 79, 255))
tlo.save(ASSETS + 'tlo_ulica.png')

# --- kowboj LinkNinja: klatki 0-4 strzał (0 = stoi, ręka przy kaburze), 5-8 pada, 9-15 rośnie kałuża ---
def klatki(sciezka, n):
    im = wczytaj(sciezka)
    return [im.crop((i * 64, 0, i * 64 + 64, 64)) for i in range(n)]

def obrys(k):
    # czarny obrys wokół postaci; pomijamy drobne krople (plamy mniejsze niż 20 pikseli)
    w, h = k.size
    pelne = {(x, y) for y in range(h) for x in range(w) if k.getpixel((x, y))[3] > 0}
    duze, byly = set(), set()
    for p in pelne:
        if p in byly:
            continue
        plama, stos = [], [p]
        while stos:
            q = stos.pop()
            if q in byly or q not in pelne:
                continue
            byly.add(q); plama.append(q)
            stos += [(q[0] + dx, q[1] + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
        if len(plama) >= 20:
            duze.update(plama)
    wynik = k.copy()
    for y in range(h):
        for x in range(w):
            if (x, y) not in pelne and any((x + dx, y + dy) in duze for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                wynik.putpixel((x, y), (0, 0, 0, 255))
    return wynik

KREW = (172, 50, 50, 255)
CIEMNA = (120, 30, 30, 255)
JASNA = (220, 110, 100, 255)

def bez_kapki(k):
    # leżące ciało bez kapki wiszącej pod brzuchem (czerwone piksele niżej niż wiersz 51),
    # opuszczone o 2 piksele, żeby leżało na ulicy, a nie wisiało nad nią
    k = k.copy()
    for y in range(52, 64):
        for x in range(27, 64):
            if k.getpixel((x, y))[:3] == KREW[:3]:
                k.putpixel((x, y), (0, 0, 0, 0))
    nizej = Image.new('RGBA', k.size, (0, 0, 0, 0))
    nizej.paste(k, (0, 2))
    return nizej

def kaluza(k, szer):
    # płaska kałuża na ziemi (widok z boku): 3 wiersze, wiersz 55 = linia ziemi w grze
    k = k.copy()
    srodek = 33
    for y, w, kolor in ((55, szer - 4, KREW), (56, szer, KREW), (57, szer - 2, CIEMNA)):
        for x in range(srodek - w // 2, srodek - w // 2 + w):
            k.putpixel((x, y), kolor)
    if szer >= 9:
        for x in (srodek - 2, srodek + 1, srodek + 2):
            k.putpixel((x, 55), JASNA)
    return k

N = ASSETS + 'linkninja/'
strzal = [obrys(k) for k in klatki(N + 'Cowboy_Attack_Animation.png', 5)]   # klatki 0-4
pada = klatki(N + 'Cowboy_Death_Animation.png', 7)
upadek = [obrys(k) for k in pada[:3]] + [obrys(bez_kapki(pada[3]))]         # klatki 5-8
lezy = upadek[-1]
kaluze = [kaluza(lezy, s) for s in (6, 10, 14, 18, 21, 24, 26)]                # klatki 9-15
wszystkie = strzal + upadek + kaluze
arkusz = Image.new('RGBA', (64 * len(wszystkie), 64), (0, 0, 0, 0))
for i, k in enumerate(wszystkie):
    arkusz.paste(k, (i * 64, 0))
arkusz.save(ASSETS + 'kowboj.png')
print('klatek w kowboj.png:', len(wszystkie))

# --- toczący się krzak (własny): kula splątanych gałązek, 8 klatek obrotu po 45 stopni ---
import random
from PIL import ImageDraw

def krzak(seed=21, galazki=16):
    random.seed(seed)                               # ten sam „los” = ten sam krzak przy każdym uruchomieniu
    S = 16
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    kolory = ((130, 85, 40, 255), (200, 150, 85, 255), (200, 150, 85, 255), (240, 205, 140, 255), (240, 205, 140, 255))
    for _ in range(galazki):                        # gałązki = łuki o losowej wielkości i miejscu
        r = random.randint(2, 6); lim = 7 - r
        cx = 7.5 + random.uniform(-lim, lim); cy = 7.5 + random.uniform(-lim, lim)
        a = random.randint(0, 359)
        d.arc((round(cx - r), round(cy - r), round(cx + r), round(cy + r)), a, a + random.randint(80, 220),
              fill=random.choice(kolory))
    wynik = im.copy()                               # czarny obrys tylko na zewnątrz kuli
    for y in range(S):
        for x in range(S):
            if im.getpixel((x, y))[3] == 0 and (x - 7.5) ** 2 + (y - 7.5) ** 2 > 25 and any(
                    0 <= x + dx < S and 0 <= y + dy < S and im.getpixel((x + dx, y + dy))[3]
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                wynik.putpixel((x, y), (0, 0, 0, 255))
    return wynik

k = krzak()
pasek = Image.new('RGBA', (16 * 8, 16), (0, 0, 0, 0))
for i in range(8):                                  # obrót zgodnie z zegarem = toczy się w prawo
    obrot = k.rotate(-45 * i, resample=Image.NEAREST, center=(7.5, 7.5))
    pasek.paste(obrot, (i * 16, 0))
pasek.save(ASSETS + 'krzak.png')
dol = k.getbbox()[3]
print('krzak: dół w klatce y =', dol, '-> pozycja y w grze =', 3 * G + 3 - 3 * (dol - 8))

stopy = wszystkie[0].getbbox()[3]
print('kowboj: dół postaci w klatce y =', stopy, '-> pozycja y w grze =', 3 * G + 3 - 3 * (stopy - 32))

# ================= ekran tytułowy (31.10.2026) =================
# Trzy warstwy tła do przesuwania z różną prędkością (paralaksa), napis i opcje w pikselach.
from PIL import ImageFont

T = ASSETS + 'tytul/'
KROJE = 'narzedzia/kroje/'
import os
os.makedirs(T, exist_ok=True)
NIEBO = skaly.getpixel((0, 0))

def wytnij_dom(box):
    # dom z przykładowej ulicy; niebo i białe pasy wokół robimy przezroczyste
    s = ulica.crop(box); w, h = s.size
    tlo_kolory = {(156, 221, 255), (255, 255, 255)}
    stos = [(x, 0) for x in range(w)] + [(x, y) for y in range(h) for x in (0, w - 1)]; byly = set()
    while stos:
        x, y = stos.pop()
        if (x, y) in byly or not (0 <= x < w and 0 <= y < h):
            continue
        byly.add((x, y))
        if s.getpixel((x, y))[:3] in tlo_kolory:
            s.putpixel((x, y), (0, 0, 0, 0)); stos += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return s

# warstwa daleka: niebo + skały (128 px szerokości, w grze powtarzana w kółko)
daleko = Image.new('RGBA', (skaly.width, H), NIEBO)
daleko.paste(skaly, (0, G - skaly.height), skaly)
daleko.save(T + 'daleko.png')

# warstwa środkowa: same kaktusy
srodek = Image.new('RGBA', (kaktusy.width, H), (0, 0, 0, 0))
srodek.paste(kaktusy, (0, G - kaktusy.height + 2), kaktusy)
srodek.save(T + 'srodek.png')

# warstwa bliska: sklep, saloon, bank, ziemia i piasek (768 px, też powtarzana)
blisko = Image.new('RGBA', (768, H), (0, 0, 0, 0))
for box, x in (((8, 60, 88, 137), 40), ((191, 56, 286, 153), 300), ((392, 84, 504, 161), 560)):
    dom = wytnij_dom(box)
    blisko.paste(dom, (x, G - dom.height + 1), dom)
for x in range(0, blisko.width, pas.width):
    blisko.paste(pas, (x, G), pas)
for y in range(G + pas.height, H):
    for x in range(blisko.width):
        blisko.putpixel((x, y), (245, 132, 79, 255))
blisko.save(T + 'blisko.png')

def maska_tekstu(tekst, kroj, rozmiar):
    f = ImageFont.truetype(KROJE + kroj, rozmiar)
    l, t, r, b = f.getbbox(tekst)
    m = Image.new('L', (r - l + 2, b - t + 2), 0)
    d = ImageDraw.Draw(m); d.fontmode = '1'          # bez wygładzania = ostre piksele
    d.text((1 - l, 1 - t), tekst, font=f, fill=255)
    return m

def napis_tytulowy(tekst, kroj, szer=300, wys=40):
    rozmiar = 10                                     # największy rozmiar, który mieści się w szer x wys
    while True:
        bb = ImageFont.truetype(KROJE + kroj, rozmiar + 1).getbbox(tekst)
        if bb[2] - bb[0] > szer or bb[3] - bb[1] > wys:
            break
        rozmiar += 1
    m = maska_tekstu(tekst, kroj, rozmiar); w, h = m.size; px = m.load()
    def pelne(x, y): return 0 <= x < w and 0 <= y < h and px[x, y] > 0
    out = Image.new('RGBA', (w + 4, h + 5), (0, 0, 0, 0))
    for y in range(-2, h + 3):                       # cień: ciemny brąz, 2 piksele niżej
        for x in range(-2, w + 2):
            if pelne(x, y - 3): out.putpixel((x + 2, y + 2), (93, 59, 25, 255))
    for y in range(-1, h + 1):                       # czarny obrys
        for x in range(-1, w + 1):
            if not pelne(x, y) and any(pelne(x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)):
                out.putpixel((x + 2, y + 2), (0, 0, 0, 255))
    for y in range(h):                               # kolory: piasek u góry, pomarańcz na dole
        a = y / max(1, h - 1)
        kol = (255, 217, 135) if a < 0.45 else ((248, 177, 65) if a < 0.75 else (245, 132, 79))
        for x in range(w):
            if pelne(x, y): out.putpixel((x + 2, y + 2), kol + (255,))
    return out

def napis_maly(tekst):
    m = maska_tekstu(tekst, 'Silkscreen-Regular.ttf', 8); w, h = m.size; px = m.load()
    out = Image.new('RGBA', (w + 2, h + 2), (0, 0, 0, 0))
    for y in range(-1, h + 1):
        for x in range(-1, w + 1):
            if any(0 <= x + dx < w and 0 <= y + dy < h and px[x + dx, y + dy] for dx in (-1, 0, 1) for dy in (-1, 0, 1)):
                out.putpixel((x + 1, y + 1), (0, 0, 0, 255))
    for y in range(h):
        for x in range(w):
            if px[x, y]: out.putpixel((x + 1, y + 1), (255, 255, 255, 255))
    return out

logo = napis_tytulowy('LAST DRAW', 'Rye-Regular.ttf')
logo.save(T + 'napis.png')
opcje = napis_maly('[1] 1 PLAYER     [2] 2 PLAYERS')
opcje.save(T + 'opcje.png')
print('ekran tytułowy: napis', logo.size, '-> pozycja', (576, 3 * 28 + 3 * logo.height // 2),
      '| opcje', opcje.size, '-> pozycja', (576, 3 * 192 + 3 * opcje.height // 2))
