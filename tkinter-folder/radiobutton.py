import tkinter as tk





root = tk.Tk()
root.title("Widgets")
root.geometry("600x400")
root.resizable(False,False)

fonts = ("Arial", 25, "bold")

def show_selection():
    selected = radio_var.get()
    label.config(text=f"You selected: {selected}")


radio_var = tk.StringVar()
radio_var.set("Option 1")


radio1 = tk.Radiobutton(root, text="Morning Shift", variable=radio_var, value="Morning Shift",font=fonts)
radio1.pack(pady=5)

radio2 = tk.Radiobutton(root, text="Evening Shift", variable=radio_var, value="Evening Shift",font=fonts)
radio2.pack(pady=5)

radio3 = tk.Radiobutton(root, text="Graveyard Shift", variable=radio_var, value="Graveyard Shift",font=fonts)
radio3.pack(pady=5)


button = tk.Button(root, text="Show Selection", command=show_selection, font=fonts, bg="yellow")
button.pack(pady=10)


label = tk.Label(root, text="Select an option", font=fonts)
label.pack(pady=10)

root.mainloop()