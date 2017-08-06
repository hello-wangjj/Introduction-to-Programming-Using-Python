from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
import copy
from sklearn.externals.six import StringIO
import os
print(os.path.dirname(__file__))
dirname = os.path.dirname(__file__)

with open(dirname + '\decisionTree.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    featureList = []
    featureLabelList = []
    for row in reader:
        featureLabelList.append(row[-1])
        rawDict = dict()
        for j in range(1, len(row) - 1):
            rawDict[header[j]] = row[j]
        featureList.append(rawDict)

print(featureLabelList)
print(featureList)

# DictVectorizer
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
print(dummyX)
print(vec.get_feature_names())

lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(featureLabelList)
print(dummyY)

# using decisionTree classification
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX, dummyY)
print('clf:', clf)
with open('decisionTree.dot', 'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

# 转化成pdf文件 dot -Tpdf .\decisionTree.dot -o output.pdf

# 测试预测
oneRowX = dummyX[0, :]
print(oneRowX)
newRowX = copy.deepcopy(oneRowX)
newRowX[0] = 1
newRowX[2] = 0
newRowX = newRowX.reshape(1, -1)
print('newRowX:', newRowX)
print('oneRowX:', oneRowX)
predictedY = clf.predict(newRowX)
print(predictedY)