import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.3, 0.59, 0.11])

img = mpimg.imread('./images/input.jpg')
plt.imshow(img)
plt.show()
gray = rgb2gray(img)

plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.show()
