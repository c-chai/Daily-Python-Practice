# Write a program that finds the sum of the digits in a string 

def sum_in_string(s):
    # Initialize the sum with 0
    total = 0
    number = ''

    for char in s:
        if char.isdigit():
            # Build the number
            number += char
        else:
            # If the current sequence ends, add the number to the total and reset number
            if number:
                total += int(number)
                number = ''
    
    # Add the last number if the string ends with digits
    if number:
        total += int(number)
        
    return total

result = sum_in_string('12https')
print(result)
