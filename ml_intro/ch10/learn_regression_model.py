from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

__author__ = 'wangj'
__date__ = '2018/01/20 23:22'


def main():
    pass


if __name__ == '__main__':
    sns.set(style='whitegrid', context='notebook')
    cols = ['LSTAT', 'INDUS', 'NOX', 'RM', 'MEDV']
    boston = datasets.load_boston()
    feature_mat = np.array(boston.data)
    target_mat = np.array(boston.target).reshape(506, 1)
    # print(feature_mat.shape, target_mat.shape)
    data = np.hstack((feature_mat, target_mat))
    df = pd.DataFrame(data, columns=np.append(boston.feature_names, 'MEDV'))
    cols = ['LSTAT', 'INDUS', 'NOX', 'RM', 'MEDV']
    plt.figure(1)
    sns.pairplot(df[cols], size=2.5)
    plt.show()
    cm = np.corrcoef(df[cols].values.T)
    plt.figure(2)
    sns.set(font_scale=1.5)
    hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size':15}, yticklabels=cols,xticklabels=cols)
    plt.show()