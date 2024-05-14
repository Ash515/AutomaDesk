# Import necessary modules
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
        messagebox.showerror("Error", "Please select a file to rename.")
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

# Set background color for the main window
window.configure(bg='light blue')

# Define GUI elements

# Frame for file organization
organize_frame = tk.Frame(window)
organize_frame.config(bg='light blue')  # Set background color
organize_frame.grid(row=7, column=0, columnspan=5, padx=5, pady=5, sticky="w")


# Define GUI elements
label_path = tk.Label(window, text="Source Directory:",bg="lightblue")
label_path.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry_path = tk.Entry(window, width=50)
entry_path.grid(row=0, column=1, padx=5, pady=5)

button_browse = tk.Button(window, text="Browse", command=browse_button,bg="lightgreen")
button_browse.grid(row=0, column=2, padx=5, pady=5)

# Frame for file rename functionality
rename_frame = tk.Frame(window,bg="lightblue")
rename_frame.grid(row=4, column=0, columnspan=5, padx=5, pady=5, sticky="w")

label_file = tk.Label(rename_frame, text="Selected File:",bg="lightblue")
label_file.grid(row=0, column=0, padx=5, pady=5, sticky="w")

file_var = tk.StringVar()
file_entry = tk.Entry(rename_frame, textvariable=file_var, state='readonly', width=40)
file_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=3)

browse_button = tk.Button(rename_frame, text="Browse", command=browse_file,bg="lightgreen")
browse_button.grid(row=0, column=4, padx=5, pady=5)

label_new_filename = tk.Label(rename_frame, text="New Filename:",bg="lightblue")
label_new_filename.grid(row=1, column=0, padx=5, pady=5, sticky="w")

new_filename_entry = tk.Entry(rename_frame, width=40)
new_filename_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=3)

rename_button = tk.Button(rename_frame, text="Rename", command=rename_button1,bg="lightgreen")
rename_button.grid(row=1, column=4, padx=5, pady=5)

# Frame for search functionality
search_frame = tk.Frame(window,bg="lightblue")
search_frame.grid(row=5, column=0, columnspan=5, padx=5, pady=5,sticky="w")

label_search = tk.Label(search_frame, text="Search Files:",bg="lightblue") 
label_search.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry_search = tk.Entry(search_frame, width=50) 
entry_search.grid(row=0, column=1, padx=5, pady=5, columnspan=3)

search_button = tk.Button(search_frame, text="Search", command=search_button,bg="lightgreen") 
search_button.grid(row=0, column=4, padx=5, pady=5)

rules_frame = tk.Frame(window,bg="lightblue") 
rules_frame.grid(row=6, column=0, columnspan=5, padx=5, pady=5, sticky="w")

label_ext = tk.Label(rules_frame, text="File Extension:",bg="lightblue") 
label_ext.grid(row=0, column=0, padx=5, pady=5, sticky="w") 
entry_ext = tk.Entry(rules_frame, width=10) 
entry_ext.grid(row=0, column=1, padx=5, pady=5)

label_dest = tk.Label(rules_frame, text="Destination Folder:",bg="lightblue") 
label_dest.grid(row=0, column=2, padx=5, pady=5, sticky="w") 
entry_dest = tk.Entry(rules_frame, width=50) 
entry_dest.grid(row=0, column=3, padx=5, pady=5, columnspan=2)

save_button = tk.Button(rules_frame, text="Save Rule", command=save_button,bg="lightgreen") 
save_button.grid(row=1, column=0, padx=5, pady=5)

delete_button = tk.Button(rules_frame, text="Delete Rule", command=delete_button,bg="lightgreen") 
delete_button.grid(row=1, column=1, padx=5, pady=5)

label_rules = tk.Label(rules_frame, text="Current Rules:",bg="lightblue") 
label_rules.grid(row=2, column=0, padx=5, pady=5, sticky="w") 
listbox_rules = tk.Listbox(rules_frame, width=60, height=10) 
listbox_rules.grid(row=3, column=0, columnspan=5, padx=5, pady=5, sticky="w")

update_rules_list()

organize_frame = tk.Frame(window,bg="lightblue") 
organize_frame.grid(row=7, column=0, columnspan=5, padx=5, pady=5, sticky="w")

label_organize = tk.Label(organize_frame, text="Organize Files:",bg="lightblue") 
label_organize.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry_path = tk.Entry(organize_frame, width=50) 
entry_path.grid(row=0, column=1, padx=5, pady=5, columnspan=3)

browse_button = tk.Button(organize_frame, text="Browse", command=browse_button,bg="lightgreen") 
browse_button.grid(row=0, column=4, padx=5, pady=5)

organize_button = tk.Button(organize_frame, text="Organize Files", command=organize_button,bg="lightgreen") 
organize_button.grid(row=1, column=0, padx=5, pady=5, columnspan=5)

window.mainloop()
