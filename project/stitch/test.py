import cv2
def resize(img):
    IMAGE_H = 680
    IMAGE_W = 600
    dim = (IMAGE_W, IMAGE_H)
    resized = cv2.resize(img, dim)
    return resized

img = cv2.imread("left1.png")
img1 = cv2.imread("right1.png")

img = resize(img)
img1 = resize(img1)

img = cv2.bitwise_or(img,img1)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()