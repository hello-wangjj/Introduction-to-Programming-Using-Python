from numpy import genfromtxt
import numpy as np
from sklearn import datasets, linear_model
import os

__author__ = 'wangj'
__date__ = '2017/08/20 17:26'

dataPath = os.path.dirname(__file__) + '/delivery.csv'
deliveryData = genfromtxt(dataPath, delimiter=',')
print('data:', deliveryData)
X = deliveryData[:, :-1]
Y = deliveryData[:, -1]
print('X:', X)
print('Y:', Y)

regr = linear_model.LinearRegression()
regr.fit(X, Y)

# 打印系数
print('coefficients:', regr.coef_)
print('intercept:', regr.intercept_)

# 预测
x_test = [80, 2]
y_test = 6.2
print(regr.predict([x_test]))


# print(dataPath)
def main():
    pass


if __name__ == '__main__':
    main()
