import os
import shutil
import time
import stat
import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo

root = tk.Tk(className="flashapp")

root.geometry("900x600")
root.resizable(False, False)

title = tk.Label(text="Pico-Ducky creator")

l1 = tk.Label(text="Select the folder where you cloned the repo")
l2 = tk.Label(text="Select the location of the pico")

path1 = tk.Entry()
path2 = tk.Entry()

#def repo_select():
#    x = filedialog.askdirectory()
#    path1.insert(0, x)

#def pico_location():
#    y = filedialog.askdirectory()
#    path2.insert(0, y)

#constructing paths

base_path = path1.get()
pico_nuke = path2.get()
print(base_path)

nuke = base_path+'/flash_nuke.uf2'
circuit_python = base_path+'/circuit_python.uf2'
local_lib = base_path+'/lib'
asyncio = base_path+'/lib_aux/asyncio//'
wsgi = base_path+'/lib_aux/adafruit_wsgi//'
hid = base_path+'/lib_aux/adafruit_hid//'
res = base_path+'/res//'

#nuke the pico and install circuitpython
def nuke_fun():

    shutil.copy2(nuke, pico_nuke)
    time.sleep(10)
    nuked = askyesno(title="Sure?", message="Pico has been nuked, continue?")
    if nuked:
        shutil.copy2(circuit_python, pico_nuke)
        time.sleep(10)
    else:
        root.destroy()
    done = showinfo(title="Info", message="Done, you can flash now")

def flash():

    root2 = tk.Tk()
    root2.geometry("400x200")
    root2.resizable(False, False)
    l3 = tk.Label(roo2, text="Select the pico path again (After installing circuitpython the path might change)")
    def pico_location2():
        pico = filedialog.askdirectory()
        time.sleep(3)
        root2.destroy()
    select_pico = tk.Button(root2, text="Select", command=pico_location)
    l3.pack()
    root2.mainloop
    time.sleep(3)

#moving libraries from the repo to the pico
    pico_lib = pico+'/lib'
    shutil.rmtree(pico_lib)
    time.sleep(10)
    shutil.move(local_lib, pico)


 #re-creating another lib in the repo (because the original folder was moved to the pico) and re-creating it's subfolders
    os.mkdir(base_path+'/lib')
    time.sleep(10)
    os.mkdir(base_path+'/lib/asyncio')
    os.mkdir(base_path+'/lib/adafruit_wsgi')
    os.mkdir(base_path+'/lib/adafruit_hid')
    time.sleep(10)

#copying everything from the aux lib in the new lib
#(This process its needed because shutil can't copy files to the pico, so we use an auxiliary lib in the repo, 
#from whom we copy the files to the new lib so we still have everything for multiple uses)
    for file_name in os.listdir(asyncio):
        source = asyncio + file_name
        destination = base_path+'/lib/asyncio//' + file_name
        if os.path.isfile(source):
            shutil.copy2(source, destination)

    for file_name in os.listdir(wsgi):
        source = wsgi + file_name
        destination = base_path+'/lib/adafruit_wsgi//' + file_name
        if os.path.isfile(source):
            shutil.copy2(source, destination)

    for file_name in os.listdir(hid):
        source = hid + file_name
        destination = base_path+'/lib/adafruit_hid//' + file_name
        if os.path.isfile(source):
            shutil.copy2(source, destination)

    shutil.copy2(base_path+'/lib_aux/adafruit_debouncer.mpy', base_path+'/lib')
    shutil.copy2(base_path+'/lib_aux/adafruit_ticks.mpy', base_path+'/lib')

#copying the last files to the pico
    os.remove(pico+'code.py')
    for file_name in os.listdir(res):
        source = res + file_name
        destination = pico+'//' + file_name
        if os.path.isfile(source):
            shutil.copy2(source, destination)

#select_base_path = tk.Button(text="Select", command=repo_select)
#select_pico_nuke = tk.Button(text="Select", command=pico_location)
format_pico  = tk.Button(text="Nuke", command=nuke_fun)
flash_button = tk.Button(text="Flash", command=flash)

title.pack()
l1.place(x=30, y=120)
#select_base_path.place(x=30, y=150)
path1.place(x=80, y=153)
l2.place(x=30, y=220)
#select_pico_nuke.place(x=30, y=250)
path2.place(x=80, y=253)
format_pico.place(x=423, y=470)
flash_button.place(x=423, y=500)
root.mainloop()
