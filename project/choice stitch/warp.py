import numpy as np


def warp_inv(im, H):
    imOut = np.zeros((im.shape[0], 2 * im.shape[1],
                      im.shape[2])).astype(im.dtype)
    for i in range(0, im.shape[0]):
        for j in range(0, im.shape[1]):
            dest_pt = np.array([i, j, 1])
            src_pt = np.dot(np.linalg.inv(H), dest_pt)
            src_pt /= src_pt[2]  # Convert to heterogeneous coordinates
            src_i = int(src_pt[0])
            src_j = int(src_pt[1])
            try:  # if src_i and src_j are within im boundaries
                imOut[i][j] = im[src_i][src_j]
            except:
                None
    return imOut

