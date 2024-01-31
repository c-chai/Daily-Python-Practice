# Create a program which calculates the area or circumference of a circle 
# Ask user which one they want to calculate, and then ask for a radius 

import math

def area_of_circle(radius):
    return  math.pi * (radius ** 2)

def circumference_of_circle(radius):
    return 2 * math.pi * radius

def main():
    '''
    This is the main function which will ask the user whether they want to calculate the area or circumference of a circle.
    Function will also ask for an input of the radius. 
    '''
    choice = input('Do you want to calculate the area or circumference of a circle? ')
    radius = float(input('Please enter the radius of the circle: '))

    if choice.lower() == 'area':
        print(f'Area of the circle: {area_of_circle(radius)} squared units')
    elif choice.lower() == 'circumference':
        print(f'Circumference of the circle: {circumference_of_circle(radius)} units')
    else:
        print('Invalid input. Please enter \'area\' or \'circumference\'')
    
if __name__ ==  "__main__":
    main()

