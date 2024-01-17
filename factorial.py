# Create a program which gives the factorial of a given number the user inputs
# Write error handle non-integers and negative numbers and will keep asking unless user types 'q'

def create_factorial():
    while True:
        user_input = input("Enter a non-negative integer, or type 'q' to quit: ")
        
        if user_input.lower() == 'q':
            print("Program exited.")
            break

        try:
            number = int(user_input)
            if number < 0:
                print("Error! Negative numbers do not have factorials.")
            else:
                factorial = 1
                for i in range(1, number + 1):
                    factorial *= i
                print(f"The factorial of {number} is {factorial}.")
        except ValueError:
            print("Error! Please enter a valid integer.")

create_factorial()