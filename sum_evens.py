# Create a program that generates random integers in a list 
# The program should find the sum of all the even numbers in the list 

import random 

def sum_of_even_numbers(n, start_range, end_range): 
    '''
    This function generates a list of 'n' random integers within the specified range. 
    This function also calculates the sum of the even numbers in the list using list comprehension.
    '''
    numbers = [random.randint(start_range, end_range) for _ in range(n)]

    even_sum = sum(number for number in numbers if number % 2 == 0)

    return numbers, even_sum 

# Call to generate a list of 10 random integers between 1 - 100. 
random_list, even_sum = sum_of_even_numbers(10, 1, 100)

print(f'From the random list {random_list}, the sum of the even numbers is {even_sum}')