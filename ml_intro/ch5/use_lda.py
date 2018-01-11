from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
__author__ = 'wangj'
__date__ = '2018/01/09 01:27'

def plot_decision_regions(X, Y, classifier, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(Y))])

    # plot decision surface

    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    print("\nx1_min, x1_max:\n", x1_min, x1_max)
    print("\nx2_min, x2_max\n", x2_min, x2_max)
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
    plt.contourf(xx, yy, z, alpha=0.4, cmap=cmap)

    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    # plot class samples
    for idx, cl in enumerate(np.unique(Y)):
        plt.scatter(x=X[Y == cl, 0], y=X[Y == cl, 1], alpha=0.8, c=cmap(idx), marker=markers[idx], label=cl)


if __name__ == '__main__':
    wine = datasets.load_wine()
    x = wine.data
    y = wine.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    stdsc = StandardScaler()
    x_train_std = stdsc.fit_transform(x_train)
    x_test_std = stdsc.transform(x_test)
    lda = LinearDiscriminantAnalysis(n_components=2)
    lr = LogisticRegression()
    x_train_lda = lda.fit_transform(x_train_std, y_train)
    x_test_lda = lda.transform(x_test_std)
    lr = lr.fit(x_train_lda,y_train)
    plot_decision_regions(x_train_lda,y_train,classifier=lr)
    plt.figure(1)
    plt.xlabel('LD 1')
    plt.ylabel('LD 2')
    plt.legend(loc='lower left')
    plt.show()
    plt.figure(2)
    plot_decision_regions(x_test_lda,y_test,classifier=lr)
    plt.xlabel('LD 1')
    plt.ylabel('LD 2')
    plt.legend(loc='lower left')
    plt.show()
