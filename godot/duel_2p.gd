extends Node2D

const WINS_NEEDED = 3

static var left_score = 0
static var right_score = 0

var fire_time = 0
var state = "ready"
var left_pressed = false
var right_pressed = false

func _ready():
	show_score()
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
			if match_over():
				left_score = 0
				right_score = 0
			get_tree().reload_current_scene()
		elif event.keycode == KEY_ESCAPE:
			left_score = 0
			right_score = 0
			get_tree().change_scene_to_file("res://menu.tscn")

func _process(_delta):
	if state == "ready":
		if left_pressed and right_pressed:
			end_round("Both too early!", "")
		elif left_pressed:
			end_round("Left too early - Right wins!", "right")
		elif right_pressed:
			end_round("Right too early - Left wins!", "left")
	elif state == "fire":
		var reaction = (Time.get_ticks_msec() - fire_time) / 1000.0
		if left_pressed and right_pressed:
			end_round("Draw!", "")
		elif left_pressed:
			end_round("%.3f s - Left wins!" % reaction, "left")
		elif right_pressed:
			end_round("%.3f s - Right wins!" % reaction, "right")
	left_pressed = false
	right_pressed = false

func end_round(text, winner):
	state = "done"
	if winner == "left":
		left_score += 1
		$Right.hide()
	elif winner == "right":
		right_score += 1
		$Left.hide()
	show_score()
	if match_over():
		$Message.text = text + "\n%s WINS THE MATCH!\n[R] new match    [Esc] menu" % winner.to_upper()
	else:
		$Message.text = text + "\n[R] next round"

func match_over():
	return left_score == WINS_NEEDED or right_score == WINS_NEEDED

func show_score():
	$Info.text = "Left (A): %d    Right (L): %d    First to %d" % [left_score, right_score, WINS_NEEDED]
