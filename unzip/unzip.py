import os
import zipfile
with zipfile.ZipFile('launcher.zip') as file:
    file.extractall(pwd = bytes('123', 'utf-8'))
