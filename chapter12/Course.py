class Course(object):
	"""docstring for Course"""
	def __init__(self, courseName):
		super(Course, self).__init__()
		self.__courseName = courseName
		self.__students=[]

	def addStudent(self,student):
		self.__students.append(student)

	def getStudents(self):
		return self.__students
	
	def getNumOfStudents(self):
		return len(self.__students)

	def getCoursenName(self):
		return self.__courseName

	def dropStudent(student):
		print ('left as an exercise')		

if __name__=='__main__':
	Course('Math')