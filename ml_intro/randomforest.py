import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from ml_intro.plot_decision_regions import plot_decision_regions

__author__ = 'wangj'
__date__ = '2017/11/29 17:04'


def main():
    iris = datasets.load_iris()
    X = iris.data[:, :2]  # 取前2个特征
    Y = iris.target
    forest = RandomForestClassifier(criterion='entropy', n_estimators=10, random_state=1, n_jobs=2)
    forest.fit(X,Y)
    plot_decision_regions(X, Y, classifier=forest)


if __name__ == '__main__':
    main()
