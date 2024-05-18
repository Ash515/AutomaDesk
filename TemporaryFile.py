import os
import tempfile
import tkinter as tk
from tkinter import messagebox

def get_temp_files():
    temp_dir = tempfile.gettempdir()
    result = []
    for f in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, f)
        if os.path.isfile(file_path):
            result.append(file_path)
    return result

def delete_temp_files():
    temp_files = get_temp_files()
    for file_path in temp_files:
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")

def check_temp_files_empty():
    temp_files = get_temp_files()
    if not temp_files:
        messagebox.showinfo("Temporary Files", "The temporary files folder is empty.")
        return True
    return False
 
def main():
    root = tk.Tk()
    root.title("Temporary Files Cleaner")
    root.minsize(300, 100)

    if check_temp_files_empty():
        root.destroy()  
        return

    temp_files = get_temp_files()
    file_count = len(temp_files)
    
    label = tk.Label(root, text=f"Number of temporary files: {file_count}")
    label.pack(pady=10)

    def on_delete():
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete all temporary files?"):
            delete_temp_files()
            messagebox.showinfo("Success", "All temporary files deleted successfully")
            root.quit()

    delete_button = tk.Button(root, text="Delete All Files", command=on_delete)
    delete_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
