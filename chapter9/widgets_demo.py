import tkinter as tk
# import Tkinter as tk

class Widgets(object):
	"""docstring for Widgets"""
	def __init__(self):
		super(Widgets, self).__init__()
		# self.arg = arg
		window=tk.Tk()
		window.title('widgets demo')

		frame1=tk.Frame(window)
		frame1.pack()
		self.v1=tk.IntVar()
		cbtBold=tk.Checkbutton(frame1,text='Bold',variable=self.v1,command=self.processCheckbutton)
		self.v2=tk.IntVar()
		rbRed=tk.Radiobutton(frame1,text='Red',bg='red',
							variable=self.v2,value=1,command=self.processRadiobutton)
		rbYellow=tk.Radiobutton(frame1,text='Yellow',bg='yellow',
							variable=self.v2,value=2,command=self.processRadiobutton)
		cbtBold.grid(row=1,column=1)
		rbRed.grid(row=1,column=2)
		rbYellow.grid(row=1,column=3)

		frame2=tk.Frame(window)
		frame2.pack()
		label=tk.Label(frame2,text='enter your name:')
		self.name=tk.StringVar()
		entryName=tk.Entry(frame2,textvariable=self.name)
		btGetName=tk.Button(frame2,text='Get name',command=self.processButton)
		# self.msg=tk.StringVar()
		msg='this is a message demo'
		self.label2=tk.Label(frame2,text=msg)
		label.grid(row=1,column=1)
		entryName.grid(row=1,column=2)
		btGetName.grid(row=1,column=3)
		self.label2.grid(row=1,column=4)

		self.message=tk.Label(window,text='hello wangjj')
		self.message.pack()



		text=tk.Text(window)
		text.pack()
		text.insert(tk.END,'tip\nthe best way to learn tkinter is to read')
		text.insert(tk.END,'these carefully designed examples and use them')
		text.insert(tk.END,'to create your applications')

		window.mainloop()

	def processCheckbutton(self):
		if self.v1.get()==1:
			self.message['font']='bold'
		elif self.v1.get()==0:
			self.message['font']=' italic'
		print('check button is '+('checked' if self.v1.get()==1 else 'unchecked'))
	def processRadiobutton(self):
		if self.v2.get()==1:
			self.message['fg']='red'
		elif self.v2.get()==2:
			self.message['fg']='yellow'


		print(('red ' if self.v2.get()==1 else 'yellow ') +'is selected')
	def processButton(self):
		print('your name is '+self.name.get())
		self.label2['text']=self.name.get()
Widgets()