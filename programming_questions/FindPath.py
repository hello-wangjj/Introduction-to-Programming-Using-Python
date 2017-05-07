# 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        res = []       
        def FindMainPath(root,path,currentSum):
            currentSum += root.val
            path.append(root.val)
             
            isLeaf = not root.left and not root.right
                 
            if root.left:
                FindMainPath(root.left,path,currentSum)
                 
            if root.right:
                FindMainPath(root.right,path,currentSum)
                 
            if currentSum == expectNumber and isLeaf:
                lis = [i for i in path]
                res.append(lis)
             
            path.pop()
 
        FindMainPath(root,[],0)
         
        return res

