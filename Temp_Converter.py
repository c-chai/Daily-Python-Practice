# Create a program that converst Celsius to Fahrenheit, and Fahrenheit to Celsius
# Create error handling to check if user inputs a valid temperature
# Program will keep running until user types in 'quit'

def convert_temperature(temp, unit):
    '''
    This function converts temperature between Celsius and Fahrenheit. 
    '''
    if unit.lower() == 'c':
        # Converts Celsius to Fahrenheit
        return (temp * 9/5) + 32
    else:
        # Convert Fahrenheit to Celsius 
        return (temp - 32) * 5/9
    
def main():
    while True: 
        # User input for temperature and unit 
        try:
            temp = float(input("Enter the temperature (or type 'quit' to exit the program): "))
            unit = input("Enter unit (C for Celsius, F for Fahrenheit): ")

            # Check if the unit is valid 
            if unit.lower() not in ['c','f']:
                print("Invalid unit. Please enter C for Celsius or F for Fahrenheit: ")
                continue

            # Convert and display the result 
            converted_temp = convert_temperature(temp, unit)
            if unit.lower() == 'c':
                print(f"{temp} Celsius is {converted_temp:.2f} Fahrenheit.")
            else: 
                print(f"{temp} Fahrenheit is {converted_temp:.2f} Celsius.")

        except ValueError as e:
            # Check if the user wants to quit 
            if str(e).startswith("could not convert string to float: 'quit'"):
                print("Exiting program.")
                break
            else:
                print("Please enter a valid number for temperature.")

main()
