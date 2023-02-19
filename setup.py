#!/usr/bin/python3
import getpass
import os

def setpwd():
    f = open('user/password.pass', 'w')
    password = getpass.getpass('Password: ', stream=None)
    f.write(password)

try:
    if os.path.exists('user/Music'):
        pass
    else:
        os.mkdir('user/Music')
#============================================================#        
    if os.path.exists('user/Videos'):
        pass
    else:
        os.mkdir('user/Videos')
#============================================================#
    if os.path.exists('user/Documents'):
        print('directory exists!')
        pass
    else:
        os.mkdir('user/Documents')
#============================================================#
    if os.path.exists('user/Downloads'):
        pass
    else:
        os.mkdir('user/Downloads')
#============================================================#
    if os.path.exists('user/Pictures'):
        pass
    else:
        os.mkdir('user/Pictures')
#============================================================#
    if os.path.exists('user/Apps'):
        pass
    else:
        os.mkdir('user/Apps') 
#============================================================#
  #  setpwd()
except:
    pass
  #  setpwd()
