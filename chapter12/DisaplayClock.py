import tkinter as tk
from StillClock import StillClock

class DisplayClock(object):
	"""docstring for DisplayClock"""
	def __init__(self):
		super(DisplayClock, self).__init__()
		# self.arg = arg
		window=tk.Tk()
		window.title('change clock time')

		self.clock=StillClock(window)
		self.clock.pack()

		frame=tk.Frame(window)
		frame.pack()

		tk.Label(frame,text='hour: ').pack(side=tk.LEFT)
		self.hour=tk.IntVar()
		self.hour.set(self.clock.getHour())
		tk.Entry(frame,textvariable=self.hour,width=2).pack(side=tk.LEFT)

		tk.Label(frame,text='minute: ').pack(side=tk.LEFT)
		self.minute=tk.IntVar()
		self.minute.set(self.clock.getMinute())
		tk.Entry(frame,textvariable=self.minute,width=2).pack(side=tk.LEFT)

		tk.Label(frame,text='second: ').pack(side=tk.LEFT)
		self.second=tk.IntVar()
		self.second.set(self.clock.getSecond())
		tk.Entry(frame,textvariable=self.second,width=2).pack(side=tk.LEFT)

		tk.Button(frame,text='set new time',command=self.setNewTime).pack(side=tk.LEFT)
		window.mainloop()

	def setNewTime(self):
		self.clock.setHour(self.hour.get())
		self.clock.setMinute(self.minute.get())
		self.clock.setSecond(self.second.get())

if __name__=='__main__':
	DisplayClock()