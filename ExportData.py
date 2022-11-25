import os
import pathlib
from pathlib import Path
from Debug import DataIsNotExist

def ExportDataTxt(filePath):
    with open(filePath, 'r') as data:
        listData = list(data)
    fileName = input("Name of the new file: ")
    path = ''.join((str(pathlib.Path.cwd()), '\\', fileName, '.txt'))
    if os.path.exists(path):
        print("Error. Data already exist.")
    else:
        try:
            with open(str(path), 'w') as data:
                data.writelines("".join(line for line in listData))
        except IOError:
            print("Error. Invalid characters.")


def ExportDataCsv(filePath):
    with open(filePath, 'r') as data:
        listData = list(data)
    fileName = input("Name of the new file: ")
    path = ''.join((str(pathlib.Path.cwd()), '\\', fileName, '.csv'))
    if os.path.exists(path):
        print("Error. Data already exist.")
    else:
        try:
            with open(str(path), 'w') as data:
                data.writelines("".join(line for line in listData))
        except IOError:
            print("Error. Invalid characters.")