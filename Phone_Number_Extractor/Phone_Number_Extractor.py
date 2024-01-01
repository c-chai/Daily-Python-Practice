# Create a program which extracts phone numbers from a text file
# The output will say extraction complete and display the numbers in a new text file 
# Each number on a new line 

import re 

def extract_phone_numbers(input_file, output_file):
    # This regex function matches phone numbers in VARIOUS formats
    phone_pattern = re.compile(r'\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}')

    extracted_numbers = []

    with open(input_file, 'r') as file:
        for line in file:
            matches = phone_pattern.findall(line)
            extracted_numbers.extend(matches)
            
    with open(output_file, 'w') as file:
        for number in extracted_numbers:
            file.write(number + '\n')

    return len(extracted_numbers)

input_file = 'Phone_Numbers.txt'
output_file = 'Extracted.txt'

num_extracted = extract_phone_numbers(input_file, output_file)
print(f"Extraction complete. {num_extracted} phone numbers found.")