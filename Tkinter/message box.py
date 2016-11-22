from Tkinter import *
import tkMessageBox


root = Tk()

tkMessageBox.showinfo("Window Tittle", "I dont know what app it is")

answer = tkMessageBox.askquestion("Question 1:", "Do you like silly faces ?")
what = tkMessageBox.askokcancel(" Question 2 :", "really ?")

if answer == 'yes':
	print ":)"
	root.quit()

else : 
	print "OMG why not ???"
	root.quit

root.mainloop()