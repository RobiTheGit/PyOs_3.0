#!/usr/bin/python3
# RobiTheGit/RobiWanKenobi  
# PyOs 3 / PyShell
# Yeah there si a shebang

import sys
import time
import colors
import os
import subprocess
import getpass
import datetime
import platform
from datetime import date
#============================================================#
user = getpass.getuser()
correctpass = open(f'user/.password/{user}password.pass')
cpass = correctpass.read()
#============================================================#
if os.path.exists('user/'):
    pass
else:
   os.mkdir('user/')
#============================================================#
home = os.getcwd()
currentdir = os.getcwd()
#============================================================#
global cmdlist
cmdlist = '''
Command List for now:

CHDIR or CD - Change the current working directory
DIR or LS - List files in the directory
HELP or ? or H - Get help for commands
MKDIR or TOUCHDIR - Make a new directory
RMDIR or DELDIR - Remove a directory
MV or MOVE - Move a file somewhere else
CP or COPY- Copy a file somewhere
TOUCH or CREATE - Make a New File
RM or REMOVE - Remove a file
EXIT or QUIT- Exit PYSHELL
RUN or EXEC - Run a program
CLEAR or CLS - Clear The Screen
ROOT or SUDO or ROOT INIT or SUDO INIT - Toggle running things as root
'''
global rt
rt = False
#============================================================#
today = date.today()
nyd = date(today.year, 12, 31)
timetilnyd = nyd - today
#============================================================#
os.system('clear') 
print(f'{colors.white}PYSHELL FOR USER "{user.upper()}"')
def login():
    if os.path.getsize(f'user/.password/{user}password.pass') == 0:
        main()   
    subprocess.run('clear')
    print(f'{colors.green}Login for {colors.cyan}{user}{colors.white}')
    passw = getpass.getpass(f'{colors.yellow}Password:{colors.white} ', stream=None)
    if passw == cpass:
        os.chdir(home+'/user/')
        subprocess.run('clear')
        try:
            main()
        except KeyboardInterrupt:
            try:
                print('')
                main()
            except KeyboardInterrupt:
                print('')
                main()
    else:
        print(f'{colors.red}INVALID PASSWORD{colors.white}')
        time.sleep(0.5)
        login()
#============================================================#
def DIR():
    path = os.getcwd()
    print(f"Files in {path}:\n")
    for x in os.scandir():
        print(f'{x}, Read: {os.R_OK}, Write: {os.W_OK}, Excecute: {os.X_OK}')
#============================================================#
def MKDIR():
    Dir = input('Directory Name? ')
    try:
        if rt == False:
            os.mkdir(Dir)
        else:
            os.system(f"sudo mkdir {Dir}")
    except PermissionError:
        print(f'{colors.red}Permission Denied{colors.white}')
    except:
        main() 
#============================================================#
def RMDIR():
    Dir = input('Directory Name? ')
    try:
        if rt == False:
            os.rmdir(Dir)
        else:
            os.system(f"sudo rmdir {Dir}")
    except PermissionError:
        print(f'{colors.red}Permission Denied{colors.white}')
    except:
        main()
#============================================================#
def CHDIR():
    cd = input('Directory to change to? ')
    currentdir = cd
    try:
        os.chdir(cd)
    except:
        os.chdir(home)
#============================================================#
def EXIT():
    sys.exit(0)
#============================================================#
def HELP():
    print(cmdlist)
#============================================================#
def MV():
    ogfile = input('File to move: ')
    newfile = input('output of move: ')
    try:
        if rt == False:
            os.system(f"mv {ogfile} {newfile}")
        else:
            os.system(f"sudo mv {ogfile} {newfile}")
    except:
        main()
#============================================================#
def CP():
    ogfile = input('File to copy: ')
    newfile = input('output of copy: ')
    try:
        if rt == False:
            os.system(f"cp {ogfile} {newfile}")
        else:
            os.system(f"sudo cp {ogfile} {newfile}")
    except:
        main()
#============================================================#
def TOUCH():
    name = input('File Name ')
    if rt == False:
        os.system(f"touch {name}")
    else:
        os.system(f"sudo touch {name}")
#============================================================#
def RM():
    name = input('File Name ')
    try:
        if rt == False:
            os.remove(name)
        else:
            os.system(f"sudo rm {name}")
    except:
        main()
#============================================================#
def RUN():
    app = input('Path to App: ')
    if rt == False:
        if app.endswith('.py'):
            subprocess.run(f'python3 {app}', shell=True)
        else:
            subprocess.run(f'{app}', shell=True)
    else:
        if app.endswith('.py'):
            subprocess.run(f'sudo python3 {app}', shell=True)
        else:
            subprocess.run(f'sudo {app}', shell=True)
#============================================================#
def CLEAR():
    os.system('clear')
def ROOT():
    global rt
    if rt == True:
        rt = False
    else:
        rt = True
#============================================================#
def main():
    command = input(f"pyshell-{colors.cyan}root={rt}&{colors.green}user={user}{colors.blue}@PyOs3{colors.cyan}~{os.getcwd()}{colors.white}: ")
    if command.upper() == 'EXIT' or command.upper() == "QUIT":
        EXIT()
    elif command.upper() == 'CLEAR' or command.upper() == "CLS":
        CLEAR()
    elif command.upper() == "TOUCH" or command.upper() == "CREATE":
        TOUCH()
    elif command.upper() == "MV" or command.upper() == "MOVE":
        MV()
    elif command.upper() == "CP" or command.upper() == "COPY":
        CP()
    elif command.upper() == "RM" or command.upper() == "REMOVE":
        RM()
    elif command.upper() == "RUN" or command.upper() == "EXEC":
        RUN()
    elif command.upper() == "CHDIR" or command.upper() == "CD":
        CHDIR()
    elif command.upper() == "HELP" or command.upper() == "?" or command.upper() == "H":
        HELP()
    elif command.upper() == "MKDIR" or command.upper() == "TOUCHDIR":
        MKDIR()
    elif command.upper() == "RMDIR" or command.upper() == "DELDIR":
        RMDIR()
    elif command.upper() == "DIR" or command.upper().startswith("LS"):
        DIR()
    elif command.upper() == "ROOT" or command.upper().startswith("SUDO") or command.upper() == "ROOT INIT" or command.upper() == "SUDO INIT":
        ROOT()
    else:
        print(f'{colors.red}COMMAND NOT FOUND OR NOT TYPED PROPERLY{colors.white}')
#============================================================#
    try:
       recurse()
    except KeyboardInterrupt:
        try:
            print('')
            recurse()
        except KeyboardInterrupt:
                print('')
                recurse()
#============================================================#
def recurse():
    try:
        main()
    except KeyboardInterrupt:
        try:
            print('')
            main()
        except KeyboardInterrupt:
            print('')
            main()
#============================================================#
if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    print('This program is incompatible with your operating system', platform.system(), platform.release())
else:
    login()
#============================================================#
