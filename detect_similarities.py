# Generate two randomly generated lists
# Create a program which detects similarities between the two lists 
# List these commonalities in ascending order! 

import random 

def generated_lists():
    '''
    This function generates two random lists with 10 random numbers, ranging from 1-20
    '''
    list1 = random.sample(range(1, 21), 10)
    list2 = random.sample(range(1, 21), 10)
    return list1, list2

def find_common_elements(list1, list2):
    '''
    First, this function converts the lists into sets (so that we can use '&' for efficiency)
    Then, it finds the common elements between the two lists and sorts them 
    '''
    common_elements = sorted(set(list1) & set(list2))

# Generate the lists 
list1, list2 = generated_lists()

# Find the common elements sorted from smallest - largest 
common = find_common_elements(list1, list2)

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Common elements in ascending order: {common}")