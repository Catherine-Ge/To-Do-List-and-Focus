import tkinter
from tkinter import *
import time
from tkinter import messagebox

def timer():
    times = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    while times > 0:
        h = 0
        m = times // 60
        s = times % 60
        if m >= 60:
            h = m // 60
            m = m % 60
        hour.set(h)
        minute.set(m)
        second.set(s)
        app.update()
        time.sleep(1)
        times = times - 1
    focus = int(focused.get()) + 1
    focused.set(focus)
    messagebox.showwarning("app", "Time's Up!")
    focusgoal = int(goal.get())
    if focusgoal == focus:
        messagebox.showwarning("app", "You Have Compeleted the Focus Goal!")

def add():
    if newtodo.get() != "":
        file = open("todo.txt", "a+")
        listbox.insert(END, newtodo.get())
        file.write(newtodo.get()+"\n")
        file.close()
        entry.delete(0, END)
    else:
        messagebox.showwarning("app", "Please enter a valid to-do assignment")

def cmplt():
    listbox.delete(ANCHOR)

def dlt():
    value=listbox.get(listbox.curselection())
    listbox.delete(ANCHOR)
    file = open("todo.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("todo.txt", "w")
    for line in lines:
        if line != (value+"\n"):
            file.write(line)
    file.close()

def load():
    listbox.delete(0, END)
    file = open("todo.txt", "r")
    line = file.readline()
    while line != "":
        listbox.insert(END, line)
        line = file.readline()
    file.close()
    
    
app = Tk()
app.geometry('350x400')
app.title("Focus")

hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("00")
minute.set("00")
second.set("00")

Entry(app, textvariable=hour, width=3, font="Arial").place(x=65, y=15)
Entry(app, textvariable=minute, width=3, font="Arial").place(x=115, y=15)
Entry(app, textvariable=second, width=3, font="Arial").place(x=165, y=15)

Button(app, text="START", command=lambda:timer(), font=("Arial")).place(x=215, y = 10)

focusL = Label(app, text="FOCUSED").place(x = 65, y = 50)
focused=StringVar()
focused.set("0")
Entry(app, textvariable=focused, state=DISABLED, width=3, font="Arial").place(x = 125, y = 50)

goalL = Label(app, text="FOCUS GOAL").place(x = 160, y = 50)
goal=StringVar()
goal.set("0")
Entry(app, textvariable=goal, width=3, font="Arial").place(x = 245, y = 50)

newtodo = StringVar()
newtodo.set("")
entry = Entry(app, textvariable=newtodo, width=37, font="Arial")
entry.place(x=5, y=330)

Button(app, text="ADD", command=lambda:add(), font="Arial").place(x=26, y=350)

Button(app, text="COMPLETE", command=lambda:cmplt(), font="Arial").place(x=76, y=350)

Button(app, text="DELETE", command=lambda:dlt(), font="Arial").place(x=179, y=350)

Button(app, text="LOAD", command=lambda:load(), font="Arial").place(x=256, y=350)


listbox = Listbox(app, height=12, width=37, font="Arial")
listbox.place(x=5, y=80)





