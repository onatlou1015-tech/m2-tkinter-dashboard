import tkinter as tk


root = tk.Tk()
root.title("Widgets")
root.geometry("600x400")
root.resizable(False,False)

fonts = ("Arial", 25, "bold")

def show_value():
    value = spinbox.get()
    label.config(text=f"Selected: {value}")


spinbox = tk.Spinbox(
    root,
    from_=0,      
    to=10,        
    width=10,
    font=fonts
)
spinbox.pack(pady=20)

tk.Button(root, text="Show Value", command=show_value, font=fonts).pack(pady=10)

label = tk.Label(root, text="Select a value", font=fonts)
label.pack()


root.mainloop()