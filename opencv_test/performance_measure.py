import cv2
import numpy as np
import time

__author__ = 'wangj'
__date__ = '2017/11/13 19:41'


def main():
    img1 = cv2.imread('1.jpg')
    e1 = cv2.getTickCount()
    t1 = time.time()
    for i in range(5, 49, 2):
        img1 = cv2.medianBlur(img1, i)
    # your code execution
    e2 = cv2.getTickCount()
    t2 = time.time()
    diff_e = (e2 - e1) / cv2.getTickFrequency()
    print(diff_e)
    print(t2 - t1)


if __name__ == '__main__':
    main()
