#!/usr/bin/python3
import getpass
import os
#============================================================#
def setpwd():
    user = getpass.getuser()
    try:
        f = open(f'user/.password/{user}password.pass', 'x')
    except:
        f = open(f'user/.password/{user}password.pass', 'w')
    password = getpass.getpass('Password: ', stream=None)
    f.write(password)

#============================================================#
def dirsetup():
    if os.path.exists('user/'):
        pass
    else:
       os.mkdir('user/')
#============================================================#
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
    if os.path.exists('user/.password'):
        pass
    else:
        os.mkdir('user/.password')
#============================================================#
try:
    dirsetup()
    setpwd()
except:
    setpwd()
#============================================================#
