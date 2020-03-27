# P7S files bulk decrypt
This code easily decrypts all .p7s files from the current folder.

# Usage
Place and run pp7s.exe in the folder where you want to decrypt files

# If you want to rebuild the exe 
Build with pyinstaller to include additional exe and dll files
>pyinstaller -F --add-data "openssl.exe;." --add-data "ssleay32.dll;." --add-data "libeay32.dll;." pp7s.py

