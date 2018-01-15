from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

__author__ = 'wangj'
__date__ = '2018/01/15 18:50'


def main():
    pass


if __name__ == '__main__':
    df = datasets.load_breast_cancer()
    x = df.data
    y = df.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    pipe_svc = Pipeline([('sc1', StandardScaler()), ('clf', SVC(random_state=1))])
    param_range = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
    param_grid = [{'clf__C': param_range,
                   'clf__kernel': ['linear']},
                  {'clf__C': param_range,
                   'clf__gamma': param_range,
                   'clf__kernel': ['rbf']}]
    gs = GridSearchCV(estimator=pipe_svc, param_grid=param_grid, scoring='accuracy', cv=110, n_jobs=-1)
    gs = gs.fit(x_train, y_train)
    print(gs.best_score_)
    print(gs.best_params_)

    # 看下模型
    clf = gs.best_estimator_
    clf.fit(x_train, y_train)
    print('test accuracy:', clf.score(x_test, y_test))
    # 另外可以考虑随机搜索方法
