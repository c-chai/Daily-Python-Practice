# Count all letters, digits, and special symbols from a given string
# Make the list randomly generated 

import random 
import string 

def generate_random_list(length):
    random_list = [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length)]
    return random_list

def count_everything(random_list):
    letter_count = 0
    digit_count = 0
    special_count = 0

    for char in random_list:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1 
    return letter_count, digit_count, special_count

# Generate a random list of length 40 
random_list = generate_random_list(40)

# Count the occurrences
letter_count, digit_count, special_count = count_everything(random_list)

# Print the results 
print("Random List:", random_list)
print("Letter Count:", letter_count)
print("Digit Count:", digit_count)
print("Special Symbol Count:", special_count)