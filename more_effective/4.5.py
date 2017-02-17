#!python3
# -*- coding: utf-8 -*-
__author__ = 'wangjj'
__mtime__ = '2016122823:04'
__doc__ = '''
将字符串进行居中，左，右的对齐
方法一：使用字符串的str.ljust(),str.rjust,str.center()
方法二：使用format方法，传递类似'<20','>20','^20'参数
'''
s = 'abc'
print(s.ljust(20, ':'))
print(s.center(20, ':'))
