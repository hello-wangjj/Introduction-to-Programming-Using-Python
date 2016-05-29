import random
import time
NUMBER_OF_ELEMENTS=1000

lst=list(range(NUMBER_OF_ELEMENTS))
random.shuffle(lst)

s=set(lst)

startTime=time.time()
for i in range(NUMBER_OF_ELEMENTS):
	i in s
endTime=time.time()
runTime=int((endTime-startTime)*1000)
print('To test if ',NUMBER_OF_ELEMENTS,'elements are in the set\n','the runTime is ',runTime,'millisseconds')

startTime=time.time()
for i in range(NUMBER_OF_ELEMENTS):
	i in lst
endTime=time.time()
runTime=int((endTime-startTime)*1000)
print('To test if ',NUMBER_OF_ELEMENTS,'elements are in the list\n','the runTime is ',runTime,'millisseconds')

startTime=time.time()
for i in range(NUMBER_OF_ELEMENTS):
	s.remove(i)
endTime=time.time()
runTime=int((endTime-startTime)*1000)
print('To remove ',NUMBER_OF_ELEMENTS,'elements are in the set\n','the runTime is ',runTime,'millisseconds')

startTime=time.time()
for i in range(NUMBER_OF_ELEMENTS):
	lst.remove(i)
endTime=time.time()
runTime=int((endTime-startTime)*1000)
print('To remove ',NUMBER_OF_ELEMENTS,'elements are in the lst\n','the runTime is ',runTime,'millisseconds')
