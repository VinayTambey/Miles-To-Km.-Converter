from tkinter import *

def calculate():
    miles = float(Miles_input.get())
    km = round(miles * 1.609344, 2)
    km_result_label.config(text=f"{km}")

# Window
window = Tk()
window.title("Miles to kilometer Converter")
window.config(padx=20, pady=20)

# Miles Input
Miles_input = Entry(width=7)
Miles_input.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# is equal Label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Kilometer result label
km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

# Kilometer label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)


# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()