profile = [["fireaustin", "7459", "Austin Faulkner-pearce", "25"], ["nicole", "ggg"]]
index = 0
new = True
user_name = input("Enter your username ")

while index < len(profile):
    if user_name != profile[index][0]:
        index += 1
    
    elif user_name == profile[index][0]:
        print("Welcome back " + str(profile[index][2]))
        new = False
        break
        
if new == True:
    print("We could not find your account")