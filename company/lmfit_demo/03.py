from numpy import sqrt, pi, exp, loadtxt
from lmfit import Model
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
__author__ = 'wangj'
__date__ = '2017/12/26 00:27'


def gaussian(x, amp, cen, wid):
    "1-d gaussian: gaussian(x, amp, cen, wid)"
    return (amp/(sqrt(2*pi)*wid)) * exp(-(x-cen)**2 /(2*wid**2))

def line(x, slope, intercept):
    "line"
    return slope * x + intercept


if __name__ == '__main__':
    x = np.linspace(-10, 10, 100)
    y = stats.norm.pdf(x, 0, 1) + 0.25*x-1
    mod = Model(gaussian) + Model(line)
    pars  = mod.make_params( amp=5, cen=5, wid=1, slope=0, intercept=1)

    result = mod.fit(y, pars, x=x)

    print(result.fit_report())

    plt.plot(x, y,         'bo')
    plt.plot(x, result.init_fit, 'k--')
    plt.plot(x, result.best_fit, 'r-')
    plt.show()