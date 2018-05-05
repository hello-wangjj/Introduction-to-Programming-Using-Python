import os
import struct
import numpy as np
from matplotlib import pyplot as plt

__author__ = 'wangj'
__date__ = '2018/04/30 11:20'


def main():
    pass


def load_mnist(path, kind='train'):
    """Load MNIST data from `path`"""
    labels_path = os.path.join(path, '{0}-labels.idx1-ubyte'.format(kind))
    images_path = os.path.join(path, '{0}-images.idx3-ubyte'.format(kind))

    with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II', lbpath.read(8))
        labels = np.fromfile(lbpath, dtype=np.uint8)

    with open(images_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack('>IIII', imgpath.read(16))
        images = np.fromfile(imgpath, dtype=np.uint8).reshape(len(labels), -1)

    return images, labels


if __name__ == '__main__':
    X_train, y_train = load_mnist('MNIST_data', kind='train')
    fix, ax = plt.subplots(nrows=2, ncols=5, sharex=True, sharey=True)
    ax = ax.flatten()
    for i in range(10):
        img = X_train[y_train == i][0].reshape(28, 28)
        # img = np.reshape((1-X_train[y_train == i][0]),(28,28))
        # ax[i].imshow(img, cmap='Greys', interpolation='nearest')
        ax[i].imshow(img, cmap='Greys', interpolation='nearest')



    ax[0].set_xticks([])
    ax[0].set_yticks([])
    plt.tight_layout()
    plt.show()

    fig, ax = plt.subplots(nrows=5, ncols=5, sharex=True, sharey=True, )

    ax = ax.flatten()
    for i in range(25):
        img = X_train[y_train == 7][i].reshape(28, 28)
        ax[i].imshow(img, cmap='Greys', interpolation='nearest')

    ax[0].set_xticks([])
    ax[0].set_yticks([])
    plt.tight_layout()
    plt.show()
