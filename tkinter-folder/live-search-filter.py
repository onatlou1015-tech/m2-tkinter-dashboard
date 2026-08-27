import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Live Search Filter")
root.geometry("500x450")
root.configure(bg="#f0f0f0")

# List of items to search through
fruits = [
    "Apple", "Apricot", "Avocado",
    "Banana", "Blackberry", "Blueberry",
    "Cherry", "Coconut", "Cranberry",
    "Durian", "Dragonfruit", "Date",
    "Elderberry", "Fig", "Grape",
    "Grapefruit", "Guava", "Kiwi",
    "Lemon", "Lime", "Lychee",
    "Mango", "Mangosteen", "Melon",
    "Orange", "Papaya", "Passionfruit",
    "Peach", "Pear", "Pineapple",
    "Plum", "Pomegranate", "Raspberry",
    "Strawberry", "Tangerine", "Watermelon"
]

# ===== DEFINE FUNCTIONS FIRST =====

# Function to filter the listbox
def filter_list(*args):
    search_text = search_entry.get().lower()
    
    # Clear the listbox
    listbox.delete(0, "end")
    
    # Add items that match the search
    if search_text == "":
        # Show all items
        for item in fruits:
            listbox.insert("end", item)
    else:
        # Show only matching items
        for item in fruits:
            if search_text in item.lower():
                listbox.insert("end", item)
    
    # Update count label
    count = listbox.size()
    count_label.config(text=f"Found {count} items")

# Function to show selected item
def show_selection():
    selection = listbox.curselection()
    if selection:
        item = listbox.get(selection[0])
        status_label.config(text=f"Selected: {item}", fg="#2980b9")
    else:
        status_label.config(text="Please select an item", fg="#e67e22")

# ===== NOW BUILD THE GUI =====

# Title
tk.Label(
    root,
    text="Live Search Filter",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
).pack(pady=15)

tk.Label(
    root,
    text="Type in the search box to filter the list",
    font=("Arial", 11),
    bg="#f0f0f0",
    fg="#7f8c8d"
).pack()

# Search frame
search_frame = tk.LabelFrame(
    root,
    text="Search",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
search_frame.pack(pady=10, padx=20, fill="x")

# Search entry
tk.Label(
    search_frame,
    text="Type to search:",
    font=("Arial", 11),
    bg="#f0f0f0"
).pack(anchor="w", padx=10, pady=(10,2))

search_entry = tk.Entry(
    search_frame,
    font=("Arial", 12),
    width=30
)
search_entry.pack(padx=10, pady=5, fill="x")

# Bind the search to update on every key press
search_entry.bind("<KeyRelease>", filter_list)

# Listbox frame
listbox_frame = tk.LabelFrame(
    root,
    text="Results",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
listbox_frame.pack(pady=10, padx=20, fill="both", expand=True)

# Create listbox with scrollbar
listbox_scrollbar = tk.Scrollbar(listbox_frame)
listbox_scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(
    listbox_frame,
    selectmode="browse",
    font=("Arial", 11),
    bg="#ffffff",
    yscrollcommand=listbox_scrollbar.set,
    height=10
)
listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)

listbox_scrollbar.config(command=listbox.yview)

# Insert all items initially
for item in fruits:
    listbox.insert("end", item)

# Count label
count_label = tk.Label(
    root,
    text=f"Found {len(fruits)} items",
    font=("Arial", 11),
    bg="#f0f0f0",
    fg="#7f8c8d"
)
count_label.pack(pady=5)

# Button frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Show Selected",
    command=show_selection,
    bg="#3498db",
    fg="white",
    font=("Arial", 11),
    padx=15,
    pady=5,
    cursor="hand2"
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Clear Search",
    command=lambda: clear_search(),
    bg="#95a5a6",
    fg="white",
    font=("Arial", 11),
    padx=15,
    pady=5,
    cursor="hand2"
).pack(side="left", padx=5)

def clear_search():
    search_entry.delete(0, "end")
    filter_list()

# Status label
status_label = tk.Label(
    root,
    text="Type to search or select an item",
    font=("Arial", 11),
    bg="#f0f0f0",
    fg="#7f8c8d"
)
status_label.pack(pady=5)

root.mainloop()