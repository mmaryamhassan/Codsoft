import tkinter as tk
from datetime import datetime

def add():
    task = e1.get()
    if task != " ":
        listbox.insert(tk.END, task)
        e1.delete(0, tk.END)

def del_task():
    task_del = listbox.curselection()[0]
    listbox.delete(task_del)

def update_clock():
    current_time = datetime.now().strftime("%d-%m-%Y")
    clock_label.config(text=current_time)

m = tk.Tk()
m.title("TO-DO LIST")
m.geometry('564x317')

canvas = tk.Canvas(m, width=564, height=317)
canvas.pack()
img = tk.PhotoImage(file="list1.png")
canvas.create_image(0, 0, anchor=tk.NW, image=img)

listbox = tk.Listbox(m, width=32, height=11, bg="cornsilk1", font=("Rockwell Condensed",12))
listbox.place(x=41, y=65)

clock_label = tk.Label(m, font=("Helvetica", 14), bg="lightseagreen")
clock_label.place(x=450, y=285)
update_clock()

l = tk.Label(m, text="YOUR LIST:", font=("Perpetua Titling MT",15),bg="darkolivegreen1",  width=14)
l.place(x=46, y=33)
l1 = tk.Label(m, text="TO-DO LIST", font=("Lucida Calligraphy",16),bg="lightgoldenrod2",  width=14,height=1)
l1.place(x=300, y=15)
l2 = tk.Label(m, text="LIST YOUR TASK:", font=("Poor Richard",14),  width=14,height=1)
l2.place(x=300, y=100)
e1 = tk.Entry(m, font=("Rage Italic",16),width=20, bg="pink")
e1.place(x=300, y=140)

add_bttn = tk.Button(m, text="ADD", font=("Jokerman",12), bg="plum",fg="white", command=add)
add_bttn.place(x=300, y=200)
del_bttn = tk.Button(m, text="DELETE", font=("Jokerman",12), bg="plum",fg="white", command=del_task)
del_bttn.place(x=400, y=200)

m.mainloop()
