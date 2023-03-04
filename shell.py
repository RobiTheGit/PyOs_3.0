#!/usr/bin/python3
# RobiTheGit/RobiWanKenobi
# PyOs 3 / PyShell
# Yeah there is a shebang
import re
import sys
import time
import colors
import os
import subprocess
import getpass
import datetime
import platform
from datetime import *
#============================================================#
user = getpass.getuser()
#============================================================#
if os.path.exists('user/'):
    pass
else:
   os.mkdir('user/')
   
if os.path.exists('touch user/.password/{user}password.pass'):
    correctpass = open(f'user/.password/{user}password.pass')
else:
   os.system(f'touch user/.password/{user}password.pass')
   correctpass = open(f'user/.password/{user}password.pass')
    
cpass = correctpass.read()
#============================================================#
home = os.getcwd()
currentdir = os.getcwd() + '/user'
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
RUN or EXEC - Run a program or run a command that is on your main system but not in PyOs
CLEAR or CLS - Clear The Screen
ROOT or SUDO or ROOT INIT or SUDO INIT - Toggle running things as root
NANO - run NANO text edtior
VIM - run VIM text editor
All commands have no arguments

'''
global today
today = datetime.now()
global rt
rt = False
global dsprt
dsprt = False
#============================================================#
os.system('clear') 
def login():
    if os.path.getsize(f'user/.password/{user}password.pass') == 0:
        print(f'''
Welcom to PyOs 3.0 {user}
Today is {today}
Check for updates at https://github.com/RobiTheGit/PyOs_3.0
''')
        main()
    subprocess.run('clear')
    print(f'{colors.green}Login for {colors.cyan}{user}{colors.white}')
    passw = getpass.getpass(f'{colors.yellow}Password:{colors.white} ', stream=None)
    if passw == cpass:
        os.chdir(home+'/user/')
        print(f'''
Welcom to PyOs 3.0 {user}
Today is {today}
Check for updates at https://github.com/RobiTheGit/PyOs_3.0
''')
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
    for x in os.listdir():
        if os.path.isdir(x):
            print(f'Directory: {x}, {os.path.getsize(x)}, Read: {os.R_OK}, Write: {os.W_OK}, Excecute: {os.X_OK}')
        elif os.path.isfile(x):
            print(f'File: {x}, {os.path.getsize(x)}, Read: {os.R_OK}, Write: {os.W_OK}, Excecute: {os.X_OK}')
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
        os.chdir(home + '/user')
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
#============================================================#
def CLRTST():
    print(colors.disptest)
#============================================================#
def NANO():
    file = input('File to open (leave blank to open a new file) ')
    os.system(f'nano {file}')
#============================================================#
def VIM():
    file = input('File to open (leave blank to open a new file) ')
    os.system(f'vim {file}')
#============================================================#
def ROOT():
    global rt
    global dsprt
    if rt == True:
        rt = False
        dsprt = False
    else:
        rt = True
        dsprt = True
#============================================================#
def main():
    global currentdir
    cd2 = currentdir
    if cd2 == os.getcwd():
        currentdir = ''
    cd2 = currentdir
    if dsprt == True:
        command = input(f"{colors.green}{user}[ROOT]@PyOs3:{colors.blue}{os.getcwd()}{currentdir}{colors.white}$ ")
    else:
        command = input(f"{colors.green}{user}@PyOs3:{colors.blue}{os.getcwd()}{currentdir}{colors.white}$ ")
#============================================================#
    if command.upper() == 'EXIT' or command.upper() == "QUIT":
        EXIT()
#============================================================#
    elif command.upper() == 'CLEAR' or command.upper() == "CLS":
        CLEAR()
#============================================================#
    elif command.upper() == "TOUCH" or command.upper() == "CREATE":
        TOUCH()
#============================================================#
    elif command.upper() == "MV" or command.upper() == "MOVE":
        MV()
#============================================================#
    elif command.upper() == "CP" or command.upper() == "COPY":
        CP()
#============================================================#
    elif command.upper() == "RM" or command.upper() == "REMOVE":
        RM()
#============================================================#
    elif command.upper() == "RUN" or command.upper() == "EXEC":
        RUN()
#============================================================#
    elif command.upper() == "CHDIR" or command.upper() == "CD":
        CHDIR()
#============================================================#
    elif command.upper() == "HELP" or command.upper() == "?" or command.upper() == "H":
        HELP()
#============================================================#
    elif command.upper() == "MKDIR" or command.upper() == "TOUCHDIR":
        MKDIR()
#============================================================#
    elif command.upper() == "RMDIR" or command.upper() == "DELDIR":
        RMDIR()
#============================================================#
    elif command.upper() == "DIR" or command.upper().startswith("LS"):
        DIR()
#============================================================#
    elif command.upper() == "ROOT" or command.upper().startswith("SUDO") or command.upper() == "ROOT INIT" or command.upper() == "SUDO INIT":
        ROOT()
#============================================================#
    elif command.upper() == "CLRTST" or command.upper() == "COLORTEST":
        CLRTST()
#============================================================#
    elif command.upper() == "NANO":
        NANO()
#============================================================#
    elif command.upper() == "VI" or command.upper() == "VIM":
        VIM()
#============================================================#
    else:
        print(f'{colors.red}COMMAND NOT FOUND OR NOT TYPED PROPERLY!{colors.white}')
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
