import cv2
import numpy as np

__author__ = 'wangj'
__date__ = '2017/11/13 21:16'


def main():
    flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
    print(flags)


def find_blue():
    cap = cv2.VideoCapture(0)
    while (1):
        ret, frame = cap.read()
        if ret:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # def range of blue in hsv
            lower_blue = np.array([110, 50, 50])
            upper_blue = np.array([130, 255, 255])

            # Threshold the HSV image to get only blue colors
            mask = cv2.inRange(hsv, lower_blue, upper_blue)

            # bitwise_and
            res = cv2.bitwise_and(frame, frame, mask=mask)
            cv2.imshow('frame', frame)
            cv2.imshow('mask', mask)
            cv2.imshow('res', res)
            k = cv2.waitKey(5)
            if k == ord('q'):
                break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
    find_blue()