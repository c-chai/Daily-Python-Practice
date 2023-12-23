import random
import time
# Binary search is faster than a naive search.
# A naive search scans entire list and checks if it's equal to target. 
# If yes, return the index. If no, return -1. 
# We will do a time analysis for proof.

def naive_search(l, target):
    # Example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target: 
            return i
    return -1 


# Binary searches use divide and conquer.
def binary_search(l, target, low=None, high=None):
    # Leverage the fact that this list is sorted. 
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1 

    if high < low:
        return -1

    # Example l = [1, 3, 5, 10, 12] # Should return 3 
    midpoint = (low + high) // 2 # 2 

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else: 
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)
    
if __name__ =='__main__':
    l = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))

    # Build a sorted list with length 10000
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds")

# Takeaway: if you ever have to search a sorted list, never search every single item