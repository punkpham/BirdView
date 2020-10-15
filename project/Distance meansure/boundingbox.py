import cv2

img = cv2.imread('box.jpg')
img = cv2.resize(img,(500,500))
cv2.rectangle(img, (230,230), (250,280), (0,255,0), (2))
cv2.circle(img,(230,230),5,(0,0,255),-1)
cv2.circle(img,(250,280),5,(0,0,255),-1)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()