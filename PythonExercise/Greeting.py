Username= input("Please enter your username followed by a space: ") 
def greet_user_By_Slicing(username):
    spaceCharcount = username.find(" ");
    firstname = username[0:spaceCharcount]
    lastname = username[spaceCharcount + 1:len(username)]
    print(f"Hello {firstname.lower().capitalize()} {lastname.lower().capitalize()}")

def greet_user_By_split(username):
    firstname = username.split()[0]
    lastname = username.split()[1]
    print(f"Hello {firstname.lower().capitalize()} {lastname.lower().capitalize()}")

greet_user_By_Slicing(Username)
greet_user_By_split(Username)