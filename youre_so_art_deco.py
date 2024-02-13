# Write a program which involves using a decorator

def art_decorater(func):
    def wrapper():
        print('You\'re so art deco, out on the floor')
        func()
        print('Shining like gunmetal, cold and unsure')
    return wrapper

@art_decorater
def next_line():
    print('This is a song')

next_line()