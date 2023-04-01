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

#def main():
#        shutil.copy2(nuke, E)
#        time.sleep(10)
#        shutil.copy2(circuit_python, E)
#        time.sleep(10)
#        shutil.move(local_lib, F)
#        time.sleep(60)
#        input("Press enter to close the window. >")
#
#if __name__ == "__main__":
#    if not pyuac.isUserAdmin():
#        print("Re-launching as admin!")
#        pyuac.runAsAdmin()
#        main()
#    else:        
#        main()

shutil.copy2(nuke, E)
time.sleep(10)
shutil.copy2(circuit_python, E)
time.sleep(10)
shutil.rmtree(pico_lib)
time.sleep(10)
shutil.move(local_lib, F)
time.sleep(40)