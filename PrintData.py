def PrintContent(path):
    data = open(path, 'r')
    dataContent = data.read()
    print(dataContent)
    data.close()