import sys
from functools import reduce

__author__ = 'wangj'
__date__ = '2017/09/18 20:36'


# 1到n随机取出几个数使其和等于m
def showCombination(ls):
    print(ls)


def findCombination(i, n, m, ls):
    # 当前数字超出范围, 或加上当前数字后会大于总和
    if i > n or i > m:
        return
    # 加上当前数字正好等于总和
    elif i == m:
        ls.append(i)
        showCombination(ls)
        ls.pop()
    # 加上当前数字后仍然小于总和
    else:
        # 加上当前数字
        ls.append(i)
        findCombination(i + 1, n, m - i, ls)
        ls.pop()
        # 不加上当前数字
        findCombination(i + 1, n, m, ls)


def main():
    input_nums = sys.stdin.readline().strip().split(' ')
    n = int(input_nums[0])
    # 和
    m = int(input_nums[1])
    ls = []
    findCombination(1, n, m, ls)


if __name__ == '__main__':
    main()
