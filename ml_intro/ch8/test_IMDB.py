import pyprind
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import re
from nltk.stem.porter import PorterStemmer
from bs4 import BeautifulSoup as BS
from nltk.corpus import stopwords

__author__ = 'wangj'
__date__ = '2018/01/18 19:12'


def main():
    pass


def preprocessor(text):
    text = re.sub('<[^>]*>', '', text)
    emotions = re.findall('(?::|;|=)?(?:-})?(?:\)|\(|D|P)?', text)
    text = re.sub('[\W]+', ' ', text.lower()).join(emotions).replace('-', '')
    return text


def tokenizer(text):
    return text.split()


def tokenizer_porter(text):
    return [PorterStemmer.stem(word) for word in text.split()]


# 完成数据处理任务
def review_to_text(review, remove_stopwords):
    # 去掉html标记
    raw_text = BS(review, 'lxml').get_text()
    # 去掉非字母字符
    letters = re.sub('[^a-zA-Z]', ' ', raw_text)
    words = letters.lower().split()
    # 如果stop_words 被激活，则进一步去掉评论中的停用词
    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        # 提取词干
        porter = PorterStemmer()
        words = [porter.stem(w) for w in words if w not in stop_words]

    return words


if __name__ == '__main__':
    data = pd.read_csv('IMDB.csv')
    data = data.reindex(np.random.permutation(data.index))
    data['review'] = data['review'].apply(review_to_text, remove_stopwords=True)
    data.to_csv('cleaned_IMDB.csv', index=False)


