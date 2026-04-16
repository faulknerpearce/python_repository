# Program to read compromised usernames from a CSV 
import csv, json

# This list will store the compromised usernames  
compromised_users = []  

# READ CSV FILE
# Open passwords CSV file and read into dict reader
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)

  # Extract just the usernames into our list
  for row in password_csv:
    compromised_users.append(row['Username'])
      
# WRITE TEXT FILE  
# Open a text file and write the usernames    
with open("compromised_users.txt", "w") as text_file:
  for user in compromised_users:
    text_file.write(user + "\n")  
      
# WRITE JSON FILE
# Create a dict to store message    
message = { "recipient": "The Boss", "message": "Mission Success" }

# Open JSON file and serialize message to it  
with open("boss_message.json", "w") as json_file:
  json.dump(message, json_file)

  slash_null_sig = """
  _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/ """

with open("new_passwords.csv", "w") as new_passwords:
  new_passwords.write(slash_null_sig)
 