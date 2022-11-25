import pathlib
from pathlib import Path


def ImportData():
    try:
        fileName = input("Enter the file name: ")
        path = ''.join((str(pathlib.Path.cwd()), '\\', fileName))
        with open(str(path), 'r') as data:
            data.read()
        return path
    except IOError:
        print("Error. File does not exist.")
        return ''