import random
import os.path
fname=input('enter a file name:')
if  os.path.isfile(fname):
	print ('The file already exists')
else:

	outfile=open(fname,'w')
	for i in range(0,100):
		a=random.randint(0, 100)
		a=str(a)
		outfile.write(a)
		outfile.write(' ')
	outfile.close()

infile=open(fname,'r')
for line in infile:
	print(line,end='')
infile.close()