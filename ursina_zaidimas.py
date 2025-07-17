from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.orange, scale_y=2)
camera.position = (0, 10, -30)
camera.rotation_x = 30

def update():
    player.x += held_keys['d'] * 0.1
    player.x -= held_keys['a'] * 0.1

app.run()
