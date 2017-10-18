__author__ = 'wangj'
__date__ = '2017/10/18 23:00'
"""
春天是鲜花的季节，水仙花就是其中最迷人的代表，数学上有个水仙花数，他是这样定义的： 
“水仙花数”是指一个三位数，它的各位数字的立方和等于其本身，
比如：153=1^3+5^3+3^3。 现在要求输出所有在m和n范围内的水仙花数。
"""


def main():
    start, end = map(int, input().split())
    res = []
    for i in range(start, end + 1):
        if i == sum([int(i) ** 3 for i in str(i)]):
            res.append(i)
    if res:
        print(' '.join([str(i) for i in res]))
    else:
        print('no')


if __name__ == '__main__':
    main()
