import os
import shutil
import time
import stat
import pyuac

base_path = 'D:/GitHub/pico-ducky_flashapp'

E = 'E:/'
F = 'F:/'
nuke = base_path+'/flash_nuke.uf2'
circuit_python = base_path+'/circuit_python.uf2'
local_lib = base_path+'/lib'
pico_lib = 'F:/lib'
asyncio = base_path+'/lib_aux/asyncio//'
wsgi = base_path+'/lib_aux/adafruit_wsgi//'
hid = base_path+'/lib_aux/adafruit_hid//'


shutil.copy2(nuke, E)
time.sleep(10)
shutil.copy2(circuit_python, E)
time.sleep(10)
shutil.rmtree(pico_lib)
time.sleep(10)
shutil.move(local_lib, F)
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
        print('Moved:', file_name)

for file_name in os.listdir(wsgi):
    source = wsgi + file_name
    destination = base_path+'/lib/adafruit_wsgi//' + file_name
    if os.path.isfile(source):
        shutil.copy2(source, destination)
        print('Moved:', file_name)

for file_name in os.listdir(hid):
    source = hid + file_name
    destination = base_path+'/lib/adafruit_hid//' + file_name
    if os.path.isfile(source):
        shutil.copy2(source, destination)
        print('Moved:', file_name)

shutil.copy2(base_path+'/lib_aux/adafruit_debouncer.mpy', base_path+'/lib')
shutil.copy2(base_path+'/lib_aux/adafruit_ticks.mpy', base_path+'/lib')

print("finally")

    


