def main():
	# pass
	s=input('please input numbers : ').strip()
	items=s.split()
	numbers=[eval(x) for x in items]
	print ('the max number is',str(MaxValue(numbers)))


def MaxValue(list):
	# pass
	return MaxValueHelper(list, len(list)-1)

def MaxValueHelper(list,high):
	# pass
	if high==0:
		return list[0]
	else:
		return max(MaxValueHelper(list,high-1),list[high])
	

if __name__=="__main__":
	main()