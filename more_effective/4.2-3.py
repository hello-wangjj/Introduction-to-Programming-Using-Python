#!python3
# -*- coding: utf-8 -*-
import os
import re
__author__ = 'wangjj'
__mtime__ = '2016122223:36'
__doc__ = '''
判断字符串a是否已字符串b开头或者结尾
'''
# 使用字符串的str.startswith() str.endswith()方法
print(os.listdir('.'))
new_file = [name for name in os.listdir('.') if name.endswith(('.py', '.sh'))]
print(new_file)
print(os.stat('1.1.py'))
print(oct(os.stat('1.1.py').st_mode))

# re.sub
s = '2016-11-25 wangjjhiwangjjhiwangjj'
print(re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', s))
print(re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', s))
