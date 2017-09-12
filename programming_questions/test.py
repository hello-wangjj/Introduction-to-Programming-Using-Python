import sys
import math
__author__ = 'wangj'
__date__ = '2017/09/08 20:06'


def main():
    n = int(sys.stdin.readline().strip())
    num = 1
    while True:
        if (num ** 2 + num) > (2 * n) and (num ** 2 - num) < (2 * n):
            print(num)
            break
        else:
            num += 1

def main2():
    n = int(sys.stdin.readline().strip())
    print(int(math.sqrt(2*n)))

if __name__ == '__main__':
    main()
