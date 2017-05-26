# 给定一个数组A[0,1,...,n-1],
# 请构建一个数组B[0,1,...,n-1],
# 其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
# 不能使用除法。
# -*- coding:utf-8 -*-


class Solution:

    def multiply(self, A):
        # write code here
        length = len(A)
        B = [1]*length
        B_1 = [1]*length
        B_2 = [1]*length
        # 计算下三角
        for i in range(1,length):
            B_1[i] = A[i-1]*B_1[i-1]
        # print(B_1)
        # 计算上三角
        for i in range(length-2,-1,-1):
            B_2[i] = A[i+1]*B_2[i+1]
        # print(B_2)
        for i in range(0,length):
            B[i] = B_1[i]*B_2[i]
        # print(B)
        return B

    def multiply_2(self, A):
        B = [1] * len(A)
        for i in range(0, len(A)):
            for j in range(0, len(B)):
                if i != j:
                    B[i] *= A[j]
        return B



if __name__ == '__main__':
    s = Solution()
    s.multiply([1,2,3,4])
