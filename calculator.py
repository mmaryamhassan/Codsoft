from tkinter import *
import math

m= Tk()
m.geometry('326x272')
m.title("CALCULATOR")

def button_click(symbol):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(symbol))

def clear():
    entry.delete(0, END)

def calculate():                     #only for + - * /
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, END)
    entry.insert(END, str(result))

def sin():
    exp = float(entry.get())
    res = math.sin(math.radians(exp))        #when we use other than arthimetic operatios we don't use eval 
    entry.delete(0, END)                     #to display our operations we directly insert it
    entry.insert(END, str(res))

def cos():
    exp = float(entry.get())
    res = math.cos(math.radians(exp))
    entry.delete(0, END)
    entry.insert(END, str(res))

def tan():
    exp = float(entry.get())
    res = math.tan(math.radians(exp))
    entry.delete(0, END)
    entry.insert(END, str(res))


entry = Entry(m, width=20, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 3)
]
for symbol, row, col in buttons:
    button = Button(m, text=symbol, width=5, height=2,bg="lightblue", font=("Arial", 14),command=lambda sym=symbol: button_click(sym))
    button.grid(row=row, column=col)

sin_bttn = Button(m, text="sin", width=5, height=2, font=("arial",14),bg="lightblue", command=sin)
sin_bttn.grid(row = 2, column=4, columnspan=2)

cos_bttn = Button(m, text="cos", width=5, height=2, font=("arial",14),bg="lightblue", command=cos)
cos_bttn.grid(row = 3, column=4, columnspan=2)

tan_bttn = Button(m, text="tan", width=5, height=2, font=("arial",14),bg="lightblue", command=tan)
tan_bttn.grid(row = 4, column=4, columnspan=2)

equal_bttn = Button(m, text="=", width=5, height=2, font=("arial",14),bg="lightblue", command=calculate)
equal_bttn.grid(row=4,column=2)

clear_bttn = Button(m, text="AC", font=("arial",14),width=5, height=2,bg="lightblue", command=clear)
clear_bttn.grid(row = 1, column=4, columnspan=2)

m.mainloop()