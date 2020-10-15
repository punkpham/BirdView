import cv2
import numpy as np
image = cv2.imread("try1.jpg")
image = cv2.resize(image,(400,400))

#cv2.line(image, (20,20), (50,50), (0,0,255), (5))

pts = np.array([[100, 250], [120, 190], [280, 190],[300,250],[101,250]], np.int32)
pts1 = np.array([[80, 320], [99, 255], [301, 255],[320,320],[81,320]], np.int32)
pts2 = np.array([[60, 399], [79, 325], [321, 325],[340,399],[61,399]], np.int32)
# Creating a yellow polygon. Parameter "False" indicates
# that our line is not closed
def warningLine(img):
    cv2.polylines(image, [pts], True, (0,255,0), 2)
    cv2.polylines(image, [pts1], False, (0,242,255), 2)
    cv2.polylines(image, [pts2], False, (0,0,255), 2)
    return img

#find points
cv2.circle(image,(80,180),5,(0,0,255),-1)
cv2.circle(image,(320,180),5,(0,0,255),-1)
cv2.circle(image,(10,400),5,(0,0,255),-1)
cv2.circle(image,(390,400),5,(0,0,255),-1)

warningLine(image)
cv2.imshow("image",image)
def sketch1(img):#transform large to small
    IMAGE_H = img.shape[0]
    IMAGE_W = img.shape[1]
    #print(IMAGE_H)
    #print(IMAGE_W)
    src = np.float32([[80,180],[10,400], [390,400], [320,180]])
    dst = np.float32([[0, 0],[0, IMAGE_H-250], [IMAGE_W, IMAGE_H-250], [IMAGE_W, 0]])
    M = cv2.getPerspectiveTransform(src, dst) # The transformation matrix
    
    #img = img[50:IMAGE_H] # Apply np slicing for ROI crop
    warped_img = cv2.warpPerspective(img,M , (IMAGE_W, IMAGE_H)) # Image warping  
    return warped_img


def sketch2(img):#transform large to small
    IMAGE_H = img.shape[0]
    IMAGE_W = img.shape[1]
    print(IMAGE_H)
    print(IMAGE_W)
    src = np.float32([[0, 0],[0, IMAGE_H], [IMAGE_W, IMAGE_H], [IMAGE_W, 0]])
    dst = np.float32([[0, 0],[0, IMAGE_H], [IMAGE_W, IMAGE_H], [IMAGE_W, 0]])
    M = cv2.getPerspectiveTransform(src, dst) # The transformation matrix
    
    #img = img[50:IMAGE_H] # Apply np slicing for ROI crop
    warped_img = cv2.warpPerspective(img,M , (IMAGE_W, IMAGE_H)) # Image warping  
    return warped_img



image = sketch1(image)
cv2.imshow("image1",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
