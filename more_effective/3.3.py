#!python3
# -*- coding: utf-8 -*-
import math
__author__ = 'wangjj'
__mtime__ = '2016122014:26'
__doc__ = '''
利用生成器函数生成可迭代对象
'''


class PrimeNumbers(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_prime_num(self, k):
        if k < 2:
            return True
        for i in range(2, int(math.sqrt(k)) + 1):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.is_prime_num(k):
                yield k
for x in PrimeNumbers(1, 100):
    print(x)
