import tkinter as tk

root = tk.Tk()
root.title("Widgets - Scale")
root.geometry("600x400")
root.resizable(False, False)

fonts = ("Arial", 25, "bold")

def show_value():
    value = scale.get()
    label.config(text=f"Value: {value}")


scale = tk.Scale(
    root,
    from_=0,      
    to=100,       
    orient=tk.HORIZONTAL,
    length=300,
    font=("Arial", 12)
)
scale.pack(pady=30)


button = tk.Button(root, text="Volume", command=show_value, font=("Arial", 12))
button.pack(pady=10)


label = tk.Label(root, text="Move the slider", font=fonts)
label.pack(pady=10)

root.mainloop()