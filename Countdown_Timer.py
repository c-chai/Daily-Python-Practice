import time 

my_time = int(input('Enter time in seconds.'))

# This counts from my_time to 1 (excluding 0) in steps of -1 
for i in range(my_time, 0, -1):
    seconds = i % 60
    minutes = int(i / 60) %  60
    hours = int(i / 3600)
    # This prints in a 'hh:mm:ss' format and the 02 ensures that each time comoponent is displayed as a two-digit number with leading zeros if needed
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1) # Timer pauses for 1 second intervals 

print("TIME'S UP")