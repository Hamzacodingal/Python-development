from tkinter import *

screen = Tk()

screen.geometry("400x400")

Entry1 = Entry()
Entry1.place(x=100,y=50)
Enrty2 = Entry()
Enrty2.place(x=100,y=100) 

button1 = Button(text="+")
button1.place(x=100,y=150)

button2 = Button(text="-")
button2.place(x=200,y=150)
button3 = Button(text="x")
button3.place(x=100,y=200)
button4 = Button(text="/")
button4.place(x=200,y=200)

label1 = Label(text = "Answer::::")
label1.place(x=150,y=300)

screen.mainloop()