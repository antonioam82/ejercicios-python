#from pyglet.window import key
import pyglet

    
animation = pyglet.image.load_animation('walk.gif')
bin = pyglet.image.atlas.TextureBin()
animation.add_to_texture_bin(bin)
sprite = pyglet.sprite.Sprite(animation)

w = sprite.width
h = sprite.height

window = pyglet.window.Window(width=w, height=h)

@window.event
def on_draw():
    sprite.draw()


pyglet.app.run()
