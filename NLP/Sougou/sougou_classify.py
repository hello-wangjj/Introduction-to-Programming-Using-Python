import os
import jieba
import chardet
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

__author__ = 'wangj'
__date__ = '2017/09/03 21:09'
base_path = os.path.dirname(__file__)
data_base = '/'.join(base_path.split('/')[:-1]) + '/Database/SogouC/ClassFile'
seg_base = '/'.join(base_path.split('/')[:-1]) + '/Database/SogouCut'


# 停用词表
def stop_word_list():
    file_path = base_path + '/stop_words_ch.txt'
    stop_words_list = []
    with open(file_path, 'r', encoding='utf8', errors='ignore') as f:
        for line in f.readlines():
            stop_words_list.append(line.strip())
    return stop_words_list


# 读取原始文件
def read_file(file):
    read_byte = min(1024, os.path.getsize(file))
    raw = open(file, 'rb')
    ct = raw.read(read_byte)
    result = chardet.detect(ct)
    raw.close()
    encoding = result['encoding']
    with open(file, 'r', encoding=encoding, errors='ignore') as f:
        content = f.read()
    return content


# 存储 处理过的文件
def save_file(file_path, content):
    folder = '/'.join(file_path.split('/')[:-1])
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(file_path, 'w', encoding='utf8') as f:
        f.write(content)


# 去重
def make_word_set(words):
    words_set = set()
    for word in words:
        if len(word) > 0 and word not in words_set:  # 去重
            words_set.add(word)
    return words_set


# 去停用词
def remove_stop_word(content, stop_words):
    new_content = []
    for word in content:
        if word.strip() not in stop_words and word.strip() != 'nbsp':
            new_content.append(word)
    return new_content


# 文本处理,分词，存储处理后的数据
def raw_text_process(folder_path, stop_words):
    folder_list = os.listdir(folder_path)
    # 遍历文件夹
    for folder in folder_list:
        # 拼全路径
        new_folder = os.path.join(folder_path, folder)
        # 文件名列表
        files = os.listdir(new_folder)
        for file in files:
            # 文件路径
            file_path = os.path.join(new_folder, file)
            content = read_file(file_path).strip()
            word_cut = jieba.cut(content, cut_all=False)
            word_cut = list(word_cut)
            content = remove_stop_word(word_cut, stop_words=stop_words)
            content = ' '.join(content)
            # 保存路径
            save_file(seg_base + '/' + folder + '/' + file, content)
    print('save success')


# 文本处理，也就是样本生成过程
def make_data_set(folder_path, test_size=0.2):
    folder_list = os.listdir(folder_path)
    data_list = []
    class_list = []
    for folder in folder_list:
        # 拼全路径
        new_folder = os.path.join(folder_path, folder)
        # 文件名列表
        files = os.listdir(new_folder)
        for file in files:
            # 文件路径
            file_path = os.path.join(new_folder, file)
            content = read_file(file_path).strip()
            # 数据集
            data_list.append(content)
            class_list.append(folder)  # 类别
    # # 划分训练集和测试集
    # train_data_list, test_data_list, train_class_list, test_class_list = train_test_split(data_list, class_list,
    #                                                                                       test_size=test_size,
    #                                                                                       random_state=1)
    return data_list, class_list


def main():
    stop_words = stop_word_list()
    # raw_text_process(data_base, stop_words)
    # print(stop_words)
    data_list, class_list = make_data_set(seg_base, test_size=0.2)
    vectorizer = CountVectorizer(max_features=1000)
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(data_list))
    feature_list = tfidf.toarray()
    # 划分训练集和测试集
    train_data_list, test_data_list, train_class_list, test_class_list = train_test_split(feature_list, class_list,
                                                                                          test_size=0.2,
                                                                                          random_state=1)
    clf = MultinomialNB().fit(train_data_list, train_class_list)
    print(clf.score(test_data_list, test_class_list))


if __name__ == '__main__':
    main()
