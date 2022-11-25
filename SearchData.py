def SearchContact(path):
    searchWord = str(input("Name or number: "))
    with open(path, 'r') as data:
        listData = list(data)
    searchData = ("\n".join(search for search in listData if searchWord.lower() in search.lower()))
    if searchData != '':
        print(searchData)
    else:
        print("Nothing found.")