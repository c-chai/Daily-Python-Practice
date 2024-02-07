# Write a program to find the smallest number in a randomly generated list 

import random 

def find_smallest_number(numbers):
    # Initialize smallest number to a very large number 

    smallest = float('inf')

    # Iterate through the list to find the smallest number 
    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest

# Generate a random list of 10 random numbers between 1 -100 inclusive 
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Find the smallest number in the list 
smallest_number = find_smallest_number(random_numbers)

print(f'Randomly generated list: {random_numbers}')
print(f'THe smallest number in the list is {smallest_number}')