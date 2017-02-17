#!python3
# -*- coding: utf-8 -*-
import string
__author__ = 'wangjj'
__mtime__ = '201612290:22'
__doc__ = '''
去掉不需要的字符
方法一：strip()
方法二：切片加 拼接
方法三：replace re.sub
方法四：字符串 translate
'''
s = 'abc1234455xyz'
str_trans = str.maketrans('abcxyz', 'xyzabc')
print(str_trans)
print(s.translate(str_trans))
s='ab1234d'
print(s.translate(str.maketrans('abcx','aaad')))
