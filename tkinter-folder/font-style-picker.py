import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Font Style Picker")
root.geometry("600x450")
root.configure(bg="#fff8e7")

# Sample text options
sample_texts = [
    "The quick brown fox jumps over the lazy dog",
    "Hello World! This is a sample text.",
    "Programming is fun with Python",
    "Font selection made easy",
    "Design your own style",
    "Typography matters"
]

# Dictionary of available fonts
available_fonts = {
    "Arial": "Sans-serif font",
    "Times New Roman": "Serif font",
    "Courier New": "Monospace font",
    "Verdana": "Sans-serif font",
    "Georgia": "Serif font",
    "Comic Sans MS": "Casual font",
    "Tahoma": "Sans-serif font",
    "Trebuchet MS": "Sans-serif font",
    "Impact": "Bold font",
    "Arial Black": "Heavy font"
}

# Available sizes
font_sizes = list(range(8, 73, 2))  # 8, 10, 12, ... 72

# Variables
selected_font = tk.StringVar(value="Arial")
selected_size = tk.IntVar(value=20)
selected_text = tk.StringVar(value=sample_texts[0])
dark_mode = tk.BooleanVar(value=False)

# Main container
main_frame = tk.Frame(root, bg="#fff8e7")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Title
tk.Label(
    main_frame,
    text="Select Your Font Style",
    font=("Arial", 20, "bold"),
    bg="#fff8e7",
    fg="#8b4513"
).pack(pady=10)

# Font selection area
control_frame = tk.Frame(main_frame, bg="#fff8e7")
control_frame.pack(pady=15)

# Left column: Font family
font_frame = tk.LabelFrame(
    control_frame,
    text="Font Family",
    font=("Arial", 11, "bold"),
    bg="#fff8e7",
    fg="#8b4513"
)
font_frame.pack(side="left", padx=10, fill="both")

# Combobox for font family (READ-ONLY)
font_combo = ttk.Combobox(
    font_frame,
    textvariable=selected_font,
    values=list(available_fonts.keys()),
    font=("Arial", 11),
    width=25,
    state="readonly"  # Read-only prevents typos
)
font_combo.pack(padx=10, pady=10)

# Show font description
font_desc_label = tk.Label(
    font_frame,
    text=available_fonts["Arial"],
    font=("Arial", 9),
    bg="#fff8e7",
    fg="#7f8c8d"
)
font_desc_label.pack(padx=10, pady=(0,10))

# Right column: Font size
size_frame = tk.LabelFrame(
    control_frame,
    text="Font Size",
    font=("Arial", 11, "bold"),
    bg="#fff8e7",
    fg="#8b4513"
)
size_frame.pack(side="left", padx=10, fill="both")

# Combobox for font size (EDITABLE - user can type custom size)
size_combo = ttk.Combobox(
    size_frame,
    textvariable=selected_size,
    values=font_sizes,
    font=("Arial", 11),
    width=10,
    state="normal"  # Editable - user can type any number
)
size_combo.pack(padx=10, pady=10)

tk.Label(
    size_frame,
    text="(You can type custom size)",
    font=("Arial", 8),
    bg="#fff8e7",
    fg="#95a5a6"
).pack(padx=10, pady=(0,10))

# Sample text selection
text_frame = tk.LabelFrame(
    main_frame,
    text="Sample Text",
    font=("Arial", 11, "bold"),
    bg="#fff8e7",
    fg="#8b4513"
)
text_frame.pack(pady=10, fill="x")

text_combo = ttk.Combobox(
    text_frame,
    textvariable=selected_text,
    values=sample_texts,
    font=("Arial", 11),
    width=30,
    state="readonly"
)
text_combo.pack(padx=10, pady=10)

# Display area (shows the sample text with selected font)
display_frame = tk.LabelFrame(
    main_frame,
    text="Preview",
    font=("Arial", 11, "bold"),
    bg="#fff8e7",
    fg="#8b4513"
)
display_frame.pack(pady=10, fill="both", expand=True)

# The actual sample display
sample_label = tk.Label(
    display_frame,
    text=selected_text.get(),
    font=(selected_font.get(), selected_size.get()),
    bg="white",
    fg="#2c3e50",
    wraplength=500,
    relief="sunken",
    padx=20,
    pady=20
)
sample_label.pack(fill="both", expand=True, padx=10, pady=10)

# Function to update the display
def update_font_display():
    try:
        font_name = selected_font.get()
        size = selected_size.get()
        
        # Validate size is a number
        if not isinstance(size, int) or size < 6 or size > 100:
            size = 20
            selected_size.set(20)
        
        # Update sample label
        sample_label.config(
            font=(font_name, size),
            text=selected_text.get()
        )
        
        # Update font description
        font_desc_label.config(text=available_fonts.get(font_name, ""))
        
        # Update status
        status_label.config(
            text=f"Using font: {font_name} Size: {size}",
            fg="#27ae60"
        )
    except Exception as e:
        status_label.config(
            text=f"Error: {str(e)}",
            fg="#e74c3c"
        )

# Function to validate size input (for editable combobox)
def validate_size():
    try:
        value = int(selected_size.get())
        if 6 <= value <= 100:
            update_font_display()
        else:
            status_label.config(
                text="Please enter size between 6-100",
                fg="#e74c3c"
            )
    except ValueError:
        status_label.config(
            text="Please enter a valid number",
            fg="#e74c3c"
        )

# Bind events
font_combo.bind("<<ComboboxSelected>>", lambda e: update_font_display())
size_combo.bind("<<ComboboxSelected>>", lambda e: update_font_display())
size_combo.bind("<Return>", lambda e: validate_size())  # Enter key for custom size
text_combo.bind("<<ComboboxSelected>>", lambda e: update_font_display())

# Dark mode toggle (additional feature)
def toggle_dark_mode():
    if dark_mode.get():
        bg_color = "#2c3e50"
        fg_color = "#ecf0f1"
        widget_bg = "#34495e"
        display_bg = "#2c3e50"
    else:
        bg_color = "#fff8e7"
        fg_color = "#2c3e50"
        widget_bg = "#fff8e7"
        display_bg = "white"
    
    # Update root and frames
    root.config(bg=bg_color)
    main_frame.config(bg=bg_color)
    control_frame.config(bg=bg_color)
    
    # Update all widgets in main_frame
    for widget in main_frame.winfo_children():
        try:
            widget.config(bg=bg_color, fg=fg_color)
        except:
            pass
        # Update children of child widgets
        if isinstance(widget, tk.LabelFrame):
            for child in widget.winfo_children():
                try:
                    child.config(bg=bg_color, fg=fg_color)
                except:
                    pass
    
    # Update sample label specially
    sample_label.config(bg=display_bg)
    
    # Update status
    mode = "Dark" if dark_mode.get() else "Light"
    status_label.config(
        text=f"Mode: {mode} - Using font: {selected_font.get()}",
        bg="#34495e" if dark_mode.get() else "#ecf0f1",
        fg="#ecf0f1" if dark_mode.get() else "#7f8c8d"
    )

dark_toggle = tk.Checkbutton(
    main_frame,
    text="Enable Dark Mode",
    variable=dark_mode,
    command=toggle_dark_mode,
    font=("Arial", 10),
    bg="#fff8e7"
)
dark_toggle.pack(pady=5)

# Status bar
status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 9),
    bg="#ecf0f1",
    fg="#7f8c8d",
    relief="sunken",
    anchor="w",
    padx=10
)
status_label.pack(side="bottom", fill="x")

# Initial update
update_font_display()

root.mainloop()