import numpy as np
from matplotlib import pyplot as plt
from ml_intro.plot_decision_regions import plot_decision_regions
from sklearn.svm import SVC

__author__ = 'wangj'
__date__ = '2017/11/29 14:39'


def plot():
    np.random.seed(0)
    X_xor = np.random.randn(200, 2)
    Y_xor = np.logical_xor(X_xor[:, 0] > 0, X_xor[:, 1] > 0)
    Y_xor = np.where(Y_xor, 1, -1)
    plt.scatter(X_xor[Y_xor == 1, 0], X_xor[Y_xor == 1, 1], c='b', marker='x', label='1')
    plt.scatter(X_xor[Y_xor == -1, 0], X_xor[Y_xor == -1, 1], c='r', marker='s', label='-1')
    plt.ylim(-3, 0)
    plt.legend(loc='upper left')
    plt.show()
    return X_xor, Y_xor


def main():
    X_xor, Y_xor = plot()
    svm = SVC(kernel='rbf', random_state=0, gamma=0.1, C=10.0)
    svm.fit(X_xor, Y_xor)
    plot_decision_regions(X_xor, Y_xor, classifier=svm)
    svm = SVC(kernel='rbf', random_state=0, gamma=1, C=10.0)
    svm.fit(X_xor, Y_xor)
    plot_decision_regions(X_xor, Y_xor, classifier=svm)


if __name__ == '__main__':
    main()
