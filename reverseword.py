
# input text, put in var
backWards = str(input('Type a word: '))
# how many letters? Take one away because lists
# start at 0

countStr = len(backWards) - 1
sdrawKacb = ''
while countStr > -1:
    sdrawKacb = sdrawKacb + backWards[countStr]
    countStr = countStr - 1
print(sdrawKacb)