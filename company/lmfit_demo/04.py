from numpy import sqrt, pi, exp, sin, arccos, cos
from lmfit import Model
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

__author__ = 'wangj'
__date__ = '2017/12/26 00:41'


def my_sin(x, w1, k):
    return w1 * sin(k * x)


def my_damping(x, w2, a, b, c):
    return w2 * (1 - 1 / sqrt(1 - a ** 2) * exp(-c) * sin(sqrt(1 - a ** 2) * b * x + arccos(a)))


def my_peak(x, m, n):
    return m * stats.poisson.cdf(x, n)


# k1 = 1.501169e-01
# 待求参数
# k2 = 1.209591e-01
# 待求参数
# k3 = 9.115386e-01
# 待求参数
# k4 = -7.802862e-01
# 待求参数
# k5 = 1.938117e+00
# 待求参数
# k6 = 9.155105e-02

if __name__ == '__main__':
    x = np.linspace(1, 200, 200)
    # y = 10*cos(x) + sin(x)+exp(-2)*sin(x)
    y = - 1/2*sin(x+2)+1
    mod = Model(my_sin) + Model(my_damping)
    pars = mod.make_params(w1=6.3367e-09, k=-6.8788e+05, w2=-0.00114982, a=0.09950371, b=1.00498756, c=2,
                           m=0, n=10)
    pars['a'].set(min=0.01, max=0.9999)
    result = mod.fit(y, pars, x=x)

    print(result.fit_report())
    fig = plt.figure(figsize=(20, 10))
    initial, = plt.plot(x, y, 'bo-')
    # plt.plot(x, result.init_fit, 'k--')
    best_fit, =  plt.plot(x, result.best_fit, 'r*-')
    plt.legend(handles=[initial, best_fit, ], labels=['initial', 'best_fit'], loc='best')
    plt.show()
