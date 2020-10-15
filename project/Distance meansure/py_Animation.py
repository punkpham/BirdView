import cv2 as cv

move_rectangle = False
BLUE = [255,0,0]

fg = cv.imread('box.jpg')
bg = cv.imread('box1.jpg')
bgCopy = bg.copy()

def mouse(event,x,y,flags,params):
    global move_rectangle, BLUE, fg, bg, bgCopy
    #draw rectangle where x,y is rectangle center
    if event == cv.EVENT_LBUTTONDOWN:
        move_rectangle = True

    elif event == cv.EVENT_MOUSEMOVE:
        bg = bgCopy.copy() #!! your image is reinitialized with initial one
        if move_rectangle:
            cv.rectangle(bg,(x-int(0.5*cols),y-int(0.5*rows)),
            (x+int(0.5*cols),y+int(0.5*rows)),BLUE, -1)

    elif event == cv.EVENT_LBUTTONUP:
        move_rectangle = False
        cv.rectangle(bg,(x-int(0.5*cols),y-int(0.5*rows)),
        (x+int(0.5*cols),y+int(0.5*rows)),BLUE, -1)

if __name__ == '__main__':
    rows, cols = fg.shape[:2]

    cv.namedWindow('draw')
    cv.setMouseCallback('draw', mouse)

    while True:

        cv.imshow('draw', bg)
        k = cv.waitKey(1)

        #waiting for esc to exit
        if k == 27 & 0xFF:
            break

    cv.destroyAllWindows()