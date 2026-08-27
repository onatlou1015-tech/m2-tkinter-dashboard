import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Widgets - Progressbar")
root.geometry("600x400")
root.resizable(False, False)

fonts = ("Arial", 25, "bold")

def start_progress():
    progress_bar.start() 

def stop_progress():
    progress_bar.stop()  


progress_bar = ttk.Progressbar(
    root,
    orient=tk.HORIZONTAL,
    length=200,
    mode='indeterminate'  
)
progress_bar.pack(pady=50)


btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Start", command=start_progress, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
tk.Button(btn_frame, text="Stop", command=stop_progress, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

root.mainloop()