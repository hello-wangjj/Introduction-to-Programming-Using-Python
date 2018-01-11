import cv2
import numpy as np

__author__ = 'wangj'
__date__ = '2017/11/15 20:01'

lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3


def CannyThreshold(lowThreshold):
    detected_edgs = cv2.GaussianBlur(img_gray, (3, 3), 0)
    detected_edgs = cv2.Canny(detected_edgs, lowThreshold, lowThreshold * ratio, apertureSize=kernel_size)
    dst = cv2.bitwise_and(img, img, mask=detected_edgs)
    cv2.imshow('canny', dst)


if __name__ == '__main__':
    img = cv2.imread('images/1.jpg')
    if not img.data:
        print('false')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('canny')
    cv2.createTrackbar('canny 参数：', 'canny', lowThreshold, max_lowThreshold, CannyThreshold)
    CannyThreshold(0)  # initialization
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()
