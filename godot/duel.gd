extends Node2D

func _ready():
		$Message.text = "Ready..."
		await get_tree().create_timer(randf_range(2.0, 5.0)).timeout
		$Message.text = "FIRE!"
