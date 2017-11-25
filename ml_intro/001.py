from matplotlib import pyplot as plt
import numpy as np
from sklearn import datasets
import pandas as pd
iris = datasets.load_iris()
# print(iris.data)
# print(iris.target)
x = iris.data
y = iris.target
print(x.shape)
plt.scatter(x[:50,0],x[:50,1],color='red',marker='o',label='setosa')
plt.scatter(x[50:100,0],x[50:100,1],color='blue',marker='x',label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc='upper left')
plt.show()
