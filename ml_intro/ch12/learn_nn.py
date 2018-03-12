import os
import struct
import numpy as np
import matplotlib.pyplot as plt

__author__ = 'wangj'
__date__ = '2018/01/30 10:38'


def main():
    pass


def load_mnist(path, kind='train'):
    '''
    load mnist data from path
    :param path:
    :param kind:
    :return:
    '''
    label_path = os.path.join(path, '{0}-labels.idx1-ubyte'.format(kind))
    image_path = os.path.join(path, '{0}-images.idx3-ubyte'.format(kind))
    with open(label_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II', lbpath.read(8))
        labels = np.fromfile(lbpath, dtype=np.uint8)

    with open(image_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack('>IIII', imgpath.read(16))
        images = np.fromfile(imgpath, dtype=np.uint8).reshape(len(labels), 784)

    return images, labels


if __name__ == '__main__':
    x_train, y_train = load_mnist('E:\document\mnist', kind='train')
    print('rows:{0:d}, columns: {1:d}'.format(x_train.shape[0], x_train.shape[1]))
    x_test, y_test = load_mnist('E:\document\mnist', kind='t10k')
    print('rows:{0:d}, columns: {1:d}'.format(x_test.shape[0], x_test.shape[1]))
    plt.figure(1)
    fig, ax = plt.subplots(nrows=2, ncols=5, sharex=True, sharey=True)
    ax = ax.flatten()
    for i in range(10):
        img = x_train[y_train == i][0].reshape(28, 28)
        ax[i].imshow(img, cmap='Greys', interpolation='nearest')
    ax[0].set_xticks([])
    ax[0].set_yticks([])
    plt.tight_layout()
    plt.show()
    # 看下不同版本的数字
    plt.figure(2)
    fig, ax = plt.subplots(nrows=5, ncols=5, sharex=True, sharey=True)
    ax = ax.flatten()
    for i in range(25):
        img = x_train[y_train == 7][i].reshape(28, 28)
        ax[i].imshow(img, cmap='Greys', interpolation='nearest')
    ax[0].set_xticks([])
    ax[0].set_yticks([])
    plt.tight_layout()
    plt.show()
    # 保存为numpy csv格式
    # np.savetxt('E:\document\mnist\\train_img.csv', x_train, fmt='%i', delimiter=',')
    # np.savetxt('E:\document\mnist\\train_labels.csv', y_train, fmt='%i', delimiter=',')
    # np.savetxt('E:\document\mnist\\test_img.csv', x_test, fmt='%i', delimiter=',')
    # np.savetxt('E:\document\mnist\\test_labels.csv', y_test, fmt='%i', delimiter=',')
    # 读取csv
    x_train = np.genfromtxt('E:\document\mnist\\train_img.csv', dtype=int, delimiter=',')
