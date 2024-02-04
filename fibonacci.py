# Write a program that asks the user how many Fibonacci numbers to generate and then generates them 

def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    for _ in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

#Ask the user for input 
try: 
    num_terms = int(input("How any Fibonacci numbers would you like to generate? "))
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        # This generates and prints the Fibonacci sequence
        fibonacci_numbers = generate_fibonacci(num_terms)
        print("Fibonacci sequence:", fibonacci_numbers)
except ValueError:
    print("Invalid input. Please enter a positive integer.")