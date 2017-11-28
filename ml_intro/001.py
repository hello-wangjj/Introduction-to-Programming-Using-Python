from matplotlib import pyplot as plt
import numpy as np
from sklearn import datasets
import pandas as pd
from ml_intro.ganzhiqi import Perceptron
from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    camp = ListedColormap(colors[:len(np.unique(y))])
    # plot the decision surface
    # 对2个特征的最大和最小值做限定
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    print("x1_min,x1_max:", x1_min, x1_max)
    print("x2_min, x2_max", x2_min, x2_max)
    # x1_min,x1_max: 3.3 8.0
    # x2_min, x2_max 1.0 5.4
    # 生成2维数组 xx1=[] xx2=[] shape=(220,235)
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    print(np.array([xx1.ravel(), xx2.ravel()]).shape)
    z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    # z.shape = 51700
    print(z.shape)
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, alpha=0.4, camp=camp)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=0.8, c=camp(idx), marker=markers[idx], label=cl)


iris = datasets.load_iris()
# print(iris.data)
# print(iris.target)
x = iris.data

y = iris.target
# print(x.shape, y.shape)
x = x[:100, :]
y = y[:100]
y[:50] = -1
fig1 = plt.figure('fig1')
plt.scatter(x[:50, 0], x[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(x[50:100, 0], x[50:100, 1], color='blue', marker='x', label='versicolor')

plt.xlabel('petal length')
plt.ylabel('sepal width')
plt.legend(loc='upper left')
plt.show('fig1')
ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X=x, y=y)
fig2 = plt.figure('fig2')
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of mis classification')
plt.show('fig2')
print(ppn.w_)
print(ppn.predict([5.1, 3.5, 1.4, 0.2]))
print(ppn.predict([4.9, 3, 1.4, 0.2]))
fig3 = plt.figure('fig3')
x = x[:, :2]
ppn2 = Perceptron(eta=0.1, n_iter=10)
ppn2.fit(X=x, y=y)
plt.plot(range(1, len(ppn2.errors_) + 1), ppn2.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of mis classification')
plt.show('fig3')
fig4 = plt.figure('fig4')
plot_decision_regions(x, y, classifier=ppn2)
plt.xlabel('petal length')
plt.ylabel('sepal width')
plt.legend(loc='upper left')
plt.show('fig4')

fig5 = plt
