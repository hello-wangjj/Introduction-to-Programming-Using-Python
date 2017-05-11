# HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
# 今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
# 但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
# 例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。你会不会被他忽悠住？(子向量的长度至少是1)
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array)<1:
            return
        sum = [0 for i in range(len(array))]
        sum[0] = array[0]
        for i in range(1,len(array)):
            sum[i] = max(array[i],array[i]+sum[i-1])
        return max(sum)

def FindGreatestSumOfSubArray(arrary):
    if len(arrary)<1:
        return
    sum = [0 for i in range(len(arrary))]
    for i in range(len(arrary)):
        if i == 0:
            sum[i] = arrary[i]
        else:
            sum[i] = sum[i-1]+arrary[i]
    return max(sum)

    
def getSumAll(array):
    result = []
    for i in range(len(array)):
        result.append(FindGreatestSumOfSubArray(array[i:]))
    return max(result)



print(getSumAll([1,2,3,4]))