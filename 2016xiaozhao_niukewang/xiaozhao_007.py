import sys
"""
判断缺失的括号数目
"""
__author__ = 'wangj'
__date__ = '2017/10/28 19:23'


def main():
    s = sys.stdin.readline().strip()

    left = []
    right = []
    count = 0
    for i in s:
        if i == '(':
            left.append('(')
        elif i == ')':
            if len(left) == 0:
                count += 1
            else:
                left.pop()
    print(len(left)+count)


if __name__ == '__main__':
    main()
