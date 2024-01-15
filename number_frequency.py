# Create a program which counts the number of each element (int in this case)
# There will be duplicates and more in the list 

crazy_list = [1, 2, 2, 2, 3, 4, 4, 5, 4, 4, 4, 4, 7, 6, 8, 9, 10, 10, 10, 1, 5, 2, 2, 5, 2, 6, 7, 3, 6, 8, 2, 9, 5, 9, 9, 4, 8, 5, 6, 7, 7, 1, 10, 3, 1, 10, 2, 2, 4, 2, 5, 6, 2, 1, 1, 3, 2, 4, 2, 2, 6, 4, 7, 3, 4, 5, 7, 2, 9, 9, 9, 3 , 7, 7, 4, 8, 6, 5, 2, 7, 1, 7, 2, 4, 7, 2, 4, 5, 2, 4, 8, 2, 2, 4]

def number_counter(list_to_count):
    '''
    This function counts the frequency of each element in a given list. 
    '''
    count_dict = {}
    for number in list_to_count:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    return count_dict

frequency = number_counter(crazy_list)
print(f'Frequency of each element: {frequency}') 
