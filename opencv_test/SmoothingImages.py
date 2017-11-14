import cv2
import numpy as np
from matplotlib import pyplot as plt

__author__ = 'wangj'
__date__ = '2017/11/15 00:38'


def main():
    img = cv2.imread('2.jpg')

    kernel = np.ones((5, 5), np.float32) / 25
    dst = cv2.filter2D(img, -1, kernel)

    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()


def avg_blur():
    img = cv2.imread('logo.jpg')

    blur = cv2.blur(img, (5, 5))

    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    main()
    avg_blur()
