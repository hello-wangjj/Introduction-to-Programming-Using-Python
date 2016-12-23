#!python3
# -*- coding: utf-8 -*-
import re
__author__ = 'wangjj'
__mtime__ = '2016122222:24'
__doc__ = '''
拆分字符串，该字符串包含多种不同的分割符，例如：
s = 'a;b|cd |efg|,gj\js;res\tsx'
'''


s = "ab;c|def|ghi,jkl,m|no;pqrs\tuv;|wxyz"
# 第一种方法 连续使用str.split()
res = s.split(';')
print(res)
t = []
for i in map(lambda x: x.split('|'), res):
    t.extend(i)
print(t)


def my_split(s, ds):
    res = [s]
    for d in ds:
        t = []
        for i in map(lambda x: x.split(d), res):
            t.extend(i)
        res = t
    return [x for x in res if x]
print(my_split(s, ';|,\t'))

# 第二种方法 re.split，正则表达式
new_s = re.split('[;,|\t]+', s)
print(new_s)
