extends Sprite2D

# Krzak toczy się przez ulicę od lewej do prawej i podskakuje na nierównościach.
# Skrypt jest przypięty do samego krzaka, więc działa w każdej scenie, do której go wstawimy.

const SPEED = 180.0     # piksele na sekundę (więcej = szybciej)
const HOP = 9.0         # wysokość podskoku w pikselach
const ROLL = 17.5       # ile pikseli drogi na jedną klatkę obrotu (obwód krzaka / 8 klatek)
const START_X = -40.0   # zaczyna tuż za lewą krawędzią ekranu

var ground_y

func _ready():
	ground_y = position.y
	position.x = START_X

func _process(delta):
	position.x += SPEED * delta
	var distance = position.x - START_X
	frame = int(distance / ROLL) % 8                          # obraca się tak, jak daleko zajechał
	position.y = ground_y - abs(sin(distance / 60.0)) * HOP   # podskoki
	if position.x > 1200:
		queue_free()                                          # wyjechał za ekran: sprzątamy
