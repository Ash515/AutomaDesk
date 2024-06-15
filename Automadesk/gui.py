import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from organizer.organizer import organize_files
import os
from PIL import Image, ImageTk
import time

def select_folder():
    desktop_path = os.path.expanduser("~/Desktop")
    folder_path = filedialog.askdirectory(initialdir=desktop_path)
    if folder_path:
        progress_bar.pack()
        root.update_idletasks()
        root.after(100, organize_files_async, folder_path)
    else:
        status_label.config(text="No folder selected.", fg="red")

def organize_files_async(folder_path):
    try:
        progress_bar["maximum"] = 100
        for i in range(101):
            progress_bar["value"] = i
            root.update_idletasks()
            time.sleep(0.01)
        organize_files(folder_path)
        status_label.config(text="Files organized successfully!", fg="green")
    except Exception as e:
        status_label.config(text=f"Failed to organize files: {e}", fg="red")
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        progress_bar.pack_forget()
        root.update_idletasks()

root = tk.Tk()
root.title("Automadesk")

image_path = os.path.abspath("bg.jpeg")

bg_image = Image.open(image_path)
bg_image = bg_image.resize((600, 400))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

content_frame = tk.Frame(canvas, bg="")
content_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8)

title_label = tk.Label(content_frame, text="Organize Files on Desktop", font=("Helvetica", 20, "bold"))
title_label.pack(pady=20)

instructions_label = tk.Label(content_frame, text="Select a folder on your Desktop to organize your files:", font=("Helvetica", 12))
instructions_label.pack(pady=10)

select_button = tk.Button(content_frame, text="Select Folder", command=select_folder, font=("Helvetica", 14), bg="#4CAF50", fg="white", padx=20, pady=10)
select_button.pack(pady=20)

progress_bar = ttk.Progressbar(content_frame, orient='horizontal', mode='determinate', length=400)
progress_bar.pack_forget()

status_label = tk.Label(content_frame, text="", font=("Helvetica", 12))
status_label.pack(pady=10)

root.mainloop()