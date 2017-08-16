#!python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as pl
from sklearn import svm
__author__ = 'wangjj'
__date__ = '2017/8/11 19:49'
np.random.seed(0)
# 产生data
X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
# 产生 labels
Y = [0] * 20 + [1] * 20
clf = svm.SVC(kernel='linear')
clf.fit(X, Y)

# get the separating hyper plane
w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(-5, 5)
yy = a * xx - (clf.intercept_[0] / w[1])

b = clf.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = clf.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])

print('w:', w)
print('a:', a)
pl.plot(xx, yy, 'k-')
pl.plot(xx, yy_down, 'k--')
pl.plot(xx, yy_up, 'k--')
pl.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80, facecolors='none')
pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)
pl.axis('tight')
pl.show()
