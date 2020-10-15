import cv2

image = cv2.imread("box.jpg")

image = cv2.resize(image,(600,600))

x = 30 
cv2.line(image, (x, 0), (x, image.shape[0]), color=(0, 0, 255), thickness=1)



cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()