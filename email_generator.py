# Create a program which combines random words from the NLTK library
# Ask user if they want to incorporate numbers into the email name 

import random
import nltk

# Download the words corpus 
# nltk.download('words')

# Load the words from NLTK
from nltk.corpus import words 
word_list = words.words()

def generate_email():
    '''
    This is the main function in which the email will be generated from. 
    '''
    word_list = words.words()
    random_word = random.choice(word_list)
    number = random.randint(1, 100) # 1 - 100 inclusive
    domain = '@example.com'
    email = f'{random_word}{number}{domain}'

    return email

print(generate_email())