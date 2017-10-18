__author__ = 'wangj'
__date__ = '2017/10/18 22:39'
"""
继MIUI8推出手机分身功能之后，MIUI9计划推出一个电话号码分身的功能：
首先将电话号码中的每个数字加上8取个位，然后使用对应的大写字母代替 
（"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"）， 
然后随机打乱这些字母，所生成的字符串即为电话号码对应的分身。
"""

def main():
    n = int(input())
    strs = []
    while (n):
        strs.append(input())
        n -= 1
    for i in strs:
        print(get_origins(i))

def get_origins(myStr):
    result = [0] * 10
    result[2] = myStr.count("Z")  # 0
    result[4] = myStr.count("W")  # 2
    result[6] = myStr.count("U")  # 4
    result[8] = myStr.count("X")  # 6
    result[9] = myStr.count("S") - result[8]
    result[7] = myStr.count("V") - result[9]
    result[3] = myStr.count("O") - result[2] - result[6] - result[4]
    result[1] = (myStr.count("N") - result[3] - result[9]) // 2
    result[0] = myStr.count("I") - result[7] - result[8] - result[1]
    result[5] = myStr.count("H") - result[0]
    output = ''
    for i in range(10):
        output += str(i) * result[i]
    return output


if __name__ == '__main__':
    main()