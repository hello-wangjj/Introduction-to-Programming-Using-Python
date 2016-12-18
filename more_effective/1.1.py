#!python3
# -*- coding: utf-8 -*-
from random import randint, sample
from functools import reduce
__author__ = 'wangjj'
__mtime__ = '201612171:08'
'''
从多个字典中取得公共的键值
'''
s = 'abcdefghi'

s1 = {x: randint(3, 6) for x in sample(s, randint(3, 6))}
s2 = {x: randint(3, 6) for x in sample(s, randint(3, 6))}
s3 = {x: randint(3, 6) for x in sample(s, randint(3, 6))}
print(s1, s2, s3, sep='\n----\n')
# one
res = []
for k in s1.keys():
    if k in s2.keys() and k in s3.keys():
        res.append(k)

# the good one
# map(dict.keys(),[s1,s2,s3])
# reduce
print(reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3])))
