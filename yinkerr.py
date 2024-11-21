import tkinter as tk
from tkinter import messagebox
import requests
import os
import subprocess
import sys
from packaging.version import Version

# Constants
VERSION="9.0.0.0"
API_URL = f"https://api.github.com/repos/TheFantome25/ISSS/releases/latest"

def get_latest_release_info():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TEAMS forSKINS")
        
        # Create the listbox (list view)
        self.listbox = tk.Listbox(root, width=40, height=10)
        self.listbox.pack(pady=10)
        
        # Create a frame to hold the buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        # Add Item button
        add_button = tk.Button(button_frame, text="Add Item", command=self.add_item)
        add_button.grid(row=0, column=0, padx=5)
        
        # Clear List button
        clear_button = tk.Button(button_frame, text="Clear List", command=self.clear_list)
        clear_button.grid(row=0, column=1, padx=5)

    def add_item(self):
        # Add an item to the listbox
        new_item = f"Item {self.listbox.size() + 1}"  # Example item name
        self.listbox.insert(tk.END, new_item)
        
    def clear_list(self):
        # Clear all items in the listbox
        if self.listbox.size() > 0:
            self.listbox.delete(0, tk.END)
        else:
            messagebox.showinfo("Info", "List is already empty.")

if __name__ == "__main__":
   
    release_info = get_latest_release_info()
    if release_info:
        latest_version = release_info["tag_name"]
        current_version = Version(VERSION)
        remote_version = Version(latest_version)
        if remote_version > current_version:
            # Assuming the first asset is what we want
            assets = release_info.get("assets", [])
            if assets:
                download_url = assets[0]["browser_download_url"]
                root = tk.Tk()
                root.withdraw()  # Hide the main tkinter window
                response = messagebox.askyesno("Update Available", "New version available. Do you want to close and update?")
                if response:
                    try:
                            # Start the updater with the specified arguments
                            subprocess.Popen(
                                ["updaterISSS.exe"],  # Arguments to the updater
                                shell=False,            # Don't use a shell to avoid unnecessary dependencies
                                close_fds=True,         # Close file descriptors to detach from the parent process
                                creationflags=subprocess.DETACHED_PROCESS if sys.platform == "win32" else 0  # Detach process on Windows
                            )
                            sys.exit()  # Close the main application
                    except Exception as e:
                        sys.exit(1)  # Exit with an error code                


    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
    

