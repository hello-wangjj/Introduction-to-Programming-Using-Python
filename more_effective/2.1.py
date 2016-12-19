#!python3
# -*- coding: utf-8 -*-
from random import randint, sample

__author__ = 'wangjj'
__mtime__ = '2016121822:38'
'''
在列表，字典，集合根据条件筛选数据
'''

ls = [randint(-10, 10) for i in range(10)]
print(ls)
# one filter
new_ls = filter(lambda x: x > 0, ls)
print(new_ls)
# 列表解析式
new_ls2 = [x for x in ls if x > 0]
print(new_ls2)

# 字典
d = {x: randint(0, 100) for x in range(1, 21)}
print(d)
new_d = {k: v for k, v in d.items() if v > 90}
print(new_d)
# 集合
s = set(ls)
new_s = {x for x in s if x % 3 == 0}
print(new_s)