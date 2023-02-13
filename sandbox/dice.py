import random
dice_list = []
i = 0 

while i < 2:
    num = random.randint(0, 10)
    dice_list.append(num)
    i += 1
msg = " "

for n in dice_list:
    msg += str(n) + " "
print(msg)
