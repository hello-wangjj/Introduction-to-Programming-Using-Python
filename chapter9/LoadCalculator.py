import tkinter as tk

class LoadCalculator(object):
	"""docstring for LoadCalculator"""
	def __init__(self):
		super(LoadCalculator, self).__init__()
		# self.arg = arg
		window=tk.Tk()
		window.title('Load Calculator')


		tk.Label(window,text='Annual Interest Rate:').grid(row=1,column=1,sticky=tk.W)
		tk.Label(window,text='Number of Years:').grid(row=2,column=1,sticky=tk.W)
		tk.Label(window,text='Loan Amount:').grid(row=3,column=1,sticky=tk.W)
		tk.Label(window,text='Monthly Payment:').grid(row=4,column=1,sticky=tk.W)
		tk.Label(window,text='Total Payment:').grid(row=5,column=1,sticky=tk.W)

		self.annualRate=tk.StringVar()
		tk.Entry(window,textvariable=self.annualRate,justify=tk.RIGHT).grid(row=1,column=2)
		self.numberYear=tk.StringVar()
		tk.Entry(window,textvariable=self.numberYear,justify=tk.RIGHT).grid(row=2,column=2)
		self.loanAmount=tk.StringVar()
		tk.Entry(window,textvariable=self.loanAmount,justify=tk.RIGHT).grid(row=3,column=2)
		
		self.monthlyPayment=tk.StringVar()
		monthlyPaymentLabel=tk.Label(window,textvariable=self.monthlyPayment).grid(row=4,column=2,sticky=tk.E)
		self.totalPayment=tk.StringVar()
		totalPaymentLabel=tk.Label(window,textvariable=self.totalPayment).grid(row=5,column=2,sticky=tk.E)

		computeBtn=tk.Button(window,text='compute',command=self.compute).grid(row=6,column=2,sticky=tk.E)

		window.mainloop()

	def compute(self):
		monthlyPay=self.getMonthlyPayment(float(self.loanAmount.get()),
						float(self.annualRate.get()),
						int(self.numberYear.get()))
		self.monthlyPayment.set(format(monthlyPay,'10.2f'))
		totalPay=float(self.monthlyPayment.get())*12*int(self.numberYear.get())
		self.totalPayment.set(format(totalPay,'10.2f'))

	def getMonthlyPayment(self,loanAmount,annualRate,numberYear):
		monthlyPay=loanAmount*annualRate/(1-1/(1+annualRate)**(numberYear*12))
		return monthlyPay

LoadCalculator()

