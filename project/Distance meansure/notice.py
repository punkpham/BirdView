import cv2
import time

img = cv2.imread("box.jpg")
imgcopy = img.copy()
img = cv2.resize(img,(400,400))
imgcopy = cv2.resize(imgcopy,(400,400))
x = 450
axesx = 40
axesy = 40
count = 4
counttime = 400
cap = cv2.VideoCapture(0)

while count >= 0:    
    ret, frame = cap.read()
    frame = cv2.resize(frame,(400,400))
    if x == 450 and counttime > 0:
        cv2.ellipse(frame, (100,x),(axesx,axesy),200,50,90, (0,0,255), (7))
        counttime -= 1
    cv2.imshow("img", frame)
    
    time.sleep(1/120)
   
    axesx +=20
    axesy +=20
    if count == 0:
        count = 4
        axesx = 40
        axesy = 40
        #img = imgcopy
    count -= 1
    k = cv2.waitKey(10)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()