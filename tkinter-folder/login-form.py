import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("450x400")
root.configure(bg="#f0f0f0")

# ===== DEFINE FUNCTIONS FIRST =====

# Function to toggle password visibility
def toggle_password():
    if show_password_var.get() == 1:
        # Show password
        password_entry.config(show="")
        toggle_button.config(text="Hide Password")
    else:
        # Hide password
        password_entry.config(show="*")
        toggle_button.config(text="Show Password")

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "" or password == "":
        status_label.config(text="Please enter both username and password", fg="#e74c3c")
    elif username == "admin" and password == "password123":
        status_label.config(text="Login Successful! Welcome admin!", fg="#27ae60")
    else:
        status_label.config(text="Invalid username or password!", fg="#e74c3c")

# Function to clear the form
def clear_form():
    username_entry.delete(0, "end")
    password_entry.delete(0, "end")
    show_password_var.set(0)
    password_entry.config(show="*")
    toggle_button.config(text="Show Password")
    status_label.config(text="Form cleared", fg="#7f8c8d")

# ===== NOW BUILD THE GUI =====

# Title
tk.Label(
    root,
    text="Login Form",
    font=("Arial", 20, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
).pack(pady=20)

# Login frame
login_frame = tk.LabelFrame(
    root,
    text="Enter Your Credentials",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
login_frame.pack(pady=10, padx=30, fill="x")

# Username
tk.Label(
    login_frame,
    text="Username:",
    font=("Arial", 11),
    bg="#f0f0f0",
    fg="#2c3e50"
).pack(anchor="w", padx=10, pady=(10,2))

username_entry = tk.Entry(
    login_frame,
    font=("Arial", 12),
    width=25
)
username_entry.pack(padx=10, pady=5, fill="x")

# Password
tk.Label(
    login_frame,
    text="Password:",
    font=("Arial", 11),
    bg="#f0f0f0",
    fg="#2c3e50"
).pack(anchor="w", padx=10, pady=(10,2))

# Password entry with hidden text
password_entry = tk.Entry(
    login_frame,
    font=("Arial", 12),
    width=25,
    show="*"  # Hides password with asterisks
)
password_entry.pack(padx=10, pady=5, fill="x")

# Show password checkbox
show_password_var = tk.IntVar(value=0)

toggle_button = tk.Checkbutton(
    login_frame,
    text="Show Password",
    variable=show_password_var,
    command=toggle_password,  # This will work now
    bg="#f0f0f0",
    font=("Arial", 10)
)
toggle_button.pack(anchor="w", padx=10, pady=5)

# Button frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

tk.Button(
    button_frame,
    text="Login",
    command=login,  # This will work now
    bg="#27ae60",
    fg="white",
    font=("Arial", 12),
    padx=25,
    pady=8,
    cursor="hand2"
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Clear",
    command=clear_form,  # This will work now
    bg="#95a5a6",
    fg="white",
    font=("Arial", 12),
    padx=25,
    pady=8,
    cursor="hand2"
).pack(side="left", padx=5)

# Status label
status_label = tk.Label(
    root,
    text="Enter username and password",
    font=("Arial", 11),
    bg="#f0f0f0",
    fg="#7f8c8d"
)
status_label.pack(pady=10)

# Hint label
tk.Label(
    root,
    text="Hint: Use 'admin' as username and 'password123' as password",
    font=("Arial", 9),
    bg="#f0f0f0",
    fg="#95a5a6"
).pack(pady=5)

root.mainloop()