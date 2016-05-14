import tkinter as tk
class MenuDemo(object):
	"""docstring for MenuDemo"""
	def __init__(self):
		super(MenuDemo, self).__init__()
		# self.arg = arg
		window=tk.Tk()
		window.title('Menu demo')

		menubar=tk.Menu(window)
		window.config(menu=menubar)

		operationMenu=tk.Menu(menubar,tearoff=0)
		menubar.add_cascade(label='Operation',menu=operationMenu)
		operationMenu.add_command(label='add',command=self.add)
		operationMenu.add_command(label='subtract',command=self.subtract)
		operationMenu.add_separator()
		operationMenu.add_command(label='Multiply',command=self.multiply)
		operationMenu.add_command(label='Divide',command=self.divide)

		exitMenu=tk.Menu(menubar,tearoff=0)
		menubar.add_cascade(label='Exit',menu=exitMenu)
		exitMenu.add_command(label='exit',command=window.quit)

		frame0=tk.Frame(window)
		frame0.grid(row=1,column=1,sticky=tk.W)

		plusImg=tk.PhotoImage(file='images/1.gif')
		minusImg=tk.PhotoImage(file='images/2.gif')
		timesImg=tk.PhotoImage(file='images/3.gif')
		divideImg=tk.PhotoImage(file='images/4.gif')

		tk.Button(frame0,image=plusImg,command=self.add).grid(row=1,column=1,sticky=tk.W)
		tk.Button(frame0,image=minusImg,command=self.subtract).grid(row=1,column=2)
		tk.Button(frame0,image=timesImg,command=self.multiply).grid(row=1,column=3)
		tk.Button(frame0,image=divideImg,command=self.divide).grid(row=1,column=4)

		frame1=tk.Frame(window)
		frame1.grid(row=2,column=1,pady=10)
		tk.Label(frame1,text='Number 1:').pack(side=tk.LEFT)
		self.v1=tk.StringVar()
		tk.Entry(frame1,textvariable=self.v1,justify=tk.RIGHT).pack(side=tk.LEFT)
		frame1.grid(row=2,column=1,pady=10)

		tk.Label(frame1,text='Number 2:').pack(side=tk.LEFT)
		self.v2=tk.StringVar()
		tk.Entry(frame1,textvariable=self.v2,justify=tk.RIGHT).pack(side=tk.LEFT)
		frame1.grid(row=2,column=1,pady=10)
		tk.Label(frame1,text='Result:').pack(side=tk.LEFT)
		self.v3=tk.StringVar()
		tk.Entry(frame1,textvariable=self.v3,justify=tk.RIGHT,width=5).pack(side=tk.LEFT)

		frame2=tk.Frame(window)
		frame2.grid(row=3,column=1,pady=10,sticky=tk.E)
		tk.Button(frame2,text='add',command=self.add).pack(side=tk.LEFT)
		tk.Button(frame2,text='subtract',command=self.subtract).pack(side=tk.LEFT)
		tk.Button(frame2,text='multiply',command=self.multiply).pack(side=tk.LEFT)
		tk.Button(frame2,text='divide',command=self.divide).pack(side=tk.LEFT)		

		window.mainloop()

	def add(self):
		self.v3.set(eval(self.v1.get())+eval(self.v2.get()))

	def subtract(self):
		self.v3.set(eval(self.v1.get())-eval(self.v2.get()))
	def multiply(self):
		self.v3.set(eval(self.v1.get())*eval(self.v2.get()))
	def divide(self):
		self.v3.set(eval(self.v1.get())/eval(self.v2.get()))

MenuDemo()