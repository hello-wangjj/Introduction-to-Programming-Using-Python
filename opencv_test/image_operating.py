import cv2
import numpy as np
import matplotlib.pyplot as plt

__author__ = 'wangj'
__date__ = '2017/11/02 21:03'


def main():
    img = cv2.imread('1.jpg')
    px = img[10, 10]
    print(px)
    blue = img[100, 100, 2]
    print(blue)
    img[101, 101] = [255, 255, 255]
    print(img[101, 101])


def use_numpy():
    img = cv2.imread('1.jpg')
    print(img.item(10, 10, 2))
    img.itemset((10, 10, 2), 100)
    print(img.item(10, 10, 2))


def get_image_info():
    img = cv2.imread('1.jpg')
    print(img.shape)
    print(img.size)
    print(img.dtype)


def img_roi():
    img = cv2.imread('1.jpg')
    roi = img[100:201, 100:201]
    img[100:201, 500:601] = roi
    cv2.namedWindow('image')
    cv2.imshow('image', img)
    k = cv2.waitKey(0)
    if k == ord('q'):  # 按q键退出
        cv2.destroyAllWindows()


def img_split_merge():
    img = cv2.imread('1.jpg')
    b, g, r = cv2.split(img)
    img2 = cv2.merge([r, g, b])
    plt.subplot(121)
    plt.imshow(img)
    plt.subplot(122)
    plt.imshow(img2)
    plt.show()
    cv2.imshow('bgr image', img)  # expects true color
    cv2.imshow('rgb image', img2)  # expects distorted color
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def border():
    BLUE = [0, 0, 255]

    img1 = cv2.imread('2.jpg')

    replicate = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_WRAP)
    constant = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=BLUE)

    plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
    plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
    plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
    plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
    plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
    plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

    plt.show()


if __name__ == '__main__':
    main()
    use_numpy()
    get_image_info()
    img_roi()
    img_split_merge()
    border()
