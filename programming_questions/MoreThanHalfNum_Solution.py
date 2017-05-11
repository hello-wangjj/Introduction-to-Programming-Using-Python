# -*- coding:utf-8 -*-
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        for i in list(set(numbers)):
            if numbers.count(i) > len(numbers)/2:
                return i
        return 0

def MoreThanHalfNum_Solution2(numbers):
    # write code here
    dc=dict.fromkeys(list(set(numbers)),0)
    for i in numbers:
        dc[i]+=1
    for (key,value) in dc.items():
        if value > len(numbers)/2:
            return key
    return 0

print(MoreThanHalfNum_Solution2([1,2,3,2,2,2,5,4,2]))