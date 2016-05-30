import tkinter as tk
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
def openFile():
	# pass
	filenameForReading=askopenfilename()
	filename.set(filenameForReading)

def showResult():
	# pass
	analyseFile(filename.get())

def analyseFile(filename):
	# pass
	try:
		infile=open(filename,'r')
		counts=26*[0]
		text.delete(0.0,tk.END)
		for line in infile:
			countLetters(line.lower(),counts)
		for i in range(len(counts)):
			text.insert(tk.END,chr(ord('a')+i)+' appears '+str(counts[i])+('time' if counts[i]<2 else 'times')+'\n')
		infile.close()
		# return counts
	except IOError:
		tkinter.messagebox.showwarning('Analyze File','File '+filename+' dose not exist')
	# counts=analyseFile(filename.get)
	canvas.delete('line')
	bottomGap=10
	canvas.create_line(10,height-bottomGap,width-10,height-bottomGap,tag='line')
	barWidth=(width-20)/(len(counts))
	maxCount=int(max(counts))
	for i in range(len(counts)):
		canvas.create_rectangle(i*barWidth+10,(height-bottomGap)*(1-counts[i]/(maxCount+4)),
								(i+1)*barWidth+10,height-bottomGap,tag='line')
		canvas.create_text(i*barWidth+10+barWidth/2,(height-bottomGap)*(1-counts[i]/(maxCount+4))-8,
								text=chr(ord('a')+i),tag='line')
		
def countLetters(line,counts):
	# pass
	for ch in line:
		if ch.isalpha():
			counts[ord(ch)-ord('a')]+=1

def drawHistogram():
	analyseFile(filename.get())






window=tk.Tk()
window.title('Occurence of Letters')

frame1=tk.Frame(window)
frame1.pack()

scrollBar=tk.Scrollbar(frame1)
scrollBar.pack(side=tk.RIGHT,fill=tk.Y)
text=tk.Text(frame1,width=60,height=10,wrap=tk.WORD,yscrollcommand=scrollBar.set)
text.pack()
scrollBar.config(command=text.yview)

width=280
height=200

canvas=tk.Canvas(window,width=width,height=height)
canvas.pack()

frame2=tk.Frame(window)
frame2.pack()



tk.Label(frame2,text='enter a file name: ').pack(side=tk.LEFT)
filename=tk.StringVar()
tk.Entry(frame2,width=20,textvariable=filename).pack(side=tk.LEFT)
tk.Button(frame2,text='Browse',command=openFile).pack(side=tk.LEFT)
tk.Button(frame2,text='Show Result',command=showResult).pack(side=tk.LEFT)
tk.Button(frame2,text='Draw Histogram',command=drawHistogram).pack(side=tk.LEFT)






window.mainloop()