import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

__author__ = 'wangj'
__date__ = '2018/01/19 15:18'


def main():
    pass


if __name__ == '__main__':
    df = pd.read_csv('cleaned_IMDB.csv')
    X_train = df.loc[:25000, 'review'].values
    y_train = df.loc[:25000, 'sentiment'].values
    X_test = df.loc[25000:, 'review'].values
    y_test = df.loc[25000:, 'sentiment'].values
    # 使用GridSearchCV 寻找逻辑斯蒂回归的最佳参数组合
    train = True
    if train:
        tfidf = TfidfVectorizer(strip_accents=None, lowercase=False, preprocessor=None)
        param_grid = [
            {'vect__ngram_range': [(1, 1)],
             'clf__penalty': ['l1', 'l2'],
             'clf__C': [1.0, 10.0, 100.0]
             },
            {
                'vect__ngram_range': [(1, 1)],
                'vect__use_idf': [False],
                'vect__norm': [None],
                'clf__penalty': ['l1', 'l2'],
                'clf__C': [1.0, 10.0, 100.0]
            }
        ]
        lr_tfidf = Pipeline([('vect', tfidf), ('clf', LogisticRegression(random_state=0))])
        gs_lr_tfidf = GridSearchCV(estimator=lr_tfidf, param_grid=param_grid, scoring='accuracy', cv=5, verbose=1,
                                   n_jobs=-1)
        gs_lr_tfidf.fit(X_train, y_train)
        print('Best parameter set:{}'.format(gs_lr_tfidf.best_params_))
        clf = gs_lr_tfidf.best_estimator_
    # Best
    # parameter
    # set: {'clf__penalty': 'l2', 'vect__ngram_range': (1, 1), 'clf__C': 10.0}
    else:
        tfidf = TfidfVectorizer(strip_accents=None, lowercase=False, preprocessor=None, ngram_range=(1, 1))
        clf = Pipeline([('vect', tfidf), ('clf', LogisticRegression(random_state=0, penalty='l2', C=10.0))])
        clf.fit(X_train, y_train)
    print('Test accuracy:{}'.format(clf.score(X_test, y_test)))
