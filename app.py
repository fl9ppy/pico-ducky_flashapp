import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog

def flash_pico():
    # Retrieve input paths from GUI
    base_path = repo_path_entry.get()
    pico_nuke = pico_path_entry.get()

    # Construct other necessary paths
    nuke = os.path.join(base_path, 'flash_nuke.uf2')
    circuit_python = os.path.join(base_path, 'circuit_python.uf2')
    local_lib = os.path.join(base_path, 'lib')
    asyncio = os.path.join(base_path, 'lib_aux', 'asyncio')
    wsgi = os.path.join(base_path, 'lib_aux', 'adafruit_wsgi')
    hid = os.path.join(base_path, 'lib_aux', 'adafruit_hid')
    res = os.path.join(base_path, 'res')

    # Nuke the Pico and install CircuitPython
    shutil.copy2(nuke, pico_nuke)
    time.sleep(10)
    next_step = tk.messagebox.askyesno("Nuke Successful", "Pico nuked successfully. Continue with CircuitPython installation?")
    if next_step:
        shutil.copy2(circuit_python, pico_nuke)
        time.sleep(10)
    else:
        return

    # Move libraries from the repo to the Pico
    pico_lib = os.path.join(pico_nuke, 'lib')
    shutil.rmtree(pico_lib, ignore_errors=True)
    time.sleep(10)
    shutil.move(local_lib, pico_nuke)

    # Recreate library structure in the repo
    os.makedirs(os.path.join(base_path, 'lib', 'asyncio'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'lib', 'adafruit_wsgi'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'lib', 'adafruit_hid'), exist_ok=True)
    time.sleep(10)

    # Copy library files
    for lib_folder in [asyncio, wsgi, hid]:
        for file_name in os.listdir(lib_folder):
            source = os.path.join(lib_folder, file_name)
            if os.path.isfile(source):
                if 'asyncio' in lib_folder:
                    destination = os.path.join(base_path, 'lib', 'asyncio', file_name)
                elif 'adafruit_wsgi' in lib_folder:
                    destination = os.path.join(base_path, 'lib', 'adafruit_wsgi', file_name)
                elif 'adafruit_hid' in lib_folder:
                    destination = os.path.join(base_path, 'lib', 'adafruit_hid', file_name)
                shutil.copy2(source, destination)

    # Copy additional files to the Pico
    os.remove(os.path.join(pico_nuke, 'code.py'), None)
    for file_name in os.listdir(res):
        source = os.path.join(res, file_name)
        destination = os.path.join(pico_nuke, file_name)
        if os.path.isfile(source):
            shutil.copy2(source, destination)

    tk.messagebox.showinfo("Success", "Script executed successfully. Pico flash and library setup complete.")

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
