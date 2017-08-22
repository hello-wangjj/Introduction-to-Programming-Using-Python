import numpy as np
import math

__author__ = 'wangj'
__date__ = '2017/08/21 16:22'


def compute_correlation(X, Y):
    xBar = np.mean(X)
    yBar = np.mean(Y)

    SSR = 0
    varX = 0
    varY = 0

    for i in range(0, len(X)):
        diff_X_XBar = X[i] - xBar
        diff_Y_YBar = Y[i] - yBar
        SSR += (diff_X_XBar * diff_Y_YBar)
        varX = diff_X_XBar ** 2
        varY = diff_Y_YBar ** 2

    SST = math.sqrt(varX * varY)
    return SSR / SST


def main():
    testX = [1, 3, 8, 7, 9]
    testY = [10, 12, 24, 21, 34]
    print('r:', compute_correlation(testX, testY))
    print('coeffs:', np.polyfit(testX, testY, 1))

if __name__ == '__main__':
    main()
