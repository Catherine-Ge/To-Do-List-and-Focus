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
    second.set(0)
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
        messagebox.showwarning("app", "Please enter a valid task")

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
app.geometry('400x400')
app.title("Focus")

hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("00")
minute.set("00")
second.set("00")

Label(app, text="Hour", font="Arial").grid(row=0, column=0, sticky=W, pady=10)
Entry(app, textvariable=hour, width=3, font="Arial").grid(row=0, column=1)
Label(app, text="Minute", font="Arial").grid(row=0, column=2)
Entry(app, textvariable=minute, width=3, font="Arial").grid(row=0, column=3)
Label(app, text="Second", font="Arial").grid(row=0, column=4)
Entry(app, textvariable=second, width=3, font="Arial").grid(row=0, column=5)

Button(app, text="START", command=lambda:timer(), font=("Arial")).grid(row=0, column=6)

focusL = Label(app, text="DONE").grid(row=1,column=1)
focused=StringVar()
focused.set("0")
Entry(app, textvariable=focused, state=DISABLED, width=3, font="Arial").grid(row=1,column=2)

goalL = Label(app, text="FOCUS GOAL").grid(row=1,column=3, columnspan=2)
goal=StringVar()
goal.set("0")
Entry(app, textvariable=goal, width=3, font="Arial").grid(row=1,column=5)

listbox = Listbox(app, height=12, width=37, font="Arial")
listbox.grid(row=2,column=0,columnspan=8,rowspan=10)

newtodo = StringVar()
newtodo.set("")
entry = Entry(app, textvariable=newtodo, width=37, font="Arial")
entry.grid(row=13,column=0,columnspan=8,rowspan=1)

Button(app, text="ADD", command=lambda:add(), font="Arial").grid(row=14,column=1,columnspan=1)

Button(app, text="COMPLETE", command=lambda:cmplt(), font="Arial").grid(row=14,column=2,columnspan=2)

Button(app, text="DELETE", command=lambda:dlt(), font="Arial").grid(row=14,column=4,columnspan=1)

Button(app, text="LOAD", command=lambda:load(), font="Arial").grid(row=14,column=5,columnspan=1)
