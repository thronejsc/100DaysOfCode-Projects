from tkinter import *


window = Tk()
window.title("Mile to Kilometer Converter")

window.config(padx=20, pady=20)
is_equal_to = Label(text="is equal to ", font=("Arial", 12, "bold"))
is_equal_to.grid(column=0, row=1)

miles = Label(text="Miles", font=("Arial", 12, "bold"))
miles.grid(column=2, row=0)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)


km = Label(text="Km", font=("Arial", 12, "bold"))
km.grid(column=2, row=1)

km_result = Label(font=("Arial", 12, "bold"))
km_result.grid(column=1, row=1)

def calculate():
    miles_a = int(miles_input.get())
    result = miles_a * 1.609344
    km_result.config(text=(round(result,2)))


btn_calculate = Button(text="Calculate!",command=calculate)
btn_calculate.grid(column=1, row=2)
window.mainloop()
