import tkinter as tk
from tkinter import filedialog
import os

# Assuming classify_genre is the function that uses your model
from your_model import classify_genre  

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        label_file_explorer.configure(text="File Opened: " + file_path)
        genre = classify_genre(file_path)
        label_genre.configure(text="Predicted Genre: " + genre)

# Create the root window
window = tk.Tk()
window.title('Music Genre Classification')

# Set window size
window.geometry("500x250")

# File explorer label
label_file_explorer = tk.Label(window, text="Select an Audio File", width=100, height=4, fg="blue")
label_file_explorer.pack()

# Genre label
label_genre = tk.Label(window, text="Genre: ", width=100, height=4, fg="blue")
label_genre.pack()

# Button to browse files
button_explore = tk.Button(window, text="Browse Files", command=open_file)
button_explore.pack()

# Close button
button_exit = tk.Button(window, text="Exit", command=exit)
button_exit.pack()

# Run the GUI
window.mainloop()
