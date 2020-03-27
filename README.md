# P7S files bulk decrypt

Decrypts all .p7s files in a folder

1.Build exe with pyinstaller include additional exe and dll files
>pyinstaller -F --add-data "openssl.exe;." --add-data "ssleay32.dll;." --add-data "libeay32.dll;." pp7s.py

2.Place and run pp7s.exe in the folder where you want to decrypt files
