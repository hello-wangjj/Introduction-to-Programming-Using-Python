# 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
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


# way2
class Solution2:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        
        self.expectNumber = expectNumber
        self.res = []
        self.find(root,root.val,[root.val])
        return self.res
    def find(self,node,sum,path):
        if sum>self.expectNumber:
            return
        if self.isLeaf(node) and sum ==self.expectNumber:
            self.res.append(path)
            return
        if node.left:
            self.find(node.left,sum+node.left.val,path+[node.left.val])
        if node.right:
            self.find(node.right,sum+node.right.val,path+[node.right.val])    
        
    def isLeaf(self,root):
        if not root.left and not root.right:
            return True
        else:
            return False

if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    root.right = TreeNode(12)
 
    s = Solution2()
    print(s.FindPath(root, 22)) 