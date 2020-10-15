import pyglet
import cv2
from PIL import Image
import numpy as np
from pyglet.window import key


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



imagee = cv2glet(image,format)

window = pyglet.window.Window(resizable=True, width=600, height=600)
keys = key.KeyStateHandler()
window.push_handlers(keys)


sprite = pyglet.sprite.Sprite(imagee, x = 300, y = 0)
@window.event     
def on_draw():  
    window.clear() 
    sprite.draw()
    


def updateImage(dt):
    if keys[key.LEFT]:
        sprite.x -= 100 * dt
    elif keys[key.RIGHT]:
        sprite.x += 100 * dt
        
pyglet.clock.schedule(updateImage)

pyglet.app.run()