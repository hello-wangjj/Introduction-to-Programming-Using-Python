import sys
import math

__author__ = 'wangj'
__date__ = '2017/09/08 20:19'


def main():
    n = int(sys.stdin.readline().strip())
    count = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                for d in range(1, n + 1):
                    if math.pow(a, b) == math.pow(c, d):
                        count += 1
    print(count)

if __name__ == '__main__':
    main()
