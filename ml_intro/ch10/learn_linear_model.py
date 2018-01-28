import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, RANSACRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import Ridge, Lasso, ElasticNet

__author__ = 'wangj'
__date__ = '2018/01/22 01:39'


def main():
    pass


class LinearRegressionGD(object):
    def __init__(self, eta=0.001, n_iter=20):
        self.eta = eta
        self.n_iter = n_iter
        self.w_ = None
        self.cost_ = None

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1]).reshape(-1, 1)
        self.cost_ = []

        for i in range(self.n_iter):
            output = self.net_input(X).reshape(506, 1)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors ** 2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        # x 506x1,w_[1:] 1,
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return self.net_input(X)


def line_regplot(X, y, model):
    plt.scatter(X, y, c='blue')
    plt.plot(X, model.predict(X), color='red')
    return None


if __name__ == '__main__':
    boston = datasets.load_boston()
    feature_mat = np.array(boston.data)
    target_mat = np.array(boston.target).reshape(506, 1)
    sc_x = StandardScaler()
    X = feature_mat[:, 5].reshape(-1, 1)
    y = target_mat
    sc_y = StandardScaler()
    X_std = sc_x.fit_transform(X)
    y_std = sc_y.fit_transform(y)
    lr = LinearRegressionGD()
    lr.fit(X_std, y_std)
    plt.figure(1)
    plt.plot(range(1, lr.n_iter + 1), lr.cost_)
    plt.ylabel('SSE')
    plt.xlabel('Epoch')
    plt.show()
    plt.figure(2)
    line_regplot(X_std, y_std, lr)
    plt.xlabel('average number of rooms (RM) (standardized) ')
    plt.ylabel('Price in $1000\'s (MRDV) (standardized)')
    plt.show()

    # sklearn linear model
    slr = LinearRegression()
    slr.fit(X, y)
    print(' Slop: {0:.3f}'.format(float(slr.coef_[0])))
    print('Intercept: {0:.3f}'.format(float(slr.intercept_)))
    plt.figure(3)
    line_regplot(X, y, slr)
    plt.xlabel('average number of rooms (RM) (standardized) ')
    plt.ylabel('Price in $1000\'s (MRDV) (standardized)')
    plt.show()
    ransac = RANSACRegressor(LinearRegression(), max_trials=100, min_samples=50, loss='absolute_loss',
                             residual_threshold=5, random_state=0)
    ransac.fit(X, y)
    inlier_mask = ransac.inlier_mask_
    outlier_mask = np.logical_not(inlier_mask)
    line_X = np.arange(3, 10, 1)
    line_y_ransac = ransac.predict(line_X[:, np.newaxis])
    plt.figure(4)
    plt.scatter(X[inlier_mask], y[inlier_mask], c='blue', marker='o', label='Inliers')
    plt.scatter(X[outlier_mask], y[outlier_mask], c='lightgreen', marker='s', label='Outliers')
    plt.plot(line_X, line_y_ransac, color='red')
    plt.xlabel('average number of rooms (RM) (standardized) ')
    plt.ylabel('Price in $1000\'s (MRDV) (standardized)')
    plt.legend(loc='upper left')
    plt.show()
    print(' Slop: {0:.3f}'.format(float(ransac.estimator_.coef_[0])))
    print('Intercept: {0:.3f}'.format(float(ransac.estimator_.intercept_)))
    # 评估性能
    x = boston.data
    y = boston.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    slr_2 = LinearRegression()
    slr_2.fit(x, y)
    y_train_pred = slr_2.predict(x_train)
    y_test_pred = slr_2.predict(x_test)
    plt.figure(5)
    plt.scatter(y_train_pred, y_train_pred - y_train, c='blue', marker='o', label='Training Data')
    plt.scatter(y_test_pred, y_test_pred - y_test, c='lightgreen', marker='s', label='Test Data')
    plt.xlabel('Predict values')
    plt.ylabel('Residuals')
    plt.legend(loc='best')
    plt.hlines(y=0, xmin=-10, xmax=50, lw=2, color='red')
    plt.xlim([-10, 50])
    plt.show()
    print('MSE train: {0:.3f},MSE test: {1:.3f}'.format(mean_squared_error(y_train, y_train_pred),
                                                        mean_squared_error(y_test, y_test_pred)))
    print('r2 train: {0:.3f},r2 test: {1:.3f}'.format(r2_score(y_train, y_train_pred), r2_score(y_test, y_test_pred)))
    # 正则化
    ridge = Ridge(alpha=1.0)
    lasso = Lasso(alpha=1.0)
    ela = ElasticNet(alpha=1.0)
    # 曲线化-多项式回归
    # 回归点
    x_p = np.array([258.0, 270.0, 294.0, 320.0, 342.0, 368.0, 396.0, 446.0, 480.0, 586.0])[:, np.newaxis]
    y_p = np.array([236.4, 234.4, 252.8, 298.6, 314.2, 342.2, 360.8, 368.0, 391.2, 390.8])
    # 2个回归模型
    lr_r = LinearRegression()
    pr_r = LinearRegression()
    # 多项式
    quadratic = PolynomialFeatures(degree=2)
    # 转化特征
    X_quad = quadratic.fit_transform(x_p)
    # lr_r
    lr_r.fit(x_p, y_p)
    x_r_fit = np.arange(250, 600, 10)[:, np.newaxis]
    # 线性拟合
    # 线性线
    y_lin_fit = lr_r.predict(x_r_fit)
    # 多项式
    pr_r.fit(X_quad, y_p)
    y_quad_fit = pr_r.predict(quadratic.fit_transform(x_r_fit))
    plt.figure(6)
    plt.scatter(x_p, y_p, label='training points')
    plt.plot(x_r_fit, y_lin_fit, label='linear fit', linestyle='--')
    plt.plot(x_r_fit, y_quad_fit, label='quadratic fit')
    plt.legend(loc='upper left')
    plt.show()
    y_lin_pred = lr_r.predict(x_p)
    y_quad_pred = pr_r.predict(X_quad)
    print('MSE train: {0:.3f},quadratic MSE : {1:.3f}'.format(mean_squared_error(y_p, y_lin_pred),
                                                                  mean_squared_error(y_p, y_quad_pred)))
    print('r2 train: {0:.3f},r2 quadratic: {1:.3f}'.format(r2_score(y_p, y_lin_pred), r2_score(y_p, y_quad_pred)))
