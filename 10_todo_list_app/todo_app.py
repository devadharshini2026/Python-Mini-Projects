import tkinter as tk
from tkinter import messagebox


def add_task():
    task = entry.get()
    if task.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
    else:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")


def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        listbox.delete(selected)
        listbox.insert(tk.END, f"✓ {task}")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")


# Create main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.resizable(False, False)

# Input field
entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=10)

# Buttons
frame = tk.Frame(root)
frame.pack()

add_btn = tk.Button(frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(frame, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

done_btn = tk.Button(frame, text="Mark Done", width=12, command=mark_done)
done_btn.grid(row=0, column=2, padx=5)

# Task List
listbox = tk.Listbox(root, font=("Helvetica", 14), width=40, height=12, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Run app
root.mainloop()
