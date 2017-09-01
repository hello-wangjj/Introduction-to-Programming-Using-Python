import jieba.analyse
import os
from collections import Counter
__author__ = 'wangj'
__date__ = '2017/09/01 10:06'
path = os.path.dirname(__file__)
train_path = '/'.join(path.split('/')[:-1]) + '/data/training.csv'
jieba.analyse.set_stop_words('stop_words_ch.txt')
s = '根据《上市公司行业分类指引》（2012年修订），公司所属行业为其他金融业（J69）；根据《国民经济行业分类》（GB/T4754-2011），公司所属行业为其他金融业（J69）；根据《挂牌公司管理型行业分类指引》（股转系统公告〔2015〕23号），公司所属行业为资本投资服务（J6740）；根据《挂牌公司投资型行业分类指引》（股转系统公告〔2015〕23号），公司所属行业为私募基金管理人（16111013）。自成立以来，公司长期专注于房地产行业及相关领域的投资管理，积累了丰富的投资经验，兼具相当的分析判断和管理能力，成为了房地产行业及相关领域具有成功投资经验的专家。目前，公司存在自有资产管理、受托资产管理、投资顾问服务、不动产经营管理等业务。报告期内，主营业务未发生重大变化。'


def main():
    tags = jieba.analyse.extract_tags(s, 20)
    print(tags)


def stop_words():
    stop_words_file = open('stop_words_ch.txt', 'r', encoding='utf8', errors='ignore')
    stop_words_list = []
    for line in stop_words_file.readlines():
        stop_words_list.append(line.strip())
    return stop_words_list


# 结巴分词
def jieba_fenci_raw(raw):
    word_list = list(jieba.cut(raw, cut_all=False))
    word_list = dict(Counter(word_list))
    word_list = sorted(word_list.items(), key=lambda f: f[1], reverse=True)
    return word_list


def jieba_fenci(raw, stop_word_list):
    word_list = list(jieba.cut(raw, cut_all=False))
    word_list = [word.strip() for word in word_list if word not in stop_word_list]
    word_list = dict(Counter(word_list))
    word_list = sorted(word_list.items(), key=lambda f: f[1], reverse=True)
    return word_list


if __name__ == '__main__':
    main()
    stop_words_list = stop_words()
    print(stop_words_list)
    print(jieba_fenci_raw(s))
    print(jieba_fenci(s, stop_words_list))
