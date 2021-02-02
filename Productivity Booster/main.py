from tkinter import *
from tkinter import messagebox
from todolist import todo

root = Tk()
root.title("Productivity Booster")
root.iconbitmap('assets/productivity.ico')
# root.resizable(False, False)
# root.geometry("400x400")

prog_title = Label(root,text="Productivity")
prog_title.grid(row=0,column=0,columnspan=3,pady=5)

to_do_list_button = Button(root, text="To-Do List", width=13, command=todo)
to_do_list_button.grid(row=1,column=0)

if __name__ == "__main__":
    root.mainloop()