import cv2
import numpy as np

__author__ = 'wangj'
__date__ = '2017/11/08 21:41'


def nothing(pos):
    pass


def draw_circle(event, x, y, flags, param):
    # global r, g, b, s, radius
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(r, g, b, s, radius)
        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]
        cv2.circle(img, (x, y), radius, (r, g, b), -1)


if __name__ == '__main__':

    img = np.zeros((300, 512, 3), np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)
    cv2.createTrackbar('R', 'image', 0, 255, nothing)
    cv2.createTrackbar('G', 'image', 0, 255, nothing)
    cv2.createTrackbar('B', 'image', 0, 255, nothing)

    switch = '0:OFF\n1:ON'
    cv2.createTrackbar(switch, 'image', 0, 1, nothing)
    cv2.createTrackbar('radius', 'image', 0, 10, nothing)

    while (1):
        cv2.imshow('image', img)
        r = cv2.getTrackbarPos('R', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')
        s = cv2.getTrackbarPos(switch, 'image')
        radius = cv2.getTrackbarPos('radius', 'image')

        # if s == 0:
        #     img[:] = 0
        # else:
        #     img[:] = 255
        k = cv2.waitKey(1)
        if k == ord('q'):  # 按q键退出
            break

    cv2.destroyAllWindows()
