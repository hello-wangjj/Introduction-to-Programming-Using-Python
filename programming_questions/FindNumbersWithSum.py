# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，
# 是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
# 对应每个测试案例，输出两个数，小的先输出。
# -*- coding:utf-8 -*-

# 数列满足递增，设两个头尾两个指针i和j，
# 若ai + aj == sum，就是答案（相差越远乘积越小）
# 若ai + aj > sum，aj肯定不是答案之一（前面已得出 i 前面的数已是不可能），j -= 1
# 若ai + aj < sum，ai肯定不是答案之一（前面已得出 j 后面的数已是不可能），i += 1
# O(n)
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        result = []
        end = len(array)-1
        start = 0
        while start <end:
            if array[start]+array[end] == tsum:
                result.append(array[start])
                result.append(array[end])
                break
            if start<end and array[start]+array[end]>tsum:
                end = end-1
            if start<end and array[start]+array[end]<tsum:
                start =start+1
        return result

s=Solution()
print(s.FindNumbersWithSum([1,2,4,7,11,15],15))
