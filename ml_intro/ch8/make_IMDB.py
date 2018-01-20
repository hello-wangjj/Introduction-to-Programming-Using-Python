import pyprind
import pandas as pd
import os
import numpy as np

__author__ = 'wangj'
__date__ = '2018/01/19 01:11'


def main():
    pass


if __name__ == '__main__':
    pbar = pyprind.ProgBar(50000)
    df = pd.DataFrame()
    labels = {'pos': 1, 'neg': 0}
    for s in ('test', 'train'):
        for l in ('pos', 'neg'):
            path = './IMDB/{}/{}'.format(s, l)
            for file in os.listdir(path):
                with open(os.path.join(path, file), 'r', errors='ignore', encoding='utf8') as infile:
                    txt = infile.read()
                df = df.append([[txt, labels[l]]], ignore_index=True)
                pbar.update()
    df.columns = ['review', 'sentiment']
    # df.to_csv('IMDB.csv', index_label='id')
    np.random.seed(0)
    df = df.reindex(np.random.permutation(df.index))
    df.to_csv('IMDB_Data.csv', index=False)
