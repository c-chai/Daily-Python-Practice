# Create a program which returns the elements whose value is equal to that of its index value 

class Solution: 

    def valueEqualtoIndex(self, arr, n):
        '''
        arr is expected ot be a list(or array) of integers. 
        n is an integer representing the number of elements in 'arr'.
        
        '''
        lst = [] # create empty list to store the indices where value in 'arr' == index
        for i in range(1, n+1):
            if i == arr[i-1]:

                lst.append(i)
        return lst