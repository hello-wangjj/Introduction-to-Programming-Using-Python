import numpy as np
import matplotlib.pyplot as plt

__author__ = 'wangj'
__date__ = '2017/11/29 00:28'


def plot_decision_regions(X, Y, classifier, resolution=0.02):
    # setup marker generator and color map

    x1_min, x1_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    x2_min, x2_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    print("x1_min,x1_max:", x1_min, x1_max)
    print("x2_min, x2_max", x2_min, x2_max)
    # x1_min,x1_max: 3.3 8.0 4.7
    # x2_min, x2_max 1.0 5.4 4.4
    # 生成2维数组 xx1=[] xx2=[] shape=(220,235)
    xx, yy = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    print(np.array([xx.ravel(), yy.ravel()]).shape)
    z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    # z.shape = 51700
    print(z.shape)
    z = z.reshape(xx.shape)
    plt.figure(1, figsize=(4, 3))
    plt.pcolormesh(xx, yy, z, cmap=plt.cm.Paired)
    # plt.contourf(xx, yy, z, alpha=0.4, cmap=plt.cm.Paired)
    plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')

    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    # plot class samples
    plt.xticks(())
    plt.yticks(())

    plt.show()


def main():
    pass


if __name__ == '__main__':
    main()
