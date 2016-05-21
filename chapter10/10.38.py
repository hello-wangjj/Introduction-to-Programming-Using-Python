import tkinter as tk
import tkinter.messagebox
import random

class StepControl(object):
	"""docstring for StepControl"""
	def __init__(self):
		super(StepControl, self).__init__()
		# self.arg = arg
		self.list=[x for x in range(1,20)]
		self.reset()
		self.key=0

	def reset(self):
		# pass
		self.i=0
		self.done=False
		random.shuffle(self.list)
		self.drawStep()

	def step(self):
		# pass
		if self.i>len(self.list)-1:
			tkinter.messagebox.showinfo('showinfo','the list is already sorted')
			return
		#假定第一个就是最小值
		currentMin=self.list[self.i]
		currentMinIndex=self.i
		for j in range(self.i+1,len(self.list)):
			#找到最小值和他的index
			if currentMin>self.list[j]:
				currentMin=self.list[j]
				currentMinIndex=j
		#
		if currentMinIndex!=self.i:
			self.list[currentMinIndex]=self.list[self.i]
			self.list[self.i]=currentMin
		self.drawStep()
		self.i+=1


	def drawStep(self):
		# pass
		bottomGap = 10
		canvas.delete("line")
		canvas.create_line(10, height - bottomGap, width - 10, height - bottomGap, tag = "line")
		barWidth = (width - 20) / len(self.list)
        
		maxCount = int(max(self.list))
		for i in range(len(self.list)):
			canvas.create_rectangle(i * barWidth + 10, (height - bottomGap) * (1 - self.list[i] / (maxCount + 4)), 
                (i + 1) * barWidth + 10, height - bottomGap, tag = "line")       
                         
			canvas.create_text(i * barWidth + 10 + barWidth / 2, (height - bottomGap) * ( 1 - self.list[i] / (maxCount + 4)) - 8, 
                               text = str(self.list[i]), tag = "line")

		if self.i >= 0:
			canvas.create_rectangle(self.i * barWidth + 10, (height - bottomGap) * ( 1 - self.list[self.i] / (maxCount + 4)), 
                                    (self.i + 1) * barWidth + 10, height - bottomGap, fill = "red", tag = "line")


def step():
	control.step()
	# pass

def reset():
	# pass
	control.reset()

window=tk.Tk()
window.title('Selection Sort Animation')

width=340
height=150
radius=2
canvas=tk.Canvas(window,width=width,height=height)
canvas.pack()

frame=tk.Frame(window)
frame.pack()
tk.Button(frame,text='Step',command=step).pack(side=tk.LEFT)
tk.Button(frame,text='reset',command=reset).pack(side=tk.LEFT)
control=StepControl()
control.drawStep()
window.mainloop()
