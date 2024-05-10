import os
import tkinter as tk
from tkinter import filedialog

def organize_files():
    # Get the selected directory
    directory = filedialog.askdirectory()

    # Define your rules for organizing files
    rules = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Music': ['.mp3', '.wav'],
    }

    # Organize files based on the rules
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = os.path.splitext(filename)[1]
            for folder, extensions in rules.items():
                if file_extension.lower() in extensions:
                    folder_path = os.path.join(directory, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    os.rename(
                        os.path.join(directory, filename),
                        os.path.join(folder_path, filename)
                    )

    # Show a message box when the organization is complete
    tk.messagebox.showinfo('File Organizer', 'Files organized successfully!')

# Create the main window
window = tk.Tk()

# Add a button to trigger file organization
organize_button = tk.Button(window, text='Organize Files', command=organize_files)
organize_button.pack()

# Start the main event loop
window.mainloop()
