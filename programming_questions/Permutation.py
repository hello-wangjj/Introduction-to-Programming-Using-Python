# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。 
import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        return sorted(list(set(map(''.join, itertools.permutations(ss)))))

class Solution2:
    def Permutation1(self, ss):
        # write code here
        #可能有重复字母
        n = len(ss)
        if n==0:
            return []
        result = []
        self.getPermutation(ss, result, [], n)
        #result.sort()
        return result
         
    def getPermutation1(self, ss, result, tmpResult, n):
        if len(tmpResult)==n:
            result.append("".join(tmpResult))
            return
        #为避免结果集中有重复的排列（因为有重复字母），那么在选排列起点时就要去掉重复
        for ch in sorted(set(ss)):#结果请按字母顺序输出
            tmpResult.append(ch)
            idx = ss.index(ch)
            self.getPermutation(ss[:idx]+ss[idx+1:], result, tmpResult, n)
            tmpResult.pop()
     
     
    #法2：基于交换
    def Permutation(self, ss):
        n = len(ss)
        if n==0:
            return []
        result = []
        ssList = list(ss)
        ssList.sort()#避免后面的计算结果集重复
        self.getPermutation(ssList, result, 0, n-1)
        #result.sort()
        return result
     
    def getPermutation(self, ss, result, start, end):
        if start>end:
            result.append("".join(ss))
            return
         
        #ss = ss[:start]+sorted(ss[start:end+1])################排序是为了避免后面的计算结果集重复
        for i in range(start, end+1):
            if i>start and ss[i]==ss[i-1]:#遇到重复字母，不重复计算
                continue
            ss[start], ss[i] = ss[i], ss[start]
            self.getPermutation(ss[:], result, start+1, end) 



