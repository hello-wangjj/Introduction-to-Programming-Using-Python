__author__ = 'wangj'
__date__ = '2017/10/20 00:39'
"""
一只袋鼠要从河这边跳到河对岸，河很宽，
但是河中间打了很多桩子，每隔一米就有一个，每个桩子上都有一个弹簧，
袋鼠跳到弹簧上就可以跳的更远。每个弹簧力量不同，
用一个数字代表它的力量，如果弹簧力量为5，就代表袋鼠下一跳最多能够跳5米，
如果为0，就会陷进去无法继续跳跃。河流一共N米宽，袋鼠初始位置就在第一个弹簧上面，
要跳到最后一个弹簧之后就算过河了，给定每个弹簧的力量，求袋鼠最少需要多少跳能够到达对岸。
如果无法到达输出-1
"""


def main():
    n = int(input())
    l = list(map(int, input().split()))
    d = [0 for i in range(n)]
    d[0] = 1
    arrived = []
    for i in range(n):
        if d[i] == 0:
            continue
        for j in range(l[i], 0, -1):
            if i + j >= n:
                arrived.append(d[i])
                continue
            elif d[i + j] == 0 or d[i + j] > d[i]:
                d[i + j] = d[i] + 1
    if len(arrived) == 0:
        print(-1)
    else:
        print(min(arrived))


if __name__ == '__main__':
    main()

    """
    链接：https://www.nowcoder.com/questionTerminal/74acf832651e45bd9e059c59bc6e1cbf
来源：牛客网

n = int(input())
nums = list(map(int, input().split()))
dp = [0xfffffff]*n
for i in range(n-1, -1, -1):
    for j in range(1, nums[i]+1):
        dp[i] = min(dp[i], dp[i+j]+1 if i+j<n else 1)
print(dp[0] if dp[0]<0xfffffff else -1)
    """

    """
    链接：https://www.nowcoder.com/questionTerminal/74acf832651e45bd9e059c59bc6e1cbf
来源：牛客网

if __name__ == '__main__':
    N = int(input())
    nums = [int(x) for x in input().split()]
 
    inf = float('inf')
    dp = [inf for j in range(N+1)]  # 跳到第i个木桩需要的最少次数
    dp[0] = 0  # 第0个木桩需要跳0次
    for i in range(N):
        j = 1
        # 跳 j 步会跳到i+j，需要跳dp[i]+1次，不要跳出去
        while j <= nums[i] and i+j <= N:
            dp[i+j] = min(dp[i+j], dp[i]+1)
            j += 1
    print(dp[N] if dp[N] < inf else -1)
    """
