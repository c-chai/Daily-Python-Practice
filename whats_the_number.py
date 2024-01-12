# Create a program where the user guesses the number (which is randomly generated)
# Program will keep asking until user guesses right or enters 'quit'
# Program will keep track of how many attempts were made by user 

import random 

count = 0
def random_num():
    '''
    This function generates a random number between 1-10 inclusive. 
    '''
    return random.randint(1, 10)

def main(): 
    correct_num = random_num()
    count = 0

    while True:
        user_input = input("Please guess the number or type 'q' to quit: ")
        if user_input.lower() == 'q':
            print('Thank you for playing. Bye!')
            break

        try:
            guess = int(user_input)
            count += 1
            if guess == correct_num:
                print(f"Congratulations! You got the right number in {count} tries!")
            else:
                print("Wrong guess, try again.")
        except ValueError:
            print("Please enter a valid number or 'q' to quit: ")

if __name__ == "__main__":
    main()