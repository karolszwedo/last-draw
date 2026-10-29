extends Node2D

var fire_time = 0
var state = "ready"
var left_pressed = false
var right_pressed = false

func _ready():
	$Info.text = "Left: A    Right: L"
	$Message.text = "Ready..."
	await get_tree().create_timer(randf_range(2.0, 6.0)).timeout
	if state == "ready":
		state = "fire"
		$Message.text = "FIRE!"
		fire_time = Time.get_ticks_msec()

func _unhandled_input(event):
	if event is InputEventKey and event.pressed and not event.echo:
		if event.keycode == KEY_A:
			left_pressed = true
		elif event.keycode == KEY_L:
			right_pressed = true
		elif event.keycode == KEY_R and state == "done":
			get_tree().reload_current_scene()

func _process(_delta):
	if state == "ready":
		if left_pressed and right_pressed:
			end_round("Both too early!", null)
		elif left_pressed:
			end_round("Left too early - Right wins!", $Left)
		elif right_pressed:
			end_round("Right too early - Left wins!", $Right)
	elif state == "fire":
		var reaction = (Time.get_ticks_msec() - fire_time) / 1000.0
		if left_pressed and right_pressed:
			end_round("Draw!", null)
		elif left_pressed:
			end_round("%.3f s - Left wins!" % reaction, $Right)
		elif right_pressed:
			end_round("%.3f s - Right wins!" % reaction, $Left)
	left_pressed = false
	right_pressed = false

func end_round(text, loser):
	state = "done"
	$Message.text = text + "\n[R] next round"
	if loser != null:
		loser.hide()
