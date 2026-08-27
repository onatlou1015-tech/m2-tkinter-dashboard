import tkinter as tk


root = tk.Tk()
root.title("Widgets")
root.geometry("600x400")
root.resizable(False,False)

fonts = ("Arial", 25, "bold")

def show_selection():
    result = ""
    if var1.get():
        result += "Student 1 "
    if var2.get():
        result += "Student 2 "
    if var3.get():
        result += "Student 3 "
    
    if result:
        label.config(text=f"Selected: {result}")
    else:
        label.config(text="Nothing selected!")



var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()


cb1 = tk.Checkbutton(root, text="Student 1", variable=var1, font=fonts)
cb1.pack(pady=5)

cb2 = tk.Checkbutton(root, text="Student 2", variable=var2, font=fonts)
cb2.pack(pady=5)

cb3 = tk.Checkbutton(root, text="Student 3", variable=var3, font=fonts)
cb3.pack(pady=5)


tk.Button(root, text="Show Selection", font=fonts, command=show_selection).pack(pady=10)


label = tk.Label(root, text="Select options above", font=fonts)
label.pack(pady=10)

root.mainloop()