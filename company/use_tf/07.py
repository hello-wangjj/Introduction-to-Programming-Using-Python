import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

__author__ = 'wangj'
__date__ = '2017/12/24 02:16'


# 需要拟合的函数
def f(x, p):
    return p[0] * np.sin(p[4] * x) + p[1] * (
            1 - 1 / np.sqrt(1 - p[2] * p[2]) * np.e ** (-p[3]) * np.sin(
        np.sqrt(1 - p[2] * p[2]) * p[5] * x + np.arccos(p[2])))


# 误差项
def residual(p, y, x):
    return y - f(x, p)


if __name__ == '__main__':
    x = np.linspace(0, 100, 100)
    p = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    y_true = np.sin(x)
    plesq = optimize.leastsq(residual, p, args=(y_true, x))
    print(plesq)
    fig = plt.figure()
    plt.plot(x, f(x, plesq[0]), x, y_true, 'o')
    fig.show()
