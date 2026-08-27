import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Shopping Cart")
root.geometry("650x500")
root.configure(bg="#f8f9fa")

# List of products with prices in Thai Baht
products = {
    "Laptop": 29999.00,
    "Smartphone": 15999.00,
    "Headphones": 2490.00,
    "Keyboard": 890.00,
    "Mouse": 450.00,
    "Monitor": 6990.00,
    "Printer": 4990.00,
    "Tablet": 7990.00,
    "Smartwatch": 5990.00,
    "Speakers": 2190.00,
    "Camera": 12990.00,
    "External Hard Drive": 1990.00
}

# Header
tk.Label(
    root,
    text="Shopping Cart",
    font=("Arial", 20, "bold"),
    bg="#f8f9fa",
    fg="#2c3e50"
).pack(pady=10)

tk.Label(
    root,
    text="Hold CTRL to select multiple items",
    font=("Arial", 11),
    bg="#f8f9fa",
    fg="#7f8c8d"
).pack()

# Main frame
main_frame = tk.Frame(root, bg="#f8f9fa")
main_frame.pack(pady=10, padx=20, fill="both", expand=True)

# Left side: Product list
product_frame = tk.LabelFrame(
    main_frame,
    text="Products",
    font=("Arial", 12, "bold"),
    bg="#f8f9fa",
    fg="#2c3e50"
)
product_frame.pack(side="left", fill="both", expand=True, padx=(0,10))

# Create Listbox with MULTIPLE selection mode
product_scrollbar = tk.Scrollbar(product_frame)
product_scrollbar.pack(side="right", fill="y")

product_listbox = tk.Listbox(
    product_frame,
    selectmode="multiple",  # MULTIPLE - can select multiple items
    font=("Arial", 11),
    bg="#ffffff",
    fg="#2c3e50",
    height=15,
    width=30,
    yscrollcommand=product_scrollbar.set
)
product_listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)

product_scrollbar.config(command=product_listbox.yview)

# Insert products into listbox
for product in products.keys():
    product_listbox.insert("end", product)

# Right side: Cart and Total
cart_frame = tk.LabelFrame(
    main_frame,
    text="Your Cart",
    font=("Arial", 12, "bold"),
    bg="#f8f9fa",
    fg="#2c3e50"
)
cart_frame.pack(side="right", fill="both", expand=True, padx=(10,0))

# Cart listbox
cart_scrollbar = tk.Scrollbar(cart_frame)
cart_scrollbar.pack(side="right", fill="y")

cart_listbox = tk.Listbox(
    cart_frame,
    selectmode="browse",
    font=("Arial", 11),
    bg="#ffffff",
    fg="#2c3e50",
    height=10,
    width=25,
    yscrollcommand=cart_scrollbar.set
)
cart_listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)

cart_scrollbar.config(command=cart_listbox.yview)

# Total display
total_label = tk.Label(
    cart_frame,
    text="Total: ฿0.00",
    font=("Arial", 16, "bold"),
    bg="#f8f9fa",
    fg="#27ae60"
)
total_label.pack(pady=10)

# Function to add selected items to cart
def add_to_cart():
    # Get all selected indices
    selected_indices = product_listbox.curselection()
    
    if not selected_indices:
        status_label.config(
            text="Please select at least one product",
            fg="#e74c3c"
        )
        return
    
    # Add selected items to cart
    added_count = 0
    for index in selected_indices:
        product = product_listbox.get(index)
        # Check if already in cart
        cart_items = list(cart_listbox.get(0, "end"))
        if product not in cart_items:
            cart_listbox.insert("end", product)
            added_count += 1
    
    # Update total
    update_total()
    
    # Clear selection
    product_listbox.selection_clear(0, "end")
    
    if added_count > 0:
        status_label.config(
            text=f"Added {added_count} item(s) to cart",
            fg="#27ae60"
        )
    else:
        status_label.config(
            text="Items already in cart",
            fg="#e67e22"
        )

# Function to remove selected items from cart
def remove_from_cart():
    selected_indices = cart_listbox.curselection()
    
    if not selected_indices:
        status_label.config(
            text="Please select item(s) to remove",
            fg="#e74c3c"
        )
        return
    
    # Remove items (in reverse order to maintain indices)
    for index in reversed(selected_indices):
        cart_listbox.delete(index)
    
    update_total()
    status_label.config(
        text="Removed item(s) from cart",
        fg="#e74c3c"
    )

# Function to clear entire cart
def clear_cart():
    cart_listbox.delete(0, "end")
    update_total()
    status_label.config(
        text="Cart cleared",
        fg="#7f8c8d"
    )

# Function to update total cost
def update_total():
    total = 0.0
    cart_items = cart_listbox.get(0, "end")
    
    for item in cart_items:
        if item in products:
            total += products[item]
    
    # Format with comma separators for thousands
    total_label.config(text=f"Total: ฿{total:,.2f}")
    
    # Show item count
    item_count = len(cart_items)
    if item_count > 0:
        count_label.config(text=f"Items: {item_count}")
    else:
        count_label.config(text="Cart is empty")

# Button frame
button_frame = tk.Frame(cart_frame, bg="#f8f9fa")
button_frame.pack(pady=5)

add_button = tk.Button(
    button_frame,
    text="Add to Cart",
    command=add_to_cart,
    bg="#27ae60",
    fg="white",
    font=("Arial", 10),
    padx=10,
    pady=5,
    width=12
)
add_button.pack(side="left", padx=5)

remove_button = tk.Button(
    button_frame,
    text="Remove",
    command=remove_from_cart,
    bg="#e74c3c",
    fg="white",
    font=("Arial", 10),
    padx=10,
    pady=5,
    width=12
)
remove_button.pack(side="left", padx=5)

clear_button = tk.Button(
    cart_frame,
    text="Clear Cart",
    command=clear_cart,
    bg="#95a5a6",
    fg="white",
    font=("Arial", 10),
    padx=15,
    pady=5
)
clear_button.pack(pady=5)

# Item count
count_label = tk.Label(
    cart_frame,
    text="Cart is empty",
    font=("Arial", 10),
    bg="#f8f9fa",
    fg="#7f8c8d"
)
count_label.pack()

# Bottom frame for additional info
bottom_frame = tk.Frame(root, bg="#f8f9fa")
bottom_frame.pack(pady=5, padx=20, fill="x")

# Show all products with prices
def show_price_list():
    price_text = "Product Prices:\n"
    for product, price in products.items():
        price_text += f"{product}: ฿{price:.2f}\n"
    return price_text

price_button = tk.Button(
    bottom_frame,
    text="Show Price List",
    command=lambda: show_prices(),
    bg="#3498db",
    fg="white",
    font=("Arial", 9),
    padx=10
)
price_button.pack(side="left")

def show_prices():
    price_window = tk.Toplevel(root)
    price_window.title("Price List")
    price_window.geometry("350x450")
    
    tk.Label(
        price_window,
        text="Product Prices",
        font=("Arial", 14, "bold")
    ).pack(pady=10)
    
    price_listbox = tk.Listbox(price_window, font=("Arial", 10), width=35, height=15)
    price_listbox.pack(padx=10, pady=10, fill="both", expand=True)
    
    for product, price in products.items():
        price_listbox.insert("end", f"{product}: ฿{price:,.2f}")
    
    tk.Button(
        price_window,
        text="Close",
        command=price_window.destroy,
        bg="#95a5a6",
        fg="white",
        padx=15
    ).pack(pady=10)

# Status bar
status_label = tk.Label(
    root,
    text="Select products and click 'Add to Cart'",
    font=("Arial", 10),
    bg="#ecf0f1",
    fg="#7f8c8d",
    relief="sunken",
    anchor="w",
    padx=10
)
status_label.pack(side="bottom", fill="x")

root.mainloop()