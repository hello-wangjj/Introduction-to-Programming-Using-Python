from sklearn import datasets
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import numpy as np

__author__ = 'wangj'
__date__ = '2018/01/11 20:58'

if __name__ == '__main__':
    df = datasets.load_breast_cancer()
    x = df.data
    y = df.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    pipe_lr = Pipeline(
        [('sc1', StandardScaler()), ('pca', PCA(n_components=2)), ('clf', LogisticRegression(random_state=2))])
    pipe_lr.fit(x_train, y_train)
    print('Test Accuracy:{0:.3f}'.format(pipe_lr.score(x_test, y_test)))

    # k折交叉检验
    kfold = StratifiedKFold(n_splits=10, random_state=1)
    scores = []
    for k, (train, test) in enumerate(kfold.split(x_train, y_train)):
        pipe_lr.fit(x_train[train], y_train[train])
        score = pipe_lr.score(x_train[test], y_train[test])
        scores.append(score)
        print('Fold:{0},class dist.:{1}, Acc: {2:.3f}'.format(k + 1, np.bincount(y_train[train]), score))
    score = cross_val_score(estimator=pipe_lr, X=x_train, y=y_train, cv=10, n_jobs=1)
    print('cv accuracy score: {}'.format(score))
    print('cv accuracy: {0:.3f}+/1{1:.3f}'.format(np.mean(score), np.std(score)))
