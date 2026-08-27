import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Country and Capital Selector")
root.geometry("500x400")
root.configure(bg="#f0f8ff")

# Dictionary of countries and their capitals (focusing on Southeast Asia)
country_capitals = {
    "Thailand": "Bangkok",
    "Laos": "Vientiane",
    "Cambodia": "Phnom Penh",
    "Vietnam": "Hanoi",
    "Myanmar": "Naypyidaw",
    "Malaysia": "Kuala Lumpur",
    "Singapore": "Singapore",
    "Indonesia": "Jakarta",
    "Philippines": "Manila",
    "Japan": "Tokyo",
    "South Korea": "Seoul",
    "China": "Beijing",
    "India": "New Delhi",
    "United States": "Washington D.C.",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Australia": "Canberra"
}

# Header
header_label = tk.Label(
    root,
    text="Select a Country to See Its Capital",
    font=("Arial", 16, "bold"),
    bg="#f0f8ff",
    fg="#2c3e50"
)
header_label.pack(pady=20)

# Subtitle
tk.Label(
    root,
    text="Choose a country from the list below",
    font=("Arial", 11),
    bg="#f0f8ff",
    fg="#34495e"
).pack(pady=5)

# Variable to store selected country
selected_country = tk.StringVar()

# Combobox for country selection (READ-ONLY)
country_combo = ttk.Combobox(
    root,
    textvariable=selected_country,
    values=list(country_capitals.keys()),
    font=("Arial", 12),
    width=30,
    state="readonly"  # Read-only mode
)
country_combo.pack(pady=15)

# Function to update capital display
def show_capital():
    country = selected_country.get()
    if country in country_capitals:
        capital = country_capitals[country]
        result_label.config(
            text=f"Capital of {country} is {capital}",
            fg="#27ae60"
        )
        info_text.set(f"Country: {country}\nCapital: {capital}")
    else:
        result_label.config(
            text="Please select a country from the list",
            fg="#e74c3c"
        )
        info_text.set("Please select a valid country")

# Button to show capital
show_button = tk.Button(
    root,
    text="Show Capital",
    command=show_capital,
    font=("Arial", 12),
    bg="#3498db",
    fg="white",
    padx=20,
    pady=5,
    cursor="hand2"
)
show_button.pack(pady=10)

# Result label (big display)
result_label = tk.Label(
    root,
    text="Select a country and click the button",
    font=("Arial", 14, "bold"),
    bg="#f0f8ff",
    fg="#7f8c8d",
    wraplength=400
)
result_label.pack(pady=15)

# Information display (detailed)
info_frame = tk.LabelFrame(
    root,
    text="Country Information",
    font=("Arial", 11, "bold"),
    bg="#f0f8ff",
    fg="#2c3e50"
)
info_frame.pack(pady=10, padx=30, fill="x")

info_text = tk.StringVar()
info_text.set("Waiting for country selection...")

info_label = tk.Label(
    info_frame,
    textvariable=info_text,
    font=("Arial", 12),
    bg="#f0f8ff",
    fg="#2c3e50",
    justify="left"
)
info_label.pack(pady=10, padx=20)

# Status bar (shows selected value)
status_label = tk.Label(
    root,
    text="Status: Ready",
    font=("Arial", 10),
    bg="#ecf0f1",
    fg="#7f8c8d",
    relief="sunken",
    anchor="w",
    padx=10
)
status_label.pack(side="bottom", fill="x", pady=(10,0))

# Function to update status when selection changes
def on_country_select(event):
    country = selected_country.get()
    if country in country_capitals:
        status_label.config(
            text=f"Selected: {country} - Capital: {country_capitals[country]}",
            fg="#27ae60"
        )
    else:
        status_label.config(
            text="Please select a country from the list only",
            fg="#e74c3c"
        )

# Bind selection event
country_combo.bind("<<ComboboxSelected>>", on_country_select)

# Additional feature: Auto-show capital when selected
def auto_show_capital(event=None):
    if selected_country.get() in country_capitals:
        show_capital()

# Auto-show when selected
country_combo.bind("<<ComboboxSelected>>", auto_show_capital)

root.mainloop()