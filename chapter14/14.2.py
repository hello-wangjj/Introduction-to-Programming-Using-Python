def main():
	s=input('enter the numbers : ').strip()
	numbers=[eval(x) for x in s.split()]
	dictionary={}
	for number in numbers:
		# if number in dictionary:
		# 	dictionary[number]+=1
		# else :
			# dictionary[number]=1
		dictionary[number]=dictionary.get(number,0)+1
	maxCount=max(dictionary.values())
	pairs=list(dictionary.items())
	items=[[x,y] for (x,y) in pairs]
	print('the numbers with the most occurence are ',end='')
	for (x,y) in items:
		if y==maxCount:
			print (x,end=' ')
if __name__=='__main__':
	main()