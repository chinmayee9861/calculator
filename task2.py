from tkinter import *
from tkinter import messagebox


def click(char):
    num_entry.insert(END, char)


def clear():
    num_entry.delete(0, END)


def equal():
    num = num_entry.get()
    if len(num) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave num field empty!😓")
    else:
        result = str(eval(num))
        num_entry.delete(0, END)
        num_entry.insert(END, result)


windows = Tk()
windows.title("Calculator")
windows.config(padx=30, pady=20)
canvas = Canvas(width=644, height=900)

num_entry = Entry(width=20, font=("lucid", 20, "bold"))
num_entry.grid(row=0, column=0, columnspan=3)
button_9 = Button(text="9", font=("lucid", 20, "bold"), command=lambda: click(9))
button_9.grid(row=1, column=0)

button_8 = Button(text="8", font=("lucid", 20, "bold"), command=lambda: click(8))
button_8.grid(row=1, column=1)

button_7 = Button(text="7", font=("lucid", 20, "bold"), command=lambda: click(7))
button_7.grid(row=1, column=2)

button_6 = Button(text="6", font=("lucid", 20, "bold"), command=lambda: click(6))
button_6.grid(row=2, column=0)

button_5 = Button(text="5", font=("lucid", 20, "bold"), command=lambda: click(5))
button_5.grid(row=2, column=1)

button_4 = Button(text="4", font=("lucid", 20, "bold"), command=lambda: click(4))
button_4.grid(row=2, column=2)

button_3 = Button(text="3", font=("lucid", 20, "bold"), command=lambda: click(3))
button_3.grid(row=3, column=0)

button_2 = Button(text="2", font=("lucid", 20, "bold"), command=lambda: click(2))
button_2.grid(row=3, column=1)

button_1 = Button(text="1", font=("lucid", 20, "bold"), command=lambda: click(1))
button_1.grid(row=3, column=2)

button_C = Button(text="C", padx=2, pady=6, font=("lucid", 19, "bold"), command=clear)
button_C.grid(row=4, column=0)

button_0 = Button(text="0", padx=2, pady=5, font=("lucid", 20, "bold"), command=lambda: click(0))
button_0.grid(row=4, column=1)

button_dec = Button(text=".", padx=4, pady=5, font=("lucid", 20, "bold"), command=lambda: click("."))
button_dec.grid(row=4, column=2)

button_plus = Button(text="+", pady=5, font=("lucid", 20, "bold"), command=lambda: click("+"))
button_plus.grid(row=5, column=0)

button_minus = Button(text="-", padx=2, pady=4, font=("lucid", 23, "bold"), command=lambda: click("-"))
button_minus.grid(row=5, column=1)

button_mul = Button(text="*", padx=2, pady=5, font=("lucid", 20, "bold"), command=lambda: click("*"))
button_mul.grid(row=5, column=2)

button_div = Button(text="/", font=("lucid", 23, "bold"), command=lambda: click("/"))
button_div.grid(row=6, column=0)

button_mod = Button(text="%", pady=5, font=("lucid", 18, "bold"), command=lambda: click("%"))
button_mod.grid(row=6, column=1)

button_equal = Button(text="=", padx=2, pady=5, font=("lucid", 19, "bold"), command=equal)
button_equal.grid(row=6, column=2)
windows.mainloop()