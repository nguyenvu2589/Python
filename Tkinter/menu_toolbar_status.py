from Tkinter import *

def donothing():
	print "this really do nothing... !"

root = Tk()
menu = Menu(root)
root.config(menu= menu)

# Menu 
subMenu = Menu(menu)
menu.add_cascade(label = "File", menu= subMenu)
subMenu.add_command(label = "New File", command= donothing)
subMenu.add_command(label = "Save" , command = donothing)
subMenu.add_separator()
subMenu.add_command(label = "Exit", command= root.quit())

editMenu = Menu(menu)
menu.add_cascade(label = "Edit", menu= editMenu)
editMenu.add_command(label= "Cut", command= donothing)
editMenu.add_command(label = "Paste", command= donothing)

# adding toolbar 
# padx or pady ... give a little space between direction
# fill = X or Y .... fill the frame in X, Y direction 

toolBar = Frame(root,bg="blue")

insertButton = Button(toolBar, text ="Insert Image", command= donothing)
insertButton.pack(side = LEFT, padx=2 , pady = 2)
printButton = Button(toolBar, text ="Print", command= donothing)
printButton.pack(side = LEFT, padx=2 , pady = 2)
toolBar.pack(side=TOP, fill= X)

# Status Bar
# bd = border,
# relief = SUNKEN ... sunking in .... 
# anchor ....where does it start.
status = Label(root, text = "Getting ready....", bd = 1, relief= SUNKEN, anchor = W)
status.pack(side =BOTTOM, fill = X)
root.mainloop()