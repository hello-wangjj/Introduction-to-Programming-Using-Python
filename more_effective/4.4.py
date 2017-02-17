#!python3
# -*- coding: utf-8 -*-
__author__ = 'wangjj'
__mtime__ = '201612250:25'
__doc__ = '''
拼接字符串
'''

# 第一种  +
l = ['abc', 'cde', 'asd']
s = ''
for i in l:
    s += i
    print(s)

# 第二种 str.join
print(''.join(l))

# 如果有数字 使用生成器
new_l = ['abc', 'cde', '123', '456', 'asd']
print(''.join((str(i) for i in new_l)))
