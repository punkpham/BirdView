import cv2
import time

img = cv2.imread("box.jpg")
img = cv2.resize(img,(400,400))

x = 450
axesx = 40
axesy = 40
cv2.ellipse(img, (400,x),(80,80),200,50,90, (0,0,255),(2))
#cv2.ellipse(img, (100,x),(80,80),200,50,90, (0,0,0),(2))

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()