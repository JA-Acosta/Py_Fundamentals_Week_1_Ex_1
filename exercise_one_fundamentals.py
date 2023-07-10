'''
>>> JAAR
>>> 07/09/2023
>>> Practicing Fundamentals Program 1
>>> Version 1
'''

import math
pi_value = math.pi

'''
>>> Greets the user based on the name they provide then asks the user if they need help with basic mathematics followed by the calculation of both area and perimeter for basic geometric shapes. Afterwards will ask the user for the current temperature to convert it between Fahrenheit or Celsius based on the user input.
'''

def main() :
    # Assume the user inputs their name correctly.
    user_name = input('Enter your name: ')
    print(f'\nHello {user_name}! Are you ready for some basic math!? Lets go!\n')

    # Assume the user inputs two numbers solely separated by a space
    number_list = input('Enter two numbers separated by a space and I\'ll do basic mathematic operations on them: ').split()

    number_list = [float(n) for n in number_list]
    print(f'''
        \t{number_list[0]} + {number_list[1]} = {sum(number_list)}

        \t{number_list[0]} - {number_list[1]} = {number_list[0] - number_list[1]}

        \t{number_list[0]} * {number_list[1]} = {number_list[0] * number_list[1]}

        \t{number_list[0]} / {number_list[1]} = {number_list[0] / number_list[1]}

    ''')

    print('Great Job Team! Now lets work with shapes.\n')

    # Assume the user will only input a, b, c, or d
    selected_shape = input('''Choose a shape from the following list and I will calculate both it's area and perimeter:

        \t\ta) Circle\t\t\tb) Rectangle

        \t\tc) Square\t\t\tc) Triangle

        \tEnter shape: ''')
    print('')
    # Assume the user inputs all dimensions as requested in the following conditional.
    if selected_shape == 'a' :
        radius = float(input('Enter the radius of the circle (m) : '))
        print(f'''
            \tPerimeter: {2 * pi_value * radius:.2f} m

            \tArea: {pi_value * radius ** 2:.2f} m\u00B2

            ''')
    elif selected_shape == 'b' :
        rectangle_dimensions = input('Enter the length and height of the rectangle separated by a space (m): ').split()
        rectangle_dimensions = [float(n) for n in rectangle_dimensions]
        print(f'''
            \tPerimeter: {2 * sum(rectangle_dimensions):.2f} m

            \tArea: {rectangle_dimensions[0] * rectangle_dimensions[1]:.2f} m\u00B2

            ''')
    elif selected_shape == 'c':
        square_side = float(input('Enter the length of one side of the square (m) : '))
        print(f'''
            \tPerimeter: {4 * square_side:.2f} m

            \tArea: {square_side ** 2:.2f} m\u00B2

            ''')
    else :
        triangle_dimension = input('Enter each side of the triangle separated by a space starting with the base (m) : ').split()
        triangle_height = float(input('Enter the height of the triangle: '))
        triangle_dimension = [float(n) for n in triangle_dimension]
        print(f'''
            \tPerimeter: {sum(triangle_dimension):.2f} m

            \tArea: {.5 * triangle_dimension[0] * triangle_height:.2f} m\u00B2

            ''')

    print('How insightful! Lets finish up by looking at the weather today in both \u00B0C and \u00B0F.')

    # Assume the user will input either a or b
    temperature_scale = input('''Do you want to input the weather in Celsius or Ferenheigh?

        \t\ta) Celsius\t\t\tb) Ferenheigh

        \tEnter temperature scale: ''')

    temperature = float(input('\nWhat is the current temperature?: '))
    print()
    if temperature_scale == 'a' :
        print(f'\tThe temperature in \u00B0F is {(temperature * 9 / 5) + 32:.2f}')
    else :
        print(f'\tThe temperature in \u00B0C is {(temperature - 32) * 5 / 9:.2f}')

    print('Done!')

if __name__ == '__main__' :
    main()