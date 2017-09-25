import sys

__author__ = 'wangj'
__date__ = '2017/09/16 16:24'


def main():
    n = sys.stdin.readline().strip()
    count_n = 0
    duiwus = {}
    n = int(n)
    while True:
        duiwu = sys.stdin.readline().strip()
        duiwus.setdefault(duiwu, 0)
        count_n += 1
        if count_n == n:
            break
    fenshus = []
    count_fen = 0
    while True:
        fenshu = sys.stdin.readline().strip()
        fenshus.append(fenshu)
        count_fen += 1
        if count_fen == n * (n - 1) / 2:
            break
    for i in fenshus:
        cmp = i.split(' ')[0]
        bifen = i.split(' ')[1]
        cmp_1 = cmp.split('-')[0]
        cmp_2 = cmp.split('-')[1]
        num1 = int(bifen.split(':')[0])
        num2 = int(bifen.split(':')[1])
        if num1 > num2:
            duiwus[cmp_1] += 3
        elif num1 == num2:
            duiwus[cmp_1] += 1
            duiwus[cmp_2] += 1
        else:
            duiwus[cmp_2] += 3
    new_duiwus = sorted(duiwus.items(), key=lambda item: item[1], reverse=True)
    res = list(new_duiwus)[0:int(n/2)]
    new_res = []
    for i in res:
        new_res.append(i[0])
    new_res = sorted(new_res)
    for i in new_res:
        print(i)


if __name__ == '__main__':
    main()
