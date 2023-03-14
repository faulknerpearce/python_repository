from utility import check_user
from utility import make_account
from utility import found_account
from utility import password_check
#This is my main profile program
profiles = [["2375", "Austin Faulkner-Pearce", 25], ["4458", "Nicole Leon", 24]]

user_in = input("Enter your password: ")

myvalue = check_user(user_in, profiles)

if type(myvalue) == int:
    found_account(myvalue, profiles)
else:
    choice = input("No account was found. press (1) to make one or Press 2 to exit: ")

if choice == "1":
    available = password_check(profiles)
else: 
    print("Program terminated")

if available == 1:
    make_account(profiles)
   