# Write a program where the function calculates the sum of numbers from 0 - 100

def addition(num):
    '''
    This function takes one argument 'num'
    It is intended to calculate the sum of numbers from 0 - 100
    '''
    if num:
        # This part checks if num is not zero 
        # If num is not zero (aka it's positive), the function calls itself with the argument decreased by 1 
        # This is a recursive call, where function keeps calling itself with a smaller number each time 
        # The function then returns the current value of 'num' added to the result of 
        # addition(num - 1)
        # This step accumulates the sum of all numbers from 'num' down to 1 
        return num + addition(num - 1)
    else:
        # This part is the base case for the recursion
        # When 'num' becomes 0, the function stops calling itself and returns 0 
        return 0
# This commences the recursion
res = addition(100)
print(res)
        