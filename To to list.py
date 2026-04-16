import tkinter as tk

# Create window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

tasks = []

# Add task
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

# Delete task
def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        tasks.pop(selected[0])

# Input field
entry = tk.Entry(root)
entry.pack(pady=10)

# Buttons
add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack()

# List display
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True, pady=10)

root.mainloop()