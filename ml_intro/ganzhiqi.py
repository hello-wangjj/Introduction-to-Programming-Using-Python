import numpy as np

__author__ = 'wangj'
__date__ = '2017/11/27 00:25'


class Perceptron(object):
    """
    @:parameter
    eta: float, learning rate
    n_iter: int
    @:arg
    w_: 1d-array,weights after fitting
    errors_: list, number of mis classification in every epoch
    """

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
        self.w_ = None
        self.errors_ = None

    def fit(self, X, y):
        """

        :param X: array-like,shape = [m_samples,n_features],training vector
        :param y: array-like,shape = [m_samples].target
        :return: self: object
        """
        # w.shape = n+1,
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                # update.shape = 1 , xi.shape=1,n
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def predict(self, X):
        """

        :param X:
        :return: class label after unit step
        """
        # print(self.w_)
        return np.where(self.net_input(X) >= 0.0, 1, -1)

    def net_input(self, X):
        """
        calculate net input
        :param X:
        :return:
        """
        return np.dot(X, self.w_[1:]) + self.w_[0]


def main():
    pass


if __name__ == '__main__':
    main()
