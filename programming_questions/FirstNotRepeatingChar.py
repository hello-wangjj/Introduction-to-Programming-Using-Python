# 在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)中找到第一个只出现一次的字符,并返回它的位置
def FirstNotRepeatingChar(s):
    index = 0
    if len(s) == 0:
        return -1
    else:
        for char in s:
            if s.count(char) == 1:
                return index
            index += 1
