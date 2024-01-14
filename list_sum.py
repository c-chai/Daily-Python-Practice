# Create a program which gives the sum of a list 
# List is randomly generated 

import random 

def list_generator():
    '''
    This function generates a list of random numbers between 1-100 inclusive. 
    Length of length will be random number between 1-10. 
    '''
    list_length = random.randint(1, 10)
    return [random.randint(1, 100) for _ in range(list_length)]

random_list = list_generator()
print(f"Random List: {random_list}")

sum_of_numbers = sum(random_list)
print(f"Sum of Numbers: {sum_of_numbers}")