from tkinter import *
from tkinter import messagebox
from pickle import load, dump
from tkinter import filedialog
import os

def todo():
    module1 = Tk()
    module1.title("To-Do List")
    module1.iconbitmap('assets/productivity.ico')
    module1.resizable(False, False)
    # module1.geometry("400x400")

    def add_task():
        task_entry = new_task_entry.get()
        if task_entry == "":
            messagebox.showwarning(title="Empty Task", message="You must enter a task first!")
        else:
            task_entry = '-> ' + task_entry
            tasks_box.insert(END, task_entry)
            new_task_entry.delete(0, END)
        
        status.config(
            text="Tasks " + str(count_completed()) + " of " + str(tasks_box.size()) + " completed"
        )

    def delete_task():
        try:
            tasks_box.delete(tasks_box.curselection())
        except:
            messagebox.showwarning(title="No task Selected", message="You must select a task first!")
        
        status.config(
            text="Tasks " + str(count_completed()) + " of " + str(tasks_box.size()) + " completed"
        )

    def check_task():
        tasks_box.itemconfig(
            tasks_box.curselection(),
            fg='#dedede'
        )
        tasks_box.selection_clear(0, END)
        
        status.config(
            text="Tasks " + str(count_completed()) + " of " + str(tasks_box.size()) + " completed"
        )

    def uncheck_task():
        tasks_box.itemconfig(
            tasks_box.curselection(),
            fg='#000000'
        )
        tasks_box.selection_clear(0, END)
        
        status.config(
            text="Tasks " + str(count_completed()) + " of " + str(tasks_box.size()) + " completed"
        )

    def increase_priority():
        curr_position = tasks_box.curselection()
        if curr_position:
            for pos in curr_position:
                if pos != 0:
                    text = tasks_box.get(pos)
                    color = tasks_box.itemcget(pos, "fg")
                    tasks_box.delete(pos)
                    tasks_box.insert(pos-1,text)
                    tasks_box.itemconfig(
                        pos-1,
                        fg = color
                    )
                    tasks_box.selection_set(pos-1)
                    
        

    def decrease_priority():
        curr_position = tasks_box.curselection()
        if curr_position:
            for pos in curr_position:
                if pos < tasks_box.size()-1:
                    text = tasks_box.get(pos)
                    color = tasks_box.itemcget(pos, "fg")
                    tasks_box.delete(pos)
                    tasks_box.insert(pos+1,text)
                    tasks_box.itemconfig(
                        pos+1,
                        fg = color
                    )
                    tasks_box.selection_set(pos+1)

    def clear_tasks():
        response = messagebox.askyesno(title="Clear tasks", message="Are you sure you want to clear the tasks?")
        if response:
            tasks_box.delete(0, END)
        
        status.config(
            text="Tasks " + str(count_completed()) + " of " + str(tasks_box.size()) + " completed"
        )
        
    def clear_completed_tasks():
        count = 0
        while count < tasks_box.size():
            if tasks_box.itemcget(count, "fg") == '#dedede':
                tasks_box.delete(tasks_box.index(count))
            count += 1
        
        status.config(
            text="Tasks " + str(count_completed()) + " of " + str(tasks_box.size()) + " completed"
        )
        
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
        filename = filedialog.askopenfilename(
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
        tasks = load(open(filename, "rb"))
        tasks_box.delete(0, END)
        for task in tasks:
            tasks_box.insert(END, task)
        status.config(
            text="Tasks " + str(count_completed()) + " of " + str(tasks_box.size()) + " completed"
        )

    def count_completed():
        i=0
        count=0
        while i < tasks_box.size():
            if tasks_box.itemcget(i, "fg") == '#dedede':
                count += 1
            i += 1 
        return count

    def change_color():
        to_change = tasks_box.curselection()
        if to_change:
            changer = Tk()
            changer.title("Change Color")
            changer.iconbitmap('assets/productivity.ico')
            changer.resizable(False, False)

            def red_change():
                tasks_box.itemconfig(
                    tasks_box.curselection(),
                    fg='red'
                )

            def blue_change():
                tasks_box.itemconfig(
                    tasks_box.curselection(),
                    fg='blue'
                )

            def green_change():
                tasks_box.itemconfig(
                    tasks_box.curselection(),
                    fg='green'
                )

            def orange_change():
                tasks_box.itemconfig(
                    tasks_box.curselection(),
                    fg='orange'
                )

            def hexa_change():
                hexa_code = hexa_entry.get()
                try:
                    tasks_box.itemconfig(
                        tasks_box.curselection(),
                        fg=hexa_code
                    )
                except:
                    messagebox.showerror(title="Invalid Code", message="Enter a valid hexa color")

            red_button = Button(changer,text="Red",width=13,fg='red',command=red_change)
            red_button.grid(row=0,column=0,pady=5,padx=5)

            blue_button = Button(changer,text="Blue",width=13,fg='blue',command=blue_change)
            blue_button.grid(row=0,column=1,pady=5,padx=5)

            green_button = Button(changer,text="Green",width=13,fg='green',command=green_change)
            green_button.grid(row=1,column=0,pady=5,padx=5)

            orange_button = Button(changer,text="Orange",width=13,fg='orange',command=orange_change)
            orange_button.grid(row=1,column=1,pady=5,padx=5)

            hexa_label = Label(changer,text="Hexa")
            hexa_label.grid(row=2,column=0,pady=5,padx=5)

            hexa_entry = Entry(changer,width=10,borderwidth=5)
            hexa_entry.grid(row=2,column=1,padx=5,pady=5)

            enter_button = Button(changer,text="Enter",width=13,command=hexa_change)
            enter_button.grid(row=3,column=0,columnspan=2,pady=5,padx=10)
        
        else:
            messagebox.showwarning(title="No task Selected", message="You must select a task first!")

    
    menu_bar = Menu(module1)
    module1.config(menu=menu_bar)

    file_menu = Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label="File", menu=file_menu)

    file_menu.add_command(label="Save file..", command=save_tasks)
    file_menu.add_command(label="Load file..", command=load_tasks)

    edit_menu = Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    edit_menu.add_command(label="Change color", command=change_color)

    module_title = Label(module1,text="To-Do List")
    module_title.grid(row=0,column=0,columnspan=3,pady=5)

    tasks_frame = Frame(module1)

    tasks_box = Listbox(tasks_frame,width=35,height=13,borderwidth=5)
    tasks_box.pack(side='left', fill='y')

    box_scrollbar = Scrollbar(tasks_frame, orient='vertical', command=tasks_box.yview)
    box_scrollbar.pack(side='right', fill='y')

    tasks_box.config(yscrollcommand=box_scrollbar.set)

    tasks_frame.grid(row=1,column=0,columnspan=2,padx=10)

    new_task_entry = Entry(module1,width=37,borderwidth=5)
    new_task_entry.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

    add_button = Button(module1,text="Add",width=13,command=add_task)
    add_button.grid(row=3,column=0)

    delete_button = Button(module1,text="Delete",width=13,command=delete_task)
    delete_button.grid(row=3,column=1)

    check_button = Button(module1,text="Check",width=13,command=check_task)
    check_button.grid(row=4,column=0,pady=5)

    uncheck_button = Button(module1,text="Uncheck",width=13,command=uncheck_task)
    uncheck_button.grid(row=4,column=1,pady=5)

    increase_priority_button = Button(module1,text="Move up",width=13,command=increase_priority)
    increase_priority_button.grid(row=5,column=0,pady=5)

    decrease_priority_button = Button(module1,text="Move down",width=13,command=decrease_priority)
    decrease_priority_button.grid(row=5,column=1,pady=5)

    clear_completed_button = Button(module1,text="Clear Completed Tasks",width=31,command=clear_completed_tasks)
    clear_completed_button.grid(row=6,column=0,columnspan=2,pady=3)

    clear_button = Button(module1,text="Clear Tasks",width=31,command=clear_tasks)
    clear_button.grid(row=7,column=0,columnspan=2,pady=3)

    statusvar = StringVar()
    statusvar.set("Tasks " + str(count_completed()) + " of " + str(tasks_box.size()) + " completed")

    status = Label(module1,text="Tasks " + str(count_completed()) + " of " + str(tasks_box.size()) + " completed",bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=8,column=0,columnspan=2,sticky=W+E)

    module1.mainloop()