# Create a program that reverses the words in a string

def reverse_string(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Reverse the order of words
    reversed_words = words[::-1]

    # Join the reversed words back into a sentence
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

user_sentence = input('Enter a sentence: ')

# Reverse the sentence
result = reverse_string(user_sentence)

print(f'Reversed sentence: {result}')