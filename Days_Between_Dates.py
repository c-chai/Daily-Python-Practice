# Create a program which tells you the number of days between two given dates 
# This program will also catch invalid inputs and prompt the user to re-enter the date correctly

from datetime import datetime

def days_between_dates(date1, date2):
    '''
    This function calculates the number of days between two given dates. 
    '''

    date_format = "%Y-%m-%d"
    try:
        d1 = datetime.strptime(date1, date_format)
        d2 = datetime.strptime(date2, date_format)

        # Calculate the difference between the two dates
        difference = d2 - d1
        return abs(difference.days)
    except ValueError as e:
        print("Invalid input. Please enter the date in YYYY-MM-DD format.")
        return None

while True: 
    date1 = input('Enter the first date (YYYY-MM-DD): ')
    date2 = input('Enter the second date (YYYY-MM-DD): ')

    num_days = days_between_dates(date1, date2)
    
    if num_days is not None:
        print(f'The number of days between {date1} and {date2} are {num_days} days~!!!')
        break