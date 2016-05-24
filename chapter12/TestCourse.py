from Course import Course
def main():
	Course1=Course('Data Structures')
	Course2=Course('Database System')

	Course1.addStudent('Peter Wang')
	Course1.addStudent('Brian Li')
	Course1.addStudent('Anne Wu')

	Course2.addStudent('Peter Sun')
	Course2.addStudent('Steve Cai')

	print ('number of students in Course1: ', Course1.getNumOfStudents())
	students=Course1.getStudents()
	for student in students:
		print (student,end=', ')
	print ('\nnumber of students in Course2: ',Course2.getNumOfStudents())

if __name__=='__main__':
	main()