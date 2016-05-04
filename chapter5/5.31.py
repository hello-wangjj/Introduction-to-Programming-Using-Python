year= eval(input("Enter a year: "))
firstDay = eval(input("Enter the first day of the year: "))

numberOfDaysInMonth = 0
# Display calendar for each month
for month in range(1, 12 + 1):
    # Display Calendar title
    if month == 1:
        # print("January 1,", str(year), "is ", end = "")
        print (format('January '+str(year),'^40s'))
        print ('-'*40)
        print ('Sun  Mon  Tue  Wed  Thu  Fri  Sat  ')
        numberOfDaysInMonth = 31
    elif month == 2:
        # print("February 1,", str(year), "is ", end = "")
        print (format('February '+str(year),'^40s'))
        print ('-'*40)
        print ('Sun  Mon  Tue  Wed  Thu  Fri  Sat  ')
        if (year% 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            numberOfDaysInMonth = 29
        else:
            numberOfDaysInMonth = 28
    elif month == 3:
        # print("March 1,", str(year), "is ", end = "")
        print (format('March '+str(year),'^40s'))
        print ('-'*40)
        print ('Sun  Mon  Tue  Wed  Thu  Fri  Sat  ')
        numberOfDaysInMonth = 31
    elif month == 4:
        # print("April 1,", str(year), "is ", end = "")
        print (format('April '+str(year),'^40s'))
        print ('-'*40)
        print ('Sun  Mon  Tue  Wed  Thu  Fri  Sat  ')
        numberOfDaysInMonth = 30
    elif month == 5:
        # print("May 1,", str(year), "is ", end = "")
        print (format('May '+str(year),'^40s'))
        print ('-'*40)
        print ('Sun  Mon  Tue  Wed  Thu  Fri  Sat  ')
        numberOfDaysInMonth = 31
    elif month == 6:
        # print("June 1,", str(year), "is ", end = "")
        print (format('June '+str(year),'^40s'))
        print ('-'*40)
        print ('Sun  Mon  Tue  Wed  Thu  Fri  Sat  ')
        numberOfDaysInMonth = 30
    elif month == 7:
        # print("July 1,", str(year), "is ", end = "")
        print (format('July '+str(year),'^40s'))
        print ('-'*40)
        print ('Sun  Mon  Tue  Wed  Thu  Fri  Sat  ')
        numberOfDaysInMonth = 31
    elif month == 8:
        # print("August 1,", str(year), "is ", end = "")
        print (format('August '+str(year),'^40s'))
        print ('-'*40)
        print ('Sun  Mon  Tue  Wed  Thu  Fri  Sat  ')
        numberOfDaysInMonth = 31
    elif month == 9:
        # print("September 1,", str(year), "is ", end = "")
        print (format('September '+str(year),'^40s'))
        print ('-'*40)
        print ('Sun  Mon  Tue  Wed  Thu  Fri  Sat  ')
        numberOfDaysInMonth = 30
    elif month == 10:
        # print("October 1,", str(year), "is ", end = "")
        print (format('October '+str(year),'^40s'))
        print ('-'*40)
        print ('Sun  Mon  Tue  Wed  Thu  Fri  Sat  ')
        numberOfDaysInMonth = 31
    elif month == 11:
        # print("November 1,", str(year), "is ", end = "")
        print (format('November '+str(year),'^40s'))
        print ('-'*40)
        print ('Sun  Mon  Tue  Wed  Thu  Fri  Sat  ')
        numberOfDaysInMonth = 30
    elif (month == 12):
        # print("December 1,", str(year), "is ", end = "")
        print (format('December '+str(year),'^40s'))
        print ('-'*40)
        print ('Sun  Mon  Tue  Wed  Thu  Fri  Sat  ')
        numberOfDaysInMonth = 31

    if firstDay == 0:
        # print("Sunday") 
        count=0
        for i in range(1,numberOfDaysInMonth+1):
        	print (format(i,'<5d'),end='')
        	count+=1
        	if count%7==0:
        		print()
        print()
    elif firstDay == 1:
        # print("Monday") 
        print (' '*5+str(1)+' '*4+str(2)+' '*4+str(3)+' '*4+str(4)+' '*4+str(5))
        count=0
        for i in range(6,numberOfDaysInMonth+1):
        	print (format(i,'<5d'),end='')
        	count+=1
        	if count%7==0:
        		print()
        print()
    elif firstDay == 2:
        # print("Tuesday")
        print (' '*10+str(1)+' '*4+str(2)+' '*4+str(3)+' '*4+str(4)+' '*4+str(5))
        count=0
        for i in range(6,numberOfDaysInMonth+1):
        	print (format(i,'<5d'),end='')
        	count+=1
        	if count%7==0:
        		print()
        print() 
    elif firstDay == 3:
        # print("Wednesday") 
        print (' '*15+str(1)+' '*4+str(2)+' '*4+str(3)+' '*4+str(4))
        count=0
        for i in range(5,numberOfDaysInMonth+1):
        	print (format(i,'<5d'),end='')
        	count+=1
        	if count%7==0:
        		print()
        print()
    elif firstDay == 4:
        # print("Thursday") 
        print (' '*20+str(1)+' '*4+str(2)+' '*4+str(3))
        count=0
        for i in range(4,numberOfDaysInMonth+1):
        	print (format(i,'<5d'),end='')
        	count+=1
        	if count%7==0:
        		print()
        print()
    elif firstDay == 5:
        # print("Friday")
        print (' '*25+str(1)+' '*4+str(2))
        count=0
        for i in range(3,numberOfDaysInMonth+1):
        	print (format(i,'<5d'),end='')
        	count+=1
        	if count%7==0:
        		print()
        print()
    elif firstDay == 6:
        # print("Saturday")
        print (' '*30+str(1))
        count=0
        for i in range(2,numberOfDaysInMonth+1):
        	print (format(i,'<5d'),end='')
        	count+=1
        	if count%7==0:
        		print()
        print()

    # Get the start day for the next month
    firstDay = (firstDay + numberOfDaysInMonth) % 7


# print (format('January 2005','^40s'))