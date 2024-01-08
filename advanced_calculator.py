# Create a calculator that can perform the basic addition, subtraction, multiplication, division
# To make it advanced, add modulus, exponentiation, and some trig functions 
# Calculator should be able to handle errors such as 0 as a divisor 

import math # to add the trig functions 

def addition(a, b):
    return a + b 

def subtraction(a, b): 
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def modulus(a, b):
    return a % b

def exponentiation(a, b):
    return a ** b 

def sin(degrees):
    radians = math.radians(degrees)
    return math.sin(radians)

def cosine(degrees):
    radians = math.radians(degrees)
    return math.cos(radians)

def tangent(degrees):
    radians = math.radians(degrees)
    return math.tan(radians)
 
 # Main function to prompt user 
def main():
    while True:
        print("What operation would you like to perform?")
        print("Available operations: add, subtract, multiply, divide, modulus, exponentiate, sine, cosine, tangent, or quit.")
        operation = input("Enter operation: ").lower()

        if operation == 'quit':
            print("Exiting the calculator.")
            break

        num1 = float(input("Enter the first number: "))
        if operation not in ['sine', 'cosine', 'tangent']:
            num2 = float(input("Enter the second number: "))

        if operation == 'add':
            print("Result:", addition(num1, num2))
        elif operation == 'subtract':
            print("Result:", subtraction(num1, num2))
        elif operation == 'multiply':
            print("Result:", multiplication(num1, num2))
        elif operation == 'divide':
            print("Result:", division(num1, num2))
        elif operation == 'modulus':
            print("Result:", modulus(num1, num2))
        elif operation == 'exponentiatiate':
            print("Result:", exponentiation(num1, num2))
        elif operation == 'sine':
            print("Result:", sin(num1))
        elif operation == 'cosine':
            print("Result:", cosine(num1))
        elif operation == 'tangent':
            print("Result:", tangent(num1))
        else:
            print("Invalid operation. Please try again.")

# Call the main function to run the calculator
main()

