import tkinter as tk
from tkinter import messagebox
import winshell
import win32con

def get_recycle_bin_files():
    files = list(winshell.recycle_bin())
    return files

def delete_recycle_bin_files():
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

def check_recycle_bin_empty():
    files = get_recycle_bin_files()
    if not files:
        messagebox.showinfo("Recycle Bin Empty", "The Recycle Bin is empty.")
        return True
    return False

def main():
    root = tk.Tk()
    root.title("Recycle Bin Manager")
    root.minsize(300,100)
    
    if check_recycle_bin_empty():
        root.destroy()  
        return
    
    files = get_recycle_bin_files()
    file_count = len(files)
    
    label = tk.Label(root, text=f"Number of files in Recycle Bin: {file_count}")
    label.pack(pady=10)
    
    def on_delete():
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete all files in the Recycle Bin?"):
            delete_recycle_bin_files()
            messagebox.showinfo("Success", "All Recycle Bin files deleted successfully")
            root.quit()
    
    delete_button = tk.Button(root, text="Delete All Files", command=on_delete)
    delete_button.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
