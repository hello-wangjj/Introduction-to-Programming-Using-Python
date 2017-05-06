# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
# 例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
# 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
# -*- coding:utf-8 -*-
# class Solution:
#     # matrix类型为二维列表，需要返回列表
#     def printMatrix(self, matrix):
#         # write code here

#  思想，用左上和右下的坐标定位出一次要旋转打印的数据，一次旋转打印结束后，往对角分别前进和后退一个单位。
#     提交代码时，主要的问题出在没有控制好后两个for循环，需要加入条件判断，防止出现单行或者单列的情况。
def printMatrix_2(matrix):
    l = []
    row = len(matrix)
    if (row == 0):
        return l
    col = len(matrix[0])
    #  定义四个关键变量，表示左上和右下的打印范围
    left,top,right,bottom = 0,0,col,row
    while(left<=right-1 and top<= bottom-1):
        # left to right
        for i in range(left,right):
            l.append(matrix[top][i])
            print('left to right',l)
        # top to bottom
        for i in range(top+1,bottom):
            l.append(matrix[i][right-1])
            print('top to bottom',l)
        # right to left
        if (top != bottom-1):
            for i in range(right-2,left-1,-1):
                l.append(matrix[bottom-1][i])
                print('right to left',l)
        # bottom to top
        if (left !=right-1):
            for i in range(bottom-2,top,-1):
                l.append(matrix[i][left])
                print('bottom to top',l)
        left+=1
        top+=1
        right-=1
        bottom-=1
        print(left,top,right,bottom)
    return l


#way 2
# 可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作
# 例如 
# 1 2 3
# 4 5 6
# 7 8 9
# 输出并删除第一行后，再进行一次逆时针旋转，就变成：
# 6 9
# 5 8
# 4 7
# 继续重复上述操作即可。
def printMatrix(matrix):
    l =[]
    while(matrix):
        l.extend(matrix.pop(0))
        if not matrix or not matrix[0]:
            break
        matrix = reverseMatrix(matrix)
    return l

def reverseMatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    new_matrix = []
    for i in range(col):
        new_matrix_2 = []
        for j in range(row):
            new_matrix_2.append(matrix[j][i])
        new_matrix.append(new_matrix_2)
    new_matrix.reverse()
    return new_matrix

if __name__ == '__main__':
    print(printMatrix_2([[1],[2],[3],[4],[5]]))
    print('----------------')
    print(printMatrix([[1],[2],[3],[4],[5]]))

    
    
        