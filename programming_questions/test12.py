import sys


def main():
    n = int(sys.stdin.readline().strip())
    n_ls = (sys.stdin.readline().strip()).split(' ')
    height_n = []
    for i in n_ls:
        height_n.append(int(i))
    m = int(sys.stdin.readline().strip())
    count = 0
    m_ls = []
    while True:
        x = (sys.stdin.readline().strip())
        m_ls.append(x)
        count += 1
        if count == m:
            break

    counts = []
    for item in m_ls:
        a = int(item.split(' ')[0])
        b = int(item.split(' ')[1])
        new_m_ls = []
        if b - a < 2:
            counts.append(0)
        elif b - a == 2:
            height = height_n[a - 1:b]
            counts.append(find(height))
        else:
            for i in range(a, b + 1):
                if i + 3 <= b + 1:
                    new_m_ls.append(height_n[i - 1:i + 2])
            ct = 0
            for i in new_m_ls:
                ct += find(i)
            counts.append(ct)
    for i in counts:
        print(i)


def find(height):
    if height[0] <= height[1] <= height[2]:
        return 1
    else:
        return 0


if __name__ == '__main__':
    main()
