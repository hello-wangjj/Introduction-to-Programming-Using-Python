import cv2
import numpy as np
from matplotlib import pyplot as plt
__author__ = 'wangj'
__date__ = '2017/11/15 01:15'


def main():
    img = cv2.imread('mor.png', 0)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(img, kernel, iterations=1)
    cv2.imshow('ero',erosion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()