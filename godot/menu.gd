extends Node2D

func _ready():
	Music.fade_in()

func _process(_delta):
	# opcje migają: pół sekundy widać, pół sekundy nie
	$Options.visible = int(Time.get_ticks_msec() / 500.0) % 2 == 0

func _unhandled_input(event):
	if event is InputEventKey and event.pressed and not event.echo:
		if event.keycode == KEY_1 or event.keycode == KEY_KP_1:
			get_tree().change_scene_to_file("res://duel.tscn")
		elif event.keycode == KEY_2 or event.keycode == KEY_KP_2:
			get_tree().change_scene_to_file("res://duel_2p.tscn")
