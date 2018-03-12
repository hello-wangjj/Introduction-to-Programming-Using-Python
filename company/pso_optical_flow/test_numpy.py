import numpy as np
import pandas as pd

__author__ = 'wangj'
__date__ = '2018/02/02 21:50'


def main():
    pass


if __name__ == '__main__':
    arr = np.array([[1, 3, 2, 4, 5],
                    [2, 3, 5, 1, 4]])
    ind = np.argpartition(arr, kth=3, axis=1)
    print(ind)
    arg = np.argmax(arr, axis=1)
    df = pd.DataFrame(arr)

    new_arg = np.array(df.T.apply(np.argsort).T)[:,0:3]
    arg_list = new_arg.tolist()
    for i, j in enumerate(arg_list):
        print(arr[i, j])

