#!python3
# -*- coding: utf-8 -*-
def minNumberInRotateArray(rotateArray):
        # write code here
    if len(rotateArray) == 0:
        return 0
    target = rotateArray[0]
    for i in rotateArray[1:]:
        if target > i :
            return i
        target = i
    return target
        
        


def main():
    pass

if __name__ == '__main__':
    main()
    print(minNumberInRotateArray([3,4,5,1,2]))
    print(minNumberInRotateArray([1,1,1,0,1,1]))
    print(minNumberInRotateArray([0,1,1,1,0]))