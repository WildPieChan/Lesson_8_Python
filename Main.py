from Controller import *

phoneDirectoryPath = StartProgram()

while phoneDirectoryPath == '':
    phoneDirectoryPath = FirstActionSelect()

if phoneDirectoryPath != 0:
    action = 0
    while action < 5:
        action = ActionSelect(phoneDirectoryPath)