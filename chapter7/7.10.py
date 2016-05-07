import time
class Time(object):
	"""docstring for Time"""
	def __init__(self):
		super(Time, self).__init__()
		# self.arg = arg
		self.setTime(int(time.time()))

	def setTime(self,elapseTime):
		self.__second=elapseTime%60

		totalMinutes=elapseTime//60
		self.__minute=totalMinutes%60

		totalHour=totalMinutes//60
		self.__hour=totalHour%24

	def getHour(self):
		return self.__hour
	def getMinute(self):
		return self.__minute
	def getSecond(self):
		return self.__second
def main():
	currentTime=Time()
	print('current time is '+str(currentTime.getHour())+':'\
		+str(currentTime.getMinute())+':'+str(currentTime.getSecond()))

	elapseTime=eval(input('enter the elapseTime: '))
	currentTime.setTime(elapseTime)
	print('the hour:minute:second for the elapse Time is '+str(currentTime.getHour())+':'\
		+str(currentTime.getMinute())+':'+str(currentTime.getSecond()))
if __name__=='__main__':
	main()
