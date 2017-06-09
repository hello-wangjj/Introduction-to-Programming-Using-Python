# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        # 从根节点开始
        temp = [pRoot]
        while temp:
            # temp长度
            size = len(temp)
            # 待输出行
            row = []
            for i in temp:
                row.append(i.val)
            res.append(row)
            for i in range(size):
                node = temp.pop(0)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
        return res
