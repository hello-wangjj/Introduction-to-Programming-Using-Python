#!python3
# -*- coding: utf-8 -*-
from collections import deque
import pickle
from random import randint
import os
import sys
__author__ = 'wangjj'
__mtime__ = '201612180:30'
'''
实现一个类似历史记录的保存
'''
N = randint(0, 100)
if os.path.exists('history'):
    history = pickle.load(open('history', 'rb'))
else:
    history = deque([], 5)


def guess(k):
    if k == N:
        print('right')
        return True
    if k < N:
        print("{} is less than N".format(k))
    else:
        print("{} is greater than N".format(k))
    return False
while True:
    line = input('please input a number: ')
    if line.isdigit():
        k = int(line)
        history.append(k)
        pickle.dump(history, open('history', 'wb'))
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print(list(history))
    elif line == 'exit':
        print('exit')
        sys.exit()



