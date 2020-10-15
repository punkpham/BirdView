import pyglet
import ratcave as rc
from pyglet.gl import gl
from pyglet.window import key
import cv2
from PIL import Image

window = pyglet.window.Window(resizable=True, width=600, height=600)
keys = key.KeyStateHandler()
window.push_handlers(keys)


image = cv2.imread("try1.jpg")
image = cv2.resize(image,(600,600))

def cv2glet(img,format):
    '''Assumes image is in BGR color space. Returns a pyimg object'''
    if format == 'GRAY':
      rows, cols = img.shape
      channels = 1
    else:
      rows, cols, channels = img.shape

    raw_img = Image.fromarray(img).tobytes()

    top_to_bottom_flag = -1
    bytes_per_row = channels*cols
    pyimg = pyglet.image.ImageData(width=cols, 
                                   height=rows, 
                                   format="BRG", 
                                   data=raw_img, 
                                   pitch=top_to_bottom_flag*bytes_per_row)
    return pyimg

# get an object
model_file = rc.resources.obj_primitives
monkey = rc.WavefrontReader(model_file).get_mesh('Monkey')
monkey.position.xyz = 0, 0, -5

#get an object file
obj_filename = "3D.obj"
obj_reader = rc.WavefrontReader(obj_filename)
Object = obj_reader.get_mesh("3D.obj", position=(0, -1, -4), scale= .6)

image= cv2glet(image,format)



sprite = pyglet.sprite.Sprite(image, x = 0, y = 0)
camera = rc.StereoCameraGroup()

print(type(sprite))


print(image)
@window.event
def on_draw():
    gl.glColorMask(True, True, True, True)
    window.clear()
    sprite.draw()
    with rc.default_shader, rc.default_states:
        with camera.right:
            gl.glColorMask(False, True, True, True)
            Object.draw()

        gl.glClear(gl.GL_DEPTH_BUFFER_BIT)

        with camera.left:
            gl.glColorMask(True, False, False, True)
            Object.draw()

#t = 0
def updateImage(dt):
    if keys[key.LEFT]:
        sprite.x -= 100 * dt
    elif keys[key.RIGHT]:
        sprite.x += 100 * dt

#rotate 3D
def update3D(dt):
    if keys[key.RIGHT]:
        
        Object.rotation.y -= 10 * dt
        
    elif keys[key.LEFT]:
        
        Object.rotation.y += 10 * dt
        
    
    for cam in camera.cameras:
        cam.uniforms['projection_matrix'] = cam.projection_matrix

pyglet.clock.schedule(update3D)
pyglet.clock.schedule(updateImage)

pyglet.app.run()