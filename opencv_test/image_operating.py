import cv2
import numpy

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


if __name__ == '__main__':
    main()
    use_numpy()
    get_image_info()
    img_roi()
    split_img()
