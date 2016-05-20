import tkinter as tk
import tkinter.messagebox
import random

class SterpControl(object):
	"""docstring for SterpControl"""
	def __init__(self):
		super(SterpControl, self).__init__()
		# self.arg = arg
		self.list=[x for x in range(1,20)]
		self.reset()
		self.key=0

	def reset(self):
		self.i=-1
		self.done=False
		random.shuffle(self.list)
		self.drawStep()

	def step(self):
		if self.done:
			tkinter.messagebox.showinfo('showinfo','key is found')
			return
		if self.i==-1:
			self.i+=1
		self.drawStep()
		if self.i>=0 and self.list[self.i]==self.key:
			self.done=True
			tkinter.messagebox.showinfo('showinfo','key is found')
		elif self.i>=len(self.list)-1:
			tkinter.messagebox.showinfo('showinfo','key is not found')
		else:
			self.i+=1
	def drawStep(self):
		# pass
		bottomGap=10
		canvas.delete('line')
		canvas.create_line(10,height-bottomGap,width-10,height-bottomGap,tag='line')
		barWidth=(width-20)/len(self.list)
		maxCount=int(max(self.list))
		for i in range(len(self.list)):
			canvas.create_rectangle(i * barWidth + 10, (height - bottomGap) * (1 - self.list[i] / (maxCount + 4)), 
                (i + 1) * barWidth + 10, height - bottomGap, tag = "line")            
			canvas.create_text(i * barWidth + 10 + barWidth / 2, (height - bottomGap) * ( 1 - self.list[i] / (maxCount + 4)) - 8, 
                               text = str(self.list[i]), tag = "line")

		if self.i >= 0:
			canvas.create_rectangle(self.i * barWidth + 10, (height - bottomGap) * ( 1 - self.list[self.i] / (maxCount + 4)), 
                                    (self.i + 1) * barWidth + 10, height - bottomGap, fill = "red", tag = "line")


def step():
	# pass
	control.key=float(key.get())
	control.step()
def reset():
	# pass
	control.reset()

window=tk.Tk()
window.title('linear searche animation')

width=340
height=150
radius=2
canvas=tk.Canvas(window,width=width,height=height)
canvas.pack()

frame=tk.Frame(window)
frame.pack()
tk.Label(frame,text='enter a key (in float): ').pack(side=tk.LEFT)
key=tk.StringVar()
tk.Entry(frame,textvariable=key,justify=tk.RIGHT,width=5).pack(side=tk.LEFT)
tk.Button(frame,text='step',command=step).pack(side=tk.LEFT)
tk.Button(frame,text='reset',command=reset).pack(side=tk.LEFT)

control=SterpControl()
control.drawStep()

window.mainloop()

