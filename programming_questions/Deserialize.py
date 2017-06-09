# 请实现两个函数，分别用来序列化和反序列化二叉树
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.flag = -1

    def Serialize(self, root):
        # write code here
        s = ''
        s = self.recursionSerialize(root, s)
        return s
        
    def Deserialize(self, s):
        # write code here
        self.flag += 1
        l = s.split(',')
        if (self.flag >= len(s)):
            return None
        root = None
        if (l[self.flag] != '$'):
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root
# way2
class Solution2:
    flag = -1
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)
     
    def Deserialize(self, s):
        # write code here
        self.flag += 1
         
        l = s.split(',')
        if self.flag >= len(s):
            return None
         
        root = None
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root
    def recursionSerialize(self,root,s):
        if root is None:
            s = '$'
            return s
        s = str(root.val) + ','
        left = self.recursionSerialize(root.left, s)
        right = self.recursionSerialize(root.right, s)
        s += left + right
        return s