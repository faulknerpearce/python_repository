#Fizz Buzz N Times 
import random 
num = 1
my_list = []

#Create a list of random numbers 
while len(my_list) <= 10:
   rand = random.randint(0, 20)
   my_list.append(rand)

#Fizz Buzz Loop!
while num <= 10:
   if my_list[num] % 15 == 0:
      print("Fizz")
      num += 1 
   elif my_list[num] % 3 == 0:
      print("Buzz")
      num += 1 
   elif my_list[num] % 5 == 0: 
      print("FizzBuzz")
      num += 1 
   else: num += 1 