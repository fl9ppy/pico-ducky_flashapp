import os
import shutil
import time
import stat



#constructing paths
base_path = input("Path to repo: ")
pico_nuke = input("Path to pico: ")
nuke = base_path+'/flash_nuke.uf2'
circuit_python = base_path+'/circuit_python.uf2'
local_lib = base_path+'/lib'
asyncio = base_path+'/lib_aux/asyncio//'
wsgi = base_path+'/lib_aux/adafruit_wsgi//'
hid = base_path+'/lib_aux/adafruit_hid//'

#nuke the pico and install circuitpython
shutil.copy2(nuke, pico_nuke)
time.sleep(10)
next = input("continue? y/n: ")
if next == "y" or next == "Y":
    shutil.copy2(circuit_python, pico_nuke)
    time.sleep(10)
else:
    exit()

#moving libraries from the repo to the pico
pico = input("Path to pico (After nuking it can change): ")
pico_lib = pico+'/lib'
shutil.rmtree(pico_lib)
time.sleep(10)
shutil.move(local_lib, pico)
shutil.copy2(base_path+'/lib_aux/adafruit_debouncer.mpy', base_path+'/lib')
shutil.copy2(base_path+'/lib_aux/adafruit_ticks.mpy', base_path+'/lib')

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








print("DONE")

    


