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

static var enemy_index = 0
static var lives = 2

var fire_time = 0
var state = "ready"

func _ready():
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
								win("%.3f s - You win!" % reaction)
				elif event.keycode == KEY_R and state == "done":
						if lives == 0 or enemy_index == ENEMY_TIMES.size():
								enemy_index = 0
								lives = 2
						get_tree().reload_current_scene()

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
		$Info.text = "%s (%d/5)    Lives: %d\n\"%s\"" % [ENEMY_NAMES[enemy_index], enemy_index + 1, lives, ENEMY_LINES[enemy_index]]

func end_round(text, loser):
		state = "done"
		$Message.text = text + "\n[R] continue"
		loser.hide()

func end_game(title, detail):
		state = "done"
		$Player.hide()
		$Enemy.hide()
		$Info.text = detail
		$Message.text = title + "\n[R] play again"
