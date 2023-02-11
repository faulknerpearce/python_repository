from util import *

# reads into a list of one string
lines = f_readlines("1.txt")

# grab first and only string in list and split into a list of characters
parenthesis_list = split_string(lines[0])


# convert parenthesis list into list of 1s and 0s and sum it
def mapper(c):
    if c == '(':
        return 1
    return -1


floor = 0
pos = 1
for p in parenthesis_list:
    if p == '(':
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        break
    pos += 1

print(floor)
print(pos)

ans1 = sum(lmap(mapper, parenthesis_list))
print(ans1)
