# Create a program that determines whether the user's input number is a "happy number"
# Happy number definition:
# Starting with any positive integer, replace the number by the sum of the squares of its digits 
# Repeat process until the number = 1 (where it will stay), or loop endlessly in a cycle that doesn't include 1 
# Those numbers for which this ends ends in 1 are happy numbers! 

def is_happy_number(num):
    def get_digits_square_num(n):
        return sum(int(digit)** 2 for digit in str(n))
    
    seen = set() # keep track of the numbers encountered during the process to detect loops 
    while num != 1 and num not in seen:
        seen.add(num)
        num = get_digits_square_num(num)
    
    return num == 1

user_input = int(input('Enter a number to check if it\'s a happy number: '))
result = is_happy_number(user_input)
print(f'Is the number {user_input} a happy number? {result}')