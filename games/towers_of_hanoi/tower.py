from stack import Stack

# Create a list of three stacks: left, middle, and right.
def create_stack_list():
    stacks = []
    
    left_stack = Stack('Left')
    middle_stack = Stack('Middle')
    right_stack = Stack('Right')
    
    stacks.append(left_stack)
    stacks.append(middle_stack)
    stacks.append(right_stack)
    
    return stacks

# Get the number of disks from the user.
def get_number_of_disks():
    num_disks = int(input('\nHow many disks do you want to play with?: '))
    while num_disks < 3:
        num_disks = int(input('Enter a number greater than or equal to 3: '))
    return num_disks

# Add disks to the left stack.
def add_disks_to_stack(num_disks, my_stack_list):
    for disk in range(num_disks, 0, -1):
        my_stack_list[0].push(disk)

# Print the stack choices to the user.      
def print_choices(my_choices, my_stack_list):
    for i in range(len(my_stack_list)):
         name = my_stack_list[i].get_name()
         letter = my_choices[i]
         print(f'Enter {letter} for {name}')

# Get user input for selecting source and destination stacks.
def get_user_input(my_stack_list):
    choices = [stack.get_name()[0] for stack in my_stack_list]
    
    while True:
        print_choices(choices, my_stack_list)
        choice = input(f'\nEnter your choice: ')
        
        if choice in choices:
            i = choices.index(choice)
            return my_stack_list[i]
        else:
            print('Invalid Input. Try Again.\n')
         
# main program
print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stack_list = create_stack_list()

#Set up the Game
num_disks = get_number_of_disks()
add_disks_to_stack(num_disks, stack_list)

optimal_number = (2 ** num_disks) - 1

#Play the Game
num_user_moves = 0 

while stack_list[2].get_size() != num_disks:
    
    print('\n...Current Towers...\n')
    for stack in stack_list:
        print(f'{stack.print_items()}\n')
    
    while True:
        print('Which stack do you want to move from?\n')
        from_stack = get_user_input(stack_list)
        
        print('\nWhich stack do you want to move to?\n')
        to_stack = get_user_input(stack_list)

        if from_stack.get_size() == 0:
            print('\nThis tower is empty. Try Again.')
        
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        
        else:
            print('\nCannot move a larger disk onto a smaller disk. Try Again')

print(f'\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {optimal_number}')