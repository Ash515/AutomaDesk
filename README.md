# AutomaDesk

A powerful tool to organize your files and folders based on pre-defined rules, saving you time and effort in maintaining a clean and efficient digital workspace.

## Key Features

### Flexible Rule Creation
Define rules to automatically move files based on extension (e.g., PDFs to a "Documents" folder, images to a "Pictures" folder).

### SQLite Database Integration
Store rules persistently for easy access and management.

### User-Friendly Interface
Interact with AutomaDesk through a visually appealing Tkinter GUI.

### Renaming Functionality
Rename files using customizable patterns for enhanced organization.

### Search Capability
Locate specific files within your designated source directory.

## Tech Stack

- Python (Core functionality)
- Tkinter (GUI development)
- SQLite (Database storage)

## Installation

### Prerequisites

Ensure you have Python 3 installed on your system. You can download it from [Python Official Website](https://www.python.org/downloads/windows/).

### Clone the Repository

Use Git to clone this repository to your local machine:

git clone https://github.com/your-username/AutomaDesk.git

## Usage

### Run AutomaDesk
Execute the main script (automadesk.py or similar) from your terminal.

### Source Directory
Specify the directory containing the files you want to organize.

### Rule Management
#### Creating Rules

1. Enter the file extension in the "File Extension" field (e.g., ".pdf").
2. Specify the destination folder in the "Destination Folder" field (e.g., "C:/Documents").
3. Click the "Save Rule" button to establish the rule.

### Viewing Rules

The "Current Rules" section displays the existing rules.

### Deleting Rules

1. Enter the extension of the rule you want to remove in the "File Extension" field.
2. Click the "Delete Rule" button to confirm removal.

### Organize Files
Once rules are defined, click the "Organize Files" button to activate file organization based on the established rules.

### Renaming Files
1. Click the "Browse" button next to the "File" field to select a file for renaming.
2. Enter the desired new filename in the "New Filename" field.
3. Click the "Rename" button to execute the renaming process.
Search Files
4. Type the search term for the files you want to locate in the "Search" field.
5. Click the "Search" button to initiate the search. Results will be displayed in a message box.

## Customization

The code provides a solid foundation. You can extend it to accommodate more complex rule-based organization, such as including subdirectories based on file content or creation date.

Consider implementing visual feedback (progress bars, confirmation messages) to enhance the user experience.

## Contributing

We welcome contributions to this project! Feel free to fork the repository, make your changes, and submit a pull request. We appreciate your interest in keeping AutomaDesk a valuable tool.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it under the terms of this license.

## Additional Notes

For advanced usage or troubleshooting, refer to the code comments and documentation within the project.

Consider creating a standalone executable using tools like PyInstaller to distribute AutomaDesk more easily (optional).

## Project Admin
- Ashwin Kumar R

## Developer(s)
- Ashwin Kumar R

## Communication Server
https://discord.gg/XsYcNdFm46