def main():
	ls=input('please input numbers seperate by space')
	ls=ls.split(' ')
	numbers=[eval(x) for x in ls ]
	# print (numbers)
	bubbleSort(numbers)
	print (numbers)

def bubbleSort(list):
	needNextPass=True

	k=1
	while k < len(list) and needNextPass:
		needNextPass=False
		for i in range(len(list)-k):
			if list[i]>list[i+1]:
				list[i],list[i+1]=list[i+1],list[i]

				needNextPass=True


if __name__=='__main__':
	main()