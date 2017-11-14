import cv2
import numpy as np
from matplotlib import pyplot as plt

__author__ = 'wangj'
__date__ = '2017/11/14 00:15'


def main():
    img = cv2.imread('2.jpg')

    res1 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # OR

    height, width = img.shape[:2]
    res2 = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('res1', res1)
    cv2.imshow('res2', res2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def trans():
    img = cv2.imread('2.jpg', 0)
    rows, cols = img.shape

    M = np.float32([[1, 0, 100], [0, 1, 50]])
    dst = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow('img', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def rotate():
    img = cv2.imread('2.jpg')
    rows, cols = img.shape[:2]

    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('img', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def affine_trans():
    img = cv2.imread('1.jpg')
    rows, cols, ch = img.shape

    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    M = cv2.getAffineTransform(pts1, pts2)

    dst = cv2.warpAffine(img, M, (cols, rows))

    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Output')
    plt.show()


def per_trans():
    img = cv2.imread('2.jpg')
    rows, cols, ch = img.shape

    pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

    M = cv2.getPerspectiveTransform(pts1, pts2)
    # InputArray
    # src：输入的图像
    # OutputArray
    # dst：输出的图像
    # InputArray
    # M：透视变换的矩阵
    # Size
    # dsize：输出图像的大小
    # int
    # flags = INTER_LINEAR：输出图像的插值方法
    dst = cv2.warpPerspective(img, M, (300, 300))

    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Output')
    plt.show()


if __name__ == '__main__':
    main()
    trans()
    rotate()
    affine_trans()
    per_trans()
