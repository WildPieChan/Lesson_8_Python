import PrintData
import Debug


def DeleteLine(path):
    PrintData.PrintContent(path)
    with open(path, "r") as data:
        listData = list(data)
    line = Debug.DeleteExistLine(listData)
    del listData[line + 2]
    with open(path, "w") as data:
        for element in listData:
            data.write(element)