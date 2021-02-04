from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from PIL import ImageTk, Image
from todolist import todo
import os
import time
import getpass

root = Tk()
root.state("zoomed")

root.configure(background='black')
root.title("Productivity Booster")
root.iconbitmap('assets/productivity.ico')
# root.resizable(False, False)
# root.geometry("400x400")

"""             
Background
"""
base_path = os.path.dirname(__file__)

bg_path = os.path.join(base_path, "assets/bg2.jpg")
bg_img = ImageTk.PhotoImage(Image.open(bg_path))

bg_label = Label(root, image = bg_img)
bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)


prog_title = Label(root,text="Productivity Booster", font = "helvetica 45 bold", fg = "white", bg= "black")
prog_title.place(x = 690, y = 120)

"""
Digital Clock
"""

def clock_start():
    time_text = time.strftime("%I:%M:%S %p")
    time_label.config(text=time_text)
    time_label.after(200, clock_start)

time_label=Label(root,font=("ds-digital",50,'bold'),fg='red')
time_label.place(x = 790, y = 250)
clock_start()

"""     Welcome
"""

user = getpass.getuser()
welcome_text = Label(root, text = "Welcome, " + str(user), font = "helvetica 20 italic bold")
welcome_text.place(x = 885, y = 490)

"""
Productivity Tools
"""

to_do_list_button = Button(root, text="To-Do List", width=13,padx=10,pady=10,command=todo)
to_do_list_button.place(x = 360, y = 740)

motivation_button = Button(root, text="Motivation", width=13,padx=10,pady=10)
motivation_button.place(x = 925, y = 740)

timer_button = Button(root, text="Timer", width=13,padx=10,pady=10)
timer_button.place(x = 1490, y = 740)

if __name__ == "__main__":
    root.mainloop()