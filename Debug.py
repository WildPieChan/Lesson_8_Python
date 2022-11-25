def InputNumber(inputText):
    ok = False
    while not ok:
        try:
            number = int(input(f"{inputText}"))
            ok = True
        except ValueError:
            print("Error. Only integer numbers. Try again...")
    return number
 

def SelectFromThree(inputText):
    ok = False
    while not ok:
        number = InputNumber(inputText)
        if (number == 1) or (number == 2) or (number == 3):
            ok = True
        else:
            print("Error. Choose correct number.")
    return number


def SelectFromAll(inputText):
    ok = False
    while not ok:
        number = InputNumber(inputText)
        if (number > 0) or (number < 8):
            ok = True
        else:
            print("Error. Choose correct number.")
    return number


def DeleteExistLine(listData):
    ok = False
    while not ok:
        line = InputNumber("Delete line: ")
        if (line > 0) and (line < len(listData) - 2):
            ok = True
        else:
            print("Error. Line is out of range.")
    return line