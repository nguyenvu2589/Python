from Tkinter import *

root = Tk()

# canvas = Canvas(root, width = 200, height = 400)

# canvas.pack()

# blackLine = canvas.create_line(0,0,200,200)
# redLine = canvas.create_line(0,200,200,200, fill = "red")

# greenBox = canvas.create_rectangle(25,25,150,60, fill= "green")
# canvas.delete(redLine)

photo = PhotoImage(file="IMG_3071.jpg")
label = Label(root, image = photo)
label.pack(side= LEFT)


root.mainloop()