# Create a program that shows how quickly a user can type 
# A script will be displayed, user will be prompted to type it, and then the time and accuracy is calculated

import time

def calculate_accuracy(typed_text, original_text):
    match_count = sum(t1 == t2 for t1, t2 in zip(typed_text, original_text))
    accuracy = (match_count / len(original_text)) * 100 
    return accuracy

def typing_speed_test():
    original_text = 'The quick brown fox jumps over the lazy dog.'
    print('Type this sentence as accurately as you can:')
    print(original_text)

    input('Press Enter when you are ready...')

    start_time = time.time()
    typed_text = input("Start typing:\n")
    end_time = time.time()

    time_taken = end_time - start_time
    accuracy = calculate_accuracy(typed_text, original_text)

    print(f'\nTime taken: {time_taken:.2f} seconds')
    print(f['Accuracy: {accuracy:.2f}'])

typing_speed_test()