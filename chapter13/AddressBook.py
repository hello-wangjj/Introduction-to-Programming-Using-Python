import pickle
import os.path
import tkinter as tk
import tkinter.messagebox

class Adress(object):
	"""docstring for Adress"""
	def __init__(self, name,street,city,state,zip):
		super(Adress, self).__init__()
		# self.arg = arg
		self.name=name
		self.street=street
		self.city=city
		self.state=state
		self.zip=zip

class AdressBook(object):
	"""docstring for AdressBook"""
	def __init__(self):
		super(AdressBook, self).__init__()
		# self.arg = arg

		#!-----
		#窗口设置
		window=tk.Tk()
		window.title('AdressBook')

		self.nameVar=tk.StringVar()
		self.streetVar=tk.StringVar()
		self.cityVar=tk.StringVar()
		self.stateVar=tk.StringVar()
		self.zipVar=tk.StringVar()

		frame1=tk.Frame(window)
		frame1.pack()
		tk.Label(frame1,text='name').grid(row=1,column=1,sticky=tk.W)
		tk.Entry(frame1,textvariable=self.nameVar,width=40).grid(row=1,column=2)

		frame2=tk.Frame(window)
		frame2.pack()
		tk.Label(frame2,text='street').grid(row=1,column=1,sticky=tk.W)
		tk.Entry(frame2,textvariable=self.streetVar,width=40).grid(row=1,column=2)

		frame3=tk.Frame(window)
		frame3.pack()
		tk.Label(frame3,text='city').grid(row=1,column=1,sticky=tk.W)
		tk.Entry(frame3,textvariable=self.cityVar,width=5).grid(row=1,column=2)
		tk.Label(frame3,text='state').grid(row=1,column=3,sticky=tk.W)
		tk.Entry(frame3,textvariable=self.stateVar,width=5).grid(row=1,column=4)
		tk.Label(frame3,text='zip').grid(row=1,column=5,sticky=tk.W)
		tk.Entry(frame3,textvariable=self.zipVar,width=5).grid(row=1,column=6)

		frame4=tk.Frame(window)
		frame4.pack()
		tk.Button(frame4,text='add',command=self.add).grid(row=1,column=1)
		btFirst=tk.Button(frame4,text='First',command=self.First).grid(row=1,column=2)
		btNext=tk.Button(frame4,text='Next',command=self.Next).grid(row=1,column=3)
		btPrevious=tk.Button(frame4,text='Previous',command=self.Previous).grid(row=1,column=4)
		btLast=tk.Button(frame4,text='Last',command=self.Last).grid(row=1,column=5)

		self.addressList=self.loadAddress()
		self.current=0
		if(len(self.addressList)>0):
			self.setAddress()
		window.mainloop()
		#窗口



	def saveAddress(self):
		outfile=open('address.dat','wb')
		pickle.dump(self.addressList, outfile)
		tkinter.messagebox.showinfo('address saved','a new address is saved')
		outfile.close()

	def loadAddress(self):
		if not os.path.isfile('address.dat'):
			return []
		try:
			infile=open('address.dat','rb')
			addressList=pickle.load(infile)
		except EOFError:
			addressList=[]
		infile.close()
		return addressList

	def add(self):
		address=Adress(self.nameVar.get(),self.streetVar.get(),self.cityVar.get(),self.stateVar.get(),self.zipVar.get())
		self.addressList.append(address)
		self.saveAddress()

	def First(self):
		self.current=0
		self.setAddress()

	def Next(self):
		if self.current<len(self.addressList)-1:
			self.current+=1
			self.setAddress()

	def Previous(self):
		if self.current>0:
			self.current-=1
			self.setAddress()

	def Last(self):
		self.current=len(self.addressList)-1
		self.setAddress()

	def setAddress(self):
		self.nameVar.set(self.addressList[self.current].name)
		self.streetVar.set(self.addressList[self.current].street)
		self.cityVar.set(self.addressList[self.current].city)
		self.stateVar.set(self.addressList[self.current].state)
		self.zipVar.set(self.addressList[self.current].zip)

if __name__=="__main__":
	AdressBook()
		
