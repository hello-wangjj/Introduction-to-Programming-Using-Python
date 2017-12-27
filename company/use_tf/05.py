import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

__author__ = 'wangj'
__date__ = '2017/12/20 17:03'


def func(x, p):
    """
    数据拟合所用的函数: A*sin(2*pi*k*x + theta)
    """

    return p[0] * np.sin(x) + p[1] * (
            1 - 1 / np.sqrt(1 - p[2] * p[2]) * np.sin(np.sqrt(1 - p[2] * p[2]) * x + np.arccos(p[2])))


def residuals(p, y, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y - func(x, p)


if __name__ == '__main__':
    x = np.linspace(0, -2 * np.pi, 100)
    p = [0.0001, 0.0001, 0.0001, 0.0001]
    # 假设的真实数据
    y0 = np.cos(x)
    # 调用leastsq进行数据拟合
    # residuals为计算误差的函数
    # p0为拟合参数的初始值
    # args为需要拟合的实验数据
    plsq = leastsq(residuals, p0, args=(y1, x))