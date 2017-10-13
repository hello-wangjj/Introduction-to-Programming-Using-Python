class Solution(object):
    def __init__(self):
        self.dp = dict()

    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size <= 1: return s
        if s in self.dp: return self.dp[s]
        ans = s
        for p in range(1, size + 1):
            left, right = s[:p], s[p:]
            t = self.solve(left) + self.encode(right)
            if len(t) < len(ans): ans = t
        self.dp[s] = ans
        return ans

    def solve(self, s):
        ans = s
        size = len(s)
        for x in range(1, int(size / 2) + 1):
            if size % x or s[:x] * (int(size / x)) != s: continue
            y = str(int(size / x)) + '[' + self.encode(s[:x]) + ']'
            if len(y) < len(ans): ans = y
        return ans

s = Solution()
while True:
    ls = input()
    print(len(s.encode(ls)))

