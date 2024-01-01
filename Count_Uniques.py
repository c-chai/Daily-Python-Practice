# Write a program that counts the number of unique characters in a given string
# Case-insensitive

def count_uniques(s):
    '''
    This function counts the number of unique characters in the user's input string
    Case-insensitive by using s.lower()
    Thenn a set is used to store the unique characters 
    Finally, function returns length of unique characters 
    '''
    s = s.lower()
    unique_chars = set(s)
    return len(unique_chars)


user_input = input("Write your sentence here! ")
unique_count = count_uniques(user_input)
print(f'Number of unique characters is {unique_count}.')
