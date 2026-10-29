extends Node2D

var fire_time = 0

func _ready():
		$Message.text = "Ready..."
		await get_tree().create_timer(randf_range(2.0, 5.0)).timeout
		$Message.text = "FIRE!"
		fire_time = Time.get_ticks_msec()

func _unhandled_input(event):
		if event is InputEventKey and event.pressed and event.keycode == KEY_SPACE:
				if fire_time > 0:
						var reaction = Time.get_ticks_msec() - fire_time
						$Message.text = str(reaction) + " ms"
						fire_time = 0
