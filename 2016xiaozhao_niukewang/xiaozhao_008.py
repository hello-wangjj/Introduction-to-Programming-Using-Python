import sys


__author__ = 'wangj'
__date__ = '2017/10/28 19:56'


def main():
    s = sys.stdin.readline().strip()
    ls = ['A', 'G', 'C', 'T']
    result = 0
    Flag = True
    ob = ['']
    while Flag:
        ob = deep(ob, ls)
        for i in ob:
            if s.find(i) != -1:
                continue
            else:
                Flag = False
                break
        result += 1

    print(result)


def deep(root, ls):
    new_root = []
    for i in root:
        for j in ls:
            new_root.append(i+j)
    return new_root


if __name__ == '__main__':
    main()
