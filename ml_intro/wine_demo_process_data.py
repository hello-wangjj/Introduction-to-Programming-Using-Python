from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np

__author__ = 'wangj'
__date__ = '2018/01/01 15:57'

if __name__ == '__main__':
    wine = datasets.load_wine()
    x = wine.data
    y = wine.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    stdsc = StandardScaler()
    x_train_std = stdsc.fit_transform(x_train)
    x_test_std = stdsc.transform(x_test)
    # 逻辑回归L1正则
    lr = LogisticRegression(penalty='l1', C=0.1)
    lr.fit(x_train_std, y_train)
    print('Training accuracy:', lr.score(x_train_std, y_train))
    print('Test accuracy:', lr.score(x_test_std, y_test))
    fig = plt.figure(figsize=(10,5))
    ax = plt.subplot(111)
    colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow',
              'black', 'pink', 'lightgreen', 'lightblue', 'gray',
              'indigo', 'orange']
    weights, params = [], []
    for c in np.arange(-4, 6):
        lr2 = LogisticRegression(penalty='l1', C=np.power(10, float(c)), random_state=0)
        lr2.fit(x_train_std, y_train)
        weights.append(lr2.coef_[1])
        params.append(np.power(10, float(c)))
    weights = np.array(weights)
    for column, color in zip(range(weights.shape[1]), colors):
        plt.plot(params, weights[:, column], label=wine.feature_names[column], color=color)
    plt.axhline(0, color='black', linestyle='--', linewidth=3)
    plt.xlim([10 ** (-5), 10 ** 5])
    plt.ylabel('weight coefficient')
    plt.xlabel('C')
    plt.xscale('log')
    ax.legend(loc='lower left', fancybox=True, ncol=1)
    plt.show()
