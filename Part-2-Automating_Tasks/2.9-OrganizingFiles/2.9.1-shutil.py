import shutil, os,send2trash

getCWD = os.getcwd()

CWDFile = open('cwdfile.txt', 'a')

CWDFile.write(getCWD)

send2trash.send2trash(CWDFile)

