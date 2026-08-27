import tkinter as tk

root = tk.Tk()
root.title("Widgets")
root.geometry("600x400")
root.resizable(False, False)

fonts = ("Arial", 25, "bold")

def on_select(event):
    
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        label.config(text=f"You selected: {item}")

def on_double_click(event):
    
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        label.config(text=f"Double-clicked: {item}")

listbox = tk.Listbox(root, height=6, width=30, font=("Arial", 12))
listbox.pack(pady=20)

for item in ["Apple", "Banana", "Orange", "Grape", "Mango"]:
    listbox.insert(tk.END, item)


listbox.bind('<<ListboxSelect>>', on_select) 
listbox.bind('<Double-Button-1>', on_double_click) 

label = tk.Label(root, text="Select an item", font=fonts)
label.pack(pady=10)

root.mainloop()