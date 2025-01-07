from tkinter import *

Window = Tk()

Window.geometry("300x400")
Window.title("GUI")

label1 = Label(Window,text = "My first tkinter project",fg = "#ffee6e")
label1.place(x=100,y=100)
button1 = Button(Window,text= "click to see the results",bg = "Red",fg = "yellow")
button1.place(x=100,y=200)
entry1 = Entry()
entry1.place(x=70 , y = 34)
Entry2 = Entry()

Entry2.grid(row= 3,column= 3)
Entry2.pack()

Window.mainloop()