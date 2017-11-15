import cv2
import numpy as np

__author__ = 'wangj'
__date__ = '2017/11/15 20:53'
"""
Image Pyramids 图像金字塔
"""


def sameSize(img1, img2):
    """
    使得img1的大小与img2相同
    """
    rows, cols, dpt = img2.shape
    dst = img1[:rows, :cols]
    return dst


def main():
    A = cv2.imread('1.jpg')
    B = cv2.imread('3.jpg')

    # generate Gaussian pyramid for A
    G = A.copy()
    gpA = [G]
    for i in range(6):
        G = cv2.pyrDown(G)
        gpA.append(G)

    # generate Gaussian pyramid for B
    G = B.copy()
    gpB = [G]
    for i in range(6):
        G = cv2.pyrDown(G)
        gpB.append(G)

    # generate Laplacian Pyramid for A
    lpA = [gpA[5]]
    for i in range(5, 0, -1):
        GE = cv2.pyrUp(gpA[i])
        L = cv2.subtract(gpA[i - 1], sameSize(GE, gpA[i-1]))
        lpA.append(L)

    # generate Laplacian Pyramid for B
    lpB = [gpB[5]]
    for i in range(5, 0, -1):
        GE = cv2.pyrUp(gpB[i])
        L = cv2.subtract(gpB[i - 1], sameSize(GE, gpB[i-1]))
        lpB.append(L)

    # Now add left and right halves of images in each level
    LS = []
    for la, lb in zip(lpA, lpB):
        rows, cols, dpt = la.shape
        ls = np.hstack((la[:, 0:cols // 2], lb[:, cols // 2:]))
        LS.append(ls)

    # now reconstruct
    ls_ = LS[0]
    for i in range(1, 6):
        ls_ = cv2.pyrUp(ls_)
        ls_ = cv2.add(sameSize(ls_, LS[i]), LS[i])

    # image with direct connecting each half
    real = np.hstack((A[:, :cols // 2], B[:, cols // 2:]))

    cv2.imwrite('7.jpg', ls_)
    cv2.imwrite('8.jpg', real)


if __name__ == '__main__':
    main()
