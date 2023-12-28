# Create a dog class, and a breed which inherits from it

class Dog:
    def __init__ (self, name, breed, color):
        self.name = name 
        self.breed = breed 
        self.color = color

    def adoption(self, availability):
        return f"{self.name} the {self.breed} is {availability} for adoption!!"

my_dog = Dog('Pepper', 'German Sherpherd', 'brown')
another_dog = Dog('Spike', 'Pitbull', 'tan')

print(my_dog.adoption('available'))