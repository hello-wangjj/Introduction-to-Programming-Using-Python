#!python3
# -*- coding: utf-8 -*-
__author__ = 'wangjj'
__mtime__ = '2017061616:29'
'''
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''


class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        flag = [0] * (rows * cols)
        count = self.moving(threshold, rows, cols, 0, 0, flag)
        return count

    def moving(self, threshold, rows, cols, row, col, flag):
        count = 0
        if self.check(threshold, rows, cols, row, col, flag):
            flag[row * cols + col] = 1
            count = 1 + self.moving(threshold, rows, cols, row - 1, col, flag) + \
                    self.moving(threshold, rows, cols, row, col - 1, flag) + \
                    self.moving(threshold, rows, cols, row + 1, col, flag) + \
                    self.moving(threshold, rows, cols, row, col + 1, flag)
        return count

    def check(self, threshold, rows, cols, row, col, flag):
        if 0 <= row < rows and 0 <= col < cols and self.getSum(row) + self.getSum(col) <= threshold and flag[
                            row * cols + col] == 0:
            return True
        return False

    @staticmethod
    def getSum(number):
        sums = 0
        while number > 0:
            sums += number % 10
            number //= 10
        return sums


if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(5, 10, 10))
