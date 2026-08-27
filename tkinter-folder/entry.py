import tkinter as tk

root = tk.Tk()
root.title("Widgets")
root.geometry("600x400")
root.resizable(False,False)

fonts = ("Arial", 25, "bold")

def click():
    my_text = int(entry1.get())
    total = my_text * 5
    label_output.config(text = f"{total}")
    entry1.delete(0,tk.END)

def clear_me():        
    label_output.config(text = "Output here...")
    entry1.delete(0,tk.END)


label = tk.Label(root, text="Enter Integer", font=fonts)
label.pack()

entry1 = tk.Entry(root, font=fonts)
entry1.pack()

button1 = tk.Button(root,text="Click Me!", font = fonts, command=click)
button1.pack()

button2 = tk.Button(root,text="Clear Me!", font= fonts, command=clear_me)
button2.pack()

label_output = tk.Label(root, text="Output here...", font=fonts)
label_output.pack()

root.mainloop()