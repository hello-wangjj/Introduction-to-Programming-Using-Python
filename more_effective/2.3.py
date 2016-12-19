#!python3
# -*- coding: utf-8 -*-
from random import randint
from collections import Counter
import re
__author__ = 'wangjj'
__mtime__ = '2016121915:10'
'''
统计序列中元素出现的频度
'''
data = [randint(0, 20) for i in range(30)]
print(data)
c = dict.fromkeys(data, 0)
print(c)
for x in data:
    c[x] += 1
print(c)
# 出现频度最高的3个
new_c = sorted(c.items(), key=lambda x: x[1], reverse=True)
print(new_c)

c1=Counter(data)
print(c1)
print(c1.most_common(3))
'''
英语文章字频统计
'''
with open('hamlet.txt', 'r') as f:
    file=f.read()
    ls=re.split('\W+',file)
    c3=Counter(ls)
    print(c3)
    print(c3.most_common(10))