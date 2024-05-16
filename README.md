

# AutomaDesk 📂✨
 
AutomaDesk is a desktop application that helps you organize files and folders based on predefined rules. This tool can save you time and effort spent on manually maintaining a clean and organized desktop.

## Features 🚀

 - Organize Files: Automatically move files to specified    directories based on their extensions.
 - Add/Remove Rules: Save and delete organization rules specifying which file types go to which directories.
 - Rename Files: Rename files using user-defined patterns.
 - Search Files: Search for files containing a specific term within the selected directory.

## Getting Started 🏁
### Prerequisites 📋
Ensure you have the following installed:

- Python 3.x
- Tkinter (included with most Python installations)
- SQLite (included with Python's sqlite3 module)

### Installation 🛠️
1). Clone the repository:

sh
Copy code
git clone https://github.com/your-username/automadesk.git
cd automadesk

2). Run the application:

sh
Copy code
python automadesk.py


## Usage 📚
1). Select Source Directory:

 - Click on the "Browse" button next to the "Source Directory" field to select the directory containing the files you want to organize.
2). Add a Rule:

 - Enter the file extension (e.g., jpg, pdf) in the "File Extension" field.
 - Enter the destination folder where files of this type should be moved in the "Destination Folder" field.
 - Click the "Save Rule" button to save the rule to the database.
3).Delete a Rule:

 - Enter the file extension of the rule you want to delete in the "File Extension" field.
 - Click the "Delete Rule" button to remove the rule from the database.

4).Organize Files:

 - Once you have added the necessary rules, click the "Organize Files" button to move files according to the defined rules.

5).Rename Files:

 - Click the "Browse" button to select a file you want to rename.
 - Enter the new filename in the "New Filename" field.
 - Click the "Rename" button to rename the file.

6) Search Files:

 - Enter the search term in the "Search" field.
 - Click the "Search" button to find files containing the search term in the selected directory.

## Database Structure 🗄️
The application uses an SQLite database (file_organizer.db) to store file organization rules. The database contains a single table file_rules with the following structure:

 - extension: The file extension (e.g., jpg, pdf).
 - destination: The directory where files with the specified extension should be moved.

## Code Overview 📝
 - organize_files: Function to organize files based on the rules from the database.
 - save_rule_to_db: Function to save a file organization rule to the SQLite database.
 - delete_rule_from_db: Function to delete a file organization rule from the SQLite database.
 - load_rules_from_db: Function to load file organization rules from the SQLite database.
 - rename_files: Function to rename files based on a user-defined pattern.
 -browse_button: Function to handle the browse button click event for selecting a directory.
 -save_button: Function to handle the save button click event for saving a rule.
 - delete_button: Function to handle the delete button click event for deleting a rule.
 - update_rules_list: Function to update the rules list displayed in the GUI.
 - organize_button: Function to handle the organize button click event for organizing files.
 - rename_button1: Function to handle the rename button click event for renaming a file.
 - browse_file: Function to handle the browse button click event for selecting a file.
 - search_button: Function to handle the search button click event for searching files.

## License 📄
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact Information 📬
For more information or if you have any questions, feel free to reach out:

[Ashwin Kumar R]https://www.linkedin.com/in/ashwinkumarramasamy/

Thank you for using AutomaDesk! 🎉

## Tech Stacks
- Python - Tkinter
- SQlite

## Project Admin
- Ashwin Kumar R

## Developer(s)
- Ashwin Kumar R

## Communication Server
https://discord.gg/XsYcNdFm46
