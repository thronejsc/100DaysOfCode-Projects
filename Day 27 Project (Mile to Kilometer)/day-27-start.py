from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# creating label
label = Label(text="I am a label", font = ("Arial", 24, "bold"))
label.grid(column=0, row=0)

label["text"] = "New Text"


# create button
def button_clicked():
    label["text"] = entry.get()


button = Button(text="Click me", command=button_clicked)
button.grid(column=1,row=1)
button_two = Button(text="Click me", command=button_clicked)
button_two.grid(column=2,row=0)

# create entry (input)
entry = Entry(width=10)
entry.grid(column=3,row=2)



window.mainloop()