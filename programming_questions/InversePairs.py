# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007 
# 输入描述:
# 题目保证输入的数组中没有的相同的数字
# 数据范围：
# 	对于%50的数据,size<=10^4
# 	对于%75的数据,size<=10^5
# 	对于%100的数据,size<=2*10^5


# 输入例子:
# 1,2,3,4,5,6,7,0

# 输出例子:
# 7
# 链接：https://www.nowcoder.com/questionTerminal/96bd6684e04a44eb80e6a68efc0ec6c5
# 来源：牛客网

# /*归并排序的改进，把数据分成前后两个数组(递归分到每个数组仅有一个数据项)，
# 合并数组，合并时，出现前面的数组值array[i]大于后面数组值array[j]时；则前面
# 数组array[i]~array[mid]都是大于array[j]的，count += mid+1 - i
# 参考剑指Offer，但是感觉剑指Offer归并过程少了一步拷贝过程。
# 还有就是测试用例输出结果比较大，对每次返回的count mod(1000000007)求余
# */
import copy


    # 算法复杂度过大
    # def InversePairs(self, data):
    #     # write code here
    #     count = 0
    #     for i in range(len(data)):
    #         for j in range(i,len(data)):
    #             if data[i]>data[j]:
    #                 count +=1
    #     return count%1000000007
class nx:
    def __init__(self):
        self.count = 0

    def merge(self, ListA, ListB):
        newlist = []
        while ListA and ListB:
            if int(ListA[0]) > int(ListB[0]):
                self.count += len(ListA)
                newlist.append(ListB.pop(0))               
            else:
                newlist.append(ListA.pop(0)) 
        return newlist + ListA + ListB     

    def merge_sort(self, A):
        if len(A) == 1: return A
        else:
            middle = int(len(A)/2)        
            return self.merge(self.merge_sort(A[:middle]), self.merge_sort(A[middle:]))        
    def count_inversion(self, data):
        self.merge_sort(data)
        return self.count




            


if __name__ == '__main__':
    s=nx()
    print(s.count_inversion([4,3,1]))



