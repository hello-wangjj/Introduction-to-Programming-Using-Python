# 统计一个数字在排序数组中出现的次数。
# 二分查找
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return self.getUpper(data,k)-self.getLower(data,k)+1
    # 第一个K的位置
    def getLower(self,data,k):
        start,end = 0,len(data)-1
        mid = (start+end)>>1
        while   start <= end:
            if data[mid]<k:
                start = mid+1
            else:
                end = mid-1
            mid = (start+end)>>1
        return start
    
    # 最后一个K的位置
    def getUpper(self,data,k):
        start,end = 0,len(data)-1
        mid = (start+end)>>1
        while   start <= end:
            if data[mid]<=k:
                start = mid+1
            else:
                end = mid-1
            mid = (start+end)>>1
        return end

# 第一个K的位置
def getFirstNumber(data,k):
    start = 0
    end = len(data)-1
    mid = (start+end)>>1
    while start <= end:
        if data[mid] == k:
            end = mid-1
        elif data[mid]<k:
            start = mid+1
        else:
            end = mid-1
        mid = (start+end)>>1
    return start

def getLastNumber(data,k):
    start = 0
    end = len(data)-1
    mid = (start+end)>>1
    while start <= end:
        if data[mid] == k:
            start = mid+1
        elif data[mid]<k:
            start = mid+1
        else:
            end = mid-1
        mid = (start+end)>>1
    return end


print(getFirstNumber([0,1,2,3,4,5,5,6,7,8,9,10,11,12],5))
print(getLastNumber([0,1,2,3,4,5,5,6,7,8,9,10,11,12],5))