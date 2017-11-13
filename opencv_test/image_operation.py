import cv2
import numpy as np

__author__ = 'wangj'
__date__ = '2017/11/12 19:34'


def main():
    x = np.uint8([250])
    y = np.uint8([20])
    print('cv2: x+y=', cv2.add(x, y))
    print('x+y=', x + y)


def img_blending():
    img1 = cv2.imread('1.jpg')
    img2 = cv2.imread('3.jpg')
    dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def bitwise_op():
    img1 = cv2.imread('1.jpg')
    img2 = cv2.imread('2.jpg')
    # I want to put logo on top-left corner, So I create a ROI
    rows, cols, channels = img2.shape
    roi = img1[0:rows, 0:cols]

    # Now create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # cv2.imshow('mask_inv', mask_inv)
    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
    cv2.imshow('img1_bg', img1_bg)
    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
    cv2.imshow('img2_fg', img2_fg)
    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg, img2_fg)
    img1[0:rows, 0:cols] = dst
    cv2.imshow('res', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
    img_blending()
    bitwise_op()
