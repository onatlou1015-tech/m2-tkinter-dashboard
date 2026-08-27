import tkinter as tk
from tkinter import ttk
import time

# Create main window
root = tk.Tk()
root.title("File Download Simulator")
root.geometry("500x350")
root.configure(bg="#f0f4f8")

# Variables
download_progress = tk.IntVar(value=0)
is_downloading = False
download_speed = 100  # milliseconds per update

# Header
tk.Label(
    root,
    text="File Download Simulator",
    font=("Arial", 18, "bold"),
    bg="#f0f4f8",
    fg="#2c3e50"
).pack(pady=15)

# File information
file_frame = tk.LabelFrame(
    root,
    text="File Information",
    font=("Arial", 11, "bold"),
    bg="#f0f4f8",
    fg="#2c3e50"
)
file_frame.pack(pady=5, padx=20, fill="x")

tk.Label(
    file_frame,
    text="File: Python_Programming_Course.zip",
    font=("Arial", 11),
    bg="#f0f4f8",
    fg="#34495e"
).pack(anchor="w", padx=10, pady=2)

tk.Label(
    file_frame,
    text="File Size: 1.2 GB",
    font=("Arial", 11),
    bg="#f0f4f8",
    fg="#34495e"
).pack(anchor="w", padx=10, pady=2)

tk.Label(
    file_frame,
    text="Download Speed: 10 MB/s",
    font=("Arial", 11),
    bg="#f0f4f8",
    fg="#34495e"
).pack(anchor="w", padx=10, pady=2)

# Progress bar
progress_frame = tk.LabelFrame(
    root,
    text="Download Progress",
    font=("Arial", 11, "bold"),
    bg="#f0f4f8",
    fg="#2c3e50"
)
progress_frame.pack(pady=10, padx=20, fill="x")

# Progress bar (determinate mode - we know total size)
progress_bar = ttk.Progressbar(
    progress_frame,
    variable=download_progress,
    maximum=100,
    mode="determinate",
    length=400
)
progress_bar.pack(pady=10, padx=10)

# Progress label
progress_label = tk.Label(
    progress_frame,
    text="0% Complete",
    font=("Arial", 12, "bold"),
    bg="#f0f4f8",
    fg="#2980b9"
)
progress_label.pack(pady=5)

# Download details
details_frame = tk.Frame(progress_frame, bg="#f0f4f8")
details_frame.pack(pady=5)

# Downloaded size
downloaded_label = tk.Label(
    details_frame,
    text="Downloaded: 0 MB",
    font=("Arial", 10),
    bg="#f0f4f8",
    fg="#7f8c8d"
)
downloaded_label.pack(side="left", padx=15)

# Remaining time
time_label = tk.Label(
    details_frame,
    text="Remaining: --:--",
    font=("Arial", 10),
    bg="#f0f4f8",
    fg="#7f8c8d"
)
time_label.pack(side="left", padx=15)

# Function to format time
def format_time(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"

# Function to simulate download
def start_download():
    global is_downloading
    
    if is_downloading:
        return
    
    is_downloading = True
    download_progress.set(0)
    status_label.config(text="Downloading...", fg="#27ae60")
    start_button.config(state="disabled", text="Downloading...")
    pause_button.config(state="normal")
    reset_button.config(state="disabled")
    
    # Calculate total time (simulated)
    total_time = 100  # 100 steps at 100ms each = 10 seconds
    start_time = time.time()
    
    def update_progress():
        global is_downloading
        
        if not is_downloading:
            return
        
        current = download_progress.get()
        
        if current < 100:
            # Increase by 1%
            new_value = current + 1
            download_progress.set(new_value)
            
            # Update progress label
            progress_label.config(text=f"{new_value}% Complete")
            
            # Update downloaded size (1.2 GB = 1200 MB)
            downloaded_mb = (new_value / 100) * 1200
            downloaded_label.config(text=f"Downloaded: {downloaded_mb:.1f} MB")
            
            # Update remaining time
            elapsed = time.time() - start_time
            remaining = (total_time - elapsed) * (1 - new_value / 100) / (new_value / 100 + 0.001)
            if remaining > 0:
                time_label.config(text=f"Remaining: {format_time(remaining)}")
            else:
                time_label.config(text="Remaining: 00:00")
            
            # Schedule next update
            root.after(download_speed, update_progress)
        else:
            # Download complete
            progress_label.config(text="100% Complete - Done!", fg="#27ae60")
            downloaded_label.config(text="Downloaded: 1200.0 MB")
            time_label.config(text="Remaining: 00:00")
            status_label.config(text="Download complete!", fg="#27ae60")
            start_button.config(state="normal", text="Start Download")
            pause_button.config(state="disabled")
            reset_button.config(state="normal")
            is_downloading = False
    
    # Start the download
    root.after(100, update_progress)

# Function to pause download
def pause_download():
    global is_downloading
    if is_downloading:
        is_downloading = False
        status_label.config(text="Paused", fg="#e67e22")
        start_button.config(text="Resume Download", state="normal")
        pause_button.config(state="disabled")

# Function to reset download
def reset_download():
    global is_downloading
    is_downloading = False
    download_progress.set(0)
    progress_label.config(text="0% Complete", fg="#2980b9")
    downloaded_label.config(text="Downloaded: 0 MB")
    time_label.config(text="Remaining: --:--")
    status_label.config(text="Ready to download", fg="#7f8c8d")
    start_button.config(text="Start Download", state="normal")
    pause_button.config(state="disabled")
    reset_button.config(state="disabled")

# Button frame
button_frame = tk.Frame(root, bg="#f0f4f8")
button_frame.pack(pady=15)

start_button = tk.Button(
    button_frame,
    text="Start Download",
    command=start_download,
    bg="#27ae60",
    fg="white",
    font=("Arial", 11),
    padx=20,
    pady=8,
    cursor="hand2"
)
start_button.pack(side="left", padx=5)

pause_button = tk.Button(
    button_frame,
    text="Pause",
    command=pause_download,
    bg="#f39c12",
    fg="white",
    font=("Arial", 11),
    padx=20,
    pady=8,
    state="disabled",
    cursor="hand2"
)
pause_button.pack(side="left", padx=5)

reset_button = tk.Button(
    button_frame,
    text="Reset",
    command=reset_download,
    bg="#e74c3c",
    fg="white",
    font=("Arial", 11),
    padx=20,
    pady=8,
    state="disabled",
    cursor="hand2"
)
reset_button.pack(side="left", padx=5)

# Status bar
status_label = tk.Label(
    root,
    text="Ready to download",
    font=("Arial", 10),
    bg="#ecf0f1",
    fg="#7f8c8d",
    relief="sunken",
    anchor="w",
    padx=10
)
status_label.pack(side="bottom", fill="x")

root.mainloop()