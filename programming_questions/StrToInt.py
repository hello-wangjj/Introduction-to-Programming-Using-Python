#!python3
# -*- coding: utf-8 -*-
__author__ = 'wangjj'
__mtime__ = '2017052215:27'
'''
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
'''


class Solution:

    def StrToInt(self, s):
        # write code here
        ls = list(s)
        length = len(ls)
        flag = 1
        res = []
        if length == 0:
            return 0
        if length == 1:
            if ls[0] in '0123456789':
                return int(ls[0])
            else:
                return 0
        if ls[0] == '+':
            ls = ls[1:]
            flag = 1
        if ls[0] == '-':
            ls = ls[1:]
            flag = -1
        for i in ls:
            if i in '0123456789':
                res.append(i)
            else:
                return 0
        num = ''.join(res)
        result = int(num) * flag
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.StrToInt('-12345680989797897'))
