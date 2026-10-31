extends Node2D

const WINS_NEEDED = 3

static var left_score = 0
static var right_score = 0

var fire_time = 0
var state = "ready"
var left_pressed = false
var right_pressed = false

func _ready():
	for label in [$Message, $Info]:
		label.add_theme_constant_override("outline_size", 10)
		label.add_theme_color_override("font_outline_color", Color.BLACK)
	Music.fade_out()
	show_score()
	$Message.text = "Ready..."
	await get_tree().create_timer(randf_range(2.0, 6.0)).timeout
	if state == "ready":
		state = "fire"
		$Message.text = "FIRE!"
		$Bell.play()
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
	music_back()
	if winner == "left":
		left_score += 1
		shoot($Left, $Right)
	elif winner == "right":
		right_score += 1
		shoot($Right, $Left)
	show_score()
	if match_over():
		$Message.text = text + "\n%s WINS THE MATCH!\n[R] new match    [Esc] menu" % winner.to_upper()
	else:
		$Message.text = text + "\n[R] next round"

# Klatki w kowboj.png: 0 = stoi, 1-4 = strzela, 5-8 = pada, 9-15 = rośnie kałuża.
func shoot(winner, loser):
	$Shot.play()
	var tween = create_tween()
	tween.tween_property(winner, "frame", 4, 0.25).from(1)
	tween.tween_property(loser, "frame", 8, 0.4).from(5)
	tween.tween_property(loser, "frame", 15, 1.5).from(9)

# Po strzale: 1,5 s ciszy na echo, potem muzyka wraca, a wiatr cichnie.
func music_back():
	Music.fade_in(1.5)
	var tween = create_tween()
	tween.tween_interval(1.5)
	tween.tween_property($Wind, "volume_db", -60.0, 1.0)

func match_over():
	return left_score == WINS_NEEDED or right_score == WINS_NEEDED

func show_score():
	$Info.text = "Left (A): %d    Right (L): %d    First to %d" % [left_score, right_score, WINS_NEEDED]
