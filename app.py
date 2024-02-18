import os
import sys
import shutil
import time
import tkinter as tk
from tkinter import filedialog, messagebox
import ctypes

def run_as_admin():
    if sys.platform == 'win32':
        try:
            if not ctypes.windll.shell32.IsUserAnAdmin():
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
                sys.exit(0)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run as admin: {e}")
            sys.exit(1)

def flash_pico():
    
    # Retrieve input paths from GUI
    base_path = repo_path_entry.get()
    pico_root_path = pico_path_entry.get()

    # Construct necessary paths
    flash_nuke = os.path.join(base_path, 'flash_nuke.uf2')
    circuit_python = os.path.join(base_path, 'circuit_python.uf2')
    PicoBoard = os.path.join(base_path, 'PicoBoard')
    aux_folder = os.path.join(base_path, 'PicoBoard_Aux')
    pico_lib = os.path.join(pico_root_path, 'lib')

    # Copy flash_nuke file to the Pico
    shutil.copy2(flash_nuke, pico_root_path)
    time.sleep(10)
    next_step = messagebox.askyesno("Copy Successful", "Nuke file copied successfully. Continue?")
    if not next_step:
        return

    # Copy CircuitPython file to the Pico
    shutil.copy2(circuit_python, pico_root_path)
    time.sleep(10)
    next_step = messagebox.askyesno("Copy Successful", "CircuitPython copied successfully. Continue?")
    if not next_step:
        return

    def copy(src, dst):
        if os.path.isdir(dst):
            dst = os.path.join(dst, os.path.basename(src))
        shutil.copyfile(src, dst)

    # Copy files from PicoBoard to the Pico
    for file_name in os.listdir(PicoBoard):
        if file_name == 'lib':
            for file_name2 in os.listdir(os.path.join(PicoBoard, 'lib')):
                lib1 = os.path.join(PicoBoard, 'lib')
                lib2 = os.path.join(pico_root_path, 'lib')
                src = os.path.join(lib1, file_name2)
                dest = os.path.join(lib2, file_name2)
                shutil.move(src, dest)
            continue
        source = os.path.join(PicoBoard, file_name)
        destination = os.path.join(pico_root_path, file_name)
        shutil.move(source, destination)

    # Copy files from auxiliary folder back to the lib folder
    for file_name in os.listdir(aux_folder):
        if file_name == 'lib':
            for file_name2 in os.listdir(os.path.join(aux_folder, 'lib')):
                lib1 = os.path.join(aux_folder, 'lib')
                lib2 = os.path.join(PicoBoard, 'lib')
                if file_name2 == 'adafruit_hid':
                    for file_name3 in os.listdir(os.path.join(lib1, 'adafruit_hid')):
                        lib3 = os.path.join(lib1, 'adafruit_hid')
                        lib4 = os.path.join(lib2, 'adafruit_hid')
                        src2 = os.path.join(lib3, file_name3)
                        dest2 = os.path.join(lib4, file_name3)
                        os.makedirs(os.path.dirname(dest2), exist_ok=True)
                        shutil.copy2(src2, dest2)
                    continue
                src = os.path.join(lib1, file_name2)
                dest = os.path.join(lib2, file_name2)
                shutil.copy2(src, dest)
            continue
        source = os.path.join(aux_folder, file_name)
        destination = os.path.join(PicoBoard, file_name)
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
