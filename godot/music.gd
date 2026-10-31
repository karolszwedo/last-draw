extends AudioStreamPlayer

# Muzyka gra przez całą grę, także przy zmianie sceny (menu -> pojedynek -> menu).
# Dlatego to „autoload”: Godot tworzy ten węzeł raz, na starcie, i nie usuwa go przy zmianie sceny.
# Z każdego skryptu wołamy ją po nazwie: Music.fade_out() albo Music.fade_in().

const LOUD = -10.0     # normalna głośność (dB); co 1 dB w dół = ok. 10% ciszej, -6 dB = o połowę
const SILENT = -60.0   # praktycznie cisza

var fade_tween

func _ready():
	# Przy okazji: F12 = zrzut ekranu (tylko przy uruchamianiu z Godota, patrz zrzuty.gd).
	# Podpinamy go tutaj, bo Music i tak działa w całej grze, więc nie trzeba drugiego autoloadu.
	add_child(load("res://zrzuty.gd").new())
	stream = load("res://assets/muzyka/lassolady.ogg")
	stream.loop = true
	volume_db = LOUD
	play()

# Przed pojedynkiem: muzyka cichnie, zostaje wiatr.
func fade_out():
	fade_to(SILENT, 1.5, 0.0)

# Po strzale: chwila ciszy na echo, potem muzyka wraca.
func fade_in(delay = 0.0):
	fade_to(LOUD, 1.0, delay)

func fade_to(db, seconds, delay):
	if fade_tween:
		fade_tween.kill()    # przerywamy poprzednie ściszanie/podgłaśnianie, żeby się nie kłóciły
	fade_tween = create_tween()
	fade_tween.tween_interval(delay)
	fade_tween.tween_property(self, "volume_db", db, seconds)
