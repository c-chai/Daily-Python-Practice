# Create a program which counts the number of words in a text file 

def count_total_words(file_path):
    total_words = 0

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            total_words += len(words)

    return total_words

# Example usage
file_path = '/count_words_in_text/words_to_count.txt' # Full path not disclosed 
total_word_count = count_total_words(file_path)

print(f"Total number of words in the file: {total_word_count}")
