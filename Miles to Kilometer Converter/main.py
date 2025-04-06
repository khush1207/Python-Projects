from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=10, pady=10)

label1 = Label(text="Miles", font=("Arial", 12, "bold"))
label1.grid(column=2, row=0)
label1.config(padx=10, pady=10)
label2 = Label(text="is equal to", font=("Arial", 12, "bold"))
label2.grid(column=0, row=1)
label2.config(padx=10, pady=10)
label3 = Label(text="Km", font=("Arial", 12, "bold"))
label3.grid(column=2, row=1)
label3.config(padx=10, pady=10)
label4 = Label(text="0", font=("Arial", 12, "bold"))
label4.grid(column=1, row=1)
label4.config(padx=10, pady=10)


def conversion():
    convert = round(float(input.get()) * 1.609, 3)
    label4.config(text=convert)


button = Button(text="Calculate", command=conversion, font=("Arial", 12, "bold"))
button.grid(column=1, row=2)
button.config(padx=10, pady=10)

input = Entry()
input.grid(column=1, row=0)

window.mainloop()
