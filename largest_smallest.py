# Write a program that finds the largest and smallest number in a random list 
# Write this in a single pass 

import random 

def find_largest_smallest():
    # Generates a list of 10 random integers between 1 - 100 inclusive
    numbers = [random.randint(1, 100) for _ in range(10)]

    largest = smallest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
        elif number < smallest:
            smallest = number

    return numbers, largest, smallest

numbers, largest, smallest = find_largest_smallest()

print(f'In this randomly generated list {numbers}, the largest number is {largest} and the smallest number is {smallest} :)')