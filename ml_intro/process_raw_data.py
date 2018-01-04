from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder
import pandas as pd
from io import StringIO
import numpy as np

__author__ = 'wangj'
__date__ = '2017/12/27 20:24'
__doc__ = '''
数据预处理，构建模型
'''


def process_raw_data():
    csv_data = '''
    A,B,C,D
    1.0,2.0,3.0,4.0
    5.0,6.0,,8.0
    0.0,11.0,12.0,
    '''
    df = pd.read_csv(StringIO(csv_data))
    print(df)
    imr = Imputer(missing_values='NaN', strategy='mean', axis=1)
    imr = imr.fit(df)
    imputed_data = imr.transform(df.values)
    print(imputed_data)


def process_raw_label():
    df = pd.DataFrame([
        ['green', 'M', 10.1, 'class1'],
        ['red', 'L', 13.5, 'class2'],
        ['blue', 'XL', 15.3, 'class1']
    ])
    df.columns = ['color', 'size', 'price', 'classlabel']
    print(df)
    size_mapping = {
        'XL': 3,
        'L': 2,
        'M': 1
    }
    df['size'] = df['size'].map(size_mapping)
    print(df)
    class_mapping = {label: idx for idx, label in enumerate(np.unique(df['classlabel']))}
    print(class_mapping)
    df['classlabel'] = df['classlabel'].map(class_mapping)
    print(df)
    # inv
    inv_class_mapping = {v: k for k, v in class_mapping.items()}
    df['classlabel'] = df['classlabel'].map(inv_class_mapping)
    print(df)
    class_le = LabelEncoder()
    y = class_le.fit_transform(df['classlabel'].values)
    print(y)
    x = df[['color', 'size', 'price']].values
    print(x)
    color_le = LabelEncoder()
    x[:, 0] = color_le.fit_transform(x[:, 0])
    print('label encoder\n', x)
    ohe = OneHotEncoder(categorical_features=[0], sparse=False)
    x = ohe.fit_transform(x)
    print(x)
    print(pd.get_dummies(df[['price', 'color', 'size']]))


if __name__ == '__main__':
    # process_raw_data()
    process_raw_label()
