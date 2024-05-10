import os
import sqlite3
from tkinter import filedialog, Tk, Label, Entry, Button, Listbox, StringVar, messagebox

# Set up SQLite connection
conn = sqlite3.connect('automa.db')
c = conn.cursor()

# Create table for rules if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS rules
             (name text, extensions text, destination text)''')

def add_rule(name, extensions, destination):
    c.execute("INSERT INTO rules VALUES (?,?,?)", (name, extensions, destination))
    conn.commit()

def delete_rule(name):
    c.execute("DELETE FROM rules WHERE name=?", (name,))
    conn.commit()

def get_rules():
    c.execute("SELECT * FROM rules")
    return c.fetchall()

def organize_files(directory):
    # Get rules from the database
    rules = {name: (extensions.split(','), destination) for name, extensions, destination in get_rules()}

    # Organize files based on the rules
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = os.path.splitext(filename)[1]
            for rule, (extensions, destination) in rules.items():
                if file_extension in extensions:
                    # Move file to the appropriate folder
                    os.rename(os.path.join(directory, filename), os.path.join(directory, destination, filename))

# Initialize Tkinter
root = Tk()
root.title("File Organizer")

# Rule name entry
Label(root, text="Rule name").grid(row=0)
rule_name = StringVar()
Entry(root, textvariable=rule_name).grid(row=0, column=1)

# Extensions entry
Label(root, text="Extensions").grid(row=1)
extensions = StringVar()
Entry(root, textvariable=extensions).grid(row=1, column=1)

# Destination entry
Label(root, text="Destination").grid(row=2)
destination = StringVar()
Entry(root, textvariable=destination).grid(row=2, column=1)

# Rule list
Label(root, text="Rules").grid(row=4)
rule_list = Listbox(root)
rule_list.grid(row=4, column=1)

def update_rule_list():
    # Clear the listbox
    rule_list.delete(0, 'end')

    # Add the rules to the listbox
    for name, extensions, destination in get_rules():
        rule_list.insert('end', f"{name}: {extensions} -> {destination}")

## Add rule button
Button(root, text="Add rule", command=lambda: (add_rule(rule_name.get(), extensions.get(), destination.get()), update_rule_list()), bg='light blue').grid(row=3, column=0)

# Delete rule button
Button(root, text="Delete rule", command=lambda: (delete_rule(rule_name.get()), update_rule_list()), bg='light blue').grid(row=3, column=1)

# Organize files button
Button(root, text="Organize files", command=lambda: organize_files(filedialog.askdirectory()), bg='light blue').grid(row=5)
update_rule_list()

root.mainloop()


