import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("🌓 Dark Mode Toggle")
root.geometry("500x400")

# Variable to track dark mode state (0 = light, 1 = dark)
dark_mode = tk.IntVar(value=0)

# Define color schemes
light_mode = {
    "bg": "#f0f0f0",
    "fg": "#000000",
    "button_bg": "#e0e0e0",
    "entry_bg": "#ffffff"
}

dark_mode_colors = {
    "bg": "#2d2d2d",
    "fg": "#ffffff",
    "button_bg": "#4a4a4a",
    "entry_bg": "#3d3d3d"
}

# Function to toggle dark mode
def toggle_dark_mode():
    if dark_mode.get() == 1:
        colors = dark_mode_colors
    else:
        colors = light_mode
    
    # Change main window background
    root.config(bg=colors["bg"])
    
    # Change all widgets
    for widget in root.winfo_children():
        try:
            widget.config(bg=colors["bg"], fg=colors["fg"])
        except:
            pass  # Some widgets may not accept bg/fg
        
        # Handle specific widget types
        if isinstance(widget, tk.Button):
            widget.config(bg=colors["button_bg"])
        elif isinstance(widget, tk.Entry):
            widget.config(bg=colors["entry_bg"])
        elif isinstance(widget, tk.Text):
            widget.config(bg=colors["entry_bg"])
        elif isinstance(widget, tk.LabelFrame):
            widget.config(bg=colors["bg"], fg=colors["fg"])
            # Change children inside LabelFrame
            for child in widget.winfo_children():
                try:
                    child.config(bg=colors["bg"], fg=colors["fg"])
                except:
                    pass

# Main content frame
content_frame = tk.Frame(root)
content_frame.pack(pady=30, padx=40, fill="both", expand=True)

# Header
tk.Label(
    content_frame, 
    text="Dark Mode Demo", 
    font=("Arial", 18, "bold")
).pack(pady=10)

# Checkbutton for dark mode toggle
toggle_cb = tk.Checkbutton(
    content_frame,
    text="Enable Dark Mode",
    variable=dark_mode,
    command=toggle_dark_mode,
    font=("Arial", 12)
)
toggle_cb.pack(pady=10)

# Sample content to show the effect
sample_frame = tk.LabelFrame(content_frame, text="Sample Content", font=("Arial", 11))
sample_frame.pack(pady=15, fill="x")

tk.Label(sample_frame, text="This is a sample label").pack(pady=5)
tk.Entry(sample_frame).pack(pady=5, padx=10, fill="x")
tk.Button(sample_frame, text="Sample Button").pack(pady=5)

# Description
tk.Label(
    content_frame,
    text="Check the box above to toggle\nbetween Light and Dark modes",
    font=("Arial", 10),
    justify="center"
).pack(pady=10)

# Initialize in light mode
toggle_dark_mode()

root.mainloop()