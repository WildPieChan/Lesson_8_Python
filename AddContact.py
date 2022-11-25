def NewContact(path):
    contactName = input("Enter a name: ")
    phoneNumber = input("Enter a phone number: ")
    classNumber = input("Student's class: ")
    newLine = ''.join(('\n', contactName, ',', phoneNumber, ',', classNumber))
    with open(str(path), 'a') as data:
        data.writelines(newLine)