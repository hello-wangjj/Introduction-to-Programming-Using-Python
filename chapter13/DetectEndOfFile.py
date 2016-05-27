import pickle
def main():
	outfile=open('numbers.dat','wb')

	data=eval(input('please enter an integer (the input exists if the input is 0): '))
	while data!=0:
		# pass
		pickle.dump(data, outfile)
		data=eval(input('please enter an integer (the input exists if the input is 0): '))

	outfile.close()

	infile=open('numbers.dat','rb')
	end_of_file=False
	while not end_of_file:
		# pass
		try:
			print(pickle.load(infile),end=' ')
		except EOFError:
			end_of_file=True
	infile.close()

	print('\nall objects are readed')
if __name__=='__main__':
	main()