'''from tkinter import * 
import tkinter.messagebox 
import tkinter as tk


window = tk.Tk()
window.title("to do list app")
window.mainLoop()
frame_task= Frame(window)
frame_task.pack()

Listbox_task=Listbox(frame_task,bg="black",fg="white",height=15,width=50,font = "Helvetica") 
Listbox_task.pack(side=tkinter.LEFT)

scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)
Listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=Listbox_task.yview)

#button widget
entry_button=Button(window, txt="add task", width=50,command=entertask)
entry_button.pack(pady=3)

delete_button=Button(window,text="delete selected task", width=50, command= deletetask)
delete_button.pack(pady=3)

mark_button=Button(window, text="mark as complete", width=60, command= markcompleted)
mark_button.pack(pady=3)


def entertask():
    input_text=""
    def add():
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
            tkinter.messagebox.showwaring(title="warning!", message="please enter some text")
        else:
            Listbox_task.insert(END,input_text)
            root1.destroy()
            
    root1=Tk()
    root1.title("add task")
    entry_task=Text(root1,width=40,height=4)
    entry_task.pack()
    button_temp=Button(root1,text="add task",command= add)
    button_temp.pack()
    root1.mainloop()
    
#function to facilitate the delete task from the listbox
    
    def deletetask():
        selected=Listbox_task.curselection()
        Listbox_task.delete(selected[0])
        

 #exicutes this to mark completed
    def markcompleted():
        marked=Listbox_task.curselection()
        temp=marked[0]
        #store the text of selected item in a string
        
        temp_marked=Listbox_task.get(marked)
        
        #update it
        
        temp_marked=temp_marked+" ⛳"
        #delete it then insert it
        Listbox_task.delete(temp)
        Listbox_task.insert(temp,temp_marked)
     
     
window.mainloop()'''

'''from tkinter import *
import tkinter.messagebox
import tkinter as tk

def entertask():
    input_text=""
    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please enter some text")
        else:
            Listbox_task.insert(END, input_text)
            root1.destroy()

    root1 = Tk()
    root1.title("Add Task")
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1, text="Add Task", command=add)
    button_temp.pack()
    root1.mainloop()

def deletetask():
    selected = Listbox_task.curselection()
    Listbox_task.delete(selected[0])

def markcompleted():
    marked = Listbox_task.curselection()
    temp = marked[0]
    temp_marked = Listbox_task.get(marked)
    temp_marked = temp_marked + " ⛳"
    Listbox_task.delete(temp)
    Listbox_task.insert(temp, temp_marked)

window = tk.Tk()
window.title("To Do List App")

frame_task = Frame(window)
frame_task.pack()

Listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="Helvetica")
Listbox_task.pack(side=tk.LEFT)

scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=tk.RIGHT, fill=tk.Y)
Listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=Listbox_task.yview)

# Button widgets
entry_button = Button(window, text="Add Task", width=50, command=entertask)
entry_button.pack(pady=3)

delete_button = Button(window, text="Delete Selected Task", width=50, command=deletetask)
delete_button.pack(pady=3)

mark_button = Button(window, text="Mark as Complete", width=60, command=markcompleted)
mark_button.pack(pady=3)

window.mainloop()'''

from tkinter import *
import tkinter.messagebox
import tkinter as tk
from tkinter import ttk

def entertask():
    input_text = ""
    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please enter some text")
        else:
            Listbox_task.insert(END, input_text)
            root1.destroy()

    root1 = Tk()
    root1.title("Add Task")
    root1.geometry("300x200")
    root1.configure(bg="#f0f0f0")
    
    entry_task = Text(root1, width=40, height=4, font=("Helvetica", 12))
    entry_task.pack(pady=10)
    
    button_temp = Button(root1, text="Add Task", command=add, bg="#4CAF50", fg="white", font=("Helvetica", 12))
    button_temp.pack(pady=10)
    
    root1.mainloop()

def deletetask():
    selected = Listbox_task.curselection()
    if selected:
        Listbox_task.delete(selected[0])
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Please select a task to delete")

def markcompleted():
    marked = Listbox_task.curselection()
    if marked:
        temp = marked[0]
        temp_marked = Listbox_task.get(marked)
        temp_marked = temp_marked + " ⛳"
        Listbox_task.delete(temp)
        Listbox_task.insert(temp, temp_marked)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Please select a task to mark as complete")

window = tk.Tk()
window.title("To Do List App")
window.geometry("500x400")
window.configure(bg="#f0f0f0")

# Frame for the listbox and scrollbar
frame_task = Frame(window, bg="#f0f0f0")
frame_task.pack(pady=20)

# Listbox widget
Listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font=("Helvetica", 12))
Listbox_task.pack(side=tk.LEFT, padx=10)

# Scrollbar widget
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=tk.RIGHT, fill=tk.Y)
Listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=Listbox_task.yview)

# Button widgets
entry_button = Button(window, text="Add Task", width=50, command=entertask, bg="#4CAF50", fg="white", font=("Helvetica", 12))
entry_button.pack(pady=5)

delete_button = Button(window, text="Delete Selected Task", width=50, command=deletetask, bg="#f44336", fg="white", font=("Helvetica", 12))
delete_button.pack(pady=5)

mark_button = Button(window, text="Mark as Complete", width=50, command=markcompleted, bg="#2196F3", fg="white", font=("Helvetica", 12))
mark_button.pack(pady=5)

window.mainloop()

