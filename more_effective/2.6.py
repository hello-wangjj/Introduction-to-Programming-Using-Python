#!python3
# -*- coding: utf-8 -*-
from collections import OrderedDict
from random import randint
import time
__author__ = 'wangjj'
__mtime__ = '2016121722:06'
d = {'jim': (1, 35), 'bob': (3, 40), 'leo': (2, 37), 'axx': (4, 50)}
for k in d.keys():
    print(k)

od = OrderedDict()
od['jim'] = (1, 35)
od['leo'] = (2, 37)
od['bob'] = (3, 40)
od['axx'] = (4, 50)
for k in od.keys():
    print(k)

'''
如何让字典保持有序
'''
ord_d = OrderedDict()
players = list('ABCDEFGH')
start = time.time()
for i in range(8):
    input()
    p = players.pop(randint(0, 7 - i))
    end = time.time()
    print(i + 1, p, end - start)
    ord_d[p] = (i + 1, p, end - start)
print('\n-----------\n')
for k in ord_d.keys():
    print(k, ord_d[k])
