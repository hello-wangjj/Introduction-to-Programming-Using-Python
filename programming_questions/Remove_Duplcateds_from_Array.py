# 同样是移除重复的元素，但是加深了难度,可以允许最多两次重复的元素存在
# 多种变换解法

# way1
def remove_duplacteds_from_array(nums):
    duplacted_elemnte_more_than_twice = []
    for i in range(len(nums)):
        count = 1
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                count +=1
        if count>2:
            duplacted_elemnte_more_than_twice.append(i)
    for i in duplacted_elemnte_more_than_twice[::-1]:
        nums.pop(i)
    print(duplacted_elemnte_more_than_twice)
    print(nums)

# way2 使用set
def remove_duplacteds_from_array_2(nums):
    nums_set = set(nums)
    for num in nums_set:
        # print(nums.count(num))
        while nums.count(num) > 2:
            nums.remove(num)
    print(nums)
    


if __name__ == '__main__':
    remove_duplacteds_from_array([1,2,3,4,2,2,3,3,3,1,1])
    remove_duplacteds_from_array_2([1,2,3,4,2,2,3,3,3,1,1])