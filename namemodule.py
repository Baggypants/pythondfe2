def nameCheck(inName):
    while True:
        name = str(input(f'Enter the {inName} name \n')).lower()
        if not name.isalpha():  # if it's not just letters then print message
            print('Alphabet charactors only please! Not even spaces.')
        else:
            return name  # this breaks out the loop



def numCheck(inName):
    while True:
        name = str(input(f'Enter the {inName} name \n')).lower()
        if not name.isdigit():  # if it's not just letters then print message
            print('Number charactors only please! Not even spaces.')
        else:
            return name  # this breaks out the loop

def random(inName):
        name = str(input(f'Enter the {inName} name \n')).lower()
        if not name.isalnum():  # if it's not just letters then print message
            print('Number AND alphabet charactors please! Not even spaces.')
        else:
            return name  # this breaks out the loop
