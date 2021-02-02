from tkinter import *
from tkinter import messagebox
import time
from todolist import todo

root = Tk()
root.title("Productivity Booster")
root.iconbitmap('assets/productivity.ico')
# root.resizable(False, False)
# root.geometry("400x400")

prog_title = Label(root,text="Productivity Booster")
prog_title.grid(row=0,column=0,columnspan=3,pady=5)

'''             Digital Clock                     '''
def clock_start():
    time_text = time.strftime("%I:%M:%S %p")
    time_label.config(text=time_text)
    time_label.after(200, clock_start)

time_label=Label(root,font=("ds-digital",50,'bold'),bg='black',fg='red',bd=50)
time_label.grid(row=1,column=0)
clock_start()

to_do_list_button = Button(root, text="To-Do List", width=13, command=todo)
to_do_list_button.grid(row=2,column=0)

if __name__ == "__main__":
    root.mainloop()