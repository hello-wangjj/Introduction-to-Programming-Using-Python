import sys

__author__ = 'wangj'
__date__ = '2017/09/14 20:35'


def main():
    n = sys.stdin.readline().strip()
    s = sys.stdin.readline().strip()
    new_s = s.split(' ')
    count = 0
    s_l = len(new_s)
    for i in range(s_l):
        for j in range(i+1, s_l):
            num_1 = int(new_s[i] + new_s[j])
            num_2 = int(new_s[j] + new_s[i])
            if num_2 % 7 == 0:
                count += 1
            if num_1 % 7 == 0:
                count += 1
    print(count)


if __name__ == '__main__':
    main()
