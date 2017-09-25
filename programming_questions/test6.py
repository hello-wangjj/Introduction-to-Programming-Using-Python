import sys
import re
__author__ = 'wangj'
__date__ = '2017/09/15 19:30'


def main():
    s = sys.stdin.readline().strip()
    pattern = re.compile(r'^x.*@tal.*')
    if pattern.match(s):
        print('1')


if __name__ == '__main__':
    main()