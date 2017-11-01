def DFS_bracker(n,left_used,right_used):
    if left_used == right_used and left_used+right_used == 2*n:
        print(bracker[:-1])
        return
    if left_used < right_used or left_used + right_used > 2*n:
        return 
    index = left_used + right_used
    bracker[index] = '('
    DFS_bracker(n,left_used+1,right_used)
    bracker[index] = ')'
    DFS_bracker(n,left_used,right_used+1)


def main():
    n = int(input().strip())
    global bracker 
    bracker = ['']*2*n + ['']
    DFS_bracker(n,0,0)


if __name__ == '__main__':
    main()
        