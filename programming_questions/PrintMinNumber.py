# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
# 例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
# -*- coding:utf-8 -*-
# class Solution:
#     def PrintMinNumber(self, numbers):
#         # write code here
from functools import cmp_to_key
def PrintMinNumber(numbers):
    if not numbers:
        return None
    key =cmp_to_key(lambda num1,num2: int(str(num1)+str(num2))-int(str(num2)+str(num1)))
    array = sorted(numbers,key = key)
    return ''.join([str(i) for i in array])

print(PrintMinNumber([3,32,321]))