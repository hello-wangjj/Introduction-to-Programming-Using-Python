import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve, train_test_split, validation_curve
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import numpy as np

__author__ = 'wangj'
__date__ = '2018/01/14 00:19'


def main():
    pass


if __name__ == '__main__':
    df = datasets.load_breast_cancer()
    x = df.data
    y = df.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    pipe_lr = Pipeline([('sc1', StandardScaler()), ('clf', LogisticRegression(penalty='l2', random_state=0))])
    train_size, train_score, test_score = learning_curve(estimator=pipe_lr, X=x_train, y=y_train,
                                                         train_sizes=np.linspace(0.1, 1, 10), cv=10, n_jobs=-1)
    train_mean = np.mean(train_score, axis=1)
    train_std = np.std(train_score, axis=1)
    test_mean = np.mean(test_score, axis=1)
    test_std = np.std(test_score, axis=1)
    plt.figure(1)
    plt.plot(train_size, train_mean, color='blue', marker='o', markersize=5, label='training accuracy')
    plt.fill_between(train_size, train_mean + train_std, train_mean - train_std, alpha=0.15, color='blue')
    plt.plot(train_size, test_mean, color='green', linestyle='--', marker='s', markersize=5, label='validate accuracy')
    plt.fill_between(train_size, test_mean + test_std, test_mean - test_std, alpha=0.15, color='green')
    plt.grid()
    plt.legend(loc='best')
    plt.ylim([0.8, 1.0])
    plt.show()
    # 验证曲线
    # estimator.get_params().keys() 获取模型参数
    param_range = [0.001, 0.01, 0.1, 1, 10.0, 100.0]
    train_score_validate, test_score_validate = validation_curve(estimator=pipe_lr, X=x_train, y=y_train,
                                                                 param_name='clf__C', param_range=param_range, cv=10)
    train_mean_validate = np.mean(train_score_validate, axis=1)
    train_std_validate = np.std(train_score_validate, axis=1)
    test_mean_validate = np.mean(test_score_validate, axis=1)
    test_std_validate = np.std(test_score_validate, axis=1)
    plt.figure(2)
    plt.plot(param_range, train_mean_validate, color='blue', marker='o', markersize=5, label='training accuracy')
    plt.fill_between(param_range, train_mean_validate + train_std_validate, train_mean_validate - train_std_validate,
                     alpha=0.15, color='blue')
    plt.plot(param_range, test_mean_validate, color='green', marker='s', linestyle='--', markersize=5,
             label='validate accuracy')
    plt.fill_between(param_range, test_mean_validate + test_std_validate, test_mean_validate - test_std_validate,
                     alpha=0.15, color='green')
    plt.grid()
    plt.xscale('log')
    plt.legend(loc='best')
    plt.xlabel('param C')
    plt.ylabel('accuracy')
    plt.ylim([0.8, 1])
    plt.show()
