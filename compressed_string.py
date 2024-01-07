# Create a program that compresses a string using the counts of repeated characters 
# If the comrpessed string will not become smaller, function will return original string 
# Strings tested will be randomly generated 

import random 
import string 

def compress_string(input_string):
    '''
    If the string is empty, return as is. 
    '''
    if not input_string:
        return input_string
    
    compressed = []
    count = 1

    # Iterate through the string, counting consecutive characters
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            compressed.append(input_string[i - 1] + str(count))
            count = 1

    # Add the last set of characters 
    compressed.append(input_string[-1] + str(count))

    # Join the compressed parts 
    compressed_string = ''.join(compressed)

    # Check if compression is efficient
    if len(compressed_string) < len(input_string):
        return compressed_string
    else:
        return input_string
    
def generate_random_string(length_range=(5, 15), characters=string.ascii_lowercase):
    '''
    Generate a random string of a length within the specified range.
    Default characters are only lowercase letters. 
    '''
    length = random.randint(*length_range)
    return ''.join(random.choices(characters, k=length))

def main():
    '''
    This function generates and tests random strings.
    '''
    for _ in range(5):  # Generate 5 random strings
        random_string = generate_random_string()
        compressed = compress_string(random_string)
        print(f"Original: {random_string}, Compressed: {compressed}")

if __name__ == "__main__":
    main()