# name compatibility compatibility calculator
# two names as input
# take name lengh
# loop that counts all vowels*
# validate name isn't numbers  ALL DONE!
# - need avar
# - use tolower?
# do maths
# write at least two procedures

# name = '123'  or name = 'abce'  or name = 'leon123' <- .isalnum()

import namemodule


def calculation(firstName,lastName):
    vowlesVar = 'aeiou'
    len1 = len(firstName)
    len2 = len(lastName)
    vowleCount1 = 0
    vowleCount2 = 0
    for l in firstName:
        if vowlesVar.find(l):
            vowleCount1 += 1
    for l in lastName:
        if l in vowlesVar:
            vowleCount2 += 1
    percent1 = (vowleCount1 / len1) * 100
    percent2 = (vowleCount2 / len2) * 100
    totalCompat = (percent1 + percent2)/2
    print(f"You compatibility percentage is: {totalCompat}%")
    print('Have a long and happy life💕')

    

def mainProg():
    firstNameInput = namemodule.nameCheck('first')
    lastNameInput = namemodule.nameCheck('second')
    calculation(firstNameInput,lastNameInput)

mainProg()