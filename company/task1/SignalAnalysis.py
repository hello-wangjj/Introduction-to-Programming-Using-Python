from matplotlib import pyplot as plt
import numpy as np

__author__ = 'wangj'
__date__ = '2017/12/16 16:25'
__doc__ = '''
回归算法：
假设一个时序信号S(t)可以写成F1,F2和F3三个函数的线性叠加,即
S(t)=a1*F1+a2*F2+a3*F3.那么在S(t)已知,和F1,F2,F3形式已知的情况下,回归出三个
权重系数a1,a2,a3,和所有F1-F3函数里的未知参数.
任务：对于任意输入S(t),用Matlab或者Python实现所有位置参数的求解
'''


def main():
    x = np.arange(0, 10 * np.pi, 0.1)
    f1 = np.sin(x)
    fig1 = plt.figure()
    plt.plot(x, f1, 'r')
    plt.grid()
    fig1.show()
    f2_w1 = 0.1
    f2_w2 = 3
    f2 = 1 - 1 / np.sqrt(1 - f2_w1 ** 2) * np.sin(np.sqrt(1 - f2_w1 ** 2) * f2_w2 * x + np.arccos(f2_w1))
    fig2 = plt.figure()
    plt.plot(x, f2, 'b')
    fig2.show()


if __name__ == '__main__':
    x = np.linspace(1, 10, 100)
