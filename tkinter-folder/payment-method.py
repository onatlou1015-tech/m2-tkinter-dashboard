import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Payment Method Selector")
root.geometry("500x600")
root.configure(bg="#f0f0f0")

# Title
tk.Label(
    root,
    text="Payment Method",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
).pack(pady=15)

# Variable to store selected payment method
# All radiobuttons with the same variable are in the SAME group
payment_method = tk.StringVar(value="cash")  # Default selection

# ===== DEFINE FUNCTIONS FIRST =====

# Function to enable/disable fields based on selection
def update_fields():
    method = payment_method.get()
    
    # Enable/disable based on payment method
    if method == "cash":
        cash_entry.config(state="normal", bg="white")
        credit_entry.config(state="disabled", bg="#e0e0e0")
        crypto_entry.config(state="disabled", bg="#e0e0e0")
        status_label.config(text="Selected: Cash - Enter amount", fg="#27ae60")
    
    elif method == "credit":
        cash_entry.config(state="disabled", bg="#e0e0e0")
        credit_entry.config(state="normal", bg="white")
        crypto_entry.config(state="disabled", bg="#e0e0e0")
        status_label.config(text="Selected: Credit Card - Enter card number", fg="#27ae60")
    
    elif method == "crypto":
        cash_entry.config(state="disabled", bg="#e0e0e0")
        credit_entry.config(state="disabled", bg="#e0e0e0")
        crypto_entry.config(state="normal", bg="white")
        status_label.config(text="Selected: Crypto - Enter wallet address", fg="#27ae60")

# Function to reset the form
def reset_form():
    payment_method.set("cash")
    cash_entry.delete(0, "end")
    credit_entry.delete(0, "end")
    crypto_entry.delete(0, "end")
    update_fields()
    status_label.config(text="Form reset", fg="#7f8c8d")

# Function to show selected payment method
def show_selection():
    method = payment_method.get()
    if method == "cash":
        amount = cash_entry.get()
        if amount:
            status_label.config(text=f"Paying {amount} THB in Cash", fg="#2980b9")
        else:
            status_label.config(text="Please enter amount", fg="#e74c3c")
    elif method == "credit":
        card = credit_entry.get()
        if len(card) >= 4:
            status_label.config(text=f"Paying with Credit Card ending in {card[-4:]}", fg="#2980b9")
        else:
            status_label.config(text="Please enter card number", fg="#e74c3c")
    elif method == "crypto":
        wallet = crypto_entry.get()
        if wallet:
            status_label.config(text=f"Paying with Crypto wallet: {wallet[:6]}...", fg="#2980b9")
        else:
            status_label.config(text="Please enter wallet address", fg="#e74c3c")

# ===== NOW BUILD THE GUI =====

# Frame for payment options
payment_frame = tk.LabelFrame(
    root,
    text="Select Payment Method",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
payment_frame.pack(pady=10, padx=20, fill="x")

# Radiobuttons - all use the SAME variable
tk.Radiobutton(
    payment_frame,
    text="Cash",
    variable=payment_method,
    value="cash",
    font=("Arial", 11),
    bg="#f0f0f0",
    command=update_fields
).pack(anchor="w", padx=20, pady=5)

tk.Radiobutton(
    payment_frame,
    text="Credit Card",
    variable=payment_method,
    value="credit",
    font=("Arial", 11),
    bg="#f0f0f0",
    command=update_fields
).pack(anchor="w", padx=20, pady=5)

tk.Radiobutton(
    payment_frame,
    text="Crypto Currency",
    variable=payment_method,
    value="crypto",
    font=("Arial", 11),
    bg="#f0f0f0",
    command=update_fields
).pack(anchor="w", padx=20, pady=5)

# Frame for payment details
details_frame = tk.LabelFrame(
    root,
    text="Payment Details",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
details_frame.pack(pady=10, padx=20, fill="x")

# Cash details
cash_frame = tk.Frame(details_frame, bg="#f0f0f0")
cash_frame.pack(fill="x", pady=5)

tk.Label(
    cash_frame,
    text="Amount:",
    font=("Arial", 11),
    bg="#f0f0f0"
).pack(side="left", padx=5)

cash_entry = tk.Entry(cash_frame, width=15, font=("Arial", 11))
cash_entry.pack(side="left", padx=5)

tk.Label(
    cash_frame,
    text="THB",
    font=("Arial", 11),
    bg="#f0f0f0"
).pack(side="left", padx=5)

# Credit Card details
credit_frame = tk.Frame(details_frame, bg="#f0f0f0")
credit_frame.pack(fill="x", pady=5)

tk.Label(
    credit_frame,
    text="Card Number:",
    font=("Arial", 11),
    bg="#f0f0f0"
).pack(side="left", padx=5)

credit_entry = tk.Entry(credit_frame, width=20, font=("Arial", 11))
credit_entry.pack(side="left", padx=5)

# Crypto details
crypto_frame = tk.Frame(details_frame, bg="#f0f0f0")
crypto_frame.pack(fill="x", pady=5)

tk.Label(
    crypto_frame,
    text="Wallet Address:",
    font=("Arial", 11),
    bg="#f0f0f0"
).pack(side="left", padx=5)

crypto_entry = tk.Entry(crypto_frame, width=20, font=("Arial", 11))
crypto_entry.pack(side="left", padx=5)

# Button frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="Pay Now",
    command=show_selection,
    bg="#27ae60",
    fg="white",
    font=("Arial", 12),
    padx=20,
    pady=8,
    cursor="hand2"
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Reset",
    command=reset_form,
    bg="#95a5a6",
    fg="white",
    font=("Arial", 10),
    padx=15,
    pady=5
).pack(side="left", padx=5)

# Status label
status_label = tk.Label(
    root,
    text="Select a payment method",
    font=("Arial", 11),
    bg="#f0f0f0",
    fg="#7f8c8d"
)
status_label.pack(pady=10)

# Initialize fields (call the function after it's defined)
update_fields()

root.mainloop()