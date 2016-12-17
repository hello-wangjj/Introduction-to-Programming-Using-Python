def main():
    n = eval(input('enter number of disks : '))
    print('The moves are')
    move(n, 'A', 'B', 'C')


def move(n, fromTower, toTower, auxTower):
    if n == 1:
        print('Move disk ', n, 'from', fromTower, 'to', toTower)
    else:
        move(n - 1, fromTower, auxTower, toTower)
        print('Move disk ', n, 'from', fromTower, 'to', toTower)
        move(n - 1, auxTower, toTower, fromTower)
if __name__ == '__main__':
    main()
