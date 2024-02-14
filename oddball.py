# Create a program that takes a string as input 
# For each character in the string, the function should convert it into its corresponding ASCII art representation 
# Print the ASCII art for the entire input string 

import pyfiglet

def ascii_art_generator(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

user_input = input('Enter a text to convert into ASCII art: ')
ascii_art_generator(user_input)