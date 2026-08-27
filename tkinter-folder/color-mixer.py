import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Color Mixer")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

# Title
tk.Label(
    root,
    text="Color Mixer",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
).pack(pady=15)

tk.Label(
    root,
    text="Move the sliders to mix colors",
    font=("Arial", 11),
    bg="#f0f0f0",
    fg="#7f8c8d"
).pack()

# Variables for RGB values
red_value = tk.IntVar(value=128)
green_value = tk.IntVar(value=128)
blue_value = tk.IntVar(value=128)

# Frame for color display
color_display = tk.Frame(
    root,
    width=300,
    height=150,
    bg="#808080",
    relief="sunken"
)
color_display.pack(pady=15, padx=20)

# Prevent the frame from shrinking
color_display.pack_propagate(False)

# Label inside color display
color_label = tk.Label(
    color_display,
    text="Color Preview",
    font=("Arial", 14, "bold"),
    bg="#808080",
    fg="white"
)
color_label.pack(expand=True)

# Function to update color
def update_color(*args):
    r = red_value.get()
    g = green_value.get()
    b = blue_value.get()
    
    # Convert to hex color
    hex_color = f"#{r:02x}{g:02x}{b:02x}"
    
    # Update background
    color_display.config(bg=hex_color)
    color_label.config(bg=hex_color)
    
    # Update RGB labels
    rgb_label.config(text=f"RGB: ({r}, {g}, {b})")
    hex_label.config(text=f"HEX: {hex_color}")
    
    # Auto-adjust text color for visibility
    brightness = (r * 299 + g * 587 + b * 114) / 1000
    if brightness > 128:
        color_label.config(fg="black")
    else:
        color_label.config(fg="white")

# Frame for sliders
slider_frame = tk.LabelFrame(
    root,
    text="Adjust Colors",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
slider_frame.pack(pady=10, padx=20, fill="x")

# Red Slider
red_frame = tk.Frame(slider_frame, bg="#f0f0f0")
red_frame.pack(fill="x", pady=5, padx=10)

tk.Label(
    red_frame,
    text="Red:",
    font=("Arial", 11, "bold"),
    bg="#f0f0f0",
    fg="#e74c3c",
    width=6
).pack(side="left")

red_slider = tk.Scale(
    red_frame,
    from_=0,
    to=255,
    orient="horizontal",
    variable=red_value,
    command=update_color,
    bg="#f0f0f0",
    length=300,
    tickinterval=50,
    resolution=1
)
red_slider.pack(side="left", padx=10)

red_label = tk.Label(
    red_frame,
    text="128",
    font=("Arial", 10),
    bg="#f0f0f0",
    width=4
)
red_label.pack(side="left")

# Green Slider
green_frame = tk.Frame(slider_frame, bg="#f0f0f0")
green_frame.pack(fill="x", pady=5, padx=10)

tk.Label(
    green_frame,
    text="Green:",
    font=("Arial", 11, "bold"),
    bg="#f0f0f0",
    fg="#27ae60",
    width=6
).pack(side="left")

green_slider = tk.Scale(
    green_frame,
    from_=0,
    to=255,
    orient="horizontal",
    variable=green_value,
    command=update_color,
    bg="#f0f0f0",
    length=300,
    tickinterval=50,
    resolution=1
)
green_slider.pack(side="left", padx=10)

green_label = tk.Label(
    green_frame,
    text="128",
    font=("Arial", 10),
    bg="#f0f0f0",
    width=4
)
green_label.pack(side="left")

# Blue Slider
blue_frame = tk.Frame(slider_frame, bg="#f0f0f0")
blue_frame.pack(fill="x", pady=5, padx=10)

tk.Label(
    blue_frame,
    text="Blue:",
    font=("Arial", 11, "bold"),
    bg="#f0f0f0",
    fg="#2980b9",
    width=6
).pack(side="left")

blue_slider = tk.Scale(
    blue_frame,
    from_=0,
    to=255,
    orient="horizontal",
    variable=blue_value,
    command=update_color,
    bg="#f0f0f0",
    length=300,
    tickinterval=50,
    resolution=1
)
blue_slider.pack(side="left", padx=10)

blue_label = tk.Label(
    blue_frame,
    text="128",
    font=("Arial", 10),
    bg="#f0f0f0",
    width=4
)
blue_label.pack(side="left")

# Function to update labels when slider moves
def update_labels(*args):
    red_label.config(text=str(red_value.get()))
    green_label.config(text=str(green_value.get()))
    blue_label.config(text=str(blue_value.get()))

# Bind variable updates to update labels
red_value.trace("w", update_labels)
green_value.trace("w", update_labels)
blue_value.trace("w", update_labels)

# Info frame
info_frame = tk.LabelFrame(
    root,
    text="Color Information",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
info_frame.pack(pady=10, padx=20, fill="x")

# RGB values
rgb_label = tk.Label(
    info_frame,
    text="RGB: (128, 128, 128)",
    font=("Arial", 11),
    bg="#f0f0f0",
    fg="#2c3e50"
)
rgb_label.pack(pady=2)

# HEX value
hex_label = tk.Label(
    info_frame,
    text="HEX: #808080",
    font=("Arial", 11),
    bg="#f0f0f0",
    fg="#2c3e50"
)
hex_label.pack(pady=2)

# Reset button
def reset_colors():
    red_value.set(128)
    green_value.set(128)
    blue_value.set(128)
    update_color()

tk.Button(
    root,
    text="Reset to Gray",
    command=reset_colors,
    bg="#95a5a6",
    fg="white",
    font=("Arial", 10),
    padx=15,
    pady=5
).pack(pady=10)

# Initialize color
update_color()

root.mainloop()