from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

__author__ = 'wangj'
__date__ = '2018/01/04 17:02'

if __name__ == '__main__':
    # 数据预处理
    wine = datasets.load_wine()
    x = wine.data
    y = wine.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    stdsc = StandardScaler()
    x_train_std = stdsc.fit_transform(x_train)
    x_test_std = stdsc.transform(x_test)
    # 构造协方差矩阵
    cov_mat = np.cov(x_train_std.T)
    eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)
    print('\nEigenvalues \n {0}'.format(eigen_vals))
    tot = sum(eigen_vals)
    var_exp = [(i / tot) for i in sorted(eigen_vals, reverse=True)]
    cum_var_exp = np.cumsum(var_exp)
    plt.bar(range(1, 14), var_exp, align='center', label='individual explained variance')
    plt.step(range(1, 14), cum_var_exp, where='mid', label='cumulative explained variance')
    plt.ylabel('explained variance ratio')
    plt.xlabel('principal components')
    plt.legend(loc='best')
    plt.show()
    # 将特征值排序
    eigen_pairs = [(np.abs(eigen_vals[i]), eigen_vecs[:, i]) for i in range(len(eigen_vals))]
    eigen_pairs.sort(reverse=True)
    # 测试 选取对应特征值最大的特征向量
    w = np.hstack((eigen_pairs[0][1][:, np.newaxis],
                   eigen_pairs[1][1][:, np.newaxis]))
    print('\nMatrix w:\n', w)
    # x_train_std[0].dot(w)
    x_train_pca = x_train_std.dot(w)
    colors = ['r', 'b', 'g']
    markers = ['s', 'x', 'o']
    for l, c, m in zip(np.unique(y_train), colors, markers):
        plt.scatter(x_train_pca[y_train == l, 0],
                    x_train_pca[y_train == l, 1],
                    color=c, label=l, marker=m)
    plt.xlabel('PC 1')
    plt.ylabel('PC 2')
    plt.legend(loc='lower left')
    plt.show()
