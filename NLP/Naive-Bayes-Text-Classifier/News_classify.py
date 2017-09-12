import os
import random
import jieba
import sklearn
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import nltk
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier

__author__ = 'wangj'
__date__ = '2017/09/01 16:22'


# 粗暴的词去重,词袋
def make_word_set(words_file):
    words_set = set()
    with open(words_file, 'r', encoding='utf8', errors='ignore') as fp:
        for line in fp.readlines():
            word = line.strip()
            if len(word) > 0 and word not in words_set:  # 去重
                words_set.add(word)
    return words_set


# 文本处理，也就是样本生成过程
def text_processing(folder_path, test_size=0.2):
    folder_list = os.listdir(folder_path)
    # 特征
    data_list = []
    # 标签
    class_list = []

    # 遍历文件夹
    for folder in folder_list:
        new_folder_path = os.path.join(folder_path, folder)
        files = os.listdir(new_folder_path)
        # 读取文件
        j = 1
        for file in files:
            if j > 100:  # 怕内存爆掉，只取100个样本文件，你可以注释掉取完
                break
            with open(os.path.join(new_folder_path, file), 'r', encoding='utf8', errors='ignore') as fp:
                raw = fp.read()
            # jieba中文分词
            # 开启并行分词模式，参数为并行进程数，不支持windows
            # jieba.enable_parallel(4)
            word_cut = jieba.cut(raw, cut_all=False)  # 精确模式，返回的结构是一个可迭代的Generator
            word_list = list(word_cut)  # Generator转化为list，每个词unicode格式
            # 关闭并行分词模式
            # jieba.disable_parallel()

            # 训练集list
            data_list.append(word_list)
            class_list.append(folder)  # 类别
            j += 1

    # 粗暴地划分训练集和测试集
    data_class_list = list(zip(data_list, class_list))
    # 乱序
    random.shuffle(data_class_list)
    # 划分测试集和训练集
    index = int(len(data_class_list) * test_size) + 1
    train_list = data_class_list[index:]
    test_list = data_class_list[:index]
    train_data_list, train_class_list = list(zip(*train_list))
    test_data_list, test_class_list = list(zip(*test_list))

    # 其实可以用sklearn自带的部分做
    # train_data_list, test_data_list, train_class_list, test_class_list = sklearn.cross_validation.train_test_split(data_list, class_list, test_size=test_size)

    # 统计词频放入all_words_dict
    all_words_dict = {}
    for word_list in train_data_list:
        for word in word_list:
            if word in all_words_dict:
                all_words_dict[word] += 1
            else:
                all_words_dict[word] = 1

    # key函数利用词频进行降序排序
    all_words_tuple_list = sorted(all_words_dict.items(), key=lambda f: f[1], reverse=True)  # 内建函数sorted参数需为list
    all_words_list = list(list(zip(*all_words_tuple_list))[0])

    return all_words_list, train_data_list, test_data_list, train_class_list, test_class_list


def words_dict(all_words_list, deleteN, stopwords_set=set()):
    '''
    :param all_words_list: 统计词频
    :param deleteN: 特征词数目
    :param stopwords_set: 停用词
    :return:
    '''
    # 选取特征词
    feature_words = []
    n = 1
    for t in range(deleteN, len(all_words_list), 1):
        if n > 1000:  # feature_words的维度1000
            break

        if not all_words_list[t].isdigit() and all_words_list[t] not in stopwords_set and 1 < len(
                all_words_list[t]) < 5:
            feature_words.append(all_words_list[t])
            n += 1
    return feature_words


# 文本特征
def text_features(train_data_list, test_data_list, feature_words, flag='nltk'):

    def text_feature(text, feature_words_):
        text_words = set(text)

        if flag == 'nltk':
            # nltk特征 dict
            features = {word: 1 if word in text_words else 0 for word in feature_words_}
        elif flag == 'sklearn':
            # sklearn特征 list
            features = [1 if word in text_words else 0 for word in feature_words_]
        else:
            features = []
        return features

    train_feature_list = [text_feature(text, feature_words) for text in train_data_list]
    test_feature_list = [text_feature(text, feature_words) for text in test_data_list]
    return train_feature_list, test_feature_list


# 分类，同时输出准确率等
def text_classifier(train_feature_list, test_feature_list, train_class_list, test_class_list, flag='nltk'):
    # -----------------------------------------------------------------------------------
    if flag == 'nltk':
        # 使用nltk分类器
        train_flist = list(zip(train_feature_list, train_class_list))
        test_flist = list(zip(test_feature_list, test_class_list))
        classifier = nltk.classify.NaiveBayesClassifier.train(train_flist)
        test_accuracy = nltk.classify.accuracy(classifier, test_flist)
    elif flag == 'sklearn':
        # sklearn分类器
        classifier = MultinomialNB().fit(train_feature_list, train_class_list)
        test_accuracy = classifier.score(test_feature_list, test_class_list)
        # svm
        # clf = OneVsRestClassifier(SVC(kernel='linear'))
        # clf.fit(train_feature_list, train_class_list)
        # test_accuracy = clf.score(test_feature_list, test_class_list)

    else:
        test_accuracy = []
    return test_accuracy


def main():
    print('start')
    path = os.path.dirname(__file__)
    # 文本预处理
    folder_path = path + '/Database/SogouC/Sample'
    all_words_list, train_data_list, test_data_list, train_class_list, test_class_list = text_processing(folder_path,
                                                                                                         test_size=0.2)

    # 生成stopwords_set
    stopwords_file = path + '/stop_words_cn.txt'
    stopwords_set = make_word_set(stopwords_file)

    # 文本特征提取和分类
    # flag = 'nltk'
    flag = 'sklearn'
    deleteNs = range(0, 1000, 20)
    test_accuracy_list = []
    for deleteN in deleteNs:
        # feature_words = words_dict(all_words_list, deleteN)
        feature_words = words_dict(all_words_list, deleteN, stopwords_set)
        train_feature_list, test_feature_list = text_features(train_data_list, test_data_list, feature_words, flag)
        test_accuracy = text_classifier(train_feature_list, test_feature_list, train_class_list, test_class_list, flag)
        test_accuracy_list.append(test_accuracy)
    print(test_accuracy_list)

    # 结果评价
    # plt.figure()
    plt.plot(deleteNs, test_accuracy_list)
    plt.title('Relationship of deleteNs and test_accuracy')
    plt.xlabel('deleteNs')
    plt.ylabel('test_accuracy')
    plt.show()
    # plt.savefig('result.png')

    print('finished')


if __name__ == '__main__':
    main()
