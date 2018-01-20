import pandas as pd
import csv
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import SGDClassifier
import pyprind
import numpy as np
import os
import pickle

__author__ = 'wangj'
__date__ = '2018/01/19 19:06'


def main():
    pass


def stream_docs(path):
    with open(path, 'r') as file:
        next(file)  # skip header
        reader = csv.reader(file)
        for line in reader:
            text, label = line[0], line[1]
            yield text, label
            # yield line


# 处理原来cleaned_IMDB数据
def read_data(path):
    df = pd.read_csv(path)
    df.drop(columns=['id'], inplace=True)
    return df


def get_minibatch(doc_stream, size):
    docs, y = [], []
    try:
        for _ in range(size):
            text, label = next(doc_stream)
            docs.append(text)
            y.append(int(label))
    except StopIteration:
        return None, None
    return docs, y


if __name__ == '__main__':
    # 去除原来的index
    # df = read_data(path='./cleaned_IMDB.csv')
    # df.to_csv('cleaned_IMDB_data.csv', index=False)
    # 新的读取数据
    # next(stream_docs(path='./cleaned_IMDB_data.csv'))
    vect = HashingVectorizer(decode_error='ignore', n_features=2 ** 21, preprocessor=None)
    doc_stream = stream_docs(path='./cleaned_IMDB_data.csv')
    clf = SGDClassifier(loss='log', random_state=1)
    pbar = pyprind.ProgBar(45)
    classes = np.array([0, 1])
    for _ in range(45):
        X_train, y_train = get_minibatch(doc_stream, size=1000)
        if not X_train:
            break
        X_train = vect.transform(X_train)
        clf.partial_fit(X_train, y_train, classes=classes)
        pbar.update()
    X_test, y_test = get_minibatch(doc_stream, size=5000)
    X_test = vect.transform(X_test)
    print('Accuracy: {0:.3f}'.format(clf.score(X_test, y_test)))
    dest = os.path.join('movieclassifier', 'pkl_objects')
    if not os.path.exists(dest):
        os.makedirs(dest)
    pickle.dump(clf, open(os.path.join(dest, 'classifier.pkl'), 'wb'), protocol=4)
