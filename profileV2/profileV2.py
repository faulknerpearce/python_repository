# write a nested function for cheking username and password.
users = [["austin", "1234"]]
user = ""
choice = 0 

# This function locates the entered username 
def username_check(user_list, userName):
    i = 0
    while i < len(user_list):
        if userName == user_list[i][0]:
            print("Your account was located.")
            password = input("Enter your password: ")
            theUser, option = password_check(user_list, password, i)
            return theUser, option
        else:
            i += 1
    # If no account it found provide an option to create a new one. 
    if i >= len(user_list):
        option = int(input("No account located. Press 2 to create an account: "))
        return None, option 
          
# this fucntion verifys the entered password 
def password_check(user_list, userPassWord, index):        
    tries = 3
    option = 1
    while tries >= 0 and option == 1:
        if userPassWord == user_list[index][1]:
            option = input("Welcome to the game " + str(user_list[index][0]))
            theName = user_list[index][0]
            return theName, option 
        else:
            print("Incorrect password. Tries remaining: " + str(tries))
            option = int(input("Press 1 to try again: ")) 

# this function will create an account 
def create_account(user_list, userName):
    while option == 1:
        taken = available(user_list, userName)
        if taken == False:
            user_list[-1].append([userName])
            password = input("Create a password: ")
            user_list[-1].insert(1, password)
            option = int(input("Account created. Press 3 to log in: "))
            return option
        else:
            option = int(input("This username is taken, would you like to try again? Press 1: Press 5 to exit"))
    if option == 5: 
        print("Program terminated ")
        return option 

# this function will ensure that the username is available 
def available(user_list, name):
   is_taken = None 
   for i in range(len(user_list)):
       if name == user_list[i][0]:
           is_taken = True
           return is_taken 
   if is_taken == None:
       is_taken = False
       return is_taken

# The Main Program #
while choice != 5:
    count = 1
    if users == [] or choice == 2:
        keyboard = input("Create Account. Please enter Your name: ")
        choice = create_account(users, keyboard)
    
    elif choice == 3 or count == 1:
        keyboard = input("Log in. Please enter Your name: ")
        user, choice = username_check(users, keyboard)
    count += 1

# exit this loop once an account has been located or created. 
print(user)
