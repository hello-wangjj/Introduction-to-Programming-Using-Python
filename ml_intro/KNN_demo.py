from sklearn import datasets
from ml_intro.plot_decision_regions import plot_decision_regions
from sklearn.neighbors import KNeighborsClassifier

__author__ = 'wangj'
__date__ = '2017/11/29 20:33'


def main():
    iris = datasets.load_iris()
    X = iris.data[:, :2]  # 取前2个特征
    Y = iris.target
    knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
    knn.fit(X, Y)
    plot_decision_regions(X, Y, classifier=knn)


if __name__ == '__main__':
    main()
