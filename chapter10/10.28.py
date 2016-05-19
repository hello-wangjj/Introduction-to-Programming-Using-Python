def main():
	s=input('please input a list')
	items=s.split()
	ls=[eval(x) for x in items]

	ls=partition(ls)
	print(ls)

def partition(ls):
	l=len(ls)
	pivot=ls[0]
	high=l-1
	low=1

	while high>low:
		# pass
		while low<=high and ls[low]<=pivot:
			# pass
			low+=1

		while low<=high and ls[high]>pivot:
			# pass
			high-=1

		if high>low:
			ls[high],ls[low]=ls[low],ls[high]
	while high>1 and ls[high]>=pivot:
		# pass
		high-=1
	if pivot>ls[high]:
		ls[0]=ls[high]
		ls[high]=pivot

	return ls

main()

