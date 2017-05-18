# LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
# 他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
# “红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....
# LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
# 上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 
# 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何。为了方便起见,你可以认为大小王是0。
# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        # 必须满足两个条件
        # 1. 除0外没有重复的数
        # 2. max - min < 5
        if len(numbers)<5: return False
        min = -1
        max = 14
        ls_0 = []
        ls_1 = []
        for i in range(len(numbers)):
            number=numbers[i]
            if number<0 or number>13: return False
            if number == 0:
                ls_0.append(number)
                continue
            if number not in ls_1:
                ls_1.append(number)
            else:
                return False
        ls_1.sort()
        if len(ls_1)==1: return True
        if ls_1[-1]-ls_1[0]<5: return True
        return False
s=Solution()
print(s.IsContinuous([1,0,0,0,6]))


        

            