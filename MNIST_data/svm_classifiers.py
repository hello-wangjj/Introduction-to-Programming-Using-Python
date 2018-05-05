from load_data import load_mnist
from sklearn.decomposition import PCA
from sklearn.svm import SVC
import numpy as np

__author__ = 'wangj'
__date__ = '2018/05/01 14:42'

COMPONENT_NUM = 35  # 设置pca降维的维度值

if __name__ == '__main__':
    print('{0}load data{1}'.format('*' * 10, '*' * 10))
    X_train, y_train = load_mnist('E:\document\mnist', kind='train')
    X_test, y_test = load_mnist('E:\document\mnist', kind='t10k')
    print('X_train.shape:{0},y_train.shape:{1}'.format(X_train.shape, y_train.shape))
    print('X_test.shape:{0},y_test.shape:{1}'.format(X_test.shape, y_test.shape))
    print('{0}load success{1}'.format('*' * 10, '*' * 10))

    # pca 降维
    pca = PCA(n_components=COMPONENT_NUM, whiten=True)
    pca.fit(X_train) # Fit the model with X
    X_train = pca.transform(X_train) # Fit the model with X and 在X上完成降维.
    # 降维之后的维度
    print('X_train.shape:{0}'.format(X_train.shape))

    print('start svm')
    svc = SVC()
    svc.fit(X_train, y_train)

    # 测试
    X_test = pca.transform(X_test)
    y_predict = svc.predict(X_test)

