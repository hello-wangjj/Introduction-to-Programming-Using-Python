# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 处理左子树
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left
        #连接根与左子树最大节点
        if left:
            while left.right:
                left = left.right
            pRootOfTree.left ,left.right = left,pRootOfTree
        # 处理右子树
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right
        # 连接根与右子树最小结点
        if right:
            while right.left:
                right = right.left
            pRootOfTree.right, right.left = right, pRootOfTree
        while(pRootOfTree.left):
            pRootOfTree = pRootOfTree.left
        return pRootOfTree

# 方法二：递归版
# 解题思路：
# 1.将左子树构造成双链表，并返回链表头节点。
# 2.定位至左子树双链表最后一个节点。
# 3.如果左子树链表不为空的话，将当前root追加到左子树链表。
# 4.将右子树构造成双链表，并返回链表头节点。
# 5.如果右子树链表不为空的话，将该链表追加到root节点之后。
# 6.根据左子树链表是否为空确定返回的节点。
#     public TreeNode Convert(TreeNode root) {
#         if(root==null)
#             return null;
#         if(root.left==null&&root.right==null)
#             return root;
#         // 1.将左子树构造成双链表，并返回链表头节点
#         TreeNode left = Convert(root.left);
#         TreeNode p = left;
#         // 2.定位至左子树双链表最后一个节点
#         while(p!=null&&p.right!=null){
#             p = p.right;
#         }
#         // 3.如果左子树链表不为空的话，将当前root追加到左子树链表
#         if(left!=null){
#             p.right = root;
#             root.left = p;
#         }
#         // 4.将右子树构造成双链表，并返回链表头节点
#         TreeNode right = Convert(root.right);
#         // 5.如果右子树链表不为空的话，将该链表追加到root节点之后
#         if(right!=null){
#             right.left = root;
#             root.right = right;
#         }
#         return left!=null?left:root;       
#     }
# 方法三：改进递归版
# 解题思路：
# 思路与方法二中的递归版一致，仅对第2点中的定位作了修改，新增一个全局变量记录左子树的最后一个节点。
#     // 记录子树链表的最后一个节点，终结点只可能为只含左子树的非叶节点与叶节点
#     protected TreeNode leftLast = null;
#     public TreeNode Convert(TreeNode root) {
#         if(root==null)
#             return null;
#         if(root.left==null&&root.right==null){
#             leftLast = root;// 最后的一个节点可能为最右侧的叶节点
#             return root;
#         }
#         // 1.将左子树构造成双链表，并返回链表头节点
#         TreeNode left = Convert(root.left);
#         // 3.如果左子树链表不为空的话，将当前root追加到左子树链表
#         if(left!=null){
#             leftLast.right = root;
#             root.left = leftLast;
#         }
#         leftLast = root;// 当根节点只含左子树时，则该根节点为最后一个节点
#         // 4.将右子树构造成双链表，并返回链表头节点
#         TreeNode right = Convert(root.right);
#         // 5.如果右子树链表不为空的话，将该链表追加到root节点之后
#         if(right!=null){
#             right.left = root;
#             root.right = right;
#         }
#         return left!=null?left:root;       
#     }
