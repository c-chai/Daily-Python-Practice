# Create a program that merges two lists while maintaining their sorted order
# Lists are randomly generated 

import random

def merged_sorted_listed(list1, list2):
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    while i < len(list1):
        merged_list.append(list1[i])

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

list1 = sorted([random.randint(1, 100) for _ in range(10)])
list2 = sorted([random.randint(1, 100) for _ in range(10)])

merged_list = merged_sorted_listed(list1, list2)

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Merged List: {merged_list}")