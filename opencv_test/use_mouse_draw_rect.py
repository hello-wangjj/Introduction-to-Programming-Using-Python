import cv2
import numpy as np

__author__ = 'wangj'
__date__ = '2017/11/08 20:05'

drawing = False
ix, iy = -1, -1


def draw_rect(event, x, y, flags, param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        # cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
        place = str(ix) + ',' + str(iy)
        cv2.putText(img, place, (ix, iy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing:
            cv2.line(img, (ix, iy), (ix, y), (0, 255, 0), 3)
            cv2.line(img, (ix, iy), (x, iy), (0, 255, 0), 3)

    elif event == cv2.EVENT_LBUTTONUP:
        # cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 3)
        cv2.line(img, (ix, y), (x, y), (0, 255, 0), 3)
        cv2.line(img, (x, iy), (x, y), (0, 255, 0), 3)
        drawing = False


if __name__ == '__main__':
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_rect)

    while (1):
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF

        if k == ord('q'):
            break

    cv2.destroyAllWindows()
