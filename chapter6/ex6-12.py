import exFunction

Number_of_Chars=175
Chars_Per_Line=25

for i in range(Number_of_Chars):
	print(exFunction.getRandomLowerCaseLetter(),end='')
	if(i+1)%Chars_Per_Line==0:
		print()