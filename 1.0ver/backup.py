import os
import shutil
soucre = input("enter soucre folder name")
destation = input("enter destation folder")
soucre = soucre+"/"
destation = destation+"/"
listoffiles = os.listdir(soucre)
for file in listoffiles:
    shutil.copy((soucre+file),destation)    