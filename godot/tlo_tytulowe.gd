extends Node2D

# Ruchome tło ekranu tytułowego. Trzy warstwy jadą w lewo z różną prędkością:
# skały daleko wolno, kaktusy szybciej, domy najszybciej. Tak oko odczytuje głębię (paralaksa),
# jak za oknem pociągu. Każda warstwa to obrazek powtarzany w kółko, więc ulica nigdy się nie kończy.

const LAYERS = [
	["res://assets/tytul/daleko.png", 5.0],    # [obrazek, prędkość w pikselach obrazka na sekundę]
	["res://assets/tytul/srodek.png", 10.0],
	["res://assets/tytul/blisko.png", 20.0],
]

var layers = []
var speeds = []
var sun
var sun_time = 0.0

func _ready():
	for i in LAYERS.size():
		var sprite = Sprite2D.new()
		sprite.texture = load(LAYERS[i][0])
		sprite.centered = false
		sprite.scale = Vector2(3, 3)
		sprite.texture_repeat = CanvasItem.TEXTURE_REPEAT_ENABLED   # obrazek powtarza się w kółko
		sprite.region_enabled = true                                # pokazujemy tylko „okno” 384x216
		sprite.region_rect = Rect2(0, 0, 384, 216)
		add_child(sprite)
		layers.append(sprite)
		speeds.append(LAYERS[i][1])
		if i == 0:
			add_sun()    # słońce na niebie, przed domami

func add_sun():
	sun = Sprite2D.new()
	sun.texture = load("res://assets/yeehaw/yeehaw_env_sun_sprite.png")
	sun.hframes = 3
	sun.centered = false
	sun.scale = Vector2(3, 3)
	sun.position = Vector2(1038, 9)
	add_child(sun)

func _process(delta):
	for i in layers.size():
		layers[i].region_rect.position.x += speeds[i] * delta     # przesuwamy „okno” po obrazku
	sun_time += delta
	sun.frame = int(sun_time * 4) % 3                             # promienie migoczą
