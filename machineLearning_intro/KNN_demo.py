#!python3
# -*- coding: utf-8 -*-
from sklearn import neighbors
from sklearn import datasets
__author__ = 'wangjj'
__date__ = '2017/8/11 0:05'

knn = neighbors.KNeighborsClassifier()

iris = datasets.load_iris()
print(iris)

knn.fit(iris.data, iris.target)

predictedLabel = knn.predict([[0.1, 0.2, 0.3, 0.4]])
print(predictedLabel)
