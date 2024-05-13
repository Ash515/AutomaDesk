import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
import re

# Function to organize files based on rules
def organize_files(source_dir, rules):
    for filename in os.listdir(source_dir):
        src_path = os.path.join(source_dir, filename)
        if os.path.isfile(src_path):
            file_ext = filename.split('.')[-1]
            if file_ext in rules:
                dest_dir = rules[file_ext]
                dest_path = os.path.join(dest_dir, filename)
                shutil.move(src_path, dest_path)
    messagebox.showinfo("Success", "Files organized successfully!")

# Function to save a rule to SQLite database
def save_rule_to_db(extension, destination):
    try:
        conn = sqlite3.connect('file_organizer.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT OR REPLACE INTO file_rules (extension, destination)
                          VALUES (?, ?)''', (extension, destination))
        conn.commit()
        messagebox.showinfo("Success", "Rule saved successfully!")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error saving rule to database: {e}")
    finally:
        conn.close()

# Function to delete a rule from SQLite database
def delete_rule_from_db(extension):
    try:
        conn = sqlite3.connect('file_organizer.db')
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM file_rules WHERE extension=?''', (extension,))
        conn.commit()
        messagebox.showinfo("Success", "Rule deleted successfully!")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error deleting rule from database: {e}")
    finally:
        conn.close()

# Function to load rules from SQLite database
def load_rules_from_db():
    rules = {}
    try:
        conn = sqlite3.connect('file_organizer.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS file_rules
                          (extension TEXT PRIMARY KEY, destination TEXT)''')
        cursor.execute('SELECT * FROM file_rules')
        rows = cursor.fetchall()
        rules = {row[0]: row[1] for row in rows}
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error loading rules from database: {e}")
    finally:
        conn.close()
    return rules

# Function to rename files based on user-defined pattern
def rename_files(source_dir, pattern, file_name):
    src_path = os.path.join(source_dir, file_name)
    if os.path.isfile(src_path):
        new_name = re.sub(r'{\w+}', lambda x: file_name.split('.')[0], pattern)
        new_path = os.path.join(source_dir, new_name)
        os.rename(src_path, new_path)
        messagebox.showinfo("Success", "File renamed successfully!")
    else:
        messagebox.showerror("Error", "File not found.")

# Function to handle browse button click event
def browse_button():
    folder_path = filedialog.askdirectory()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, folder_path)

# Function to handle save button click event
def save_button():
    extension = entry_ext.get().strip().lower()
    dest_folder = entry_dest.get().strip()
    if not extension or not dest_folder:
        messagebox.showerror("Error", "Please enter both extension and destination.")
        return
    save_rule_to_db(extension, dest_folder)
    update_rules_list()

# Function to handle delete button click event
def delete_button():
    extension = entry_ext.get().strip().lower()
    if not extension:
        messagebox.showerror("Error", "Please enter an extension to delete.")
        return
    if messagebox.askyesno("Delete Rule", f"Are you sure you want to delete the rule for '{extension}'?"):
        delete_rule_from_db(extension)
        update_rules_list()

# Function to update the rules list displayed in the GUI
def update_rules_list():
    rules = load_rules_from_db()
    listbox_rules.delete(0, tk.END)
    for extension, destination in rules.items():
        listbox_rules.insert(tk.END, f"{extension}: {destination}")

# Function to handle organize button click event
def organize_button():
    source_dir = entry_path.get()
    if not os.path.isdir(source_dir):
        messagebox.showerror("Error", "Please select a valid source directory.")
        return
    rules = load_rules_from_db()
    if not rules:
        messagebox.showerror("Error", "No rules found. Please add rules first.")
        return
    organize_files(source_dir, rules)

# Function to handle rename button click event
def rename_button1():
    # Get the selected file and the new filename
    selected_file = file_var.get()
    new_filename = new_filename_entry.get()

    if not selected_file:
        messagebox.showerror("Error", "Please select a file.")
        return

    if not new_filename:
        messagebox.showerror("Error", "Please enter a new filename.")
        return

    try:
        # Rename the file
        os.rename(selected_file, os.path.join(os.path.dirname(selected_file), new_filename))
        messagebox.showinfo("Success", "File renamed successfully.")
        file_var.set("")
        new_filename_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
def browse_file():
    # Open file dialog to select a file
    file_path = filedialog.askopenfilename()
    if file_path:
        file_var.set(file_path)
# Function to handle search button click event
def search_button():
    search_term = entry_search.get().strip()
    if not search_term:
        messagebox.showerror("Error", "Please enter a search term.")
        return
    source_dir = entry_path.get()
    if not os.path.isdir(source_dir):
        messagebox.showerror("Error", "Please select a valid source directory.")
        return
    files_found = []
    for filename in os.listdir(source_dir):
        if search_term in filename:
            files_found.append(filename)
    if files_found:
        messagebox.showinfo("Search Results", f"Files found: {', '.join(files_found)}")
    else:
        messagebox.showinfo("Search Results", "No files found.")

# Initialize Tkinter window
window = tk.Tk()
window.title("File Organizer")

# Define GUI elements
label_path = tk.Label(window, text="Source Directory:")
label_path.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry_path = tk.Entry(window, width=50)
entry_path.grid(row=0, column=1, padx=5, pady=5)

button_browse = tk.Button(window, text="Browse", command=browse_button)
button_browse.grid(row=0, column=2, padx=5, pady=5)

label_ext = tk.Label(window, text="File Extension:")
label_ext.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_ext = tk.Entry(window, width=10)
entry_ext.grid(row=1, column=1, padx=5, pady=5)

label_dest = tk.Label(window, text="Destination Folder:")
label_dest.grid(row=1, column=2, padx=5, pady=5, sticky="w")
entry_dest = tk.Entry(window, width=50)
entry_dest.grid(row=1, column=3, padx=5, pady=5)

button_save = tk.Button(window, text="Save Rule", command=save_button)
button_save.grid(row=1, column=4, padx=5, pady=5)

button_delete = tk.Button(window, text="Delete Rule", command=delete_button)
button_delete.grid(row=1, column=5, padx=5, pady=5)

label_rules = tk.Label(window, text="Current Rules:")
label_rules.grid(row=2, column=0, padx=5, pady=5, sticky="w")
listbox_rules = tk.Listbox(window, width=60, height=10)
listbox_rules.grid(row=3, column=0, columnspan=5, padx=5, pady=5, sticky="w")
update_rules_list()



button_organize = tk.Button(window, text="Organize Files", command=organize_button)
button_organize.grid(row=10, column=1, columnspan=3, padx=5, pady=5)



file_label = tk.Label(window, text="File:")
file_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

file_var = tk.StringVar()
file_entry = tk.Entry(window, textvariable=file_var, state='readonly', width=40)
file_entry.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Browse button
browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

# New filename label and entry
new_filename_label = tk.Label(window, text="New Filename:")
new_filename_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

new_filename_entry = tk.Entry(window, width=40)
new_filename_entry.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

# Rename button
rename_button = tk.Button(window, text="Rename", command=rename_button1)
rename_button.grid(row=6, column=1, columnspan=3, padx=5, pady=5)

# Start the Tkinter event loop
window.mainloop()

