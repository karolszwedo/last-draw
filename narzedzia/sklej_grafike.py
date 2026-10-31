# Przepis na grafikę Last Draw: skleja tło ulicy i arkusz kowboja z pobranych paczek.
# Uruchomienie (z folderu 01-last-draw):  python -P narzedzia/sklej_grafike.py
# Wynik: godot/assets/tlo_ulica.png (384x216) i godot/assets/kowboj.png (16 klatek 64x64).
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

stopy = wszystkie[0].getbbox()[3]
print('kowboj: dół postaci w klatce y =', stopy, '-> pozycja y w grze =', 3 * G + 3 - 3 * (stopy - 32))
