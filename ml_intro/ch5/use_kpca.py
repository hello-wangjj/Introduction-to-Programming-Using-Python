from sklearn.decomposition import KernelPCA
from sklearn import datasets
import matplotlib.pyplot as plt

__author__ = 'wangj'
__date__ = '2018/01/11 20:38'

if __name__ == '__main__':
    x, y = datasets.make_moons(n_samples=100, random_state=123)
    scikit_kpca = KernelPCA(n_components=2, kernel='rbf', gamma=15)
    x_skpca = scikit_kpca.fit_transform(x)
    plt.figure(1)
    plt.scatter(x_skpca[y == 0, 0], x_skpca[y == 0, 1], color='red', marker='^', alpha=0.5)
    plt.scatter(x_skpca[y == 1, 0], x_skpca[y == 1, 1], color='red', marker='o', alpha=0.5)
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.show()
