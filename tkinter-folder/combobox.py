import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Widgets - Combobox")
root.geometry("600x400")
root.resizable(False, False)

fonts = ("Arial", 25, "bold")

def show_selection():
    selected = combo.get()
    if selected:
        label.config(text=f"Selected: {selected}")
    else:
        label.config(text="Nothing selected!")


combo = ttk.Combobox(root, values=["Computer 1", "Computer 2", "Computer 3", "Computer 4", "Computer 5"], width=30)
combo.pack(pady=30)


combo.set("Select a computer")


button = tk.Button(root, text="Show Selection", command=show_selection, font=("Arial", 12))
button.pack(pady=10)


label = tk.Label(root, text="Select a computer", font=fonts)
label.pack(pady=10)

root.mainloop()