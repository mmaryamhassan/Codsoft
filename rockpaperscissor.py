from tkinter import *
from tkinter import messagebox
import random

m = Tk()
m.title("Rock Paper Scissors")
m.config(background="mistyrose2")

user_score = 0
comp_score = 0

def play(user_choice):
    global user_score, comp_score
    choices = ['ROCK', 'PAPER', 'SCISSOR']
    comp_choice = random.choice(choices)
    result = ""
    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (user_choice == 'ROCK' and comp_choice == 'SCISSOR') or \
         (user_choice == 'PAPER' and comp_choice == 'ROCK') or \
         (user_choice == 'SCISSOR' and comp_choice == 'PAPER'):
        result = "You win!!"
        user_score += 1
    else:
        result = "Computer wins!!"
        comp_score += 1
    messagebox.showinfo("Result", f"Computer chose: {comp_choice}\n{result}\n\nUser Score: {user_score}\nComputer Score: {comp_score}")

def u_choice(user_choice):
    play(user_choice)

def replay():
    global user_score, comp_score
    if user_score > comp_score:
        winner = "User"
    elif user_score < comp_score:
        winner = "Computer"
    else:
        winner = "No one"
    messagebox.showinfo("Match Result", f"{winner} won the match!\n\nFinal Scores:\nUser: {user_score}\nComputer: {comp_score}")
    user_score = 0
    comp_score = 0
    l1.config(text="CHOOSE YOUR MOVE :")

img_rps = PhotoImage(file="rps.png")
img_rps_sample = img_rps.subsample(1, 1)
img_rps_label = Label(image=img_rps_sample)
img_rps_label.pack(fill=X)

l1 = Label(m, text="CHOOSE YOUR MOVE", background="burlywood1", fg="black", width=10, font=("poor richard", 16,"bold"))
l1.pack(fill=X, side=TOP)

img_rock = PhotoImage(file="rock1.png")
img_rock_sample = img_rock.subsample(10, 11)
b1 = Button(m, text="ROCK", image=img_rock_sample, compound=BOTTOM, command=lambda: u_choice('ROCK'), background="teal")
b1.pack(fill=X, side=LEFT, padx=15, pady=15)

img_paper = PhotoImage(file="paper1.png")
img_paper_sample = img_paper.subsample(3, 3)
b2 = Button(m, text="PAPER", image=img_paper_sample, compound=BOTTOM, command=lambda: u_choice('PAPER'), background="silver")
b2.pack(fill=X, side=LEFT, padx=15, pady=15)

img_scissor = PhotoImage(file="scissor2.png")
img_scissor_sample = img_scissor.subsample(3, 3)
b3 = Button(m, text="SCISSOR", image=img_scissor_sample, compound=BOTTOM, command=lambda: u_choice('SCISSOR'), background="light blue")
b3.pack(fill=X, side=LEFT, padx=15, pady=15)

replay_button = Button(m, text="Replay", command=replay, background="plum", font=("Segoe Print", 10),foreground="black" )
replay_button.pack(fill=X, side=BOTTOM, padx=15, pady=15)

m.mainloop()
