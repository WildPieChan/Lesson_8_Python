def SearchContact(path):
    print("Start typing the student's name, number or class.")
    searchWord = str(input("Press enter when it's done: "))
    with open(path, 'r') as data:
        listData = list(data)
    searchData = ("\n".join(search for search in listData if searchWord.lower() in search.lower()))
    if searchData != '':
        print(searchData)
    else:
        print("Nothing found.")