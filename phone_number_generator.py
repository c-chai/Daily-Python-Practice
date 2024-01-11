# Create a program which randomly generates a US phone number

import random 

def generate_phone_number():
    # generate random number between 200 - 999 inclusive
    area_code = random.randint(200, 999)

    # generate random numbers for first part of phone number between 200 - 999 inclusive
    # first digit should not be 1 or 0
    first_three = random.randint(200, 999)

    # generate last part of phone number between 1000 - 9999 inclusive
    last_four = random.randint(1000, 9999)

    # combine the parts into a standard phone number format
    phone_number = f"{area_code}-{first_three}-{last_four}"

    return phone_number

print(generate_phone_number())