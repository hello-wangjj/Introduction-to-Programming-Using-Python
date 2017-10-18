import sys
from functools import cmp_to_key

__author__ = 'wangj'
__date__ = '2017/10/18 00:14'
"""
设有n个正整数，将他们连接成一排，组成一个最大的多位整数。
如:n=3时，3个整数13,312,343,连成的最大整数为34331213。
如:n=4时,4个整数7,13,4,246连接成的最大整数为7424613。
"""


def mycamp(x, y):
    if x + y > x + y:
        return 1
    elif x == y:
        return 0
    else:
        return -1


def main():
    num = input()
    v = input()

    v = v.strip().split()
    v.sort(key=cmp_to_key(mycamp), reverse=False)
    print(''.join(v).lstrip('0'))


if __name__ == '__main__':
    main()
