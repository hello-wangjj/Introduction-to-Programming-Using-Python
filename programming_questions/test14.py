import sys

__author__ = 'wangj'
__date__ = '2017/09/26 19:54'


def findMax(time_start, time_end, n):
    time_start = sorted(time_start)
    time_end = sorted(time_end)
    guest_in = 1
    max_guests = 1
    time = time_start[0]
    i = 1
    j = 0
    while i < n and j < n:
        if time_start[i] <= time_end[j]:
            guest_in += 1
            if guest_in > max_guests:
                max_guests = guest_in
                time = time_start[i]
            i += 1
        else:
            guest_in -= 1
            j += 1
    print(max_guests)


def main():
    n = int(sys.stdin.readline().strip())
    time_1 = sys.stdin.readline().strip().split(' ')
    time_2 = sys.stdin.readline().strip().split(' ')
    time_start = [int(x) for x in time_1]
    time_end = [int(x) for x in time_2]
    findMax(time_start, time_end, n)


if __name__ == '__main__':
    main()
