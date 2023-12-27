# A dictionary that stores questions and answers 
# A variable that keeps track of player's score
# Loop through the dict using key value pairs 
# Display each question to the user and allow them to answer 
# Tell them if they are right or wrong 
# Show the final result when the quiz is done 

quiz = {
    'question1': {
        'question': 'What is the capital of Japan?',
        'answer': 'Tokyo'
    },
    'question2':{
        'question': 'What is the capital of Germany?',
        'answer': 'Berlin'
    },
    'question3': {
        'question': 'What is the capital of Italy?',
        'answer': 'Rome'
    },
    'question4': {
        'question': 'What is the capital of Australia?',
        'answer': 'Canberra'
    },
    'question5': {
        'question': 'What is the capital of Finland?',
        'answer': 'Helsinki'
    }
}

score = 0
for key, value in quiz.items():
    print(value['question'])
    answer = input('Answer? ')
    
    if answer.lower() == value['answer'].lower():
        print('Correct')
        score += 1
        print(f"Your score is {score}")
    else: 
        print('Wrong')
    
        print(f'The answer is {value['answer']}')

print(f'Final score: {score}')