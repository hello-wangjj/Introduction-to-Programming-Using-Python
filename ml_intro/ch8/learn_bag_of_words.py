import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
__author__ = 'wangj'
__date__ = '2018/01/18 19:46'


def main():
    pass


if __name__ == '__main__':
    count = CountVectorizer()
    docs = np.array([
        'The sun is shining',
        'The weather is sweet',
        'The sun is shining and the weather is sweet'
    ])
    bag = count.fit_transform(docs)
    tfidf = TfidfTransformer()
    np.set_printoptions(precision=2)
    print(tfidf.fit_transform(count.fit_transform(docs)).toarray())
