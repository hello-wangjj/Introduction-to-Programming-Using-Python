#打印日历

def printMonth(year,month):
	printMonthTitle(year,month)

	printMonthBody(year,month)

def printMonthTitle(year,month):
	print(format(getMonthName(month)+str(year),'^42s'))
	print('-'*42)
	print('Sun   Mon   Tue   Wed   Thu   Fri   Sat   ')

def printMonthBody(year,month):
	startDay=getStartDay(year,month)

	number_of_Month=getNumberOfDaysInMonth(year,month)

	# i=0
	for i in range(0,startDay):
		print(' '*6,end='')
	for i in range(1,number_of_Month+1):
		print(format(i,'<6d'),end='')
		if (i+startDay)%7==0:
			print ()

def getMonthName(month):
	Month={1:'January',2:'Febrary',3:'March',4:'April',5:'May',6:'June',7:'July',
			8:'August',9:'September',10:'October',11:'November',12:'December'}
	return Month[month]

def getStartDay(year,month):
	StartDay_For_Jan_1_1800=3
	totalNumberOfDays=getTotalNumberOfDays(year,month)

	return (totalNumberOfDays+StartDay_For_Jan_1_1800)%7

def getTotalNumberOfDays(year,month):
	total=0
	for i in range(1800,year):
		if isLeapYear(i):
			total=total+366
		else:
			total=total+365
	for i in range(1,month):
		total=total+getNumberOfDaysInMonth(year,i)
	return total
def getNumberOfDaysInMonth(year,month):
	if (month==1 or month==3 or month==5 or month==7 or month==8
		or month==10 or month==12):
		return 31
	elif(month==4 or month==6 or month==9 or month==11):
		return 30
	elif month==2:
		return 29 if isLeapYear(year) else 28
	return 0

def isLeapYear(year):
	return year%400==0 or (year%4==0 and year%100!=0)

if __name__=='__main__':
	year=eval(input('please input a year (e.g:2001): '))
	month=eval(input('please input a month between 1 and 12 :'))
	printMonth(year, month)