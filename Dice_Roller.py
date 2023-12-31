# Create a program which rolls a dice with however many sides the user wants 

import random 

def roll_dice(num_sides=6):
    '''
    This function rolls a dice that has 6 sides.
    Default num_sides is 6, but user can input a number. 
    Returns a random number between 1 and num_sides. 
    '''
    return random.randint(1, num_sides)

num_sides = input('Enter the number of sides on your dice (default is 6): ')
num_sides = int(num_sides) if num_sides.isdigit() else 6
result = roll_dice(num_sides)
print(f'You rolled a(n) {result} on a(n) {num_sides}-sided dice!')