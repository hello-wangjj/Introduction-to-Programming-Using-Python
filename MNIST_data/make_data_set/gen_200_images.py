import os
import numpy as np
from PIL import Image
from tensorflow.examples.tutorials.mnist import input_data

__author__ = 'wangj'
__date__ = '2018/05/04 00:22'


def main():
    pass


def gen_images(arr, index, label):
    # 直接保存 arr，是黑底图片，1.0 - arr 是白底图片
    matrix = (np.reshape(1.0-arr, (28, 28))*255).astype(np.uint8)
    img = Image.fromarray(matrix, 'L')
    # 存储图片时，label_index的格式，方便在制作数据集时，从文件名即可知道label
    img.save("./images/{}_{}.png".format(label, index))


if __name__ == '__main__':
    if not os.path.exists('./images'):
        os.mkdir('./images')
    data = input_data.read_data_sets('../MNIST_data')
    x, y = data.train.next_batch(200)
    for i, (arr, label) in enumerate(zip(x, y)):
        print(i, label)
        gen_images(arr, i, label)
