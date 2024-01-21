# Create a program which counts the number of vowels in a string
# String is randomly generated 

import random 
import string 

def generated_random_string(length):
    '''
    This function defines the characters to include in the string.
    '''
    chars = string.ascii_letters # includes both upper and lowercases
    return ''.join(random.choice(chars) for _ in range(length))

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# Generate a random string of a specified length 
random_string = generated_random_string(10) # 10 character string 
print(f"Random string: {random_string}")

# Count the vowels in the string 
vowel_count = count_vowels(random_string)
print(f"Number of vowels in the string: {vowel_count}")