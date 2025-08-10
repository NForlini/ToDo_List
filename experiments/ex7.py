with open('../files/doc.txt') as file:
    print('hello')
    print(file.read())

#by default for open had r as the second argument
#cant have more than one file.read()