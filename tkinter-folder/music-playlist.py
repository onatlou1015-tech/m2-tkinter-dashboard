import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Music Playlist Player")
root.geometry("550x400")
root.configure(bg="#f0f0f0")

# List of songs
song_list = [
    "Bohemian Rhapsody - Queen",
    "Stairway to Heaven - Led Zeppelin",
    "Imagine - John Lennon",
    "Hotel California - Eagles",
    "Like a Rolling Stone - Bob Dylan",
    "Smells Like Teen Spirit - Nirvana",
    "Billie Jean - Michael Jackson",
    "Hey Jude - The Beatles",
    "Wonderwall - Oasis",
    "Don't Stop Believin' - Journey",
    "Sweet Child O' Mine - Guns N' Roses",
    "Shape of You - Ed Sheeran",
    "Rolling in the Deep - Adele",
    "Uptown Funk - Mark Ronson",
    "Happy - Pharrell Williams"
]

# Header
tk.Label(
    root,
    text="Music Playlist",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
).pack(pady=10)

# Main frame
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(pady=10, padx=20, fill="both", expand=True)

# Left side: Playlist
playlist_frame = tk.LabelFrame(
    main_frame,
    text="Playlist",
    font=("Arial", 11, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
playlist_frame.pack(side="left", fill="both", expand=True, padx=(0,10))

# Create Listbox with scrollbar
playlist_scrollbar = tk.Scrollbar(playlist_frame)
playlist_scrollbar.pack(side="right", fill="y")

playlist = tk.Listbox(
    playlist_frame,
    selectmode="browse",  # Can select one item at a time
    font=("Arial", 11),
    bg="#ffffff",
    fg="#2c3e50",
    height=15,
    width=30,
    yscrollcommand=playlist_scrollbar.set
)
playlist.pack(side="left", fill="both", expand=True, padx=5, pady=5)

playlist_scrollbar.config(command=playlist.yview)

# Insert songs into listbox
for song in song_list:
    playlist.insert("end", song)

# Right side: Now Playing and Controls
now_playing_frame = tk.LabelFrame(
    main_frame,
    text="Now Playing",
    font=("Arial", 11, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
now_playing_frame.pack(side="right", fill="both", expand=True, padx=(10,0))

# Now playing display
now_playing_label = tk.Label(
    now_playing_frame,
    text="No song selected",
    font=("Arial", 14, "bold"),
    bg="#ffffff",
    fg="#7f8c8d",
    relief="sunken",
    padx=20,
    pady=30,
    wraplength=200
)
now_playing_label.pack(pady=20, padx=10, fill="both", expand=True)

# Function to play selected song (called on double-click)
def play_song(event):
    try:
        # Get selected song
        selection = playlist.curselection()
        if selection:
            index = selection[0]
            song = playlist.get(index)
            now_playing_label.config(
                text=f"Now Playing:\n{song}",
                fg="#27ae60"
            )
            status_label.config(
                text=f"Playing: {song}",
                fg="#27ae60"
            )
    except:
        pass

# Bind double-click event
playlist.bind("<Double-Button-1>", play_song)

# Play button
def play_selected():
    selection = playlist.curselection()
    if selection:
        index = selection[0]
        song = playlist.get(index)
        now_playing_label.config(
            text=f"Now Playing:\n{song}",
            fg="#27ae60"
        )
        status_label.config(
            text=f"Playing: {song}",
            fg="#27ae60"
        )
    else:
        status_label.config(
            text="Please select a song first",
            fg="#e74c3c"
        )

play_button = tk.Button(
    now_playing_frame,
    text="Play Selected",
    command=play_selected,
    bg="#27ae60",
    fg="white",
    font=("Arial", 11),
    padx=15,
    pady=5
)
play_button.pack(pady=10)

# Clear button
def clear_now_playing():
    now_playing_label.config(
        text="No song selected",
        fg="#7f8c8d"
    )
    status_label.config(
        text="Cleared",
        fg="#7f8c8d"
    )

clear_button = tk.Button(
    now_playing_frame,
    text="Clear",
    command=clear_now_playing,
    bg="#e74c3c",
    fg="white",
    font=("Arial", 10),
    padx=10
)
clear_button.pack(pady=5)

# Status bar
status_label = tk.Label(
    root,
    text="Double-click a song to play",
    font=("Arial", 10),
    bg="#ecf0f1",
    fg="#7f8c8d",
    relief="sunken",
    anchor="w",
    padx=10
)
status_label.pack(side="bottom", fill="x")

root.mainloop()