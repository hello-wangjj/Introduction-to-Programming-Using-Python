import tkinter as tk
class Gridmaneger(object):
	"""docstring for Gridmaneger"""
	def __init__(self):
		super(Gridmaneger, self).__init__()
		# self.arg = arg
		window=tk.Tk()
		window.title('grid manager demo')
		message=tk.Message(window,text='this message widget occupies three rows and two columns')
		message.grid(row=1,column=1,rowspan=3,columnspan=2)
		tk.Label(window,text='first name:').grid(row=1,column=3)
		tk.Entry(window).grid(row=1,column=4,padx=5,pady=5)
		tk.Label(window,text='laset name:').grid(row=2,column=3)
		tk.Entry(window).grid(row=2,column=4)
		tk.Button(window,text='get name').grid(row=3,padx=5,pady=5,column=4,sticky=tk.E)
		window.mainloop()
Gridmaneger()
