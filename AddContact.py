def NewContact(path):
    contactName = input("Enter a name: ")
    phoneNumber = input("Enter a phone number: ")
    newLine = ''.join(('\n', contactName, ',', phoneNumber))
    with open(str(path), 'a') as data:
        data.writelines(newLine)