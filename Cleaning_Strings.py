# Remove special symbols / punctuation / numbers / spaces from a string
# Also format it correctly with title() 
import re # Very useful here 
import string

sentence = "#(*1) whY aRe YoU THE $ w@ay ^ thaT y-ou ARE? "
# Removes all characteres except alphabets and spaces
cleaned_sentence = re.sub(r'[^A-Za-z ]+', '', sentence)
# Removes any trailing and leading spaces, and then capitalizes the first letter of sentence
formatted_sentence = cleaned_sentence.strip().capitalize()
print(formatted_sentence)
