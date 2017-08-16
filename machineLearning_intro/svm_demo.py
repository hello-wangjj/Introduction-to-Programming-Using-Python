#!python3
# -*- coding: utf-8 -*-
from sklearn import svm
__author__ = 'wangjj'
__date__ = '2017/8/11 19:41'

x = [[2, 0], [1, 1], [2, 3]]
y = [0, 0, 1]
clf = svm.SVC(kernel='linear')
clf.fit(x, y)
print(clf)
print(clf.support_vectors_)
print(clf.support_)
print(clf.n_support_)
print(clf.predict([[2, 0], [3, 0], [3, 6]]))
