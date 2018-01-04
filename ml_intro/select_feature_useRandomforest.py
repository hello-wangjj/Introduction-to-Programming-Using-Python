from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

__author__ = 'wangj'
__date__ = '2018/01/04 00:52'
__doc__ = '''
使用RandomForest选择特征
'''

if __name__ == '__main__':
    wine = datasets.load_wine()
    x = wine.data
    y = wine.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    stdsc = StandardScaler()
    x_train_std = stdsc.fit_transform(x_train)
    x_test_std = stdsc.transform(x_test)
    feature_names = wine.feature_names
    forest = RandomForestClassifier(n_estimators=10, random_state=0, n_jobs=-1)
    forest.fit(x_train_std, y_train)
    importances = forest.feature_importances_
    indices = np.argsort(importances)[::-1]
    for f in range(x_train_std.shape[1]):
        print('{0:<3}{1:30}{2}'.format(f + 1, feature_names[f], importances[indices[f]]))
    plt.title('Feature Importance')
    plt.bar(range(x_train_std.shape[1]), importances[indices], color='lightblue', align='center')
    plt.xticks(range(x_train_std.shape[1]), feature_names, rotation=90)
    plt.xlim([-1, x_train_std.shape[1]])
    plt.tight_layout()
    plt.show()
