import random
dice_list = []
i = 0 

while i < 2:
    num = random.randint(0, 10)
    dice_list.append(num)
    i += 1
#sum the roll of both dice
dice_sum = 0
for n in dice_list:
    dice_sum += n 
print(str(dice_sum))