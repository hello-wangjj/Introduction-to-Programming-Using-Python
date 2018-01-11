from scipy.spatial.distance import pdist, squareform
from scipy import exp
from scipy.linalg import eigh
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from matplotlib.ticker import FormatStrFormatter

__author__ = 'wangj'
__date__ = '2018/01/09 20:53'


def rbf_kernel_pca(X, gamma, n_components):
    '''
    RBF kernel PCA implementation
    :param X: shape={n_samples, n_features}
    :param gamma: float, tuning parameter of the rbf kernel
    :param n_components:  number of principal components to return
    :return:  X_pca shape={n_samples, k_features}
    '''
    # calculate pairwise squared Euclidean matrix in the MxN dimensional dataset
    sq_dists = pdist(X, 'sqeuclidean')
    # convert pairwise distance into a square matrix
    mat_sq_dists = squareform(sq_dists)

    # compute the symmetric kernel matrix
    K = exp(-gamma * mat_sq_dists)

    # center the kernel matrix
    N = K.shape[0]
    one_n = np.ones((N, N)) / N
    K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)

    # obtaining eigenpairs from the centered kernel matrix
    # numpy.eigh returns them in sorted order
    eigvals, eigvecs = eigh(K)

    # collect the top k eigen vectors (projected samples)
    # x_pc = np.column_stack((eigvecs[:, -i]) for i in range(1, n_components + 1))
    alphas = np.column_stack((eigvecs[:, -i]) for i in range(1, n_components + 1))

    # collect the corresponding eigenvalues
    lambdas = [eigvals[-i] for i in range(1, n_components + 1)]
    return alphas, lambdas


if __name__ == '__main__':
    # 半月形数据
    x, y = datasets.make_moons(n_samples=100, random_state=123)
    plt.figure(1)
    plt.scatter(x[y == 0, 0], x[y == 0, 1], color='red', marker='^', alpha=0.5)
    plt.scatter(x[y == 1, 0], x[y == 1, 1], color='blue', marker='o', alpha=0.5)
    plt.show()
    scikit_pca = PCA(n_components=2)
    x_spca = scikit_pca.fit_transform(x)
    # pca
    plt.figure(2)
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7, 4))
    ax[0].scatter(x_spca[y == 0, 0], x_spca[y == 0, 1], color='red', marker='^', alpha=0.5)
    ax[0].scatter(x_spca[y == 1, 0], x_spca[y == 1, 1], color='blue', marker='o', alpha=0.5)
    ax[1].scatter(x_spca[y == 0, 0], np.zeros((50, 1)) + 0.02, color='red', marker='^', alpha=0.5)
    ax[1].scatter(x_spca[y == 1, 0], np.zeros((50, 1)) - 0.02, color='blue', marker='o', alpha=0.5)
    ax[0].set_xlabel('pc 1')
    ax[0].set_ylabel('pc 2')
    ax[1].set_ylim([-1, 1])
    ax[1].set_yticks([])
    ax[1].set_xlabel('pc1')
    plt.show()
    # k pca
    x_kpca, _ = rbf_kernel_pca(x, gamma=15, n_components=2)
    plt.figure(3)
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7, 4))
    ax[0].scatter(x_kpca[y == 0, 0], x_kpca[y == 0, 1], color='red', marker='^', alpha=0.5)
    ax[0].scatter(x_kpca[y == 1, 0], x_kpca[y == 1, 1], color='blue', marker='o', alpha=0.5)
    ax[1].scatter(x_kpca[y == 0, 0], np.zeros((50, 1)) + 0.02, color='red', marker='^', alpha=0.5)
    ax[1].scatter(x_kpca[y == 1, 0], np.zeros((50, 1)) - 0.02, color='blue', marker='o', alpha=0.5)
    ax[0].set_xlabel('pc 1')
    ax[0].set_ylabel('pc 2')
    ax[1].set_ylim([-1, 1])
    ax[1].set_yticks([])
    ax[1].set_xlabel('pc1')
    ax[0].xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
    ax[1].xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
    plt.show()

    # 分离同心圆
    x_circle, y_circle = datasets.make_circles(n_samples=1000, random_state=123, noise=0.1, factor=0.2)
    plt.figure(4)
    plt.scatter(x_circle[y_circle == 0, 0], x_circle[y_circle == 0, 1], color='red', marker='^', alpha=0.5)
    plt.scatter(x_circle[y_circle == 1, 0], x_circle[y_circle == 1, 1], color='blue', marker='o', alpha=0.5)
    plt.show()
    # pca
    x_circle_spca = scikit_pca.fit_transform(x_circle)
    plt.figure(5)
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7, 4))
    ax[0].scatter(x_circle_spca[y_circle == 0, 0], x_circle_spca[y_circle == 0, 1], color='red', marker='^', alpha=0.5)
    ax[0].scatter(x_circle_spca[y_circle == 1, 0], x_circle_spca[y_circle == 1, 1], color='blue', marker='o', alpha=0.5)
    ax[1].scatter(x_circle_spca[y_circle == 0, 0], np.zeros((500, 1)) + 0.02, color='red', marker='^', alpha=0.5)
    ax[1].scatter(x_circle_spca[y_circle == 1, 0], np.zeros((500, 1)) - 0.02, color='blue', marker='o', alpha=0.5)
    ax[0].set_xlabel('pc 1')
    ax[0].set_ylabel('pc 2')
    ax[1].set_ylim([-1, 1])
    ax[1].set_yticks([])
    ax[1].set_xlabel('pc1')
    plt.show()
    # k pca
    x_circle_kpca, _ = rbf_kernel_pca(x_circle, gamma=15, n_components=2)
    plt.figure(6)
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(7, 4))
    ax[0].scatter(x_circle_kpca[y_circle == 0, 0], x_circle_kpca[y_circle == 0, 1], color='red', marker='^', alpha=0.5)
    ax[0].scatter(x_circle_kpca[y_circle == 1, 0], x_circle_kpca[y_circle == 1, 1], color='blue', marker='o', alpha=0.5)
    ax[1].scatter(x_circle_kpca[y_circle == 0, 0], np.zeros((500, 1)) + 0.02, color='red', marker='^', alpha=0.5)
    ax[1].scatter(x_circle_kpca[y_circle == 1, 0], np.zeros((500, 1)) - 0.02, color='blue', marker='o', alpha=0.5)
    ax[0].set_xlabel('pc 1')
    ax[0].set_ylabel('pc 2')
    ax[1].set_ylim([-1, 1])
    ax[1].set_yticks([])
    ax[1].set_xlabel('pc1')
    plt.show()

    # 新的rbf核
    x_moon, y_moon = datasets.make_moons(n_samples=100, random_state=123)
    alphas, lambdas = rbf_kernel_pca(x_moon, gamma=15, n_components=1)
    x_new = x_moon[25]
    x_moon_proj = alphas[25]  # original projection


    def project_x(x_new, x, gamma, alphas, lambdas):
        pair_dist = np.array([np.sum(x_new - row) ** 2 for row in x])
        k = np.exp(-gamma * pair_dist)
        return k.dot(alphas / lambdas)


    x_moon_proj_re = project_x(x_new, x_moon, gamma=15, alphas=alphas, lambdas=lambdas)
    plt.figure(7)
    plt.scatter(alphas[y_moon == 0, 0], np.zeros((50)), color='red', marker='^', alpha=0.5)
    plt.scatter(alphas[y_moon == 1, 0], np.zeros((50)), color='blue', marker='o', alpha=0.5)
    plt.scatter(x_moon_proj, 0, color='black', marker='^', s=100, label='original projection of point x[25]')
    plt.scatter(x_moon_proj_re, 0, color='green', marker='x', s=500, label='remapped point x[25]')
    plt.legend(scatterpoints=1)
    plt.show()
