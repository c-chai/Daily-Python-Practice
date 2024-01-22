# Create a program where it flips the string sentence the user inputs 

def flip_it(s):
    words = s.split()
    words_reversed = words[::-1]

    flipped_sentence = ' '.join(words_reversed)

    return flipped_sentence

user_input = input("Enter a string to flip: ")
result = flip_it(user_input)
print(f'Flipped sentence: {result}')