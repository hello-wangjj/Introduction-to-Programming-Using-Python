"""
将一个正整数分解质因数
"""

import math
number = int(input())

list = []


def getChildren(num):

    isZhishu = True
    i = 2
    square = int(math.sqrt(num)) + 1
    while i <= square:
        if num % i == 0:
            list.append(i)
            isZhishu = False
            getChildren(num / i)
            i += 1
            break
        i += 1
    if isZhishu:
        list.append(num)


getChildren(number)
list.sort()
print(int(list.pop()))
