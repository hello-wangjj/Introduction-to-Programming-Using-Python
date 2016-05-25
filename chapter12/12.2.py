class Location(object):
	"""docstring for Location"""
	def __init__(self, row,column,maxValue):
		super(Location, self).__init__()
		# self.arg = arg
		self.row=row
		self.column=column
		self.maxValue=maxValue
	def getRow(self):
		return self.row

	def getColumn(self):
		return self.column

	def getMaxValue(self):
		return self.maxValue


def main():
	row,column=eval(input('enter the number of rows and cols of the list :'))

	matrix=[]

	for i in range(row):
		s=input('enter row '+ str(i)+':')
		items=s.split()
		ls=[eval(x) for x in items]
		matrix.append(ls)

	location=locateLargest(matrix)
	print ('the location of the largest element is '+
		str(location.getMaxValue())+
			" at("+str(location.getRow())+","+
			str(location.getColumn())+")")

def locateLargest(a):
	maxValue=a[0][0]
	row=0
	col=0
	for i in range(len(a)):
		for j in range(len(a[i])):
			if maxValue<a[i][j]:
				maxValue=a[i][j]
				row=i
				col=j
	return Location(row, col, maxValue)

if __name__=='__main__':
	main()
		