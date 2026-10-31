extends Node2D

const ENEMY_TIMES = [0.60, 0.48, 0.38, 0.30, 0.24]
const ENEMY_NAMES = ["Slow Joe", "Dusty Pete", "Rattlesnake Rosa", "Deacon Graves", "The Undertaker"]
const ENEMY_LINES = [
	"Drunk since noon. Still dangerous.",
	"Never lost a duel. Never fought one either.",
	"Bites before you see her move.",
	"Reads your last rites while you draw.",
	"Already measured you for a coffin.",
]
const RECORD_PATH = "user://record.txt"

static var enemy_index = 0
static var lives = 2

var fire_time = 0
var state = "ready"
var best = 0.0

func _ready():
	for label in [$Message, $Info]:
		label.add_theme_constant_override("outline_size", 10)
		label.add_theme_color_override("font_outline_color", Color.BLACK)
	load_best()
	show_info()
	$Message.text = "Ready..."
	await get_tree().create_timer(randf_range(2.0, 6.0)).timeout
	if state == "ready":
		state = "fire"
		$Message.text = "FIRE!"
		fire_time = Time.get_ticks_msec()
		var base = ENEMY_TIMES[enemy_index]
		var enemy_time = randf_range(base - 0.03, base + 0.03)
		await get_tree().create_timer(enemy_time).timeout
		if state == "fire":
			lose("%.3f s - You lose" % enemy_time)

func _unhandled_input(event):
	if event is InputEventKey and event.pressed:
		if event.keycode == KEY_SPACE:
			if state == "ready":
				lose("Too early!")
			elif state == "fire":
				var reaction = (Time.get_ticks_msec() - fire_time) / 1000.0
				var text = "%.3f s - You win!" % reaction
				if best == 0.0 or reaction < best:
					best = reaction
					save_best()
					text += "\nNew record!"
				win(text)
		elif event.keycode == KEY_R and state == "done":
			if lives == 0 or enemy_index == ENEMY_TIMES.size():
				enemy_index = 0
				lives = 2
			get_tree().reload_current_scene()
		elif event.keycode == KEY_ESCAPE:
			enemy_index = 0
			lives = 2
			get_tree().change_scene_to_file("res://menu.tscn")

func win(text):
	enemy_index += 1
	if enemy_index == ENEMY_TIMES.size():
		end_game("YOU WIN!", "The Undertaker is dead. The town is yours.")
	else:
		end_round(text, $Enemy)

func lose(text):
	lives -= 1
	if lives == 0:
		end_game("GAME OVER", "Lost to %s (%d/5)" % [ENEMY_NAMES[enemy_index], enemy_index + 1])
	else:
		show_info()
		end_round(text, $Player)

func show_info():
	$Info.text = "%s (%d/5)    Lives: %d    %s\n\"%s\"" % [ENEMY_NAMES[enemy_index], enemy_index + 1, lives, best_text(), ENEMY_LINES[enemy_index]]

func end_round(text, loser):
	state = "done"
	$Message.text = text + "\n[R] continue"
	loser.hide()

func end_game(title, detail):
	state = "done"
	$Player.hide()
	$Enemy.hide()
	$Info.text = detail + "\n" + best_text()
	$Message.text = title + "\n[R] play again\n[Esc] menu"

func best_text():
	if best == 0.0:
		return "Best: -"
	return "Best: %.3f s" % best

func load_best():
	if FileAccess.file_exists(RECORD_PATH):
		var file = FileAccess.open(RECORD_PATH, FileAccess.READ)
		best = file.get_as_text().to_float()

func save_best():
	var file = FileAccess.open(RECORD_PATH, FileAccess.WRITE)
	file.store_string(str(best))
