import numpy as np 

def calculateHomography(src, dst):
    A = []
    i = 0
    for i in range (len(src)):
        x1 = src[i][0]
        y1 = src[i][1]
        x2 = dst[i][0]
        y2 = dst[i][1]
        row1 = np.array([-x1, -y1, -1, 0, 0, 0, x1 * x2, y1 * x2, x2])
        row2 = np.array([0, 0, 0, -x1, -y1, -1, x1 * y2, y1 * y2, y2])
        A.append(row1)
        A.append(row2)
    u,s,v = np.linalg.svd(A)
    h = v[8]
    h = np.array(h)
    h = h.reshape((3,3))
    return h