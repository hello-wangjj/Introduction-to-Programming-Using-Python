import cv2
import numpy as np

__author__ = 'wangj'
__date__ = '2017/11/13 21:59'


def main():
    cap = cv2.VideoCapture(0)

    while (1):
        ret, frame = cap.read()

        # convert bgr to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define range of color
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])

        lower_green = np.array([50, 50, 50])
        upper_green = np.array([70, 255, 255])

        green_mask = cv2.inRange(hsv, lower_green, upper_green)
        blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        mask = green_mask + blue_mask

        # bit 操作
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
