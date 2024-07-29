import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do App")
root.geometry("400x400")
root.configure(bg="lightgreen")


tasks = []


def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def delete_task():
    try:
        task_index = int(listbox.curselection()[0])
        del tasks[task_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")


def update_listbox():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        listbox.insert(tk.END, f"{i+1}. {task}")


entry = tk.Entry(root, width=40)
entry.pack(pady=10)


add_button = tk.Button(root, text="Submit", width=10, command=add_task, bg="red", fg="white")
add_button.pack()

listbox = tk.Listbox(root, height=10, width=40)
listbox.pack(pady=10)


delete_button = tk.Button(root, text="Delete Task Number", width=20, command=delete_task, bg="blue", fg="white")
delete_button.pack(pady=5)


delete_entry = tk.Entry(root, width=5)
delete_entry.pack()


delete_button = tk.Button(root, text="Delete", width=10, command=delete_task, bg="red", fg="white")
delete_button.pack(pady=5)


exit_button = tk.Button(root, text="Exit", width=10, command=root.quit, bg="red", fg="white")
exit_button.pack(pady=10)

root.mainloop()  