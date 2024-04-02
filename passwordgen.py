import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
import random
import string
from PIL import Image, ImageTk
from tkinter import messagebox

def generate_password(level, length):
    alphabets = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    if level == "Easy":
        characters = alphabets + numbers
    elif level == "Medium":
        characters = alphabets + numbers + symbols
    elif level == "Hard":
        characters = alphabets + numbers + symbols
        length = min(length, 12)  

    generated_password = ''.join(random.choices(characters, k=length))
    return generated_password

def handle_level_selection():
    level = selected_level.get()
    value = []
    if level == "Hard":
        for i in range(4,13):
            value.append(str(i))
        combobox.config(values=value)
    else:
        for i in range(4, 13):
            value.append(str(i))
        combobox.config(values=value)
        combobox.set("Select password length:")
    
def del_password():
    del_password = listbox.curselection()[0]
    listbox.delete(del_password)
    messagebox.showinfo("Deleted!", "Password deleted successfully!")


original_passwords = []  #List to store original passwords

def generate_and_display_password():
    level = selected_level.get()
    length = combobox.get()
    if level == "" or level is None or level == "Select Level":
        messagebox.showinfo("Error", "Please select a level!")
    elif length == "" or length == "Select password length:":
        messagebox.showinfo("Error", "Please select a password length!")
    else:
        
        password = generate_password(level, int(length))
        password_label.config(text=password)
        messagebox.showinfo("Generated Password", "Password generated!!")
        return password        

def save_password():
    password = password_label.cget("text")
    if password:
        original_passwords.append(password)  # Store the original password
        messagebox.showinfo("Password Saved", "Password has been saved successfully.")
    else:
        messagebox.showinfo("Error", "Please generate password first.")

def reset_components():    # to reset everything after a password is saved and stored in listbox.
    selected_level.set("Select Level")
    combobox.set("Select password length")
    password_label.config(text="")

def add_password():
    selected_password = password_label.cget("text")
    if selected_password:
        listbox.insert(tk.END, selected_password)
        reset_components() 
        messagebox.showinfo("Success", "Password successfully added!")
    else:
        messagebox.showinfo("Error", "Please generate password first.")

def hide_selected_password():
    selected_indices = listbox.curselection()
    if selected_indices:
        for index in selected_indices:
            password = listbox.get(index)
            hidden_password = '*' * len(password)
            listbox.delete(index)
            listbox.insert(index, hidden_password)
        messagebox.showinfo("Hidden!", "Password hidden!!")
    else:
        messagebox.showinfo("Error", "Select password to hide!")
def show_selected_passwords():
    selected_indices = listbox.curselection()
    if selected_indices:
        for index in selected_indices:
            original_password = original_passwords[index]
            listbox.delete(index)
            listbox.insert(index, original_password)
    else:
        messagebox.showinfo("Error", "Select password to show!")
    
m =  tk.Tk()
m.geometry('555x670')
m.title("PASSWORD GENERATOR")

img = Image.open("password.png")
img = img.resize((555, 670), Image.BILINEAR) #resizes my bg image to the size i want 
tk_img = ImageTk.PhotoImage(img)

selected_level = tk.StringVar()

canvas = tk.Canvas(m, bg="bisque2", width=555, height=670)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, anchor="nw", image=tk_img)

combobox = Combobox(m, font=("Segoe Print",9), width=16)
combobox.set("Select password length")
combobox.place(x=360, y=240)

listbox = tk.Listbox(m, width=25, height=7, bg="cornsilk1", font=("Segoe Print",12))
listbox.place(x=110, y=420)

easy_radio = ttk.Radiobutton(m, text="Easy", variable=selected_level, value="Easy", command=handle_level_selection)
easy_radio.place(x=360, y=130)

medium_radio = ttk.Radiobutton(m, text="Medium",  variable=selected_level, value="Medium", command=handle_level_selection)
medium_radio.place(x=360, y=165)

hard_radio = ttk.Radiobutton(m, text="Hard",  variable=selected_level, value="Hard", command=handle_level_selection)
hard_radio.place(x=360, y=200)

l1 = ttk.Label(m, text="Select level:",font=("Segoe Print",10, "underline"), background="antiquewhite2")
l1.place(x=360, y=90)

password_label = ttk.Label(m, font=("Segoe UI Semibold",13), background="bisque1", foreground="bisque4", width=28)
password_label.place(x=30, y=255)

title_lbl = ttk.Label(m, text="PASSWORD", background="honeydew3", width=10, font=("Eras Light ITC", 17,"bold", "italic","underline"), foreground="gray29")
title_lbl.place(x=30, y=91)
title_lbl = ttk.Label(m, text="GENERATOR!!", background="honeydew3",width=12, font=("Eras Light ITC", 17,"bold", "italic","underline"), foreground="gray29")
title_lbl.place(x=141, y=132)

gen_bttn = ttk.Button(m, text="Generate", command=generate_and_display_password)
gen_bttn.place(x=360, y=290)

emoji_label = ttk.Label(m, text="😊 😊 😊", font=("Segoe UI Emoji", 20))  #just for funnn
emoji_label.place(x=80, y=190)

save_bttn = ttk.Button(m, text="Save",command=save_password)
save_bttn.place(x=450, y=290)

show_bttn = ttk.Button(m, text="Show", command=show_selected_passwords)
show_bttn.place(x=423, y=560, width=45)

hide_button = ttk.Button(m, text="Hide", command=hide_selected_password)
hide_button.place(x=423, y=520, width=45)

add_bttn = ttk.Button(m, text="Add", command=add_password)
add_bttn.place(x=423, y=440, width=45)

del_bttn = ttk.Button(m, text="Del", command=del_password)
del_bttn.place(x=423, y=480, width=45)

m.mainloop()
