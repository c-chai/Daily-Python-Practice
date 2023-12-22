# Title: Unexpected Day at the Zoo

def get_input(prompt, input_type=str):
    '''
    This function will catch any numeric inputs and tell the user no numbers. 
    '''    
    while True:
        user_input = input(prompt)
        try:
            if user_input.isnumeric():
                raise ValueError ("Aiyo, no numbers. ")
            return user_input
        except ValueError as e: 
            print(e)

adj1 = get_input("Adjective: ")
adj2 = get_input("Another adjective: ")
silly = get_input("A silly word: ")
animal = get_input("An animal: ")
transporation_type = get_input("A type of transporation: ")
funny_sound = get_input("A funny sound: ")
unusual_color = get_input("An unusual color: ")
food_item = get_input("A ridiculous food item: ")
celebrity = get_input("A famous celebrity (fictional):  ")
strange_object = get_input("A strange object: ")
activity = get_input("A hilarious activity: ")
odd_job = get_input("An oddly specific job: ")

p1 = f"Once upon a time, in the middle of a {adj1} day, a(n) {adj2} {animal} escaped from its enclosure at the zoo. The zookeeper shouted, 'Holy {silly}! We need to catch it!' So, they hopped into their trusty golf cart, making a loud {funny_sound} as they sped away."

p2 = f"As they chased the animal, it suddenly turned a {unusual_color} color, which was absolutely unexpected. 'I\'ve never seen anything like it!' exclaimed the zookeeper, munching on a {food_item} for stress relief."

p3 = f"Just then, {celebrity} appeared out of nowhere, riding a {transporation_type} and wielding a {strange_object}. 'I\'m here to help!' they declared."

p4 = f"Together, they all started {activity}, which, surprisingly, calmed the animal down. It turned out that the animal was just looking for someone to interact with!"

p5 = f"In the end, the zoo hired a {odd_job} to ensure this hilarious situation would never happen again. And everyone lived happily ever after, occasionally turning {unusual_color} for no reason at all." 

print(p1, p2, p3, p4, p5)
