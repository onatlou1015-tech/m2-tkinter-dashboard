import tkinter as tk
from tkinter import ttk
import time

# Create main window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("400x350")
root.configure(bg="#f0f0f0")

# Title
tk.Label(
    root,
    text="Countdown Timer",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
).pack(pady=15)

# Time input
time_frame = tk.Frame(root, bg="#f0f0f0")
time_frame.pack(pady=5)

tk.Label(
    time_frame,
    text="Set time (seconds):",
    font=("Arial", 11),
    bg="#f0f0f0"
).pack(side="left", padx=5)

# Spinbox to choose seconds
seconds_spin = tk.Spinbox(
    time_frame,
    from_=5,
    to=60,
    width=5,
    font=("Arial", 12)
)
seconds_spin.pack(side="left", padx=5)
seconds_spin.delete(0, "end")
seconds_spin.insert(0, "10")

# Progress bar
progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=300,
    mode="determinate",
    maximum=100
)
progress.pack(pady=20)

# Label to show percentage
percent_label = tk.Label(
    root,
    text="100%",
    font=("Arial", 14, "bold"),
    bg="#f0f0f0",
    fg="#2980b9"
)
percent_label.pack(pady=5)

# Label to show time remaining
time_label = tk.Label(
    root,
    text="Time remaining: 10 seconds",
    font=("Arial", 12),
    bg="#f0f0f0",
    fg="#2c3e50"
)
time_label.pack(pady=5)

# Status label
status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 11),
    bg="#f0f0f0",
    fg="#7f8c8d"
)
status_label.pack(pady=5)

# Function to start countdown
def start_countdown():
    # Get the number of seconds
    try:
        total_seconds = int(seconds_spin.get())
        if total_seconds < 1:
            status_label.config(text="Please enter a number >= 1", fg="#e74c3c")
            return
    except:
        status_label.config(text="Please enter a valid number", fg="#e74c3c")
        return
    
    # Disable controls during countdown
    start_button.config(state="disabled")
    seconds_spin.config(state="disabled")
    status_label.config(text="Counting down...", fg="#27ae60")
    
    # Reset progress to 100%
    progress["value"] = 100
    percent_label.config(text="100%")
    
    # Countdown loop
    for remaining in range(total_seconds, -1, -1):
        # Calculate percentage
        percent = (remaining / total_seconds) * 100
        progress["value"] = percent
        percent_label.config(text=f"{int(percent)}%")
        time_label.config(text=f"Time remaining: {remaining} seconds")
        root.update()
        time.sleep(1)  # Wait 1 second
    
    # Countdown complete
    progress["value"] = 0
    percent_label.config(text="0%", fg="#e74c3c")
    time_label.config(text="Time's up!", fg="#e74c3c")
    status_label.config(text="Countdown finished!", fg="#e74c3c")
    
    # Re-enable controls
    start_button.config(state="normal")
    seconds_spin.config(state="normal")

# Start button
start_button = tk.Button(
    root,
    text="Start Countdown",
    command=start_countdown,
    bg="#e67e22",
    fg="white",
    font=("Arial", 12),
    padx=20,
    pady=8,
    cursor="hand2"
)
start_button.pack(pady=10)

# Reset button
def reset_timer():
    progress["value"] = 100
    percent_label.config(text="100%", fg="#2980b9")
    time_label.config(text=f"Time remaining: {seconds_spin.get()} seconds", fg="#2c3e50")
    status_label.config(text="Ready", fg="#7f8c8d")
    start_button.config(state="normal")
    seconds_spin.config(state="normal")

reset_button = tk.Button(
    root,
    text="Reset",
    command=reset_timer,
    bg="#95a5a6",
    fg="white",
    font=("Arial", 10),
    padx=15,
    pady=5
)
reset_button.pack()

root.mainloop()