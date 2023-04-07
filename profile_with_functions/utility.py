# this is where i will write the functions for my profile program

# The Check user function will return an int if if find the account and a bool if no account was found. 
def check_user(password, list):
    i = 0 
    while i < len(list):
        if password == list[i][0]:
            print("Your account was located.")
            myvalue = i
            return myvalue
        else: 
            print(i)
            i += 1 
    if i >= len(list):
        myvalue = True
        return myvalue

def password_check(list):
    index = 0  
    tries = 1
    while index < len(list) and int(tries) == 1 :
        password = input("Enter a 4 digit password: ")
        if password == list[index][0]:
            tries = input("this password is taken. Try again? press 1 for yes and 2 to exit  ")
            index += 1 
        else:
            print("Password is avaliable")
            list.append([password])
            available = 1 
            return available
            

def make_account(list):
    username = input("Enter your full name: ")
    list[-1].insert(1, username)
    age = input("Enter your age: ")
    list[-1].insert(2, int(age))
    print(list)

def found_account(num, list):
    print("Welcome back " + list[num][1])