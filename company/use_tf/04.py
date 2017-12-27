import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root, fsolve

__author__ = 'wangj'
__date__ = '2017/12/20 00:58'


# 1、求解f(x)=2*sin(x)-x+1
def f1(x):
    return np.sin(x) * 2 - x + 1


# 2、求解线性方程组{3X1+2X2=3;X1-2X2=5}
def f2(x):
    return np.array([3 * x[0] + 2 * x[1] - 3, x[0] - 2 * x[1] - 5])


# 3、求解非线性方程组
def f3(x):
    return np.array([2 * x[0] ** 2 + 3 * x[1] - 3 * x[2] ** 3 - 7,
                     x[0] + 4 * x[1] ** 2 + 8 * x[2] - 10,
                     x[0] - 2 * x[1] ** 3 - 2 * x[2] ** 2 + 1])


if __name__ == '__main__':
    range_x_1 = np.linspace(-2, 8)
    range_y_1, range_y_2 = 2 * np.sin(range_x_1), range_x_1 - 1
    fig_1 = plt.figure(1)
    plt.plot(range_x_1, range_y_1, 'r', range_x_1, range_y_2, 'b--')
    plt.title('$2sin(x)$ and $x-1$')
    # sol_1_root = root(f1, [2])
    sol_1_fsolve = fsolve(f1, [2])
    plt.scatter(sol_1_fsolve, 2 * np.sin(sol_1_fsolve), linewidths=9)
    fig_1.show()

    sol_2_root = root(f2, [0, 0])
    sol_2_fsolve = fsolve(f2, [0, 0])
    print(sol_2_root)
    print('sol_2_fsolve:', sol_2_fsolve)

    sol3_root = root(f3, [0, 0, 0])
    sol3_fsolve = fsolve(f3, [0, 0, 0])
    print('sol_3_fsolve:', sol3_fsolve)
