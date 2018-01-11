from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

__author__ = 'wangj'
__date__ = '2018/01/07 17:03'


def main():
    pass


if __name__ == '__main__':
    # 数据预处理
    wine = datasets.load_wine()
    x = wine.data
    y = wine.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    stdsc = StandardScaler()
    x_train_std = stdsc.fit_transform(x_train)
    x_test_std = stdsc.transform(x_test)
    np.set_printoptions(precision=4)
    # 计算每一类的特征均值向量
    mean_vecs = []
    for label in range(0, 3):
        mean_vecs.append(np.mean(x_train_std[y_train == label], axis=0))
        print('\nMV{}:{}\n'.format(label, mean_vecs[label]))
    # 计算类内散布矩阵Sw
    # number of features 13维的特征
    d = 13
    s_w = np.zeros((d, d))
    for label, mv in zip(range(0, 3), mean_vecs):
        # class_scatter = np.zeros((d, d))
        # for row in x[y == label]:
        #     row, mv = row.reshape(d, 1), mv.reshape(d, 1)
        #     class_scatter += (row - mv).dot((row - mv).T)
        # 在通过累加方式计算散布矩阵 需要对si做缩放处理，发现与计算协方差的方式一致
        class_scatter = np.cov(x_train_std[y_train == label].T)
        s_w += class_scatter
    print('within-class scatter matirx:{}x{}'.format(s_w.shape[0], s_w.shape[1]))
    print('class label distribution: {}'.format(np.bincount(y_train)))
    # 计算类间散布矩阵
    mean_overall = np.mean(x_train_std, axis=0)
    d = 13
    s_b = np.zeros((d, d))
    for i, mean_vec in enumerate(mean_vecs):
        n = x[y == i].shape[0]
        mean_vec = mean_vec.reshape(d, 1)
        mean_overall = mean_overall.reshape(d, 1)
        s_b += n * (mean_vec - mean_overall).dot((mean_vec - mean_overall).T)
    print('between class scatter matrix: {}x{}'.format(s_b.shape[0], s_b.shape[1]))

    # 在新的特征子空间上选取线性判别算法
    # 求s_w-1*s_b
    eigen_vals, eigen_vecs = np.linalg.eig(np.linalg.inv(s_w).dot(s_b))
    eigen_pairs = [(np.abs(eigen_vals[i]), eigen_vecs[i]) for i in range(len(eigen_vals))]
    eigen_pairs = sorted(eigen_pairs, key=lambda k: k[0], reverse=True)
    print('Eigenvalues in decreasing order:\n')
    for eigen_val in eigen_pairs:
        print(eigen_val[0])
    tot = sum(eigen_vals.real)
    discr = [(i / tot) for i in sorted(eigen_vals.real, reverse=True)]
    cum_discr = np.cumsum(discr)
    plt.figure(1)
    plt.bar(range(1, 14), discr, alpha=0.5, align='center', label='individual "discriminability"')
    plt.step(range(1, 14), cum_discr, where='mid', label='cumulative "discriminability"')
    plt.ylabel('"discriminability" ratio')
    plt.xlabel('Linear Discriminants')
    plt.ylim([-0.1, 1.1])
    plt.legend(loc='best')
    plt.show()
    # 选择2个判别能力最强的特征向量来构建转换矩阵
    w = np.hstack((eigen_pairs[0][1][:, np.newaxis].real,
                   eigen_pairs[1][1][:, np.newaxis].real))
    print('Matirx:\n:', w)
    # 通过乘积的方式对训练数据集进行转换
    x_train_lda = x_train_std.dot(w)
    colors = ['r', 'g', 'b']
    markers = ['s', 'x', 'o']
    plt.figure(2)
    for l, c, m in zip(np.unique(y_train), colors, markers):
        plt.scatter(x_train_lda[y_train == l, 0], x_train_lda[y_train == l, 1], c=c, label=l, marker=m)
    plt.xlabel('LD 1')
    plt.ylabel('LD 2')
    plt.legend(loc='upper right')
    plt.show()
