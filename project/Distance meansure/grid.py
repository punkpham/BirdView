
import numpy as np
import cv2 

image = cv2.imread("car.jpg")
image = cv2.resize(image,(600,600))
(H,W) = image.shape[:2]
def drawBasicGrid(img, pxstep):
    x = pxstep
    y = pxstep
    #Draw all x lines
    while x < img.shape[1]:
        cv2.line(img, (x, 0), (x, img.shape[0]), color=(0, 0, 255), thickness=1)
        x += pxstep
    
    while y < img.shape[0]:
        cv2.line(img, (0, y), (img.shape[1], y), color=(0, 0, 255),thickness=1)
        y += pxstep
     
        

def drawCenterLine(img,H,W):
    midY = H//2
    midX = W//2
    print("Middle Y pixel", midY)
    #Draw center line
    cv2.line(img, (0, midY), (W, midY), (0,255,0), thickness=2)
    cv2.line(img, (midX, 0), (midX, H), (0,255,0), thickness=2)
    

    
    


drawBasicGrid(image,3)

cv2.imshow("image",image)    
cv2.waitKey(0)
cv2.destroyAllWindows()