from sklearn.svm import SVC
from ml_intro.plot_decision_regions import plot_decision_regions
from sklearn import datasets
import numpy as np
from matplotlib import pylab as plt

__author__ = 'wangj'
__date__ = '2017/11/29 00:26'


def main():
    iris = datasets.load_iris()
    X = iris.data[:, :2]  # 取前2个特征
    Y = iris.target
    svm = SVC(kernel='linear', C=1.0, random_state=0)
    svm.fit(X, Y)
    plot_decision_regions(X, Y, classifier=svm)


if __name__ == '__main__':
    main()
