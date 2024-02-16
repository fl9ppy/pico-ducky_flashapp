import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog, messagebox

def flash_pico():
    # Retrieve input paths from GUI
    base_path = repo_path_entry.get()
    pico_nuke = pico_path_entry.get()

    # Construct necessary paths
    circuit_python = os.path.join(base_path, 'circuitpython.uf2')

    # Copy CircuitPython file to the Pico
    shutil.copy2(circuit_python, pico_nuke)
    time.sleep(10)
    next_step = messagebox.askyesno("Copy Successful", "CircuitPython copied successfully. Continue with copying lib folder and .py files?")
    if not next_step:
        return

    # Copy lib folder to the Pico
    pico_lib = os.path.join(pico_nuke, 'lib')
    shutil.rmtree(pico_lib, ignore_errors=True)
    time.sleep(2)
    shutil.copytree(os.path.join(base_path, 'lib'), pico_lib)

    # Copy .py files to the Pico
    for file_name in os.listdir(base_path):
        if file_name.endswith('.py'):
            source = os.path.join(base_path, file_name)
            destination = os.path.join(pico_nuke, file_name)
            shutil.copy2(source, destination)

    messagebox.showinfo("Success", "Script executed successfully. Pico flash and file copy complete.")

# GUI setup
root = tk.Tk()
root.title("Pico Flasher")

# Labels
tk.Label(root, text="Repository Path:").grid(row=0, column=0, sticky="w")
tk.Label(root, text="Pico Path:").grid(row=1, column=0, sticky="w")

# Entry fields
repo_path_entry = tk.Entry(root, width=50)
repo_path_entry.grid(row=0, column=1, padx=5, pady=5)
pico_path_entry = tk.Entry(root, width=50)
pico_path_entry.grid(row=1, column=1, padx=5, pady=5)

# Browse buttons
def browse_repo_path():
    repo_path = filedialog.askdirectory()
    repo_path_entry.delete(0, tk.END)
    repo_path_entry.insert(0, repo_path)

def browse_pico_path():
    pico_path = filedialog.askdirectory()
    pico_path_entry.delete(0, tk.END)
    pico_path_entry.insert(0, pico_path)

tk.Button(root, text="Browse", command=browse_repo_path).grid(row=0, column=2, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_pico_path).grid(row=1, column=2, padx=5, pady=5)

# Run button
tk.Button(root, text="Flash Pico", command=flash_pico).grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
