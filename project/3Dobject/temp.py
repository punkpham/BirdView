import pyglet
from pyglet.window import key
import ratcave as rc

# Create Window and Add Keyboard State Handler to it's Event Loop
window = pyglet.window.Window()
keys = key.KeyStateHandler()
window.push_handlers(keys)

# Insert filename into WavefrontReader.
obj_filename = "3D.obj"
obj_reader = rc.WavefrontReader(obj_filename)

# Create Mesh
Object = obj_reader.get_mesh("3D.obj", position=(0, -0.4, -3), scale= .6)

#create camera
        

# Create Scene
scene = rc.Scene(meshes=[Object])


# Functions to Run in Event Loop
def rotate_meshes(dt):
    Object.rotation.y += 0 * dt  # dt is the time between frames
    
pyglet.clock.schedule(rotate_meshes)


def move_camera(dt):
    #camera_speed = 3
    if keys[key.LEFT]:
        #scene.camera.position.y -= camera_speed * dt
        Object.rotation.y -= 17 * dt
    if keys[key.RIGHT]:
        #scene.camera.position.y += camera_speed * dt
        Object.rotation.y += 17 * dt
pyglet.clock.schedule(move_camera)

image = pyglet.image.load("Capture.PNG")
sprite = pyglet.sprite.Sprite(img=image, x = 0, y = 0)

@window.event     
def on_draw():  
    window.clear() 
    sprite.draw()
    with rc.default_shader:
    # clear the window  
        window.clear()  
        scene.draw()    
    
pyglet.app.run()
