import tkinter
from tkinter import *
import os

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []


def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)


def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfie:
            for task in task_list:
                taskfie.write(task + "\n")
        listbox.delete(ANCHOR)


def openTaskFile():
    try:
        global task_list
        if os.path.exists("tasklist.txt"):  # Check if the file exists
            with open("tasklist.txt", "r") as taskfile:
                tasks = taskfile.readlines()

            for task in tasks:
                if task.strip():  # Check if the task is not just a newline
                    task_list.append(task)
                    listbox.insert(END, task.strip())

    except Exception as e:  # Catch and handle exceptions more specifically
        print(f"An error occurred: {str(e)}")


#---------------Icons------------------#

Image_icon = PhotoImage(file="task.png")
root.iconphoto(False, Image_icon)

TopImage = PhotoImage(file="topbar.png")
Label(root, image=TopImage).pack()

dockImage = PhotoImage(file="dock.png")
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)

noteImage = PhotoImage(file="task.png")
Label(root, image=noteImage, bg="#32405b").place(x=340, y=25)

heading = Label(root, text="ALL TASKS", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=140, y=25)

#---------------Main------------------#

frame = Frame(root, width=400, height=50, bg="black")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bg="black", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(
    frame,
    text="ADD",
    font="arial 20 bold",
    width=6,
    highlightbackground="#5a95ff",
    fg="#fff",
    bd=0,
    command=addTask,
)
button.place(x=300, y=8)

#---------------Listbox------------------#
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(
    frame1,
    font=("arial", 12),
    width=50,
    height=18,
    bg="#32405b",
    fg="white",
    cursor="hand2",
    selectbackground="#5a95ff",
)
listbox.pack(side=LEFT, fill=BOTH, padx=3)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


# Delete
Delete_icon = PhotoImage(file="delete.png")
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

openTaskFile()

root.mainloop()
