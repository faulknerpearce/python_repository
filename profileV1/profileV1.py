from utility import log_in, make_account, accsess_account, password_check
#This is my main profile program
profiles = [["2375", "Bob Anderson", 25], ["4458", "Alice Whales", 24]]

user_in = input("Enter your password: ")

myvalue = log_in(user_in, profiles)

if type(myvalue) == int:
    accsess_account(myvalue, profiles)
else:
    choice = input("No account was found. press (1) to make one or Press 2 to exit: ")

if choice == "1":
    available = password_check(profiles)
else: 
    print("Program terminated")

if available == 1:
    make_account(profiles)