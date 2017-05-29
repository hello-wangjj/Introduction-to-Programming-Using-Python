# 请实现一个函数，用来判断一颗二叉树是不是对称的。
# 注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        result = self.sysTree(pRoot.left,pRoot.right)
        return result
    
    def sysTree(self,root1,root2):
        '''判断两个树是不是对称的
 
        :param root1:
        :param root2:
        :return:
        '''
        # 匹配完毕
        if not root1 and not root2:
            return True
        if root1 and not root2:
            return False
        if root2 and not root1:
            return False
        # 两个树不为空树
        if root1.val != root2.val:
            return False
        # 判断左右子树是否一致
        left = self.sysTree(root1.left,root2.right)
        if not left:
            return False
        right = self.sysTree(root1.right,root2.left)
        if not right:
            return True
        return True

        
