import sys

__author__ = 'wangj'
__date__ = '2017/09/26 20:02'


def main():
    ls = (sys.stdin.readline().strip()).split(' ')
    ls = [x.strip() for x in ls if x != '']
    new_l = ' '.join(ls[::-1])
    print(new_l)


if __name__ == '__main__':
    main()
