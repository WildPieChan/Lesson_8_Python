import os
import pathlib
from pathlib import Path
from Debug import DataExist


def CreateDataTxt():
    fileName = input("Enter the file name: ")
    path = ''.join((str(pathlib.Path.cwd()), '\\', fileName, '.txt'))
    if os.path.exists(path):
        print("Error. Data already exist.")
    else:
        try:
            with open(str(path), 'w') as data:
                data.writelines("Name,Phone number")
                data.writelines("\n-----------------\n")
            return path
        except IOError:
            print("Error. Invalid characters.")
            return ''


def CreateDataCsv():
    fileName = input("Enter the file name: ")
    path = ''.join((str(pathlib.Path.cwd()), '\\', fileName, '.csv'))
    if os.path.exists(path):
        print("Error. Data already exist.")
    else:
        try:
            with open(str(path), 'w') as data:
                data.writelines("Name,Phone number")
                data.writelines("\n-----------------\n")
            return path
        except IOError:
            print("Error. Invalid characters.")
            return ''