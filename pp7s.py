"""
Bulk decryptor for all .p7s files in a folder

1.Build exe with pyinstaller include additional exe and dll files
pyinstaller -F --add-data "openssl.exe;." --add-data "ssleay32.dll;." --add-data "libeay32.dll;." pp7s.py

2.Place and run pp7s.exe in the folder where you want to decrypt files
"""


import os
import subprocess
import sys

os.chdir(os.path.abspath(os.path.dirname( __file__ )))

dir = "0decript"
if not os.path.exists(dir):
    os.mkdir(dir)

def app_path():
    if getattr(sys, 'frozen', False):
        app_path = os.path.dirname(sys.executable)
    elif __file__:
        app_path = os.path.dirname(__file__)
    return app_path

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

for path in os.listdir():
    if os.path.splitext(path)[-1] == '.p7s':
        full_path = os.path.abspath(path)
        if os.path.isfile(full_path):
            output_path=dir+'\\' + os.path.splitext(path)[0]
            subprocess.Popen([resource_path('openssl.exe'), "smime","-inform", "DER", "-verify" ,"-noverify",'-in', full_path,"-out",output_path])