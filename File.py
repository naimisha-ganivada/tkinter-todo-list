from tkinter import *
from tkinter import simpledialog

list_entries = []
count = 0

def add_tasks():
    global count
    if count == 0:
        list_box_widget.delete(0, END)
    count += 1
    value = simpledialog.askstring("Input", "Enter the Task to be added")
    list_box_widget.insert(END, str(count) + ") " + value.upper())

def clear():
    global count
    count = 0
    size = list_box_widget.size()
    for i in range(size):
        list_box_widget.delete(i, END)
    list_box_widget.insert(END, "NO TASKS ADDED")

if __name__ == '__main__':
    frame = Tk()
    frame.geometry('500x500')
    frame.title("TO DO LIST")

    list_box_widget = Listbox(frame, height=20, width=50, borderwidth=2, relief="solid", justify="left")
    list_box_widget.insert(END, "NO TASKS ADDED")
    list_box_widget.pack(expand=True, fill=BOTH)
    list_box_widget.place(relx=.5, rely=.4, anchor="center")

    button_add_tasks = Button(frame, text="ADD_TASK", borderwidth=2, relief="solid", command=add_tasks)
    button_add_tasks.place(relx=0.3, rely=0.9)

    button_clear_tasks = Button(frame, text="CLEAR", borderwidth=2, relief="solid", command=clear)
    button_clear_tasks.place(relx=0.5, rely=0.9)

    frame.mainloop()