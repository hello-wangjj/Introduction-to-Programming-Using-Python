import numpy as np
import random

__author__ = 'wangj'
__date__ = '2017/08/21 10:52'


def gradientDescent(x, y, theta, alpha, m, numIterations):
    '''
    梯度下降算法
    :param x: 实例
    :param y:
    :param theta: 向量值，目标值
    :param alpha: 学习率
    :param m: 实例个数
    :param numIterations: 迭代次数
    :return:
    '''
    xTrans = np.transpose(x)
    for i in range(0, numIterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y

        cost = np.sum(loss ** 2) / (2 * m)
        print('iteration: {0:d} / cost: {1:f}'.format(i, cost))
        gradient = np.dot(xTrans, loss) / m
        theta = theta - alpha * gradient
    return theta


def genData(numPoints, bias, variance):
    '''
    生成数据
    :param numPoints: 实例, 行数
    :param bias: 偏好值
    :param variance: 方差
    :return:
    '''
    x = np.zeros(shape=(numPoints, 2))
    y = np.zeros(shape=numPoints)

    for i in range(0, numPoints):
        # bias feature
        x[i][0] = 1
        x[i][1] = i
        y[i] = (i + bias) + random.uniform(0, 1) * variance
    return x, y


def main():
    x, y = genData(100, 25, 10)
    print('x:', x)
    print('y:', y)
    print('x shape:', np.shape(x))
    m, n = np.shape(x)
    print('y shape:', np.shape(y))
    numIteration = 10000
    alpha = 0.0005
    theta = np.ones(n)
    theta = gradientDescent(x, y, theta, alpha, m, numIteration)
    print('theta:', theta)


if __name__ == '__main__':
    main()
