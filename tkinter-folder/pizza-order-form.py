import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Pizza Order Form")
root.geometry("400x350")

# Topping prices dictionary
topping_prices = {
    "Pepperoni": 22.50,
    "Mushrooms": 31.50,
    "Olives": 11.00,
    "Extra Cheese": 31.75,
    "Bacon": 32.00
}

topping_vars = {}


tk.Label(root, text="Choose Your Toppings", font=("Arial", 16, "bold")).pack(pady=10)


def update_total():
    total = 0.0
    for topping, var in topping_vars.items():
        if var.get() == 1:  # Checked
            total += topping_prices[topping]
    total_label.config(text=f"Total: ${total:.2f}")


def reset_order():
    for var in topping_vars.values():
        var.set(0)
    update_total()


for topping, price in topping_prices.items():
    var = tk.IntVar(value=0)  # 0 = unchecked, 1 = checked
    topping_vars[topping] = var
    
    cb = tk.Checkbutton(
        root, 
        text=f"{topping} (฿{price:.2f})", 
        variable=var,
        command=update_total,
        font=("Arial", 11)
    )
    cb.pack(anchor="w", padx=50, pady=2)

ttk.Separator(root, orient="horizontal").pack(fill="x", pady=15, padx=20)

total_label = tk.Label(
    root, 
    text="Total: ฿0.00", 
    font=("Arial", 18, "bold"),
    fg="green"
)
total_label.pack(pady=10)


tk.Button(
    root, 
    text="Reset Order", 
    command=reset_order,
    bg="#f0f0f0",
    padx=20
).pack(pady=10)

root.mainloop()