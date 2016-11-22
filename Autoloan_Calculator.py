from Tkinter import *
from math import *
import tkMessageBox


fields = ('Vehicle Price:', 'Down Payments:', 'Trade-in Value:', 'Sale Tax:', 
	      'Interest Rate:', 'Term:','Loan:', 'Monthly Payment:')

# fix 2 decimal point for float.
# add $ and % sign 
# update monthly payment and Loan. 
def updateResult(entries, loan, A):
	vehicalPrice =(float(entries['Vehicle Price:'].get()))
	entries['Vehicle Price:'].delete(0,END)
	entries['Vehicle Price:'].insert(0,"$ %.2f" % vehicalPrice )

	downPayment =(float(entries['Down Payments:'].get()))
	entries['Down Payments:'].delete(0,END)
	entries['Down Payments:'].insert(0,"$ %.2f" % downPayment )

	tradeIn =(float(entries['Trade-in Value:'].get()))
	entries['Trade-in Value:'].delete(0,END)
	entries['Trade-in Value:'].insert(0,"$ %.2f" % tradeIn )

	tax =(float(entries['Sale Tax:'].get()))
	entries['Sale Tax:'].delete(0,END)
	entries['Sale Tax:'].insert(0,"%% %.2f" % tax )

	rate =(float(entries['Interest Rate:'].get()))
	entries['Interest Rate:'].delete(0,END)
	entries['Interest Rate:'].insert(0,"%% %.2f" % rate )

	term =(int(entries['Term:'].get()))
	entries['Term:'].delete(0,END)
	entries['Term:'].insert(0,"%d months" % term )

	entries['Loan:'].delete(0,END)
	entries['Loan:'].insert(0,"$ %.2f" % loan )

	entries['Monthly Payment:'].delete(0,END)
	entries['Monthly Payment:'].insert(0, "$ %.2f" % A)
	entries['Monthly Payment:'].configure(font = "Times 15 bold")

# check for 0 value at all entry except Loan and Monthly payment . Also 
# check for interest rate and sale tax < 100. 
def errorChecking(root,entries):
	if ((float(entries['Sale Tax:'].get()) > 100) or (float(entries['Sale Tax:'].get()) < 0) or
	(float(entries['Interest Rate:'].get()) > 100) or (float(entries['Interest Rate:'].get()) < 0) ): 
		tkMessageBox.showinfo("Invalid Value " , "Either Sale tax or Interest rate is invalid \n Please try again" )

	for field in fields:
		if field == 'Loan:':
			break
		temp = float(entries[field].get())
		if temp == 0:
			tkMessageBox.showinfo("Invalid Value " , "Value of %s is empty. \n Please try again" % field)

# calculate monthly payment and loan
def calculate(entries):
	errorChecking(root, entries)
	# interest rate per month
	r = (float(entries['Interest Rate:'].get()) / 100) / 12
	# tax 0.0 ....
	tax = (float (entries['Sale Tax:'].get()) / 100)
	# principle.
	P = ((float(entries['Vehicle Price:'].get()) * (1+tax))  -
		    float(entries['Down Payments:'].get()) - 
		    float(entries['Trade-in Value:'].get()))
	# total number of months
	n= int( entries['Term:'].get())
	f1 = r*((1+r)**n)
	f2 = (1+r)**n -1
	# A is monthly paymnet
	A = P * f1 / f2
	updateResult(entries, P, A)
	print ("This is A: %f " % A )

# insert all the lable and entry
# also store entry into dict. 
def makeform (root, fields):
	Label(root, text="Auto Loan Calculator", justify= CENTER, 
		relief = RAISED,fg="red",font="Times 30 bold",).pack()
	entries = {}
	for field in fields:
		frame = Frame(root,bg = "grey" )
		Label(frame,text = field, width = 15, anchor='w', bg = "grey").pack(side=LEFT)
		entri = Entry(frame)
		entri.insert(0, "0")
		frame.pack(side =TOP, fill=X,padx =5, pady=5)
		entri.pack(side= RIGHT, expand= YES, fill =X)
		entries[field] = entri
	return entries 

if __name__ == '__main__':
	root = Tk()
	frame = Frame(root, bg = "grey")
	# set up display.
	entri = makeform(frame, fields)
	# 2 button
	b1 = Button(frame, text='Show',command =(lambda e=entri: calculate(e))).pack(side=LEFT, padx=5,pady=5)
	b2 = Button(frame,text='Quit', command= root.quit).pack(side=LEFT, padx =5, pady=5)
	frame.pack(expand = YES, fill = BOTH)
	root.mainloop()


