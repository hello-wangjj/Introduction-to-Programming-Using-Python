import sys
import os
from sklearn import metrics
import numpy as np
import pickle
import time
from load_data import load_mnist
from sklearn.decomposition import PCA

__author__ = 'wangj'
__date__ = '2018/05/02 16:04'


def naive_bayes_classifier(X_train, y_train):
    from sklearn.naive_bayes import GaussianNB
    model = GaussianNB()
    model.fit(X_train, y_train)
    return model


def knn_classifier(X_train, y_train):
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier()
    model.fit(X_train, y_train)
    return model


def logistic_regression_classifier(X_train, y_train):
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(penalty='l2')
    model.fit(X_train, y_train)
    return model


def random_forest_classifier(X_train, y_train):
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=8)
    model.fit(X_train, y_train)
    return model


# Decision Tree Classifier
def decision_tree_classifier(X_train, y_train):
    from sklearn import tree
    model = tree.DecisionTreeClassifier()
    model.fit(X_train, y_train)
    return model


# GBDT(Gradient Boosting Decision Tree) Classifier
def gradient_boosting_classifier(X_train, y_train):
    from sklearn.ensemble import GradientBoostingClassifier
    model = GradientBoostingClassifier(n_estimators=200)
    model.fit(X_train, y_train)
    return model


# SVM Classifier
def svm_classifier(X_train, y_train):
    from sklearn.svm import SVC
    model = SVC()
    model.fit(X_train, y_train)
    return model


# SVM Classifier using cross validation
def svm_cross_validation(X_train, y_train):
    from sklearn.model_selection import GridSearchCV
    from sklearn.svm import SVC
    model = SVC()
    param_grid = {'C': [1e-3, 1e-2, 1e-1, 1, 10, 100, 1000], 'gamma': [0.001, 0.0001]}
    grid_search = GridSearchCV(model, param_grid, n_jobs=1, verbose=1)
    grid_search.fit(X_train, y_train)
    best_parameters = grid_search.best_estimator_.get_params()
    for para, val in best_parameters.items():
        print(para, val)
    model = SVC(kernel='rbf', C=best_parameters['C'], gamma=best_parameters['gamma'], probability=True)
    model.fit(X_train, y_train)
    return model


if __name__ == '__main__':
    model_save_file = None
    model_save = {}

    test_classifiers = ['NB', 'KNN', 'LR', 'RF', 'DT', 'SVM', 'GBDT']
    classifiers = {'NB': naive_bayes_classifier,
                   'KNN': knn_classifier,
                   'LR': logistic_regression_classifier,
                   'RF': random_forest_classifier,
                   'DT': decision_tree_classifier,
                   'SVM': svm_classifier,
                   'SVMCV': svm_cross_validation,
                   'GBDT': gradient_boosting_classifier
                   }
    print('reading training and testing data...')
    X_train, y_train = load_mnist('E:\document\mnist', kind='train')
    X_test, y_test = load_mnist('E:\document\mnist', kind='t10k')
    num_train, num_feature = X_train.shape
    num_test, num_feature_y = X_test.shape
    is_binary_class = (len(np.unique(y_train)) == 2)
    print('data info *********************')
    print('#training data: {0}, #testing_data: {1}, dimension: {2}'.format(num_train, num_test, num_feature))
    COMPONENT_NUM = 35
    # pca 降维
    print('----------------------------PCA-------------------')
    pca = PCA(n_components=COMPONENT_NUM)
    pca.fit(X_train)  # Fit the model with X
    X_train = pca.transform(X_train)  # Fit the model with X and 在X上完成降维.
    X_test = pca.transform(X_test)

    for classifier in test_classifiers:
        print('--------------------------{0}----------------'.format(classifier))
        start_time = time.time()
        model = classifiers[classifier](X_train, y_train)
        print('training take {0}s!'.format(time.time() - start_time))
        predict = model.predict(X_test)
        if model_save_file is not None:
            model_save[classifier] = model
        if is_binary_class:
            precision = metrics.precision_score(y_test, predict)
            recall = metrics.recall_score(y_test, predict)
            print('precision: {0:.2f}%, recall: {1:.2f}%'.format(100 * precision, 100 * recall))
        accuracy = metrics.accuracy_score(y_test, predict)
        print('accuracy: {0:.2f}%'.format(100 * accuracy))
        if model_save_file is not None:
            pickle.dump(model_save, open(model_save_file, 'wb'))
