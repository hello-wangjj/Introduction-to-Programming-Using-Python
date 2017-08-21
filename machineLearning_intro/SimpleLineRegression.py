import numpy as np
import matplotlib.pyplot as plt
__author__ = 'wangj'
__date__ = '2017/08/19 20:09'


def fitslr(x, y):
    n = len(x)
    denominator = 0
    numerator = 0
    for i in range(0, n):
        numerator += (x[i] - np.mean(x))*(y[i]-np.mean(y))
        denominator += (x[i] - np.mean(x))**2

    print('numerator:', numerator)
    print('denominator:', denominator)
    b1 = numerator/float(denominator)
    b0 = np.mean(y)/float(np.mean(x))
    return b0, b1


def predict(x, b0, b1):
    return b0 + x*b1


def main():
    x = [1, 3, 2, 1, 3]
    y = [14, 24, 18, 17, 27]
    b0, b1 = fitslr(x, y)
    print('intercept:', b0, 'slope:', b1)
    x_test = 6
    y_test = predict(x_test, b0, b1)
    print('y_test:', y_test)

    # 画图
    # 散点
    plt.scatter(x, y)
    plt.scatter(x_test, y_test, c='green')
    # 直线
    xx = np.linspace(1, 6)
    yy = b1 * xx + b0
    plt.plot(xx, yy, 'k-')
    plt.show()


if __name__ == '__main__':
    main()