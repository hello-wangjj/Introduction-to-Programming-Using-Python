#!python3
# -*- coding: utf-8 -*-
from collections import namedtuple
__author__ = 'wangjj'
__mtime__ = '2016121914:43'
'''
给元组元素命名
'''
student = ('wangjj', 16, 'male', 'wangjj886688@163.com')
NAME = 0
AGE = 1
SEX = 2
EMAIL = 3
# name
print(student[0])
print(student[NAME])
# age
print(student[1])
print(student[AGE])
# sex
print(student[2])
print(student[SEX])
# mail
print(student[3])
print(student[EMAIL])

name, age, sex, email = range(4)
print(name, age, sex, email)

Student = namedtuple('Student', ['Name', 'Age', 'Sex', 'Email'])
s1 = Student('wangjj', 16, 'male', 'wangjj886688@163.com')
print(s1)
print(isinstance(s1, tuple))
