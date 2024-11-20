import tkinter as tk
from tkinter import messagebox


# Functions for the To-Do List Application
def add_task():
    task = task_entry.get().strip()
    if not task:
        messagebox.showwarning("Input Error", "Task cannot be empty!")
    else:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)


def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showerror("Selection Error", "Please select a task to remove.")


def clear_all_tasks():
    if task_listbox.size() == 0:
        messagebox.showinfo("No Tasks", "There are no tasks to clear.")
    else:
        confirm = messagebox.askyesno(
            "Clear All", "Are you sure you want to clear all tasks?"
        )
        if confirm:
            task_listbox.delete(0, tk.END)


# GUI Setup
root = tk.Tk()
root.title("📝 To-Do List Application")
root.geometry("500x500")
root.configure(bg="#f0f8ff")

# Header
header_label = tk.Label(
    root, text="To-Do List", font=("Arial", 20, "bold"), bg="#f0f8ff", fg="#1e3d59"
)
header_label.pack(pady=10)

# Input Frame for Adding Tasks
input_frame = tk.Frame(root, bg="#f0f8ff")
input_frame.pack(pady=20)

task_entry = tk.Entry(input_frame, font=("Arial", 14), width=30)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(
    input_frame,
    text="Add Task",
    font=("Arial", 12, "bold"),
    bg="#0073e6",
    fg="white",
    relief="flat",
    command=add_task,
)
add_button.pack(side=tk.LEFT, padx=5)

# Task Listbox
task_listbox = tk.Listbox(
    root,
    font=("Arial", 14),
    width=45,
    height=15,
    bg="#ffffff",
    fg="#333333",
    selectbackground="#0073e6",
)
task_listbox.pack(pady=10)

# Control Buttons
control_frame = tk.Frame(root, bg="#f0f8ff")
control_frame.pack(pady=10)

remove_button = tk.Button(
    control_frame,
    text="Remove Task",
    font=("Arial", 12, "bold"),
    bg="#ff4d4d",
    fg="white",
    relief="flat",
    command=remove_task,
)
remove_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(
    control_frame,
    text="Clear All",
    font=("Arial", 12, "bold"),
    bg="#ffaa00",
    fg="white",
    relief="flat",
    command=clear_all_tasks,
)
clear_button.pack(side=tk.LEFT, padx=10)

# Footer
footer_label = tk.Label(
    root,
    text="Keep track of your tasks, one step at a time! 😊",
    font=("Arial", 10),
    bg="#f0f8ff",
    fg="#555555",
)
footer_label.pack(side=tk.BOTTOM, pady=10)

# Start the GUI
root.mainloop()
