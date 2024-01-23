# Create a program which gives the sum of all the digits in a given number 

def sum_of_digits(number):
    # Convert the number to a string to iterate over its digits 
    str_number = str(number)

    # Sum the digits using the list comprehension and sum()
    digit_sum = sum(int(digit) for digit in str_number)

    return digit_sum

test_number = 4378190123642
result = sum_of_digits(test_number)
print(result)