import os
import shutil
import time
import stat

pico = 'E:/'
nuke = 'C:/Users/adica/Documents/GitHub/pico-ducky_flashapp/flash_nuke.uf2'
circuit_python = 'C:/Users/adica/Documents/GitHub/pico-ducky_flashapp/circuit_python.uf2'
local_lib = 'C:/Users/adica/Documents/GitHub/pico-ducky_flashapp/lib'
pico_lib = 'F:/lib'

shutil.copy2(nuke, pico)
time.sleep(10)
shutil.copy2(circuit_python, pico)
pico = 'F:/'
time.sleep(10)
shutil.rmtree(pico_lib)
shutil.copytree(local_lib, pico)