import sys
import re

__author__ = 'wangj'
__date__ = '2017/09/14 21:09'


def main():
    n = sys.stdin.readline().strip()
    count = 0
    pwd = []
    while True:
        s = sys.stdin.readline().strip()
        pwd.append(s)
        count += 1
        if count == int(n):
            break
    start = re.compile(r'^[a-zA-Z]')
    full_c = re.compile(r'\w+\d+|\d+\w+')
    for i in pwd:
        if len(i) < 8:
            print('NO')
        elif start.match(i) and full_c.match(i):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
