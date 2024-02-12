# Create a quiz program about the Amazon rainforest! 
# Store the questions in a dictionary and keep track of the user's score 

def amazon_rainforest_quiz():
    '''
    This function holds a dictionary of questions~
    ''' 
    questions = {
        'What is the largest river in the Amazon rainforest?': 'Amazon',
        'Which country has the largest portion for the Amazon?': 'Brazil',
        'What is the approximate area of the Amazon rainforest?': '5.5 million square kilometers',
        'What type of forest is the Amazon rainforest?': 'Tropical rainforest',
        'What is the most dangerous animal in the Amazon rainforest?': 'Jaguar'
    }

    score = 0
    for question, correct_answer in questions.items():
        user_answer = input(f'{question}: ')
        if user_answer.lower() == correct_answer.lower():
            print('Correct!')
            score += 1
        else:
            print(f'Wrong, the correct answer is {correct_answer}.')

    print(f'Your final score is {score}/{len(questions)}')

amazon_rainforest_quiz()