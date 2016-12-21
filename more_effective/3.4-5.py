#!python3
# -*- coding: utf-8 -*-
from itertools import islice
__author__ = 'wangjj'
__mtime__ = '2016122016:01'
__doc__ = '''
反向迭代器 利用生成器yield
对迭代器 进行切片操作
'''


class FloatRange(object):

    def __init__(self, start, end, step=0.1):
        super(FloatRange, self).__init__()
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step
for x in FloatRange(1.0, 4.0, 0.5):
    print(x)
for x in reversed(FloatRange(1.0, 4.0, 0.5)):
    print(x)

with open('hamlet.txt', 'r') as f:
    print(type(f))
    for line in f:
        print(line)
    f.seek(0)
    print('\n**************************************\n')
    for line in islice(f,10,30):
        print(line)