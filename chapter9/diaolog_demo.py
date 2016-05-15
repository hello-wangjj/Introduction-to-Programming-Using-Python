import tkinter.messagebox
import tkinter.simpledialog
import tkinter.colorchooser

tkinter.messagebox.showinfo('showinfo','this is an info msg')
tkinter.messagebox.showwarning('showwarning','this is a warning')
tkinter.messagebox.showerror('showerror','this is an error')

isYes=tkinter.messagebox.askyesno('askyeno','continue?')
print(isYes)

isOk=tkinter.messagebox.askokcancel('askcancel','Ok?')
print(isOk)

isYesNoCancel=tkinter.messagebox.askyesnocancel('askyesnocancel','yes,no cancel?')
print(isYesNoCancel)

name=tkinter.simpledialog.askstring('askstring','enter your name')
print (name)

weight=tkinter.simpledialog.askfloat('askfloat','enter your weight')
print (weight)