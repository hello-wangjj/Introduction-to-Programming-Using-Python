#!python3
# -*- coding: utf-8 -*-
__author__ = 'wangjj'
__mtime__ = '2017052120:10'
'''
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）
'''


class Solution:

    def __init__(self):
        self.sum = 0

    def Sum_Solution(self, n):
        # write code here
        self.get_sum(n)
        return self.sum

    def get_sum(self, n):
        self.sum += n
        n -= 1
        return n > 0 and self.Sum_Solution(n)

if __name__ == '__main__':
    s = Solution()
    print(s.Sum_Solution(6))
