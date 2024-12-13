import os
import shutil
import requests
import tkinter as tk
from tkinter import Tk, Label, Button, Toplevel, Listbox, END, filedialog, messagebox, DoubleVar
from threading import Thread, Event
from queue import Queue

# Get the current directory
current_directory = os.getcwd()

def create_folders(directory, file_types):
    # Create folders if they don't exist
    for folder in set(file_types.values()):  # Use set() to avoid duplicate folder creation
        if not os.path.exists(os.path.join(directory, folder)):
            os.makedirs(os.path.join(directory, folder))

def move_file(directory, filename, file_types):
    # Get file extension
    file_ext = os.path.splitext(filename)[1].lower()

    # Check if file extension is in the dictionary
    if file_ext in file_types:
        # Move file to respective folder
        src_path = os.path.join(directory, filename)
        dest_folder = file_types[file_ext]
        dest_path = os.path.join(directory, dest_folder, filename)
        shutil.move(src_path, dest_path)
        return f"Moved {filename} to {dest_folder} folder."

def organize_files(directory, queue, stop_event, file_types):
    try:
        create_folders(directory, file_types)
        files = os.listdir(directory)
        total_files = len(files)
        messages = []

        # Iterate through files in directory
        for filename in files:
            if stop_event.is_set():
                break
            if os.path.isfile(os.path.join(directory, filename)):
                message = move_file(directory, filename, file_types)
                if message:
                    queue.put(message)
                    messages.append(message)

        return messages, total_files
    except Exception as e:
        queue.put(f"Error: {str(e)}")

def display_messages(messages):
    window = Tk()
    listbox = Listbox(window)
    listbox.pack()

    for message in messages:
        listbox.insert(END, f"• {message}")

    window.mainloop()

def stop_thread(window, thread, stop_event):
    stop_event.set()  # Signal the thread to stop
    window.destroy()

import customtkinter as ctk

def gui_organize_files(file_types):
    try:
        directory = filedialog.askdirectory()
        if not directory:
            messagebox.showinfo("No Directory", "No directory selected.")
            return

        window = ctk.CTk()  # Use CTk instead of Toplevel
        queue = Queue()
        messages = []  # Define the "messages" list

        stop_event = Event()
        thread = Thread(target=organize_files, args=(directory, queue, stop_event, file_types))
        thread.start()

        # Bind the stop_thread function to the window's close button
        window.protocol("WM_DELETE_WINDOW", lambda: stop_thread(window, thread, stop_event))

        total_files = len(os.listdir(directory))
        if total_files == 0:
            messagebox.showinfo("No Files", "No files available to organize.")
            return
        while thread.is_alive() or not queue.empty():
            window.update()
            while not queue.empty():
                message = queue.get()
                messages.append(message)

        window.destroy()

        # Check if any messages were added
        if not messages:
            messagebox.showinfo("No New Files", "No new files to organize.")
            return

        # display_messages(messages)
        messagebox.showinfo("Success", "Files organized successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Dictionary to map file extensions to folder names
file_types = {
    '.png': 'Images',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.gif': 'Images',
    '.pdf': 'Documents',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.txt': 'Documents',
    '.mp4': 'Videos',
    '.mov': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',
    '.ppt': 'Documents',
    '.pptx': 'Documents',
    '.zip': 'Compressed',
    '.py': 'Code',
    '.h': 'Code',
    '.cpp': 'Code',
    '.c': 'Code',
    '.csv': 'Data',
    # Add more file extensions and their corresponding folders as needed
}

# root = tk.Tk()
# organize_button = tk.Button(root, text="Organize Files", command=lambda: gui_organize_files(file_types))
# organize_button.pack()


import customtkinter as ctk
import tkinter as tk

root = tk.Tk()
root.geometry('300x200')  # Set the window size

organize_button = ctk.CTkButton(
    root, 
    text="Organize Files", 
    command=lambda: gui_organize_files(file_types),
    text_color="white",  # Set the text color
    bg_color="blue",  # Set the background color
    hover_color="darkblue",  # Set the color when the mouse hovers over the button
    corner_radius=10,  # Set the corner radius to make the button rounder
    width=200,  # Set the button width
    height=40  # Set the button height
)
organize_button.pack(pady=20)  # Add some padding around the button

root.mainloop()