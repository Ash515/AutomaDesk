# AutomaDesk

AutomaDesk is a tool that organizes files and folders based on pre-defined rules. This can save time and effort spent on manually maintaining a clean desktop. It uses the Tkinter library to provide a graphical user interface (GUI) for selecting the directory to be organized.

## Tech Stacks

- Python - Tkinter
- SQLite
- CustomTkinter

## Developer(s)

- Ashwin Kumar R (Repo Creator)
- Aditya Tomar(@ascendantaditya)

## How it Works

The script creates a GUI window with a button labeled "Organize Files". When this button is clicked, it triggers the `organize_files` function which organizes the files in the selected directory based on their extensions.

The script categorizes files into 'Images', 'Documents', 'Videos', and 'Music' based on predefined rules. It creates these folders in the selected directory and moves the files into their respective folders. If a folder doesn't exist, the script creates it.

Once the organization is complete, a message box appears to inform you that the files have been organized successfully.

The main window for the GUI is created using `window = tk.Tk()`. A button to trigger file organization is added using `organize_button = tk.Button(window, text='Organize Files', command=organize_files)`. The button is then packed into the window using `organize_button.pack()`. The main event loop for the GUI is started using `window.mainloop()`.
