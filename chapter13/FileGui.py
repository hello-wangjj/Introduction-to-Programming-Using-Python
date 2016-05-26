import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

class FileEditor(object):
	"""docstring for FileEditor"""
	def __init__(self):
		super(FileEditor, self).__init__()
		# self.arg = arg
		window=tk.Tk()
		window.title('simple file edit')

		menubar=tk.Menu(window)
		window.config(menu=menubar)

		operationMenu=tk.Menu(menubar,tearoff=0)
		menubar.add_cascade(label='File',menu=operationMenu)
		operationMenu.add_command(label='open',command=self.openFile)
		operationMenu.add_command(label='save',command=self.saveFile)

		frame0=tk.Frame(window)
		frame0.grid(row=1,column=1,sticky=tk.W)
		openImg=tk.PhotoImage(file='images/open.gif')
		saveImg=tk.PhotoImage(file='images/save.gif')
		tk.Button(frame0,image=openImg,command=self.openFile).grid(row=1,column=1,sticky=tk.W)
		tk.Button(frame0,image=saveImg,command=self.saveFile).grid(row=1,column=2)

		frame1=tk.Frame(window)
		frame1.grid(row=2,column=1)
		scrollBar=tk.Scrollbar(frame1)
		scrollBar.pack(side=tk.RIGHT,fill=tk.Y)
		self.text=tk.Text(frame1,width=40,height=20,wrap=tk.WORD,yscrollcommand=scrollBar.set)
		self.text.pack()
		scrollBar.config(command=self.text.yview)
		window.mainloop()



	def openFile(self):
		filenameforReading=askopenfilename()
		infile=open(filenameforReading,'r')
		self.text.insert(tk.END,infile.read())
		infile.close()

	def saveFile(self):
		filenameforWriting=asksaveasfilename()
		outfile=open(filenameforWriting,'w')
		outfile.write(self.text.get(1.0,tk.END))
		outfile.close()
if __name__=='__main__':
	FileEditor()