from Tkinter import *

root = Tk()




def leftClick(event):
	print "Left Click"

def rightClick(event):
	print "Right Click"

def MiddleClick(event):
	print "MiddleClick"

frame = Frame(root, width = 300, height = 400)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", MiddleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()


root.mainloop()