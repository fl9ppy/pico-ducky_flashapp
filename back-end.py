import os
import shutil
import time
import stat

base_path = input("Path to repo: ")

pico_nuke = input("Path to pico: ")
nuke = base_path+'/flash_nuke.uf2'
circuit_python = base_path+'/circuit_python.uf2'
local_lib = base_path+'/lib'
asyncio = base_path+'/lib_aux/asyncio//'
wsgi = base_path+'/lib_aux/adafruit_wsgi//'
hid = base_path+'/lib_aux/adafruit_hid//'


shutil.copy2(nuke, pico_nuke)
time.sleep(10)
next = input("continue? y/n: ")
if next == "y":
    shutil.copy2(circuit_python, pico_nuke)
    time.sleep(10)
pico = input("Path to pico (After nuking it can change): ")
pico_lib = pico+'/lib'
shutil.rmtree(pico_lib)
time.sleep(10)
shutil.move(local_lib, pico)
os.mkdir(base_path+'/lib')
time.sleep(10)
os.mkdir(base_path+'/lib/asyncio')
os.mkdir(base_path+'/lib/adafruit_wsgi')
os.mkdir(base_path+'/lib/adafruit_hid')
time.sleep(10)

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

print("DONE")

    


