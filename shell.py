#!/usr/bin/python3

import sys
import time
import colors
import os
import subprocess
import getpass
import datetime
from datetime import date
if os.path.exists('user/'):
    pass
else:
   os.mkdir('user/')
home = os.getcwd()+"/user/"
os.chdir(home)
global cmdlist
cmdlist = '''
Command List for now:

CHDIR - Change the current working directory
DIR - List files in the directory
HELP - Get help for commands
MKDIR - Make a new directory
RMDIR - Remove a directory
MV - Move a file somewhere else
CP - Copy a file somewhere
TOUCH - Make a New File
RM - Remove a file
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
    os.chdir(cd)
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
    subprocess.run(f'python3 user/{app}', shell=True)
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
    elif command.upper() == "MV":
        MV()
    elif command.upper() == "CP":
        CP()
    elif command.upper() == "RM":
        RM()
    elif command.upper() == "RUN":
        RUN()
    elif command.upper() == "CHDIR":
        CHDIR()
    elif command.upper() == "HELP":
        HELP()
    elif command.upper() == "MKDIR":
        MKDIR()
    elif command.upper() == "RMDIR":
        RMDIR()
    elif command.upper() == "DIR" or command.upper() == "LS":
        DIR()
    else:
        print('COMMAND NOT FOUND OR NOT TYPED PROPERLY')
    recurse()
def recurse():
    main()
main()
