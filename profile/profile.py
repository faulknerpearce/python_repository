profile = [["Mr-Orange", "7459", "James Bancroft"], ["Bob_007", "6677", "Bob Morewell"]]
new = True
user_in = 0

while user_in != 2:
    my_len = len(profile) - 1
    user_name = input("\nEnter your username: ")
    index = 0
    #This loop checks for an existing account with the username  
    while index <= my_len:
      if user_name == profile[index][0]:
        new = False
        break
      else:
        index += 1
    #Option to create an account 
    if new == True:
      print("\nWe could not find your account.")
      user_in = input("Press(1) to create an account. Press(2) to quit: ")
    else: 
      #Password loop
      tries = 3
      print("\nAccount Located.")
      while tries > 0: 
          password = input("Enter your password: ")
          if password != profile[index][1]:
              tries += -1
              print("incorrect password, try again.\nTries remaining: " + str(tries))
              break
          else:
              print("\n\nWelcome Back " + str(profile[index][2]))
              user_in = 2
              break  
    #Account creation. 
    if int(user_in) == 1:
      #print("\nYou made it to the checkpoint")
      i = 0
      user_name_tries = 3
      account_clash = False
      #Check if the username is taken 
      while i < my_len and user_name_tries > 0:
        new_user = input("Create a username: ")
        if new_user == profile[i][0]:
         user_name_tries += -1
         print("This username is taken, Try again.\nTries remaining until timeout: " + str(user_name_tries)) 
        else: 
          i += 1
      #append list if the username is available  
      if account_clash == False:
        print("\nThis username is available! ")
        profile.append([new_user])
        password = input("Create a password: ")
        profile[-1].insert(1, password)
        full_name = input("Enter your full name: ")
        profile[-1].insert(2, full_name)
        print(profile)
    
    if int(user_in) == 2:
     print("\nProgram terminated.\n")
     break
    
