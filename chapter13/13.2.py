def main():
	fname=input('please input a file name : ')
	fhandle=open(fname,'r')
	chars=0
	words=0
	lines=0
	for line in fhandle:
		lines+=1
		line=line.strip()
		word=line.split()
		words+=len(word)
		for char in word:
			chars+=len(char)
	print ('There are',chars,'characters')
	print ('There are',words,'words')
	print ('There are',lines,'lines')

if __name__=='__main__':
	main()