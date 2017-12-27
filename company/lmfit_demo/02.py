from numpy import sqrt, pi, exp, linspace, loadtxt
from lmfit import Model
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

__author__ = 'wangj'
__date__ = '2017/12/26 00:03'


def gaussian(x, amp, cen, wid):
    "1-d gaussian: gaussian(x, amp, cen, wid)"
    return (amp / (sqrt(2 * pi) * wid)) * exp(-(x - cen) ** 2 / (2 * wid ** 2))


if __name__ == '__main__':
    # data = loadtxt('model1d_gauss.dat')
    x = np.linspace(-10, 10, 100)
    y = stats.norm.pdf(x, 0, 1)
    gmodel = Model(gaussian)
    result = gmodel.fit(y, x=x, amp=5, cen=5, wid=1)
    print(result.fit_report())

    plt.plot(x, y, 'bo')
    plt.plot(x, result.init_fit, 'k--')
    plt.plot(x, result.best_fit, 'r-')
    plt.show()
