from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn import model_selection
from sklearn.preprocessing import StandardScaler
from ml_intro.ganzhiqi import Perceptron

__author__ = 'wangj'
__date__ = '2017/11/27 22:22'


def main():
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target
    X = X[:100, :]
    Y = Y[:100]
    Y[:50] = -1

    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.3, random_state=0)
    # 特征标准化处理
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    ppn = Perceptron(n_iter=40, eta=0.1)
    ppn.fit(X_train_std, Y_train)
    y_pred = ppn.predict(X_test_std)
    print('mis classified samples %d' % (Y_test != y_pred).sum())


if __name__ == '__main__':
    main()
