# Write a program which finds the second largest number in the list 
# List will be randomly generated 

import random 

def generate_random_list(length, range_start, range_end):
    return [random.randint(range_start, range_end) for _ in range(length)]

def find_second_largest(numbers):
    if len(numbers) < 2:
        return None # Not enough elements to determine second largest number 

    largest = second_largest = float('-inf') # Both set to negative infinity
    for number in numbers:
        if number > largest:
            second_largest, largest = largest, number
        elif largest > number > second_largest:
            second_largest = number 
    
    return second_largest

random_numbers = generate_random_list(10, 1, 10) # Generate 10 random numbers between 1-10 inclusive 

print(f'Random List: {random_numbers}')
print('Second Largest Number:', find_second_largest(random_numbers))