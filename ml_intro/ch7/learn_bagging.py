from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

__author__ = 'wangj'
__date__ = '2018/01/17 20:46'


def main():
    pass


if __name__ == '__main__':
    wine = datasets.load_wine()
    X = wine.data
    y = wine.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)
    tree = DecisionTreeClassifier(criterion='entropy', max_depth=None)
    bag = BaggingClassifier(base_estimator=tree, n_estimators=500, max_samples=1.0, max_features=1.0, bootstrap=True,
                            bootstrap_features=False, n_jobs=-1, random_state=1)

    tree.fit(X_train, y_train)
    y_train_pred = tree.predict(X_train)
    y_test_pred = tree.predict(X_test)
    tree_train = accuracy_score(y_true=y_train, y_pred=y_train_pred)
    tree_test = accuracy_score(y_true=y_test, y_pred=y_test_pred)
    print("Decision tree train/test accuracy {0:.3f}/{1:.3f}".format(tree_train, tree_test))
    bag.fit(X_train, y_train)
    y_train_pred_bag = bag.predict(X_train)
    y_test_pred_bag = bag.predict(X_test)
    bag_train = accuracy_score(y_true=y_train, y_pred=y_train_pred_bag)
    bag_test = accuracy_score(y_true=y_test, y_pred=y_test_pred_bag)
    print("Bagging train/test accuracy {0:.3f}/{1:.3f}".format(bag_train, bag_test))
    x_min = X_train[:, 0].min() - 1
    x_max = X_train[:, 0].max() + 1
    y_min = X_train[:, 1].min() - 1
    y_max = X_train[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
    f, axarr = plt.subplots(nrows=1, ncols=2, sharex='col', sharey='row', figsize=(8, 3))
    for idx, clf, tt in zip([0, 1], [tree, bag], ['Decision Tree', 'Bagging']):
        clf.fit(X_train[:, 0:2], y_train)
        z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
        z = z.reshape(xx.shape)
        axarr[idx].contourf(xx, yy, z, alpha=0.3)
        axarr[idx].scatter(X_train[y_train == 0, 0], X_train[y_train == 0, 1], c='blue', marker='^')
        axarr[idx].scatter(X_train[y_train == 1, 0], X_train[y_train == 1, 1], c='blue', marker='o')
        axarr[idx].set_title(tt)
    axarr[0].set_ylabel('Alcohol', fontsize=12)
    plt.text(10.2, -1.2, s='Hue', ha='center', va='center', fontsize=12)
    plt.show()

    # adaboost
    ada = AdaBoostClassifier(base_estimator=tree, n_estimators=500, learning_rate=0.1, random_state=0)
    ada.fit(X_train, y_train)
    y_train_pred_ada = ada.predict(X_train)
    y_test_pred_ada = ada.predict(X_test)
    ada_train = accuracy_score(y_train, y_train_pred_ada)
    ada_test = accuracy_score(y_test, y_test_pred_ada)
    print("adaboost train/test accuracy {0:.3f}/{1:.3f}".format(ada_train, ada_test))
