from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import numpy as np
from matplotlib import pylab as plt
__author__ = 'wangj'
__date__ = '2017/11/28 21:13'


def main():
    iris = datasets.load_iris()
    X = iris.data[:,:2] # 取前2个特征
    Y = iris.target

    h = .02  # step size in the mesh

    lr = LogisticRegression(C=1e5)
    lr.fit(X,Y)
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    # 生成网格
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = lr.predict(np.c_[xx.ravel(), yy.ravel()])
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(1, figsize=(4, 3))
    plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)
    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')

    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())

    plt.show()
    print(lr.predict_proba([5, 3.4]))



if __name__ == '__main__':
    main()