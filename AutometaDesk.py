import os
import shutil
import sqlite3
import tkinter as tk
from tkinter import filedialog, messagebox

#Defining class FileOrganiserApp
class AutometaDesk:
    def __init__(self, master):
        self.master = master
        self.master.title("AutometaDesk")
        self.master.geometry("400x200")

        self.label = tk.Label(master, text="Select directory to organize:")
        self.label.pack()

        self.select_button = tk.Button(master, text="Select Directory", command=self.select_directory)
        self.select_button.pack()

    def select_directory(self):
        self.directory = filedialog.askdirectory()
        if self.directory:
            self.organize_files()

    def organize_files(self):
        # Connect to the SQLite database
        conn = sqlite3.connect("AutometaDesk.db")
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS rules
                          (extension TEXT PRIMARY KEY, folder TEXT)''')

        # Insert some sample rules
        cursor.execute("INSERT OR IGNORE INTO rules (extension, folder) VALUES ('.txt', 'TextFiles')")
        cursor.execute("INSERT OR IGNORE INTO rules (extension, folder) VALUES ('.pdf', 'PDFs')")

        # Fetch rules from the database
        cursor.execute("SELECT * FROM rules")
        rules = cursor.fetchall()

        # Create folders based on rules
        for rule in rules:
            folder_path = os.path.join(self.directory, rule[1])
            os.makedirs(folder_path, exist_ok=True)

        # Organize files based on rules
        for file_name in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory, file_name)):
                file_extension = os.path.splitext(file_name)[1]
                for rule in rules:
                    if rule[0] == file_extension:
                        source = os.path.join(self.directory, file_name)
                        destination = os.path.join(self.directory, rule[1], file_name)
                        shutil.move(source, destination)
                        break

        conn.commit()
        conn.close()

        messagebox.showinfo("AutometaDesk", "Files organized successfully!")

def main():
    root = tk.Tk()
    app = AutometaDesk(root)
    root.mainloop()

if __name__ == "__main__":
    main()
