def reversename(personname):
    if personname.isdigit():
        print('No Numbers!')
        exit()
    countStr = len(personname) - 1
    sdrawKacb = ''
    while countStr > -1:
        sdrawKacb = sdrawKacb + personname[countStr]
        countStr = countStr - 1 
    return sdrawKacb


studentName = str(input('Enter Student Name: '))
reveresdNameVar = reversename(studentName)
print(f"{studentName} is {reveresdNameVar} backwards")

studentSurName = str(input('Enter Student Surname: '))
reveresdSurNameVar = reversename(studentSurName)
print(f"{studentSurName} is {reveresdSurNameVar} backwards")