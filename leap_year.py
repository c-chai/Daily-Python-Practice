# Create a program that determines whether the user input of a year is a leap year 

def is_leap_year(year):
    '''
    Check if year is divisble by 4 but not by 100.
    Or it is divisible by 400. 
    '''
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
test_year = int(input('Enter a year to see if it is a leap year: '))
result = is_leap_year(test_year)

if result:
    print(f"{test_year} is a leap year!!!")
else:
    print(f"{test_year} is not a leap year :<")