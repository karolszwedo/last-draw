extends Node

# F12 = zrzut ekranu gry (do strony na itch.io i README).
# Działa tylko przy uruchamianiu z Godota (OS.has_feature("editor")); w wersji na itch.io nic nie robi.
# Podpięty w music.gd (Music działa w każdej scenie). Obrazki trafiają do materialy/zrzuty/ obok projektu.

func _input(event):
	if not OS.has_feature("editor"):
		return
	if event is InputEventKey and event.pressed and not event.echo and event.keycode == KEY_F12:
		var folder = ProjectSettings.globalize_path("res://").path_join("../materialy/zrzuty")
		DirAccess.make_dir_recursive_absolute(folder)
		var image = get_viewport().get_texture().get_image()
		var file_name = "zrzut_%s.png" % Time.get_datetime_string_from_system().replace(":", "-")
		image.save_png(folder.path_join(file_name))
		print("Zrzut zapisany: ", file_name, " (", image.get_width(), "x", image.get_height(), ")")
