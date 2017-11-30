import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import datasets
from ml_intro.plot_decision_regions import plot_decision_regions

__author__ = 'wangj'
__date__ = '2017/11/29 16:31'


def main():
    iris = datasets.load_iris()
    X = iris.data[:, :2]  # 取前2个特征
    Y = iris.target
    tree = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
    tree.fit(X, Y)
    plot_decision_regions(X, Y, tree)
    export_graphviz(tree, out_file='tree.dot', feature_names=iris.feature_names[:2])


if __name__ == '__main__':
    main()
