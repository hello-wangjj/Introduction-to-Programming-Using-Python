#!python3
# -*- coding: utf-8 -*-
from itertools import chain
from random import randint

__author__ = 'wangjj'
__mtime__ = '2016122123:38'
__doc__ = '''
如何在一个for循环中迭代多个可迭代对象
并行：使用zip
串行：使用标准库中的itertools.chain
'''
# 某年级4个班 ，成绩存储在4个列表里面，依次迭代每个列表，统计高于90份的人数
# print(help(chain))
for x in chain([1, 2, 3], ['a', 'b', 'c']):
    print(x)
c1 = [randint(60, 100) for i in range(60)]
c2 = [randint(60, 100) for i in range(50)]
c3 = [randint(60, 100) for i in range(40)]
c4 = [randint(60, 100) for i in range(30)]
count = 0
for i in chain(c1, c2, c3, c4):
    if i > 90:
        count += 1
print(count)
