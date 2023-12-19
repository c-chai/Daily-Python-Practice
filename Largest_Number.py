# Write a program which finds the largest number in a given list 

import random 

def gen_random_list():
    ''' 
    This function creates a random length list between 1-10
    '''
    list_length = random.randint(1,10)

    # Creates a random list of integers with values between 1-200
    random_list = [random.randint(1, 200) for _ in range(list_length)]

    return random_list

def find_largest_number(my_list):
    '''
    This function checks if the list is empty and finds the largest number in the list
    '''
    if not my_list: 
        return None 
    max_number = max(my_list)

    return max_number

# Create a random list 
my_random_list = gen_random_list()

# Prints out the random list 
print("Random List:", my_random_list)

# Prints out the highest value number
largest_number = find_largest_number(my_random_list)
print("Largest Number:", largest_number)
