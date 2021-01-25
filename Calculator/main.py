from tkinter import *
import math as m

frame = Tk()
frame.title("Calculator")
frame.iconbitmap("assets/calculator.ico")

user_in = Entry(frame,width=45,borderwidth=5)
user_in.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
user_in.insert(0,"")

def click(number):
    current = user_in.get()
    user_in.delete(0, END)
    user_in.insert(0,str(current) + str(number)) 

def clear():
    user_in.delete(0, END)

def add():
    first = user_in.get()
    global f_num
    global op
    op = '+'
    f_num = int(first)
    user_in.delete(0,END)

def subtract():
    first = user_in.get()
    global f_num
    global op
    op = '-'
    f_num = int(first)
    user_in.delete(0,END)

def multiply():
    first = user_in.get()
    global f_num
    global op
    op = '*'
    f_num = int(first)
    user_in.delete(0,END)

def divide():
    first = user_in.get()
    global f_num
    global op
    op = '/'
    f_num = int(first)
    user_in.delete(0,END)

def sqroot():
    first = user_in.get()
    global f_num
    global op
    op = '√'
    f_num = int(first)
    user_in.delete(0,END)
    user_in.insert(0,m.sqrt(f_num))

def sqr():
    first = user_in.get()
    global f_num
    global op
    op = '²'
    f_num = int(first)
    user_in.delete(0,END)
    user_in.insert(0,f_num*f_num)

def fact():
    first = user_in.get()
    global f_num
    global op
    op = '!'
    f_num = int(first)
    user_in.delete(0,END)
    user_in.insert(0,m.factorial(f_num))

def equal():
    second = user_in.get()
    user_in.delete(0,END)
    if op == '+':
        user_in.insert(0,f_num + int(second))
    elif op == '-':
        user_in.insert(0,f_num - int(second))
    elif op == '*':
        user_in.insert(0,f_num * int(second))
    elif op == '/':
        user_in.insert(0,f_num / int(second))



button_1 = Button(frame,text="1",padx=40,pady=20,command=lambda: click(1))
button_2 = Button(frame,text="2",padx=40,pady=20,command=lambda: click(2))
button_3 = Button(frame,text="3",padx=40,pady=20,command=lambda: click(3))
button_4 = Button(frame,text="4",padx=40,pady=20,command=lambda: click(4))
button_5 = Button(frame,text="5",padx=40,pady=20,command=lambda: click(5))
button_6 = Button(frame,text="6",padx=40,pady=20,command=lambda: click(6))
button_7 = Button(frame,text="7",padx=40,pady=20,command=lambda: click(7))
button_8 = Button(frame,text="8",padx=40,pady=20,command=lambda: click(8))
button_9 = Button(frame,text="9",padx=40,pady=20,command=lambda: click(9))
button_0 = Button(frame,text="0",padx=40,pady=20,command=lambda: click(0))

button_add = Button(frame,text="+",padx=39,pady=20,command=add)
button_subtract = Button(frame,text="-",padx=39,pady=20,command=subtract)
button_multiply = Button(frame,text="*",padx=39,pady=20,command=multiply)
button_divide = Button(frame,text="/",padx=39,pady=20,command=divide)
button_sqroot = Button(frame,text="√",padx=39,pady=20,command=sqroot)
button_sqr = Button(frame,text="x²",padx=39,pady=20,command=sqr)
button_fact = Button(frame,text="x!",padx=39,pady=20,command=fact)

button_equal = Button(frame,text="=",padx=89,pady=20,command=equal)
button_clear = Button(frame,text="AC",padx=84,pady=20,command=clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)

button_equal.grid(row=5,column=1,columnspan=2)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)
button_sqroot.grid(row=7,column=0)
button_sqr.grid(row=7,column=1)
button_fact.grid(row=7,column=2)

frame.mainloop()