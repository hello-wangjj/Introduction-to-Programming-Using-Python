import cv2
import numpy as np

__author__ = 'wangj'
__date__ = '2017/10/23 22:40'


def main():
    # 0为默认计算机默认摄像头，1可以更换来源；
    cap = cv2.VideoCapture(0)
    cap.set(3, 320)
    cap.set(4, 240)
    while True:
        # capture frame-by-frame
        ret, frame = cap.read()
        # our operation on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # when everything done , release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
