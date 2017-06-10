# 给定一颗二叉搜索树，请找出其中的第k大的结点。例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        #第三个节点是4
        #前序遍历5324768
        #中序遍历2345678
        #后序遍历2436875
        #所以是中序遍历，左根右
        if not pRoot or k == 0:
            return None
        res = self.midNode(pRoot)
        if len(res)<k:
            return None
        else:
            return res[k-1]

    def midNode(self,root):
        result = []
        if not root:
            return None
        if root.left:
            result.extend(self.midNode(root.left))
        result.append(root)
        if root.right:
            result.extend(self.midNode(root.right))
        return result

