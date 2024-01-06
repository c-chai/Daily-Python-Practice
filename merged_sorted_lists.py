# Create a program that merges two different length lists 
# The two lists are randomly generated 

import random

def generate_random_lists():
    '''
    This function generates two lists with random numbers between 1-10 and a random length between 1-5.
    '''
    length1 = random.randint(1, 5)
    length2 = random.randint(1, 5)
    list1 = sorted(random.sample(range(1, 11), length1))
    list2 = sorted(random.sample(range(1, 11), length2))
    return list1, list2

def merge_sorted_lists(list1, list2):
    '''
    This function merges two sorted lists into one sorted list. 
    '''
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[i]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append remaining elements of list1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    # Append elements of list2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list

# Generate the random lists 
list1, list2 = generate_random_lists()

# Merge the lists 
merged_list = merge_sorted_lists(list1, list2)

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Merged List: {merged_list}")