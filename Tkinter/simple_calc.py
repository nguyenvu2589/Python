from Tkinter import *


def calculator(source, side):
	storeObj = Frame(source, borderwidth= 1, bd = 2, bg= "powder blue")
	storeObj.pack(side= side, expand=YES, fill = BOTH)
	return storeObj

def button (source, side, text, command= None):
	storeObj = Button(source, text=text, command = command)
	storeObj.pack(side=side, expand = YES, fill=BOTH)
	return storeObj

class appp(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.option_add('*Front', 'arial 20 bold')
		self.pack(expand = YES, fill= BOTH)
		self.master.title('Calculator')

		display = StringVar()
		Entry(self, relief= RIDGE, textvariable=display,justify='right', bd=30,bg="gray").pack(expand=YES, fill = BOTH)

		for clearBut in (["CE"], ["C"]):
			erase = calculator(self, TOP)
			for ichar in clearBut:
				button(erase, LEFT, ichar, lambda storeObj=display, q= ichar:storeObj.set(''))

		for numBut in ("789/", "456*", "123-", "0.+"):
			numFunct = calculator(self, TOP)
			for EqualBut in numBut:
				button(numFunct, LEFT, EqualBut, lambda storeObj=display, q =EqualBut: storeObj.set(storeObj.get() +q))

		EqualButton = calculator(self, TOP)
		for EqualBut in "=":
			if EqualBut == "=":
				btniEquals = button(EqualButton, LEFT, EqualBut)
				btniEquals.bind ('<ButtonRelease-1>', lambda e, s=self,storeObj=display:s.calc(storeObj), '+')
			else:
				btniEquals = button(EqualButton, LEFT, EqualBut,lambda storeObj=display, s = ' %s'%EqualBut: storeObj.set(storeObj.get()+s))

	def calc(self, display):
		try: 
			display.set(eval(display.get()))
		except:
			display.set("Error")
if __name__ == '__main__':
	appp().mainloop()

