# Create a program that takes a string and determines whether it is a palidrome or not 
# Will return True or False 
# Ignores case and non-letter characters 

def is_palindrome(s):
    '''
    This function removes non-letter characters and coverts string to lowercase.
    Then, it checks if the string is reversed. 
    '''
    cleaned = "".join(char.lower() for char in s if char.isalpha())
    return cleaned == cleaned[::-1]

user_input = input("Enter a word or phrase to check if it's a palindrome: ")
if is_palindrome(user_input):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")