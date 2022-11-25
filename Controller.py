import Debug
import CreateData
import PrintData
import DeleteContact
import ExportData as Exp
from AddContact import NewContact
from ImportData import ImportData
from SearchData import SearchContact


def StartProgram():
    print("Phone directory.")
    return ''


def FirstActionSelect():
    print("\nSelect an action:\n\
        1 - Import directory;\n\
        2 - Create a new directory;\n\
        3 - End a program.")
    action = Debug.SelectFromThree("Action: ")
    # Import derictory
    if action == 1:
        filePath = ImportData()
        if filePath == '':
            return ''
    # Create directory
    elif action == 2:
        print("\nSelect an action:\n\
            1 - Create as .txt;\n\
            2 - Create as .csv.\n\
            3 - End program.")
        action = Debug.SelectFromThree("Action: ")
        # Create .txt directory
        if action == 1:
            filePath = CreateData.CreateDataTxt()
            if filePath == '':
                return ''
        # Create .csv directory
        elif action == 2:
            filePath = CreateData.CreateDataCsv()
            if filePath == '':
                return ''
    elif action == 3:
        return 0
    return filePath


def ActionSelect(filePath):
    print("\nSelect an action:\n\
        1 - Add contact;\n\
        2 - Delete contact;\n\
        3 - Search contact;\n\
        4 - Print directory;\n\
        5 - Export as .txt;\n\
        6 - Export as .csv;\n\
        7 - End program.")
    action = Debug.SelectFromAll("\nAction: ")
    # Add new contact
    if action == 1:
        NewContact(filePath)
    # Delete contact
    if action == 2:
        DeleteContact.DeleteLine(filePath)
    # Search contact
    if action == 3:
        SearchContact(filePath)
    # Print content
    if action == 4:
        PrintData.PrintContent(filePath)
    # Export as .txt
    if action == 5:
        Exp.ExportDataTxt(filePath)
    # Export as .csv
    if action == 6:
        Exp.ExportDataCsv(filePath)
    return action