# Create a function that splits a string on hyphens 

str1 = 'dr-bender-is-a-dentist'

def divisive(input_string):
    '''
    This function splits the string on hyphens and breaks it into new lines. 
    '''
    new_list = input_string.split('-')
    spaced_out = '\n'.join(new_list)
    return spaced_out

# Call the function with the given string 
result_list = divisive(str1)

# Print the result 
print(result_list)