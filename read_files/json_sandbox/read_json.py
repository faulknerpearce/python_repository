import json

# this is how to read from a json file 
with open("message.json") as message_json:
  message = json.load(message_json)
  print(message["text"])