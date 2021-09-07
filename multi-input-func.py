def studentdeets(nameVar,ageVar):
    if len(nameVar) > ageVar:
        print('Your name has more letters than years you have lived')
        nameGtAge = True
    else:
        print('You are older in years than your name has letters')
        nameGtAge = False
    return {'name':nameVar,'age':ageVar,'namelengtthanage':nameGtAge}


def inputLR(message,maxVal):
    testInp = input(message)
    if int(testInp) > maxVal:
        exit()
    return testInp

studentName = str(inputLR('Put in a name: ',50))
studentAge  = int(inputLR('Type in your Age: ',120))
funcReturn = studentdeets(studentName,studentAge)

print(funcReturn)