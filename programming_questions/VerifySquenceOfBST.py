# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

def VerifySquenceOfBST(sequence):
    # write code here
    if len(sequence)==0:
        return False
    if len(sequence)<=1:
        return True
    root = sequence[-1]
        
    for i in range(len(sequence)):
        if sequence[i]>=root:
            start = i
            break
    for i in range(start,len(sequence)-1):
        if sequence[i]<root:
            return False
    left = True
    right = True
        
    if start>1:
        left =VerifySquenceOfBST(sequence[:start])
    if left==True and start<len(sequence)-2:
        right =VerifySquenceOfBST(sequence[start:-1])
    return left and right

print(VerifySquenceOfBST([1,2,3,4,5]))