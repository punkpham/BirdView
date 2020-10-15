import numpy as np
import cv2
from homography import calculateHomography as homography
from warp import warp_inv as warp

img = cv2.imread('left.jpg')
img2 = cv2.imread('right.jpg')

img1Clicks = []
img2Clicks = []


def click(event, x, y, flags, param):
    if event == 1:
        param.append(np.array([y, x]))


cv2.namedWindow('image')
cv2.setMouseCallback('image', click, img1Clicks)
cv2.namedWindow('image2')
cv2.setMouseCallback('image2', click, img2Clicks)

# Get correspondences from mouse clicks
while(1):
    cv2.imshow('image', img)
    cv2.imshow('image2', img2)
    k = cv2.waitKey(1)
    if k > 0:
        break

H = homography(img2Clicks, img1Clicks)
imOut = warp(img2, H)

imOut[0:img.shape[0], 0:img.shape[1]] = img
while (1):
    cv2.imshow('output', imOut)
    k = cv2.waitKey(1) & 0XFF
    if k > 0:
        break


cv2.waitKey(0)
cv2.destroyAllWindows()