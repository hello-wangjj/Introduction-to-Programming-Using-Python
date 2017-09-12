import sys

__author__ = 'wangj'
__date__ = '2017/09/10 19:43'


def main():
    s = sys.stdin.readline().strip()
    l = list(s)
    new_l = []
    length = len(s)
    if length % 2 == 0:
        for i in range(len(l)):
            if i % 2 == 0:
                new_l.append(l[i + 1])
            else:
                new_l.append(l[i - 1])
    else:
        for i in range(len(l) - 1):
            if i % 2 == 0:
                new_l.append(l[i + 1])
            else:
                new_l.append(l[i - 1])
        new_l.append(l[-1])
    print(new_l)


if __name__ == '__main__':
    main()
