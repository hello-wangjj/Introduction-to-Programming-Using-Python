import cv2
import numpy as np
from matplotlib import pyplot as plt

__author__ = 'wangj'
__date__ = '2017/10/20 23:47'


def main():
    img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image', img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('test_gray.png', img)
        cv2.destroyAllWindows()
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    # plt.xticks([]),plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()


if __name__ == '__main__':
    main()
