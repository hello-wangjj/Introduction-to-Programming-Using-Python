def recursiveBianrySearch(lst,key):
	# pass
	low=0
	high=len(lst)-1
	return resursiveBinarySearchHelper(lst, key, low, high)



def resursiveBinarySearchHelper(lst,key,low,high):
	# pass
	if low>high:
		return -low-1
	mid=(low+high)//2

	if key<lst[mid]:
		return resursiveBinarySearchHelper(lst, key, low, mid-1)
	elif key==lst[mid]:
		return mid
	else:
		return resursiveBinarySearchHelper(lst, key, mid+1, high)


def main():
	lst=[3,5,6,8,9,12,34,36]
	print(recursiveBianrySearch(lst,3))
	print(recursiveBianrySearch(lst,4))

if __name__=='__main__':
	main()