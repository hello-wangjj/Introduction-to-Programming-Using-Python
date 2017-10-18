import math

__author__ = 'wangj'
__date__ = '2017/10/18 23:15'
"""
数列的第一项为n，以后各项为前一项的平方根，求数列的前m项的和。
"""


def main():
    n, m = map(int, input().strip().split())
    res = 0
    for i in range(m):
        res += n
        n = math.sqrt(n)
    print("%.2f" % res)


if __name__ == '__main__':
    main()
