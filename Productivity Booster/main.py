from tkinter import *
from tkinter import messagebox
from pickle import load, dump
from tkinter import filedialog
import os

root = Tk()
root.title("Productivity Booster")
root.iconbitmap('assets/productivity.ico')
# root.geometry("400x400")

def add_task():
    task_entry = new_task_entry.get()
    if task_entry == "":
        messagebox.showwarning(title="Empty Task", message="You must enter a task first!")
    else:
        tasks_box.insert(END, task_entry)
        new_task_entry.delete(0, END)


def delete_task():
    try:
        tasks_box.delete(tasks_box.curselection())
    except:
        messagebox.showwarning(title="No task Selected", message="You must select a task first!")

def check_task():
    pass

def uncheck_task():
    pass

def clear_tasks():
    pass

def save_tasks():
    tasks = tasks_box.get(0, tasks_box.size())
    filename = filedialog.asksaveasfilename(
        initialdir=os.getcwd(),
        title="Save File..",
        filetypes=(
            ("DAT Files", "*.dat"),("All Files", "*.*")
            )
    )
    if filename:
        if filename.endswith(".dat"):
            pass
        else:
            filename = f'{filename}.dat'
    dump(tasks, open(filename, "wb"))

def load_tasks():
    tasks = load(open("tasks.dat", "rb"))
    tasks_box.delete(0, END)
    for task in tasks:
        tasks_box.insert(END, task)

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Save file..", command=save_tasks)
file_menu.add_command(label="Load file..")

prog_title = Label(root,text="To-Do List")
prog_title.grid(row=0,column=0,columnspan=3,pady=5)

tasks_frame = Frame(root)

tasks_box = Listbox(tasks_frame,width=35,height=13,borderwidth=5)
tasks_box.pack(side='left', fill='y')

box_scrollbar = Scrollbar(tasks_frame, orient='vertical', command=tasks_box.yview)
box_scrollbar.pack(side='right', fill='y')

tasks_box.config(yscrollcommand=box_scrollbar.set)

tasks_frame.grid(row=1,column=0,columnspan=2,padx=10)

new_task_entry = Entry(root,width=37,borderwidth=5)
new_task_entry.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

add_button = Button(root,text="Add",width=13,command=add_task)
add_button.grid(row=3,column=0)

delete_button = Button(root,text="Delete",width=13,command=delete_task)
delete_button.grid(row=3,column=1)

check_button = Button(root,text="Check",width=13,command=check_task)
check_button.grid(row=4,column=0,pady=5)

uncheck_button = Button(root,text="Uncheck",width=13,command=uncheck_task)
uncheck_button.grid(row=4,column=1,pady=5)

clear_button = Button(root,text="Clear Tasks",width=31,command=clear_tasks)
clear_button.grid(row=5,column=0,columnspan=2,pady=3)

status = Label(root,text="Tasks x of x completed",bd=1,relief=SUNKEN,anchor=E)
status.grid(row=6,column=0,columnspan=2,sticky=W+E)

root.mainloop()