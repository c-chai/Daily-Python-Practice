# Write a program which asks the user to input an English word
# This word will be transformed into Pig Latin and printed out 

def to_pig_latin(word):
    vowels = 'aeiou'

    # Check if the first word is a vowel
    if word[0].lower() in vowels:
        return word + 'way'
    
    else:
        # Find the index of the first vowel in the word 
        for index, letter in enumerate(word):
            if letter.lower() in vowels:
                return word[index:] + word[:index] + 'ay'
        # In case there is no vowel, return the original word
        return word
    
word = input('Enter an English word: ')
pig_latin_word = to_pig_latin(word)
print(f'Pig Latin: {pig_latin_word}')
