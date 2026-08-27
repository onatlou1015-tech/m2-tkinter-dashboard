import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Movie Ticket Selector")
root.geometry("450x400")
root.configure(bg="#f0f0f0")

# Ticket prices in Thai Baht
TICKET_PRICE = 180  # Baht per ticket

# Variables
ticket_quantity = tk.IntVar(value=1)

# ===== DEFINE FUNCTIONS FIRST =====

# Function to update total
def update_total():
    qty = ticket_quantity.get()
    total = qty * TICKET_PRICE
    
    # Update labels
    qty_label.config(text=f"{qty} ticket(s)")
    total_label.config(text=f"{total:,.2f} THB")
    
    # Update status
    status_label.config(
        text=f"Selected {qty} ticket(s) - Total: {total:,.2f} THB",
        fg="#27ae60"
    )

# Function to set quantity from buttons
def set_quantity(value):
    ticket_quantity.set(value)
    update_total()

# ===== NOW BUILD THE GUI =====

# Title
tk.Label(
    root,
    text="Movie Ticket Selector",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
).pack(pady=15)

# Movie info frame
movie_frame = tk.LabelFrame(
    root,
    text="Movie Details",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
movie_frame.pack(pady=10, padx=20, fill="x")

tk.Label(
    movie_frame,
    text="Movie: Avengers: Endgame",
    font=("Arial", 12),
    bg="#f0f0f0",
    fg="#34495e"
).pack(anchor="w", padx=10, pady=2)

tk.Label(
    movie_frame,
    text=f"Ticket Price: {TICKET_PRICE} THB",
    font=("Arial", 12),
    bg="#f0f0f0",
    fg="#34495e"
).pack(anchor="w", padx=10, pady=2)

# Ticket quantity frame
quantity_frame = tk.LabelFrame(
    root,
    text="Ticket Quantity",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
quantity_frame.pack(pady=10, padx=20, fill="x")

# Frame for spinbox and buttons
spin_frame = tk.Frame(quantity_frame, bg="#f0f0f0")
spin_frame.pack(pady=15)

tk.Label(
    spin_frame,
    text="Number of Tickets:",
    font=("Arial", 11),
    bg="#f0f0f0"
).pack(side="left", padx=5)

# Spinbox for quantity (1-10)
ticket_spinbox = tk.Spinbox(
    spin_frame,
    from_=1,
    to=10,
    width=5,
    font=("Arial", 14),
    textvariable=ticket_quantity,
    command=update_total  # Updates when arrows are clicked
)
ticket_spinbox.pack(side="left", padx=10)

# Quick buttons
quick_frame = tk.Frame(quantity_frame, bg="#f0f0f0")
quick_frame.pack(pady=5)

tk.Button(
    quick_frame,
    text="1",
    command=lambda: set_quantity(1),
    bg="#3498db",
    fg="white",
    width=4,
    font=("Arial", 10)
).pack(side="left", padx=2)

tk.Button(
    quick_frame,
    text="2",
    command=lambda: set_quantity(2),
    bg="#3498db",
    fg="white",
    width=4,
    font=("Arial", 10)
).pack(side="left", padx=2)

tk.Button(
    quick_frame,
    text="5",
    command=lambda: set_quantity(5),
    bg="#3498db",
    fg="white",
    width=4,
    font=("Arial", 10)
).pack(side="left", padx=2)

tk.Button(
    quick_frame,
    text="10",
    command=lambda: set_quantity(10),
    bg="#3498db",
    fg="white",
    width=4,
    font=("Arial", 10)
).pack(side="left", padx=2)

# Summary frame
summary_frame = tk.LabelFrame(
    root,
    text="Order Summary",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
summary_frame.pack(pady=10, padx=20, fill="x")

# Display labels
tk.Label(
    summary_frame,
    text="Quantity:",
    font=("Arial", 11),
    bg="#f0f0f0"
).pack(anchor="w", padx=10, pady=2)

qty_label = tk.Label(
    summary_frame,
    text="1 ticket(s)",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="#2980b9"
)
qty_label.pack(anchor="w", padx=20, pady=2)

tk.Label(
    summary_frame,
    text="Total Price:",
    font=("Arial", 11),
    bg="#f0f0f0"
).pack(anchor="w", padx=10, pady=2)

total_label = tk.Label(
    summary_frame,
    text=f"{TICKET_PRICE:,.2f} THB",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0",
    fg="#27ae60"
)
total_label.pack(anchor="w", padx=20, pady=5)

# Status label
status_label = tk.Label(
    root,
    text="Select ticket quantity",
    font=("Arial", 11),
    bg="#f0f0f0",
    fg="#7f8c8d"
)
status_label.pack(pady=10)

# Initialize
update_total()

root.mainloop()