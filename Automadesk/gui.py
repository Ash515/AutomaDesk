import tkinter as tk
import tkinter as tk
from tkinter import filedialog
from organizer.organizer import organize_files
import os

def select_folder():
    desktop_path = os.path.expanduser("~/Desktop")
    folder_path = filedialog.askdirectory(initialdir=desktop_path)
    if folder_path:
        organize_files(folder_path)
        status_label.config(text="Files organized successfully!")
    


root = tk.Tk()
root.title("Automadesk")


title_label = tk.Label(root, text="Organize Files on Desktop", font=("Helvetica", 16))
title_label.pack(pady=10)


select_button = tk.Button(root, text="Select Files on desktop", command=select_folder)
select_button.pack(pady=10)


status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=5)
root.geometry("800x600")


root.mainloop()

