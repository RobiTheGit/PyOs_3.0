#!/usr/bin/python3
#Hey look, a shebang, don't complain about me not having one
import sys
import time
import colors
import os
import subprocess
import getpass
import datetime
from datetime import date
correctpass = open('user/.password/password.pass')
cpass = correctpass.read()
if os.path.exists('user/'):
    pass
else:
   os.mkdir('user/')
home = os.getcwd()
global cmdlist
cmdlist = '''
Command List for now:

CHDIR or CD- Change the current working directory
DIR or LS- List files in the directory
HELP - Get help for commands
MKDIR - Make a new directory
RMDIR - Remove a directory
MV or MOVE - Move a file somewhere else
CP or COPY- Copy a file somewhere
TOUCH - Make a New File
RM or REMOVE - Remove a file
EXIT - Exit PYSHELL
RUN - Run a program
CLEAR - Clear The Screen
'''
today = date.today()
nyd = date(today.year, 12, 31)
timetilnyd = nyd - today
user = getpass.getuser()
os.system('clear') 
print(f'PYSHELL FOR USER "{user.upper()}"')
def login():
    if os.path.getsize('user/.password/password.pass') == 0:
        main()   
    subprocess.run('clear')
    print(f'Login for {user}')
    passw = getpass.getpass('Password: ', stream=None)
    if passw == cpass:
        os.chdir(home+'/user/')
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
        print(f'INVALID PASSWORD')
        time.sleep(0.5)
        login()
        
def DIR():
    path = os.getcwd()
    print(f"Files in {path}:\n")
    for x in os.scandir():
        print(f'{x}, Read: {os.R_OK}, Write: {os.W_OK}, Excecute: {os.X_OK}')
        
def MKDIR():
    Dir = input('Directory Name? ')
    os.mkdir(Dir)
    
def RMDIR():
    Dir = input('Directory Name? ')
    os.rmdir(Dir)
    
def CHDIR():
    cd = input('Directory to change to? ')
    try:
        os.chdir(cd)
    except:
        os.chdir(home)
def EXIT():
    sys.exit(0)

def HELP():
    print(cmdlist)

def MV():
    ogfile = input('File to move: ')
    newfile = input('output of move: ')
    os.system(f"mv {ogfile} {newfile}")

def CP():
    ogfile = input('File to copy: ')
    newfile = input('output of copy: ')
    os.system(f"cp {ogfile} {newfile}")

def TOUCH():
    name = input('File Name ')
    files = open(name, "x")

def RM():
    name = input('File Name ')
    os.remove(name)
def RUN():
    app = input('Path to App: ')
    if app.endswith('.py'):
        subprocess.run(f'python3 {app}', shell=True)
    else:
        subprocess.run(f'{app}', shell=True)
def CLEAR():
    os.system('clear')
    
def main():
    command = input(f"pyshell-{user}@PyOs3~{os.getcwd()}: ")
    if command.upper() == 'EXIT':
        EXIT()
    elif command.upper() == 'CLEAR':
        CLEAR()
    elif command.upper() == "TOUCH":
        TOUCH()
    elif command.upper() == "MV" or command.upper() == "MOVE":
        MV()
    elif command.upper() == "CP" or command.upper() == "COPY":
        CP()
    elif command.upper() == "RM" or command.upper() == "REMOVE":
        RM()
    elif command.upper() == "RUN":
        RUN()
    elif command.upper() == "CHDIR" or command.upper() == "CD":
        CHDIR()
    elif command.upper() == "HELP":
        HELP()
    elif command.upper() == "MKDIR":
        MKDIR()
    elif command.upper() == "RMDIR":
        RMDIR()
    elif command.upper() == "DIR" or command.upper().startswith("LS"):
        DIR()
    else:
        print('COMMAND NOT FOUND OR NOT TYPED PROPERLY')
    try:
       recurse()
    except KeyboardInterrupt:
        try:
            print('')
            recurse()        
        except KeyboardInterrupt:  
                print('')            
                recurse()
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
login()
