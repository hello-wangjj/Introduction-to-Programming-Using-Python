from sklearn import datasets
from sklearn import svm
iris = datasets.load_iris()
digits = datasets.load_digits()
# print(digits.data)
# print(digits.target)
clf = svm.SVC()
X, y = iris.data, iris.target
print(clf.fit(X, y))