extends Node2D

var fire_time = 0
var state = "ready"

func _ready():
		$Message.text = "Ready..."
		await get_tree().create_timer(randf_range(2.0, 6.0)).timeout
		if state == "ready":
				state = "fire"
				$Message.text = "FIRE!"
				fire_time = Time.get_ticks_msec()
				var enemy_time = randf_range(0.55, 0.65)
				await get_tree().create_timer(enemy_time).timeout
				if state == "fire":
						state = "done"
						$Message.text = "%.3f s - You lose" % enemy_time
						$Player.hide()

func _unhandled_input(event):
		if event is InputEventKey and event.pressed and event.keycode == KEY_SPACE:
				if state == "ready":
						state = "done"
						$Message.text = "Too early! You lose"
						$Player.hide()
				elif state == "fire":
						state = "done"
						var reaction = (Time.get_ticks_msec() - fire_time) / 1000.0
						$Message.text = "%.3f s - You win!" % reaction
						$Enemy.hide()
