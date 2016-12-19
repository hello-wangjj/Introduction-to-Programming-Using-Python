#!python3
# -*- coding: utf-8 -*-
from random import randint
__author__ = 'wangjj'
__mtime__ = '2016121915:44'
'''
字典根据value排序
'''
d = {x: randint(60, 100) for x in 'abcxyz'}
print(d)
print(sorted(d))
print(sorted(d.items(), key=lambda v: v[1], reverse=True))
