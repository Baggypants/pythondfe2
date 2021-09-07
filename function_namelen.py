# function that shows the lenght of a given string 
def countname(personname):
    return len(personname)

student = "Slartibartfarst"
letters = countname(student)

print(f"{student} has {letters} letters in their name")

