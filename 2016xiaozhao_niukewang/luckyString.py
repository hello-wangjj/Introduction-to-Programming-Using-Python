'''
A string s is LUCKY if and only if the number of different characters in s is a fibonacci number. 
Given a string consisting of only lower case letters , output all its lucky non-empty substrings in lexicographical order. Same substrings should be printed once.
'''
# 输入描述:
# a string consisting no more than 100 lower case letters.


# 输出描述:
# output the lucky substrings in lexicographical order.one per line. Same substrings should be printed once.
fib = [1,2,3,5,8,13,21]
def run():
    string = input('Please input string:')
    string_list = findFibonacci(string)
    for ls in string_list:
        print(ls)


def findFibonacci(string):
    res = set()
    for start in range(len(string)):
        current_res = set()
        current = 0
        for end in range(start,len(string)):
            if string[end] not in current_res:
                current += 1
                current_res.add(string[end])
            if current in fib:
                res.add(string[start:end+1])
    res = list(res)
    return sorted(res)

    
run()
